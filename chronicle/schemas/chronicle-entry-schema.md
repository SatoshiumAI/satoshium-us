# Chronicle Entry Schema

## Purpose

The Chronicle Entry Schema defines the structure used to represent historical entries within Chronicle.

Entries are the primary records of historical activity and may describe events, observations, decisions, publications, milestones, investigations, or other significant occurrences.

The schema provides a consistent framework for preserving historical information while supporting verification, evidence, corrections, and long-term archival use.

---

## Schema Overview

A Chronicle entry should answer the following questions:

* What happened?
* When did it happen?
* When was it recorded?
* Why is it significant?
* What evidence supports it?
* What sources describe it?
* What is the current verification status?

---

## Required Fields

### entry_id

Unique identifier assigned to the entry.

Example:

```text
CHR-ENTRY-000001
```

### title

Short descriptive title.

Example:

```text
Initial Chronicle Launch
```

### summary

Brief summary of the event or subject.

Example:

```text
Chronicle was publicly introduced as a historical preservation component of the Satoshium ecosystem.
```

### entry_type

Classification of the entry.

Examples:

```text
event
publication
observation
decision
milestone
investigation
correction
reference
```

### event_timestamp

Date and time associated with the historical event.

Example:

```text
2026-09-01T00:00:00Z
```

### recorded_timestamp

Date and time the entry was recorded within Chronicle.

Example:

```text
2026-09-01T12:30:00Z
```

### status

Current lifecycle state.

Examples:

```text
draft
active
archived
superseded
corrected
```

---

## Recommended Fields

### description

Extended narrative describing the entry.

### significance

Explanation of why the entry is historically relevant.

### tags

Keywords used for organization and discovery.

Example:

```text
chronicle
launch
satoshium
history
```

### jurisdiction

Optional geographic, organizational, or operational scope.

Example:

```text
global
```

---

## Relationship Fields

### source_references

References to associated source records.

Example:

```text
SRC-000014
SRC-000027
```

### evidence_references

References to supporting evidence records.

Example:

```text
EVD-000002
EVD-000009
```

### correction_references

References to correction records affecting the entry.

Example:

```text
COR-000001
```

### related_entries

References to other Chronicle entries.

Example:

```text
CHR-ENTRY-000015
CHR-ENTRY-000021
```

---

## Verification Fields

### verification_status

Current confidence assessment.

Examples:

```text
unverified
under_review
partially_verified
verified
disputed
```

### verification_reference

Optional reference to supporting verification records.

Example:

```text
VER-000003
```

---

## Metadata Fields

### author

Entity that created the entry.

### version

Current schema version.

Example:

```text
1.0
```

### created_at

System creation timestamp.

### updated_at

Most recent modification timestamp.

---

## Example Record

```yaml
entry_id: CHR-ENTRY-000001

title: Initial Chronicle Launch

summary: >
  Chronicle was publicly introduced as a historical
  preservation component of the Satoshium ecosystem.

entry_type: milestone

event_timestamp: 2026-09-01T00:00:00Z
recorded_timestamp: 2026-09-01T12:30:00Z

status: active

verification_status: verified

tags:
  - chronicle
  - satoshium
  - launch

source_references:
  - SRC-000001

evidence_references:
  - EVD-000001

created_at: 2026-09-01T12:30:00Z
updated_at: 2026-09-01T12:30:00Z

version: 1.0
```

---

## Design Goals

The Chronicle Entry Schema seeks to:

* Preserve historical context
* Support evidence-based review
* Enable traceability
* Maintain interoperability
* Support long-term archival use
* Remain understandable to both humans and machines

---

## Future Development

Future versions may support:

* Digital signatures
* Cryptographic integrity verification
* Distributed storage references
* Structured relationship mapping
* Attestation references
* AI-assisted classification

---

## Status

Draft schema.

This schema serves as the initial structure for Chronicle entries and may evolve as Chronicle develops.

