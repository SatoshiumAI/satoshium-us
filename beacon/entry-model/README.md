# Satoshium Beacon — Discovery Signal Entry Model

**Path:** `/beacon/entry-model/`  
**Institution:** Satoshium Beacon  
**Canonical Object:** Discovery Signal  
**Status:** Operational · September 2026  
**First Production Object:** `BEAC-2026-0001`

## Purpose

The Discovery Signal Entry Model defines the canonical structure of a Beacon-owned Discovery Signal.

The conceptual structure is:

```text
Identity
→ Subject
→ Signal Type
→ Source
→ Provenance
→ Canonical References
→ Discovery Metadata
→ Timestamps
→ Version
→ Status
→ Relationships
```

Beacon owns the Discovery Signal and its Beacon-side institutional representation. Referenced institutions retain authority over their own canonical objects.

> **Reference does not transfer authority.**

## Core Components

Expected core components are:

- Identity
- Subject
- Signal Type
- Source
- Provenance
- Discovery Metadata
- Timestamps
- Version
- Status

Conditional components may include:

- Canonical-object references
- External references
- Relationships
- Supersession data
- Navigator workflow context

## Governed Downstream Architecture

Phase II subsequently established:

- Identifier Standard: `BEAC-YYYY-NNNN`
- Initial Signal Types: Information, Jurisdiction, Certification, Registry, Historical, Integrity, Trust, Relationship
- Lifecycle: Draft → Active → Superseded / Resolved / Withdrawn
- Publication: Unpublished / Published
- Versioning and supersession rules
- Validation architecture
- Provenance architecture
- Authority model
- Relationship model
- Publication model
- Beacon Records
- Individual Beacon Record representation
- Discovery Methodology
- Production Model

Critical classification rule:

```text
Signal Type ≠ Source Object Type ≠ Source Status
```

## First Production Exercise

The Entry Model has been exercised through:

**`BEAC-2026-0001`**

Title:

**Active Operational Certification — Atlas Jurisdiction Record — El Salvador**

State:

- Signal Type: Certification
- Primary Source: `SC-CERT-2026-0001`
- Lifecycle: Active
- Publication: Published
- Version: 1.0
- Published: September 13, 2026

## Remaining Open Implementation Details

The institutional architecture is defined and production-exercised. Remaining intentionally open implementation matters include:

- exact machine serialization
- final `.schema.json` dialect and constraints
- exact machine relationship predicates
- future Signal Type extensions
- later API, monitoring, analytics, automation, and federation capabilities

## Current Status

```text
Beacon Status → Operational · September 2026
Phase I → Complete
Phase II → Complete
Entry Model → Defined and production-exercised
First Production Discovery Signal → BEAC-2026-0001 · Active · Published
```
