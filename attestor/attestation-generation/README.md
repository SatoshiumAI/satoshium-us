# Satoshium Attestor — Attestation Generation

## Page

`/attestor/attestation-generation/`

## Purpose

This page establishes the foundational architecture for **forming an Attestation** within Satoshium Attestor.

An Attestation is a governed, attributable, bounded assertion.

Attestation Generation therefore concerns how such an assertion is formed from eligible inputs while preserving:

- purpose;
- subject;
- assertion;
- scope;
- attribution;
- evidence relationships;
- provenance;
- source state;
- source authority.

It does **not** define Trust Statement generation.

## Governing Principle

> **Reference does not transfer authority.**

Attestor may reference authoritative objects produced by other institutions without transforming those objects into Attestor-owned authority.

## Critical Object Distinction

The June-era page blurred **Attestation** and **Trust Statement**.

It stated both that the output of attestation generation was a structured Trust Statement and that an Attestation was itself a Trust Statement referencing certification.

That distinction is not carried forward.

The reconciled architecture is:

`Eligible Inputs → Attestation → Attestor Evaluation → Trust Statement`

### Attestation

A governed, attributable, bounded assertion.

### Trust Statement

Attestor's canonical institutional output: a governed, attributable, bounded conclusion produced through Attestor evaluation.

The Attestation participates in the evaluation.

It is not itself the final Trust Statement.

## No Automatic Source-to-Attestation Conversion

The old page described authoritative records as becoming structured Attestations.

The reconciled model does not treat source objects this way.

A source object remains its own canonical object.

Examples include:

- Atlas intelligence;
- Certification Package;
- Satoshium Registry Record;
- Chronicle Entry;
- Anchor Integrity Reference;
- Beacon Discovery Signal;
- Beacon Discovery Metadata.

An Attestation may reference an eligible source object.

The source object does not become the Attestation.

## Conceptual Generation Sequence

The foundational sequence is:

`Purpose Established → Subject Identified → Assertion Defined → Scope Bounded → Eligible Inputs Referenced → Provenance Preserved → Attestation Formed`

The page also recognizes attribution of the **Attesting Authority** as a foundational requirement, while leaving the final authority model unresolved.

This sequence is conceptual.

It does not establish a normative validation order or production algorithm.

## Generation Requirements

### Purpose Established

The reason for forming the Attestation should be sufficiently clear to determine the assertion and relevant inputs.

Whether “purpose” becomes a machine field remains unresolved.

### Subject Identified

The subject should be identifiable within the applicable model.

The final subject model remains unresolved.

### Assertion Defined

The Attestation should state the proposition being asserted.

It should not merely copy the contents of a source object.

### Scope Bounded

The assertion should preserve the conditions and limitations within which it applies.

The final scope schema remains unresolved.

### Eligible Inputs Referenced

Evidence and authoritative references may be associated only where future Attestor eligibility rules permit them.

Technical availability is not eligibility.

### Provenance Preserved

The origin, attribution, source relationships, relevant state, and authority of supporting inputs should remain traceable.

### Attesting Authority Attributed

An Attestation must ultimately identify who or what stands behind the assertion.

The final Attesting Authority model remains an advanced-architecture question.

### Attestation Formed

An Attestation may be formed once applicable generation and validation requirements are satisfied.

Those exact requirements remain to be established.

## Potential Governed Inputs

Potential Attestor inputs may include:

- Atlas Authoritative Intelligence;
- Navigator workflow context;
- Certifier Certification Packages;
- Satoshium Registry Records;
- Chronicle Entries;
- Anchor Integrity References;
- Beacon Discovery Signals;
- Beacon Discovery Metadata;
- other eligible governed sources.

These are **potential inputs**, not mandatory ingredients.

No source class is made universally required by this page.

## Certification Artifacts

The June page specifically named:

- Certification Package;
- SCPR;
- SCR;
- SCRD.

Those terms are preserved as historical/current Certifier-context possibilities where recognized by Certifier architecture.

This Attestor page does not independently redefine them or establish them as mandatory Attestation inputs.

Where a canonical Certification Package already provides the appropriate governed reference, advanced Attestor architecture should avoid unnecessary duplication of subordinate certification artifacts unless a specific evaluation requirement justifies direct reference.

## Attestation Generation vs Trust Statement Generation

This is the central reconciliation.

### Attestation Generation

Forms the governed assertion that will participate in Attestor evaluation.

### Attestor Evaluation

Applies Attestor rules to eligible inputs, evidence, provenance, status, scope, limitations, and the Attestation.

### Trust Statement Generation

Produces Attestor's canonical conclusion when applicable evaluation requirements are satisfied.

The next `/attestor/true-statements/` page should therefore be reconciled as the foundational **Trust Statements** page rather than as a claim that Attestor produces universally “true” statements.

## What Attestation Generation Does Not Do

Attestation Generation does not:

- issue a Certifier Certification Package;
- create or modify a Satoshium Registry Record;
- preserve a Chronicle Entry;
- establish an Anchor Integrity Reference;
- create a Beacon Discovery Signal or Discovery Metadata;
- assume Atlas authority;
- assume Navigator workflow authority;
- determine universal truth;
- automatically produce a Trust Statement.

## Publication

The June page included “Public Reference Preserved” as the final generation step and stated that a generated Attestation might be published, indexed, discovered, anchored, or cataloged.

This reconciliation does not make publication part of Attestation formation.

Formation and publication should remain separate concerns until advanced architecture determines:

- whether Attestations are public objects;
- whether all Attestations are publishable;
- publication states;
- discovery eligibility;
- Registry relationships;
- Anchor relationships;
- Trust Statement publication behavior.

## Reconciliation Notes

Major changes include:

- separating Attestation Generation from Trust Statement generation;
- defining the Attestation as the output of this page's process;
- removing the claim that Attestor “transforms referenced authority”;
- removing automatic conversion of certification or other source objects into Attestations;
- replacing the certification-first generation sequence with a source-neutral sequence;
- adding purpose;
- adding subject;
- adding assertion;
- adding scope;
- adding input eligibility;
- adding provenance;
- adding Attesting Authority attribution;
- preserving reference-based design;
- expanding possible governed inputs across the current Suite architecture;
- removing publication as an assumed final generation step;
- removing the implication that Certification Packages, SCRDs, SREGs, Chronicle events, Anchor references, and Beacon signals are all required;
- preserving exact machine generation rules for advanced architecture.

## Deferred to Advanced Architecture

The following remain intentionally unresolved:

- generation trigger;
- Attestation identifier format;
- Attestation schema;
- required and optional fields;
- subject model;
- Attesting Authority model;
- Attestation Type controls;
- purpose representation;
- scope fields;
- evidence eligibility;
- source eligibility;
- provenance fields;
- status vocabulary;
- initial lifecycle state;
- validation sequence;
- PASS/FAIL rules;
- duplicate-detection rules;
- correction and supersession relationships;
- publication eligibility;
- publication states;
- discovery relationships;
- Trust Statement generation criteria;
- conformance tests;
- reference vectors.

## Files

- `index.html` — public Attestation Generation page.
- `README.md` — repository documentation for the Attestation Generation page.
