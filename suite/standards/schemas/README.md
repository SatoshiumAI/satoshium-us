# Schemas Standard

## Overview

The **Satoshium Schemas Standard** defines Suite-wide expectations for machine-readable records, structured data models, canonical representations, validation-ready structures, and schema evolution.

Schemas describe governed representations and structural constraints. They do not themselves create canonical objects, canonical ownership, institutional authority, or substantive conclusions.

The governing principle is:

> Durable records require durable structure.

This Standard is shared across the Satoshium Suite. Individual institutions may specialize it, but should not redefine a Suite-wide structural concept merely because a local implementation needs it.

---

## Standard Role

The Schemas Standard provides the structural language that allows Satoshium records to be:

```text
created
validated
exchanged
preserved
interpreted
verified
```

consistently across Suite institutions.

---

## Record Models

Suite schemas may govern records including:

```text
Certification Package
Satoshium Registry Entry
Chronicle Entry
Integrity Reference
Discovery Signal / Metadata
Attestation
Trust Statement
Workflow Definition
Atlas structured records
supporting evidence / verification objects
```

Each institution remains authoritative for its own canonical object.

> Reference does not transfer authority.

The same constitutional discipline applies to schemas:

```text
SCHEMA
≠ CANONICAL OBJECT

SHARED SCHEMA
≠ SHARED OWNERSHIP

SCHEMA CONFORMANCE
≠ INSTITUTIONAL AUTHORITY
```

---

## Schema vs. Canonical Object

A schema defines the structure expected of a representation.

A canonical object is the institution-owned governed object whose identity, lifecycle, correction, versioning, publication, and substantive canonical state are controlled by the owning institution.

Therefore:

```text
Schema
→ structural contract / representation rules

Canonical Object
→ institution-owned governed object
```

A schema may describe one or more representations of a canonical object.

That does not make the schema the canonical object.

```text
SCHEMA
≠ CANONICAL OBJECT

MULTIPLE REPRESENTATIONS
≠ MULTIPLE AUTHORITIES
```

Canonical ownership remains where the Suite architecture assigns it.

## Required Fields

A production schema should identify the minimum structure necessary for the governed object to remain:

- identifiable;
- interpretable;
- validation-ready;
- interoperable;
- versionable;
- preservable;
- reviewable over time.

Required fields should be driven by institutional need rather than structural symmetry.

---

## Validation Rules

Structured Suite records should be validated before entering a governed production state when their institution requires formal validation.

Schema validation may establish structural conformance to the applicable schema.

Institutional Validation may additionally evaluate requirements that cannot be expressed completely in a machine schema.

Neither schema validation nor schema conformance independently establishes source authority, truth, certification, trust, publication state, lifecycle state, or canonical ownership.

```text
Schema conformance
≠
complete institutional Validation

Schema conformance
≠
source authority

Schema conformance
≠
certification / trust / publication
```

---

# Canonical JSON

A Suite record may declare a representation as:

```text
canonical_json
```

When it does, the Suite-wide canonicalization rule is:

```text
Canonicalization Standard
→ RFC 8785 — JSON Canonicalization Scheme (JCS)

Character Encoding
→ UTF-8
```

This rule exists so equivalent JSON data can be serialized deterministically for hashing, signing, verification, comparison, interchange, and long-term preservation.

---

## Canonical JSON Principle

A Suite institution must not use the `canonical_json` representation type while applying a conflicting institution-specific normalization scheme.

Conceptually:

```text
JSON data
        ↓
RFC 8785 JCS
        ↓
canonical UTF-8 JSON representation
```

Presentation-only differences such as indentation or insignificant whitespace should not create a different canonical representation.

Object-member presentation order in the source JSON should likewise not determine the canonical representation where JCS defines deterministic ordering.

---

## Representation Type vs. Media Type

`canonical_json` describes a governed representation type.

It does not replace the media type:

```text
application/json
```

or the character encoding:

```text
UTF-8
```

These concepts should remain distinct where recorded.

