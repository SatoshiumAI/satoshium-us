# Satoshium Attestor — Attestations

## Page
`/attestor/attestations/`

## Purpose
This page defines the canonical **Attestation** object within Satoshium Attestor and serves as the public entry point for published Attestations.

## Definition
An **Attestation** is a governed, attributable assertion used by Satoshium Attestor to express a bounded statement about a subject, record, relationship, condition, event, or other trust-relevant matter.

## Canonical Identifier
`ATT-YYYY-NNNN`

The identifier is assigned at canonical creation and is not reused or reassigned.

## Canonical Model
`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

> **Attestation → governed, attributable assertion**

> **Trust Statement → governed, attributable, bounded Attestor conclusion**

## Adopted Attestation Types
- `identity`
- `evidence`
- `source-provenance`
- `verification-related`
- `relationship-condition`
- `correction-supersession`

> **Type ≠ Eligibility**

> **Attestation Type ≠ Evaluation Outcome**

> **Type does not transfer authority.**

## Core Structure
An Attestation preserves, as applicable:
- canonical identifier;
- Attestation Type;
- Attesting Authority;
- subject;
- assertion;
- scope;
- eligible governed references;
- provenance;
- relationships;
- Lifecycle State;
- Publication State;
- timestamps;
- version identity;
- limitations / notes.

Canonical machine-readable serialization is implemented for production Attestations.

## Authority
The Attestation identifies its **Attesting Authority**.

Referenced Authority remains distinct.

> **Reference does not transfer authority.**

> **Attribution ≠ Adoption**

## Evidence
Evidence and authoritative references may participate as eligible governed inputs.

Evidence is not the Attestation.

> **Availability ≠ Eligibility**

> **Authority ≠ Eligibility**

> **Reference ≠ Eligibility**

## Provenance
Adopted provenance modes:
- `direct`
- `referenced`
- `derived`

## Relationships
Adopted relationships:
- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

> **supports ≠ supported**

## Lifecycle
Adopted Lifecycle States:
- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

Correction and review are activities rather than lifecycle states.

## Publication
Adopted Publication States:
- `unpublished`
- `published`

> **Canonical Creation ≠ Lifecycle Activation ≠ Publication**

## Versioning and Material Change
A bounded revision may preserve canonical identity when essential institutional meaning remains intact.

A materially changed assertion requires a new `ATT-YYYY-NNNN`.

## Trust Statement Relationship
An Attestation is not the final Attestor conclusion.

It participates in Rule-Constrained Evaluation. A resulting bounded conclusion, when canonically formed, is represented by a separate `TRST-YYYY-NNNN`.

> **Outcome ≠ Conclusion ≠ Trust Statement Identity**

## Published Attestations
### ATT-2026-0001
**Active · Published · V1.0**

First canonical production Attestation of Satoshium Attestor.

Subject: `SC-CERT-2026-0001`

Canonical public record:

`/attestor/attestations/ATT-2026-0001/`

## Status
**Attestations → Operational production capability demonstrated.**

Satoshium Attestor has created, governed, validated, reviewed, conformance-tested, activated, and published its first canonical production Attestation.

Operational status does not make every future Attestation automatically valid, conformant, active, published, or correct. Each object remains subject to applicable Attestor governance.

## Files
- `index.html` — public Attestations page.
- `README.md` — repository documentation.
- `ATT-2026-0001/` — first canonical published production Attestation.
