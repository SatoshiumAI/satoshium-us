# Satoshium Attestor — Schemas

## Path
`/attestor/schemas/`

## Purpose
This directory preserves the early Attestor schema work while reconciling it with the current foundational architecture.

The June files contained useful structural candidates, but they also prematurely treated several conceptual objects, identifiers, controlled values, lifecycle states, confidence indicators, and trust signals as though they were already adopted technical standards.

They are therefore retained here as **foundational schema profiles / candidate structures**, not final normative schemas.

## Canonical Responsibility
**Attestor → Trust Statement**

## Governing Principle
> **Reference does not transfer authority.**

## Foundational Relationship
`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

## Files
- `attestation-schema.md` — candidate structural profile for an Attestation.
- `evidence-attestation-schema.md` — candidate specialization for an evidence-related Attestation.
- `source-attestation-schema.md` — candidate specialization for a source/provenance-related Attestation.
- `correction-attestation-template.md` — candidate correction/change profile for Attestor-owned Attestations.
- `trust-signal-schema.md` — historical June schema retained as a **non-canonical legacy candidate**; no Trust Signal object is adopted.
- `index.html` — public landing page for this schema area.

## Important Architectural Boundary
These files do not establish final:
- identifier formats;
- required/optional field sets;
- controlled vocabularies;
- status values;
- confidence scales;
- scoring;
- lifecycle models;
- validation sequences;
- machine schemas;
- conformance requirements.

Those belong to advanced architecture.

## Trust Signal Schema
The June `trust-signal-schema.md` is architecturally problematic because the reconciled foundation does not recognize **Trust Signal** as Attestor's canonical object.

It is retained rather than silently deleted because it is part of the historical design record. Its candidate fields may later inform evaluation-context architecture, but the object itself is **not adopted**.

Beacon's **Discovery Signal** remains a separate canonical Beacon object.

## Correction Template
The correction template is also not yet a final independent object model. The foundational Corrections work left open whether correction should be represented as:
- an Attestation Type;
- a lifecycle/versioning operation;
- a governed change object/profile;
- some combination determined by advanced architecture.

Accordingly, the template is preserved as a candidate profile without canonizing `Correction Attestation` as a separate object class.

## Whole-Foundation Review
The review should determine:
1. which schema candidates remain architecturally useful;
2. whether Evidence and Source profiles should be formal Attestation Type profiles;
3. how Attesting Authority is represented;
4. whether `statement` becomes `assertion` or another canonical field name;
5. how Scope and Provenance become structurally mandatory;
6. how evaluation relates to Trust Statement generation;
7. whether any legacy Trust Signal fields belong in evaluation context;
8. how corrections/versioning should actually be modeled.

## Status
**Foundational schema reconciliation complete; normative schema design deferred to Advanced Architecture.**
