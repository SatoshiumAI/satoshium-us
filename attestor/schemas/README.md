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
- `attestation-schema.md` — canonical structural schema for a governed Attestation (`ATT-YYYY-NNNN`), including authority, provenance, lifecycle, publication, relationships, versioning, and validation boundaries; exercised by `ATT-2026-0001`.
- `trust-statement-schema.md` — canonical structural schema for a Trust Statement (`TRST-YYYY-NNNN`); exercised by `TRST-2026-0001`.
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

Evidence and Source / Provenance are adopted Attestation Types. Their specialized profile documents remain profile-specific contracts and must remain aligned with the canonical base Attestation schema before specialized executable validation or production use. The first production operation proves the base ATT/TRST contracts; it does not by itself prove every specialized profile.

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

The base Attestation and Trust Statement schemas provide the canonical object contracts used by production instances. Their applicable machine representation and validation requirements are now exercised through the production objects and Validator v0.5, while profile-specific and future optional combinations remain subject to their governing schemas and rules.

## First Production Schema Demonstration

The first controlled production operation exercised the canonical base Attestation and Trust Statement contracts through:

- `ATT-2026-0001`; and
- `TRST-2026-0001`.

The final canonical representations exercised, as applicable:

- canonical identifier;
- object class;
- version `V1.0`;
- lifecycle state `active`;
- publication state `published`;
- authority/provenance context;
- scope;
- limitations;
- structured relationships;
- Attestation assertion; and
- Trust Statement conclusion and Evaluation Outcome.

Both final active/published representations passed Validator v0.5 with no mandatory failure or mandatory `not-tested` result.

The production operation also exercised relationship-serialization remediation. Early descriptive relationship strings were corrected to structured relationship blocks with explicit relationship type and target identifier while canonical identity and substantive meaning remained unchanged.

**Base ATT / TRST Schema Architecture → DEMONSTRATED IN PRODUCTION**

## Schema and Validation Boundary

Schemas define structural contracts. Validation tests applicable normative requirements against an object and its execution context.

The first production operation demonstrated both without collapsing them.

`Schema → Structural Contract`

`Validation → Applicable Rule Testing`

`Conformance → Separate Determination`

`Evaluation → Separate Institutional Act`

Therefore:

`Validation ≠ Evaluation`

`Validation ≠ Conformance`

`Valid ≠ Published`

`Schema Representation ≠ Universal Truth`

## Implementation Boundary

Production has exercised a concrete canonical representation for the first ATT/TRST objects, including version, lifecycle, publication, and structured relationships. That implementation does not freeze every future serialization or optional profile choice.

Implementation-level decisions remain subordinate to established Attestor architecture and the canonical base schemas, including where applicable:

- serialization choices not already fixed by a governing contract;
- profile-specific required/optional cardinalities;
- identifier allocation and collision mechanics;
- specialized profile deltas;
- optional or future relationship combinations;
- Validation Result/report representation changes; and
- future production-instance requirements.

A production-exercised representation is evidence of operational capability, not permission for implementations to redefine canonical architecture.

## Status

**Schema Architecture → Established and Production-Proven**

- Base Attestation Schema → established and production-exercised
- Base Trust Statement Schema → established and production-exercised
- canonical ATT/TRST structured representation → exercised
- production version identity → exercised
- lifecycle / publication representation → exercised
- structured relationships → exercised
- relationship serialization correction → exercised
- executable validation alignment → demonstrated with Validator v0.5
- Evidence / Source-Provenance specialized profiles → remain profile-specific reconciliation work unless separately completed
- Correction / Change profile → governed change structure; not separate canonical object class
- Trust Signal schema → legacy / noncanonical
- production proof → **ESTABLISHED for base ATT/TRST contracts**

## Continuing Schema Governance

Production proof is bounded to the canonical base object contracts and structures actually exercised.

It does not establish that:

- every specialized Attestation profile has been production-tested;
- every optional field combination is proven;
- every future serialization is automatically valid;
- every relationship type is valid for every source/target pair; or
- schema validity determines Evaluation Outcome, Conformance, Publication, or truth.

`Architecture → Schema/Profile → Template → Governed Instance`

**Schemas implement architecture. They do not create it.**
