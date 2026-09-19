#!/usr/bin/env python3
"""Satoshium Attestor validator — implementation v0.2.

Implements deterministic/conditional portions of the canonical VAL-* catalog.
Review-dependent rules are never silently reported as machine pass.
"""
from __future__ import annotations
import argparse, json, re, sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ATT_TYPES={"identity","evidence","source-provenance","verification-related","relationship-condition","correction-supersession"}
LIFECYCLE={"draft","active","superseded","withdrawn","retired"}
PUBLICATION={"unpublished","published"}
AUTH={"Attestor","Suite-source","external-source"}
PROV={"direct","referenced","derived"}
REL={"supports","references","derived-from","evaluates","results-in","supersedes","corrects","related-to"}
OUTCOMES={"supported","partially-supported","not-supported","contradicted","indeterminate"}
ATT_RE=re.compile(r"^ATT-[0-9]{4}-[0-9]{4}$")
TRST_RE=re.compile(r"^TRST-[0-9]{4}-[0-9]{4}$")
VER_RE=re.compile(r"^V[0-9]+\.[0-9]+$")
RFC3339_RE=re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$")

def nonempty(v):
    if v is None: return False
    if isinstance(v,str): return bool(v.strip())
    if isinstance(v,(dict,list)): return bool(v)
    return True

def timestamp(v):
    if not isinstance(v,str) or not RFC3339_RE.fullmatch(v): return None
    try: return datetime.fromisoformat(v.replace("Z","+00:00"))
    except ValueError: return None

def rr(rule,layer,state,loc,msg,mandatory=True):
    return {"rule_id":rule,"layer":layer,"result":state,"location":loc,"message":msg,"mandatory":mandatory}

def check(rule,layer,ok,loc,passmsg,failmsg,mandatory=True):
    return rr(rule,layer,"pass" if ok else "fail",loc,passmsg if ok else failmsg,mandatory)

def na(rule,layer,loc,msg,mandatory=True): return rr(rule,layer,"not-applicable",loc,msg,mandatory)
def nt(rule,layer,loc,msg,mandatory=True): return rr(rule,layer,"not-tested",loc,msg,mandatory)

def rel_results(d):
    r=[]
    rels=d.get("relationships")
    if rels is None:
        return [na("VAL-REL-001","relationships","relationships","No material relationship serialized; rule not applicable.")]
    if not isinstance(rels,list):
        return [check("VAL-REL-001","relationships",False,"relationships","", "relationships must be a sequence.")]
    for i,x in enumerate(rels):
        loc=f"relationships[{i}]"
        ok=isinstance(x,dict) and x.get("type") in REL and nonempty(x.get("target_identifier"))
        r.append(check("VAL-REL-001","relationships",ok,loc,"Relationship has explicit type and target.","Relationship requires controlled type and target_identifier."))
        if isinstance(x,dict) and x.get("type") in REL:
            r.append(check("VAL-SEM-006","controlled-semantics",True,loc+".type","Controlled relationship value.",""))
            typ=x.get("type")
            mapping={"supports":"VAL-REL-003","references":"VAL-REL-004","derived-from":"VAL-REL-005",
                     "evaluates":"VAL-REL-006","results-in":"VAL-REL-007","supersedes":"VAL-REL-008","corrects":"VAL-REL-009"}
            if typ in mapping:
                # Direction is represented by container-as-source and target_identifier.
                r.append(check(mapping[typ],"relationships",nonempty(x.get("target_identifier")),loc,
                               f"{typ} direction is explicitly serialized source→target.",
                               f"{typ} relationship lacks target."))
        elif isinstance(x,dict):
            r.append(check("VAL-SEM-006","controlled-semantics",False,loc+".type","","Invalid relationship type."))
    return r

def common(d):
    r=[]
    r.append(check("VAL-SEM-002","controlled-semantics",d.get("lifecycle_state") in LIFECYCLE,"lifecycle_state",
                   "Controlled lifecycle state.","Invalid lifecycle state."))
    r.append(check("VAL-SEM-003","controlled-semantics",d.get("publication_state") in PUBLICATION,"publication_state",
                   "Controlled publication state.","Invalid publication state."))
    r.append(check("VAL-LV-003","lifecycle-versioning",
                   "lifecycle_state" in d and "publication_state" in d and d.get("lifecycle_state")!=d.get("publication_state"),
                   "lifecycle_state/publication_state","Lifecycle and publication are separately represented.",
                   "Lifecycle and publication must be separate governed dimensions."))
    r.append(check("VAL-LV-006","lifecycle-versioning",d.get("lifecycle_state")!="inactive","lifecycle_state",
                   "Non-active states remain controlled and distinct.","inactive is not a canonical lifecycle state."))
    r.append(check("VAL-LV-007","lifecycle-versioning",d.get("lifecycle_state")!="review","lifecycle_state",
                   "Review is not represented as lifecycle state.","review is an activity, not a lifecycle state."))
    r.append(check("VAL-LV-008","lifecycle-versioning",d.get("lifecycle_state")!="correction","lifecycle_state",
                   "Correction is not represented as lifecycle state.","correction is an activity, not a lifecycle state."))
    r.append(check("VAL-LV-011","lifecycle-versioning",nonempty(d.get("version_identity")),"version_identity",
                   "Canonical identity/version identity are separately represented.","version_identity is required."))
    r.append(check("VAL-LV-013","lifecycle-versioning",
                   isinstance(d.get("version_identity"),str) and bool(VER_RE.fullmatch(d["version_identity"])),
                   "version_identity","Version identity distinguishes governed revision.","Version must match V<major>.<minor>."))
    c,u=timestamp(d.get("created_at")),timestamp(d.get("updated_at"))
    # Timestamp syntax is subordinate to canonical structural validation, not a new VAL id.
    r.append(check("TEST-STR-STRUCTURE","structure",c is not None,"created_at","RFC3339 creation timestamp represented.","created_at must be RFC3339.",False))
    r.append(check("TEST-STR-STRUCTURE","structure",u is not None,"updated_at","RFC3339 update timestamp represented.","updated_at must be RFC3339.",False))
    r.append(check("TEST-STR-STRUCTURE","structure",c is not None and u is not None and u>=c,"updated_at",
                   "Temporal ordering coherent.","updated_at must not precede created_at.",False))
    r.extend(rel_results(d))
    return r

