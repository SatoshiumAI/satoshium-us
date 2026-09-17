# Satoshium Attestor — FAQ

## Page

`/attestor/faq/`

## Purpose

This page provides concise answers to common questions about the reconciled foundational architecture of **Satoshium Attestor**.

The FAQ is explanatory.

It should reflect adopted or established foundational architecture without independently creating new canonical objects, controlled values, lifecycle states, or machine rules.

## Canonical Responsibility

**Attestor → Trust Statement**

A Trust Statement is a governed, attributable, bounded conclusion produced through Attestor evaluation.

## Governing Principle

> **Reference does not transfer authority.**

A source institution remains authoritative for its canonical object even when Attestor references that object during evaluation.

## Core FAQ Architecture

### What is Attestor?

Attestor is the Satoshium Suite institution responsible for producing governed, attributable, bounded Trust Statements through evaluation of eligible inputs.

The June-era description of Attestor as the generic “trust layer” is not carried forward.

### What is a Trust Statement?

A Trust Statement is Attestor's canonical output.

It is a bounded conclusion, not universal truth and not a generic trust score.

### Does Attestor determine truth?

No.

Attestor produces a conclusion within a defined scope under Attestor rules.

It does not establish universal truth.

### What is an Attestation?

An Attestation is a governed, attributable, bounded assertion.

It is distinct from the Trust Statement.

### Attestation vs Trust Statement

The foundational relationship is:

`Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

- **Attestation** → assertion.
- **Trust Statement** → evaluated conclusion.

### What role does Evidence play?

Evidence provides supporting material or authoritative references used during evaluation.

Evidence does not become proof merely because Attestor references it.

Applicable provenance, relevance, scope, status, limitations, and source authority should remain visible.

### What is a trust signal?

The term remains descriptive language for **trust-relevant evaluation context**.

It is not presently established as:

- a canonical Attestor object;
- a controlled record type;
- a reputation score;
- an automatic trust indicator.

It must remain distinct from:

**Beacon → Discovery Signal / Discovery Metadata**

### Certifier relationship

**Certifier → Certification Package**

Attestor may reference a Certification Package when relevant and eligible.

Attestor does not certify or recertify the subject.

### Anchor relationship

**Anchor → Integrity Reference**

The June FAQ incorrectly stated:

> “Anchor manages identity.”

That mapping is not carried forward.

Attestor may reference an Anchor Integrity Reference without assuming Anchor authority.

### Beacon relationship

**Beacon → Discovery Signal / Discovery Metadata**

Attestor may reference Beacon discovery objects.

It does not create or redefine them.

### Registry and Chronicle

**Registry → Satoshium Registry Record**

**Chronicle → Chronicle Entry**

Attestor may reference these objects while their source institutions retain authority.

## Reference Does Not Transfer Authority

The FAQ includes an explicit plain-language explanation of the governing principle.

Conceptually:

`Source Object → Retains Source Authority`

`Attestor Evaluation → Governs Attestor Use`

`Trust Statement → Retains Attestor Authority`

This distinction is central to Suite interoperability.

## Corrections

The June FAQ asked whether “records” can be corrected.

That wording was too broad because Attestor does not own every referenced record.

The reconciled question is:

> **Can Attestor-owned information be corrected?**

Yes.

Attestor requires governed treatment for changes affecting its own Attestations and Trust Statements.

The exact correction, withdrawal, supersession, and versioning mechanics remain advanced architecture.

## Reputation and Trust Scores

The June FAQ described reputation frameworks as potentially part of future Attestor implementations.

That assumption is not carried forward.

Under the current foundational architecture:

- reputation is not an Attestor canonical object;
- no Attestor reputation system is established;
- no automatic trust score is established;
- Attestor's canonical output is the Trust Statement.

A future requirement could be evaluated later, but it should not be inherited from the June model without architectural justification.

## Publication

The FAQ explicitly states that Trust Statements are **not yet assumed to be automatically public**.

Advanced architecture must determine:

- publication eligibility;
- visibility;
- publication states;
- public/private treatment;
- Registry relationships;
- Beacon discovery relationships;
- Anchor relationships;
- publication validation.

## Operational Status

Attestor is **not yet operational**.

Current posture:

**Foundational Reconciliation**

Remaining work includes:

- advanced schemas;
- controlled values;
- evaluation rules;
- lifecycle architecture;
- validation;
- conformance;
- first governed production Trust Statement.

Production status should be earned through production proof.

## What Remains Open

The FAQ summarizes major unresolved advanced-architecture areas:

- identifiers;
- schemas;
- controlled values;
- Attestation Types;
- subject model;
- Attesting Authority / producer model;
- scope fields;
- evidence eligibility;
- evaluation rules;
- sufficiency rules;
- uncertainty representation;
- lifecycle states;
- validation;
- publication;
- conformance tests;
- reference vectors;
- production procedures.

This list is explanatory and does not itself define the future architecture.

## Removal of the June Trust Progression

The June FAQ ended with:

`Attestation → Evidence → Trust Signals → Reputation → Trust`

That progression is not carried forward.

It implied:

- a linear trust-production process;
- canonical Trust Signals;
- reputation as an Attestor architectural stage;
- “Trust” as the final Attestor output.

The reconciled foundational relationship is:

`Governed Inputs → Attestation → Evaluation → Trust Statement`

Attestor does not manufacture abstract trust.

It produces governed Trust Statements.

## Reconciliation Notes

Major changes include:

- replacing “trust layer” with Attestor's canonical institutional responsibility;
- adding a direct Trust Statement definition;
- strengthening the universal-truth boundary;
- updating the Attestation definition;
- adding the Attestation vs Trust Statement distinction;
- updating Evidence terminology;
- demoting Trust Signal to descriptive trust-relevant context;
- correcting Certifier from generic verification to Certification Package;
- correcting Anchor from identity management to Integrity Reference;
- adding Beacon's canonical Discovery Signal / Discovery Metadata boundary;
- adding Registry and Chronicle authority boundaries;
- explaining “Reference does not transfer authority” in plain language;
- narrowing correction language to Attestor-owned objects;
- removing reputation systems and trust scores as assumed future architecture;
- adding publication uncertainty;
- updating operational status to foundational reconciliation;
- adding an explanation of unresolved advanced architecture;
- replacing the old trust progression with the reconciled Attestor model;
- updating the closing reflection to emphasize reviewability, scope, provenance, limitations, and authority.

## Foundational Review Note

This FAQ is the final page in the current foundational Attestor page-by-page reconciliation sequence.

Completion of this page should **not** automatically trigger advanced architecture.

The recommended next step is a whole-foundation review across all reconciled Attestor pages to identify:

- terminology collisions;
- inconsistent definitions;
- duplicated responsibilities;
- missing concepts;
- premature claims;
- unresolved route issues;
- stale navigation;
- inconsistencies between public pages and READMEs;
- concepts that have become foundational through repeated use;
- questions that should be formally carried into advanced architecture.

Only after that review should the Attestor foundation be treated as reconciled and the advanced architecture phase begin.

## Files

- `index.html` — public FAQ page.
- `README.md` — repository documentation for the FAQ page.
