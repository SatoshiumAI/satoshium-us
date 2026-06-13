# Evidence Record Schema

## Purpose

The Evidence Record Schema defines the structure used to represent evidence within Chronicle.

Evidence records preserve materials that support, challenge, clarify, or contextualize historical entries, claims, events, and conclusions.

Evidence exists to improve transparency and support independent review.

The existence of evidence does not determine truth. Instead, evidence provides information that may contribute to verification and historical understanding.

---

## Schema Overview

An evidence record should answer the following questions:

* What is the evidence?
* Where did it originate?
* When was it collected?
* How does it relate to Chronicle records?
* Has it been verified?
* Can its integrity be assessed?

---

## Required Fields

### evidence_id

Unique identifier assigned to the evidence record.

Example:

```text
EVD-000001
```

### title

Short descriptive title.

Example:

```text
Screenshot of Initial Chronicle Launch
```

### evidence_type

Classification of evidence.

Examples:

```text
document
image
video
audio
digital_record
physical_artifact
testimonial
measurement
log
archive
```

### description

Brief description of the evidence.

Example:

```text
Homepage screenshot captured on launch day.
```

### collection_timestamp

Date and time the evidence was collected or recorded.

Example:

```text
2026-09-01T09:15:00Z
```

### status

Current lifecycle state.

Examples:

```text
draft
active
archived
superseded
```

---

## Recommended Fields

### significance

Explanation of why the evidence is relevant.

### collection_method

Description of how the evidence was obtained.

### collector

Entity responsible for collecting the evidence.

### jurisdiction

Optional geographic or organizational context.

---

## Origin Fields

### source_reference

Associated source record.

Example:

```text
SRC-000001
```

### original_creator

Entity responsible for creating the original material.

### original_timestamp

Date and time associated with the original material.

Example:

```text
2026-09-01T00:00:00Z
```

### origin_description

Additional context regarding provenance.

---

## Relationship Fields

### related_entries

Chronicle entries associated with the evidence.

Example:

```text
CHR-ENTRY-000001
```

### related_evidence

Associated evidence records.

Example:

```text
EVD-000014
EVD-000015
```

### related_corrections

Corrections affecting the evidence record.

Example:

```text
COR-000002
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

Optional verification record.

Example:

```text
VER-000003
```

---

## Integrity Fields

### checksum

Optional checksum value.

Example:

```text
SHA256:8d4c1f...
```

### digital_signature

Optional cryptographic signature reference.

### chain_of_custody

Optional documentation describing evidence handling history.

### integrity_notes

Additional information relevant to authenticity and preservation.

---

## Metadata Fields

### tags

Keywords used for organization and discovery.

Example:

```text
launch
screenshot
chronicle
```

### author

Entity that created the evidence record.

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
evidence_id: EVD-000001

title: Screenshot of Initial Chronicle Launch

evidence_type: image

description: >
  Homepage screenshot captured on launch day.

collection_timestamp: 2026-09-01T09:15:00Z

original_timestamp: 2026-09-01T00:00:00Z

status: active

verification_status: verified

source_reference: SRC-000001

related_entries:
  - CHR-ENTRY-000001

tags:
  - chronicle
  - launch
  - screenshot

checksum: SHA256:8d4c1f...

created_at: 2026-09-01T09:15:00Z
updated_at: 2026-09-01T09:15:00Z

version: 1.0
```

---

## Design Goals

The Evidence Record Schema seeks to:

* Preserve supporting materials
* Improve transparency
* Support verification efforts
* Enable independent review
* Maintain provenance information
* Support long-term archival preservation
* Facilitate historical research

---

## Preservation Principles

Evidence should remain available whenever practical.

Historical conclusions may change over time, but preserving the underlying evidence allows future reviewers to revisit and reassess the record.

Whenever possible:

* Original materials should remain preserved
* Provenance should remain documented
* Integrity information should remain available
* Historical relationships should remain intact

---

## Future Development

Future versions may support:

* Content-addressable storage
* Distributed evidence repositories
* Cryptographic integrity verification
* Automated provenance tracking
* Immutable evidence histories
* Public archival networks

---

## Status

Draft schema.

This schema serves as the initial structure for Chronicle evidence records and may evolve as Chronicle develops.