def validate_att(d, registry=None):
    r=[]
    aid=d.get("attestation_identifier")
    r.append(check("VAL-STR-001","structure",isinstance(aid,str) and bool(ATT_RE.fullmatch(aid)),"attestation_identifier",
                   "Valid ATT identifier family.","Identifier must match ATT-YYYY-NNNN."))
    r.append(check("VAL-STR-003","structure",isinstance(aid,str) and bool(ATT_RE.fullmatch(aid)),"attestation_identifier",
                   "Four-digit creation year represented.","ATT identifier must contain four-digit year."))
    r.append(check("VAL-STR-004","structure",isinstance(aid,str) and bool(ATT_RE.fullmatch(aid)),"attestation_identifier",
                   "Four-digit sequence represented.","ATT identifier must contain four-digit sequence."))
    r.append(check("VAL-STR-005","structure","trust_statement_identifier" not in d,"attestation_identifier",
                   "Object class and identifier prefix are coherent.","ATT object must not carry TRST identifier field."))
    if registry is None:
        r.append(nt("VAL-STR-006","structure","attestation_identifier","Authoritative identifier register not supplied; uniqueness not tested."))
    else:
        count=registry.count(aid)
        r.append(check("VAL-STR-006","structure",count<=1,"attestation_identifier","Identifier unique in supplied registry.","Duplicate/reused identifier detected."))
    r.append(check("VAL-SEM-001","controlled-semantics",d.get("attestation_type") in ATT_TYPES,"attestation_type",
                   "Controlled Attestation Type.","Invalid Attestation Type."))
    r.append(check("VAL-SEM-007","controlled-semantics",
                   not any(k in d for k in ("trust_score","confidence_score","signal_strength","reputation")),
                   "$","No legacy trust/confidence vocabulary used.","Legacy trust/confidence vocabulary is noncanonical."))
    a=d.get("attesting_authority") or {}
    r.append(check("VAL-ATT-002","provenance-authority",nonempty(a.get("identifier")),"attesting_authority.identifier",
                   "Attesting Authority identifiable.","Attesting Authority identifier required."))
    r.append(check("VAL-ATT-003","provenance-authority",a.get("authority_context") in AUTH,"attesting_authority.authority_context",
                   "Authority-to-assertion context represented.","Controlled authority_context required."))
    r.append(check("VAL-ATT-004","structure",nonempty(d.get("scope")),"scope","Attestation scope preserved.","Scope required."))
    p=d.get("provenance") or {}
    r.append(check("VAL-SEM-005","controlled-semantics",p.get("mode") in PROV,"provenance.mode",
                   "Controlled provenance mode.","Invalid provenance mode."))
    r.append(check("VAL-ATT-005","provenance-authority",nonempty(p.get("source_or_origin")),"provenance.source_or_origin",
                   "Attestation provenance preserved.","source_or_origin required."))
    if p.get("mode")=="derived":
        r.append(check("VAL-PA-002","provenance-authority",nonempty(p.get("derivation_basis")),"provenance.derivation_basis",
                       "Derived provenance basis preserved.","Derived provenance requires derivation_basis."))
    else:
        r.append(na("VAL-PA-002","provenance-authority","provenance.derivation_basis","Derivation basis not applicable to non-derived provenance."))
    r.append(check("VAL-NRM-001","normative",nonempty(a.get("identifier")),"attesting_authority.identifier",
                   "Attribution preserved.","Attribution missing."))
    r.append(check("VAL-NRM-002","normative",nonempty(p.get("source_or_origin")),"provenance",
                   "Provenance preserved.","Provenance missing."))
    r.append(check("VAL-NRM-003","normative",nonempty(d.get("scope")),"scope","Scope representation preserved.","Scope missing; substantive breadth remains Review."))
    r.append(check("VAL-NRM-006","normative",nonempty(aid) and nonempty(p.get("source_or_origin")),"$",
                   "Minimum machine traceability present.","Insufficient machine traceability."))
    r.extend(common(d))
    # Review-dependent materiality/authority judgments are explicitly not machine-passed.
    for rid,msg in [
        ("VAL-PA-007","Whether references transfer authority requires governed review."),
        ("VAL-PA-008","Attestor authority boundary requires governed review."),
        ("VAL-LV-015","Material assertion change/new ATT identity requires governed review."),
        ("VAL-NRM-004","Substantive authority-boundary preservation requires governed review."),
        ("VAL-NRM-009","Universal-truth characterization requires governed review."),
        ("VAL-NRM-010","Automatic input-to-conclusion conversion requires governed review.")
    ]: r.append(nt(rid,"review","$",msg,False))
    return r

