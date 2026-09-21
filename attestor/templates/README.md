# Satoshium Attestor — Templates

**Path:** `/attestor/templates/`  
**Current Stage:** Operational Implementation Layer  
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

## First Production Template Demonstration

The first controlled production operation exercised the core authoring structures represented by the Attestation and Trust Statement templates through:

- `ATT-2026-0001`; and
- `TRST-2026-0001`.

The operation demonstrated:

- core Attestation authoring structure → exercised;
- core Trust Statement authoring structure → exercised;
- `verification-related` Attestation Type → exercised by `ATT-2026-0001`;
- governed correction/change workflow → exercised during relationship remediation;
- canonical identity remained distinct from template/authoring structure; and
- lifecycle activation and publication remained separate governed acts after object creation.

The operation does **not** independently establish production proof for every specialized template or Attestation Type.

In particular:

- Evidence Attestation specialized template → not independently production-proven by this operation;
- Source / Provenance specialized template → not independently production-proven by this operation;
- Trust Signal template → legacy and non-operational.

**Core Template Architecture → DEMONSTRATED IN PRODUCTION**

## Template and Canonical Object Boundary

A template is an authoring aid, not a canonical object.

`Template → Authoring Aid`

`Completed Draft → Candidate Governed Representation`

`Canonical Creation → Canonical Object + Identifier`

Therefore:

`Template ≠ Canonical Object`

`Template Completion ≠ Lifecycle Activation`

`Template Completion ≠ Publication`

A template cannot establish a new canonical object class, controlled value, authority, or institutional responsibility merely by containing a field or authoring path.

## Status

**Templates → Established and Production-Proven for Core Authoring Structures**

- core Attestation template structure → production-exercised
- core Trust Statement template structure → production-exercised
- `verification-related` Attestation path → production-exercised
- governed correction/change worksheet function → operationally demonstrated
- template / canonical-object distinction → preserved
- Evidence specialized template → established profile; not independently production-proven here
- Source / Provenance specialized template → established profile; not independently production-proven here
- Trust Signal template → legacy / non-operational
- production proof → **ESTABLISHED for core ATT/TRST authoring structures**

## Continuing Template Governance

Templates remain subordinate to:

- canonical architecture;
- applicable schemas/profiles;
- controlled values;
- authority and provenance rules;
- Lifecycle and Versioning;
- Validation and Conformance;
- Publication; and
- Methodology.

Production use of one template path does not validate every other template path.

`Architecture → Schema/Profile → Template → Governed Instance`

**Templates implement architecture. They do not create it.**

