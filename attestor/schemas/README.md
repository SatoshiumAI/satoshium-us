# Schemas

## Purpose

Schemas provide the structural foundation for Attestor.

They define how attestations, evidence, reputation signals, trust relationships, corrections, and related information may be represented, exchanged, stored, and interpreted.

Schemas help create consistency across records while supporting interoperability with the broader Satoshium ecosystem.

---

## Why Schemas Matter

Trust systems depend upon structured information.

Without common structures:

* Records become inconsistent.
* Interoperability becomes difficult.
* Relationships become unclear.
* Historical review becomes more complicated.

Schemas help establish shared expectations regarding how information is organized.

---

## Schema Philosophy

Schemas should support:

* Transparency
* Attribution
* Traceability
* Interoperability
* Preservation

Schemas exist to improve understanding, not to impose conclusions.

They provide structure for trust-related information.

---

## What Schemas Define

Schemas may define:

* Record structures
* Required fields
* Optional fields
* Relationships
* Identifiers
* Metadata
* References
* Status indicators

Specific schema implementations may evolve over time.

---

## Core Schema Categories

### Attestation Schemas

Define how attestations are represented.

Examples:

* Identity attestations
* Qualification attestations
* Ownership attestations
* Participation attestations
* Relationship attestations

---

### Evidence Schemas

Define structures for supporting evidence.

Examples:

* Source references
* Evidence records
* Supporting materials
* Verification references

---

### Reputation Schemas

Define structures for reputation-related information.

Examples:

* Reputation signals
* Reputation events
* Reputation histories
* Reputation summaries

---

### Trust Schemas

Define structures for trust-related records.

Examples:

* Trust relationships
* Confidence indicators
* Trust observations
* Trust contexts

---

### Correction Schemas

Define structures for corrections and amendments.

Examples:

* Correction records
* Retraction records
* Revision histories
* Correction metadata

---

### Source Schemas

Define structures for source references.

Examples:

* Source identifiers
* Source metadata
* Attribution records
* Reference structures

---

## Current Attestor Schemas

The initial Attestor schema framework includes:

```text id="z8x5nt"
Attestation Record Schema
Evidence Record Schema
Reputation Record Schema
Trust Signal Schema
Correction Record Schema
```

Additional schemas may be introduced as the system evolves.

---

## Schema Objectives

### Consistency

Information should be represented predictably.

### Interoperability

Records should remain understandable across systems.

### Traceability

Relationships should remain reviewable.

### Portability

Records should support movement between environments.

### Longevity

Schemas should support long-term preservation.

---

## Relationship to Records

Records are often created using schemas.

A simplified relationship may be represented as:

```text id="p4u6mv"
Schema → Record
```

Schemas provide structure.

Records provide content.

---

## Relationship to Attestations

Attestations may be documented through standardized schemas.

Schemas help preserve:

* Attribution
* Evidence references
* Timestamps
* Context
* Status information

---

## Relationship to Registry

Registry provides structured record management.

Schemas help ensure Attestor records remain compatible with Registry systems.

A simplified relationship may be represented as:

```text id="n2k7ef"
Schema → Registry Record
```

---

## Relationship to Chronicle

Chronicle preserves historical information.

Schemas help maintain consistency in historical records derived from Attestor.

Structured records improve historical traceability.

---

## Relationship to Anchor

Anchor manages identity-related information.

Attestor schemas may reference identity records maintained by Anchor.

Consistent schema structures improve interoperability.

---

## Relationship to Certifier

Certifier focuses on verification.

Attestor schemas may reference verification outcomes and supporting certifications.

Common schema structures help preserve context across systems.

---

## Relationship to Beacon

Beacon focuses on discovery.

Structured schemas improve discoverability by making information easier to organize, search, and interpret.

A simplified relationship may be represented as:

```text id="m9j3rd"
Schema → Discovery
```

---

## Relationship to the Satoshium Suite

Schemas help support interoperability across:

```text id="u5c8qf"
Atlas
Navigator
Beacon
Certifier
Registry
Chronicle
Anchor
Attestor
```

Shared structures improve communication among systems.

---

## Guiding Principles

### Transparency

Schema structures should remain understandable.

### Attribution

Responsible parties should remain identifiable.

### Traceability

Relationships should remain reviewable.

### Preservation

Historical information should remain accessible.

### Interoperability

Schema designs should support cross-system compatibility.

---

## Long-Term Vision

As Attestor evolves, schemas may become part of a broader trust interoperability framework capable of supporting attestations, evidence, reputation systems, governance models, and trust-related information across diverse digital environments.

The long-term goal is not merely standardization.

The goal is preserving trust context through structure.

---

## Guiding Statement

The purpose of a schema may be summarized as:

```text id="k7v4ba"
Trust requires structure.
Schemas provide structure.
```

---

## Status

Attestor schemas are currently in an early development phase.

This document defines conceptual principles rather than finalized technical specifications.
