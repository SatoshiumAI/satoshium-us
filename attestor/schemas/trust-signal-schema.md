# Trust Signal Schema

## Purpose

The Trust Signal Schema defines a standardized structure for documenting trust signals within Attestor.

Its purpose is to provide a consistent framework for recording information that may influence trust-related evaluations while preserving transparency, attribution, traceability, and historical context.

Trust signals contribute information.

They do not determine trust.

---

## Overview

A trust signal is an observation, event, indicator, relationship, or piece of information that may influence how users evaluate a subject.

Trust signals may originate from:

* Attestations
* Evidence
* Verification outcomes
* Historical records
* Reputation events
* Corrections
* Source transparency
* Accountability activities

The Trust Signal Schema provides a structure for documenting those signals.

---

## Core Schema Structure

```yaml id="n4v8kd"
trust_signal_id:

signal_type:

status:

subject:

signal_source:

signal_description:

signal_direction:

signal_strength:

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

### trust_signal_id

Unique identifier assigned to the trust signal.

Example:

```text id="h2x5mr"
TS-000001
```

---

### signal_type

Classification of signal.

Examples:

```text id="v8m3qt"
attestation
verification
evidence
reputation
historical
accountability
correction
source
```

---

### subject

The entity, record, event, organization, or identity associated with the signal.

Example:

```yaml id="f5k7dw"
subject:
  id: ANC-000101
  type: individual
```

---

### signal_source

Origin of the signal.

Example:

```yaml id="r3n8vp"
signal_source:
  type: certification
  reference: CERT-000201
```

---

### signal_description

Description of the signal.

Example:

```text id="q9m2xe"
Independent verification completed successfully.
```

---

### created_at

Timestamp associated with creation.

Example:

```text id="j6t4ry"
2026-06-15T00:00:00Z
```

---

## Optional Fields

### status

Current status.

Examples:

```text id="g4x9wk"
active
corrected
retracted
archived
superseded
```

---

### signal_direction

Describes the perceived effect of the signal.

Examples:

```text id="z7v3pb"
positive
negative
neutral
mixed
unknown
```

Signal direction provides context only.

---

### signal_strength

Optional representation of signal significance.

Examples:

```text id="m8f2qa"
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

```yaml id="t2n5kv"
evidence_refs:
  - EVD-000501
```

---

### source_refs

Associated source references.

Example:

```yaml id="p7x4jm"
source_refs:
  - SRC-000021
```

---

### related_records

Associated records.

Example:

```yaml id="w5r8dn"
related_records:
  - REG-000301
  - CHR-000088
```

---

### updated_at

Timestamp of most recent modification.

Example:

```text id="u1m6te"
2026-07-01T00:00:00Z
```

---

### confidence_indicator

Optional confidence assessment.

Examples:

```text id="k3v7rz"
low
medium
high
unknown
```

Confidence should not be interpreted as proof.

---

### notes

Additional context.

Example:

```text id="d9p4xf"
Signal generated from independently reviewed evidence.
```

---

## Trust Signal Types

The schema may support numerous signal categories.

### Attestation Signal

Generated from an attestation.

### Verification Signal

Generated from verification outcomes.

### Evidence Signal

Generated from supporting evidence.

### Reputation Signal

Generated from historical activity or reputation events.

### Historical Signal

Generated from historical records.

### Accountability Signal

Generated from transparent actions or disclosures.

### Correction Signal

Generated from corrections or amendments.

### Source Signal

Generated from source transparency or source quality.

Additional signal types may emerge over time.

---

## Signal Direction Types

Trust signals may have different effects.

### Positive

Potentially increases confidence.

### Negative

Potentially decreases confidence.

### Neutral

Provides context without directional influence.

### Mixed

Contains both positive and negative elements.

### Unknown

Direction cannot be determined.

Interpretation remains context dependent.

---

## Example Record

```yaml id="a8n2mr"
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

## Relationship to Attestations

Attestations may generate trust signals.

A simplified relationship may be represented as:

```text id="b6t9qw"
Attestation
     ↓
Trust Signal
```

Trust signals help preserve context derived from attestations.

---

## Relationship to Verification

Verification outcomes frequently generate trust signals.

A simplified relationship may be represented as:

```text id="c4x7pa"
Verification
      ↓
Trust Signal
```

Verification provides information that may influence trust evaluations.

---

## Relationship to Reputation

Reputation may be viewed as the accumulation of trust signals over time.

A simplified relationship may be represented as:

```text id="r8m5zk"
Trust Signals
      ↓
 Reputation
```

Trust signals contribute context for reputation development.

---

## Relationship to Evidence

Evidence may generate trust signals.

Evidence remains separate from the trust signal derived from it.

This distinction helps preserve transparency.

---

## Relationship to Registry

Registry may catalog trust signal records.

Structured schemas improve discoverability and interoperability.

---

## Relationship to Chronicle

Trust signals may become historically significant.

Chronicle may preserve their historical development and evolution.

---

## Guiding Principles

### Transparency

Trust signals should remain understandable.

### Attribution

Signal origins should remain identifiable.

### Traceability

Relationships should support review.

### Context

Signals should remain connected to supporting information.

### Interoperability

Schema structures should support cross-system compatibility.

---

## Guiding Statement

```text id="f2k8jd"
Trust signals do not determine trust.

They provide information that may influence it.
```

---

## Status

This schema represents an initial conceptual structure and may evolve as Attestor standards mature.
