# Satoshium Attestor — Validation

**Path:** `/attestor/validation/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

Validation defines whether an Attestor object satisfies Attestor's applicable normative structural and rule requirements.

It determines whether an object is correctly formed and governed according to Attestor architecture.

It does **not** determine whether an assertion is true or whether a Trust Statement conclusion is favorable.

## Governing Model

`Object + Applicable Normative Requirements → Validation → Governed Validation Result`

## Validation Layers

Attestor validation is layered:

1. Representation / syntax
2. Structural requirements
3. Controlled semantics
4. Relationships
5. Provenance / authority context
6. Lifecycle / versioning
7. Normative Attestor rules

`Machine-readable ≠ Valid`

## Normative Requirement Chain

`Principle → Rule → Normative Requirement → Validation Rule → Validation Result`

The validator implements adopted architecture.

**The validator does not create architecture.**

## Object-Class Validation

Attestations and Trust Statements require distinct validation profiles.

### Attestation

Conceptual validation areas include:

- canonical identity;
- Attestation type;
- Attesting Authority;
- subject;
- assertion;
- scope;
- provenance;
- governed references;
- lifecycle context; and
- applicable relationships.

### Trust Statement

Conceptual validation areas include:

- canonical identity;
- subject;
- bounded conclusion;
- Attestor attribution;
- supporting Attestation(s);
- evaluation basis;
- provenance;
- limitations / uncertainty;
- relevant time/state;
- lifecycle context; and
- applicable relationships.

Shared requirements may be reused where architecture permits.

## Evaluation vs. Validation

Evaluation asks:

> What bounded conclusion does the eligible governed basis support?

Validation asks:

> Does this object satisfy the normative requirements applicable to it?

`Validation ≠ Evaluation`

`Validation Result ≠ Evaluation Outcome`

Validation may test that required evaluation context exists and is internally coherent without rerunning the substantive evaluation.

## Eligibility vs. Validation

Eligibility is an evaluation-specific admission determination.

Validation may test required representation and rule compliance surrounding that determination.

`Validation ≠ Eligibility`

## Validation Failure

A failure means an applicable normative requirement was not satisfied.

Failures should identify:

- the applicable requirement;
- the failed test;
- the affected object/context; and
- enough reason to support correction.

`Validation Failure ≠ Assertion Proven False`

## Validation and Correction

A validation failure may trigger correction review.

A bounded defect may be corrected within the same canonical identity where Versioning permits.

An identity-changing correction may require:

`New Canonical Object → supersedes → Prior Object`

Validation does not override Versioning.

## Validation vs. Conformance

Validation asks whether a particular object satisfies applicable normative checks.

Conformance asks whether an object, implementation, producer, or process meets its declared Attestor specification/profile requirements.

`Validation supports Conformance`

`Validation ≠ Conformance`

## Validation vs. Publication

`Valid ≠ Published`

`Published ≠ Automatically Valid`

Publication is a separate governed public-representation decision.

## Deferred Machine Specification

This architecture intentionally does not yet freeze:

- final required/optional fields;
- field cardinalities;
- regex patterns;
- exact version syntax;
- final validation-result vocabulary;
- error codes;
- executable validation sequence; or
- validator report serialization.

Those details depend on normative Attestor Schemas and the later formal validation specification.

## What Validation Does Not Establish

`Valid ≠ True`

`Valid ≠ Authoritative`

`Valid ≠ Eligible`

`Valid ≠ Supported`

`Valid ≠ Published`

`Valid ≠ Conformant by itself`

Validation establishes satisfaction of applicable normative structural and rule requirements.

## Dependency Position

Architectural dependency remains:

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

This page establishes the **conceptual Validation architecture**. Final machine validation remains dependent on advancement of the normative Schemas.

## Status

**Validation → Established conceptually**

- structural validation → required
- semantic validation → required
- rule validation → required
- relationship validation → required
- lifecycle/version validation → required
- validation vs. evaluation → distinguished
- validation vs. conformance → distinguished
- machine rule set → dependent on normative Schemas
- production validation → pending
