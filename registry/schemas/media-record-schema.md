# Media Record Schema

## Overview

This document defines the recommended schema for Media Records within Satoshium Registry.

The purpose of this schema is to establish a consistent structure for documenting videos, images, thumbnails, audio resources, documents, media pages, and future media assets.

Schemas improve discoverability, interoperability, continuity, and long-term maintainability.

---

## Schema Purpose

A media record should answer several foundational questions:

- What media resource is being referenced?
- What type of media is it?
- What resource is it associated with?
- What related records exist?
- What is its current Registry status?

This schema provides a framework for answering those questions consistently.

---

## Core Record Structure

```text
Identifier
Title
Record Type
Status
Media Type
Associated Resource
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
MED-US-NH-0001
```

---

### Title

Human-readable media title.

Example:

```text
New Hampshire Orientation Video
```

---

### Record Type

The record category.

Value:

```text
Media
```

---

### Status

Current Registry status.

Examples:

```text
Draft
Active
Published
Superseded
Archived
```

---

### Media Type

Defines the category of media.

Examples:

```text
Video
Image
Thumbnail
Audio
Document
Media Page
```

Additional media categories may be introduced in future versions.

---

### Associated Resource

The primary resource associated with the media.

Examples:

```text
Atlas
Certifier
Registry
Chronicle
Anchor
Attestor
```

---

## Optional Fields

### Description

Narrative description of the media resource.

Example:

```text
Orientation video introducing New Hampshire jurisdiction resources.
```

---

### References

Associated resources related to the media.

Examples:

- Atlas pages
- Certification records
- Attestation records
- Historical references

---

### Related Records

Cross-references to other Registry records.

Examples:

- Tool Records
- Jurisdiction Records
- Historical Records

---

### Notes

Additional context that may assist future interpretation.

---

## Example Metadata Structure

| Field | Example |
|---------|---------|
| Identifier | MED-US-NH-0001 |
| Title | New Hampshire Orientation Video |
| Record Type | Media |
| Status | Active |
| Media Type | Video |
| Associated Resource | Atlas |

---

## Relationship Mapping

Media records may connect to:

```text
Tool Records
Jurisdiction Records
Certification Records
Attestation Records
Historical Records
Reference Records
```

Relationship mapping improves interoperability across the ecosystem.

---

## Media Relationships

Example:

```text
Atlas
  ↓
Media Record
  ↓
New Hampshire
```

or

```text
Jurisdiction
  ↓
Media Record
  ↓
Certification
```

Registry helps preserve these relationships.

---

## Future Expansion

Future versions of this schema may include:

- Media metadata standards
- Content classifications
- Preservation references
- Integrity references
- Automated validation
- Machine-readable schemas

Future enhancements should remain aligned with Registry's organizational mission.

---

## Validation Considerations

A valid media record should generally include:

✓ Identifier

✓ Title

✓ Record Type

✓ Status

✓ Media Type

Additional fields may vary depending on implementation requirements.

---

## Guiding Statement

> Media communicates information.
>
> Schemas provide the structure needed to preserve references to that information consistently.