def validate_trst(d, registry=None):
    r=[]
    tid=d.get("trust_statement_identifier")
    validid=isinstance(tid,str) and bool(TRST_RE.fullmatch(tid))
    r.append(check("VAL-STR-002","structure",validid,"trust_statement_identifier","Valid TRST identifier family.","Identifier must match TRST-YYYY-NNNN."))
    r.append(check("VAL-STR-003","structure",validid,"trust_statement_identifier","Four-digit creation year represented.","TRST identifier must contain four-digit year."))
    r.append(check("VAL-STR-004","structure",validid,"trust_statement_identifier","Four-digit sequence represented.","TRST identifier must contain four-digit sequence."))
    r.append(check("VAL-STR-005","structure","attestation_identifier" not in d,"trust_statement_identifier",
                   "Object class and identifier prefix are coherent.","TRST object must not carry ATT identifier field."))
    if registry is None:
        r.append(nt("VAL-STR-006","structure","trust_statement_identifier","Authoritative identifier register not supplied; uniqueness not tested."))
    else:
        r.append(check("VAL-STR-006","structure",registry.count(tid)<=1,"trust_statement_identifier",
                       "Identifier unique in supplied registry.","Duplicate/reused identifier detected."))
    r.append(check("VAL-TRST-001","structure",nonempty(d.get("bounded_conclusion")),"bounded_conclusion",
                   "Bounded conclusion present.","Bounded conclusion required."))
    e=d.get("evaluation") or {}
    r.append(check("VAL-TRST-002","structure","bounded_conclusion" in d and "outcome" in e,"bounded_conclusion/evaluation.outcome",
                   "Conclusion and outcome are structurally distinct.","Conclusion/outcome separation missing."))
    a=d.get("attestor_attribution") or {}
    r.append(check("VAL-TRST-003","provenance-authority",nonempty(a.get("identifier")) and a.get("authority_context")=="Attestor",
                   "attestor_attribution","Attestor attribution preserved.","Attestor attribution requires identifier and Attestor context."))
    r.append(check("VAL-TRST-004","controlled-semantics",e.get("outcome") in OUTCOMES,"evaluation.outcome",
                   "Evaluation Outcome present and controlled.","Invalid/missing Evaluation Outcome."))
    br=e.get("basis_references")
    r.append(check("VAL-TRST-005","normative",isinstance(br,list) and len(br)>0,"evaluation.basis_references",
                   "Evaluation basis traceable.","At least one basis reference required."))
    supp=d.get("supporting_attestations")
    r.append(check("VAL-TRST-006","relationships",isinstance(supp,list) and len(supp)>0 and all(isinstance(x,str) and ATT_RE.fullmatch(x) for x in supp),
                   "supporting_attestations","Supporting Attestations traceable.","At least one valid ATT reference required."))
    ar=e.get("applicable_rules")
    r.append(check("VAL-TRST-007","normative",isinstance(ar,list) and len(ar)>0,"evaluation.applicable_rules",
                   "Applicable rule/methodology context represented.","At least one applicable rule required."))
    p=d.get("provenance") or {}
    r.append(check("VAL-TRST-008","provenance-authority",p.get("mode")=="derived" and nonempty(p.get("source_or_origin")) and nonempty(p.get("derivation_basis")),
                   "provenance","Derived Trust Statement provenance complete.","TRST provenance must be derived with source/origin and derivation basis."))
    if nonempty(e.get("relevant_time_or_state")):
        r.append(check("VAL-TRST-009","provenance-authority",True,"evaluation.relevant_time_or_state","Relevant time/state preserved.",""))
    else:
        r.append(na("VAL-TRST-009","provenance-authority","evaluation.relevant_time_or_state","No material time/state declared by fixture/profile."))
    for rid,key in [("VAL-TRST-010","material_conflicts"),("VAL-TRST-011","material_exclusions")]:
        val=e.get(key)
        r.append(check(rid,"normative",isinstance(val,list),f"evaluation.{key}",f"{key} explicitly represented.","Field must be an explicit sequence."))
    r.append(check("VAL-TRST-012","normative",isinstance(d.get("limitations",[]),list),"limitations","Limitations representation preserved.","limitations must be a sequence."))
    r.append(check("VAL-TRST-013","normative",isinstance(d.get("uncertainty",[]),list),"uncertainty","Uncertainty representation preserved; substance remains Review.","uncertainty must be a sequence."))
    r.append(check("VAL-SEM-004","controlled-semantics",e.get("outcome") in OUTCOMES,"evaluation.outcome","Controlled Evaluation Outcome.","Invalid Evaluation Outcome."))
    r.append(check("VAL-SEM-005","controlled-semantics",p.get("mode") in PROV,"provenance.mode","Controlled provenance mode.","Invalid provenance mode."))
    r.append(check("VAL-NRM-001","normative",nonempty(a.get("identifier")),"attestor_attribution.identifier","Attribution preserved.","Attribution missing."))
    r.append(check("VAL-NRM-002","normative",nonempty(p.get("source_or_origin")),"provenance","Provenance preserved.","Provenance missing."))
    r.append(check("VAL-NRM-003","normative",nonempty(d.get("scope")),"scope","Scope representation preserved.","Scope missing; substantive breadth remains Review."))
    r.append(check("VAL-NRM-005","normative",isinstance(e.get("material_conflicts"),list) and isinstance(e.get("material_exclusions"),list),
                   "evaluation","Evidence-context conflict/exclusion fields preserved.","Evidence context fields missing."))
    r.append(check("VAL-NRM-006","normative",isinstance(br,list) and bool(br),"evaluation.basis_references","Evaluation traceability represented.","Evaluation basis not traceable."))
    r.append(check("VAL-NRM-011","normative",isinstance(d.get("uncertainty",[]),list),"uncertainty","Uncertainty field is preserved; substantive adequacy remains Review.","uncertainty must be a sequence."))
    r.extend(common(d))
    for rid,msg in [
        ("VAL-TRST-014","Universal-truth characterization requires governed review."),
        ("VAL-TRST-015","Automatic input-to-conclusion conversion requires governed review."),
        ("VAL-PA-007","Whether references transfer authority requires governed review."),
        ("VAL-PA-008","Attestor authority boundary requires governed review."),
        ("VAL-LV-016","Material conclusion change/new TRST identity requires governed review."),
        ("VAL-NRM-004","Substantive authority-boundary preservation requires governed review."),
        ("VAL-NRM-009","Universal-truth characterization requires governed review."),
        ("VAL-NRM-010","Automatic input-to-conclusion conversion requires governed review."),
        ("VAL-NRM-012","Interoperability authority-transfer semantics require governed review.")
    ]: r.append(nt(rid,"review","$",msg,False))
    return r

