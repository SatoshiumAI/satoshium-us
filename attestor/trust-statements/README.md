# Satoshium Attestor — Trust Statements

## Page
`/attestor/trust-statements/`

## Canonical Responsibility
**Attestor → Trust Statement**

## Definition
A **Trust Statement** is a governed, attributable, bounded Attestor conclusion produced through Rule-Constrained Evaluation of an Attestation against eligible governed inputs.

Canonical model:

`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

## Governing Principle
> **Reference does not transfer authority.**

Attestor owns the Trust Statement and its bounded conclusion. Referenced institutions and external authorities retain authority over their own source objects.

## Trust Statement vs Attestation
- **Attestation** → governed, attributable assertion.
- **Trust Statement** → governed, attributable, bounded Attestor conclusion.

> **Outcome ≠ Conclusion ≠ Trust Statement Identity**

## Canonical Identifier
Trust Statements use:

`TRST-YYYY-NNNN`

The canonical identifier answers **which governed object**. Version identity answers **which governed state of that object**.

Identifiers are assigned at canonical creation and are not reused or reassigned.

## Structural Architecture
The adopted Trust Statement schema preserves, as applicable:
- canonical identity;
- lifecycle state;
- publication state;
- subject identity/context;
- bounded conclusion;
- scope;
- Attestor attribution;
- supporting Attestation reference(s);
- Evaluation Outcome;
- evaluation basis;
- applicable rules/methodology;
- relevant time/source state;
- material conflicts and exclusions;
- provenance;
- relationships;
- creation/update information;
- version identity;
- limitations;
- uncertainty.

Exact production serialization and executable validation remain governed by the implementation layer.

## Evaluation Outcomes
Adopted values:
- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

An Evaluation Outcome is not itself the bounded conclusion and is not the identity of the Trust Statement.

## Authority
Attestor is authoritative for the Trust Statement and its bounded Attestor conclusion.

Referenced authority remains with the originating source.

> **Attribution ≠ Adoption**

> **Authority ≠ Eligibility ≠ Evaluation Outcome**

## Provenance
A Trust Statement is ordinarily a **derived** object.

Its provenance should preserve:
- supporting Attestations;
- eligible governed inputs;
- evaluation basis;
- applicable rules;
- relevant source state at evaluation;
- derivation basis;
- material limitations;
- conflicts or exclusions.

## Relationships
Adopted relationship vocabulary:
- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

## Lifecycle
Adopted lifecycle states:
- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

Review and correction are activities, not lifecycle states.

## Publication
Adopted publication states:
- `unpublished`
- `published`

> **Canonical Creation ≠ Lifecycle Activation ≠ Publication**

Technically accessible does not necessarily mean Published.

## Versioning and Material Change
A bounded correction may preserve canonical identity when the Trust Statement's essential institutional meaning remains intact.

A materially different conclusion requires a new canonical Trust Statement and therefore a new `TRST-YYYY-NNNN`.

> **A changed conclusion is a changed canonical statement.**

Prior governed states remain preserved rather than silently overwritten.

## Validation
Conceptual validation model:

`Trust Statement → Applicable Validation Rules → Validation Result`

> **Validation ≠ Evaluation**

> **Valid ≠ Published**

Executable validation rules and final Validation Result vocabulary remain implementation work.

## Conformance
Validation supports conformance, but does not equal it.

> **Validation ≠ Conformance**

Conformance mechanics, tests, and final result vocabulary remain implementation work.

## Relationship to the Suite
- **Atlas → Authoritative Intelligence**
- **Navigator → Workflow Definition / Orchestration**
- **Certifier → Certification Package**
- **Registry → Satoshium Registry Record**
- **Chronicle → Chronicle Entry**
- **Anchor → Integrity Reference**
- **Beacon → Discovery Signal / Discovery Metadata**
- **Attestor → Trust Statement**

Attestor may reference these outputs without absorbing their institutional authority.

## Trust Statement Boundaries
A Trust Statement is not:
- a declaration of universal truth;
- a generic reputation record;
- a trust score;
- a confidence percentage;
- a certification;
- a verification result;
- a Beacon Discovery Signal;
- an automatic restatement of source authority;
- a guarantee of permanent correctness.

It is authoritative as an Attestor conclusion within its defined scope.

## Current Status
**Trust Statement Architecture → Advanced Architecture established.**

The Trust Statement schema, identifier family, controlled evaluation outcomes, lifecycle, publication states, provenance model, relationships, validation architecture, conformance architecture, methodology, and production path are established.

Remaining work is implementation and production proof:
- executable validation;
- conformance mechanics;
- production alignment;
- Production Readiness Gate;
- first real governed Trust Statement operation;
- post-operation review;
- operational proof determination.

## Files
- `index.html` — public Trust Statements page.
- `README.md` — repository documentation for the Trust Statements page.
