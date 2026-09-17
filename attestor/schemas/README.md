# Satoshium Attestor — Schemas

## Path
`/attestor/schemas/`

## Purpose
This directory contains the structural schema layer through which adopted Attestor architecture is expressed for implementation, authoring, validation, and production use.

`Architecture → Schema/Profile → Template → Governed Instance`

Schemas implement adopted architecture. They do not independently create new canonical objects, authority, controlled values, or institutional responsibilities.

## Canonical Responsibility
**Attestor → Trust Statement**

## Governing Principle
> **Reference does not transfer authority.**

## Canonical Relationship
`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

## Files
- `attestation-schema.md` — structural schema for a canonical Attestation (`ATT-YYYY-NNNN`).
- `trust-statement-schema.md` — structural schema for a canonical Trust Statement (`TRST-YYYY-NNNN`).
- `evidence-attestation-schema.md` — specialized profile for the adopted `evidence` Attestation Type.
- `source-attestation-schema.md` — specialized profile for the adopted `source-provenance` Attestation Type.
- `correction-attestation-template.md` — governed correction/change profile used with Lifecycle and Versioning; not a separate canonical object class.
- `trust-signal-schema.md` — retained historical legacy artifact; Trust Signal is not a canonical Attestor object.
- `index.html` — public landing page.

## Canonical Objects

### Attestation
A governed, attributable assertion.

Identifier: `ATT-YYYY-NNNN`

### Trust Statement
A governed, attributable, bounded Attestor conclusion produced through Rule-Constrained Evaluation.

Identifier: `TRST-YYYY-NNNN`

> **Outcome ≠ Conclusion ≠ Trust Statement Identity**

## Adopted Attestation Types
- `identity`
- `evidence`
- `source-provenance`
- `verification-related`
- `relationship-condition`
- `correction-supersession`

Evidence and Source / Provenance are formal specialized Attestation profiles.

## Lifecycle and Publication
Lifecycle State:
- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

Publication State:
- `unpublished`
- `published`

> **Canonical Creation ≠ Lifecycle Activation ≠ Publication**

## Evaluation Outcomes
- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

## Provenance and Authority
Provenance modes:
- `direct`
- `referenced`
- `derived`

Authority contexts:
- `Attestor`
- `Suite-source`
- `external-source`

> **Reference does not transfer authority.**

## Relationships
- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

Relationship direction and semantics are governed by `/attestor/relationships/`.

## Correction and Versioning
Correction is not established as a separate canonical object class merely because a correction profile exists here.

Lifecycle and Versioning govern change behavior.

A bounded change may preserve canonical identity through governed versioning when essential institutional meaning remains intact.

A materially changed Attestation assertion requires a new `ATT-YYYY-NNNN`.

A materially changed Trust Statement conclusion requires a new `TRST-YYYY-NNNN`.

Prior governed states remain traceable.

## Trust Signal
`trust-signal-schema.md` remains only as a historical design artifact.

Trust Signal is not a canonical Attestor object, identifier family, score, reputation mechanism, or production schema.

Beacon separately owns **Discovery Signal / Discovery Metadata**.

## Validation and Conformance
`Object + Applicable Normative Requirements → Validation → Validation Result`

> **Validation ≠ Evaluation**

> **Validation ≠ Conformance**

> **Valid ≠ Published**

Executable validation rules and final machine serialization must remain aligned with `/attestor/validation/` and `/attestor/conformance/`.

## Status
**Schema Architecture → Advanced Architecture established.**

The schema layer now reflects adopted Attestor architecture. Executable machine validation, serialization details, and production-instance requirements remain governed by the corresponding implementation and production specifications.
