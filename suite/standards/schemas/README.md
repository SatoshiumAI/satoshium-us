# Schemas Standard

## Overview

The **Satoshium Schemas Standard** defines Suite-wide expectations for machine-readable records, structured data models, canonical representations, validation-ready objects, and schema evolution.

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
Trust Statement
Workflow Definition
Atlas structured records
supporting evidence / verification objects
```

Each institution remains authoritative for its own canonical object.

> Reference does not transfer authority.

---

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

Schema validation may establish structural conformance.

Institutional Validation may additionally evaluate requirements that cannot be expressed completely in a machine schema.

```text
Schema conformance
≠
complete institutional Validation
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

---

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

---

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
```

---

## Status

**Suite Standard · Production-Reconciled**

The Schemas Standard now defines the first Suite-wide canonical representation rule required by live production architecture.

**Version:** 1.0-draft

**Maintained By:** Satoshium
