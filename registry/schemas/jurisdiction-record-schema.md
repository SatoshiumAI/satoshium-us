# Jurisdiction Record Schema

## Overview

This document defines the recommended schema for Jurisdiction Records within Satoshium Registry.

The purpose of this schema is to establish a consistent structure for documenting countries, states, provinces, territories, regions, and future jurisdiction classifications.

Schemas improve discoverability, interoperability, continuity, and long-term maintainability.

---

## Schema Purpose

A jurisdiction record should answer several foundational questions:

- What jurisdiction is being referenced?
- What type of jurisdiction is it?
- What parent jurisdiction does it belong to?
- What related resources exist?
- What is its current Registry status?

This schema provides a framework for answering those questions consistently.

---

## Core Record Structure

```text
Identifier
Title
Record Type
Status
Jurisdiction Type
Parent Jurisdiction
Description
References
Related Records
Metadata
```

---

## Required Fields

### Identifier

A unique Registry identifier.

Example:

```text
JUR-US-CA-0001
```

---

### Title

Human-readable jurisdiction name.

Example:

```text
California
```

---

### Record Type

The record category.

Value:

```text
Jurisdiction
```

---

### Status

Current Registry status.

Examples:

```text
Draft
Active
Superseded
Retired
Archived
```

---

### Jurisdiction Type

Defines the classification of the jurisdiction.

Examples:

```text
Country
State
Province
Territory
Region
District
```

Additional types may be introduced in future versions.

---

### Parent Jurisdiction

Identifies the jurisdiction hierarchy.

Example:

```text
United States
```

---

## Optional Fields

### Description

Narrative description of the jurisdiction.

Example:

```text
California is a state located within the United States.
```

---

### References

Associated resources related to the jurisdiction.

Examples:

- Atlas pages
- Media resources
- Certification records
- Attestation records

---

### Related Records

Cross-references to other Registry records.

Examples:

- Tool Records
- Media Records
- Historical Records

---

### Notes

Additional context that may assist future interpretation.

---

## Example Metadata Structure

| Field | Example |
|---------|---------|
| Identifier | JUR-US-CA-0001 |
| Title | California |
| Record Type | Jurisdiction |
| Status | Active |
| Jurisdiction Type | State |
| Parent Jurisdiction | United States |

---

## Hierarchical Representation

Jurisdiction records may be represented hierarchically.

Example:

```text
World
 └── United States
      └── California
```

Hierarchies improve discoverability and organization.

---

## Relationship Mapping

Jurisdiction records may connect to:

```text
Atlas
Media
Certification
Attestation
Historical
Reference
```

Relationship mapping improves interoperability across the ecosystem.

---

## Future Expansion

Future versions of this schema may include:

- Geographic identifiers
- Jurisdiction codes
- Regional relationships
- Historical jurisdiction tracking
- Machine-readable metadata
- Automated validation

Future enhancements should remain aligned with Registry's organizational mission.

---

## Validation Considerations

A valid jurisdiction record should generally include:

✓ Identifier

✓ Title

✓ Record Type

✓ Status

✓ Jurisdiction Type

Additional fields may vary depending on implementation requirements.

---

## Guiding Statement

> Jurisdictions define places.
>
> Schemas provide the structure needed to document those places consistently.

