# Evidence Attestation Template

## Purpose

This template provides a standardized format for documenting attestations regarding evidence.

Its purpose is to preserve transparency, attribution, traceability, and context when an attestor makes a statement concerning evidence, supporting documentation, records, datasets, media, or other information relevant to a claim, event, identity, or record.

An evidence attestation documents an observation or statement about evidence.

It does not determine whether the evidence is correct.

---

## Template

```yaml
attestation_id:

attestation_type: evidence_attestation

status:

attestor:
  id:
  type:

subject:
  id:
  type:

evidence_record:
  id:
  type:

attestation_statement:

evidence_classification:

support_level:

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

Unique identifier assigned to the evidence attestation.

Example:

```text
ATT-EVD-000001
```

---

### attestation_type

Classification of attestation.

Example:

```text
evidence_attestation
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

Identity issuing the evidence attestation.

Example:

```yaml
attestor:
  id: ANC-000101
  type: organization
```

---

### subject

The claim, event, identity, record, or object associated with the evidence.

Example:

```yaml
subject:
  id: REG-000301
  type: record
```

---

### evidence_record

Reference to the evidence being discussed.

Example:

```yaml
evidence_record:
  id: EVD-000501
  type: document
```

---

### attestation_statement

Statement regarding the evidence.

Example:

```text
The referenced evidence supports the associated participation claim.
```

---

### evidence_classification

Classification of evidence.

Examples:

```text
document
publication
record
image
video
audio
dataset
historical_record
other
```

---

### support_level

Relationship between the evidence and the subject.

Examples:

```text
supports
partially_supports
contradicts
neutral
unclear
```

Support levels provide context and should not be interpreted as proof.

---

### evidence_refs

References to related evidence.

Example:

```yaml
evidence_refs:
  - EVD-000501
  - EVD-000502
```

---

### source_refs

References to associated sources.

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
Evidence independently reviewed and linked to supporting records.
```

---

## Example Evidence Attestation

```yaml
attestation_id: ATT-EVD-000001

attestation_type: evidence_attestation

status: active

attestor:
  id: ANC-000101
  type: organization

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
  Evidence reviewed and associated with supporting records.
```

---

## Evidence Categories

The template may be used for:

### Documentary Evidence

Reports, agreements, publications, and records.

### Digital Evidence

Metadata, logs, transaction records, and digital artifacts.

### Media Evidence

Images, audio recordings, and video materials.

### Historical Evidence

Archived materials and historical records.

### Dataset Evidence

Structured collections of information.

### Observational Evidence

Direct observations and witness reports.

Additional categories may emerge over time.

---

## Relationship to Attestations

Evidence attestations are specialized attestations.

A simplified relationship may be represented as:

```text
Evidence
    ↓
Evidence Attestation
    ↓
Trust Context
```

The evidence remains separate from the statement made about it.

---

## Relationship to Verification

Evidence attestations may reference verification activities.

Verification remains the responsibility of Certifier.

A simplified distinction may be represented as:

```text
Evidence Attestation → Statement
Verification → Evaluation
```

---

## Guiding Principles

### Attribution

Evidence origins should remain visible.

### Transparency

Evidence relationships should remain understandable.

### Traceability

Evidence references should support review and investigation.

### Context

Evidence should remain connected to relevant records.

### Preservation

Evidence history should remain available whenever practical.

---

## Guiding Statement

```text
Evidence provides information.

Evidence attestations explain how that information relates to a subject.
```

---

## Status

This template represents an initial conceptual evidence-attestation format and may evolve as Attestor standards mature.
