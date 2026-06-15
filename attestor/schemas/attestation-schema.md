# Attestation Schema

## Purpose

The Attestation Schema defines the foundational structure for representing attestations within Attestor.

Its purpose is to provide a consistent framework for documenting statements, preserving attribution, maintaining traceability, and supporting interoperability across trust-related systems.

The schema defines structure.

It does not determine truth.

---

## Overview

An attestation is a statement made by an attestor regarding a subject.

The Attestation Schema helps document:

* Who made the statement
* What was stated
* When it was stated
* What evidence may support it
* What context may be relevant

This structure helps improve transparency and reviewability.

---

## Core Schema Structure

```yaml
attestation_id:
attestation_type:
status:

attestor:
subject:

statement:

evidence_refs:
source_refs:
related_records:

created_at:
updated_at:

confidence_indicator:

notes:
```

Implementations may evolve over time.

---

## Required Fields

### attestation_id

Unique identifier for the attestation.

Example:

```text id="b7q4mv"
ATT-000001
```

---

### attestation_type

Classification of the attestation.

Examples:

```text id="t3v8dx"
identity
qualification
ownership
participation
relationship
verification
reputation
```

---

### attestor

The individual, organization, institution, or system making the attestation.

Example:

```yaml
attestor:
  id: ANC-000001
  type: individual
```

---

### subject

The entity, claim, record, event, or condition being attested.

Example:

```yaml
subject:
  id: ANC-000002
  type: individual
```

---

### statement

The content of the attestation.

Example:

```text id="x4n2kr"
The subject participated in the event.
```

---

### created_at

Timestamp associated with creation of the attestation.

Example:

```text id="p6m7tv"
2026-01-01T00:00:00Z
```

---

## Optional Fields

### status

Current state of the attestation.

Examples:

```text id="y8k5fp"
active
corrected
retracted
archived
superseded
```

---

### evidence_refs

References to supporting evidence.

Example:

```yaml
evidence_refs:
  - EVD-000001
  - EVD-000002
```

---

### source_refs

References to supporting sources.

Example:

```yaml
source_refs:
  - SRC-000001
  - SRC-000002
```

---

### related_records

Associated records.

Example:

```yaml
related_records:
  - REG-000001
  - CHR-000005
```

---

### confidence_indicator

Optional confidence assessment.

Examples:

```text id="r5t9xv"
low
medium
high
unknown
```

Confidence should not be interpreted as certainty.

---

### updated_at

Timestamp of most recent modification.

Example:

```text id="u7j3mq"
2026-03-15T18:32:00Z
```

---

### notes

Additional contextual information.

Example:

```text id="n8v2pd"
Additional supporting context.
```

---

## Attestation Types

The schema supports multiple attestation categories.

Examples include:

### Identity Attestation

Statements regarding identity.

### Qualification Attestation

Statements regarding qualifications.

### Participation Attestation

Statements regarding involvement in activities.

### Ownership Attestation

Statements regarding ownership.

### Relationship Attestation

Statements regarding relationships.

### Verification Attestation

Statements regarding verification outcomes.

### Reputation Attestation

Statements regarding reputation-related observations.

Additional categories may emerge over time.

---

## Example Record

```yaml
attestation_id: ATT-000001

attestation_type: participation

status: active

attestor:
  id: ANC-000001
  type: individual

subject:
  id: ANC-000002
  type: individual

statement: >
  The subject participated in the event.

evidence_refs:
  - EVD-000101

source_refs:
  - SRC-000021

related_records:
  - REG-000005

created_at: 2026-01-01T00:00:00Z

confidence_indicator: medium

notes: >
  Participation documented through supporting records.
```

---

## Relationship to Evidence Schema

Attestations may reference evidence.

A simplified relationship may be represented as:

```text id="c4m7qb"
Attestation
     ↓
Evidence
```

Evidence provides supporting context.

---

## Relationship to Trust Signals

Attestations may generate trust signals.

Examples:

* Identity confirmations
* Participation records
* Qualification statements

Trust signals may emerge from attestation activity.

---

## Relationship to Verification

Attestations document statements.

Verification evaluates support for statements.

A simplified distinction may be represented as:

```text id="w9k2te"
Attestation → Statement
Verification → Evaluation
```

---

## Relationship to Registry

Registry may catalog attestation records.

Structured schemas improve interoperability and discoverability.

---

## Relationship to Chronicle

Attestations may become part of the historical record preserved by Chronicle.

Historical context often contributes to trust evaluations.

---

## Relationship to Anchor

Attestations frequently reference identities maintained by Anchor.

Consistent identity references improve traceability.

---

## Guiding Principles

### Attribution

Attestors should remain identifiable whenever practical.

### Transparency

Statements should remain visible.

### Traceability

Relationships should support review.

### Context

Attestations should preserve supporting information.

### Interoperability

Schema structures should support cross-system compatibility.

---

## Long-Term Vision

As Attestor evolves, the Attestation Schema may become a foundational component of broader trust frameworks, reputation systems, interoperability standards, and digital trust networks.

The goal is not merely to record statements.

The goal is to preserve trust-related context around those statements.

---

## Status

This schema represents an initial conceptual structure and may evolve as Attestor standards mature.
