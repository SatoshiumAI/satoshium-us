# Correction Record Schema

## Purpose

The Correction Record Schema defines the structure used to document modifications, clarifications, updates, and corrections to Chronicle records.

Corrections are intended to improve the accuracy, completeness, and transparency of the historical record while preserving historical traceability.

Rather than removing information, Chronicle favors documenting how and why records evolve over time.

---

## Schema Overview

A correction record should answer the following questions:

* What record was affected?
* What was changed?
* Why was the change made?
* When was the correction made?
* What evidence supports the correction?
* Who initiated the correction?

---

## Required Fields

### correction_id

Unique identifier assigned to the correction.

Example:

```text
COR-000001
```

### title

Short descriptive title.

Example:

```text
Correction to Initial Launch Date
```

### correction_type

Classification of correction.

Examples:

```text
factual
clarification
evidence_update
metadata
administrative
reclassification
```

### affected_record

Identifier of the record being corrected.

Example:

```text
CHR-ENTRY-000001
```

### correction_summary

Brief explanation of the correction.

Example:

```text
Original publication date was incorrectly recorded.
```

### correction_timestamp

Date and time the correction was recorded.

Example:

```text
2026-10-15T14:22:00Z
```

### status

Current correction status.

Examples:

```text
draft
active
superseded
archived
```

---

## Recommended Fields

### description

Detailed explanation of the correction.

### reason

Explanation of why the correction was necessary.

### significance

Description of the impact of the correction.

### requested_by

Entity that requested the correction.

### reviewed_by

Entity responsible for review.

---

## Change Documentation Fields

### previous_value

Original value or state.

Example:

```text
2026-09-02
```

### corrected_value

Updated value or state.

Example:

```text
2026-09-01
```

### change_summary

Human-readable explanation of the modification.

Example:

```text
Launch date updated to reflect official publication records.
```

---

## Relationship Fields

### source_references

Sources supporting the correction.

Example:

```text
SRC-000014
```

### evidence_references

Evidence supporting the correction.

Example:

```text
EVD-000021
```

### related_entries

Associated Chronicle entries.

Example:

```text
CHR-ENTRY-000001
```

### related_corrections

Other corrections connected to this record.

Example:

```text
COR-000005
```

---

## Verification Fields

### verification_status

Current confidence assessment.

Examples:

```text
unverified
under_review
verified
disputed
```

### verification_reference

Optional verification record.

Example:

```text
VER-000004
```

---

## Metadata Fields

### author

Entity that created the correction record.

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
correction_id: COR-000001

title: Correction to Initial Launch Date

correction_type: factual

affected_record: CHR-ENTRY-000001

correction_summary: >
  Original launch date was recorded incorrectly.

previous_value: 2026-09-02
corrected_value: 2026-09-01

change_summary: >
  Launch date updated to reflect official publication records.

correction_timestamp: 2026-10-15T14:22:00Z

status: active

verification_status: verified

source_references:
  - SRC-000014

evidence_references:
  - EVD-000021

created_at: 2026-10-15T14:22:00Z
updated_at: 2026-10-15T14:22:00Z

version: 1.0
```

---

## Design Goals

The Correction Record Schema seeks to:

* Preserve historical transparency
* Improve accuracy
* Maintain traceability
* Document change history
* Support evidence-based review
* Reduce information loss
* Preserve confidence in the historical record

---

## Preservation Principles

Corrections should supplement the historical record rather than erase it.

Whenever practical:

* Original records remain accessible
* Corrections remain visible
* Historical relationships remain intact
* Reviewers can reconstruct record history

The objective is not to hide mistakes.

The objective is to document how understanding evolved.

---

## Future Development

Future versions may support:

* Structured change tracking
* Digital signatures
* Multi-party review workflows
* Cryptographic integrity verification
* Immutable correction chains
* Distributed correction registries

---

## Status

Draft schema.

This schema serves as the initial structure for Chronicle correction records and may evolve as Chronicle develops.

