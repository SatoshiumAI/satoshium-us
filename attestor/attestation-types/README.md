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

Executable Validation and Conformance are now operational. The first production Attestation used the controlled value `verification-related`; its final production representation passed Validator v0.5 and the production Attestation received a `conformant` Conformance outcome.

Validation and Conformance do not determine the Attestation Type and do not replace Evaluation.

## First Production Attestation-Type Demonstration

The first controlled production operation exercised the adopted Attestation Type vocabulary through:

`ATT-2026-0001 → verification-related`

The classification was appropriate because the bounded assertion concerned the canonical identity, attributable Certifier origin, relevant certification state, and traceable Suite relationships of `SC-CERT-2026-0001`.

The classification did **not** transfer Certifier authority to Attestor and did not convert the Attestation into a new certification.

The production operation preserved the following distinctions:

`Attestation Type ≠ Source Object Type`

`Attestation Type ≠ Eligibility`

`Attestation Type ≠ Evaluation Outcome`

`Attestation Type ≠ Relationship Type`

`verification-related ≠ Attestor Certification Authority`

The operation subsequently produced the Evaluation Outcome `supported`, demonstrating that classification and outcome remained separate governed dimensions.

**Attestation Type Architecture → DEMONSTRATED IN PRODUCTION**

Production proof is value-specific. The first operation exercised `verification-related`; it did not independently production-test the other five adopted Attestation Types.

## Status
**Attestation Type Architecture → Established and Production-Proven**

- controlled Attestation Type vocabulary → established
- `verification-related` → production-exercised through `ATT-2026-0001`
- classification / source-authority boundary → demonstrated
- Type / Eligibility distinction → demonstrated
- Type / Evaluation Outcome distinction → demonstrated
- Type / Relationship distinction → preserved
- executable Validation → exercised
- Conformance → exercised
- `identity` → established; not independently production-tested
- `evidence` → established; not independently production-tested
- `source-provenance` → established; not independently production-tested
- `relationship-condition` → established; not independently production-tested
- `correction-supersession` → established; not independently production-tested
- reputation Attestation Type → not adopted
- production proof → **ESTABLISHED for `verification-related`**

## Continuing Attestation-Type Governance

Production use of one controlled type does not imply that every Attestation Type has been production-tested.

New Attestation Types still require governed architectural change.

A type remains classification of the Attestation assertion only.

`Type ≠ Eligibility`

`Type ≠ Evaluation Outcome`

`Type ≠ Relationship`

`Type ≠ Source Authority`

**Reference does not transfer authority.**

## Files
- `index.html` — public Attestation Types page.
- `README.md` — repository documentation.
