# Satoshium Attestor — Interoperability

## Page

`/attestor/interoperability/`

## Purpose

This page establishes the foundational interoperability principles for **Satoshium Attestor**.

Attestor must be able to reference and exchange governed information across the Satoshium Suite while preserving the meaning, provenance, scope, identifiers, relationships, status, and authority of the objects involved.

Interoperability does not collapse institutional boundaries.

## Governing Principle

> **Reference does not transfer authority.**

A referenced object remains governed by the institution or authority that produced it.

Attestor governs only its own use of that reference and the Attestation, evaluation, or Trust Statement it produces.

## Canonical Responsibility

**Attestor → Trust Statement**

Interoperability exists to support Attestor's ability to produce governed Trust Statements from eligible inputs without absorbing the canonical responsibilities of source institutions.

## Suite Relationships

### Atlas

**Atlas → Authoritative Intelligence**

Attestor may reference authoritative Atlas intelligence.

Atlas remains authoritative for its intelligence and structural record.

### Navigator

**Navigator → Workflow Definition / Orchestration**

Attestor may participate in workflows defined or orchestrated through Navigator.

Navigator retains workflow responsibility. Attestor retains responsibility for its evaluation and Trust Statement.

### Certifier

**Certifier → Certification Package**

Attestor may reference a Certification Package as an authoritative input.

The certification remains governed by Certifier.

### Registry

**Registry → Satoshium Registry Record**

Attestor may reference Registry records and governed relationships.

Registry retains authority over its record identifiers, status, and lifecycle.

### Chronicle

**Chronicle → Chronicle Entry**

Attestor may reference Chronicle Entries for historical, event, or provenance context.

Chronicle retains authority over the preserved historical entry.

### Anchor

**Anchor → Integrity Reference**

Attestor may reference Anchor Integrity References.

Anchor retains authority over its integrity model and canonical reference.

### Beacon

**Beacon → Discovery Signal / Discovery Metadata**

Attestor may reference Beacon Discovery Signals or Discovery Metadata.

Beacon retains authority over its discovery objects and lifecycle.

### Attestor

**Attestor → Trust Statement**

Attestor retains authority over its own Attestations, evaluations, lifecycle operations, and Trust Statements as defined by Attestor architecture.

## What Must Travel With a Reference

The June-era page correctly emphasized preserving context across systems.

This reconciliation makes that requirement more precise.

A usable interoperable reference may need to preserve, as applicable:

- identifier;
- source;
- provenance;
- object type;
- status;
- scope;
- relationship to the Attestor evaluation;
- source authority;
- version or state;
- relevant limitations.

Conceptually:

`Identifier + Source + Provenance + Type + Status + Scope + Relationship + Authority`

This is a foundational information requirement, not yet a final schema.

## Reference Rather Than Duplicate

Where a governed Suite object already exists, Attestor should normally reference the authoritative object rather than silently duplicate it as an Attestor-owned record.

Attestor may preserve enough information to:

- resolve the reference;
- validate its eligibility;
- understand its provenance;
- evaluate its relevance;
- preserve the state considered during evaluation;
- trace the resulting Trust Statement.

The source object remains authoritative in its originating institution.

Conceptually:

`Source Object → Governed Reference → Attestor Evaluation → Trust Statement`

## Source Changes

Interoperability must account for change.

A referenced source object may later:

- change status;
- be corrected;
- be superseded;
- change version;
- change publication state;
- be withdrawn;
- otherwise change under its governing institution.

Attestor should be able to distinguish the source state used during its original evaluation from later source changes.

Depending upon Attestor rules, a material source change may trigger review of Attestor's own object.

Possible Attestor responses may eventually include:

- no change;
- clarification;
- correction;
- withdrawal;
- supersession;
- new evaluation.

The exact trigger and response rules remain unresolved.

## External Interoperability

Attestor may eventually accept eligible governed information from external systems, authorities, protocols, platforms, or repositories.

This page does not adopt external interoperability standards.

Advanced architecture must establish requirements for matters such as:

- eligibility;
- source authority;
- provenance;
- identity of the source;
- object resolution;
- status;
- scope;
- validation;
- versioning;
- persistence;
- limitations;
- permitted use.

External interoperability does not transfer external authority to Attestor.

## Correction of Pre-Suite Architecture

The June page contained several mappings that are no longer carried forward:

- `Anchor → Identity`
- `Certifier → Verification`
- `Registry → Records`
- `Chronicle → History`
- `Beacon → Discovery`
- `Atlas → Data`
- `Navigator → Query`
- `Attestor → Trust`

The reconciled institutional mapping is:

`Atlas → Authoritative Intelligence`
`Navigator → Workflow Definition / Orchestration`
`Certifier → Certification Package`
`Registry → Satoshium Registry Record`
`Chronicle → Chronicle Entry`
`Anchor → Integrity Reference`
`Beacon → Discovery Signal / Discovery Metadata`
`Attestor → Trust Statement`

## Trust Signals and Reputation

The June page described verification records, Registry records, and Chronicle information as contributing to Trust Signals and reputation development.

Those claims are not carried forward as established architecture.

The reconciled Attestor model does not presently establish:

- Trust Signal as a separate canonical Attestor object;
- reputation as an Attestor canonical object;
- a reputation system;
- automatic transformation of source objects into trust conclusions.

Governed inputs participate in Attestor evaluation according to Attestor rules.

## Interoperability vs Integration

This page establishes **what must remain true when information crosses institutional boundaries**.

The separate `/attestor/integration/` page should address **how Attestor participates operationally with those institutions and systems**.

This distinction should be preserved during the next reconciliation:

- **Interoperability** → semantic and authority-preserving compatibility.
- **Integration** → operational connection and exchange.

The exact technical protocols remain advanced architecture.

## Reconciliation Notes

Major changes include:

- replacing generic “trust information portability” with authority-preserving interoperability;
- correcting all pre-Suite institutional mappings;
- adding Atlas and Navigator as explicit Attestor interoperability relationships;
- replacing the old Anchor identity relationship with Anchor Integrity Reference;
- replacing Certifier verification language with Certification Package;
- replacing generic Beacon discovery language with Discovery Signal / Discovery Metadata;
- removing reputation development as an assumed Attestor concern;
- removing Trust Signals as an assumed interoperable Attestor object;
- adding explicit reference requirements for provenance, scope, status, relationships, and authority;
- establishing a reference-rather-than-duplicate principle;
- adding treatment for changes to referenced source objects;
- preserving external interoperability as possible but unresolved;
- distinguishing interoperability from integration.

## Deferred to Advanced Architecture

The following remain intentionally unresolved:

- interoperable reference schema;
- required reference fields;
- canonical relationship types;
- object-resolution rules;
- source-state snapshots or equivalent mechanism;
- version handling;
- status synchronization;
- change-detection rules;
- material-change triggers;
- external-source eligibility;
- external authority representation;
- protocol formats;
- API requirements;
- transport mechanisms;
- validation rules;
- conformance tests;
- reference vectors.

## Files

- `index.html` — public Interoperability page.
- `README.md` — repository documentation for the Interoperability page.
