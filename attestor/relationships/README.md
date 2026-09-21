# Satoshium Attestor — Relationships

**Path:** `/attestor/relationships/`  
**Institution:** Satoshium Attestor  
**Current Stage:** Operational Relationships  
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

## Structural Constraints

This page establishes relationship semantics and direction.

Canonical structured relationship representation is now exercised in production.

Schemas and Validation govern applicable:

- permitted source/target object combinations;
- required vs. optional relationships;
- cardinality;
- inverse representations where defined;
- schema fields; and
- machine enforcement.

Production use of a relationship type does not make that relationship valid for every object pair.

## First Production Relationship Demonstration

The first controlled production operation exercised structured relationships across the canonical Attestation and Trust Statement.

`ATT-2026-0001` preserved explicit `references` relationships to:

- `SC-CERT-2026-0001`
- `SREG-2026-0001`
- `CHR-2026-0001`
- `ANCH-2026-0001`
- `BEAC-2026-0001`

`TRST-2026-0001` preserved:

- `derived-from` → `ATT-2026-0001`
- `references` → `SC-CERT-2026-0001`
- `references` → `SREG-2026-0001`
- `references` → `CHR-2026-0001`
- `references` → `ANCH-2026-0001`
- `references` → `BEAC-2026-0001`

**Production relationship representation → DEMONSTRATED**

The operation confirmed:

`Reference ≠ Derivation`

`Reference ≠ Support`

`Relationship ≠ Eligibility`

`Connection ≠ Identity`

`Reference ≠ Authority Transfer`

## Production Relationship Correction

The first production operation also exercised governed relationship remediation.

Early production representations used descriptive relationship strings. Those representations were corrected to structured relationship blocks containing explicit relationship types and target identifiers.

The correction preserved:

- canonical ATT and TRST identifiers;
- the Attestation assertion;
- the Trust Statement conclusion;
- scope;
- provenance;
- limitations;
- production history; and
- version `V1.0`.

The earlier representations were preserved as history rather than silently overwritten.

For this bounded operation, the relationship correction was determined to be a serialization-only correction rather than a material change to the canonical assertion or conclusion.

Therefore:

`Correction ≠ Deletion`

`Correction ≠ Silent Historical Overwrite`

`Serialization Correction ≠ Automatic New Canonical Object`

The V1.0 treatment is not a universal rule for all future relationship corrections. Materiality must be determined under the applicable Lifecycle, Versioning, and Correction rules.

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

**Relationships → Established and Production-Proven**

- canonical relationship vocabulary → defined
- directionality → established
- structured relationship representation → exercised
- Attestation / Evaluation / Trust Statement lineage → demonstrated
- `references` → exercised in production
- `derived-from` → exercised in production
- support vs. outcome → distinguished
- reference vs. derivation → distinguished and demonstrated
- connection vs. identity → preserved
- relationship vs. eligibility → preserved
- source authority boundaries → preserved
- relationship correction continuity → exercised
- historical representations → preserved
- applicable structural / machine constraints → governed through Schemas / Validation
- production proof → **ESTABLISHED**

## Continuing Relationship Governance

The first production operation proves that governed relationships can preserve lineage and institutional boundaries across real Attestor objects.

It does not establish that every relationship type is valid between every object class.

Future relationship creation or correction must continue to preserve:

- source and target identity;
- relationship type and direction;
- provenance;
- authority boundaries;
- lifecycle context;
- versioning consequences;
- correction history; and
- materiality.

`Connection ≠ Identity`

`Reference ≠ Derivation`

`Reference ≠ Support`

`Relationship ≠ Eligibility`

**Reference does not transfer authority.**