---

## Institutional Schema Profiles

Suite institutions may define narrower schema profiles where production requires additional constraints.

The hierarchy is:

```text
Suite Schema Standard
        ↓
Institutional Base Schema / Profile
        ↓
Production Record
```

An institutional profile may constrain:

- required fields;
- Controlled Values;
- conditional fields;
- object structure;
- method-specific requirements;

without contradicting Suite-wide rules.

An institutional profile may specialize structure, but specialization does not transfer canonical ownership to the Schemas layer or create shared ownership with other institutions.

---

## Shared Structure vs. Shared Ownership

The use of shared schema conventions improves interoperability.

It does not merge institutional objects or authority.

```text
SHARED STRUCTURE
≠ SHARED OWNERSHIP

SHARED FIELD NAME
≠ SHARED AUTHORITY

SHARED IDENTIFIER PATTERN
≠ SHARED CANONICAL IDENTITY

SCHEMA REUSE
≠ AUTHORITY TRANSFER
```

Where two institutions use similar or identical structural fields, each institution still owns the canonical object and lifecycle authority assigned to it by Suite architecture.

## Anchor Application

Satoshium Anchor's first production Integrity Reference uses a machine-readable SCRD JSON Source Artifact.

For that production case:

```text
Representation Type
→ canonical_json

Canonicalization
→ RFC 8785 JCS

Encoding
→ UTF-8
```

Anchor inherits these rules from the Suite Schema Standard.

Anchor does not create a separate local meaning for `canonical_json`.

---

# Schema Evolution

Suite schemas should support controlled evolution.

Evolution may include:

- new fields;
- stronger validation constraints;
- new Controlled Values;
- new profiles;
- deprecated fields;
- successor schema Versions.

Published historical records should remain interpretable under the schema and vocabulary that governed them.

---

# Relationship to Interoperability

Schemas define structure.

Interoperability defines how those structures are exchanged, referenced, and interpreted across systems.

Interoperability may require structural compatibility, but compatibility does not create canonical ownership or invalidate the source object merely because an exchange fails.

```text
Schemas
→ structure

Interoperability
→ shared interpretation and exchange
```

---

# Relationship to Institutional Authority

A Suite schema does not transfer authority over a record.

For example:

```text
Certifier schema
→ structures a Certifier record

Anchor schema
→ structures an Anchor Integrity Reference
```

Using shared Suite conventions does not merge those institutional objects.

The Schemas Standard also does not become the authority layer for those objects merely because it defines their machine-readable structure.

---

# Governance Boundary

Schema work operates within settled Suite architecture.

A schema change may alter representation requirements.

It may not silently alter:

- institutional role;
- canonical ownership;
- canonical object identity;
- Suite membership;
- authority allocation; or
- constitutional dependency.

If a proposed schema change would change one of those architectural matters, the issue must move to the applicable **Suite Governance / Architecture Reconciliation** process.

```text
SCHEMA CHANGE
≠ ARCHITECTURAL AUTHORITY

SCHEMA SOPHISTICATION
≠ CANONICALIZATION

CANONICALIZATION SIGNALS
≠ CANONICALIZATION
```

Canonical ownership may change only through explicit Constitutional Governance.

# Current Freeze Decisions

### Suite-Wide Canonical JSON Rule

```text
Representation Type → canonical_json
Canonicalization Standard → RFC 8785 JCS
Encoding → UTF-8
```

### Still Institution- or Production-Specific

```text
which records require canonical_json
institution-specific schema fields
institution-specific Controlled Values
method-specific profile constraints
publication requirements
validation procedures
canonical object ownership
institutional lifecycle authority
```

---

## Status

**Suite Standard · Production-Reconciled**

The Schemas Standard now defines the first Suite-wide canonical representation rule required by live production architecture.

**Version:** 1.0-draft

**Maintained By:** Satoshium


---

## Governing Principle

**Schemas define structure. Institutions own canonical objects. Shared structure improves interoperability without creating shared ownership or authority.**
