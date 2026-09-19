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
    r.append(check("VAL-STR-STRUCTURE","structure",c is not None,"created_at","RFC3339 creation timestamp represented.","created_at must be RFC3339.",False))
    r.append(check("VAL-STR-STRUCTURE","structure",u is not None,"updated_at","RFC3339 update timestamp represented.","updated_at must be RFC3339.",False))
    r.append(check("VAL-STR-STRUCTURE","structure",c is not None and u is not None and u>=c,"updated_at",
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

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--output")
    ap.add_argument("--registry")
    args=ap.parse_args()
    try:
        d=load(args.target)
        if not isinstance(d,dict): raise ValueError("Root document must be a mapping/object.")
        reg=registry_values(args.registry)
        if "attestation_identifier" in d:
            profile="attestor.attestation.base"; ident=d.get("attestation_identifier"); results=validate_att(d,reg)
        elif "trust_statement_identifier" in d:
            profile="attestor.trust-statement.base"; ident=d.get("trust_statement_identifier"); results=validate_trst(d,reg)
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

if __name__=="__main__": sys.exit(main())
