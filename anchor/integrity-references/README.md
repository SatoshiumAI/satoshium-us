# Satoshium Anchor — Integrity References

**Path:** `/anchor/integrity-references/`  
**Public page:** `index.html`  
**Status:** Active published-record index

## Purpose

The `/anchor/integrity-references/` directory is the public index of **published Satoshium Anchor Integrity References**.

A record appears here only after the governed Anchor publication path is complete.

This directory is not a candidate queue, workspace, or staging surface.

## Index Boundary

The current Anchor architecture distinguishes between:

```text
/anchor/anchored-items/
→ all production packages, including unpublished candidates

/anchor/integrity-references/
→ published Integrity References only
```

This boundary is intentional.

The Integrity References index should contain only records that have completed the required publication sequence and entered public Anchor authority.

## Publication Requirements

Before an Anchor record may appear in this index, it must complete the governed publication path.

The current publication requirements include:

- Stage A Validation → PASS
- Initial Verification → governed result
- Canonical HTML + Canonical JSON
- Stage B Validation → PASS
- Publication Gate → APPROVED
- Publication → COMPLETE

Inclusion in this directory therefore reflects completed publication, not merely record creation.

## Current Published Integrity Reference

### `ANCH-2026-0001`

**Status:** Published · Active

First published Satoshium Anchor Integrity Reference.

Current record metadata:

- Anchor Identifier: `ANCH-2026-0001`
- Anchor Version: `1`
- Source Institution: Satoshium Certifier
- Source-System Identifier: `SCRD-SC-CERT-2026-0001`
- Source Artifact Type: Satoshium Certified Record (SCRD JSON)
- Representation Type: `canonical_json`
- Canonicalization: RFC 8785 JCS
- Integrity Method: `cryptographic_digest`
- Algorithm: SHA-256
- Integrity State: current
- Publication State: published
- Lifecycle State: active
- Published At: `2026-08-29T15:40:14-07:00`

Current published record count:

**1**

## Identifier Resolution

The Anchor Identifier identifies the Integrity Reference.

Example:

```text
ANCH-2026-0001
→ /anchor/anchored-items/ANCH-2026-0001/
```

The URL resolves the record.

The URL is not itself the Anchor Identifier.

## Authority Boundary

Publication makes Anchor authoritative for:

- the published Integrity Reference;
- Anchor-owned metadata;
- Anchor lifecycle and publication state;
- Anchor integrity assertions within the defined scope of the record.

Publication does **not** transfer authority over the referenced Source Artifact.

The governing distinction is:

```text
Anchor Identifier
→ Anchor authority

Source-System Identifier
→ Source Institution authority
```

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

Likewise:

- **Connection ≠ Identity.**
- **Reference ≠ Derivation.**
- **Reference ≠ Support.**
- **Reference ≠ Authority Transfer.**

## Relationship to Source Artifacts

Anchor may establish a durable integrity relationship to a source artifact without assuming ownership of that source artifact.

For `ANCH-2026-0001`:

- Anchor owns the Integrity Reference;
- Satoshium Certifier remains authoritative for the referenced SCRD source artifact.

The integrity relationship does not merge institutional identity.

## Canonical Representation

The current published record uses:

- canonical JSON representation;
- RFC 8785 JSON Canonicalization Scheme (JCS);
- SHA-256 cryptographic digest.

These implementation details belong to the published Integrity Reference and should be documented as record properties rather than generalized beyond the supported Anchor architecture.

## Repository Role

The public `index.html` is the principal representation of the published Integrity References index.

Individual published Anchor records resolve through `/anchor/anchored-items/<ANCH-ID>/`.

This README documents the purpose, boundaries, and maintenance expectations of the index itself.

## Maintenance

Repository maintenance for `/anchor/integrity-references/` should:

- index only records that Anchor has actually published;
- exclude unpublished candidates;
- keep published record counts synchronized with actual publication state;
- preserve Anchor Identifier resolution;
- retain clear separation between Anchor authority and Source Institution authority;
- keep publication requirements aligned with governed Anchor process;
- avoid treating a published Integrity Reference as ownership of the referenced source artifact;
- preserve canonical record metadata exactly where it is part of the published record.

## Anchor Index Principle

> **Index only what Anchor has actually published.**

README reconciliation documents the Anchor index architecture that exists. It does not redesign it.
