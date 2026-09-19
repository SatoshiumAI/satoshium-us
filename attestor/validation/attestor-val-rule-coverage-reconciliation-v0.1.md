# Satoshium Attestor — VAL-* Rule Coverage Reconciliation

**Version:** 0.1  
**Stage:** Executable Validation — Step 6  
**Validator reviewed:** `executable-validator-v01/attestor_validator.py`  
**Rule source:** `attestor-validation-rules.md`

## 1. Purpose

This reconciliation compares the complete numbered Attestor Validation Rule Catalog against the first executable validator implementation.

The objective is not to force every institutional rule into code. It is to establish, rule by rule, whether each requirement is:

- already implemented as an executable check;
- suitable for additional deterministic/conditional implementation;
- only partially machine-testable because substantive judgment remains governed Review; or
- intentionally deferred.

`VAL-* Catalog → Coverage Classification → Test Obligation → Validator / Review Boundary`

## 2. Coverage Summary

- **implemented:** 21
- **not-yet-implemented:** 50
- **partial/review:** 10
- **review-only:** 10
- **deferred:** 0
- **Total catalog rules reconciled:** 91

## 3. Rule-by-Rule Reconciliation

| Rule | Catalog class | Step 6 coverage | Disposition |
|---|---|---|---|
| `VAL-REP-001` — Parseable Representation | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-REP-002` — Declared Object Profile | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-REP-003` — Legacy Trust Signal Exclusion | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-STR-001` — Attestation Identifier Family | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-STR-002` — Trust Statement Identifier Family | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-STR-003` — Four-Digit Creation Year | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-STR-004` — Four-Digit Sequence | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-STR-005` — Object-Class / Prefix Coherence | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-STR-006` — Canonical Identifier Uniqueness | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-STR-007` — Pre-Creation Identifier Boundary | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-STR-008` — Source Identifier Preservation | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-SEM-001` — Attestation Type Vocabulary | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-SEM-002` — Lifecycle Vocabulary | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-SEM-003` — Publication Vocabulary | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-SEM-004` — Evaluation Outcome Vocabulary | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-SEM-005` — Provenance Mode Vocabulary | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-SEM-006` — Relationship Vocabulary | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-SEM-007` — Noncanonical Trust/Confidence Vocabulary | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-ATT-001` — Distinct Attestation Identity | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-ATT-002` — Attesting Authority Identifiable | CONDITIONAL | **implemented** | Executable in validator v0.1 |
| `VAL-ATT-003` — Authority-to-Assertion Context | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-ATT-004` — Attestation Scope Preserved | CONDITIONAL | **implemented** | Executable in validator v0.1 |
| `VAL-ATT-005` — Attestation Provenance Preserved | CONDITIONAL | **implemented** | Executable in validator v0.1 |
| `VAL-ATT-006` — Material Limitations Preserved | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-ATT-007` — Attestation Is Not Trust Statement | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-TRST-001` — Bounded Conclusion Present | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-TRST-002` — Conclusion / Outcome Separation | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-TRST-003` — Attestor Attribution | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-TRST-004` — Evaluation Outcome Present | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-TRST-005` — Evaluation Basis Traceable | CONDITIONAL | **implemented** | Executable in validator v0.1 |
| `VAL-TRST-006` — Supporting Attestation Traceability | CONDITIONAL | **implemented** | Executable in validator v0.1 |
| `VAL-TRST-007` — Applicable Rules / Methodology Context | CONDITIONAL | **implemented** | Executable in validator v0.1 |
| `VAL-TRST-008` — Derived Provenance | MACHINE / CONDITIONAL | **implemented** | Executable in validator v0.1 |
| `VAL-TRST-009` — Relevant Time / State | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-TRST-010` — Material Conflict Preservation | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-TRST-011` — Material Exclusion Preservation | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-TRST-012` — Limitation Preservation | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-TRST-013` — Uncertainty Preservation | CONDITIONAL / REVIEW | **partial/review** | Machine can test representation/context; substantive judgment remains review |
| `VAL-TRST-014` — No Universal-Truth Representation | REVIEW | **review-only** | Do not automate substantive institutional judgment |
| `VAL-TRST-015` — Trust Statement Is Not Automatic Input Conversion | REVIEW | **review-only** | Do not automate substantive institutional judgment |
| `VAL-PA-001` — Material Input Traceability | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-PA-002` — Minimum Provenance Context | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-PA-003` — Evaluation Provenance | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-PA-004` — Provenance Continuity | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-PA-005` — Source-State Preservation | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-PA-006` — Authority Context Preservation | CONDITIONAL | **implemented** | Executable in validator v0.1 |
| `VAL-PA-007` — No Authority Transfer | REVIEW / CONDITIONAL | **partial/review** | Machine can test representation/context; substantive judgment remains review |
| `VAL-PA-008` — Attestor Authority Boundary | REVIEW | **review-only** | Do not automate substantive institutional judgment |
| `VAL-PA-009` — Authority Conflict Preservation | CONDITIONAL / REVIEW | **partial/review** | Machine can test representation/context; substantive judgment remains review |
| `VAL-REL-001` — Explicit Source and Target | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-REL-002` — Direction Preserved | MACHINE / CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-REL-003` — `supports` Direction | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-REL-004` — `references` Does Not Imply Support | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-REL-005` — `derived-from` Direction | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-REL-006` — `evaluates` Direction | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-REL-007` — `results-in` Direction | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-REL-008` — `supersedes` Direction | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-REL-009` — `corrects` Direction | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-REL-010` — Connection Does Not Merge Identity | MACHINE / REVIEW | **partial/review** | Machine can test representation/context; substantive judgment remains review |
| `VAL-REL-011` — Relationship Does Not Establish Eligibility | REVIEW | **review-only** | Do not automate substantive institutional judgment |
| `VAL-REL-012` — Relationship Does Not Transfer Authority | REVIEW | **review-only** | Do not automate substantive institutional judgment |
| `VAL-LV-001` — Created Object Begins Draft | MACHINE / CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-LV-002` — Creation / Activation Separation | MACHINE / CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-LV-003` — Lifecycle / Publication Separation | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-LV-004` — Draft Is Not Active | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-LV-005` — Active Meaning | REVIEW | **review-only** | Do not automate substantive institutional judgment |
| `VAL-LV-006` — Non-Active State Distinction | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-LV-007` — Review Is Activity, Not State | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-LV-008` — Correction Is Activity, Not State | MACHINE | **not-yet-implemented** | Implement deterministic machine test |
| `VAL-LV-009` — Review Does Not Silently Change State | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-LV-010` — Historical Identity Preservation | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-LV-011` — Canonical Identity / Version Identity Separation | MACHINE | **implemented** | Executable in validator v0.1 |
| `VAL-LV-012` — Same-Object Revision Preserves Canonical Identifier | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-LV-013` — Version Identity Distinguishes Preserved Revision | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-LV-014` — No Silent Historical Overwrite | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-LV-015` — Material Attestation Change Requires New ATT | REVIEW / CONDITIONAL | **partial/review** | Machine can test representation/context; substantive judgment remains review |
| `VAL-LV-016` — Material Trust Statement Conclusion Requires New TRST | REVIEW / CONDITIONAL | **partial/review** | Machine can test representation/context; substantive judgment remains review |
| `VAL-LV-017` — Material Successor Relationship | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-LV-018` — Correction Reason / Versioning Decision Separation | REVIEW | **review-only** | Do not automate substantive institutional judgment |
| `VAL-NRM-001` — Preserve Attribution | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-NRM-002` — Preserve Provenance | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-NRM-003` — Preserve Scope | CONDITIONAL / REVIEW | **partial/review** | Machine can test representation/context; substantive judgment remains review |
| `VAL-NRM-004` — Preserve Authority Boundaries | REVIEW | **review-only** | Do not automate substantive institutional judgment |
| `VAL-NRM-005` — Preserve Evidence Context | CONDITIONAL / REVIEW | **partial/review** | Machine can test representation/context; substantive judgment remains review |
| `VAL-NRM-006` — Preserve Traceability | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-NRM-007` — Preserve Governed Change | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-NRM-008` — Distinguish Current / Historical State | CONDITIONAL | **not-yet-implemented** | Implement conditional machine test where context/profile permits |
| `VAL-NRM-009` — Do Not Claim Universal Truth | REVIEW | **review-only** | Do not automate substantive institutional judgment |
| `VAL-NRM-010` — Do Not Convert Inputs into Conclusions | REVIEW | **review-only** | Do not automate substantive institutional judgment |
| `VAL-NRM-011` — Preserve Uncertainty | CONDITIONAL / REVIEW | **partial/review** | Machine can test representation/context; substantive judgment remains review |
| `VAL-NRM-012` — Interoperate Without Authority Transfer | REVIEW / CONDITIONAL | **partial/review** | Machine can test representation/context; substantive judgment remains review |

