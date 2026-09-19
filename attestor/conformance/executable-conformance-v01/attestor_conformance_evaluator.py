#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from datetime import datetime

REVIEW_RULES_BY_PROFILE={
 "attestor.attestation.base":{
  "VAL-PA-007","VAL-PA-008","VAL-LV-015","VAL-NRM-004","VAL-NRM-009","VAL-NRM-010",
  "VAL-REL-010","VAL-REL-011","VAL-REL-012","VAL-LV-005","VAL-LV-018"
 },
 "attestor.trust-statement.base":{
  "VAL-TRST-014","VAL-TRST-015","VAL-PA-007","VAL-PA-008","VAL-LV-016","VAL-NRM-004",
  "VAL-NRM-009","VAL-NRM-010","VAL-NRM-012","VAL-REL-010","VAL-REL-011",
  "VAL-REL-012","VAL-LV-005","VAL-LV-018"
 }
}
VALID_REVIEW={"satisfied","not-satisfied","not-demonstrated"}

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("request")
    ap.add_argument("--evidence-dir",required=True)
    ap.add_argument("--reviews")
    ap.add_argument("--output")
    a=ap.parse_args()
    try:
        req=load(a.request)["conformance_request"]
        target=req["target"]; requirements=req["requirements"]; evidence=req["evidence"]
        tid=target["target_identifier"]; tver=target["target_version"]; profile=requirements["conformance_profile"]
        results=[]; evidence_refs=[]

        # Validation evidence must exist, match target/version, and be aggregate valid.
        reports=[]
        for name in evidence.get("validation_reports",[]):
            p=Path(a.evidence_dir)/name
            r=load(p)["validation_report"]; reports.append(r); evidence_refs.append(name)
        if not reports:
            results.append({"requirement_id":"CONF-VAL-001","disposition":"not-demonstrated",
                            "evidence_references":[],"message":"Required Validation Report absent."})
        else:
            for r in reports:
                match=(r.get("target_identifier")==tid and r.get("target_version")==tver)
                results.append({"requirement_id":"CONF-VAL-001",
                  "disposition":"satisfied" if match else "not-satisfied",
                  "evidence_references":[r.get("target_identifier")],
                  "message":"Validation evidence target/version matches request." if match else "Validation evidence target/version mismatch."})
                agg=r.get("aggregate_result")
                results.append({"requirement_id":"CONF-VAL-002",
                  "disposition":"satisfied" if agg=="valid" else ("not-satisfied" if agg=="invalid" else "not-demonstrated"),
                  "evidence_references":[r.get("target_identifier")],
                  "message":f"Validation aggregate is {agg}."})
                mandatory_nt=[x for x in r.get("results",[]) if x.get("mandatory",True) and x.get("result")=="not-tested"]
                results.append({"requirement_id":"CONF-VAL-003",
                  "disposition":"satisfied" if not mandatory_nt else "not-demonstrated",
                  "evidence_references":[r.get("target_identifier")],
                  "message":f"Mandatory machine not-tested count: {len(mandatory_nt)}."})

        # Governed Review evidence.
        required=REVIEW_RULES_BY_PROFILE.get(profile)
        if required is None:
            raise ValueError(f"Unsupported conformance profile: {profile}")
        reviews=[]
        if a.reviews:
            raw=load(a.reviews)
            reviews=raw.get("review_records",raw if isinstance(raw,list) else [])
            evidence_refs.append(Path(a.reviews).name)
        by_rule={}
        for rr in reviews:
            if rr.get("target_identifier")==tid and rr.get("target_version")==tver:
                by_rule.setdefault(rr.get("requirement_id"),[]).append(rr)

        for rid in sorted(required):
            rrlist=by_rule.get(rid,[])
            if not rrlist:
                disp="not-demonstrated"; msg="Required governed Review record absent."; refs=[]
            else:
                rr=rrlist[-1]; d=rr.get("determination")
                if d not in VALID_REVIEW:
                    disp="not-demonstrated"; msg="Governed Review determination is missing or uncontrolled."
                else:
                    disp=d; msg="Governed Review evidence supplied."
                refs=[rr.get("review_record_identifier")]
            results.append({"requirement_id":f"CONF-REV-{rid}","disposition":disp,
                            "evidence_references":refs,"message":msg})

        dispositions=[x["disposition"] for x in results]
        aggregate=("nonconformant" if "not-satisfied" in dispositions else
                   "undetermined" if "not-demonstrated" in dispositions else "conformant")
        record={"conformance_determination":{
          "determination_version":"V1.0",
          "target":target,"requirements":requirements,
          "evidence_references":evidence_refs,
          "requirement_results":results,
          "aggregate_determination":aggregate,
          "determined_by":{"identifier":"satoshium-attestor-conformance-evaluator","authority_context":"Attestor"},
          "determined_at":datetime.now().astimezone().isoformat(),
          "limitations":["Representative implementation evidence unless explicitly designated production."],
          "notes":["Validation evidence and governed Review evidence remain distinct."]}}
    except Exception as e:
        record={"conformance_determination":{"determination_version":"V1.0","aggregate_determination":"error",
          "requirement_results":[],"limitations":[],"notes":[str(e)]}}
    txt=json.dumps(record,indent=2)
    if a.output: Path(a.output).write_text(txt+"\n",encoding="utf-8")
    else: print(txt)
    return 0 if record["conformance_determination"]["aggregate_determination"]=="conformant" else 1
if __name__=="__main__": raise SystemExit(main())
