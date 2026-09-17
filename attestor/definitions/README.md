# Satoshium Attestor — Definitions

## Page

`/attestor/definitions/`

## Purpose

This page establishes the foundational vocabulary used throughout **Satoshium Attestor**.

The definitions support consistent interpretation of Attestations, Evidence, Trust Statements, provenance, scope, correction, evaluation, and authority boundaries.

They apply within Attestor's institutional scope and do not redefine canonical terminology governed by other Satoshium Suite institutions.

## Governing Principle

> **Reference does not transfer authority.**

Attestor may reference objects and terminology from other Suite institutions, but their canonical definitions, identifiers, schemas, lifecycle rules, and authority remain with their originating institutions.

## Foundational Definitions

### Attestation

A governed, attributable assertion used by Attestor to express a bounded statement about a subject, record, relationship, condition, event, or other trust-relevant matter.

### Evidence

Supporting material or an authoritative reference used by Attestor to evaluate an Attestation and support a Trust Statement.

Evidence retains its own source, provenance, status, relevance, and authority.

### Trust Statement

Attestor's canonical institutional output: a governed, attributable, bounded conclusion produced through Attestor evaluation from eligible inputs while preserving provenance, scope, limitations, status, and authority boundaries.

**Attestor → Trust Statement**

### Trust-Relevant Context

Information or an indicator that may be relevant to evaluating an Attestation or supporting a Trust Statement.

The earlier term **Trust Signal** remains descriptive only. It is not presently established as a separate canonical Attestor object.

This distinction also prevents collision with Beacon's canonical **Discovery Signal / Discovery Metadata** architecture.

### Correction

A governed change addressing an identified error in an Attestor assertion or Trust Statement while preserving the relationship between the prior and corrected state.

The implementation mechanism remains unresolved.

### Provenance

Information sufficient to understand the origin, attribution, custody, relationship, or relevant history of an input, assertion, evaluation, or Attestor output.

Exact provenance fields remain to be established.

### Scope

The defined boundary within which an assertion, evidence relationship, evaluation, or Trust Statement applies.

Scope prevents a bounded conclusion from silently becoming a universal one.

### Authority Boundary

The limit of Attestor's institutional authority in relation to an object, source, assertion, or conclusion.

Referenced objects remain governed by their originating authorities.

## Supporting Terms

Advanced Attestor architecture is expected to require additional terminology, potentially including:

- subject;
- attesting authority;
- source;
- status;
- lifecycle;
- clarification;
- withdrawal;
- supersession;
- versioning;
- eligibility;
- validation;
- evaluation.

This page intentionally does not assign final machine semantics to those terms before their governing architecture is established.

## Suite Vocabulary Boundary

Attestor may reference governed objects such as:

- Certifier Certification Packages;
- Satoshium Registry records;
- Chronicle Entries;
- Anchor Integrity References;
- Beacon Discovery Signals and Discovery Metadata;
- Atlas intelligence;
- Navigator workflow context;
- other eligible governed sources.

Attestor definitions explain how such references participate in Attestor evaluation.

They do not replace the originating institution's definitions or authority.

## Definition Governance

Foundational definitions should provide enough stability for coherent Attestor architecture while allowing refinement during advanced design.

Controlled values, machine vocabulary, schema semantics, and normative validation meanings should be adopted only when the relevant architecture is established.

Conceptually:

`Concept → Definition → Governed Use → Validation`

## Reconciliation Notes

This revision updates the June-era pre-Suite Definitions page.

Major changes include:

- replacing the generic “trust layer” framing with Attestor's institutional role;
- strengthening the definition of Attestation from a generic statement to a governed, attributable, bounded assertion;
- strengthening Evidence to include authoritative references and preserved source authority;
- adding **Trust Statement** as Attestor's canonical output;
- replacing **Trust Signal** as a formally “Defined” term with **Trust-Relevant Context**, while preserving “trust signal” only as descriptive language;
- tightening Correction to apply to governed Attestor changes;
- adding Provenance;
- adding Scope;
- adding Authority Boundary;
- removing the old `Language → Meaning → Understanding → Trust` progression;
- adding explicit Suite vocabulary boundaries;
- deferring advanced machine terminology until the underlying architecture is established.

## Deferred to Advanced Architecture

The following remain intentionally unresolved:

- complete Attestor glossary;
- normative versus informative definitions;
- controlled-value definitions;
- machine vocabulary;
- term identifiers, if needed;
- subject model;
- attesting authority model;
- source model;
- lifecycle vocabulary;
- status vocabulary;
- validation terminology;
- evaluation terminology;
- versioning and supersession semantics;
- schema-level definitions;
- conformance terminology.

## Files

- `index.html` — public Definitions page.
- `README.md` — repository documentation for the Definitions page.
