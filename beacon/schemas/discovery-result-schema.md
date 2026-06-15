# Discovery Result Schema

## Purpose

The Discovery Result Schema defines the structure used to represent information returned through Beacon discovery activities.

Discovery results are the outputs generated when Beacon processes a query, investigation, search, exploration, or signal discovery request.

The schema promotes consistency, transparency, interoperability, and traceability across discovery operations.

---

## Scope

This schema may be used for:

* Query results
* Discovery outputs
* Search results
* Signal results
* Source results
* Relationship discoveries
* Cross-system discoveries

Implementations may evolve over time.

---

## Core Principles

### Transparency

Users should understand why a result was returned.

### Attribution

Source information should remain visible.

### Relevance

Results should relate to the discovery objective.

### Traceability

Results should support verification and review.

### Interoperability

Results should support exchange between systems.

---

## Result Structure

### Result Identifier

Unique identifier assigned to the discovery result.

Example:

```text
DRS-2026-000001
```

---

### Result Type

Classification of the result.

Examples:

```text
Signal Result
Source Result
Record Result
Relationship Result
Jurisdiction Result
Historical Result
Identity Result
```

---

### Result Title

Human-readable title describing the result.

Example:

```text
Texas Digital Asset Jurisdiction Record
```

---

### Discovery Date

Date the result was generated or surfaced.

Example:

```text
2026-11-01
```

---

### Associated Query

Reference to the originating query.

Example:

```text
Find jurisdictions with favorable digital asset policies
```

---

### Summary

Brief description of the result.

Example:

```text
Jurisdiction record identified as relevant to the submitted query.
```

---

### Result Category

Category used to organize the result.

Examples:

```text
Jurisdiction
Media
Historical
Identity
Registry
Certification
Trust
Research
```

---

### Primary Source

Primary source associated with the result.

Example:

```text
Atlas Jurisdiction Record
```

---

### Supporting Sources

Additional sources related to the result.

Example:

```text
Registry Record
Chronicle Entry
Public Record
```

---

### Related Records

References to associated records.

Examples:

```text
REG-2026-000041
CHR-2026-000112
ANC-2026-000019
```

---

### Signals Identified

Signals associated with the result.

Examples:

```text
Policy Change
Regulatory Update
Record Creation
Historical Event
```

---

### Relationship Notes

Description of relevant relationships.

Example:

```text
Result connected to multiple historical and regulatory records.
```

---

### Relevance Assessment

Optional assessment of relevance.

Examples:

```text
High
Moderate
Low
Unknown
```

Relevance should not be interpreted as verification or trust.

---

### Confidence Assessment

Optional assessment of discovery confidence.

Examples:

```text
High
Moderate
Low
Unknown
```

Confidence should not be interpreted as certification or validation.

---

### Metadata

Optional metadata associated with the result.

Examples:

```text
Jurisdiction
Date Range
Topic
Source Type
Record Type
```

---

### Status

Current status of the result.

Examples:

```text
Active
Archived
Superseded
Pending Review
```

---

### Created By

System or process responsible for generating the result.

Example:

```text
Beacon
```

---

### Last Updated

Most recent modification date.

Example:

```text
2026-11-01
```

---

## Example Record

```yaml
result_id: DRS-2026-000001

result_type: Jurisdiction Result

title: Texas Digital Asset Jurisdiction Record

discovery_date: 2026-11-01

associated_query: >
  Find jurisdictions with favorable digital asset policies

summary: >
  Jurisdiction record identified as relevant
  to the submitted query.

result_category: Jurisdiction

primary_source: Atlas Jurisdiction Record

supporting_sources:
  - Registry Record
  - Chronicle Entry

related_records:
  - REG-2026-000041
  - CHR-2026-000112

signals_identified:
  - Policy Change
  - Regulatory Update

relationship_notes: >
  Connected to multiple related regulatory
  and historical records.

relevance_assessment: High

confidence_assessment: Moderate

status: Active

created_by: Beacon

last_updated: 2026-11-01
```

---

## Relationship to Other Schemas

This schema may reference:

* Beacon Record Schema
* Signal Record Schema
* Source Reference Schema
* Query Log Schema

Additional schema relationships may be established as Beacon evolves.

---

## Relationship to Discovery

Discovery activities generate results.

Results represent the information surfaced through the discovery process.

A simplified workflow may be represented as:

```text
Query → Discovery → Result
```

---

## Future Development

Future discovery result schemas may include:

* Ranked results
* Relationship graphs
* Signal prioritization
* Result clustering
* Context-aware discovery
* Multi-source aggregation
* Cross-system discovery outputs

Specific implementations may evolve over time.

---

## Status

This schema represents an initial conceptual structure for discovery results and may be expanded, revised, or refined as Beacon capabilities mature.
