# Correction Attestation Template

## Purpose

This template provides a standardized structure for documenting corrections to existing attestations.

The purpose of a correction attestation is to improve clarity, accuracy, transparency, and accountability while preserving the historical record.

Corrections should supplement history rather than erase it whenever practical.

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

Current correction status.

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

Short description of the correction.

Example:

```text
Correction of participation date.
```

---

### original_statement

Original attestation text.

Example:

```text
The subject participated on January 5, 2026.
```

---

### corrected_statement

Updated statement.

Example:

```text
The subject participated on January 15, 2026.
```

---

### reason_for_correction

Explanation for the correction.

Example:

```text
Additional records confirmed the original date was incorrect.
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

Sources associated with the correction.

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

Additional context.

Example:

```text
Original attestation remains preserved for historical review.
```

---

## Example Record

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
  Original attestation preserved for historical transparency.
```

---

## Guiding Principles

### Transparency

Corrections should remain visible.

### Traceability

Users should be able to connect corrections to original records.

### Accountability

Correcting parties should remain identifiable.

### Preservation

Original records should remain preserved whenever practical.

### Historical Integrity

Corrections should improve understanding without obscuring history.

---

## Guiding Statement

```text
A correction changes understanding.

It should not erase memory.
```

---

## Status

This template represents an initial conceptual correction-attestation format and may evolve as Attestor standards mature.
