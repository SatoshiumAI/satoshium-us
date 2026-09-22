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

The first production objects exercise version identity as `V1.0`. Versioning governs when a change preserves the existing version and when a new canonical statement or governed version is required.

### Relevant State
The material temporal, lifecycle, publication, or source-state context applicable to an Attestation, governed input, Evaluation, or Trust Statement.

### Validation
The determination of whether an Attestor object satisfies the normative structural and rule requirements applicable to that object.

`Object + Applicable Normative Requirements → Validation → Governed Validation Result`

> **Validation ≠ Evaluation**

> **Valid ≠ Published**

Validation is operational through Validator v0.5.

Established aggregate Validation Results are:
- `valid`
- `invalid`
- `incomplete`
- `error`

Established per-rule dispositions are:
- `pass`
- `fail`
- `not-applicable`
- `not-tested`

> **NOT-TESTED ≠ PASS**

### Conformance
A determination that a declared target satisfies an applicable requirements set using required validation and evidence.

`Target + Declared Requirements Set + Required Validation / Evidence → Conformance Determination`

> **Validation supports Conformance.**

> **Validation ≠ Conformance.**

Conformance is operational.

Established Conformance dispositions are:
- `satisfied`
- `not-satisfied`
- `not-applicable`
- `not-demonstrated`

Established Conformance outcomes are:
- `conformant`
- `nonconformant`
- `undetermined`
- `error`

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

`Concept → Definition → Governed Use → Validation / Governed Review → Conformance`

Machine serialization and executable mechanics remain subordinate to the governed definitions. Production has now exercised canonical ATT/TRST representations, Validation, governed Review, Conformance, lifecycle activation, Publication, and final-state revalidation.

## First Production Definition Demonstration

The first controlled production operation exercised the governed vocabulary in canonical objects and institutional actions.

Key production uses included:

- `ATT-2026-0001` → canonical **Attestation**;
- `TRST-2026-0001` → canonical **Trust Statement**;
- six Suite-source objects → **Eligible Governed Inputs** after Eligibility determinations;
- `verification-related` → exercised **Attestation Type**;
- `supported` → exercised **Evaluation Outcome**;
- `draft → active` → exercised **Lifecycle States**;
- `unpublished → published` → exercised **Publication States**;
- `references` and `derived-from` → exercised **Relationships**;
- `V1.0` → exercised **Version Identity**;
- `valid` → exercised aggregate **Validation Result**;
- `pass`, `not-applicable`, and `not-tested` → exercised Validation rule dispositions;
- `satisfied` → exercised **Conformance disposition**;
- `conformant` → exercised **Conformance outcome**;
- `Attestor` and `Suite-source` authority contexts → represented in production context;
- provenance and relevant-state distinctions → preserved through the evaluated evidence basis and final bounded conclusion.

The operation also confirmed that **Trust Signal** is not a canonical Attestor object and that Correction is a governed activity rather than a separate canonical object class.

**Definitions → DEMONSTRATED IN PRODUCTION**

Production proof remains value-specific. Established terms and controlled values not required by the first operation are not thereby claimed as independently production-tested.

## Status
**Definitions → Established and Production-Proven**

- core Attestor definitions → established
- supporting definitions → established
- canonical Attestation / Trust Statement distinction → production-demonstrated
- Eligibility / Eligible Governed Input → production-demonstrated
- Evaluation / Evaluation Outcome distinction → production-demonstrated
- Lifecycle / Publication distinction → production-demonstrated
- Relationship semantics → production-demonstrated
- Version Identity → production-demonstrated through `V1.0`
- Validation vocabulary → established and production-exercised
- Conformance vocabulary → established and production-exercised
- Authority / provenance / relevant-state boundaries → production-demonstrated
- Trust Signal → legacy/descriptive, noncanonical
- Correction → governed activity, not separate canonical object class
- Suite vocabulary boundary → preserved
- production proof → **ESTABLISHED for terminology exercised**

## Continuing Definition Governance

Definitions govern meaning before implementation mechanics.

Production use of a term does not broaden its definition, transfer source authority, or imply that every controlled value in the same vocabulary has been production-tested.

`Attestation ≠ Trust Statement`

`Eligibility ≠ Evaluation Outcome`

`Outcome ≠ Conclusion ≠ Trust Statement Identity`

`Canonical Creation ≠ Lifecycle Activation ≠ Publication`

`Validation ≠ Evaluation`

`Validation ≠ Conformance`

`NOT-TESTED ≠ PASS`

`Reference ≠ Support`

**Reference does not transfer authority.**

## Files
- `index.html` — public Definitions page.
- `README.md` — repository documentation.