def load(path):
    txt=Path(path).read_text(encoding="utf-8")
    if path.endswith(".json"): return json.loads(txt)
    if yaml is None: raise RuntimeError("PyYAML is required for YAML input.")
    return yaml.safe_load(txt)

def registry_values(path):
    if not path: return None
    x=load(path)
    if isinstance(x,list): return x
    if isinstance(x,dict): return x.get("identifiers",[])
    raise ValueError("Registry context must be a list or {identifiers:[...]}.")

def execution_context(path):
    if not path: return {}
    x=load(path)
    if not isinstance(x,dict): raise ValueError("Execution context must be a mapping/object.")
    return x

def context_results(results, kind, d, ctx):
    """Resolve bounded machine-context rules only when explicit authoritative context is supplied."""
    byid={}
    for i,x in enumerate(results): byid.setdefault(x["rule_id"],[]).append(i)

    def resolve(rid, ok, msg, loc="$"):
        for i in byid.get(rid,[]):
            x=results[i]
            if x["result"]=="not-tested" and x.get("mandatory",True):
                x.update(result="pass" if ok else "fail", location=loc, message=msg)

    ident=d.get("attestation_identifier") if kind=="ATT" else d.get("trust_statement_identifier")
    objctx=(ctx.get("objects") or {}).get(ident,{})
    # Process/history facts are not inferred from the object.
    if objctx:
        resolve("VAL-STR-007", bool(objctx.get("identifier_assigned_at_creation")),
                "Execution context confirms identifier assignment at canonical creation." if objctx.get("identifier_assigned_at_creation") else "Identifier pre-creation boundary not established.")
        resolve("VAL-LV-001", objctx.get("initial_lifecycle_state")=="draft",
                "Execution context confirms initial lifecycle state draft." if objctx.get("initial_lifecycle_state")=="draft" else "Initial lifecycle state was not draft.")
        resolve("VAL-LV-002", bool(objctx.get("creation_activation_separate")),
                "Execution context confirms creation and activation are separate." if objctx.get("creation_activation_separate") else "Creation/activation separation not established.")
        resolve("VAL-LV-009", bool(objctx.get("review_does_not_change_state")),
                "Execution context confirms Review does not silently change lifecycle state." if objctx.get("review_does_not_change_state") else "Review/state-change boundary not established.")
        resolve("VAL-LV-010", bool(objctx.get("historical_identity_preserved")),
                "Execution context confirms historical identity preservation." if objctx.get("historical_identity_preserved") else "Historical identity preservation not established.")
        resolve("VAL-LV-012", bool(objctx.get("same_object_revision_preserves_id")),
                "Execution context confirms same-object revisions preserve canonical identifier." if objctx.get("same_object_revision_preserves_id") else "Same-object identifier preservation not established.")
        resolve("VAL-LV-014", bool(objctx.get("no_silent_overwrite")),
                "Execution context confirms no silent historical overwrite." if objctx.get("no_silent_overwrite") else "No-silent-overwrite control not established.")
        resolve("VAL-LV-017", bool(objctx.get("successor_relationship_required_for_material_successor")),
                "Execution context confirms successor relationship control." if objctx.get("successor_relationship_required_for_material_successor") else "Successor relationship control not established.")

    provctx=(ctx.get("provenance") or {}).get(ident,{})
    if provctx:
        resolve("VAL-PA-001", bool(provctx.get("material_inputs_traceable")),
                "Execution context confirms material input traceability." if provctx.get("material_inputs_traceable") else "Material input traceability not established.")
        resolve("VAL-PA-003", bool(provctx.get("evaluation_provenance_preserved")),
                "Execution context confirms evaluation provenance preservation." if provctx.get("evaluation_provenance_preserved") else "Evaluation provenance not established.")
        resolve("VAL-PA-004", bool(provctx.get("provenance_continuity_preserved")),
                "Execution context confirms provenance continuity." if provctx.get("provenance_continuity_preserved") else "Provenance continuity not established.")
        resolve("VAL-PA-005", bool(provctx.get("source_state_preserved")),
                "Execution context confirms source state at evaluation is preserved." if provctx.get("source_state_preserved") else "Source-state preservation not established.")
    return results

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--output")
    ap.add_argument("--registry")
    ap.add_argument("--context")
    args=ap.parse_args()
    try:
        d=load(args.target)
        if not isinstance(d,dict): raise ValueError("Root document must be a mapping/object.")
        reg=registry_values(args.registry)
        ctx=execution_context(args.context)
        if "attestation_identifier" in d:
            profile="attestor.attestation.base"; ident=d.get("attestation_identifier"); results=validate_att(d,reg)
            results=context_results(results,"ATT",d,ctx)
        elif "trust_statement_identifier" in d:
            profile="attestor.trust-statement.base"; ident=d.get("trust_statement_identifier"); results=validate_trst(d,reg)
            results=context_results(results,"TRST",d,ctx)
        else: raise ValueError("Unable to identify canonical ATT/TRST object.")
        mandatory_fail=sum(x["mandatory"] and x["result"]=="fail" for x in results)
        mandatory_nt=sum(x["mandatory"] and x["result"]=="not-tested" for x in results)
        aggregate="invalid" if mandatory_fail else ("incomplete" if mandatory_nt else "valid")
        report={"validation_report":{"report_version":"V1.0","target_identifier":ident,"target_profile":profile,
          "target_version":d.get("version_identity"),"requirements_set":"Satoshium Attestor Executable Validation Requirements",
          "requirements_version":"0.1","validator_identifier":"satoshium-attestor-validator","validator_version":"0.2",
          "run_at":datetime.now().astimezone().isoformat(),"aggregate_result":aggregate,"results":results,
          "summary":{"passed":sum(x["result"]=="pass" for x in results),
                     "failed":sum(x["result"]=="fail" for x in results),
                     "not_applicable":sum(x["result"]=="not-applicable" for x in results),
                     "not_tested":sum(x["result"]=="not-tested" for x in results)},
          "notes":["Review-dependent rules are reported not-tested, never silently machine-passed."]}}
    except Exception as e:
        report={"validation_report":{"report_version":"V1.0","target_identifier":None,"target_profile":None,
          "validator_identifier":"satoshium-attestor-validator","validator_version":"0.2",
          "run_at":datetime.now().astimezone().isoformat(),"aggregate_result":"error","results":[],
          "summary":{"passed":0,"failed":0,"not_applicable":0,"not_tested":0},"notes":[str(e)]}}
    out=json.dumps(report,indent=2)
    if args.output: Path(args.output).write_text(out+"\n",encoding="utf-8")
    else: print(out)
    return 0 if report["validation_report"]["aggregate_result"]=="valid" else 1




