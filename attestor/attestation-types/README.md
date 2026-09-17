# Satoshium Attestor — Attestation Types

## Page
`/attestor/attestation-types/`

## Purpose
Attestation Types provide the governed classification vocabulary for canonical Attestations.

An Attestation Type classifies the **assertion expressed by the Attestation**. It does not redefine the type, identity, or authority of a referenced Suite or external source object.

## Canonical Context
**Attestor → Trust Statement**

`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

An Attestation is a governed, attributable assertion. Its Attestation Type identifies the controlled family to which that assertion belongs.

## Adopted Controlled Vocabulary

The adopted Attestation Types are:

| Controlled value | Meaning |
|---|---|
| `identity` | Bounded assertion involving identity, continuity, participation, association, or related identity context. |
| `evidence` | Bounded assertion concerning evidence, its relevance, relationship, or governed use. |
| `source-provenance` | Bounded assertion concerning source origin, attribution, authorship, provenance, or source relationship. |
| `verification-related` | Bounded assertion referencing verification, validation, review, certification, or comparable governed outcome. |
| `relationship-condition` | Bounded assertion concerning a relationship, condition, status, qualification, participation, or other scoped circumstance. |
| `correction-supersession` | Bounded assertion concerning correction, supersession, or governed change where an Attestation is the appropriate object. |

These values are established by Attestor Advanced Architecture and are also represented in `/attestor/controlled-values/`.

## Classification Principle
> **Type classifies the Attestation assertion. It does not transfer source authority.**

A verification-related Attestation does not make Attestor the Certifier.

An identity Attestation does not make Attestor the identity authority.

An evidence Attestation does not make Attestor the source of the evidence.

> **Reference does not transfer authority.**

## Type and Eligibility
Attestation Type and input eligibility are separate concepts.

- **Attestation Type** classifies the governed assertion.
- **Eligibility** determines whether a potential governed input is admissible for a particular evaluation.

> **Type ≠ Eligibility**

## Type and Evaluation
Attestation Type does not predetermine an Evaluation Outcome.

The controlled Evaluation Outcomes are:
- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

> **Attestation Type ≠ Evaluation Outcome**

## Type and Relationships
Attestation Type is also distinct from the relationship vocabulary:
- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

For example, an `evidence` Attestation may participate in a `supports` relationship, but those values describe different architectural dimensions.

## Correction / Supersession Boundary
`correction-supersession` is an adopted Attestation Type.

This does **not** make Correction a separate canonical Attestor object class.

Correction is a governed activity. Lifecycle and Versioning determine how canonical identity and state behave across change.

A materially changed Attestation assertion requires a new `ATT-YYYY-NNNN`.

A materially changed Trust Statement conclusion requires a new `TRST-YYYY-NNNN`.

## Reputation
Reputation is **not** an adopted Attestation Type.

Attestor does not establish:
- a generic reputation framework;
- a canonical reputation object;
- a reputation score;
- a universal trust score.

Attestor produces bounded Trust Statements.

## Historical Pre-Suite Categories
Earlier Attestor material explored categories such as:
- Claim Attestations;
- Record Attestations;
- Confidence Attestations;
- Reputation Attestations;
- Dispute Attestations;
- positive/negative/neutral/contextual “direction.”

These concepts are historical design inputs only. They are not part of the adopted controlled Attestation Type vocabulary unless separately represented through current Attestor architecture.

Support, contradiction, uncertainty, correction, and relationships are now handled through the appropriate Evaluation, Relationship, Lifecycle, Versioning, or other governed layers rather than an open-ended type system.

## Validation and Conformance
The controlled Attestation Type value must conform to the applicable schema/profile and controlled-value requirements.

Executable validation rules and final conformance mechanics remain implementation work.

## Status
**Attestation Type Architecture → Advanced Architecture established.**

The six controlled values are adopted.

Remaining work concerns executable validation, production profile requirements, and production proof—not selection of the Attestation Type vocabulary.

## Files
- `index.html` — public Attestation Types page.
- `README.md` — repository documentation.
