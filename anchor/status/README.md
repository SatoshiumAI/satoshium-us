# Satoshium Anchor — Status

**Path:** `/anchor/status/`  
**Status:** Operational  
**Canonical Object:** Integrity Reference  
**First Published Record:** `ANCH-2026-0001`

## Current Status

Satoshium Anchor is operational as the Satoshium Suite institution responsible for preserving durable **Integrity References** for authoritative artifacts and records.

Anchor has completed its first end-to-end production cycle through `ANCH-2026-0001`, establishing the governed path from Source Artifact through canonical representation, integrity generation, Validation, Verification, Publication Gate, Publication, and Maintenance.

Anchor is no longer in Foundation Reconciliation.

## Institutional Status

```text
Anchor Institution → Operational
Canonical Object → Integrity Reference
First Published Record → ANCH-2026-0001
Publication State → published
Lifecycle State → active
```

Anchor's institutional purpose is integrity preservation.

It preserves durable Integrity References for defined representations of authoritative artifacts while preserving the authority of the Source Institution.

## First Production Source

The first production Integrity Reference is based on:

```text
Source Institution → Satoshium Certifier
Source Artifact → SCRD-SC-CERT-2026-0001
Representation Type → canonical_json
Canonicalization → RFC 8785 JCS
Integrity Method → cryptographic_digest
Algorithm → SHA-256
```

These values document the first production implementation.

They do not imply that every future Anchor record must use the same implementation choices unless governed architecture requires it.

## Operational Milestones

Anchor has completed the following institutional milestones:

- Foundation reconciled
- Identifiers established
- Controlled Values established
- Relationships established
- Provenance established
- Base Schema established
- Validation architecture established
- Verification architecture established
- Lifecycle architecture established
- Versioning architecture established
- Corrections architecture established
- Publication architecture established
- Maintenance architecture established
- `ANCH-2026-0001` Stage A Validation — PASS
- Initial Verification — match
- Stage B Validation — PASS
- Publication Gate — APPROVED
- Publication — COMPLETE
- Published Integrity Reference Index — ACTIVE

## Canonical Object

Anchor's canonical operational object is:

```text
Integrity Reference
```

An Integrity Reference belongs to Anchor.

The referenced Source Artifact remains authoritative within its Source Institution.

> **Reference does not transfer authority.**

## Current Scope

Anchor currently governs:

- Integrity References;
- Anchor Identifiers;
- Controlled Values;
- Relationships;
- Provenance;
- Schemas;
- Validation;
- Verification;
- Lifecycle;
- Versioning;
- Corrections;
- Publication;
- Maintenance;
- production procedures.

Anchor does **not** operate:

- an identity network;
- an authentication platform;
- a claims registry;
- an attestation network;
- a reputation system;
- a trust-scoring system;
- a general certification authority.

Identity, claims, attestations, reputation, and trust remain bounded reference domains rather than Anchor-owned authority.

## Production Records

Anchor maintains two distinct operational record surfaces:

```text
/anchor/anchored-items/
→ assigned Integrity Reference production packages

/anchor/integrity-references/
→ published Integrity References only
```

The first published Integrity Reference is:

`ANCH-2026-0001`

## Validation and Verification

Anchor preserves a formal distinction between Validation and Verification.

```text
Validation
→ Does the Anchor record satisfy institutional requirements?

Verification
→ Does the integrity evidence match?
```

Both are governed institutional processes.

A successful Verification does not prove the truth of the underlying source artifact.

It establishes only what the integrity evidence supports.

## Publication

Publication occurs only after the governed production sequence completes.

For `ANCH-2026-0001`:

```text
Stage A Validation → PASS
Initial Verification → match
Stage B Validation → PASS
Publication Gate → APPROVED
Publication → COMPLETE
```

Publication makes Anchor authoritative for the published Integrity Reference and Anchor-owned metadata.

It does not transfer authority over the Source Artifact.

## Maintenance

Anchor has entered post-publication maintenance.

Current operational work includes:

- maintaining `ANCH-2026-0001`;
- scheduled or event-triggered Reverification;
- Source-link health review;
- algorithm-health review;
- future Corrections or Versions where required;
- long-term preservation;
- creation of future Integrity References only where production use warrants them.

Production evidence should continue to drive refinement of Controlled Values and procedures.

## Technology Position

Anchor remains institutionally implementation-neutral.

The first production record uses:

- canonical JSON;
- RFC 8785 JCS;
- SHA-256.

No single implementation mechanism defines Anchor.

The governing principle remains:

> **Tools may change. Integrity preservation remains the purpose.**

## Bitcoin Status

Bitcoin has not been adopted as a required production Anchor commitment mechanism.

Potential future commitment mechanisms may include:

- proof-of-existence;
- timestamp anchoring;
- Merkle-root commitments;
- batch commitments;
- long-term public integrity checkpoints.

Any future adoption should occur through governed architecture rather than assumption.

## Suite Relationship

Anchor may preserve Integrity References for authoritative artifacts from other Suite institutions.

Current Suite responsibility boundaries include:

```text
Atlas
→ Authoritative Intelligence

Navigator
→ Workflow Definition / Orchestration

Certifier
→ Certification Package

Registry
→ Satoshium Registry Record

Chronicle
→ Chronicle Entry

Anchor
→ Integrity Reference

Beacon
→ Discovery Signal / Discovery Metadata

Attestor
→ Attestation + Rule-Constrained Evaluation + Trust Statement
```

Anchor does not absorb the authority of the institutions whose artifacts it references.

## Authority Boundary

The governing distinction is:

```text
Authority
→ who owns the record

Integrity
→ whether the referenced representation remains consistent
  with the anchored representation
```

**Connection ≠ Identity.**  
**Reference ≠ Derivation.**  
**Reference ≠ Support.**  
**Reference ≠ Authority Transfer.**

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Current Project Classification

```text
Project Type:
Integrity-Preservation Institution

Institutional Status:
Operational

Canonical Object:
Integrity Reference

Production Architecture:
Established

Production Identifiers:
Established

Controlled Values:
Established

Production Validation:
Established

Production Verification:
Established

Production Publication:
Established

Production Maintenance:
Established

Bitcoin Commitment:
Not Required / Not Adopted as a Production Requirement

Production Integrity References:
1 Published

First Published Record:
ANCH-2026-0001

Technology Position:
Implementation-Neutral

Documentation Status:
Active
```

## Status Principle

The governing principle remains:

> **Define the institution. Prove the process. Then declare production.**

Anchor has now completed that progression.

The current institutional posture is therefore:

```text
Defined
→ Proven
→ Operational
→ Maintained
```

README reconciliation documents the operational architecture that exists. It does not redesign it.