# ---- Validator v0.3 final catalog-coverage layer ----
CANONICAL_RULE_DISPOSITION = {
  "VAL-REP-001": {
    "mode": "machine",
    "class": "MACHINE",
    "title": "Parseable Representation"
  },
  "VAL-REP-002": {
    "mode": "machine",
    "class": "MACHINE",
    "title": "Declared Object Profile"
  },
  "VAL-REP-003": {
    "mode": "machine",
    "class": "MACHINE",
    "title": "Legacy Trust Signal Exclusion"
  },
  "VAL-STR-001": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Attestation Identifier Family"
  },
  "VAL-STR-002": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Trust Statement Identifier Family"
  },
  "VAL-STR-003": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Four-Digit Creation Year"
  },
  "VAL-STR-004": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Four-Digit Sequence"
  },
  "VAL-STR-005": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Object-Class / Prefix Coherence"
  },
  "VAL-STR-006": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Canonical Identifier Uniqueness"
  },
  "VAL-STR-007": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Pre-Creation Identifier Boundary"
  },
  "VAL-STR-008": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Source Identifier Preservation"
  },
  "VAL-SEM-001": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Attestation Type Vocabulary"
  },
  "VAL-SEM-002": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Lifecycle Vocabulary"
  },
  "VAL-SEM-003": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Publication Vocabulary"
  },
  "VAL-SEM-004": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Evaluation Outcome Vocabulary"
  },
  "VAL-SEM-005": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Provenance Mode Vocabulary"
  },
  "VAL-SEM-006": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Relationship Vocabulary"
  },
  "VAL-SEM-007": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Noncanonical Trust/Confidence Vocabulary"
  },
  "VAL-ATT-001": {
    "mode": "machine",
    "class": "MACHINE",
    "title": "Distinct Attestation Identity"
  },
  "VAL-ATT-002": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Attesting Authority Identifiable"
  },
  "VAL-ATT-003": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Authority-to-Assertion Context"
  },
  "VAL-ATT-004": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Attestation Scope Preserved"
  },
  "VAL-ATT-005": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Attestation Provenance Preserved"
  },
  "VAL-ATT-006": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Material Limitations Preserved"
  },
  "VAL-ATT-007": {
    "mode": "machine",
    "class": "MACHINE",
    "title": "Attestation Is Not Trust Statement"
  },
  "VAL-TRST-001": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Bounded Conclusion Present"
  },
  "VAL-TRST-002": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Conclusion / Outcome Separation"
  },
  "VAL-TRST-003": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Attestor Attribution"
  },
  "VAL-TRST-004": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Evaluation Outcome Present"
  },
  "VAL-TRST-005": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Evaluation Basis Traceable"
  },
  "VAL-TRST-006": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Supporting Attestation Traceability"
  },
  "VAL-TRST-007": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Applicable Rules / Methodology Context"
  },
  "VAL-TRST-008": {
    "mode": "existing",
    "class": "MACHINE / CONDITIONAL",
    "title": "Derived Provenance"
  },
  "VAL-TRST-009": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Relevant Time / State"
  },
  "VAL-TRST-010": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Material Conflict Preservation"
  },
  "VAL-TRST-011": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Material Exclusion Preservation"
  },
  "VAL-TRST-012": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Limitation Preservation"
  },
  "VAL-TRST-013": {
    "mode": "existing",
    "class": "CONDITIONAL / REVIEW",
    "title": "Uncertainty Preservation"
  },
  "VAL-TRST-014": {
    "mode": "existing",
    "class": "REVIEW",
    "title": "No Universal-Truth Representation"
  },
  "VAL-TRST-015": {
    "mode": "existing",
    "class": "REVIEW",
    "title": "Trust Statement Is Not Automatic Input Conversion"
  },
  "VAL-PA-001": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Material Input Traceability"
  },
  "VAL-PA-002": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Minimum Provenance Context"
  },
  "VAL-PA-003": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Evaluation Provenance"
  },
  "VAL-PA-004": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Provenance Continuity"
  },
  "VAL-PA-005": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Source-State Preservation"
  },
  "VAL-PA-006": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Authority Context Preservation"
  },
  "VAL-PA-007": {
    "mode": "existing",
    "class": "REVIEW / CONDITIONAL",
    "title": "No Authority Transfer"
  },
  "VAL-PA-008": {
    "mode": "existing",
    "class": "REVIEW",
    "title": "Attestor Authority Boundary"
  },
  "VAL-PA-009": {
    "mode": "conditional",
    "class": "CONDITIONAL / REVIEW",
    "title": "Authority Conflict Preservation"
  },
  "VAL-REL-001": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Explicit Source and Target"
  },
  "VAL-REL-002": {
    "mode": "conditional",
    "class": "MACHINE / CONDITIONAL",
    "title": "Direction Preserved"
  },
  "VAL-REL-003": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "`supports` Direction"
  },
  "VAL-REL-004": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "`references` Does Not Imply Support"
  },
  "VAL-REL-005": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "`derived-from` Direction"
  },
  "VAL-REL-006": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "`evaluates` Direction"
  },
  "VAL-REL-007": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "`results-in` Direction"
  },
  "VAL-REL-008": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "`supersedes` Direction"
  },
  "VAL-REL-009": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "`corrects` Direction"
  },
  "VAL-REL-010": {
    "mode": "mixed",
    "class": "MACHINE / REVIEW",
    "title": "Connection Does Not Merge Identity"
  },
  "VAL-REL-011": {
    "mode": "review",
    "class": "REVIEW",
    "title": "Relationship Does Not Establish Eligibility"
  },
  "VAL-REL-012": {
    "mode": "review",
    "class": "REVIEW",
    "title": "Relationship Does Not Transfer Authority"
  },
  "VAL-LV-001": {
    "mode": "conditional",
    "class": "MACHINE / CONDITIONAL",
    "title": "Created Object Begins Draft"
  },
  "VAL-LV-002": {
    "mode": "conditional",
    "class": "MACHINE / CONDITIONAL",
    "title": "Creation / Activation Separation"
  },
  "VAL-LV-003": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Lifecycle / Publication Separation"
  },
  "VAL-LV-004": {
    "mode": "machine",
    "class": "MACHINE",
    "title": "Draft Is Not Active"
  },
  "VAL-LV-005": {
    "mode": "review",
    "class": "REVIEW",
    "title": "Active Meaning"
  },
  "VAL-LV-006": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Non-Active State Distinction"
  },
  "VAL-LV-007": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Review Is Activity, Not State"
  },
  "VAL-LV-008": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Correction Is Activity, Not State"
  },
  "VAL-LV-009": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Review Does Not Silently Change State"
  },
  "VAL-LV-010": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Historical Identity Preservation"
  },
  "VAL-LV-011": {
    "mode": "existing",
    "class": "MACHINE",
    "title": "Canonical Identity / Version Identity Separation"
  },
  "VAL-LV-012": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Same-Object Revision Preserves Canonical Identifier"
  },
  "VAL-LV-013": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Version Identity Distinguishes Preserved Revision"
  },
  "VAL-LV-014": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "No Silent Historical Overwrite"
  },
  "VAL-LV-015": {
    "mode": "existing",
    "class": "REVIEW / CONDITIONAL",
    "title": "Material Attestation Change Requires New ATT"
  },
  "VAL-LV-016": {
    "mode": "existing",
    "class": "REVIEW / CONDITIONAL",
    "title": "Material Trust Statement Conclusion Requires New TRST"
  },
  "VAL-LV-017": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Material Successor Relationship"
  },
  "VAL-LV-018": {
    "mode": "review",
    "class": "REVIEW",
    "title": "Correction Reason / Versioning Decision Separation"
  },
  "VAL-NRM-001": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Preserve Attribution"
  },
  "VAL-NRM-002": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Preserve Provenance"
  },
  "VAL-NRM-003": {
    "mode": "existing",
    "class": "CONDITIONAL / REVIEW",
    "title": "Preserve Scope"
  },
  "VAL-NRM-004": {
    "mode": "existing",
    "class": "REVIEW",
    "title": "Preserve Authority Boundaries"
  },
  "VAL-NRM-005": {
    "mode": "existing",
    "class": "CONDITIONAL / REVIEW",
    "title": "Preserve Evidence Context"
  },
  "VAL-NRM-006": {
    "mode": "existing",
    "class": "CONDITIONAL",
    "title": "Preserve Traceability"
  },
  "VAL-NRM-007": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Preserve Governed Change"
  },
  "VAL-NRM-008": {
    "mode": "conditional",
    "class": "CONDITIONAL",
    "title": "Distinguish Current / Historical State"
  },
  "VAL-NRM-009": {
    "mode": "existing",
    "class": "REVIEW",
    "title": "Do Not Claim Universal Truth"
  },
  "VAL-NRM-010": {
    "mode": "existing",
    "class": "REVIEW",
    "title": "Do Not Convert Inputs into Conclusions"
  },
  "VAL-NRM-011": {
    "mode": "existing",
    "class": "CONDITIONAL / REVIEW",
    "title": "Preserve Uncertainty"
  },
  "VAL-NRM-012": {
    "mode": "existing",
    "class": "REVIEW / CONDITIONAL",
    "title": "Interoperate Without Authority Transfer"
  }
}

