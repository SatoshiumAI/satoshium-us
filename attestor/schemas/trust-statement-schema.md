# Trust Statement Schema — Advanced Architecture

## Purpose

This document defines the structural schema for a canonical **Trust Statement**, the governed institutional output of Satoshium Attestor.

A Trust Statement is a governed, attributable, bounded Attestor conclusion produced through Rule-Constrained Evaluation of an Attestation against eligible governed inputs.

## Canonical Context

**Attestor → Trust Statement**

`Attestation + Eligible Governed Inputs → Rule-Constrained Evaluation → Trust Statement`

A Trust Statement is distinct from the Attestation evaluated and from the Evaluation Outcome produced during evaluation.

> **Outcome ≠ Conclusion ≠ Trust Statement Identity**

## Canonical Identifier

Trust Statements use the established identifier family:

`TRST-YYYY-NNNN`

The identifier is assigned at canonical creation and must not be reused or reassigned.

## Structural Model

```yaml
trust_statement_identifier: TRST-YYYY-NNNN

lifecycle_state:
publication_state:

subject:
  identifier:
  type:

bounded_conclusion:
scope:

attestor_attribution:
  identifier:
  authority_context: Attestor

supporting_attestations:
  -

evaluation:
  outcome:
  basis_references:
    -
  applicable_rules:
    -
  relevant_time_or_state:
  material_conflicts:
    -
  material_exclusions:
    -

provenance:
  mode: derived
  source_or_origin:
  derivation_basis:
  material_limitations:

relationships:
  -

created_at:
updated_at:
version_identity:

limitations:
  -
uncertainty:
  -
notes:
```

Exact serialization requirements and field cardinalities remain governed by the applicable normative schema and validation implementation. This structural model must not be used to invent information that is unavailable or inapplicable.

## Core Structural Requirements

A canonical Trust Statement must be capable of preserving:

- canonical Trust Statement identity;
- lifecycle state;
- publication state;
- subject identity/context;
- bounded Attestor conclusion;
- scope of that conclusion;
- Attestor attribution;
- supporting Attestation reference(s) as applicable;
- Evaluation Outcome;
- evaluation basis;
- applicable rules or methodology context;
- relevant time or source state;
- material conflicts and exclusions where applicable;
- provenance of the conclusion;
- relationships to governed objects;
- creation/update context;
- version identity;
- material limitations; and
- uncertainty where applicable.

## Evaluation Outcome

The controlled Evaluation Outcome vocabulary is:

- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

The Evaluation Outcome is an input to formation of the bounded conclusion. It is not itself the complete Trust Statement.

## Lifecycle State

The controlled lifecycle states are:

- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

Lifecycle state is distinct from publication state.

## Publication State

The controlled publication states are:

- `unpublished`
- `published`

> **Canonical Creation ≠ Lifecycle Activation ≠ Publication**

A Trust Statement may exist canonically without being publicly published.

## Provenance

A Trust Statement is ordinarily a **derived** Attestor object because its conclusion results from governed evaluation.

Its provenance must preserve sufficient traceability to reconstruct the basis of the conclusion without converting referenced source authority into Attestor authority.

Where material, provenance should preserve:

- supporting Attestation(s);
- eligible governed inputs;
- evaluation basis;
- applicable rules;
- source state at evaluation;
- derivation basis;
- limitations; and
- material exclusions or conflicts.

## Authority

Attestor is authoritative for the Trust Statement it creates and for the bounded Attestor conclusion expressed by that statement.

Attestor does not become authoritative for the underlying source objects merely because they contributed to evaluation.

> **Reference does not transfer authority.**

## Relationships

Trust Statement relationships use the adopted Attestor relationship vocabulary where applicable:

- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

Relationship direction must preserve the source → target meaning defined by Attestor relationship architecture.

A relationship does not by itself establish eligibility, authority transfer, or Evaluation Outcome.

## Versioning and Change

Canonical identifier and version identity answer different questions:

- canonical identifier → which governed Trust Statement;
- version identity → which governed state of that Trust Statement.

A bounded correction that does not materially alter the essential institutional meaning may preserve the canonical Trust Statement identifier through governed versioning.

A materially different conclusion requires a **new canonical Trust Statement** and therefore a new `TRST-YYYY-NNNN` identifier.

> **A changed conclusion is a changed canonical statement.**

Prior governed states must remain traceable.

## Validation

A Trust Statement must satisfy the normative requirements applicable to its object type before it can be treated as valid.

`Trust Statement → Applicable Validation Rules → Validation Result`

Validation determines structural/rule compliance. It does not determine whether the conclusion is substantively favorable.

> **Validation ≠ Evaluation**

> **Valid ≠ Published**

## Conformance

Conformance is separately determined against a declared requirements set.

> **Validation supports Conformance.**

> **Validation ≠ Conformance.**

A Trust Statement is not conformant merely because it exists or has been published.

## Publication

Publication is a separate governed decision.

`Canonical Trust Statement + Governed Publication Decision → Authorized Public Representation`

Publication does not enlarge the conclusion, scope, authority, or evidentiary basis of the Trust Statement.

## Explicit Boundaries

A Trust Statement is not:

- a declaration of universal truth;
- a generic reputation record;
- a trust score;
- a confidence percentage;
- a certification;
- a verification result;
- a Beacon Discovery Signal;
- an automatic restatement of source authority; or
- a guarantee of permanent correctness.

Its conclusion remains bounded by its scope, evaluation basis, relevant state, provenance, limitations, and uncertainty.

## Status

**Trust Statement Schema → Advanced Architecture established.**

Machine serialization, executable validation, and production-instance requirements must remain aligned with Attestor Validation, Conformance, Publication, Methodology, and Production architecture.
