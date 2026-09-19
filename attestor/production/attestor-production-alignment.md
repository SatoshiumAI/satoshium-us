# Satoshium Attestor — Production Alignment Specification

**Version:** 0.1  
**Stage:** Implementation & Validation  
**Step:** 15 — Production Alignment

## 1. Purpose

This specification reconciles the representative implementation proven through Steps 5–14 with the established Attestor Production architecture.

It answers:

> What must be true before representative executable proof may be used in a real Attestor production operation?

Production Alignment does not authorize production. It establishes the controls, evidence, and transitions required before the Production Readiness Gate may be evaluated.

## 2. Established Production Chain

The governing production sequence remains:

> Real Governed Matter → Attestation → Eligible Inputs → Evaluation Basis → Rule-Constrained Evaluation → Outcome → Bounded Conclusion → Trust Statement → Validation / Review / Lifecycle → Conformance where applicable → Publication where authorized

The implementation must preserve this sequence without collapsing institutional stages.

## 3. Representative-to-Production Boundary

Representative artifacts MUST NOT be promoted into production objects merely by renaming identifiers.

Production requires a fresh governed run using:

- real governed matter;
- actual source and evidence records;
- actual Attesting Authority;
- actual Eligibility determination;
- actual Evaluation Basis;
- actual rule-constrained Evaluation;
- actual bounded conclusion;
- canonical identifier allocation;
- production execution context;
- production Validation Reports;
- actual governed Review records;
- Conformance Determination where required;
- lifecycle decisions;
- publication decision where applicable;
- preservation of the resulting record trail.

Representative identifiers `ATT-2026-9001` and `TRST-2026-9001` remain fixtures only.

## 4. Production Roles

### 4.1 Governed Matter Owner / Source Authority
Provides or controls the real matter, source, or record used as input. Source authority is preserved.

### 4.2 Attesting Authority
Owns the bounded assertion represented by the production Attestation.

### 4.3 Attestor Evaluation Authority
Performs the governed rule-constrained evaluation and owns the bounded Trust Statement conclusion.

### 4.4 Validator
Executes machine-testable validation requirements. The Validator does not make Review judgments.

### 4.5 Governed Reviewer
Resolves applicable Review-bound requirements through attributable Review records.

### 4.6 Conformance Authority
Makes the bounded Conformance Determination from declared requirements and governed evidence.

### 4.7 Publication Authority
Makes the separate publication decision where publication is requested.

A single implementation or human may perform more than one operational role only where governance permits it, but the authority contexts MUST remain distinguishable in the record.

## 5. Production Evidence Package

A production run MUST preserve a reviewable evidence package containing, as applicable:

1. governed matter / source references;
2. source-state snapshot or equivalent state-at-evaluation evidence;
3. Eligibility determination;
4. production Attestation;
5. Evaluation Basis;
6. applicable rules/methodology identity;
7. evaluation record;
8. production Trust Statement;
9. production execution context;
10. identifier-allocation / registry evidence;
11. ATT Validation Report;
12. TRST Validation Report;
13. governed Review records;
14. Conformance Determination where required;
15. lifecycle records;
16. version/change records where applicable;
17. publication decision and publication evidence where applicable;
18. provenance links connecting the package.

No evidence item may be silently inferred merely because a representative run previously succeeded.

## 6. Production Identifier Allocation

Production identifiers MUST be allocated only during the real production operation under the canonical identifier rules.

The representative sequence `9001` MUST NOT be converted into production identity.

The first production identifiers remain unallocated until the Production Readiness Gate passes and the governed operation begins.

If the first production operation proceeds in 2026, the expected initial families are:

- `ATT-2026-0001`
- `TRST-2026-0001`

This specification does not allocate them.

## 7. Production Execution Context

The representative Execution Context Contract established during validation becomes a production control surface.

Production context MUST be backed by actual governed evidence for facts such as:

- identifier assigned at canonical creation;
- initial lifecycle state;
- creation / activation separation;
- Review does not silently change state;
- historical identity preservation;
- same-object revision preserves identifier;
- no silent overwrite;
- successor relationship controls;
- material input traceability;
- evaluation provenance;
- provenance continuity;
- source state at evaluation.

A production context assertion without attributable evidence MUST NOT be treated as established merely because the field is `true`.

## 8. Eligibility Alignment

Representative validation did not substitute for production Eligibility.

Before a production Attestation is used in evaluation, the relevant governed inputs MUST receive the Eligibility determination required by Attestor methodology.

Eligibility records MUST identify:

