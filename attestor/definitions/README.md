# Satoshium Attestor — Definitions

## Page
`/attestor/definitions/`

## Purpose
This page establishes the governed vocabulary used throughout **Satoshium Attestor**.

Definitions apply within Attestor's institutional scope and do not redefine canonical terminology governed by other Satoshium Suite institutions.

## Governing Principle
> **Reference does not transfer authority.**

## Canonical Institutional Model
**Attestor → Trust Statement**

`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

## Core Definitions

### Attestation
A governed, attributable assertion used by Attestor to express a bounded statement about a subject, record, relationship, condition, event, or other trust-relevant matter.

### Trust Statement
Attestor's canonical institutional output: a governed, attributable, bounded conclusion produced through Rule-Constrained Evaluation of an Attestation against eligible governed inputs.

### Evidence
Supporting material or an authoritative reference used by Attestor to evaluate an Attestation and support a Trust Statement. Evidence retains its source, provenance, relevant state, relevance, and authority context.

### Trust-Relevant Context
Information or an indicator relevant to evaluating an Attestation or supporting a Trust Statement.

The historical term **Trust Signal** is descriptive/legacy only and is not a current canonical Attestor object. It must not be confused with Beacon's **Discovery Signal / Discovery Metadata**.

### Correction
A governed activity addressing an identified error or required change in an Attestor-owned object while preserving prior state, traceability, and applicable Lifecycle and Versioning rules.

Correction is not a separate canonical Attestor object class.

### Provenance
Information sufficient to understand the origin, attribution, source relationship, derivation, and relevant history of an input, assertion, evaluation, or Attestor output.

Adopted provenance modes:
- `direct`
- `referenced`
- `derived`

### Scope
The defined boundary within which an assertion, evidence relationship, evaluation, or Trust Statement applies.

### Authority Boundary
The limit of Attestor's institutional authority in relation to an object, source, assertion, or conclusion.

Referenced objects remain governed by their originating authorities.

## Supporting Definitions

### Attesting Authority
The authority attributable to the governed assertion expressed by an Attestation.

Attesting Authority is distinct from:
- Referenced Authority;
- Attestor Authority.

### Eligible Governed Input
A governed source object, reference, evidence item, Attestation, or other admissible input that has satisfied the applicable eligibility determination for a particular Attestor evaluation.

### Eligibility
A governed admission determination for a particular Attestor evaluation.

> **Availability ≠ Eligibility**

> **Authority ≠ Eligibility**

> **Reference ≠ Eligibility**

### Evaluation
The rule-constrained institutional process through which Attestor considers an Attestation and eligible governed inputs to determine an Evaluation Outcome and form a bounded conclusion.

### Evaluation Outcome
A controlled result of Rule-Constrained Evaluation.

Adopted values:
- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

> **Outcome ≠ Conclusion ≠ Trust Statement Identity**

### Lifecycle State
The governed state of an Attestor object.

Adopted values:
- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

Review and correction are activities, not lifecycle states.

### Publication State
The governed public-representation state of an Attestor object.

Adopted values:
- `unpublished`
- `published`

> **Canonical Creation ≠ Lifecycle Activation ≠ Publication**

### Relationship
A governed directional connection between Attestor objects or referenced objects.

Adopted relationship vocabulary:
- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

A relationship does not imply identity or transfer authority.

### Version Identity
The identity of a governed state of a canonical object.

> **Canonical identifier → Which governed object?**

> **Version identity → Which governed state?**

Exact version syntax remains implementation/open architecture and is not defined here.

### Relevant State
The material temporal, lifecycle, publication, or source-state context applicable to an Attestation, governed input, Evaluation, or Trust Statement.

### Validation
The determination of whether an Attestor object satisfies the normative structural and rule requirements applicable to that object.

`Object + Applicable Normative Requirements → Validation → Governed Validation Result`

> **Validation ≠ Evaluation**

> **Valid ≠ Published**

The exact Validation Result vocabulary and executable rules remain implementation work.

### Conformance
A determination that a declared target satisfies an applicable requirements set using required validation and evidence.

`Target + Declared Requirements Set + Required Validation / Evidence → Conformance Determination`

> **Validation supports Conformance.**

> **Validation ≠ Conformance.**

Conformance mechanics and final result vocabulary remain implementation work.

## Controlled Attestation Types
Adopted values:
- `identity`
- `evidence`
- `source-provenance`
- `verification-related`
- `relationship-condition`
- `correction-supersession`

## Authority Context
Adopted values:
- `Attestor`
- `Suite-source`
- `external-source`

## Suite Vocabulary Boundary
Attestor may reference:
- Atlas Authoritative Intelligence;
- Navigator Workflow Definition / Orchestration;
- Certifier Certification Packages;
- Satoshium Registry Records;
- Chronicle Entries;
- Anchor Integrity References;
- Beacon Discovery Signals / Discovery Metadata;
- external governed sources.

Attestor definitions govern how those references participate in Attestor. They do not replace the originating institution's definitions, identifiers, schemas, lifecycle rules, or authority.

## Definition Governance
Definitions follow established Attestor architecture.

`Concept → Definition → Governed Use → Validation`

Machine serialization, executable validation-result mechanics, conformance-result mechanics, and production-specific implementation details remain subordinate to the implementation and production layers.

## Status
**Definitions → Advanced Architecture reconciled.**

The former “Supporting Terms” and “Deferred to Advanced Architecture” posture is no longer current. The supporting architecture now exists.

## Files
- `index.html` — public Definitions page.
- `README.md` — repository documentation.
