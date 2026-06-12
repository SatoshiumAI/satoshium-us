# Registry Record Schema

## Overview

This document defines the foundational schema used by Satoshium Registry.

The Registry Record Schema serves as the base structure from which all specialized Registry record types may be derived.

Examples include:

- Tool Records
- Jurisdiction Records
- Media Records
- Signal Records
- Certification Records
- Attestation Records
- Future Registry Record Types

The objective is to establish a consistent framework for organizing, cataloging, and preserving information across the Satoshium ecosystem.

---

## Schema Purpose

A Registry record should answer several foundational questions:

- What is this record?
- What category does it belong to?
- What is its current status?
- What information is associated with it?
- What records are related to it?
- How can it be found later?

This schema provides a common structure for answering those questions.

---

## Core Record Structure

```text
Identifier
Title
Record Type
Status
Description
References
Related Records
Metadata
```

Every Registry record should generally conform to this foundational structure.

---

## Required Fields

### Identifier

A unique Registry identifier.

Example:

```text
REG-0001
```

The identifier should remain stable over time whenever practical.

---

### Title

Human-readable record title.

Example:

```text
New Hampshire Orientation Video
```

Titles should be descriptive and understandable.

---

### Record Type

Defines the primary classification of the record.

Examples:

```text
Tool
Jurisdiction
Media
Signal
Certification
Attestation
Historical
Reference
```

Additional record types may be introduced in future versions.

---

### Status

Defines the current state of the record.

Examples:

```text
Draft
Active
Published
Superseded
Retired
Archived
```

Status values help communicate lifecycle state.

---

## Optional Fields

### Description

Narrative explanation of the record.

Descriptions provide context for future interpretation.

---

### References

Associated resources related to the record.

Examples:

- Documents
- Pages
- Reports
- Certifications
- Attestations
- Media resources

---

### Related Records

Cross-references to other Registry records.

Examples:

- Tool Records
- Jurisdiction Records
- Historical Records
- Certification Records

Cross-references improve discoverability.

---

### Notes

Additional information that may assist future understanding.

---

## Metadata Structure

Recommended metadata elements include:

| Field | Description |
|---------|---------|
| Identifier | Unique record identifier |
| Title | Human-readable title |
| Record Type | Primary classification |
| Status | Lifecycle status |
| Created | Creation date |
| Updated | Last update date |

Additional metadata may be added as requirements evolve.

---

## Relationship Mapping

Registry records may connect to one another.

Example:

```text
Tool
  ↓
Media
  ↓
Certification
```

or

```text
Jurisdiction
  ↓
Signal
  ↓
Historical Record
```

Relationship mapping improves continuity and interoperability.

---

## Record Lifecycle

Records may move through stages such as:

```text
Created
    ↓
Cataloged
    ↓
Referenced
    ↓
Maintained
    ↓
Preserved
```

Lifecycle processes may expand in future Registry versions.

---

## Specialized Schemas

This foundational schema serves as the basis for specialized schemas including:

- Tool Record Schema
- Jurisdiction Record Schema
- Media Record Schema
- Future Record Schemas

Specialized schemas may introduce additional required fields.

---

## Future Expansion

Future versions of this schema may support:

- Machine-readable formats
- Validation frameworks
- Relationship enforcement
- Metadata standards
- Integrity references
- Automated tooling

Future enhancements should remain aligned with Registry's organizational mission.

---

## Validation Considerations

A valid Registry record should generally include:

✓ Identifier

✓ Title

✓ Record Type

✓ Status

Additional fields may vary depending on record type.

---

## Guiding Statement

> Records preserve information.
>
> Schemas preserve structure.
>
> Registry depends upon both.

