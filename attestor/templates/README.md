# Satoshium Attestor — Templates

**Path:** `/attestor/templates/`  
**Architecture Stage:** Advanced Architecture / Implementation Layer  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

This directory provides governed authoring formats derived from adopted Attestor architecture and applicable schemas/profiles.

Templates implement architecture. They do not create it.

`Architecture → Schema/Profile → Template → Governed Instance`

## Current Files

- `attestation-template.md` — core Attestation authoring template.
- `evidence-attestation-template.md` — profile for the adopted `evidence` Attestation Type.
- `source-attestation-template.md` — profile for the adopted `source-provenance` Attestation Type.
- `trust-statement-template.md` — authoring template for Attestor's canonical output.
- `correction-attestation-template.md` — governed correction/change worksheet; not a separate canonical object class.
- `trust-signal-template.md` — legacy historical artifact; not operational.
- `index.html` — public Templates landing page.

## Governing Architecture

Canonical object identities:

- Attestation → `ATT-YYYY-NNNN`
- Trust Statement → `TRST-YYYY-NNNN`

Canonical Attestation Types currently include:

- `identity`
- `evidence`
- `source-provenance`
- `verification-related`
- `relationship-condition`
- `correction-supersession`

Lifecycle states:

- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

Publication states:

- `unpublished`
- `published`

Evaluation Outcomes:

- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

## Important Boundaries

Evidence and Source / Provenance templates are now specialized Attestation profiles because the corresponding Attestation Types have been adopted.

Correction is not established as an independent canonical object class. The correction file is a governed change worksheet implementing Lifecycle and Versioning decisions.

Trust Signal remains non-canonical and non-operational.

A Trust Statement template is required because Trust Statement is Attestor's canonical institutional output.

## Authority

**Reference does not transfer authority.**

Source objects retain source authority. Attestor retains authority for its own Attestations, evaluations, and Trust Statements.

## Status

**Templates → Advanced architecture reconciled.**

Final machine serialization, exact schema cardinalities, executable validation, and production-specific forms must remain aligned with the normative Schemas and Validation specifications.
