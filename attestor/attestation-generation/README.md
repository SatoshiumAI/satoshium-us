# Satoshium Attestor — Attestation Generation

## Page
`/attestor/attestation-generation/`

## Purpose
This page defines the governed architecture for forming a canonical **Attestation** within Satoshium Attestor.

An Attestation is a governed, attributable, bounded assertion.

Attestation Generation concerns formation of that assertion from eligible governed inputs while preserving:
- purpose;
- subject;
- assertion;
- Attestation Type;
- scope;
- Attesting Authority;
- eligible governed references;
- provenance;
- relevant source state;
- relationships;
- lifecycle context;
- source authority.

It does **not** collapse Attestation formation into Trust Statement generation.

## Governing Principle
> **Reference does not transfer authority.**

## Canonical Model
`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

### Attestation
A governed, attributable assertion.

### Trust Statement
A governed, attributable, bounded Attestor conclusion.

## Canonical Identifier
A canonical Attestation uses:

`ATT-YYYY-NNNN`

The identifier is assigned at canonical creation and is not reused or reassigned.

Canonical identity and version identity remain distinct.

## Adopted Attestation Types
- `identity`
- `evidence`
- `source-provenance`
- `verification-related`
- `relationship-condition`
- `correction-supersession`

The Attestation Type classifies the assertion. It does not transfer source authority or predetermine an Evaluation Outcome.

## Generation Sequence
The established institutional formation sequence is:

`Purpose Established → Subject Identified → Assertion Defined → Scope Bounded → Eligible Inputs Referenced → Provenance Preserved → Attesting Authority Attributed → Attestation Formed`

This is the governed institutional path.

Exact executable validation order, machine serialization, duplicate-detection mechanics, and production procedures remain implementation work.

## Purpose Established
The purpose for forming the Attestation must be sufficiently clear to determine the assertion, scope, and relevant potential inputs.

## Subject Identified
The subject must be identifiable within the applicable governed context.

## Assertion Defined
The Attestation states the bounded proposition being asserted rather than silently copying a source object.

## Scope Bounded
Scope preserves the conditions and limitations within which the assertion applies.

## Eligible Inputs Referenced
Potential inputs are admitted through the established Eligibility architecture.

> **Availability ≠ Eligibility**

> **Authority ≠ Eligibility**

> **Reference ≠ Eligibility**

## Provenance Preserved
Applicable provenance is preserved using the adopted modes:
- `direct`
- `referenced`
- `derived`

The source or origin, derivation basis where applicable, relevant source state, and material limitations remain traceable.

## Attesting Authority Attributed
The Attestation identifies the **Attesting Authority** responsible for the governed assertion.

Attesting Authority remains distinct from:
- Referenced Authority;
- Attestor Authority.

> **Attribution ≠ Adoption**

## Attestation Formed
Once applicable structural, type, scope, authority, provenance, eligibility, and relationship requirements are satisfied, an Attestation may be canonically created and assigned an `ATT-YYYY-NNNN`.

Canonical creation does not itself establish:
- `active` Lifecycle State;
- `published` Publication State;
- a favorable Evaluation Outcome;
- a Trust Statement.

## Lifecycle
Adopted Lifecycle States:
- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

A newly formed Attestation begins in governed `draft` state unless a production procedure explicitly governs a different valid transition.

Review and correction are activities rather than lifecycle states.

## Publication
Publication is separate from Attestation formation.

Adopted Publication States:
- `unpublished`
- `published`

> **Canonical Creation ≠ Lifecycle Activation ≠ Publication**

## Potential Governed Inputs
Potential source classes include:
- Atlas Authoritative Intelligence;
- Navigator Workflow Definition / Orchestration;
- Certifier Certification Packages;
- Satoshium Registry Records;
- Chronicle Entries;
- Anchor Integrity References;
- Beacon Discovery Signals / Discovery Metadata;
- other eligible governed sources.

No source class is universally required merely because Attestor can reference it.

## Source-to-Attestation Boundary
A source object remains its own canonical object.

Attestor does not transform a Certification Package, Registry Record, Chronicle Entry, Integrity Reference, Discovery Signal, or other source object into an Attestation.

The Attestation is Attestor's own governed assertion.

## Validation
Formation and Validation are distinct.

`Attestation + Applicable Normative Requirements → Validation → Governed Validation Result`

> **Machine-readable ≠ Valid**

> **Validation ≠ Evaluation**

> **Validation ≠ Eligibility**

Exact executable validation rules and final Validation Result vocabulary remain implementation work.

## Attestation Generation vs Trust Statement Generation
Attestation Generation forms the assertion.

Rule-Constrained Evaluation evaluates the Attestation and eligible governed inputs.

Trust Statement generation forms the bounded Attestor conclusion when applicable methodology and evaluation requirements are satisfied.

> **Outcome ≠ Conclusion ≠ Trust Statement Identity**

## Correction and Material Change
`correction-supersession` is an adopted Attestation Type, but Correction remains an activity rather than a separate canonical object class.

A bounded revision may preserve canonical identity when essential institutional meaning remains intact.

A materially changed assertion requires a new `ATT-YYYY-NNNN`.

## Status
**Attestation Generation Architecture → Advanced Architecture established.**

Remaining work is implementation and production proof:
- exact machine serialization;
- executable validation;
- duplicate-detection mechanics if required;
- production-specific generation procedures;
- production evidence and first-operation proof.

## Files
- `index.html` — public Attestation Generation page.
- `README.md` — repository documentation.
