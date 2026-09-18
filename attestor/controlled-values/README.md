# Satoshium Attestor — Controlled Values

**Path:** `/attestor/controlled-values/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
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

## Reserved Vocabularies

The exact executable result vocabularies for **Validation** and **Conformance** are deliberately not established here. Their governing architectures are established; result vocabularies remain reserved until implementation can define stable machine outcomes consistent with those architectures.

Related normative responsibility is already assigned:

- schema constraints → Schemas / Profiles;
- transition rules → Lifecycle;
- relationship behavior → Relationships;
- evaluation conditions → Evaluation.

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

**Controlled Values → Established**

Normative vocabularies are established for Attestation Types, lifecycle, publication, evaluation outcomes, relationships, provenance modes, and authority contexts.

Confidence/reputation scoring is not adopted. Validation and Conformance result vocabularies remain reserved for implementation.
