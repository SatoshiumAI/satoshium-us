# Source Attestation Schema

## Purpose

The Source Attestation Schema defines a standardized structure for documenting attestations regarding sources.

Its purpose is to preserve attribution, transparency, traceability, and context when an attestor makes a statement regarding the existence, reliability, relevance, authorship, provenance, or use of a source.

The schema documents statements about sources.

It does not determine whether a source is correct, trustworthy, or authoritative.

---

## Overview

Source attestations may be used to document statements such as:

* A source exists
* A source was reviewed
* A source supports a claim
* A source contradicts a claim
* A source originated from a specific entity
* A source has known limitations
* A source is relevant to a subject

Source attestations help preserve context surrounding source-related observations.

---

## Core Schema Structure

```yaml id="u6x4qb"
attestation_id:

attestation_type:

status:

attestor:

subject:

source_record:

attestation_statement:

source_classification:

source_relationship:

source_refs:
evidence_refs:
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

```text id="n3r7vx"
ATT-SRC-000001
```

---

### attestation_type

Classification of attestation.

Example:

```text id="m9k2fd"
source_attestation
```

---

### attestor

Identity issuing the attestation.

Example:

```yaml id="j4t8pr"
attestor:
  id: ANC-000101
  type: organization
```

---

### subject

The claim, record, event, identity, or object associated with the source.

Example:

```yaml id="h2v5mn"
subject:
  id: REG-000301
  type: record
```

---

### source_record

Reference to the source being discussed.

Example:

```yaml id="w7p3ke"
source_record:
  id: SRC-000021
  type: publication
```

---

### attestation_statement

Statement regarding the source.

Example:

```text id="t5x8ra"
The referenced source supports the associated claim.
```

---

### created_at

Timestamp associated with issuance.

Example:

```text id="k1m4zw"
2026-06-15T00:00:00Z
```

---

## Optional Fields

### status

Current status.

Examples:

```text id="v6r2qh"
active
corrected
retracted
archived
superseded
```

---

### source_classification

Classification of source.

Examples:

```text id="q8n5td"
government_record
publication
media_source
academic_source
corporate_source
archive
database
website
other
```

---

### source_relationship

Describes how the source relates to the subject.

Examples:

```text id="s4f9kp"
supports
partially_supports
contradicts
references
documents
mentions
unclear
```

---

### source_refs

Associated source references.

Example:

```yaml id="z2y7mb"
source_refs:
  - SRC-000021
```

---

### evidence_refs

Associated evidence references.

Example:

```yaml id="g7t4nr"
evidence_refs:
  - EVD-000501
```

---

### related_records

Related records.

Example:

```yaml id="r5x3vd"
related_records:
  - REG-000301
  - CHR-000088
```

---

### updated_at

Timestamp of most recent update.

Example:

```text id="p9k6fw"
2026-07-01T00:00:00Z
```

---

### confidence_indicator

Optional confidence assessment.

Examples:

```text id="d4v8xe"
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

```text id="b1m7qy"
Source independently referenced by multiple records.
```

---

## Source Classification Types

The schema may support classifications such as:

### Government Record

Official government-issued materials.

### Publication

Published reports, articles, or papers.

### Media Source

News organizations, journalists, or media publications.

### Academic Source

Research papers, journals, and academic materials.

### Corporate Source

Official corporate disclosures and publications.

### Archive

Historical repositories and preserved records.

### Database

Structured data collections.

### Website

Online information resources.

### Other

Additional source categories.

---

## Source Relationship Types

Source attestations may describe different relationships.

### Supports

Source supports the associated claim.

### Partially Supports

Source provides limited support.

### Contradicts

Source conflicts with the claim.

### References

Source references the subject.

### Documents

Source records or documents the subject.

### Mentions

Source contains mention of the subject.

### Unclear

Relationship remains uncertain.

---

## Example Record

```yaml id="e8n2pk"
attestation_id: ATT-SRC-000001

attestation_type: source_attestation

status: active

attestor:
  id: ANC-000101
  type: organization

subject:
  id: REG-000301
  type: record

source_record:
  id: SRC-000021
  type: publication

attestation_statement: >
  The referenced source supports the associated claim.

source_classification: publication

source_relationship: supports

source_refs:
  - SRC-000021

evidence_refs:
  - EVD-000501

related_records:
  - REG-000301

created_at: 2026-06-15T00:00:00Z

confidence_indicator: medium

notes: >
  Source independently reviewed and linked to supporting evidence.
```

---

## Relationship to Source Records

Source attestations reference source records.

A simplified relationship may be represented as:

```text id="x3v9jf"
Source Record
      ↓
Source Attestation
```

The source remains distinct from the statement made about it.

---

## Relationship to Evidence

Sources often support evidence.

A simplified relationship may be represented as:

```text id="m5r8ta"
Source
   ↓
Evidence
   ↓
Attestation
```

Source attestations help preserve these relationships.

---

## Relationship to Verification

Source attestations may reference verification activities.

Verification remains the responsibility of Certifier.

A simplified distinction may be represented as:

```text id="u7n4kw"
Source Attestation → Statement
Verification → Evaluation
```

---

## Relationship to Trust Signals

Source attestations may generate trust signals.

Examples:

* Source transparency
* Independent sourcing
* Source consistency
* Attribution quality

These signals may contribute to trust evaluations.

---

## Relationship to Registry

Registry may catalog source attestation records.

Structured schemas improve discoverability and interoperability.

---

## Relationship to Chronicle

Source attestations may become part of the historical record.

Historical source context often contributes to trust evaluations.

---

## Guiding Principles

### Attribution

Source origins should remain visible.

### Transparency

Source relationships should remain understandable.

### Traceability

Source references should support review.

### Context

Sources should remain connected to associated information.

### Interoperability

Schema structures should support cross-system compatibility.

---

## Guiding Statement

```text id="c6p2vh"
Sources provide origin.

Source attestations document how those origins relate to trust.
```

---

## Status

This schema represents an initial conceptual structure and may evolve as Attestor standards mature.
