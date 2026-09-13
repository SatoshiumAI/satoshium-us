# Satoshium Beacon — Relationship Model

**Path:** `/beacon/relationships/`  
**Institution:** Satoshium Beacon  
**Architecture:** Discovery Signal Architecture  
**Status:** Operational · September 2026  
**First Production Signal:** `BEAC-2026-0001`

## Governing Principle

> **Relationship connects objects. It does not merge them.**

All Beacon relationships also operate under:

> **Reference does not transfer authority.**

## Relationship Classes

The governed relationship classes are:

- Source
- Canonical Object
- Related Signal
- Version
- Supersession
- Workflow
- External

Signal Type and Relationship Type are separate concepts.

## Relationship Requirements

A governed relationship preserves:

- endpoints
- endpoint identity and ownership
- relationship meaning
- direction when meaningful
- attribution
- supporting basis
- provenance
- authority boundary

Observed relationships and Beacon-determined relationships must remain distinguishable.

## First Production Relationship Exercise

`BEAC-2026-0001` exercised the Relationship Model.

Primary relationship:

```text
BEAC-2026-0001
→ directly observed from / references
→ SC-CERT-2026-0001
```

Supporting canonical references:

```text
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
```

These supporting objects were reviewed as related Suite context. They are not additional links in Beacon's direct provenance chain.

Production relationship findings:

```text
Primary Source Endpoint → SC-CERT-2026-0001
Beacon Endpoint → BEAC-2026-0001
Primary Relationship Class → Source / Canonical Object
Primary Relationship Meaning → directly observed from / references
Supporting Registry Reference → SREG-2026-0001
Supporting Chronicle Reference → CHR-2026-0001
Supporting Integrity Reference → ANCH-2026-0001
Authority Boundary → Preserved
Relationship Validation → PASS with implementation note
```

The implementation note reflects that exact machine relationship predicates remain intentionally unfrozen.

## No Object Collapse

```text
SC-CERT-2026-0001
+ SREG-2026-0001
+ CHR-2026-0001
+ ANCH-2026-0001
+ BEAC-2026-0001
≠ one canonical object
```

Each object retains its own institution, identifier, object type, lifecycle, and authority.

## Versioning and Supersession

Version and supersession relationships are governed by Beacon Versioning & Supersession architecture.

A new version under the same BEAC identifier is distinct from creation of a new Discovery Signal.

## Remaining Open Implementation Details

The institutional Relationship Model is defined and production-exercised. Remaining intentionally open matters include:

- exact machine-readable relationship property names
- frozen controlled relationship predicates
- formal inverse-relationship rules
- cardinality constraints
- relationship identifiers if ever institutionally necessary
- relationship lifecycle/status machine vocabulary
- relationship-correction mechanics
- version-specific machine relationship mechanics
- specialized relationship requirements by Signal Type
- publication restrictions for sensitive relationships

## Current Status

```text
Beacon Status → Operational · September 2026
Relationship Model → Defined and production-exercised
First Production Relationship Review → PASS with implementation note
Primary Source Relationship → BEAC-2026-0001 ↔ SC-CERT-2026-0001
Supporting References → SREG-2026-0001 · CHR-2026-0001 · ANCH-2026-0001
Versioning & Supersession → Defined
Exact Machine Relationship Predicates → Not yet frozen
First Production Discovery Signal → BEAC-2026-0001 · Active · Published
```
