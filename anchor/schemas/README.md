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
source
representation
integrity
provenance
relationships
record_state
```

---

## Controlled Value Enforcement

The schema structurally supports Controlled Value fields such as:

```text
method_type
representation_type
relationship_type
integrity_state
verification_result
publication_state
lifecycle_state
correction_type
```

Most enumerations remain intentionally unfrozen until production proves which distinctions require permanent machine-level enforcement.

The first downstream Controlled Value enumeration is now frozen:

```text
Lifecycle State
→ draft
→ active
→ superseded
→ withdrawn
→ archived
```

The machine-readable Integrity Reference Base Schema now directly enforces those values for:

```text
record_state.lifecycle_state
```

The remaining Controlled Value categories continue to stay open until production evidence demonstrates the need to freeze them.

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

**Post-Foundational Architecture · Pre-Production Reconciled**

The Integrity Reference now has a formal base data structure, including the first downstream-frozen Controlled Value enforcement for Lifecycle State.

The first downstream production constraint now frozen and enforced is:

```text
Lifecycle State
→ draft
→ active
→ superseded
→ withdrawn
→ archived
```

The following remain intentionally unfrozen or pending production evidence:

```text
Anchor Identifier syntax
most Controlled Value enumerations
Relationship Type tokens
Integrity Method enumeration
Integrity Value encoding
canonicalization method enumeration
Verification Result enumeration
Integrity State enumeration
Publication State enumeration
conditional method requirements
Bitcoin-specific extension
Correction schema
method-specific schema/profile requirements
first production Integrity Reference instance
```

**Version:** 1.0-draft

**Maintained By:** Satoshium
