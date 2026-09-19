# Attestation Schema — Advanced Architecture

## Purpose
This document defines the structural schema for a canonical **Attestation** within Satoshium Attestor.

An Attestation is a governed, attributable assertion used by Satoshium Attestor to express a bounded statement about a subject, record, relationship, condition, event, or other trust-relevant matter.

It establishes the governed assertion presented for evaluation; it is not Attestor's resulting institutional conclusion.

## Canonical Context
**Attestor → Trust Statement**

`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

> **Attestation → governed, attributable assertion**

> **Trust Statement → governed, attributable, bounded Attestor conclusion**

## Canonical Identifier
Attestations use:

`ATT-YYYY-NNNN`

`YYYY` is the canonical creation year and `NNNN` is the four-digit sequence within the object family and year. The identifier is assigned at canonical creation and must not be reused or reassigned.

Canonical identifier and version identity remain distinct:
- canonical identifier → which governed Attestation;
- version identity → which governed state of that Attestation.

## Structural Model
```yaml
attestation_identifier: ATT-YYYY-NNNN
attestation_type:

lifecycle_state:
publication_state:

attesting_authority:
  identifier:
  authority_context:

subject:
  identifier:
  type:

assertion:
scope:

evidence_references:
  -
source_references:
  -
governed_references:
  -

provenance:
  mode:
  source_or_origin:
  relevant_time_or_state:
  derivation_basis:
  material_limitations:

relationships:
  -

created_at:
updated_at:
version_identity:

limitations:
  -
uncertainty:
  -
