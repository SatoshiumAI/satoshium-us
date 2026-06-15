# Signal Record Schema

## Purpose

The Signal Record Schema defines the structure used to represent signals identified through Beacon discovery activities.

Signals are observations, events, changes, indicators, records, updates, or other noteworthy information that may be relevant to users, systems, investigations, or discovery processes.

The schema promotes consistency, transparency, traceability, and interoperability.

---

## Scope

This schema may be used for:

* Discovery signals
* Information signals
* Jurisdiction signals
* Historical signals
* Media signals
* Registry signals
* Identity signals
* Trust-related signals

Implementations may evolve over time.

---

## What Is a Signal?

A signal is information that may warrant attention.

Signals may represent:

* Events
* Changes
* Observations
* Records
* Updates
* Relationships
* Emerging developments

A signal does not imply importance, accuracy, verification, or trustworthiness.

A signal indicates that information may be relevant.

---

## Core Principles

### Visibility

Signals should help surface potentially relevant information.

### Transparency

Signal origins should remain visible.

### Attribution

Sources should remain identifiable.

### Traceability

Signals should support review and investigation.

### Neutrality

Signals should not imply conclusions.

---

## Signal Structure

### Signal Identifier

Unique identifier assigned to the signal.

Example:

```text
SIG-2026-000001
```

---

### Signal Type

Classification of the signal.

Examples:

```text
Regulatory Signal
Historical Signal
Media Signal
Identity Signal
Registry Signal
Trust Signal
Research Signal
```

---

### Signal Title

Human-readable title describing the signal.

Example:

```text
Texas Digital Asset Policy Update
```

---

### Signal Date

Date associated with the signal.

Example:

```text
2026-11-01
```

---

### Signal Category

Broad category used for organization.

Examples:

```text
Jurisdiction
Media
Policy
Research
Identity
History
Technology
Trust
```

---

### Summary

Brief description of the signal.

Example:

```text
Jurisdiction record updated with new digital asset policy information.
```

---

### Signal Description

Detailed explanation of the signal.

Example:

```text
A regulatory update was identified that may affect digital asset businesses operating within the jurisdiction.
```

---

### Signal Source

Primary source associated with the signal.

Example:

```text
Atlas Jurisdiction Record
```

---

### Supporting Sources

Additional sources related to the signal.

Examples:

```text
Registry Record
Chronicle Entry
Public Source
Research Publication
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

### Related Signals

References to associated signals.

Examples:

```text
SIG-2026-000002
SIG-2026-000015
```

---

### Geographic Scope

Area associated with the signal.

Examples:

```text
Global
National
State
Regional
Local
```

---

### Topic

Primary subject matter associated with the signal.

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

### Discovery Method

Method used to identify the signal.

Examples:

```text
Search
Monitoring
Manual Review
Relationship Mapping
Cross-System Discovery
```

---

### Signal Status

Current status of the signal.

Examples:

```text
Active
Archived
Superseded
Monitoring
Closed
```

---

### Signal Confidence

Optional assessment of confidence.

Examples:

```text
High
Moderate
Low
Unknown
```

Confidence does not imply verification or certification.

---

### Signal Relevance

Optional assessment of relevance.

Examples:

```text
High
Moderate
Low
Unknown
```

Relevance may vary depending on user objectives.

---

### Metadata

Optional metadata associated with the signal.

Examples:

```text
Jurisdiction
Topic
Date Range
Source Type
Record Type
```

---

### Created By

System or process responsible for recording the signal.

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
signal_id: SIG-2026-000001

signal_type: Regulatory Signal

title: Texas Digital Asset Policy Update

signal_date: 2026-11-01

signal_category: Policy

summary: >
  Jurisdiction record updated with new
  digital asset policy information.

description: >
  A regulatory update was identified that may
  affect digital asset businesses operating
  within the jurisdiction.

signal_source: Atlas Jurisdiction Record

supporting_sources:
  - Registry Record
  - Chronicle Entry

related_records:
  - REG-2026-000041
  - CHR-2026-000112

related_signals:
  - SIG-2026-000002

geographic_scope: State

topic: Digital Assets

discovery_method: Monitoring

signal_status: Active

signal_confidence: Moderate

signal_relevance: High

created_by: Beacon

last_updated: 2026-11-01
```

---

## Relationship to Other Schemas

This schema may reference:

* Beacon Record Schema
* Discovery Result Schema
* Source Reference Schema
* Query Log Schema

Additional schema relationships may be established over time.

---

## Relationship to Discovery

Signals represent information surfaced through discovery.

A signal may:

* Generate additional investigation
* Lead to new queries
* Produce discovery results
* Reveal relationships
* Trigger future monitoring

Signals are one of the primary outputs of Beacon.

---

## Relationship to Sources

Signals should remain connected to their sources whenever possible.

Users should be able to determine:

* Where information originated
* Which sources support the signal
* How the signal was discovered

Source visibility remains an important Beacon principle.

---

## Relationship to the Satoshium Suite

Signals may originate from:

* Atlas
* Navigator
* Certifier
* Registry
* Chronicle
* Anchor
* Attestor

Beacon helps surface those signals for discovery.

---

## Future Development

Future signal schemas may include:

* Signal scoring
* Signal prioritization
* Signal clustering
* Relationship graphs
* Alerting systems
* Monitoring systems
* Automated signal generation

Specific implementations may evolve over time.

---

## Status

This schema represents an initial conceptual structure for signal records and may be expanded, revised, or refined as Beacon capabilities mature.
