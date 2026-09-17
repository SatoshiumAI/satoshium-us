# Satoshium Attestor — Principles

## Page

`/attestor/principles/`

## Purpose

This page defines the foundational principles that guide Satoshium Attestor.

The principles constrain how Attestor should:

- form Attestations;
- use Evidence and authoritative references;
- preserve provenance;
- establish scope;
- evaluate eligible inputs;
- preserve uncertainty;
- govern change;
- respect institutional authority;
- produce Trust Statements.

They are architectural commitments, not yet a complete machine-validation specification.

## Canonical Responsibility

**Attestor → Trust Statement**

## Governing Principle

> **Reference does not transfer authority.**

This principle is central to Attestor and the wider Satoshium Suite.

Attestor may reference a governed object without becoming the canonical authority for that object.

## Why This Page Was Reconciled Separately

The earlier foundational page inventory omitted `/attestor/principles/`.

The June-era Principles page nevertheless contains material that overlaps directly with the reconciled Attestor Rules, Scope, Evidence, Corrections, Interoperability, and Trust Statement architecture.

It therefore requires reconciliation before the whole-foundation review can accurately treat the Attestor foundation as complete.

## Foundational Principles

### Bounded Conclusions

A Trust Statement should say no more than the applicable:

- Attestation;
- eligible inputs;
- Evidence;
- provenance;
- scope;
- status;
- limitations;
- evaluation

support.

This replaces generic language about “trust” emerging from broad context.

### Attribution

Attestor-governed assertions, conclusions, and changes should remain attributable.

The final Attesting Authority / producer model remains advanced architecture.

### Provenance

The origin, attribution, source relationships, relevant state, and history necessary to understand an input, assertion, evaluation, or output should remain traceable.

### Scope

Assertions and conclusions must preserve the boundaries within which they apply.

A bounded conclusion must not silently become universal.

### Traceability

Relationships among:

- Attestations;
- Evidence;
- authoritative references;
- evaluations;
- Trust Statements;
- governed changes

should support review and reconstruction of the relevant basis.

### Evidence Context

Evidence should remain connected to its:

- relevance;
- provenance;
- status;
- scope;
- limitations;
- source authority.

Evidence does not become proof merely because it is referenced.

### Preserve Uncertainty

Incomplete, conflicting, qualified, or insufficient information should remain visible where material.

Attestor should not manufacture certainty.

### Governed Change

Changes to Attestor-owned objects should preserve provenance and historical traceability while allowing the current state to remain identifiable.

This includes architectural concerns such as:

- correction;
- clarification;
- withdrawal;
- supersession.

Exact lifecycle mechanics remain unresolved.

### Authority Boundaries

Attestor may reference governed objects from other institutions without assuming their canonical responsibilities.

Conceptually:

`Source Object → Retains Source Authority`

`Attestor → Governs Its Own Assertion, Evaluation, and Trust Statement`

### Interoperability

Information crossing institutional boundaries should preserve the meaning and context required for correct interpretation.

This includes, as applicable:

- provenance;
- scope;
- status;
- relationships;
- limitations;
- authority.

### No Automatic Conversion

No source object or evidence item automatically becomes an Attestation or determines a Trust Statement.

This includes:

- Certification Packages;
- Satoshium Registry records;
- Chronicle Entries;
- Anchor Integrity References;
- Beacon Discovery Signals;
- Evidence;
- other eligible governed inputs.

### Reviewability

A Trust Statement should preserve enough information to understand:

- what was concluded;
- what supported the conclusion;
- where the conclusion applies;
- what limits the conclusion;
- who or what is responsible;
- where Attestor's authority ends.

## Principles in Operation

The foundational Attestor relationship is:

