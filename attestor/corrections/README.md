# Satoshium Attestor — Corrections

## Page

`/attestor/corrections/`

## Purpose

This page establishes the foundational role of **Corrections** within Satoshium Attestor.

Corrections provide governed mechanisms for addressing errors, clarifications, withdrawals, supersession, and other changes affecting Attestor's own Attestations and Trust Statements.

The correction architecture must preserve both the currently effective state and sufficient provenance to understand what previously existed and why it changed.

## Authority Boundary

> **Attestor corrects Attestor-owned objects.**

Attestor does not correct or rewrite authoritative objects owned by other Suite institutions.

The Suite-wide principle applies:

> **Reference does not transfer authority.**

If a referenced source changes, Attestor may need to reconsider or update its own Attestation or Trust Statement. The originating institution remains responsible for the source object's correction and lifecycle.

## Required Correction Capabilities

The foundational page identifies several capabilities that advanced Attestor architecture must address:

- correction;
- clarification;
- withdrawal;
- supersession;
- provenance of change;
- historical traceability.

These are architectural concerns, not yet final machine values or lifecycle states.

## No Separate Correction Record Yet

The pre-Suite page proposed future **Correction Records**.

This reconciliation does not establish a Correction Record as another canonical Attestor object.

Attestor's canonical responsibility remains:

**Attestor → Trust Statement**

Correction may ultimately be represented through:

- lifecycle state;
- versioning;
- explicit relationships;
- replacement Attestations;
- replacement Trust Statements;
- another governed mechanism demonstrated to be necessary during advanced architecture.

No implementation is adopted here.

## Correction Attestations

The pre-Suite page also proposed **Correction Attestations**.

That mechanism is not adopted at this stage.

The Attestation Types reconciliation already left open whether correction and supersession should be represented as an Attestation Type or through lifecycle/versioning architecture. This page preserves that question rather than resolving it prematurely.

## Current State vs Historical State

A correction system should distinguish:

- the currently effective Attestor state; and
- historically relevant prior states.

A prior Attestation or Trust Statement may remain traceable without remaining current or effective.

Conceptually:

`Prior State → Governed Change → Current State`

Provenance and relationships should remain visible across the transition.

## Provenance of Change

Advanced architecture should preserve enough information to determine, as applicable:

- what changed;
- why it changed;
- who or what authorized the change;
- when the change occurred;
- which Attestor object or version was affected;
- what object or state replaced it;
- the relationship between prior and current states.

The exact required fields remain unresolved.

## Changes in Referenced Sources

If a referenced authoritative source changes, Attestor should not rewrite that source.

Depending on Attestor rules and the significance of the change, Attestor may instead:

- leave the existing Attestation or Trust Statement unchanged if the change is immaterial;
- clarify its own object;
- correct its own object;
- withdraw its own object;
- supersede its own object with a new evaluation.

The exact decision rules are deferred to advanced architecture.

## Historical Traceability

The June-era principle that corrections should improve understanding without erasing history is preserved, but expressed more precisely.

Historical traceability should coexist with a clear current state. Preserving a superseded or withdrawn object does not mean presenting it as currently effective.

Retention, public visibility, and publication behavior remain to be defined.

## Reconciliation Notes

This revision updates the June-era pre-Suite Corrections page.

Major changes include:

- replacing broad trust/accountability language with governed Attestor correction responsibilities;
- limiting Attestor correction authority to Attestor-owned objects;
- removing the assumption that a separate Correction Record will exist;
- removing Correction Attestations as a planned mechanism;
- distinguishing correction, clarification, withdrawal, and supersession as separate architectural concerns;
- adding provenance-of-change requirements;
- distinguishing current state from historical state;
- establishing treatment for changes in referenced authoritative sources;
- replacing `Original Record → Correction → Historical Context → Trust` with a lifecycle-oriented model;
- preserving Attestor's canonical Trust Statement responsibility;
- avoiding premature lifecycle values, version identifiers, schemas, and validation rules.

## Deferred to Advanced Architecture

The following remain intentionally unresolved:

- correction triggers;
- correction authorization;
- whether correction is an Attestation Type;
- whether corrections create replacement Attestations;
- whether corrected Trust Statements are versioned or replaced;
- lifecycle state vocabulary;
- withdrawal semantics;
- supersession semantics;
- versioning model;
- relationship identifiers;
- correction validation rules;
- publication behavior;
- historical retention rules;
- public visibility of prior states;
- correction of unpublished objects;
- handling changes in referenced sources;
- schemas;
- conformance tests and reference vectors.

## Files

- `index.html` — public Corrections page.
- `README.md` — repository documentation for the Corrections page.
