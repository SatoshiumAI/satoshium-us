# Satoshium Attestor — Trust Statements

## Page

`/attestor/trust-statements/`

## Canonical Responsibility

**Attestor → Trust Statement**

This page defines the foundational meaning and architectural requirements of Attestor's canonical institutional output.

## Definition

A **Trust Statement** is a governed, attributable, bounded conclusion produced by Satoshium Attestor through evaluation of eligible inputs.

A Trust Statement should preserve the basis and limits of its conclusion without replacing the authority of the evidence, records, certifications, or other governed objects it references.

## Governing Principle

> **Reference does not transfer authority.**

Attestor owns the Trust Statement it produces.

It does not inherit the canonical authority of referenced source objects.

## Trust Statement vs Attestation

This distinction is foundational.

### Attestation

A governed, attributable, bounded **assertion**.

### Trust Statement

A governed, attributable, bounded **conclusion** produced through Attestor evaluation.

The relationship is:

`Eligible Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`

The June-era page blurred these objects by describing the Trust Statement as “a structured attestation.”

That wording is not carried forward.

## Foundational Trust Statement Content

A Trust Statement should preserve enough information to make its conclusion identifiable, attributable, scoped, reviewable, and traceable.

Foundational information concerns include:

- identity;
- subject;
- conclusion;
- scope;
- attribution;
- supporting Attestations;
- Evidence;
- authoritative references;
- provenance;
- status;
- limitations;
- relevant time or source state;
- relationships.

These are **not yet adopted machine fields**.

The final schema belongs to advanced Attestor architecture.

## Identity

A Trust Statement should be uniquely distinguishable so it can participate in governed relationships and lifecycle operations.

The final identifier format is not established by this page.

## Subject

The Trust Statement must identify what its conclusion concerns.

The final subject model and supported subject classes remain unresolved.

## Conclusion

The Trust Statement should state the bounded conclusion reached by Attestor.

Its language must not claim more than the evaluation supports.

Advanced architecture must determine the conclusion model and whether controlled conclusion values are required.

## Scope

Scope defines the boundary within which the conclusion applies.

A conclusion supported for one:

- subject;
- condition;
- period;
- jurisdiction;
- purpose;
- relationship;
- other bounded context

must not silently become a universal conclusion.

No final scope-field model is adopted here.

## Attribution

The Trust Statement should preserve who or what is responsible for the Attestor conclusion under the eventual authority model.

The exact Attestor authority / producer model remains unresolved.

## Supporting Basis

The supporting basis may include:

- Attestations;
- Evidence;
- authoritative references;
- relevant source states;
- material conflicting evidence;
- qualifying information.

No single input automatically determines the Trust Statement.

## Provenance and Source Authority

The provenance and authority of supporting inputs must remain distinguishable from Attestor's authority over the Trust Statement.

Conceptually:

`Source Object → Retains Source Authority`

`Trust Statement → Retains Attestor Authority`

## Status and Relevant State

A Trust Statement should support a governed lifecycle.

It should preserve enough temporal and source-state context to understand the basis upon which the conclusion was produced.

The exact status vocabulary remains unresolved.

## Limitations and Uncertainty

Material limitations and uncertainty should remain visible when they affect interpretation of the conclusion.

This includes potentially:

- incomplete information;
- conflicting evidence;
- qualified evidence;
- unavailable sources;
- unresolved status;
- limited scope;
- temporal limitations.

The representation of uncertainty remains advanced architecture.

## Relationship to the Suite

Trust Statements may reference governed outputs across the Suite:

- **Atlas → Authoritative Intelligence**
- **Navigator → Workflow Definition / Orchestration**
- **Certifier → Certification Package**
- **Registry → Satoshium Registry Record**
- **Chronicle → Chronicle Entry**
- **Anchor → Integrity Reference**
- **Beacon → Discovery Signal / Discovery Metadata**
- **Attestor → Trust Statement**

Attestor does not absorb the canonical authority of those institutions.

## What a Trust Statement Does Not Do

A Trust Statement does not:

- establish universal truth;
- issue a Certifier Certification Package;
- create or redefine a Satoshium Registry Record;
- rewrite a Chronicle Entry;
- establish an Anchor Integrity Reference;
- create a Beacon Discovery Signal or Discovery Metadata;
- assume Atlas authority;
- assume Navigator workflow authority;
- automatically establish reputation;
- create a universal trust score;
- declare a person, organization, record, or subject universally trustworthy.

