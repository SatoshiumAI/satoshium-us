# Satoshium Attestor — Conformance

**Path:** `/attestor/conformance/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

Conformance defines what it means for an Attestor object, implementation, or governed process to conform to the applicable Attestor architecture, specification, or profile.

A conformance claim is bounded to:

- the target assessed;
- the declared requirements set;
- the applicable version/profile;
- the tested scope; and
- the evidence supporting the determination.

## Governing Model

`Target + Declared Requirements Set + Required Validation / Evidence → Conformance Determination`

## Conformance Dimensions

### Object Conformance

Determines whether an Attestation, Trust Statement, or other governed Attestor representation satisfies the complete applicable specification/profile requirements.

### Implementation Conformance

Determines whether an implementation correctly performs the Attestor capabilities and profiles it claims to support.

One valid output does not establish complete implementation conformance.

### Process Conformance

Where Attestor defines a normative process profile, determines whether the governed process follows required steps and preserves required authority, provenance, reviewability, and output behavior.

`Object Conformance ≠ Implementation Conformance ≠ Process Conformance`

## Declared Scope

A conformance claim should identify:

- conformance target;
- applicable specification/profile;
- specification/profile version;
- object class or capability;
- representation/serialization where applicable;
- validation/test basis;
- result; and
- relevant limitations.

**A conformance claim must be no broader than the scope actually assessed.**

## Validation vs. Conformance

Validation asks whether a particular object satisfies applicable normative checks.

Conformance asks whether the declared target meets the complete requirements of its claimed specification/profile.

`Validation supports Conformance`

`Validation ≠ Conformance`

Conceptually:

`Normative Requirements → Validation Rules → Validation Results → Conformance Evidence → Conformance Determination`

## Mandatory Requirements

Complete conformance requires satisfaction of all mandatory requirements applicable to the declared target/profile.

- mandatory applicable requirement → must be satisfied;
- optional requirement → governed by profile;
- not applicable → legitimately outside declared scope;
- untested mandatory requirement → complete conformance not established.

`Partial Testing ≠ Full Conformance`

## Profiles

Attestor may define:

- shared base requirements; and
- specialized profiles.

Specialized profiles may add bounded requirements for particular object classes, Attestation types, Trust Statement contexts, representations, or implementation capabilities.

`Base Conformance ≠ Specialized Profile Conformance`

## Version-Bound Conformance

Conformance is assessed against identifiable versions of applicable specifications/profiles.

`Target at Time T + Requirements Version at Time T → Conformance Determination at Time T`

Later specification changes do not silently rewrite historical conformance meaning.

## Conformance Failure

A mandatory failure means the declared conformance scope is not satisfied.

Incomplete testing means full conformance has not been established.

`Unknown ≠ Pass`

`Partial Pass ≠ Full Conformance`

## Interoperability

Conformance supports interoperability by creating a common requirements basis.

It does not guarantee universal interoperability.

`Conformance supports Interoperability`

`Conformance ≠ Universal Interoperability Guarantee`

## Authority

Conformance does not transfer institutional authority.

**Reference does not transfer authority.**

A conformant reference remains a reference to the source institution's canonical object.

## Publication

`Conformant ≠ Published`

`Published ≠ Conformant`

Conformance concerns requirements satisfaction.

Publication concerns authorization for public representation.

## Deferred Formal Specification

This architecture intentionally does not yet freeze:

- final conformance classes;
- executable test suites;
- conformance assertion format;
- final result vocabulary;
- conformance report schema;
- profile declaration syntax; or
- implementation certification mechanics.

Those depend on normative Schemas and finalized Validation rules.

## What Conformance Does Not Establish

`Conformant ≠ True`

`Conformant ≠ Supported`

`Conformant ≠ More Authoritative`

`Conformant ≠ Published`

`Conformant ≠ Universally Interoperable`

`Conformant ≠ Secure by definition`

`Conformant ≠ Trustworthy by definition`

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

This page establishes conceptual Conformance architecture. Final executable conformance remains downstream of normative Schemas and formal Validation rules.

## Status

**Conformance → Established conceptually**

- conformance target → required
- declared requirements scope → required
- object / implementation / process dimensions → distinguished
- profile-bounded claims → required
- version-bounded claims → required
- mandatory requirement completeness → required
- Validation as conformance evidence → established
- formal test suites / report schemas → deferred
- production conformance proof → pending
