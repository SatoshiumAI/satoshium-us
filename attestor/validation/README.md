# Satoshium Attestor — Validation

**Path:** `/attestor/validation/`  
**Institution:** Satoshium Attestor  
**Current Stage:** Operational Validation  
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

## Implementation Specifications

The conceptual Validation architecture is now supplemented by implementation specifications maintained in this directory:

- `attestor-validation-requirements.md` — normative bridge from established Attestor architecture to executable validation requirements.
- `attestor-validation-rules.md` — stable numbered `VAL-*` rule catalog separating deterministic machine checks, conditional checks, review-dependent requirements, and deferred implementation requirements.
- `attestor-machine-contract.md` — initial ATT/TRST machine contract defining serialization, base field requirements, deterministic invariants, Validation Result vocabulary, report structure, and base validation profiles.

The Machine Contract v0.1 establishes the initial implementation choices for:

- YAML 1.2-compatible canonical validation serialization;
- UTF-8 encoding;
- ATT/TRST identifier expressions;
- RFC 3339 timestamps;
- initial `V<major>.<minor>` version representation;
- base required and optional/conditional ATT/TRST fields;
- reusable subject, authority, reference, relationship, and provenance structures;
- deterministic ATT/TRST invariants;
- per-rule Validation Results: `pass`, `fail`, `not-applicable`, `not-tested`;
- aggregate Validation Results: `valid`, `invalid`, `incomplete`, `error`; and
- base profiles `attestor.attestation.base` and `attestor.trust-statement.base`.

These are implementation specifications subordinate to established Attestor architecture. They do not redefine institutional meaning.

## Executable Validator

Executable Validation is maintained separately from the durable Validation specifications. The implementation began with Validator v0.1 and progressed through iterative rule-coverage, execution-context, and production-validation work.

The operative production endpoint is **Validator v0.5**.

Validator v0.5 supports:

- target-object validation;
- governed Validation Result reporting;
- registry-aware validation where required;
- execution-context input;
- separation of contextual results from object-local results;
- deterministic and conditional rule execution;
- explicit preservation of genuinely Review-bound requirements; and
- aggregate result determination without treating `not-tested` as `pass`.

Per-rule Validation Results:

- `pass`
- `fail`
- `not-applicable`
- `not-tested`

Aggregate Validation Results:

- `valid`
- `invalid`
- `incomplete`
- `error`

> **NOT-TESTED NEVER EQUALS PASS.**

Review-bound rules may remain `not-tested` when genuinely nonmandatory for the aggregate machine result. Mandatory requirements may not be silently treated as passed when they have not been tested.

Earlier validator versions and fixture executions remain implementation history. Validator v0.5 is the operative production validation path.

## Production Validation Baseline

Validator v0.5 was exercised against the first canonical production Attestation and Trust Statement and their final published representations.

### ATT-2026-0001

Final **Active · Published · V1.0** representation:

- Aggregate Result → **VALID**
- Pass → 68
- Fail → 0
- Not Applicable → 24
- Review-bound Not Tested → 11
- Mandatory Not Tested → 0

### TRST-2026-0001

Final **Active · Published · V1.0** representation:

- Aggregate Result → **VALID**
- Pass → 78
- Fail → 0
- Not Applicable → 16
- Review-bound Not Tested → 14
- Mandatory Not Tested → 0

Both production objects were validated before activation/publication and revalidated after reaching their final **Active · Published · V1.0** state.

## Governed Review Boundary

Machine Validation and governed Review remain distinct.

The first production operation separately completed all Review-bound requirements:

- ATT governed Review → 11 / 11 SATISFIED
- TRST governed Review → 14 / 14 SATISFIED
- Combined → **25 / 25 SATISFIED**

`Validation ≠ Review`

`Not Tested ≠ Pass`

`Valid ≠ Review Automatically Satisfied`

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

The Validation architecture is established and implemented. Canonical Attestation and Trust Statement schemas, Validation Requirements, the numbered `VAL-*` Rule Catalog, machine contracts, executable validator software, execution-context support, and production Validation evidence now exist.

Validator v0.5 has validated the first canonical production Attestation and Trust Statement and their final published representations.

Future objects remain independently subject to the applicable Validation requirements.

## Status

**Validation Architecture → Established**

**Executable Validation → Operational and Exercised in Production**

- structural validation architecture → established
- semantic validation architecture → established
- rule validation architecture → established
- relationship validation architecture → established
- lifecycle/version validation architecture → established
- validation vs. evaluation → distinguished
- validation vs. eligibility → distinguished
- validation vs. conformance → distinguished
- canonical ATT/TRST base schemas → established
- Validation Requirements → established
- numbered `VAL-*` Rule Catalog → established
- machine result vocabulary → established
- Validation Report semantics → established
- executable validator → **v0.5 operative production endpoint**
- execution-context support → established
- contextual vs. object-local result separation → established
- Review-bound `not-tested` handling → established
- `NOT-TESTED ≠ PASS` → enforced
- `ATT-2026-0001` final validation → **VALID**
- `TRST-2026-0001` final validation → **VALID**
- mandatory not-tested → **0 for both final production objects**
- production governed Review → **25 / 25 SATISFIED**
- production Validation evidence → **established**

## Continuing Validation Governance

The first-production Validation baseline demonstrates executable institutional capability.

It does not make future Attestations or Trust Statements automatically valid. Each future object and governed representation must independently satisfy the normative requirements applicable to its object class, profile, state, and context.

> **Validator → implements architecture. Validator → does not create architecture.**