`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

The principles constrain every stage.

The sequence does **not** mean:

- every available input is eligible;
- every eligible input must be used;
- every Attestation warrants a Trust Statement;
- every Trust Statement is favorable;
- every Trust Statement is public;
- a Trust Statement is universal.

## Principles vs Rules

The Principles and Rules pages should remain distinct.

### Principles

Express foundational architectural commitments.

### Rules

Translate those commitments into institutional constraints.

### Advanced Architecture

Should translate applicable rules into:

- normative requirements;
- validation rules;
- schemas;
- controlled values;
- conformance tests;
- reference vectors.

Conceptually:

`Principle → Rule → Normative Requirement → Validation → Conformance`

This relationship should be checked during the whole-foundation review to remove unnecessary duplication between `/attestor/principles/` and `/attestor/rules/`.

## Removal of the June Principle Chain

The June page used:

`Transparency → Accountability → Reputation → Trust`

That chain is not carried forward.

It implied:

- reputation as an Attestor architectural stage;
- abstract Trust as the final Attestor output;
- a linear progression not supported by the reconciled architecture.

The reconciled operational relationship is:

`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

## Transparency

The June page treated Transparency as a standalone foundational principle.

Transparency remains valuable, but the reconciled architecture expresses the enforceable substance more precisely through:

- attribution;
- provenance;
- traceability;
- scope;
- evidence context;
- uncertainty;
- reviewability;
- governed change.

The whole-foundation review may determine whether **Transparency** should remain an explicit named principle in addition to those more precise requirements.

This page does not prematurely settle that editorial question.

## Accountability

The June page also treated Accountability as a standalone principle.

The reconciled architecture preserves its substance through:

- attribution;
- authority;
- traceability;
- governed change;
- reviewability.

The whole-foundation review should determine whether Accountability remains useful as a named umbrella principle or whether it is better expressed through these specific requirements.

## Historical Preservation

The June principle of Historical Preservation is preserved more precisely as **Governed Change** plus the distinction between current and historical state.

Attestor should preserve the provenance of what came before without presenting a superseded or withdrawn state as current.

## Context Matters

The June principle “Context Matters” is preserved through more specific concepts:

- Evidence Context;
- Scope;
- Provenance;
- Relevant State;
- Limitations;
- Relationships.

## Humility

The June principle “Humility” is preserved architecturally as **Preserve Uncertainty** and **Bounded Conclusions**.

Those terms are more directly testable and can later support normative rules.

## Guiding Philosophy

Attestor does not seek to establish:

- universal truth;
- generic reputation;
- an automatic trust score.

Its canonical output is the **Trust Statement**.

A Trust Statement should remain bounded by what its evidence, provenance, scope, limitations, status, and authority support.

## Reconciliation Notes

Major changes include:

- replacing generic trust-system framing with Attestor's canonical responsibility;
- adding the governing authority principle;
- adding Bounded Conclusions;
- retaining Attribution with stronger authority language;
- adding Provenance;
- adding Scope;
- strengthening Traceability;
- replacing generic context with Evidence Context;
- replacing Humility with Preserve Uncertainty;
- replacing Historical Preservation with Governed Change;
- adding Authority Boundaries;
- strengthening Interoperability;
- adding No Automatic Conversion;
- adding Reviewability;
- replacing the reputation/trust principle chain;
- distinguishing Principles from Rules;
- preserving Transparency and Accountability as whole-foundation editorial questions rather than silently discarding their substance;
- aligning the page with the reconciled Attestation / Evaluation / Trust Statement model.

## Whole-Foundation Review Questions

This page introduces several questions that should now be resolved during the whole-foundation review:

1. Should **Transparency** remain an explicit named Attestor principle, or is its substance sufficiently represented by provenance, traceability, scope, uncertainty, and reviewability?
2. Should **Accountability** remain an umbrella principle, or be represented through attribution, authority, traceability, governed change, and reviewability?
3. Is there unnecessary duplication between the Principles and Rules pages?
4. Which principles should become normative requirements in advanced architecture?
5. Should every foundational rule map explicitly to one or more principles?
6. Should the foundational architecture establish a formal principle identifier system, or defer identifiers until normative rules?
7. Are **Bounded Conclusions**, **Preserve Uncertainty**, and **Reviewability** sufficiently distinct to remain separate?
8. Does **Evidence Context** belong at principle level, or should it remain primarily a Rules/Evidence concern?

## Deferred to Advanced Architecture

This page does not establish:

- principle identifiers;
- normative MUST/SHOULD/MAY language;
- validation rule identifiers;
- machine schemas;
- controlled values;
- evaluation algorithms;
- sufficiency thresholds;
- conformance tests;
- reference vectors.

## Files

- `index.html` — public Principles page.
- `README.md` — repository documentation for the Principles page.
