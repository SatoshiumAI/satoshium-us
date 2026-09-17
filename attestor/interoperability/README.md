# Satoshium Attestor — Interoperability

## Page
`/attestor/interoperability/`

## Purpose
This page defines the established interoperability architecture for **Satoshium Attestor**.

Interoperability is **semantic and authority-preserving compatibility** across institutional boundaries.

It allows governed information to participate in Attestor without losing the meaning, identity, provenance, scope, relevant state, relationships, limitations, or authority necessary to interpret that information correctly.

## Governing Principle
> **Reference does not transfer authority.**

## Canonical Responsibility
**Attestor → Trust Statement**

Interoperability supports Attestor's ability to produce governed Trust Statements without absorbing the canonical responsibilities of source institutions.

## Interoperability vs Integration
> **Interoperability → Preserve Meaning and Authority**

> **Integration → Connect and Exchange**

Interoperability governs what must remain intact across a boundary.

Integration governs the operational connection through which governed information is obtained or exchanged.

## Reference Context
The established Attestor Reference Profile context is:

`Identifier + Source + Provenance + Type + Status + Scope + Relationship + Authority`

Additional relevant state, version identity, limitations, and source-specific context are preserved where applicable.

Exact machine serialization remains implementation work.

## Reference Rather Than Duplicate
Where an authoritative source object already exists, Attestor should normally reference it rather than silently duplicate it as an Attestor-owned canonical object.

The governed relationship is:

`Source Object → Governed Reference → Eligibility Determination → Attestation / Evaluation Basis → Rule-Constrained Evaluation → Trust Statement`

The source object remains authoritative in its originating institution.

## Eligibility
Interoperability does not itself establish Eligibility.

> **Availability ≠ Eligibility**

> **Authority ≠ Eligibility**

> **Reference ≠ Eligibility**

> **Eligible Here ≠ Eligible Everywhere**

## Authority
Attestor preserves the distinction among:
- Attesting Authority;
- Referenced Authority;
- Attestor Authority.

> **Attribution ≠ Adoption**

A source's authority is not transferred merely because its object is interoperable with Attestor.

## Provenance
Adopted provenance modes:
- `direct`
- `referenced`
- `derived`

Interoperability must preserve enough provenance to prevent Evaluation from becoming a provenance break.

## Relationships
Adopted relationship values:
- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

> **Connection does not imply identity.**

> **Reference ≠ Support**

> **Reference ≠ Derivation**

## Source State and Change
Attestor preserves the relevant source state used during Evaluation.

> **Source State at Evaluation ≠ Later Source State**

A material source-state change may trigger Review:

`Material Source-State Change → Review`

Review does not automatically determine:
- correction;
- withdrawal;
- supersession;
- lifecycle transition;
- new Attestation;
- new Trust Statement.

Attestor responds under its own Lifecycle, Versioning, Correction, and Evaluation architecture.

## External Interoperability
External governed information may participate when the applicable requirements can be established, including:
- source identity;
- authority;
- provenance;
- scope;
- relevant state;
- permitted use;
- Eligibility;
- applicable Validation.

External interoperability does not transfer external authority to Attestor.

No particular external standard, protocol, API, or transport is required by the institutional architecture.

## Suite Relationships
- **Atlas → Authoritative Intelligence**
- **Navigator → Workflow Definition / Orchestration**
- **Certifier → Certification Package**
- **Registry → Satoshium Registry Record**
- **Chronicle → Chronicle Entry**
- **Anchor → Integrity Reference**
- **Beacon → Discovery Signal / Discovery Metadata**
- **Attestor → Trust Statement**

Each institution retains authority for its canonical objects.

## Trust Signals and Reputation
Attestor does not establish Trust Signal as a canonical Attestor object.

Attestor does not establish a generic reputation object, reputation score, confidence percentage, or trust score.

Trust-relevant considerations are handled through the established Attestation, Evidence, Eligibility, Provenance, Relationships, Evaluation, limitations, uncertainty, and Trust Statement architecture.

## Validation and Conformance
Interoperable references and resulting Attestor objects remain subject to applicable Validation and Conformance requirements.

> **Validation ≠ Eligibility**

> **Validation ≠ Evaluation**

> **Validation ≠ Conformance**

Exact executable validation and conformance mechanics remain implementation work.

## Implementation-Open Matters
The following remain implementation or production concerns rather than unresolved Advanced Architecture:
- exact machine serialization of references;
- concrete object-resolution mechanisms;
- source-change notification/detection mechanisms;
- API and transport formats;
- authentication and authorization where required;
- external protocol adapters;
- executable validation;
- conformance tests;
- reference vectors.

## Status
**Interoperability → Advanced Architecture reconciled.**

The former posture that reference fields, relationships, source-state handling, external Eligibility, Validation, and material-change treatment were wholly deferred to Advanced Architecture is no longer current.

## Files
- `index.html` — public Interoperability page.
- `README.md` — repository documentation.
