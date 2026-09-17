# Satoshium Attestor — Provenance

**Path:** `/attestor/provenance/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

The Provenance architecture defines provenance requirements for:

- Attestations;
- material governed inputs;
- evaluation; and
- Trust Statements.

The objective is end-to-end traceability from source or origin through Attestor's governed conclusion.

## Provenance Chain

`Source / Origin → Governed Input → Attestation → Rule-Constrained Evaluation → Trust Statement`

Evaluation must not become a break in lineage.

## Attestation Provenance

An Attestation must preserve enough provenance to identify:

- where its assertion originated;
- who or what stands behind it;
- how it entered Attestor;
- which governed references materially support it;
- relevant time/state; and
- material limitations.

Provenance remains distinct from the assertion itself.

## Input Provenance

Every material input used in evaluation must remain traceable to its source or derivation path.

Conceptually, provenance must be capable of preserving:

- source/origin identity;
- source identifier or stable reference, when available;
- provenance mode;
- authority context;
- relevant time/state;
- acquisition or reference context;
- relationship to the Attestation/evaluation;
- derivation basis, when applicable;
- material limitations; and
- historical lineage, when applicable.

Exact machine fields remain a Schema concern.

## Controlled Provenance Modes

The Controlled Values architecture established three modes:

### `direct`

The input is obtained or resolved directly from the authoritative or originating source context being referenced.

Direct provenance describes the acquisition path. It does not automatically establish correctness, sufficiency, or eligibility.

### `referenced`

The Attestor object connects to an existing governed source through an explicit reference rather than taking ownership of or reproducing the source object as an Attestor object.

### `derived`

The input, assertion, or evaluation element is produced from one or more prior governed inputs.

The material derivation path must remain traceable.

## Evaluation Provenance

Attestor must preserve enough evaluation provenance to identify:

- the Attestation evaluated;
- material eligible inputs considered;
- applicable rules or methodology;
- material conflicts or exclusions where relevant; and
- the governed basis for the conclusion.

`Trust Statement → Evaluation Basis → Attestation + Material Inputs → Source / Origin`

## Trust Statement Provenance

A Trust Statement must remain traceable to:

- its supporting Attestation(s);
- eligible governed inputs;
- evaluation basis; and
- Attestor process that produced it.

Publication and later lifecycle changes must not sever this provenance chain.

## Source State at Evaluation

A source object may change after an Attestor evaluation.

Attestor therefore preserves enough context to distinguish:

- source state at evaluation;
- later source state; and
- the historical basis of the Trust Statement.

A later source representation must not silently replace the basis on which an earlier Trust Statement was produced.

## Provenance vs. Authority

- **Provenance** → where information came from and how it reached Attestor.
- **Authority** → who legitimately stands behind an assertion, object, process, or conclusion.

`Provenance ≠ Authority`

**Reference does not transfer authority.**

## Provenance vs. Eligibility

Traceable provenance supports eligibility determination but does not itself establish eligibility.

`Provenance ≠ Eligibility ≠ Evaluation Outcome`

Eligibility governs whether an input may enter a particular evaluation.

## Provenance vs. Truth

A complete provenance chain establishes traceability, not correctness.

`Traceable ≠ Correct`

`Eligible Input ≠ Automatically Sufficient`

`Complete Provenance ≠ Favorable Trust Statement`

## Historical Preservation

Corrections, supersession, withdrawal, retirement, versioning, and publication changes must preserve historical provenance where material to understanding the governed object or prior conclusion.

Detailed transition behavior belongs to Lifecycle and Versioning.

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Provenance → Established**

- Attestation provenance → required
- material input provenance → required
- evaluation provenance → required
- Trust Statement provenance → required
- provenance modes → `direct`, `referenced`, `derived`
- historical lineage → preserved where material
- machine representation → deferred to Schemas
- production proof → pending
