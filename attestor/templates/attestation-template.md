# Attestation Template

## Purpose

This template provides a standardized format for creating attestations within Attestor.

The purpose of an attestation is to document a statement made by an attestor regarding a subject while preserving attribution, transparency, traceability, and historical context.

An attestation records that a statement was made.

It does not establish truth.

---

## Template

```yaml
attestation_id:

attestation_type:

status:

attestor:
  id:
  type:

subject:
  id:
  type:

statement:

evidence_refs:
  -

source_refs:
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

Unique identifier assigned to the attestation.

Example:

```text
ATT-000001
```

---

### attestation_type

Classification of attestation.

Examples:

```text
identity
qualification
ownership
participation
relationship
verification
reputation
evidence
source
other
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

The individual, organization, institution, or system making the attestation.

Example:

```yaml
attestor:
  id: ANC-000101
  type: individual
```

---

### subject

The entity, claim, event, record, or object associated with the attestation.

Example:

```yaml
subject:
  id: ANC-000202
  type: individual
```

---

### statement

The attestation being made.

Example:

```text
The subject participated in the event.
```

---

### evidence_refs

References to supporting evidence.

Example:

```yaml
evidence_refs:
  - EVD-000101
  - EVD-000102
```

Evidence is optional but encouraged whenever available.

---

### source_refs

References to supporting sources.

Example:

```yaml
source_refs:
  - SRC-000021
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

Timestamp associated with creation of the attestation.

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

Confidence indicates the attestor's assessment and should not be interpreted as certainty.

---

### notes

Additional contextual information.

Example:

```text
Supporting records independently reviewed.
```

---

## Example Attestation

```yaml
attestation_id: ATT-000001

attestation_type: participation

status: active

attestor:
  id: ANC-000101
  type: organization

subject:
  id: ANC-000202
  type: individual

statement: >
  The subject participated in the event.

evidence_refs:
  - EVD-000101

source_refs:
  - SRC-000021

related_records:
  - REG-000301

created_at: 2026-06-15T00:00:00Z

confidence_indicator: medium

notes: >
  Participation supported by available documentation.
```

---

## Attestation Categories

The template may be used for:

### Identity Attestations

Statements regarding identity.

### Qualification Attestations

Statements regarding credentials or qualifications.

### Participation Attestations

Statements regarding involvement in activities.

### Ownership Attestations

Statements regarding ownership relationships.

### Relationship Attestations

Statements regarding connections among entities.

### Verification Attestations

Statements regarding verification outcomes.

### Evidence Attestations

Statements regarding evidence.

### Source Attestations

Statements regarding sources.

Additional categories may emerge over time.

---

## Guiding Principles

### Attribution

Attestors should remain identifiable whenever practical.

### Transparency

Statements should remain visible and understandable.

### Traceability

Attestations should support review and investigation.

### Context

Supporting information should remain connected whenever practical.

### Preservation

Historical attestations should remain available for future review.

---

## Historical Considerations

Attestations may be:

* Corrected
* Amended
* Retracted
* Archived

Whenever practical, original records should remain preserved to support transparency and historical review.

---

## Relationship to Trust

Attestations contribute information relevant to trust.

A simplified relationship may be represented as:

```text
Attestation
      ↓
Trust Context
```

Attestations help inform trust evaluations.

They do not determine trust outcomes.

---

## Guiding Statement

```text
An attestation records a statement.

Its value comes from transparency,
attribution,
and context.
```

---

## Status

This template represents an initial conceptual attestation format and may evolve as Attestor standards mature.
