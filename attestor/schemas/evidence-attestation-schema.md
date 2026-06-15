# Evidence Attestation Schema

## Purpose

The Evidence Attestation Schema defines a standardized structure for documenting attestations regarding evidence.

Its purpose is to preserve transparency, attribution, traceability, and context when an attestor makes a statement regarding evidence, supporting materials, source records, or related documentation.

The schema documents statements about evidence.

It does not determine whether the evidence is correct.

---

## Overview

Evidence attestations may be used to document statements such as:

* Evidence exists
* Evidence was reviewed
* Evidence supports a claim
* Evidence contradicts a claim
* Evidence is incomplete
* Evidence is unavailable
* Evidence was modified

Evidence attestations help preserve context surrounding evidence-related observations.

---

## Core Schema Structure

```yaml id="z4m9rf"
attestation_id:

attestation_type:

status:

attestor:

subject:

evidence_record:

attestation_statement:

evidence_classification:

support_level:

evidence_refs:
source_refs:
related_records:

created_at:
updated_at:

confidence_indicator:

notes:
```

---

## Required Fields

### attestation_id

Unique identifier assigned to the attestation.

Example:

```text id="q7v2dc"
ATT-EVD-000001
```

---

### attestation_type

Classification of attestation.

Example:

```text id="d5m8yk"
evidence_attestation
```

---

### attestor

Identity issuing the attestation.

Example:

```yaml id="r2k4pf"
attestor:
  id: ANC-000101
  type: individual
```

---

### subject

The claim, record, event, identity, or object associated with the evidence.

Example:

```yaml id="h7x3mt"
subject:
  id: REG-000301
  type: record
```

---

### evidence_record

Reference to the evidence being discussed.

Example:

```yaml id="m9q5jb"
evidence_record:
  id: EVD-000501
  type: document
```

---

### attestation_statement

The statement regarding the evidence.

Example:

```text id="w4f8ke"
The referenced evidence supports the associated participation claim.
```

---

### created_at

Timestamp associated with issuance.

Example:

```text id="t1v7ra"
2026-06-15T00:00:00Z
```

---

## Optional Fields

### status

Current status.

Examples:

```text id="n5p2zx"
active
corrected
retracted
archived
superseded
```

---

### evidence_classification

Classification of evidence.

Examples:

```text id="u8m3yc"
document
publication
record
image
video
dataset
historical_record
other
```

---

### support_level

Indicates how the attestor believes the evidence relates to the subject.

Examples:

```text id="f3t9qp"
supports
partially_supports
contradicts
neutral
unclear
```

---

### evidence_refs

Associated evidence references.

Example:

```yaml id="e6w4kh"
evidence_refs:
  - EVD-000501
  - EVD-000502
```

---

### source_refs

Associated source references.

Example:

```yaml id="y2m7jd"
source_refs:
  - SRC-000021
```

---

### related_records

Related records.

Example:

```yaml id="v8r1pq"
related_records:
  - REG-000301
  - CHR-000088
```

---

### updated_at

Timestamp of most recent update.

Example:

```text id="g5x4ut"
2026-07-01T00:00:00Z
```

---

### confidence_indicator

Optional confidence assessment.

Examples:

```text id="b7j6fw"
low
medium
high
unknown
```

Confidence should not be interpreted as certainty.

---

### notes

Additional context.

Example:

```text id="a2k8nv"
Evidence reviewed by independent sources.
```

---

## Evidence Classification Types

The schema may support classifications such as:

### Document

Written materials.

### Publication

Published articles or reports.

### Record

Structured records.

### Image

Photographic or graphical evidence.

### Video

Video-based evidence.

### Dataset

Structured data collections.

### Historical Record

Archived or historical materials.

### Other

Additional evidence categories.

---

## Support Levels

Evidence attestations may describe different relationships between evidence and a subject.

### Supports

Evidence supports the statement.

### Partially Supports

Evidence provides limited support.

### Contradicts

Evidence conflicts with the statement.

### Neutral

Evidence provides context without direct support.

### Unclear

Relationship remains uncertain.

---

## Example Record

```yaml id="p4t8dw"
attestation_id: ATT-EVD-000001

attestation_type: evidence_attestation

status: active

attestor:
  id: ANC-000101
  type: individual

subject:
  id: REG-000301
  type: record

evidence_record:
  id: EVD-000501
  type: document

attestation_statement: >
  The referenced evidence supports the associated participation claim.

evidence_classification: document

support_level: supports

evidence_refs:
  - EVD-000501

source_refs:
  - SRC-000021

related_records:
  - REG-000301

created_at: 2026-06-15T00:00:00Z

confidence_indicator: medium

notes: >
  Evidence reviewed and linked to supporting records.
```

---

## Relationship to Evidence Records

Evidence attestations reference evidence records.

A simplified relationship may be represented as:

```text id="j9n4pe"
Evidence Record
       ↓
Evidence Attestation
```

Evidence remains separate from the statement made about it.

---

## Relationship to Verification

Evidence attestations may reference verification activities.

Verification remains the responsibility of Certifier.

A simplified distinction may be represented as:

```text id="s6m2ky"
Evidence Attestation → Statement
Verification → Evaluation
```

---

## Relationship to Trust Signals

Evidence attestations may generate trust signals.

Examples:

* Independent evidence review
* Transparent source attribution
* Consistent evidence support

These signals may contribute to trust evaluations.

---

## Relationship to Registry

Registry may catalog evidence attestation records.

Structured schemas improve discoverability and interoperability.

---

## Relationship to Chronicle

Evidence attestations may become part of the historical record.

Historical evidence context often contributes to trust evaluations.

---

## Guiding Principles

### Transparency

Evidence relationships should remain visible.

### Attribution

Attestors should remain identifiable.

### Traceability

Evidence references should support review.

### Context

Evidence should remain connected to associated records.

### Interoperability

Schema structures should support cross-system compatibility.

---

## Guiding Statement

```text id="k3v7rh"
Evidence provides information.

Evidence attestations document how that information is interpreted.
```

---

## Status

This schema represents an initial conceptual structure and may evolve as Attestor standards mature.
