# Schemas

## Overview

The Satoshium Anchor Schema Architecture defines the machine-readable structure of Anchor's canonical object:

```text
Integrity Reference
```

This directory begins with the **Integrity Reference Base Schema**.

Current schema artifacts:

```text
integrity-reference-base-schema.md
integrity-reference-base-schema.json
```

The governing principle is:

> Structure the record now. Freeze policy only when downstream architecture proves it necessary.

---

## Purpose

Schema Architecture translates the completed conceptual architecture into a formal production-oriented data model.

The Base Schema draws directly from:

```text
Identifiers
Controlled Values
Relationships
Provenance
```

and is now reconciled with the downstream architecture established through:

```text
Verification
Validation
Lifecycle
Versioning
Corrections
Publication
Maintenance
Production Procedures
```

---

## Canonical Object

The schema governs:

```text
Integrity Reference
```

It does not redefine or absorb the Source Artifact.

> Reference does not transfer authority.

---

## Current Schema

### Integrity Reference Base Schema

Markdown specification:

```text
/anchor/schemas/integrity-reference-base-schema.md
```

JSON Schema:

```text
/anchor/schemas/integrity-reference-base-schema.json
```

Schema standard:

```text
JSON Schema Draft 2020-12
```

---

## Top-Level Structure

```text
Integrity Reference
├── anchor_identifier
├── anchor_version
├── schema_version
├── source
├── representation
├── integrity
├── provenance
├── relationships
├── record_state
├── verification_history
├── corrections
├── publication
├── maintenance
└── notes
```

Required structural core:

```text
anchor_identifier
anchor_version
schema_version
source
representation
integrity
provenance
relationships
record_state
```

---

## Controlled Value Enforcement

The first production candidate has now proven the minimum vocabulary that must be machine-enforced.

The Base Schema now enforces:

```text
representation_type → canonical_json
method_type → cryptographic_digest
integrity_state → current
verification_result → match
publication_state → unpublished | published
lifecycle_state → draft | active | superseded | withdrawn | archived
relationship_type → references_source
```

Production records must also contain at least one:

```text
references_source
```

relationship.

Additional Controlled Value tokens remain outside the current schema enumeration until production proves they are necessary.

---

## Structural Strictness

The schema uses:

```text
additionalProperties: false
```

for governed record objects to prevent accidental schema drift.

Method-specific extension areas remain open where required, including:

```text
parameters
verification_material
proof_material
provenance sub-objects
```

This preserves institutional structure while allowing implementation-specific detail.

---

## Status

**Post-Foundational Architecture · First-Production Schema Reconciled**

The Integrity Reference now has a formal base data structure aligned with the first production candidate.

The schema now machine-enforces the minimum vocabulary required for:

```text
SCRD-SC-CERT-2026-0001
```

including:

```text
canonical_json
cryptographic_digest
current
match
unpublished
published
references_source
draft
active
superseded
withdrawn
archived
```

`schema_version` is now required for production candidates.

The following remain intentionally unfrozen or pending the next production decision:

```text
Anchor Identifier syntax
canonicalization / serialization method
digest algorithm
Integrity Value encoding
additional Controlled Value tokens
method-specific conditional requirements
Bitcoin-specific extension
Correction Type enumeration
separate Verification Record identity
first production Integrity Reference instance
```

**Version:** 1.0-draft

**Maintained By:** Satoshium
