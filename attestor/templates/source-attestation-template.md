# Source Attestation Template

## Purpose

This template provides a standardized format for documenting attestations regarding sources.

Its purpose is to preserve attribution, transparency, traceability, and context when an attestor makes a statement concerning a source, its origin, relevance, authorship, provenance, or relationship to a claim, record, event, or subject.

A source attestation documents a statement about a source.

It does not determine whether the source is correct, authoritative, or trustworthy.

---

## Template

```yaml
attestation_id:

attestation_type: source_attestation

status:

attestor:
  id:
  type:

subject:
  id:
  type:

source_record:
  id:
  type:

attestation_statement:

source_classification:

source_relationship:

source_refs:
  -

evidence_refs:
  -

related_records:
  -

created_at:

updated_at:

confidence_indicator:

notes:
```

---

## Field Definitions

### attestation_id

Unique identifier assigned to the source attestation.

Example:

```text
ATT-SRC-000001
```

---

### attestation_type

Classification of attestation.

Example:

```text
source_attestation
```

---

### status

Current status of the attestation.

Examples:

```text
active
corrected
retracted
archived
superseded
```

---

### attestor

Identity issuing the source attestation.

Example:

```yaml
attestor:
  id: ANC-000101
  type: organization
```

---

### subject

The claim, record, event, identity, or object associated with the source.

Example:

```yaml
subject:
  id: REG-000301
  type: record
```

---

### source_record

Reference to the source being discussed.

Example:

```yaml
source_record:
  id: SRC-000021
  type: publication
```

---

### attestation_statement

Statement regarding the source.

Example:

```text
The referenced source supports the associated claim.
```

---

### source_classification

Classification of source.

Examples:

```text
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

```text
supports
partially_supports
contradicts
references
documents
mentions
unclear
```

Relationship classifications provide context and should not be interpreted as proof.

---

### source_refs

References to associated sources.

Example:

```yaml
source_refs:
  - SRC-000021
```

---

### evidence_refs

References to associated evidence.

Example:

```yaml
evidence_refs:
  - EVD-000501
```

---

### related_records

Associated records.

Example:

```yaml
related_records:
  - REG-000301
  - CHR-000055
```

---

### created_at

Timestamp associated with issuance.

Example:

```text
2026-06-15T00:00:00Z
```

---

### updated_at

Timestamp associated with the most recent update.

Example:

```text
2026-07-01T00:00:00Z
```

---

### confidence_indicator

Optional confidence assessment.

Examples:

```text
low
medium
high
unknown
```

Confidence represents the attestor's assessment and should not be interpreted as certainty.

---

### notes

Additional contextual information.

Example:

```text
Source independently reviewed and linked to supporting evidence.
```

---

## Example Source Attestation

```yaml
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

## Source Categories

The template may be used for:

### Government Sources

Official records, filings, court records, and regulatory documents.

### Academic Sources

Research papers, journals, and scholarly publications.

### Media Sources

News organizations, journalists, and investigative reporting.

### Corporate Sources

Official company disclosures, reports, and filings.

### Historical Sources

Archives, preserved records, and historical collections.

### Digital Sources

Websites, databases, repositories, and online publications.

Additional source categories may emerge over time.

---

## Relationship to Sources

Source attestations are statements about sources.

A simplified relationship may be represented as:

```text
Source
   ↓
Source Attestation
   ↓
Trust Context
```

The source remains distinct from the statement made about it.

---

## Relationship to Evidence

Sources often support evidence.

A simplified relationship may be represented as:

```text
Source
   ↓
Evidence
   ↓
Attestation
```

Source attestations help preserve those relationships.

---

## Relationship to Verification

Source attestations may reference verification activities.

Verification remains the responsibility of Certifier.

A simplified distinction may be represented as:

```text
Source Attestation → Statement
Verification → Evaluation
```

---

## Guiding Principles

### Attribution

Source origins should remain visible.

### Transparency

Source relationships should remain understandable.

### Traceability

Source references should support review and investigation.

### Context

Sources should remain connected to associated records.

### Preservation

Historical source information should remain available whenever practical.

---

## Guiding Statement

```text
Sources provide origin.

Source attestations document how those origins relate to trust.
```

---

## Status

This template represents an initial conceptual source-attestation format and may evolve as Attestor standards mature.
