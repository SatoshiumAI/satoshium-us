# Satoshium Beacon — Authority & Reference Model

**Path:** `/beacon/authority/`  
**Institution:** Satoshium Beacon  
**Architecture:** Discovery Signal Architecture  
**Status:** Operational · September 2026  
**First Production Signal:** `BEAC-2026-0001`

## Governing Rule

> **Reference does not transfer authority.**

Beacon may discover, reference, attribute, preserve provenance, and create its own Discovery Signal without acquiring the authority of the referenced institution or source.

A complementary rule is:

> **Discovery visibility must never be mistaken for institutional elevation.**

## Beacon Owns

Beacon owns:

- Discovery Signals
- `BEAC-YYYY-NNNN` identifiers
- Discovery Metadata
- Beacon lifecycle state
- Beacon publication state
- Beacon version and supersession information
- Beacon provenance
- Beacon validation determinations
- Beacon-side relationships and references

Beacon owns the reference relationship **as represented inside its own Discovery Signal**. It does not own the referenced object.

## Beacon Does Not Own

Beacon does not acquire ownership of:

- Atlas Authoritative Intelligence
- Certifier Certification Packages
- Registry SREG records
- Chronicle Entries
- Anchor Integrity References
- Attestor Trust Statements
- Navigator Workflow Definitions or orchestration authority
- external source objects or assertions

## Three-Layer Reference Model

```text
Referenced Object
→ Beacon Reference
→ Beacon Discovery Signal
```

The referenced object retains its native identity, object type, and institutional authority.

## First Production Authority Exercise

`BEAC-2026-0001` exercised the Authority & Reference Model.

```text
Beacon-Owned Object → BEAC-2026-0001
Primary Referenced Object → SC-CERT-2026-0001
Referenced Institution → Satoshium Certifier
Referenced Object Type → Canonical Certification Package
Referenced Certification Condition → Issued · Active · Operational
Underlying Subject → Atlas Jurisdiction Record — El Salvador
Subject Authority → Satoshium Atlas
Related Registry Object → SREG-2026-0001
Related Chronicle Object → CHR-2026-0001
Related Integrity Object → ANCH-2026-0001
```

Authority remains divided correctly:

- **Satoshium Certifier** retains authority for `SC-CERT-2026-0001`, including the certification decision, class, lifecycle, and status.
- **Satoshium Atlas** retains authority over the underlying jurisdiction intelligence.
- **Satoshium Beacon** owns only `BEAC-2026-0001` and its Beacon-side discovery metadata, provenance, lifecycle, publication state, validation determinations, version information, relationships, and references.

The first production Authority Boundary review passed.

## Authority vs. Provenance

```text
Authority → whose object or determination is this?
Provenance → how did Beacon encounter and preserve it?
```

These concepts remain distinct.

## Signal Type vs. Source Object Type

For the first production signal:

```text
Beacon Signal Type → Certification
Source Object Type → Canonical Certification Package
Source Status → Issued · Active · Operational
```

These are related but not interchangeable.

## Remaining Open Implementation Details

The institutional authority boundary is defined and production-exercised. Remaining intentionally open matters include:

- exact machine-readable canonical-reference property names
- formal authority-attribution field vocabulary
- reference-resolution behavior
- rules for inaccessible or restricted canonical objects
- external-source authority classifications if later needed
- reference-correction mechanics
- reference-resolution automation
- specialized Signal Type/source-institution requirements if later justified

## Current Status

```text
Beacon Status → Operational · September 2026
Authority & Reference Model → Defined and production-exercised
First Production Authority Review → PASS
Primary Referenced Object → SC-CERT-2026-0001
Certifier Authority → Preserved
Atlas Subject Authority → Preserved
Beacon Authority Boundary → Preserved
Relationship Model → Defined
First Production Discovery Signal → BEAC-2026-0001 · Active · Published
```
