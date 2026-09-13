# Satoshium Beacon — Discovery Signal Types

**Path:** `/beacon/signal-types/`  
**Institution:** Satoshium Beacon  
**Architecture:** Discovery Signal Architecture  
**Status:** Operational · September 2026  
**First Production Signal:** `BEAC-2026-0001`

## Purpose

Discovery Signal Types provide the governed classification vocabulary used to describe what kind of discovery a Beacon-owned Discovery Signal represents.

Signal Type classifies Beacon's discovery object. It does not inherit the type, status, or authority of the source object.

```text
Signal Type ≠ Source Object Type ≠ Source Status
```

## Governed Signal Types

The initial governed vocabulary contains eight types:

- Information
- Jurisdiction
- Certification
- Registry
- Historical
- Integrity
- Trust
- Relationship

One primary governed Signal Type is preferred.

Secondary context should normally be preserved through references, metadata, and relationships rather than uncontrolled multi-classification.

## First Production Exercise

`BEAC-2026-0001` is Beacon's first production Discovery Signal.

- **Title:** Active Operational Certification — Atlas Jurisdiction Record — El Salvador
- **Primary Signal Type:** Certification
- **Primary Source:** Satoshium Certifier · `SC-CERT-2026-0001`
- **Source Object Type:** Canonical Certification Package
- **Observed Source Status:** Issued · Active · Operational
- **Lifecycle:** Active
- **Publication:** Published
- **Version:** 1.0

This production object demonstrates that a Certification Signal is not itself a Certification Package and does not transfer Certifier authority to Beacon.

## Authority Boundary

Examples:

```text
Certification Signal ≠ Certification Package
Registry Signal ≠ SREG
Historical Signal ≠ Chronicle Entry
Integrity Signal ≠ Integrity Reference
Trust Signal ≠ Trust Statement
```

> **Reference does not transfer authority.**

## Controlled Vocabulary Posture

The institutional Signal Type vocabulary and validation architecture are defined and production-exercised.

Still intentionally unfrozen:

- exact machine-readable enum serialization
- aliases
- future extensibility rules
- future Signal Type additions

## Current Status

```text
Beacon Status → Operational · September 2026
Signal-Type Architecture → Defined and production-exercised
Governed Signal Types → 8
Production Validation → Exercised
First Production Discovery Signal → BEAC-2026-0001 · Certification · Active · Published
```