A Trust Statement is authoritative **as an Attestor conclusion within its defined scope**.

That authority does not extend beyond Attestor's institutional responsibility.

## Certification Relationship

The June page framed certification as establishing authority and the Trust Statement as expressing trust “about that authority.”

The reconciled model is narrower.

A Certification Package may be an authoritative input to Attestor.

Certifier remains authoritative for the certification.

Attestor remains authoritative for its own bounded Trust Statement.

Certification is therefore neither automatically required nor automatically sufficient for a Trust Statement unless future Attestor rules establish such a requirement for a particular evaluation.

## Trust Statement Type

The June page proposed a `Statement Type` with examples such as:

- certification-supported;
- integrity-supported;
- event-supported;
- record-supported.

Those values are **not adopted** as a controlled Trust Statement taxonomy.

Advanced architecture should determine whether Trust Statements require:

- types;
- classes;
- conclusion categories;
- profiles;
- another classification mechanism;
- no separate type system.

The decision should follow actual requirements.

## Public References and Publication

The June page assumed Public References as part of Trust Statement content and described Trust Statements as objects that could be cataloged, discovered, anchored, or corrected.

This reconciliation preserves traceability as a foundational requirement but does not assume every Trust Statement is public.

Advanced architecture should determine:

- publication eligibility;
- publication states;
- public/private visibility;
- public reference requirements;
- Registry relationships;
- Beacon discovery relationships;
- Anchor relationships;
- publication validation;
- withdrawal from publication.

## Lifecycle and Change

A Trust Statement may require review when its supporting basis or material conditions change.

Advanced architecture should determine lifecycle behavior for:

- creation;
- validation;
- review;
- approval, if any;
- activation;
- publication;
- correction;
- withdrawal;
- supersession;
- versioning;
- archival or historical retention.

The current state should remain distinguishable from historically relevant prior states.

## Reconciliation Notes

Major changes include:

- making Trust Statement explicitly Attestor's canonical output;
- defining a Trust Statement as a conclusion rather than an Attestation;
- separating Attestation generation from Trust Statement generation;
- replacing generic “accountable trust” language with bounded Attestor conclusion;
- adding scope as a foundational requirement;
- adding limitations and uncertainty;
- adding status and source-state context;
- adding provenance and authority separation;
- replacing the June field list with foundational information concerns rather than premature machine fields;
- removing the proposed Statement Type taxonomy from adopted architecture;
- correcting all Suite institutional mappings;
- removing the implication that certification is automatically required or sufficient;
- removing universal trust/reputation implications;
- separating traceability from mandatory public publication;
- adding lifecycle and source-change concerns;
- preserving exact schemas, identifiers, controlled values, validation, and publication mechanics for advanced architecture.

## Path Note

Earlier Attestor navigation used `/attestor/true-statements/` while this source page declares the canonical URL:

`/attestor/trust-statements/`

The reconciled content uses **Trust Statements** as the concept name.

Before final Attestor reconciliation, the site should choose one canonical public route and update navigation, canonical tags, redirects, and internal links consistently.

Given the established canonical object name **Trust Statement**, `/attestor/trust-statements/` is the semantically clearer route, but route migration should be handled deliberately rather than silently within this content reconciliation.

## Deferred to Advanced Architecture

The following remain intentionally unresolved:

- Trust Statement identifier format;
- machine schema;
- required and optional fields;
- subject model;
- producer / Attestor authority model;
- conclusion model;
- controlled conclusion values;
- Trust Statement type or profile model;
- scope fields;
- Evidence relationships;
- Attestation relationships;
- provenance fields;
- source-state representation;
- status vocabulary;
- uncertainty representation;
- sufficiency rules;
- conflicting-evidence treatment;
- validation sequence;
- generation criteria;
- lifecycle states;
- versioning;
- correction;
- withdrawal;
- supersession;
- publication eligibility;
- publication states;
- public/private visibility;
- Registry relationships;
- Beacon discovery relationships;
- Anchor relationships;
- conformance tests;
- reference vectors.

## Files

- `index.html` — public Trust Statements page.
- `README.md` — repository documentation for the Trust Statements page.