notes:
```

This establishes the canonical structural concepts required for validation. Exact machine serialization, field cardinalities, timestamp syntax, identifier-registry mechanics, and profile-specific requirements remain implementation work governed by executable Validation.

The model must not be used to invent unavailable or inapplicable information.

## Core Structural Requirements
A canonical Attestation must be capable of preserving:
- canonical Attestation identity;
- Attestation Type;
- lifecycle state;
- publication state;
- responsible Attesting Authority;
- subject identity/context;
- bounded assertion;
- scope;
- Evidence, source, and governed references where applicable;
- provenance;
- relevant time/source state where material;
- governed relationships;
- creation/update context;
- version identity;
- material limitations; and
- uncertainty where applicable.

## Attestation Types
Controlled values:
- `identity`
- `evidence`
- `source-provenance`
- `verification-related`
- `relationship-condition`
- `correction-supersession`

Type classification does not itself establish Eligibility, transfer authority, establish truth, determine Evaluation Outcome, determine publication, create a Trust Statement, or predetermine Attestor's conclusion.

Specialized profiles may impose additional requirements while remaining subordinate to this base schema.

## Lifecycle and Publication
Lifecycle states:
- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

Publication states:
- `unpublished`
- `published`

`review` and `correction` are governed activities, not lifecycle states. `inactive` is not a canonical lifecycle state.

A canonically created Attestation begins in `draft` unless a formally adopted production procedure establishes another valid creation-state rule.

> **Canonical Creation ≠ Lifecycle Activation ≠ Publication**

Publication does not enlarge the assertion, scope, authority, provenance, or evidentiary meaning.

## Authority
Every Attestation must preserve sufficient authority context to identify the party or governed source responsible for the assertion.

Attesting Authority is distinct from Referenced Authority and Attestor Authority.

> **Reference does not transfer authority.**

> **Authority ≠ Eligibility ≠ Evaluation Outcome**

> **Attribution ≠ Adoption**

## Subject, Assertion, and Scope
The subject must be sufficiently identified or described and remain distinguishable from the Attestation, source objects, Attesting Authority, and resulting Trust Statement.

The assertion is the governed statement made by the Attesting Authority. It remains distinct from Evidence, source material, Evaluation Outcome, Attestor's bounded conclusion, and the resulting Trust Statement.

A materially different assertion requires a new canonical Attestation.

Scope bounds the assertion and may include subject, jurisdiction, time, state, record, event, relationship, or other material context. Scope must not be silently broadened.

## Evidence and Governed References
An Attestation may reference Evidence, source objects, and other governed objects where applicable.

Reference alone does not establish Eligibility, support, derivation, authority transfer, truth, Evaluation Outcome, or a Trust Statement.

> **Availability ≠ Eligibility**

> **Authority ≠ Eligibility**

> **Reference ≠ Eligibility**

> **Eligible Here ≠ Eligible Everywhere**

## Provenance
Controlled provenance modes:
- `direct`
- `referenced`
- `derived`

Provenance must preserve sufficient traceability to understand assertion origin and entry into Attestor. Where material, preserve source/origin, stable reference, mode, authority context, relevant time/state, relationship, derivation basis, limitations, and historical context.

> **Source State at Evaluation ≠ Later Source State**

Later source-state change does not silently rewrite existing provenance; material change may trigger governed Review.

## Relationships
Controlled relationship values:
- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

Direction must preserve source → target meaning.

> **supports ≠ supported**

> **Reference ≠ Derivation**

> **Reference ≠ Support**

> **Connection does not imply identity.**

A relationship alone does not establish Eligibility, authority transfer, or Evaluation Outcome.

## Versioning and Governed Change
A bounded correction, clarification, metadata repair, provenance clarification, or other permitted revision that does not materially alter essential institutional meaning may preserve the canonical identifier through governed versioning.

A materially different assertion requires a **new canonical Attestation** and new `ATT-YYYY-NNNN` identifier.

Prior governed states must remain traceable. Where a successor replaces a prior Attestation because essential institutional meaning changed, the applicable `supersedes` relationship preserves continuity.

Correction explains why governed change occurs. Versioning determines whether the change stays within the same canonical identity or requires a successor.

## Validation
`Attestation → Applicable Validation Rules → Validation Result`

Validation may test representation/syntax, structure, controlled semantics, relationships, provenance/authority, lifecycle/versioning, and applicable normative rules.

Validation does not decide substantive truth, Evidence sufficiency, Eligibility for a particular evaluation, or Evaluation Outcome.

> **Machine-readable ≠ Valid**

> **Validation ≠ Evaluation**

> **Validation ≠ Eligibility**

> **Validation ≠ Conformance**

> **Valid ≠ Published**

## Conformance
Conformance is separately determined against a declared requirements set.

> **Validation supports Conformance.**

> **Validation ≠ Conformance.**

## Explicit Boundaries
An Attestation is not:
- a declaration of universal truth;
- Attestor's final bounded conclusion;
- a Trust Statement;
- a generic reputation record or trust score;
- a confidence percentage;
- a certification merely because certification is referenced;
- a verification result merely because verification is referenced;
- a Beacon Discovery Signal;
- an automatic Eligibility determination;
- an automatic Evaluation Outcome;
- an automatic transfer of source authority; or
- a guarantee of permanent correctness.

## Specialized Profile Boundary
The base schema governs all canonical Attestations.

Specialized profiles, including `evidence` and `source-provenance`, may refine requirements but must not contradict the base schema or introduce competing identifiers, lifecycle states, authority rules, provenance semantics, or relationship vocabularies.

The June-era Evidence and Source documents must be reconciled as specialized profiles before executable validation uses them.

The legacy Trust Signal schema is not an Attestation profile and is not canonical.

Correction architecture is governed by adopted Corrections, Lifecycle, Versioning, and relationship architecture; a correction template does not establish a separate canonical object class.

## Implementation Boundary
Advanced Architecture now establishes the canonical Attestation object model and semantic requirements.

The following remain implementation-level decisions:
- selected machine serialization;
- exact required/optional field cardinalities;
- timestamp syntax;
- exact executable identifier expression;
- identifier allocation/collision mechanics;
- canonical reference serialization;
- relationship serialization;
- validation report serialization;
- final Validation Result vocabulary; and
- specialized profile deltas.

These decisions must remain subordinate to this schema and established Attestor architecture.

## Status
**Attestation Schema → Advanced Architecture established.**

The former Foundational Candidate Profile has been normalized to completed Attestor architecture.

This schema may now be used with the Trust Statement Schema and Attestor Validation Rule Catalog to define exact machine contracts and executable validation behavior.
