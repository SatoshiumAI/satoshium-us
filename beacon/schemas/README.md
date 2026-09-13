# Satoshium Beacon — Beacon Schemas

**Path:** `/beacon/schemas/`  
**Institution:** Satoshium Beacon  
**Architecture:** Discovery Signal Architecture  
**Status:** Operational · September 2026  
**Canonical Object:** Discovery Signal

## Purpose

Beacon Schemas define the governed structural architecture for Beacon-owned Discovery Signals and supporting discovery structures.

Schema defines structure. It does not create truth, authority, certification, registration, historical significance, integrity, or trust.

## Canonical Schema Architecture

### Canonical

`discovery-signal-schema.md`

Represents:

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

### Supporting

`source-reference-schema.md`

Reusable source-reference structure preserving source identity, source institution or external origin, canonical source identifier where applicable, and authority boundaries.

### Optional Noncanonical

`discovery-result-schema.md`

May represent transient discovery/query output. It does not compete with the Discovery Signal as Beacon's canonical object.

### Optional Operational

`query-log-schema.md`

May support operational transparency and reproducibility. It is not a canonical Discovery Signal schema.

### Deprecated

Earlier generic `signal-record-schema.md` and `beacon-record-schema.md` concepts are deprecated as canonical schemas.

A **Beacon Record** is the public representation of a Discovery Signal, not a separate canonical object type.

## Governed Values

Signal Types:

```text
Information · Jurisdiction · Certification · Registry · Historical · Integrity · Trust · Relationship
```

Lifecycle:

```text
Draft · Active · Superseded · Resolved · Withdrawn
```

Publication:

```text
Unpublished · Published
```

Identifier:

```text
BEAC-YYYY-NNNN
```

Exact frozen machine enum serialization remains intentionally open.

## Production Exercise

The schema architecture was exercised at the governed conceptual level through `BEAC-2026-0001`.

- Canonical Object: Discovery Signal
- Identifier: `BEAC-2026-0001`
- Signal Type: Certification
- Source: Satoshium Certifier · `SC-CERT-2026-0001`
- Provenance: Direct
- Lifecycle: Active
- Publication: Published
- Version: 1.0
- Schema Conformity: PASS at governed conceptual level

No frozen `.schema.json` existed for the first production operation, so machine-serialization validation was not applicable.

## Remaining Open Implementation Details

The institutional schema architecture is defined and production-exercised. Remaining intentionally open matters include:

- exact machine property serialization
- frozen required/optional machine-property constraints
- machine-readable enum serialization
- JSON Schema version and dialect
- machine-schema version identifiers
- reusable machine sub-schema boundaries
- discovery-result retention rules
- query-log retention and privacy rules

## Authority Boundary

```text
Beacon schema → defines Beacon's object and Beacon-side references
Source schema → remains owned by the source institution
Cross-Suite reference → preserves connection, not authority transfer
```

> **Reference does not transfer authority.**

## Current Status

```text
Beacon Status → Operational · September 2026
Schema Architecture → Defined and production-exercised
Canonical Production Object → Discovery Signal
Canonical Human-Readable Schema → discovery-signal-schema.md
Supporting Schema → source-reference-schema.md
Optional Noncanonical Schema → discovery-result-schema.md
Optional Operational Schema → query-log-schema.md
Legacy Generic Record Schemas → Deprecated
Validation Architecture → Defined
Frozen Machine Schema → Not yet adopted
```