## 4. Important Finding

Validator v0.1 is a functioning **base-profile validator**, but it does not yet implement the complete machine-testable portion of the Validation Rule Catalog.

That is expected for the first executable implementation. Step 6 makes the gap explicit so later implementation cannot mistake “validator runs” for “catalog coverage complete.”

The validator also currently emits several implementation-local rule identifiers that are not yet present in the canonical catalog (for example timestamp, subject, assertion, scope, and derived-provenance helper checks). Those checks are useful, but their rule identity must be normalized before the validator is frozen. The canonical catalog remains the authority for `VAL-*` identifiers.

## 5. Coverage Closure Requirements

Before executable validation can be considered coverage-complete for the base profiles:

1. Every deterministic catalog rule must map to an executable validator test or an explicit documented reason for non-applicability.
2. Every conditional catalog rule must define its applicability trigger and machine-testable portion.
3. Every mixed machine/review rule must distinguish the executable representation check from the substantive Review determination.
4. Review-only rules must never be silently reported as machine `pass`.
5. Implementation-local helper checks must either receive canonical catalog rule IDs or be represented as subordinate tests beneath a canonical rule.
6. `not-applicable` and `not-tested` must be exercised in fixtures, not merely defined in the report vocabulary.
7. Aggregate `incomplete` and `error` behavior must be exercised.
8. Relationship direction, provenance continuity, lifecycle/history, identity/version separation, and source-state preservation require dedicated boundary fixtures.
9. Registry-dependent uniqueness/reuse checks must remain conditional until authoritative registry context is supplied.
10. Materiality decisions for new ATT/TRST identity remain governed Review unless a later methodology makes a bounded portion machine-deterministic.

## 6. Step 6 Determination

**VAL-* Rule Coverage Reconciliation v0.1 → Established.**

**Validator v0.1 → Executable, but base-profile rule coverage is not yet complete.**

The next implementation action is to close the deterministic and conditional coverage gaps and build a boundary/negative fixture suite that proves `valid`, `invalid`, `incomplete`, `error`, `not-applicable`, and `not-tested` behavior before representative-object validation.
