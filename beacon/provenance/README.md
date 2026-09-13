# Satoshium Beacon — Discovery Provenance

**Path:** `/beacon/provenance/`  
**Institution:** Satoshium Beacon  
**Architecture:** Discovery Signal Architecture  
**Status:** Operational · September 2026  
**First Production Signal:** `BEAC-2026-0001`

## Purpose

Discovery Provenance preserves the evidentiary path behind a Beacon Discovery Signal:

- where the information came from
- what Beacon observed
- when it was observed
- how it was encountered
- the context of the observation
- the reviewable basis supporting the discovery

Provenance makes a signal reviewable without transferring source authority to Beacon.

## Beacon Provenance Chain

```text
Source / Authoritative Object
→ observed by Beacon
→ Observation
→ Discovery Context
→ Beacon Discovery Signal
→ Preserved Provenance
```

Source and provenance are distinct:

```text
Source → what Beacon observed or references
Provenance → how Beacon encountered, observed, attributed, and preserved it
```

## Required Provenance Components

- Source Identity
- Observed Information
- Observation Time
- Observation Method
- Observation Context
- Supporting Basis

Direct and indirect provenance must remain distinguishable.

## First Production Provenance

`BEAC-2026-0001` exercised Beacon's provenance architecture on September 13, 2026.

```text
Provenance Type → Direct
Observer → Satoshium Beacon
Observation Date → September 13, 2026
Observation Method → Direct review of published canonical source
Observed Source → Satoshium Certifier · SC-CERT-2026-0001
Source Object Type → Canonical Certification Package
Source Version → 1.1
Observed Condition → Issued · Active · Operational
```

Supporting Suite context reviewed:

```text
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
```

These supporting objects are related context. They are **not** additional links in Beacon's direct provenance chain.

Beacon's production provenance is:

```text
SC-CERT-2026-0001
→ directly observed by Beacon
→ BEAC-2026-0001
```

## Temporal Provenance

Keep temporal meanings distinct:

- `source_published_at` — source publication time when known
- `observed_at` — Beacon observation time
- `created_at` — canonical Discovery Signal creation time
- `published_at` — Beacon publication time
- `last_observed_at` — later governed observation when applicable

Re-observation does not rewrite the original observation.

## Authority Boundary

```text
Beacon preserves where its signal came from.
Beacon does not become the source.
Beacon preserves the source object's identity.
Beacon does not inherit its authority.
```

> **Reference does not transfer authority.**

## Remaining Open Implementation Details

The institutional provenance architecture is defined and production-exercised. Remaining intentionally open matters include:

- exact machine-readable provenance property names
- frozen observation-method enum serialization
- provenance-depth refinements by Signal Type
- machine citation/location formats
- discovery-actor privacy rules
- workflow-reference syntax
- re-observation machine-schema mechanics
- unavailable-source preservation mechanics
- possible cryptographic provenance profiles
- future automated provenance capture

## Current Status

```text
Beacon Status → Operational · September 2026
Discovery Provenance → Defined and production-exercised
First Production Provenance → Direct
Primary Observed Source → SC-CERT-2026-0001
Production Provenance Validation → PASS
First Production Discovery Signal → BEAC-2026-0001 · Active · Published
```

## Governing Principle

**A discovery becomes reviewable when its path back to the source remains visible.**
