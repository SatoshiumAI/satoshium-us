# Satoshium Attestor — VAL-* Rule Coverage Reconciliation v0.2

**Stage:** Executable Validation — Step 8  
**Validator reviewed:** `executable-validator-v02/attestor_validator.py`  
**Canonical rule source:** `attestor-validation-rules.md`  
**Catalog rules reconciled:** 91

## 1. Purpose

This is the formal post-Step-7 reconciliation of Validator v0.2 against the complete canonical `VAL-*` Rule Catalog.

It answers one question:

> Has Validator v0.2 closed enough of the executable rule-coverage gap to proceed to representative ATT/TRST validation?

## 2. Before / After

Validator v0.1 explicitly implemented **21 of 91** catalog rules.

Validator v0.2 now explicitly accounts for **61 of 91** catalog rules, including rules whose machine-visible portion is implemented while substantive institutional judgment remains governed Review.

Current classification:

- **implemented:** 47
- **explicitly-accounted/review-bounded:** 14
- **remaining-executable-gap:** 24
- **remaining-mixed-gap:** 2
- **review-only:** 4
- **deferred:** 0

The remaining executable or mixed machine/review gap is **26 rules**.

## 3. Rule-by-Rule Reconciliation

| Rule | Catalog class | Validator v0.2 coverage | Disposition |
|---|---|---|---|
| `VAL-REP-001` — Parseable Representation | MACHINE | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-REP-002` — Declared Object Profile | MACHINE | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-REP-003` — Legacy Trust Signal Exclusion | MACHINE | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-STR-001` — Attestation Identifier Family | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-STR-002` — Trust Statement Identifier Family | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-STR-003` — Four-Digit Creation Year | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-STR-004` — Four-Digit Sequence | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-STR-005` — Object-Class / Prefix Coherence | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-STR-006` — Canonical Identifier Uniqueness | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-STR-007` — Pre-Creation Identifier Boundary | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-STR-008` — Source Identifier Preservation | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-SEM-001` — Attestation Type Vocabulary | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-SEM-002` — Lifecycle Vocabulary | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-SEM-003` — Publication Vocabulary | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-SEM-004` — Evaluation Outcome Vocabulary | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-SEM-005` — Provenance Mode Vocabulary | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-SEM-006` — Relationship Vocabulary | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-SEM-007` — Noncanonical Trust/Confidence Vocabulary | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-ATT-001` — Distinct Attestation Identity | MACHINE | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-ATT-002` — Attesting Authority Identifiable | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-ATT-003` — Authority-to-Assertion Context | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-ATT-004` — Attestation Scope Preserved | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-ATT-005` — Attestation Provenance Preserved | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-ATT-006` — Material Limitations Preserved | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-ATT-007` — Attestation Is Not Trust Statement | MACHINE | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-TRST-001` — Bounded Conclusion Present | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-002` — Conclusion / Outcome Separation | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-003` — Attestor Attribution | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-004` — Evaluation Outcome Present | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-005` — Evaluation Basis Traceable | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-006` — Supporting Attestation Traceability | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-007` — Applicable Rules / Methodology Context | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-008` — Derived Provenance | MACHINE / CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-009` — Relevant Time / State | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-010` — Material Conflict Preservation | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-011` — Material Exclusion Preservation | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-012` — Limitation Preservation | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-TRST-013` — Uncertainty Preservation | CONDITIONAL / REVIEW | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-TRST-014` — No Universal-Truth Representation | REVIEW | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-TRST-015` — Trust Statement Is Not Automatic Input Conversion | REVIEW | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-PA-001` — Material Input Traceability | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-PA-002` — Minimum Provenance Context | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-PA-003` — Evaluation Provenance | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-PA-004` — Provenance Continuity | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-PA-005` — Source-State Preservation | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-PA-006` — Authority Context Preservation | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-PA-007` — No Authority Transfer | REVIEW / CONDITIONAL | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-PA-008` — Attestor Authority Boundary | REVIEW | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-PA-009` — Authority Conflict Preservation | CONDITIONAL / REVIEW | **remaining-mixed-gap** | Implement machine-testable representation/context portion; retain substantive Review boundary. |
| `VAL-REL-001` — Explicit Source and Target | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-REL-002` — Direction Preserved | MACHINE / CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-REL-003` — `supports` Direction | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-REL-004` — `references` Does Not Imply Support | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-REL-005` — `derived-from` Direction | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-REL-006` — `evaluates` Direction | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-REL-007` — `results-in` Direction | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-REL-008` — `supersedes` Direction | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-REL-009` — `corrects` Direction | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-REL-010` — Connection Does Not Merge Identity | MACHINE / REVIEW | **remaining-mixed-gap** | Implement machine-testable representation/context portion; retain substantive Review boundary. |
| `VAL-REL-011` — Relationship Does Not Establish Eligibility | REVIEW | **review-only** | Keep outside automatic adjudication; add explicit not-tested representation if applicable to executed profile. |
| `VAL-REL-012` — Relationship Does Not Transfer Authority | REVIEW | **review-only** | Keep outside automatic adjudication; add explicit not-tested representation if applicable to executed profile. |
| `VAL-LV-001` — Created Object Begins Draft | MACHINE / CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-LV-002` — Creation / Activation Separation | MACHINE / CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-LV-003` — Lifecycle / Publication Separation | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-LV-004` — Draft Is Not Active | MACHINE | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-LV-005` — Active Meaning | REVIEW | **review-only** | Keep outside automatic adjudication; add explicit not-tested representation if applicable to executed profile. |
| `VAL-LV-006` — Non-Active State Distinction | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-LV-007` — Review Is Activity, Not State | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-LV-008` — Correction Is Activity, Not State | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-LV-009` — Review Does Not Silently Change State | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-LV-010` — Historical Identity Preservation | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-LV-011` — Canonical Identity / Version Identity Separation | MACHINE | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-LV-012` — Same-Object Revision Preserves Canonical Identifier | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-LV-013` — Version Identity Distinguishes Preserved Revision | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-LV-014` — No Silent Historical Overwrite | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-LV-015` — Material Attestation Change Requires New ATT | REVIEW / CONDITIONAL | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-LV-016` — Material Trust Statement Conclusion Requires New TRST | REVIEW / CONDITIONAL | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-LV-017` — Material Successor Relationship | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-LV-018` — Correction Reason / Versioning Decision Separation | REVIEW | **review-only** | Keep outside automatic adjudication; add explicit not-tested representation if applicable to executed profile. |
| `VAL-NRM-001` — Preserve Attribution | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-NRM-002` — Preserve Provenance | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-NRM-003` — Preserve Scope | CONDITIONAL / REVIEW | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-NRM-004` — Preserve Authority Boundaries | REVIEW | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-NRM-005` — Preserve Evidence Context | CONDITIONAL / REVIEW | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-NRM-006` — Preserve Traceability | CONDITIONAL | **implemented** | Executable rule path is explicitly represented in Validator v0.2. |
| `VAL-NRM-007` — Preserve Governed Change | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-NRM-008` — Distinguish Current / Historical State | CONDITIONAL | **remaining-executable-gap** | Still requires deterministic/conditional executable mapping or explicit non-applicability trigger. |
| `VAL-NRM-009` — Do Not Claim Universal Truth | REVIEW | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-NRM-010` — Do Not Convert Inputs into Conclusions | REVIEW | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-NRM-011` — Preserve Uncertainty | CONDITIONAL / REVIEW | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |
| `VAL-NRM-012` — Interoperate Without Authority Transfer | REVIEW / CONDITIONAL | **explicitly-accounted/review-bounded** | Validator explicitly represents the rule; substantive governed Review is not machine-passed. |

## 4. Rule-ID Integrity

Validator v0.2 introduces no uncataloged canonical-style `VAL-*` identifiers.

## 5. Readiness Determination

**Representative ATT/TRST validation → NOT YET AUTHORIZED.**

Validator v0.2 materially improves coverage, but **26 executable/mixed rules remain without explicit v0.2 mapping**.

The correct next action is one final focused coverage-closure iteration rather than beginning representative-object validation.

That iteration should:

1. map every remaining deterministic rule;
2. define applicability triggers for remaining conditional rules;
3. explicitly represent applicable review-only rules as `not-tested` without converting them to machine pass;
4. eliminate or subordinate every implementation-local canonical-style `VAL-*` identifier;
5. add fixtures for newly implemented rule families;
6. rerun the 91-rule reconciliation; and
7. proceed to representative ATT/TRST validation only if no material machine-testable coverage gap remains.

## 6. Step 8 Determination

**VAL-* Rule Coverage Reconciliation v0.2 → Established.**

**Validator v0.2 → Materially expanded, but not yet coverage-complete for representative-object validation.**

**Next → Validator v0.3 focused coverage closure.**
