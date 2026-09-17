# Satoshium Attestor — Rules

## Page

`/attestor/rules/`

## Purpose

This page establishes the foundational operating rules of **Satoshium Attestor**.

The rules constrain how Attestor handles:

- Attestations;
- Evidence;
- authoritative references;
- evaluation;
- corrections and governed change;
- provenance;
- scope;
- institutional authority;
- Trust Statements.

They are foundational architectural rules, not yet the complete machine-validation specification.

## Governing Principle

> **Reference does not transfer authority.**

Attestor may reference authoritative objects governed by other Satoshium Suite institutions without inheriting, replacing, or redefining their authority.

## Foundational Rules

### Rule 1: Preserve Attribution

An Attestation, evidence source, authoritative reference, evaluation, correction, or Trust Statement should preserve sufficient attribution to identify who or what is responsible for the relevant assertion, source, or action.

### Rule 2: Preserve Provenance

Attestor should preserve sufficient provenance to explain the origin, relationship, status, and relevant history of inputs and Attestor objects used during evaluation.

### Rule 3: Preserve Scope

Assertions, evidence relationships, evaluations, and Trust Statements must remain bounded by the scope in which they are supported.

A narrow conclusion must not silently become a universal one.

### Rule 4: Preserve Authority Boundaries

Attestor may reference authoritative objects governed elsewhere, but it does not inherit, replace, or redefine their authority.

### Rule 5: Preserve Evidence Context

Evidence should remain connected to the assertion and evaluation for which it is relevant, including material limitations, conflicting information, and source status where applicable.

### Rule 6: Preserve Traceability

Relationships among Attestations, Evidence, authoritative references, evaluations, corrections, and Trust Statements should remain sufficiently traceable for review and validation.

### Rule 7: Preserve Governed Change

Corrections, clarifications, withdrawals, supersession, and other changes to Attestor-owned objects must not silently erase the prior state or provenance of the change.

### Rule 8: Distinguish Current and Historical State

Historically relevant prior states should remain traceable while being clearly distinguished from the currently effective state.

### Rule 9: Do Not Claim Universal Truth

A Trust Statement is a bounded Attestor conclusion produced under Attestor rules.

It does not establish universal truth.

### Rule 10: Do Not Convert Inputs into Conclusions

No single evidence item, verification result, Certification Package, Discovery Signal, historical event, or other input automatically determines a Trust Statement.

Attestor must perform its own governed evaluation.

### Rule 11: Preserve Uncertainty

Incomplete, conflicting, qualified, or insufficient inputs should result in preserved uncertainty rather than an unsupported stronger conclusion.

### Rule 12: Support Interoperability Without Authority Transfer

Attestor should exchange and reference governed information across the Suite without changing the canonical ownership, meaning, identifiers, lifecycle, or authority of referenced objects.

## Rule Application

The June-era page expressed the rule chain as:

`Attribution → Transparency → Accountability → Trust`

That progression is not carried forward as Attestor's operating model because Attestor does not produce “trust” as an institutional object.

The reconciled model is:

`Governed Inputs → Rule-Constrained Evaluation → Trust Statement`

The foundational rules operate together as constraints on evaluation rather than as steps that mechanically manufacture trust.

## Foundational Rules vs Validation Rules

This distinction is important.

The rules on this page express architectural requirements and institutional constraints.

Advanced Attestor architecture should later determine which requirements become normative machine-validation rules.

Conceptually:

`Foundational Rule → Normative Requirement → Validation Rule → Conformance`

This page therefore does not prematurely assign PASS/FAIL behavior, schemas, controlled values, or validation sequences.

## Governance Boundary

The pre-Suite page anticipated future:

- trust frameworks;
- dispute processes;
- reputation guidance;
- governance-related procedures.

Those concepts are not adopted as a future Attestor roadmap by this reconciliation.

Attestor may ultimately require institutional procedures for matters such as:

- review;
- dispute handling;
- correction authorization;
- publication;
- lifecycle operations.

Such procedures should be added only when required by Attestor's canonical responsibility.

Attestor should not silently become the owner of:

- a generic Suite-wide trust framework;
- a reputation system;
- Suite-wide governance authority.

## Relationship to Other Suite Institutions

Attestor may reference governed objects from other institutions, including Certification Packages, Satoshium Registry records, Chronicle Entries, Anchor Integrity References, Beacon Discovery Signals or Discovery Metadata, Atlas intelligence, Navigator workflow context, and other eligible sources.

The Rules page governs **Attestor's use of those references**, not the source institutions themselves.

## Reconciliation Notes

This revision updates the June-era pre-Suite Rules page.

Major changes include:

- replacing generic “trust-related recordkeeping” with Attestor-specific institutional constraints;
- expanding the original eight broad principles into twelve foundational rules;
- adding provenance as distinct from attribution;
- adding scope;
- adding authority boundaries;
- adding evidence-context preservation;
- adding governed change;
- distinguishing current from historical state;
- replacing “Separate Trust and Truth” with the more precise “Do Not Claim Universal Truth”;
- establishing that inputs do not automatically become conclusions;
- adding preservation of uncertainty;
- strengthening interoperability with an explicit no-authority-transfer rule;
- replacing `Attribution → Transparency → Accountability → Trust` with `Governed Inputs → Rule-Constrained Evaluation → Trust Statement`;
- distinguishing foundational rules from future machine-validation rules;
- removing generic trust frameworks and reputation guidance as assumed future Attestor responsibilities.

## Deferred to Advanced Architecture

The following remain intentionally unresolved:

- normative rule identifiers;
- MUST / SHOULD / MAY classification;
- validation rule numbering;
- PASS/FAIL conditions;
- validation sequence;
- evidence sufficiency requirements;
- uncertainty representation;
- conflict-resolution rules;
- correction authorization;
- dispute procedures;
- publication rules;
- lifecycle constraints;
- Trust Statement generation criteria;
- schemas;
- controlled values;
- conformance tests;
- reference vectors.

## Files

- `index.html` — public Rules page.
- `README.md` — repository documentation for the Rules page.
