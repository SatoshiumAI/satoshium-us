# Satoshium Attestor — Publication

**Path:** `/attestor/publication/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

Publication separates canonical creation from the governed decision to make an Attestor object publicly represented.

An Attestation or Trust Statement may exist canonically before publication.

Publication changes public-representation state. It does not create the canonical object.

## Governing Model

`Canonical Object + Governed Publication Decision → Authorized Public Representation`

## Creation, Activation, and Publication

These are distinct institutional events.

### Canonical Creation

Establishes the governed object and assigns its canonical identifier.

### Activation

Establishes the object as the current governed representation within its scope.

### Publication

Authorizes public representation.

`Creation ≠ Activation ≠ Publication`

## Canonical Publication States

The Controlled Values architecture established:

- `unpublished`
- `published`

### `unpublished`

The canonical object is not currently authorized as a public representation.

### `published`

A governed public representation is authorized and exists.

Review, approval, and pending-publication activities are not silently adopted as additional publication states.

## Publication Authorization

Publication requires an affirmative governed decision under applicable Attestor requirements.

Technical accessibility does not itself establish publication.

`Technically Accessible ≠ Published by Governance`

## Publication Eligibility

Applicable publication requirements may include:

- lifecycle requirements;
- validation requirements;
- conformance requirements;
- review/authorization;
- provenance requirements; and
- representation requirements.

Publication does not substitute for these requirements.

## Public Representation Integrity

A published representation must faithfully represent the governed object/version.

Material context should remain preserved or resolvable, including:

- canonical identifier;
- governed version;
- object type;
- lifecycle state where material;
- scope;
- provenance;
- limitations/uncertainty;
- relationships; and
- institutional attribution.

`Presentation ≠ Reinterpretation`

## Version Publication

A public representation must resolve to the governed version being represented.

`Publishing a New Version ≠ Erasing an Old Version`

Historical governed versions remain part of institutional history.

## Lifecycle Changes After Publication

A previously published object may later become:

- `superseded`;
- `withdrawn`; or
- `retired`.

Its public presentation must not continue to imply current active status.

`Published ≠ Active Forever`

## Unpublication and Historical Preservation

Changing current publication authorization must not erase the historical fact of prior publication where that fact is material.

`Unpublication ≠ Deletion`

`Removal from Current Public View ≠ Historical Erasure`

Exact archival, takedown, exceptional removal, and historical-access rules remain to be formalized.

## Publication vs. Validation

Validation establishes satisfaction of applicable normative requirements.

Publication authorizes public representation.

`Valid ≠ Published`

`Published ≠ Automatically Valid`

## Publication vs. Conformance

Conformance establishes satisfaction of a declared specification/profile.

Publication authorizes public representation.

`Conformant ≠ Published`

`Published ≠ Conformant`

## Publication vs. Evaluation Outcome

Publication state does not encode favorability.

A published Trust Statement may carry any legitimate governed Evaluation Outcome:

- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

`Published ≠ Supported`

Publication must not become a hidden trust score.

## Publication and Authority

Publication does not enlarge or transfer authority.

**Reference does not transfer authority.**

Publication does not transfer authority either.

A published Trust Statement remains an Attestor-owned bounded conclusion.

## Deferred Publication Mechanics

This architecture intentionally does not yet freeze:

- exact approval roles;
- publication manifests;
- publication timestamp requirements;
- URI rules;
- archival/takedown procedures;
- publication logs;
- machine publication fields; or
- deployment workflow.

These should be derived from normative Schemas, Validation, Conformance, Templates, and Methodology.

## What Publication Does Not Establish

`Published ≠ Created`

`Published ≠ Active`

`Published ≠ True`

`Published ≠ Supported`

`Published ≠ Valid`

`Published ≠ Conformant`

`Published ≠ More Authoritative`

`Published ≠ Permanently Current`

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Publication → Established conceptually**

- creation vs. activation vs. publication → distinguished
- publication states → `unpublished`, `published`
- affirmative publication authorization → required
- public representation integrity → required
- version-specific representation → required
- historical publication preservation → required
- lifecycle changes after publication → governed
- validation / conformance / evaluation outcome → kept distinct
- operational publication mechanics → deferred
- production publication proof → pending
