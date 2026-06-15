# Source Reference Schema

## Purpose

The Source Reference Schema defines the structure used to represent information sources referenced by Beacon.

Sources provide the origin, context, attribution, and traceability necessary for responsible discovery.

This schema helps ensure that information surfaced by Beacon remains connected to its originating source whenever possible.

---

## Scope

This schema may be used for:

* Information sources
* Research sources
* Public records
* Registry records
* Historical sources
* Jurisdiction records
* Identity references
* Trust-related references

Implementations may evolve over time.

---

## Why Sources Matter

Discovery without attribution creates uncertainty.

Users should be able to understand:

* Where information originated
* Who created the information
* When the information was published
* How the information relates to discovery results

Source visibility is a core Beacon principle.

---

## Core Principles

### Attribution

Sources should remain identifiable.

### Transparency

Users should understand information origins.

### Traceability

Information should support historical review.

### Accessibility

Sources should be discoverable and understandable.

### Neutrality

Sources should be documented without implying endorsement.

---

## Source Structure

### Source Identifier

Unique identifier assigned to the source.

Example:

```text
SRC-2026-000001
```

---

### Source Type

Classification of the source.

Examples:

```text
Public Record
Government Record
Research Publication
Registry Record
Chronicle Entry
Atlas Record
Anchor Record
Attestor Record
Media Source
```

---

### Source Title

Human-readable title describing the source.

Example:

```text
Texas Jurisdiction Intelligence Record
```

---

### Source Description

Brief description of the source.

Example:

```text
Jurisdiction profile documenting information relevant to digital asset activity.
```

---

### Source Origin

Originating system, organization, or entity responsible for the source.

Examples:

```text
Atlas
Registry
Chronicle
Anchor
Attestor
Government Agency
Research Institution
Media Organization
```

---

### Source Author

Individual, organization, or system responsible for creating the source.

Example:

```text
Satoshium Atlas
```

---

### Publication Date

Date associated with publication or creation.

Example:

```text
2026-11-01
```

---

### Last Updated

Most recent modification date.

Example:

```text
2026-11-15
```

---

### Source Category

Broad category used for organization.

Examples:

```text
Jurisdiction
Media
Research
Government
Historical
Identity
Trust
Technology
```

---

### Source Format

Format associated with the source.

Examples:

```text
Record
Document
Dataset
Publication
Article
Report
Entry
Database
```

---

### Source Location

Reference or location where the source may be accessed.

Examples:

```text
URL
Repository Path
Record Identifier
Document Reference
```

---

### Source Identifier Reference

Reference used by the originating system.

Examples:

```text
REG-2026-000041
CHR-2026-000112
ANC-2026-000019
```

---

### Geographic Scope

Geographic area associated with the source.

Examples:

```text
Global
National
State
Regional
Local
```

---

### Topics

Primary subjects associated with the source.

Examples:

```text
Digital Assets
Artificial Intelligence
Taxation
Governance
Infrastructure
Privacy
```

---

### Related Sources

References to associated sources.

Examples:

```text
SRC-2026-000002
SRC-2026-000011
```

---

### Related Records

References to related records.

Examples:

```text
REG-2026-000041
CHR-2026-000112
```

---

### Verification Status

Optional indication of verification state.

Examples:

```text
Unknown
Verified
Partially Verified
Unverified
```

Verification status should not be interpreted as trustworthiness.

---

### Availability Status

Availability of the source.

Examples:

```text
Available
Archived
Restricted
Unavailable
```

---

### Metadata

Optional metadata associated with the source.

Examples:

```text
Jurisdiction
Topic
Date Range
Language
Record Type
```

---

### Source Status

Current status of the source reference.

Examples:

```text
Active
Archived
Superseded
Deprecated
```

---

### Created By

System or process responsible for recording the source.

Example:

```text
Beacon
```

---

### Created Date

Date the source reference was created.

Example:

```text
2026-11-01
```

---

## Example Record

```yaml
source_id: SRC-2026-000001

source_type: Atlas Record

title: Texas Jurisdiction Intelligence Record

description: >
  Jurisdiction profile documenting information
  relevant to digital asset activity.

source_origin: Atlas

source_author: Satoshium Atlas

publication_date: 2026-11-01

last_updated: 2026-11-15

source_category: Jurisdiction

source_format: Record

source_location: >
  atlas/jurisdictions/united-states/texas/

source_identifier_reference: TEXAS-JIE-001

geographic_scope: State

topics:
  - Digital Assets
  - Taxation

related_sources:
  - SRC-2026-000002

related_records:
  - REG-2026-000041

verification_status: Unknown

availability_status: Available

source_status: Active

created_by: Beacon

created_date: 2026-11-15
```

---

## Relationship to Other Schemas

This schema may reference:

* Beacon Record Schema
* Query Log Schema
* Signal Record Schema
* Discovery Result Schema

Additional schema relationships may be established over time.

---

## Relationship to Discovery

Sources provide context for discovery.

Discovery activities may:

* Locate sources
* Compare sources
* Organize sources
* Surface sources
* Connect sources to related records

Sources help users understand where information originated.

---

## Relationship to Signals

Signals should remain connected to supporting sources whenever possible.

A signal without a source provides limited context.

Source attribution improves transparency.

---

## Relationship to Results

Discovery results may reference one or more sources.

Users should be able to trace results back to supporting source material.

This supports review, investigation, and future verification.

---

## Future Development

Future source schemas may include:

* Source scoring
* Source reputation tracking
* Source relationship graphs
* Citation frameworks
* Source lineage tracking
* Cross-system source indexing

Specific implementations may evolve over time.

---

## Status

This schema represents an initial conceptual structure for source references and may be expanded, revised, or refined as Beacon capabilities mature.
