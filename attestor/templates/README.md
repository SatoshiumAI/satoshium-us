# Satoshium Attestor — Templates

## Path
`/attestor/templates/`

## Purpose
This directory preserves and reconciles the early Attestor template work.

Templates are practical authoring aids. They should reflect adopted architecture, but they do **not** independently establish canonical objects, identifiers, controlled values, lifecycle states, or validation rules.

## Canonical Responsibility
**Attestor → Trust Statement**

## Governing Principle
> **Reference does not transfer authority.**

## Foundational Relationship
`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

## Current Files
- `attestation-template.md`
- `evidence-attestation-template.md`
- `source-attestation-template.md`
- `correction-attestation-template.md`
- `trust-signal-template.md` — retained as a legacy, non-canonical template
- `index.html`

## Important Boundary
The June Templates README proposed templates for Evidence Records, Trust Records, Correction Records, Retraction Records, Relationship Records, reputation systems, confidence models, and trust networks. Those are not carried forward as adopted Attestor objects.

Templates must follow the architecture; they must not create it.

## Relationship to Schemas
`Architecture → Schema/Profile → Template → Governed Instance`

At the present stage, the schema/profile layer is still foundational/candidate architecture. Therefore these templates are also **candidate authoring profiles**, not production templates.

## Status
**Foundational template reconciliation complete. Operational templates remain deferred until Advanced Architecture establishes the necessary normative structures.**
