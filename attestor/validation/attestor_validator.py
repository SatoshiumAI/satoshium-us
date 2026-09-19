#!/usr/bin/env python3
"""Satoshium Attestor validator — implementation v0.1."""
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

def nonempty(v): return v is not None and (not isinstance(v,str) or bool(v.strip()))
def ts(v):
    if not isinstance(v,str): return None
    try: return datetime.fromisoformat(v.replace("Z","+00:00"))
    except ValueError: return None

def result(rule, layer, ok, location, message):
    return {"rule_id":rule,"layer":layer,"result":"pass" if ok else "fail","location":location,"message":message}

def common(data, kind):
    r=[]
    lc=data.get("lifecycle_state")
    r.append(result("VAL-SEM-002","controlled-semantics",lc in LIFECYCLE,"lifecycle_state","Lifecycle state is controlled." if lc in LIFECYCLE else "Invalid lifecycle state."))
    ps=data.get("publication_state")
    r.append(result("VAL-SEM-003","controlled-semantics",ps in PUBLICATION,"publication_state","Publication state is controlled." if ps in PUBLICATION else "Invalid publication state."))
    ver=data.get("version_identity")
    r.append(result("VAL-LV-011","lifecycle-versioning",isinstance(ver,str) and bool(VER_RE.fullmatch(ver)),"version_identity","Version identity matches initial implementation profile." if isinstance(ver,str) and VER_RE.fullmatch(ver) else "Version identity must match V<major>.<minor>."))
    c,u=ts(data.get("created_at")),ts(data.get("updated_at"))
    r.append(result("VAL-STR-TIME-001","structure",c is not None,"created_at","Valid RFC 3339 timestamp." if c else "created_at must be RFC 3339 date-time."))
    r.append(result("VAL-STR-TIME-002","structure",u is not None,"updated_at","Valid RFC 3339 timestamp." if u else "updated_at must be RFC 3339 date-time."))
    ok = c is not None and u is not None and u >= c
    r.append(result("VAL-STR-TIME-003","structure",ok,"updated_at","updated_at does not precede created_at." if ok else "updated_at must not precede created_at."))
    return r

def validate_att(d):
    r=[]
    aid=d.get("attestation_identifier")
    r.append(result("VAL-STR-001","structure",isinstance(aid,str) and bool(ATT_RE.fullmatch(aid)),"attestation_identifier","Valid ATT identifier." if isinstance(aid,str) and ATT_RE.fullmatch(aid) else "Identifier must match ATT-YYYY-NNNN."))
    typ=d.get("attestation_type")
    r.append(result("VAL-SEM-001","controlled-semantics",typ in ATT_TYPES,"attestation_type","Controlled Attestation Type." if typ in ATT_TYPES else "Invalid Attestation Type."))
    a=d.get("attesting_authority") or {}
    r.append(result("VAL-ATT-002","authority",nonempty(a.get("identifier")),"attesting_authority.identifier","Attesting Authority identified." if nonempty(a.get("identifier")) else "Attesting Authority identifier required."))
    r.append(result("VAL-PA-006","authority",a.get("authority_context") in AUTH,"attesting_authority.authority_context","Controlled authority context." if a.get("authority_context") in AUTH else "Invalid authority context."))
    s=d.get("subject") or {}
    r.append(result("VAL-ATT-SUBJECT-001","structure",nonempty(s.get("identifier")) and nonempty(s.get("type")),"subject","Subject identifier and type required."))
    r.append(result("VAL-ATT-ASSERT-001","structure",nonempty(d.get("assertion")),"assertion","Assertion present." if nonempty(d.get("assertion")) else "Non-empty assertion required."))
    r.append(result("VAL-ATT-004","structure",nonempty(d.get("scope")),"scope","Scope present." if nonempty(d.get("scope")) else "Non-empty scope required."))
    p=d.get("provenance") or {}
    r.append(result("VAL-SEM-005","provenance-authority",p.get("mode") in PROV,"provenance.mode","Controlled provenance mode." if p.get("mode") in PROV else "Invalid provenance mode."))
    r.append(result("VAL-ATT-005","provenance-authority",nonempty(p.get("source_or_origin")),"provenance.source_or_origin","Provenance source/origin present." if nonempty(p.get("source_or_origin")) else "Provenance source/origin required."))
    if p.get("mode")=="derived":
        r.append(result("VAL-PA-DERIVED-001","provenance-authority",nonempty(p.get("derivation_basis")),"provenance.derivation_basis","Derived provenance basis present." if nonempty(p.get("derivation_basis")) else "Derived provenance requires derivation_basis."))
    r += relationships(d)
    r += common(d,"ATT")
    r.append(result("VAL-ATT-001","structure","trust_statement_identifier" not in d,"trust_statement_identifier","ATT/TRST identity remains distinct." if "trust_statement_identifier" not in d else "ATT must not contain trust_statement_identifier."))
    return r

def relationships(d):
    r=[]
    for i,x in enumerate(d.get("relationships") or []):
        ok=isinstance(x,dict) and x.get("type") in REL
        r.append(result("VAL-SEM-006","relationships",ok,f"relationships[{i}].type","Controlled relationship type." if ok else "Invalid relationship type."))
        ok2=isinstance(x,dict) and nonempty(x.get("target_identifier"))
        r.append(result("VAL-REL-001","relationships",ok2,f"relationships[{i}].target_identifier","Relationship target present." if ok2 else "Relationship target required."))
    return r