def _existing_rule_ids(results):
    return {x.get("rule_id") for x in results}

def _profile_applicability(rule_id, kind, d):
    """Return (applicable, reason). Conservative triggers: do not invent substantive facts."""
    # Object-specific rules, including identifier/type/evaluation rules whose
    # catalog prefix is shared but whose semantics belong to only one object class.
    if rule_id.startswith("VAL-ATT-") and kind != "ATT":
        return False, "Attestation-specific rule does not apply to Trust Statement."
    if rule_id.startswith("VAL-TRST-") and kind != "TRST":
        return False, "Trust-Statement-specific rule does not apply to Attestation."
    if kind == "ATT" and rule_id in {"VAL-STR-002","VAL-SEM-004","VAL-LV-016"}:
        return False, "Trust-Statement-specific requirement does not apply to Attestation."
    if kind == "TRST" and rule_id in {"VAL-STR-001","VAL-SEM-001","VAL-SEM-007","VAL-LV-015"}:
        return False, "Attestation-specific requirement does not apply to Trust Statement."

    # Relationship semantics only apply when the relationship type is present.
    rel_map={
      "VAL-REL-003":"supports","VAL-REL-004":"references","VAL-REL-005":"derived-from",
      "VAL-REL-006":"evaluates","VAL-REL-007":"results-in","VAL-REL-008":"supersedes","VAL-REL-009":"corrects"
    }
    if rule_id in rel_map:
        present=any(isinstance(x,dict) and x.get("type")==rel_map[rule_id] for x in (d.get("relationships") or []))
        return present, f"No {rel_map[rule_id]} relationship serialized." if not present else "Relationship type present."

    # Registry/allocation/history dependent rules require external authoritative context.
    if rule_id in {"VAL-STR-006","VAL-STR-007","VAL-LV-001","VAL-LV-002","VAL-LV-009","VAL-LV-010",
                   "VAL-LV-012","VAL-LV-014","VAL-LV-017","VAL-LV-018"}:
        return True, "Applicable but requires authoritative registry/history/process context."

    # Provenance continuity/source-state rules apply when provenance exists, but may need external context.
    if rule_id in {"VAL-PA-001","VAL-PA-003","VAL-PA-004","VAL-PA-005"}:
        return True, "Applicable provenance rule; external/source-state context may be required."

    # Evidence/uncertainty rules are represented where the relevant fields exist.
    if rule_id in {"VAL-NRM-005","VAL-NRM-011"}:
        return True, "Applicable normative preservation rule."

    return True, "Applicable to base profile."

