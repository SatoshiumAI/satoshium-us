# Beacon Record Schema

## Purpose

The Beacon Record Schema defines the structure used to represent discovery-related records within the Beacon system.

Beacon records provide a standardized method for documenting discovery activities, surfaced signals, related sources, associated queries, and resulting information.

The schema promotes consistency, traceability, interoperability, and future automation.

---

## Scope

This schema may be used for:

* Discovery records
* Signal discoveries
* Source discoveries
* Query activities
* Discovery events
* Discovery relationships
* Discovery metadata

Implementations may evolve over time.

---

## Core Principles

### Transparency

Discovery activities should remain understandable.

### Attribution

Source information should remain identifiable.

### Traceability

Discovery records should support historical review.

### Consistency

Records should follow predictable structures.

### Interoperability

Records should support exchange between systems.

---

## Record Structure

### Record Identifier

Unique identifier assigned to the Beacon record.

Example:

```text
BEC-2026-000001
```

---

### Record Type

Classification of the discovery activity.

Examples:

```text
Signal Discovery
Source Discovery
Query Discovery
Relationship Discovery
Multi-Source Discovery
```

---

### Record Title

Human-readable title describing the discovery.

Example:

```text
Jurisdiction Signal Discovery: Texas
```

---

### Discovery Date

Date the discovery activity occurred.

Example:

```text
2026-11-01
```

---

### Discovery Method

Method used to identify or surface information.

Examples:

```text
Search
Query
Index Lookup
Relationship Mapping
Signal Monitoring
Manual Discovery
```

---

### Associated Query

Reference to the query that initiated discovery.

Example:

```text
Find jurisdictions with favorable digital asset policies
```

---

### Discovery Summary

Brief description of the discovery.

Example:

```text
Discovery identified multiple jurisdiction records relevant to the submitted query.
```

---

### Signals Identified

Signals surfaced through discovery.

Examples:

```text
Regulatory Change
Policy Update
Record Creation
Historical Event
Media Publication
```

---

### Sources Identified

References to relevant information sources.

Example:

```text
Atlas Jurisdiction Record
Registry Record
Chronicle Entry
Public Source
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

### Relationship Notes

Description of identified relationships.

Example:

```text
Discovery revealed connections between multiple jurisdiction records and related historical events.
```

---

### Discovery Confidence

Optional assessment of discovery relevance.

Examples:

```text
High
Moderate
Low
Unknown
```

Discovery confidence should not be interpreted as verification or trust.

---

### Metadata

Optional metadata associated with the discovery.

Examples:

```text
Jurisdiction
Record Type
Topic
Date Range
Source Category
```

---

### Status

Current status of the discovery record.

Examples:

```text
Open
Active
Archived
Superseded
```

---

### Created By

Individual, organization, system, or process responsible for creating the record.

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
record_id: BEC-2026-000001

record_type: Signal Discovery

title: Jurisdiction Signal Discovery: Texas

discovery_date: 2026-11-01

discovery_method: Query

associated_query: >
  Find jurisdictions with favorable digital asset policies

summary: >
  Discovery identified multiple jurisdiction records
  relevant to the submitted query.

signals_identified:
  - Regulatory Change
  - Policy Update

sources_identified:
  - Atlas Jurisdiction Record
  - Registry Record

related_records:
  - REG-2026-000041
  - CHR-2026-000112

relationship_notes: >
  Discovery revealed relationships between
  jurisdiction records and historical events.

discovery_confidence: Moderate

status: Active

created_by: Beacon

last_updated: 2026-11-01
```

---

## Relationship to Other Schemas

This schema may reference:

* Signal Record Schema
* Discovery Result Schema
* Source Reference Schema
* Query Log Schema

Additional relationships may be established as Beacon evolves.

---

## Future Development

Future Beacon record schemas may include:

* Automated discovery tracking
* Signal prioritization
* Relationship graphs
* Cross-system discovery records
* Discovery audit trails
* Discovery analytics

Specific implementations may evolve over time.

---

## Status

This schema represents an initial conceptual structure for Beacon records and may be expanded, revised, or refined as Beacon capabilities mature.