def validate_trst(d):
    r=[]
    tid=d.get("trust_statement_identifier")
    r.append(result("VAL-STR-002","structure",isinstance(tid,str) and bool(TRST_RE.fullmatch(tid)),"trust_statement_identifier","Valid TRST identifier." if isinstance(tid,str) and TRST_RE.fullmatch(tid) else "Identifier must match TRST-YYYY-NNNN."))
    s=d.get("subject") or {}
    r.append(result("VAL-TRST-SUBJECT-001","structure",nonempty(s.get("identifier")) and nonempty(s.get("type")),"subject","Subject identifier and type required."))
    r.append(result("VAL-TRST-001","structure",nonempty(d.get("bounded_conclusion")),"bounded_conclusion","Bounded conclusion present." if nonempty(d.get("bounded_conclusion")) else "Bounded conclusion required."))
    r.append(result("VAL-TRST-SCOPE-001","structure",nonempty(d.get("scope")),"scope","Scope present." if nonempty(d.get("scope")) else "Scope required."))
    a=d.get("attestor_attribution") or {}
    r.append(result("VAL-TRST-003","authority",nonempty(a.get("identifier")) and a.get("authority_context")=="Attestor","attestor_attribution","Attestor attribution preserved." if nonempty(a.get("identifier")) and a.get("authority_context")=="Attestor" else "Attestor attribution requires identifier and authority_context: Attestor."))
    supp=d.get("supporting_attestations")
    ok=isinstance(supp,list) and len(supp)>0 and all(isinstance(x,str) and ATT_RE.fullmatch(x) for x in supp)
    r.append(result("VAL-TRST-006","relationships",ok,"supporting_attestations","Supporting ATT references are traceable." if ok else "At least one valid ATT identifier required."))
    e=d.get("evaluation") or {}
    r.append(result("VAL-SEM-004","controlled-semantics",e.get("outcome") in OUTCOMES,"evaluation.outcome","Controlled Evaluation Outcome." if e.get("outcome") in OUTCOMES else "Invalid Evaluation Outcome."))
    br=e.get("basis_references")
    r.append(result("VAL-TRST-005","normative",isinstance(br,list) and len(br)>0,"evaluation.basis_references","Evaluation basis traceable." if isinstance(br,list) and br else "At least one basis reference required."))
    ar=e.get("applicable_rules")
    r.append(result("VAL-TRST-007","normative",isinstance(ar,list) and len(ar)>0,"evaluation.applicable_rules","Applicable rules represented." if isinstance(ar,list) and ar else "At least one applicable rule required."))
    p=d.get("provenance") or {}
    ok=p.get("mode")=="derived" and nonempty(p.get("source_or_origin")) and nonempty(p.get("derivation_basis"))
    r.append(result("VAL-TRST-008","provenance-authority",ok,"provenance","TRST derived provenance complete." if ok else "TRST provenance must be derived with source/origin and derivation_basis."))
    r += relationships(d)
    r += common(d,"TRST")
    r.append(result("VAL-TRST-IDENTITY-001","structure","attestation_identifier" not in d,"attestation_identifier","ATT/TRST identity remains distinct." if "attestation_identifier" not in d else "TRST must not contain attestation_identifier."))
    return r

def load(path):
    txt=Path(path).read_text(encoding="utf-8")
    if path.endswith(".json"): return json.loads(txt)
    if yaml is None: raise RuntimeError("PyYAML is required for YAML input.")
    return yaml.safe_load(txt)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--output")
    args=ap.parse_args()
    try:
        d=load(args.target)
        if not isinstance(d,dict): raise ValueError("Root document must be a mapping/object.")
        if "attestation_identifier" in d:
            profile="attestor.attestation.base"; ident=d.get("attestation_identifier"); results=validate_att(d)
        elif "trust_statement_identifier" in d:
            profile="attestor.trust-statement.base"; ident=d.get("trust_statement_identifier"); results=validate_trst(d)
        else: raise ValueError("Unable to identify canonical ATT/TRST object.")
        failed=sum(x["result"]=="fail" for x in results)
        report={"validation_report":{"report_version":"V1.0","target_identifier":ident,
          "target_profile":profile,"target_version":d.get("version_identity"),
          "requirements_set":"Satoshium Attestor Executable Validation Requirements",
          "requirements_version":"0.1","validator_identifier":"satoshium-attestor-validator",
          "validator_version":"0.1","run_at":datetime.now().astimezone().isoformat(),
          "aggregate_result":"invalid" if failed else "valid","results":results,
          "summary":{"passed":sum(x["result"]=="pass" for x in results),"failed":failed,
                     "not_applicable":0,"not_tested":0},"notes":[]}}
    except Exception as e:
        report={"validation_report":{"report_version":"V1.0","target_identifier":None,
          "target_profile":None,"validator_identifier":"satoshium-attestor-validator",
          "validator_version":"0.1","run_at":datetime.now().astimezone().isoformat(),
          "aggregate_result":"error","results":[],"summary":{"passed":0,"failed":0,"not_applicable":0,"not_tested":0},
          "notes":[str(e)]}}
    out=json.dumps(report,indent=2)
    if args.output: Path(args.output).write_text(out+"\n",encoding="utf-8")
    else: print(out)
    return 0 if report["validation_report"]["aggregate_result"]=="valid" else 1

if __name__=="__main__": sys.exit(main())
