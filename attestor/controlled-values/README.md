# Satoshium Attestor — Controlled Values

**Path:** `/attestor/controlled-values/`  
**Institution:** Satoshium Attestor  
**Current Stage:** Operational Controlled Values  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

Controlled Values establish the normative vocabularies used by Attestor to classify governed objects, states, relationships, provenance, authority context, and evaluation outcomes.

A controlled value classifies meaning within a defined Attestor context. It does not independently establish truth, authority, evidence sufficiency, validity, or trustworthiness.

## Initial Controlled Vocabulary

### Attestation Type

- `identity`
- `evidence`
- `source-provenance`
- `verification-related`
- `relationship-condition`
- `correction-supersession`

These are the established Attestation Type families. Exact profile requirements and applicability are governed by the applicable Schemas / Profiles and related Attestor architecture.

### Lifecycle State

- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

Exact transitions and object-specific applicability are defined by Lifecycle.

### Publication State

- `unpublished`
- `published`

Canonical existence and public representation remain separate.

### Evaluation Outcome

- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

Evaluation defines the exact evidentiary and rule conditions for these outcomes.

### Relationship Type

- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

Relationships defines directionality, permitted object combinations, and cardinality.

### Provenance Mode

- `direct`
- `referenced`
- `derived`

Provenance defines exact meaning, eligibility, and metadata requirements.

### Authority Context

- `Attestor`
- `Suite-source`
- `external-source`

These classify authority context; they do not rank authority or trustworthiness.

## Separation of Meaning

Attestor keeps these concepts distinct:

- **Lifecycle State** → where an object is in governed existence.
- **Publication State** → whether public representation is authorized.
- **Validation Result** → whether structural and rule requirements are satisfied.
- **Evaluation Outcome** → Attestor's conclusion from governed evaluation.

An `active` object is not automatically `published`. A published object is not automatically favorable. Structural validity does not imply an assertion is `supported`.

## No Confidence or Reputation Scale

The June-era confidence-scale and generic Trust Signal model are not adopted as normative Attestor vocabulary.

`Evaluation Outcome ≠ Confidence Percentage`

`Evaluation Outcome ≠ Reputation Score`

`Evaluation Outcome ≠ Trust Signal`

`Evaluation Outcome ≠ Universal Truth`

The canonical Attestor output remains the **Trust Statement**.

## Validation and Conformance Vocabularies

Validation and Conformance now have established operational result vocabularies governed by their respective Attestor architectures.

### Validation Aggregate Result

- `valid`
- `invalid`
- `incomplete`
- `error`

### Validation Per-Rule Disposition

- `pass`
- `fail`
- `not-applicable`
- `not-tested`

`NOT-TESTED ≠ PASS`

### Conformance Disposition

- `satisfied`
- `not-satisfied`
- `not-applicable`
- `not-demonstrated`

### Conformance Outcome

- `conformant`
- `nonconformant`
- `undetermined`
- `error`

These remain institutionally distinct:

`Validation ≠ Evaluation`

`Validation ≠ Conformance`

`Valid ≠ Published`

## First Production Controlled-Value Demonstration

The first controlled production operation exercised controlled values across the Attestor process.

Values actually exercised included:

- Attestation Type → `verification-related`;
- Lifecycle State → `draft`, then `active`;
- Publication State → `unpublished`, then `published`;
- Evaluation Outcome → `supported`;
- Relationship Type → `references`, `derived-from`;
- canonical version representation → `V1.0`;
- Validation aggregate result → `valid`;
- Validation per-rule dispositions → `pass`, `not-applicable`, `not-tested`;
- Conformance disposition → `satisfied`; and
- Conformance outcome → `conformant`.

The final production validations contained no mandatory `not-tested` result.

Production also represented governed provenance and authority context while preserving source authority and the distinction among direct/referenced/derived provenance semantics.

**Controlled Values → DEMONSTRATED IN PRODUCTION**

Production proof is deliberately value-specific. A vocabulary family may be production-exercised without every value in that family having occurred.

## Extensibility

New controlled values require governed architectural change:

`Need Identified → Meaning Defined → Authority Collision Checked → Architecture Updated → Validation Updated → Canonical Value`

Unofficial labels are not canonical Attestor controlled values.

## Authority Boundary

Attestor Controlled Values govern Attestor meaning only. Source-institution vocabularies retain their source-defined meaning.

**Reference does not transfer authority.**

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Controlled Values → Established and Production-Proven**

- Attestation Type vocabulary → established; `verification-related` exercised
- Lifecycle vocabulary → established; `draft` / `active` exercised
- Publication vocabulary → established; `unpublished` / `published` exercised
- Evaluation outcomes → established; `supported` exercised
- Relationship vocabulary → established; `references` / `derived-from` exercised
- Provenance modes → established and represented in production context
- Authority contexts → established and represented in production context
- Validation result vocabulary → established and production-exercised
- Conformance result vocabulary → established and production-exercised
- confidence / reputation scoring → not adopted
- production proof → **ESTABLISHED for values actually exercised**

## Continuing Controlled-Value Governance

The first production operation does not establish that every canonical value has been exercised.

Values not required by the operation remain established without being characterized as independently production-tested, including:

- `superseded`;
- `withdrawn`;
- `retired`;
- `partially-supported`;
- `not-supported`;
- `contradicted`;
- `indeterminate`; and
- other relationship, Validation, or Conformance values not reached by the operation.

New values still require governed architectural change.

`Lifecycle State ≠ Publication State`

`Validation Result ≠ Evaluation Outcome`

`Validation ≠ Conformance`

`Evaluation Outcome ≠ Trust Statement`

`NOT-TESTED ≠ PASS`

**Reference does not transfer authority.**
