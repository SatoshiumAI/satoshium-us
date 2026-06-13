# Source Record Schema

## Purpose

The Source Record Schema defines the structure used to represent sources within Chronicle.

Sources identify where information originated.

A source may provide evidence, context, claims, statements, records, or references that support Chronicle entries and related records.

Sources do not determine truth by themselves.

They establish origin, attribution, and context so information can be reviewed, compared, verified, challenged, or corrected.

---

## Schema Overview

A source record should answer the following questions:

* Where did the information come from?
* Who created or published it?
* When was it created, published, accessed, or archived?
* What type of source is it?
* Which Chronicle records rely on it?
* What is the current confidence or verification status?

---

## Required Fields

### source_id

Unique identifier assigned to the source record.

Example:

```text
SRC-000001
```

### title

Short descriptive title.

Example:

```text
Initial Chronicle Launch Page
```

### source_type

Classification of source.

Examples:

```text
webpage
document
publication
archive
database
public_record
statement
interview
broadcast
repository
dataset
social_post
other
```

### description

Brief description of the source.

Example:

```text
Public webpage announcing the initial Chronicle launch.
```

### access_timestamp

Date and time the source was accessed, captured, or recorded.

Example:

```text
2026-09-01T09:00:00Z
```

### status

Current lifecycle state.

Examples:

```text
draft
active
archived
superseded
unavailable
```

---

## Recommended Fields

### creator

Entity that created the source.

### publisher

Entity that published or distributed the source.

### publication_timestamp

Date and time the source was published, if known.

Example:

```text
2026-09-01T00:00:00Z
```

### source_location

Location or reference where the source can be found.

Examples:

```text
https://example.com/chronicle
archive://SRC-000001
repository://satoshium-us/chronicle
```

### archive_reference

Optional archive or preservation reference.

Example:

```text
ARCH-000001
```

---

## Relationship Fields

### related_entries

Chronicle entries associated with the source.

Example:

```text
CHR-ENTRY-000001
```

### related_evidence

Evidence records derived from or associated with the source.

Example:

```text
EVD-000001
```

### related_corrections

Correction records involving this source.

Example:

```text
COR-000001
```

### related_sources

Other source records connected to this source.

Example:

```text
SRC-000014
SRC-000015
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
unavailable
```

### verification_reference

Optional verification record.

Example:

```text
VER-000003
```

### reliability_notes

Notes regarding source reliability, limitations, conflicts, or context.

---

## Integrity Fields

### checksum

Optional checksum value for preserved source material.

Example:

```text
SHA256:8d4c1f...
```

### digital_signature

Optional digital signature or attestation reference.

### preservation_notes

Notes regarding archival status, capture method, or long-term availability.

---

## Metadata Fields

### tags

Keywords used for organization and discovery.

Example:

```text
chronicle
launch
source
webpage
```

### author

Entity that created the source record.

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
source_id: SRC-000001

title: Initial Chronicle Launch Page

source_type: webpage

description: >
  Public webpage announcing the initial Chronicle launch.

creator: Satoshium
publisher: Satoshium

publication_timestamp: 2026-09-01T00:00:00Z
access_timestamp: 2026-09-01T09:00:00Z

source_location: https://example.com/chronicle
archive_reference: ARCH-000001

status: active

verification_status: verified

related_entries:
  - CHR-ENTRY-000001

related_evidence:
  - EVD-000001

tags:
  - chronicle
  - launch
  - source
  - webpage

created_at: 2026-09-01T09:00:00Z
updated_at: 2026-09-01T09:00:00Z

version: 1.0
```

---

## Design Goals

The Source Record Schema seeks to:

* Preserve information origin
* Support attribution
* Improve traceability
* Enable verification
* Maintain context
* Support archival preservation
* Strengthen historical accountability

---

## Source and Evidence Distinction

Sources and evidence are related but distinct.

A source answers:

> Where did the information come from?

Evidence answers:

> What supports or challenges the claim?

A single source may contain multiple evidence items.

Multiple sources may support a single entry.

---

## Preservation Principles

Sources should remain accessible whenever practical.

When sources become unavailable, Chronicle should preserve references, archived versions, metadata, or notes documenting their prior existence.

Whenever possible:

* Source origin should remain clear
* Access timestamps should be preserved
* Archive references should be maintained
* Relationships to entries and evidence should remain intact

---

## Future Development

Future versions may support:

* Automated source capture
* Archive integration
* Cryptographic timestamping
* Digital attestations
* Source reliability scoring
* Distributed source preservation
* Cross-system source references

---

## Status

Draft schema.

This schema serves as the initial structure for Chronicle source records and may evolve as Chronicle develops.

