# Correction Attestation Template

## Purpose

This template provides a standardized format for documenting corrections to existing attestations.

Its purpose is to preserve transparency, accountability, traceability, and historical integrity when previously issued attestations require modification, clarification, amendment, or retraction.

Corrections should improve understanding.

They should not erase history.

---

## Template

```yaml
correction_attestation_id:

correction_type:

status:

original_attestation:
  attestation_id:
  reference_record:

correcting_attestor:
  id:
  type:

subject:
  id:
  type:

correction_summary:

original_statement:

corrected_statement:

reason_for_correction:

supporting_evidence:
  -

supporting_sources:
  -

related_records:
  -

correction_date:

effective_date:

notes:
```

---

## Field Definitions

### correction_attestation_id

Unique identifier assigned to the correction attestation.

Example:

```text
CAT-000001
```

---

### correction_type

Classification of correction.

Examples:

```text
administrative
clarification
amendment
evidence_update
attribution_update
historical_update
retraction
```

---

### status

Current status of the correction.

Examples:

```text
active
pending
superseded
archived
```

---

### original_attestation

Reference to the attestation being corrected.

Example:

```yaml
original_attestation:
  attestation_id: ATT-000101
  reference_record: REG-000451
```

---

### correcting_attestor

Identity responsible for issuing the correction.

Example:

```yaml
correcting_attestor:
  id: ANC-000021
  type: organization
```

---

### subject

The subject associated with the original attestation.

Example:

```yaml
subject:
  id: ANC-000044
  type: individual
```

---

### correction_summary

Short summary describing the correction.

Example:

```text
Correction of participation date.
```

---

### original_statement

Original attestation language.

Example:

```text
The subject participated on January 5, 2026.
```

---

### corrected_statement

Updated statement replacing or clarifying the original.

Example:

```text
The subject participated on January 15, 2026.
```

---

### reason_for_correction

Explanation describing why the correction was necessary.

Example:

```text
Additional documentation confirmed the original date was inaccurate.
```

---

### supporting_evidence

Evidence supporting the correction.

Example:

```yaml
supporting_evidence:
  - EVD-000501
  - EVD-000502
```

---

### supporting_sources

Sources supporting the correction.

Example:

```yaml
supporting_sources:
  - SRC-000041
```

---

### related_records

Associated records.

Example:

```yaml
related_records:
  - REG-000451
  - CHR-000103
```

---

### correction_date

Date the correction was issued.

Example:

```text
2026-06-15T00:00:00Z
```

---

### effective_date

Date the correction became effective.

Example:

```text
2026-06-15T00:00:00Z
```

---

### notes

Additional contextual information.

Example:

```text
Original attestation retained for historical review.
```

---

## Example Correction Attestation

```yaml
correction_attestation_id: CAT-000001

correction_type: historical_update

status: active

original_attestation:
  attestation_id: ATT-000101
  reference_record: REG-000451

correcting_attestor:
  id: ANC-000021
  type: organization

subject:
  id: ANC-000044
  type: individual

correction_summary: >
  Correction of participation date.

original_statement: >
  The subject participated on January 5, 2026.

corrected_statement: >
  The subject participated on January 15, 2026.

reason_for_correction: >
  Additional documentation confirmed the original date was inaccurate.

supporting_evidence:
  - EVD-000501

supporting_sources:
  - SRC-000041

related_records:
  - REG-000451

correction_date: 2026-06-15T00:00:00Z

effective_date: 2026-06-15T00:00:00Z

notes: >
  Original attestation preserved for transparency and historical review.
```

---

## Correction Categories

The template may be used for:

### Administrative Corrections

Corrections involving formatting, identifiers, or administrative metadata.

### Clarifications

Additional context that improves understanding without changing the underlying meaning.

### Amendments

Modifications to previously issued statements.

### Evidence Updates

Corrections based upon newly available evidence.

### Attribution Updates

Corrections involving identity or source attribution.

### Historical Updates

Corrections involving dates, events, timelines, or historical references.

### Retractions

Formal withdrawal of an attestation.

---

## Historical Preservation

Whenever practical:

* Original attestations should remain preserved.
* Corrections should remain visible.
* Relationships between records should remain traceable.
* Historical context should remain available.

Transparency is generally preferable to silent modification.

---

## Relationship to Attestations

A correction attestation is itself a form of attestation.

A simplified relationship may be represented as:

```text
Original Attestation
         ↓
Correction Attestation
         ↓
Updated Understanding
```

The correction supplements the record rather than replacing history.

---

## Guiding Principles

### Transparency

Corrections should remain visible.

### Accountability

Correcting parties should remain identifiable.

### Traceability

Users should be able to review the relationship between original and corrected records.

### Preservation

Historical information should remain available.

### Context

Corrections should explain why changes occurred.

---

## Guiding Statement

```text
A correction improves understanding.

It should not erase the path that led there.
```

---

## Status

This template represents an initial conceptual correction-attestation format and may evolve as Attestor standards mature.