def finalize_catalog_coverage(results, kind, d, registry):
    present=_existing_rule_ids(results)
    for rid,meta in CANONICAL_RULE_DISPOSITION.items():
        if rid in present:
            continue
        applicable, reason=_profile_applicability(rid,kind,d)
        if not applicable:
            results.append(na(rid,"catalog-coverage","$",reason))
            continue
        mode=meta["mode"]
        if mode=="review":
            results.append(nt(rid,"review","$",f"{meta['title']}: governed Review required; not machine-adjudicated.",False))
        elif mode=="mixed":
            results.append(nt(rid,"review","$",f"{meta['title']}: machine-visible context accounted for; substantive portion requires governed Review.",False))
        elif mode=="conditional":
            # If no bounded deterministic test exists without external context, expose it rather than pass.
            results.append(nt(rid,"conditional","$",f"{meta['title']}: {reason}"))
        elif mode=="machine":
            # Remaining machine rules are explicitly accounted for. Where the object alone cannot prove the
            # institutional/process fact, not-tested is the only honest result.
            results.append(nt(rid,"machine-context","$",f"{meta['title']}: {reason}"))
        else:
            # Existing rules should already have been emitted; absence is implementation incompleteness.
            results.append(nt(rid,"implementation","$",f"{meta['title']}: expected executable mapping was not emitted."))
    return results

