# Satoshium Attestor — Relationships

**Path:** `/attestor/relationships/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

Relationships define governed connections among:

- Attestations;
- Trust Statements;
- evidence;
- source objects;
- prior statements;
- evaluations; and
- canonical Suite objects.

A relationship connects objects without merging their identity, provenance, lifecycle, ownership, or authority.

## Governing Principles

**Connection does not imply identity.**

**Reference does not transfer authority.**

## Canonical Relationship Vocabulary

### `supports`

The source object provides material support to the target assertion, evaluation, or conclusion.

A `supports` relationship does not itself determine an evaluation outcome.

### `references`

The source object explicitly identifies or cites the target object without implying derivation, support, or authority transfer.

### `derived-from`

The source object was materially produced from the target object or governed basis.

### `evaluates`

The source evaluation acts upon the target Attestation/assertion.

### `results-in`

The source evaluation produces the target Trust Statement.

### `supersedes`

The source object becomes the governed successor to the target prior object.

### `corrects`

The source object or governed change addresses an error or material defect in the target prior object.

### `related-to`

A bounded non-specific relationship used only where a more precise canonical relationship does not apply.

## Directionality

Normative relationships are interpreted from source to target.

Examples:

`Evaluation → evaluates → Attestation`

`Evaluation → results-in → Trust Statement`

`New Object → supersedes → Prior Object`

`Corrective Object / Change → corrects → Prior Object`

Relationships must not be assumed symmetric unless explicitly defined that way.

## Core Attestor Relationship Chain

Conceptually:

`Attestation → references → Eligible Governed Inputs`

`Evaluation → evaluates → Attestation`

`Evaluation → results-in → Trust Statement`

`Trust Statement → derived-from → Governed Evaluation Basis`

Each object remains distinct.

## Evidence Relationships

Evidence remains supporting material or an authoritative reference unless later architecture explicitly establishes another canonical object model.

Evidence relationships may show material support or other evaluation context without converting evidence into an Attestation or Trust Statement.

## Support vs. Evaluation Outcome

These concepts are distinct:

- `supports` → relationship;
- `supported` → evaluation outcome.

`supports ≠ supported`

Relationship count does not determine the evaluation outcome.

## Reference vs. Derivation

`references` means an object identifies or cites another object.

`derived-from` means an object was materially produced from another governed basis.

`Reference ≠ Derivation`

`Reference ≠ Support`

`Reference ≠ Authority Transfer`

## Prior Trust Statements

Later Trust Statements may relate to prior Trust Statements through governed correction, supersession, versioning, or review relationships.

Prior objects remain historically identifiable.

`Correction ≠ Deletion`

`Supersession ≠ Historical Erasure`

Exact lifecycle effects belong to Lifecycle and Versioning.

## Suite Relationships

Attestor may relate to canonical Suite objects while preserving source responsibility:

- Atlas → Authoritative Intelligence
- Navigator → Workflow Definition / Orchestration
- Certifier → Certification Package
- Registry → Satoshium Registry Record
- Chronicle → Chronicle Entry
- Anchor → Integrity Reference
- Beacon → Discovery Signal / Discovery Metadata
- Attestor → Trust Statement

Relationships do not convert source objects into Attestor-owned objects.

## Deferred Structural Constraints

This page establishes relationship semantics and conceptual direction.

Later architecture will define:

- permitted source/target object combinations;
- required vs. optional relationships;
- cardinality;
- inverse representations where useful;
- schema fields; and
- machine validation.

## What Relationships Do Not Establish

`Relationship ≠ Identity`

`Relationship ≠ Authority Transfer`

`Relationship ≠ Eligibility`

`Relationship ≠ Evidence Sufficiency`

`Relationship ≠ Validation`

`Relationship ≠ Conformance`

`Relationship ≠ Evaluation Outcome`

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Relationships → Established**

- canonical relationship vocabulary → defined
- directionality → established conceptually
- Attestation/Evaluation/Trust Statement chain → established
- support vs. outcome → distinguished
- reference vs. derivation → distinguished
- correction/supersession continuity → established conceptually
- source authority boundaries → preserved
- cardinality/machine constraints → deferred to Schemas / Validation
- production proof → pending
