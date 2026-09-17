# Satoshium Attestor — Evaluation

**Path:** `/attestor/evaluation/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

Evaluation defines the heart of Attestor: how Attestations and eligible governed inputs undergo **Rule-Constrained Evaluation** to produce a bounded Trust Statement.

## Canonical Evaluation Path

`Attestation + Eligible Governed Inputs → Rule-Constrained Evaluation → Trust Statement`

Attestor does not convert source objects directly into conclusions.

## Evaluation Sequence

Conceptually:

1. Identify Attestation and Assertion.
2. Confirm Evaluation Purpose and Scope.
3. Establish Eligible Governed Inputs.
4. Preserve Authority and Provenance Context.
5. Apply Applicable Attestor Rules.
6. Consider Supporting, Limiting, Conflicting, and Contradictory Material.
7. Preserve Uncertainty and Material Limitations.
8. Determine Evaluation Outcome.
9. Form Bounded Attestor Conclusion.
10. Produce or Update Governed Trust Statement.

Detailed operational procedure belongs to Methodology. Machine-testable requirements belong to Validation.

## Evaluation Basis

The evaluation basis consists only of eligible governed inputs admitted for the particular evaluation.

Material information must not be excluded merely because it:

- weakens an assertion;
- conflicts with another authority;
- introduces uncertainty;
- supports contradiction; or
- prevents a preferred conclusion.

## Evaluation Outcomes

The Controlled Values architecture established five outcomes.

### `supported`

The eligible evaluation basis supports the assertion within the defined scope without a material unresolved conflict that prevents that conclusion.

### `partially-supported`

The basis supports a bounded or material portion of the assertion, but not the assertion in full as presented.

### `not-supported`

The eligible basis does not provide sufficient support for the assertion within the defined scope, without establishing the stronger conclusion that the assertion is contradicted.

### `contradicted`

The eligible basis materially supports a conclusion inconsistent with the assertion within the defined scope.

### `indeterminate`

The eligible basis, conflict, uncertainty, provenance, state, or limitations do not permit Attestor to responsibly determine support or contradiction.

Exact operational thresholds and validation conditions remain for Methodology and Validation.

## Outcome vs. Conclusion

These are distinct:

- **Evaluation Outcome** → controlled classification.
- **Bounded Conclusion** → substantive conclusion Attestor makes.
- **Trust Statement** → canonical Attestor object carrying the conclusion and its governed context.

`Outcome ≠ Conclusion ≠ Trust Statement Identity`

## Rule-Constrained Evaluation

Evaluation operates under identifiable Attestor rules and methodology.

Rules constrain:

- admission and treatment of inputs;
- preservation of scope;
- preservation of authority boundaries;
- provenance;
- treatment of conflict;
- treatment of uncertainty;
- limitations; and
- the strength and breadth of the conclusion.

## No Automatic Source Conversion

No Suite or external source object automatically becomes an Attestor conclusion.

`Source Object → Eligible Governed Input → Rule-Constrained Evaluation → Trust Statement`

**Reference does not transfer authority.**

## No Universal Weighting Model

This architecture does not adopt:

- confidence percentages;
- reputation scores;
- majority-source rules;
- universal numeric weighting;
- automatic authority hierarchy; or
- hidden ranking.

If a future specialized methodology requires weighting, it must be explicitly governed, explainable, bounded to that methodology, and separately adopted.

## Conflict and Uncertainty

Material conflict and uncertainty must remain visible and affect the conclusion where relevant.

Attestor does not force every evaluation into a positive or negative determination.

`indeterminate` is a legitimate governed outcome.

## Evaluation-Time State

An evaluation remains tied to the relevant time and state of its evaluation basis.

A later source change does not silently rewrite the historical evaluation.

Material later changes may trigger:

- review;
- correction;
- supersession; or
- new evaluation

under Lifecycle and Versioning architecture.

## Reviewability

A governed evaluation must preserve enough context to understand:

- assertion;
- scope;
- eligible basis;
- material exclusions where required;
- applicable rules/methodology;
- outcome;
- bounded conclusion;
- provenance; and
- material limitations.

## What Evaluation Does Not Establish

`Evaluation ≠ Universal Truth Determination`

`Evaluation ≠ Certification`

`Evaluation ≠ Source Authority Transfer`

`Evaluation ≠ Reputation`

`Evaluation ≠ Trust Score`

`Evaluation ≠ Guarantee`

Evaluation produces the governed basis for a bounded Attestor Trust Statement.

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Evaluation → Established**

- Rule-Constrained Evaluation → defined
- conceptual sequence → established
- outcome semantics → established conceptually
- outcome vs. conclusion → distinguished
- conflict/uncertainty treatment → required
- universal scoring/weighting → not adopted
- operational methodology → deferred to Methodology
- machine validation → deferred to Validation
- production proof → pending
