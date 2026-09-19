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
- `attestation-schema.md` — Advanced Architecture structural schema for a canonical Attestation (`ATT-YYYY-NNNN`), including authority, provenance, lifecycle, publication, relationships, versioning, and validation boundaries.
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

Evidence and Source / Provenance are adopted Attestation Types. Their existing June-era schema documents remain candidate profiles and must be reconciled to the Advanced Architecture base Attestation schema before they are used for executable validation.

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

Current Validation implementation artifacts include:

- `/attestor/validation/attestor-validation-requirements.md` — implementation bridge from established architecture to executable validation requirements.
- `/attestor/validation/attestor-validation-rules.md` — numbered `VAL-*` rule catalog separating machine, conditional, review-dependent, and deferred validation requirements.

The base Attestation and Trust Statement schemas now provide the canonical object contracts from which exact machine serialization and field cardinalities can be defined.

## Implementation Boundary
The following remain implementation-level decisions rather than unresolved architecture:

- selected machine serialization;
- exact required/optional field cardinalities;
- timestamp syntax;
- exact executable identifier expressions;
- identifier allocation and collision mechanics;
- canonical reference and relationship serialization;
- Validation Result vocabulary and report serialization;
- specialized profile deltas; and
- production-instance requirements.

These decisions must remain subordinate to the established Attestor architecture and the canonical base schemas.

## Status
**Schema Architecture → Advanced Architecture established.**

**Base Attestation Schema → Advanced Architecture normalized.**

**Base Trust Statement Schema → Advanced Architecture established.**

The schema layer now reflects the canonical ATT/TRST object model. The next implementation work is exact machine-contract definition and executable validation behavior; the Evidence and Source / Provenance candidate profiles still require reconciliation before specialized executable validation.