- governed input;
- evaluation purpose/scope;
- determination;
- authority;
- basis;
- relevant time/state;
- limitations or exclusions where material.

Eligibility ≠ Validation and Eligibility ≠ favorable Evaluation Outcome.

## 9. Evaluation Alignment

The production Trust Statement MUST arise from an actual rule-constrained Evaluation.

The Evaluation record MUST preserve:

- target/subject;
- supporting Attestations;
- eligible governed inputs;
- Evaluation Basis;
- applicable rules;
- relevant state/time;
- material conflicts;
- material exclusions;
- limitations;
- uncertainty;
- Evaluation Outcome;
- bounded conclusion;
- provenance connecting inputs to conclusion.

A prewritten conclusion MUST NOT be backfilled with evidence merely to imitate the representative fixture.

## 10. Validation Alignment

Production ATT and TRST objects MUST be validated using the established executable Validation architecture.

For production alignment:

- target identity/version MUST match the production object;
- registry context MUST be authoritative;
- execution context MUST be attributable;
- every applicable mandatory machine-testable rule MUST be resolved;
- no failed mandatory rule is permitted for a `valid` result;
- governed Review rules remain outside machine pass/fail.

Representative Validation Reports cannot serve as production Validation Reports.

## 11. Review Alignment

Production Review records MUST be actual governed decisions.

Representative Review records from Step 14 MUST NOT be copied, renamed, or reused as production Review evidence.

Each production Review record MUST identify the actual target, requirement, reviewer/authority, basis, evidence, limitations/uncertainty where material, and review time.

## 12. Conformance Alignment

Where the production profile requires Conformance:

> Production Validation Evidence + Required Governed Review Evidence + Required Context Evidence → Production Conformance Determination

A production target cannot inherit `conformant` status from a representative target.

Conformance remains bounded to target identity/version, requirements set/version, profile, and evidence package.

## 13. Lifecycle Alignment

Production object creation begins under the adopted lifecycle controls.

Creation, activation, publication, supersession, withdrawal, and retirement remain distinct governed events.

A production object MUST NOT be treated as active or published merely because validation or conformance succeeds.

## 14. Publication Alignment

Publication is optional unless a separate governing requirement makes it necessary.

A production object may be:

- valid but unpublished;
- conformant but unpublished;
- active but unpublished.

Publication requires a separate authorized publication decision and preservation of publication evidence.

## 15. Production Run Manifest

Every production operation SHOULD create a manifest:

```yaml
production_run:
  run_identifier:
  methodology_version:
  requirements_set:
  requirements_version:
  governed_matter:
  source_evidence: []
  eligibility_records: []
  attestation_identifier:
  evaluation_record:
  trust_statement_identifier:
  execution_context:
  validation_reports: []
  review_records: []
  conformance_determinations: []
  lifecycle_records: []
  publication_records: []
  started_at:
  completed_at:
  status:
  notes:
```

The manifest is an orchestration/traceability record. It does not replace any canonical ATT/TRST object or transfer authority among institutions.

## 16. Production Alignment Checklist

Before the Production Readiness Gate, Attestor must be able to answer **yes** to all of the following:

1. Are canonical ATT/TRST schemas and executable rules established?
2. Can representative ATT/TRST objects validate successfully?
3. Is the machine/Review boundary explicit?
4. Can governed Review evidence be represented?
5. Can Conformance be determined without collapsing it into Validation?
6. Is production identifier allocation controlled?
7. Is real governed matter distinguishable from fixtures?
8. Is production Eligibility separately recordable?
9. Is the Evaluation Basis separately recordable?
10. Is rule-constrained Evaluation separately recordable?
11. Can source state at evaluation be preserved?
12. Can production execution context be evidenced rather than asserted?
13. Can lifecycle events be recorded distinctly?
14. Can publication remain a separate decision?
15. Can the entire operation be reconstructed from a production evidence package?
16. Are representative artifacts explicitly barred from being relabeled as production proof?

## 17. Current Alignment Assessment

Items 1–5 are demonstrated by the completed executable-validation and executable-conformance work.

Items 6–16 are architecturally defined or bounded here, but must be checked against actual implementation artifacts before the Production Readiness Gate.

Therefore:

> Production Alignment architecture is established.

But:

> Production Readiness is not yet declared.

## 18. Step 15 Determination

**Production Alignment v0.1 → ESTABLISHED.**

**Representative proof → preserved as non-production.**

**Production evidence package → defined.**

**Production role and authority separation → defined.**

**Production identifier boundary → preserved.**

**Next → Production Alignment implementation checklist and Production Readiness Gate preparation.**
