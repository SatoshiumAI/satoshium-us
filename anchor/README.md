# Satoshium Anchor

**Path:** `/anchor/`  
**Institution:** Satoshium Anchor  
**Institutional Role:** Integrity Preservation  
**Canonical Object:** Integrity Reference  
**Status:** Operational

## Overview

Satoshium Anchor is the Satoshium Suite institution responsible for preserving durable **Integrity References** for authoritative artifacts and records.

Anchor records cryptographic, temporal, representation, and verification context without assuming authority over the artifact it references, its meaning, its certification, its historical interpretation, or any trust conclusion derived from it.

Anchor is operational and has completed its first end-to-end production cycle.

First published Integrity Reference:

`ANCH-2026-0001`

## Institutional Purpose

Anchor exists to answer a bounded integrity question:

> Does the referenced representation remain consistent with the representation that Anchor preserved?

Anchor does **not** answer:

- who owns the source record;
- whether the source record is true;
- whether the source record is certified;
- what the source record means historically;
- whether a trust conclusion should be drawn from it.

Those responsibilities remain with the appropriate source or Suite institution.

## Anchor Model

```text
Authoritative Artifact
↓
Defined Canonical Representation
↓
Integrity Value Generated
↓
Integrity Reference Created
↓
Published / Preserved
↓
Later Integrity Verification
```

Authority answers who owns the record.

Integrity answers whether the referenced representation remains consistent with the anchored representation.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Canonical Object

Anchor's canonical object is the:

**Integrity Reference**

An Integrity Reference preserves the context required to independently review the integrity relationship between an authoritative source artifact and a defined canonical representation.

## Current Operational Status

Anchor is operational.

Current production evidence includes:

- First Published Integrity Reference: `ANCH-2026-0001`
- Source Artifact: `SCRD-SC-CERT-2026-0001`
- Stage A Validation: PASS
- Initial Verification: match
- Stage B Validation: PASS
- Publication Gate: APPROVED
- Publication State: published
- Lifecycle State: active

Anchor now has:

- a production package structure;
- governed Validation records;
- governed Verification records;
- a formal Publication Gate;
- canonical HTML and JSON publication;
- lifecycle evidence;
- a published Integrity Reference index.

## Foundation Documentation

The Anchor foundation includes:

- `/anchor/purpose/`
- `/anchor/definitions/`
- `/anchor/integrity-preservation/`
- `/anchor/anchoring-process/`
- `/anchor/integration/`
- `/anchor/standards/`
- `/anchor/governance/`
- `/anchor/identities/`
- `/anchor/claims/`
- `/anchor/attestations/`
- `/anchor/reputation/`
- `/anchor/trust/`
- `/anchor/status/`
- `/anchor/faq/`

Identity-, claim-, attestation-, reputation-, and trust-related pages are bounded integrity-preservation surfaces.

They do not make Anchor the authority for identity, claims, attestations, reputation, or trust.

## Production Records

Anchor exposes two distinct operational record surfaces:

```text
/anchor/anchored-items/
→ production packages, including unpublished candidates

/anchor/integrity-references/
→ published Integrity References only
```

The first published production package is:

`/anchor/anchored-items/ANCH-2026-0001/`

The published-only index is:

`/anchor/integrity-references/`

## Production Architecture

Anchor's production architecture includes:

- Identifiers
- Controlled Values
- Relationships
- Provenance
- Schemas
- Integrity Verification
- Validation
- Lifecycle
- Versioning
- Corrections
- Publication
- Maintenance
- Production Procedures

These surfaces govern the creation, validation, verification, publication, Versioning, correction, and maintenance of real Integrity References.

## Authority Boundary

Anchor is authoritative for:

- Anchor Identifiers;
- Integrity References;
- Anchor-owned metadata;
- Anchor Validation;
- Anchor Verification results;
- Anchor lifecycle state;
- Anchor publication state;
- Anchor Corrections and Versions.

Anchor is **not** authoritative for the referenced Source Artifact.

The Source Institution retains authority over its own canonical object.

```text
Anchor Identifier
→ Anchor authority

Source-System Identifier
→ Source Institution authority
```

**Connection ≠ Identity.**  
**Reference ≠ Derivation.**  
**Reference ≠ Support.**  
**Reference ≠ Authority Transfer.**

## Relationship to Other Suite Institutions

Anchor may preserve integrity context for artifacts originating from Atlas, Certifier, Registry, Chronicle, Beacon, Attestor, Navigator, or external sources.

That relationship remains reciprocal and bounded.

Anchor does not absorb the institutional authority of the source system.

## Technology Position

Anchor is implementation-neutral at the institutional level.

Its first production Integrity Reference currently uses:

- canonical JSON;
- RFC 8785 JSON Canonicalization Scheme (JCS);
- SHA-256 cryptographic digest.

Those implementation choices describe the current production record and do not require Anchor to become dependent on a single technology forever.

## Production Path

```text
Foundation
↓
Production Architecture
↓
ANCH-2026-0001 constructed
↓
Stage A Validation — PASS
↓
Initial Verification — match
↓
Stage B Validation — PASS
↓
Publication Gate — APPROVED
↓
Publication — COMPLETE
↓
Published Integrity Reference Index — ACTIVE
↓
Maintenance / Reverification / Future Records
```

The first full production cycle is complete.

Future Integrity References follow the governed production path established through `ANCH-2026-0001`.

## Anchor Principle

> **Preserve the reference. Preserve the boundary. Preserve the authority.**

Production validates architecture.

Architecture does not validate itself.

## Repository Maintenance

Anchor documentation should:

- preserve the Integrity Reference as Anchor's canonical object;
- maintain separation between Source authority and Anchor authority;
- distinguish Validation from Verification;
- distinguish candidate production packages from published Integrity References;
- preserve lifecycle, Versioning, Correction, Publication, and Maintenance history;
- avoid reintroducing the superseded identity-layer model as Anchor's primary institutional role;
- preserve older identity/trust materials only where they remain useful as bounded integrity-preservation contexts.

README reconciliation documents the architecture that exists. It does not redesign it.
