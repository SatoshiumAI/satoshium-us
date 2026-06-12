# Registry Schemas

## Overview

The schemas directory contains structural models for Satoshium Registry records.

Schemas define the expected fields, relationships, classifications, and metadata patterns used to create consistent Registry records across the Satoshium ecosystem.

Schemas support organization, interoperability, automation, validation, and long-term maintainability.

---

## Purpose

Schemas exist to answer questions such as:

- What fields should a record include?
- How should records be structured?
- How should metadata be organized?
- How should related records be referenced?
- How can different record types remain consistent?

Schemas provide the structural foundation for answering those questions.

---

## Current Schema Files

This directory is expected to contain files such as:

```text
schemas/
├── README.md
├── registry-record-schema.md
├── tool-record-schema.md
├── jurisdiction-record-schema.md
└── media-record-schema.md
```

Additional schemas may be added as Registry evolves.

---

## Schema Objectives

Registry schemas are designed to support:

### Consistency

Records should follow predictable structures.

### Discoverability

Structured fields make records easier to search, index, and understand.

### Interoperability

Schemas help Registry interact with other Satoshium systems.

### Validation

Schemas may eventually support automated checks and review processes.

### Preservation

Structured records are easier to preserve and interpret over time.

---

## Core Schema Concepts

### Identifier

A unique value assigned to a Registry record.

### Title

A human-readable name for the record.

### Record Type

The primary category assigned to the record.

### Status

The current condition of the record.

### Metadata

Descriptive information associated with the record.

### References

Links or references to related resources.

### Related Records

Connections to other Registry records.

---

## Relationship to Record Types

Schemas support specific record types.

Examples include:

- Tool Records
- Jurisdiction Records
- Media Records
- Signal Records
- Certification Records
- Attestation Records

Each record type may require specialized fields.

---

## Relationship to Policies

Schemas define structure.

Policies define process.

```text
Schemas describe what a record looks like.
Policies describe how records are created, updated, corrected, or retired.
```

Both are necessary for reliable Registry operations.

---

## Future Development

Future schema capabilities may include:

- Machine-readable schema files
- Automated validation
- Versioned schemas
- Expanded metadata requirements
- Cross-reference enforcement
- Integration with Certifier, Chronicle, Anchor, and Attestor

Future enhancements should remain aligned with Registry's organizational mission.

---

## Schema Philosophy

A record is easier to preserve when its structure is clear.

Schemas provide that structure.

---

## Guiding Statement

> Records need structure.
>
> Structure requires schemas.
>
> Registry begins by defining both.