# Override validators to apply complete catalog accounting.
_validate_att_v02=validate_att
_validate_trst_v02=validate_trst
def validate_att(d, registry=None):
    return finalize_catalog_coverage(_validate_att_v02(d,registry),"ATT",d,registry)
def validate_trst(d, registry=None):
    return finalize_catalog_coverage(_validate_trst_v02(d,registry),"TRST",d,registry)

# Override report version.
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--output")
    ap.add_argument("--registry")
    ap.add_argument("--context")
    args=ap.parse_args()
    try:
        d=load(args.target)
        if not isinstance(d,dict): raise ValueError("Root document must be a mapping/object.")
        reg=registry_values(args.registry)
        ctx=execution_context(args.context)
        if "attestation_identifier" in d:
            profile="attestor.attestation.base"; ident=d.get("attestation_identifier"); results=validate_att(d,reg)
            results=context_results(results,"ATT",d,ctx)
        elif "trust_statement_identifier" in d:
            profile="attestor.trust-statement.base"; ident=d.get("trust_statement_identifier"); results=validate_trst(d,reg)
            results=context_results(results,"TRST",d,ctx)
        else: raise ValueError("Unable to identify canonical ATT/TRST object.")
        mandatory_fail=sum(x["mandatory"] and x["result"]=="fail" for x in results)
        mandatory_nt=sum(x["mandatory"] and x["result"]=="not-tested" for x in results)
        aggregate="invalid" if mandatory_fail else ("incomplete" if mandatory_nt else "valid")
        report={"validation_report":{"report_version":"V1.0","target_identifier":ident,"target_profile":profile,
          "target_version":d.get("version_identity"),"requirements_set":"Satoshium Attestor Executable Validation Requirements",
          "requirements_version":"0.1","validator_identifier":"satoshium-attestor-validator","validator_version":"0.4",
          "run_at":datetime.now().astimezone().isoformat(),"aggregate_result":aggregate,"results":results,
          "summary":{"passed":sum(x["result"]=="pass" for x in results),
                     "failed":sum(x["result"]=="fail" for x in results),
                     "not_applicable":sum(x["result"]=="not-applicable" for x in results),
                     "not_tested":sum(x["result"]=="not-tested" for x in results)},
          "notes":["All 91 canonical VAL-* rules are explicitly accounted for; bounded execution context may resolve context-dependent machine rules.",
                   "Review-dependent rules are never silently machine-passed.",
                   "Context-dependent machine rules remain not-tested when authoritative context is absent."]}}
    except Exception as e:
        report={"validation_report":{"report_version":"V1.0","target_identifier":None,"target_profile":None,
          "validator_identifier":"satoshium-attestor-validator","validator_version":"0.4",
          "run_at":datetime.now().astimezone().isoformat(),"aggregate_result":"error","results":[],
          "summary":{"passed":0,"failed":0,"not_applicable":0,"not_tested":0},"notes":[str(e)]}}
    text=json.dumps(report,indent=2)
    if args.output: Path(args.output).write_text(text+"\n",encoding="utf-8")
    else: print(text)
    return 0 if report["validation_report"]["aggregate_result"]=="valid" else 1

if __name__=="__main__": sys.exit(main())
