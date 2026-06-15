# Query Log Schema

## Purpose

The Query Log Schema defines the structure used to document discovery requests processed by Beacon.

Query logs provide a record of user intent, discovery activities, search parameters, and associated outcomes.

The schema supports transparency, traceability, auditing, analytics, and future discovery improvements.

---

## Scope

This schema may be used for:

* Discovery requests
* Search activities
* Research queries
* Investigative queries
* Exploratory queries
* Automated discovery processes
* Cross-system discovery operations

Implementations may evolve over time.

---

## Core Principles

### Transparency

Discovery requests should remain understandable.

### Traceability

Queries should support historical review.

### Accountability

Discovery activities should be documentable.

### Consistency

Query records should follow predictable structures.

### Interoperability

Query records should support exchange across systems.

---

## Query Structure

### Query Identifier

Unique identifier assigned to the query.

Example:

```text
QRY-2026-000001
```

---

### Query Type

Classification of the discovery request.

Examples:

```text
Search Query
Research Query
Investigative Query
Exploratory Query
Automated Query
Relationship Query
```

---

### Query Title

Human-readable title describing the request.

Example:

```text
Digital Asset Friendly Jurisdictions
```

---

### Query Date

Date the query was submitted.

Example:

```text
2026-11-01
```

---

### Query Text

Original query submitted to Beacon.

Example:

```text
Find jurisdictions with favorable digital asset policies.
```

---

### Query Objective

Description of the intended discovery outcome.

Example:

```text
Identify jurisdictions relevant to digital asset businesses.
```

---

### Query Scope

Boundaries associated with the request.

Examples:

```text
Global
National
State
Historical
Media
Identity
Registry
```

---

### Query Parameters

Optional parameters used during discovery.

Examples:

```text
Date Range
Jurisdiction
Topic
Record Type
Source Type
Confidence Threshold
```

---

### Discovery Method

Method used to process the query.

Examples:

```text
Search
Index Lookup
Signal Discovery
Relationship Mapping
Cross-System Discovery
```

---

### Sources Consulted

Sources examined during discovery.

Examples:

```text
Atlas
Registry
Chronicle
Anchor
Attestor
Public Sources
```

---

### Results Generated

Number of results generated.

Example:

```text
27
```

---

### Related Result Records

References to associated discovery results.

Examples:

```text
DRS-2026-000041
DRS-2026-000042
DRS-2026-000043
```

---

### Query Status

Current state of the query.

Examples:

```text
Submitted
Processing
Completed
Archived
Failed
```

---

### Processing Duration

Optional measurement of discovery processing time.

Example:

```text
3.4 seconds
```

---

### Notes

Optional observations associated with the query.

Example:

```text
Discovery produced multiple related jurisdiction records.
```

---

### Submitted By

Individual, organization, system, or process responsible for the query.

Examples:

```text
User
Navigator
Beacon
Automated Process
```

---

### Created Timestamp

Timestamp associated with query creation.

Example:

```text
2026-11-01T14:22:10Z
```

---

### Last Updated

Most recent modification timestamp.

Example:

```text
2026-11-01T14:22:14Z
```

---

## Example Record

```yaml
query_id: QRY-2026-000001

query_type: Research Query

title: Digital Asset Friendly Jurisdictions

query_date: 2026-11-01

query_text: >
  Find jurisdictions with favorable digital
  asset policies.

query_objective: >
  Identify jurisdictions relevant to digital
  asset businesses.

query_scope: Global

query_parameters:
  topic: Digital Assets
  record_type: Jurisdiction

discovery_method: Cross-System Discovery

sources_consulted:
  - Atlas
  - Registry
  - Chronicle

results_generated: 27

related_results:
  - DRS-2026-000041
  - DRS-2026-000042
  - DRS-2026-000043

query_status: Completed

processing_duration: 3.4 seconds

notes: >
  Discovery produced multiple related
  jurisdiction records.

submitted_by: User

created_timestamp: 2026-11-01T14:22:10Z

last_updated: 2026-11-01T14:22:14Z
```

---

## Relationship to Other Schemas

This schema may reference:

* Beacon Record Schema
* Discovery Result Schema
* Signal Record Schema
* Source Reference Schema

Additional schema relationships may be established over time.

---

## Relationship to Navigator

Navigator may generate, refine, organize, or execute queries.

Beacon may process those queries and produce discovery results.

A simplified interaction may be represented as:

```text
Navigator → Query → Beacon
```

---

## Relationship to Discovery

Queries initiate discovery.

Discovery activities are performed in response to queries.

Results are generated from those activities.

A simplified workflow may be represented as:

```text
Query
  ↓
Discovery
  ↓
Result
```

---

## Query Analytics

Future implementations may use query logs to support:

* Discovery optimization
* Signal analysis
* Query trends
* Relationship mapping
* Search improvements
* User experience improvements

Specific implementations may evolve over time.

---

## Privacy Considerations

Implementations may choose to:

* Store queries
* Anonymize queries
* Aggregate query statistics
* Limit retention periods

Privacy policies should be documented separately.

---

## Future Development

Future query log schemas may include:

* Query versioning
* Query history
* Query refinement tracking
* Relationship analytics
* Multi-system discovery tracking
* Automated query orchestration

Specific implementations may evolve over time.

---

## Status

This schema represents an initial conceptual structure for query logging and may be expanded, revised, or refined as Beacon capabilities mature.
