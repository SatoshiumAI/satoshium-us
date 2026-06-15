# Trust Signal Template

## Purpose

This template provides a standardized format for documenting trust signals within Attestor.

Its purpose is to preserve transparency, attribution, traceability, and context when recording observations, indicators, events, relationships, or information that may influence trust-related evaluations.

Trust signals contribute information relevant to trust.

They do not determine trust.

---

## Template

```yaml
trust_signal_id:

signal_type:

status:

subject:
  id:
  type:

signal_source:
  type:
  reference:

signal_description:

signal_direction:

signal_strength:

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

### trust_signal_id

Unique identifier assigned to the trust signal.

Example:

```text
TS-000001
```

---

### signal_type

Classification of trust signal.

Examples:

```text
attestation
verification
evidence
reputation
historical
accountability
correction
source
identity
other
```

---

### status

Current status of the trust signal.

Examples:

```text
active
corrected
retracted
archived
superseded
```

---

### subject

The entity, record, identity, organization, event, or object associated with the trust signal.

Example:

```yaml
subject:
  id: ANC-000101
  type: individual
```

---

### signal_source

Origin of the trust signal.

Example:

```yaml
signal_source:
  type: certification
  reference: CERT-000201
```

Possible source types include:

```text
attestation
evidence
verification
source
historical_record
correction
reputation_event
other
```

---

### signal_description

Description of the trust signal.

Example:

```text
Independent verification completed successfully.
```

---

### signal_direction

Represents the perceived influence of the signal.

Examples:

```text
positive
negative
neutral
mixed
unknown
```

Signal direction provides context only.

---

### signal_strength

Optional assessment of significance.

Examples:

```text
low
medium
high
unknown
```

Signal strength should not be interpreted as certainty.

---

### evidence_refs

Associated evidence references.

Example:

```yaml
evidence_refs:
  - EVD-000501
```

---

### source_refs

Associated source references.

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
  - CHR-000088
```

---

### created_at

Timestamp associated with creation.

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

Confidence represents the recorder's assessment and should not be interpreted as proof.

---

### notes

Additional contextual information.

Example:

```text
Signal generated through independent verification review.
```

---

## Example Trust Signal

```yaml
trust_signal_id: TS-000001

signal_type: verification

status: active

subject:
  id: ANC-000101
  type: individual

signal_source:
  type: certification
  reference: CERT-000201

signal_description: >
  Independent verification completed successfully.

signal_direction: positive

signal_strength: medium

evidence_refs:
  - EVD-000501

source_refs:
  - SRC-000021

related_records:
  - REG-000301

created_at: 2026-06-15T00:00:00Z

confidence_indicator: medium

notes: >
  Verification completed using documented evidence.
```

---

## Trust Signal Categories

The template may be used for:

### Attestation Signals

Signals generated from attestations.

### Verification Signals

Signals generated from certification or verification activities.

### Evidence Signals

Signals derived from supporting evidence.

### Reputation Signals

Signals derived from historical participation and reputation events.

### Historical Signals

Signals originating from historical records.

### Accountability Signals

Signals generated through transparency, disclosure, or corrective actions.

### Correction Signals

Signals generated through corrections, amendments, or retractions.

### Source Signals

Signals derived from source transparency and attribution.

Additional categories may emerge over time.

---

## Signal Direction Guidance

### Positive

May contribute favorable trust context.

### Negative

May contribute unfavorable trust context.

### Neutral

Provides context without directional influence.

### Mixed

Contains both positive and negative elements.

### Unknown

Direction cannot reasonably be determined.

Interpretation remains context dependent.

---

## Relationship to Trust

Trust signals contribute information relevant to trust.

A simplified relationship may be represented as:

```text
Trust Signal
      ↓
Trust Context
      ↓
Trust Evaluation
```

Trust signals inform evaluation.

They do not determine outcomes.

---

## Relationship to Reputation

Reputation may be viewed as the accumulation of trust signals over time.

A simplified relationship may be represented as:

```text
Trust Signals
      ↓
 Reputation
```

Trust signals help preserve the information that contributes to reputation.

---

## Relationship to Verification

Verification outcomes frequently generate trust signals.

Examples:

* Certifications
* Validation reports
* Review outcomes
* Independent confirmations

Trust signals help preserve verification context.

---

## Guiding Principles

### Transparency

Trust signals should remain understandable.

### Attribution

Signal origins should remain identifiable.

### Traceability

Relationships should support review and investigation.

### Context

Signals should remain connected to supporting information.

### Preservation

Historically significant signals should remain accessible.

---

## Guiding Statement

```text
Trust signals do not tell us what to believe.

They provide information that may influence belief.
```

---

## Status

This template represents an initial conceptual trust-signal format and may evolve as Attestor standards mature.

