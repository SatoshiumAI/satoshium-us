# Satoshium Attestor — Versioning

**Path:** `/attestor/versioning/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

Versioning defines governed:

- change;
- revision;
- supersession;
- historical preservation; and
- version identity.

Its central responsibility is distinguishing a new governed state of the **same canonical object** from a substantive change requiring a **new canonical object**.

## Governing Principle

**Revise the same object when its essential institutional meaning remains intact. Create a new canonical object when that meaning materially changes.**

## Canonical Object vs. Version

Canonical identity answers:

> Which governed object is this?

Version identity answers:

> Which governed state of that object is this?

Attestation identity:

`ATT-YYYY-NNNN`

Trust Statement identity:

`TRST-YYYY-NNNN`

A permitted revision preserves the canonical identifier while creating a distinguishable governed version.

`Version ≠ New Canonical Object`

Exact machine syntax for version labels remains deferred to Schemas.

## Same-Object Revision

A change may remain within the same canonical identity when essential institutional meaning is preserved.

Examples generally compatible with bounded revision include:

- editorial correction;
- formatting repair;
- non-substantive metadata correction;
- broken/improved reference resolution;
- clarification that does not alter meaning;
- additional provenance detail that does not change the underlying basis; and
- administrative lifecycle metadata.

## New-Object Boundary

A new canonical object is normally required when a change materially alters:

- subject;
- Attestation assertion;
- controlling scope;
- evaluation basis in a way that materially changes the conclusion;
- Trust Statement conclusion; or
- the institutional meaning represented by the prior object.

`Changed Essential Meaning → New Canonical Object → supersedes → Prior Object`

## Attestation Versioning

A bounded correction or clarification may preserve the same `ATT` identifier.

A material change to the governed assertion requires a new Attestation.

`ATT + Bounded Revision → Same ATT / New Version`

`ATT + Material Assertion Change → New ATT`

## Trust Statement Versioning

A bounded correction that preserves the substantive conclusion and scope may preserve the same `TRST` identifier.

A materially different conclusion requires a new Trust Statement.

`TRST + Bounded Revision → Same TRST / New Version`

`TRST + Material Conclusion Change → New TRST`

**A changed conclusion is a changed canonical statement.**

## Evaluation-Basis Changes

New evidence or changed source state triggers review rather than automatic versioning.

`Material New Input / Source Change → Review`

If the conclusion remains substantively unchanged:

- preserve the current Trust Statement; or
- create a bounded revision if needed.

If the conclusion materially changes:

- create a new Trust Statement; and
- relate it to the prior Trust Statement through `supersedes`.

## Correction vs. Versioning

Correction explains **why** governed change occurs.

Versioning determines **how identity behaves** across that change.

`Correction ≠ Version`

A correction may:

- produce a new version of the same object; or
- require a new canonical successor object.

## Version History

Governed version history must be capable of preserving:

- canonical identifier;
- version identity;
- prior-version reference where applicable;
- change time;
- change type/reason where material;
- responsible Attestor context;
- provenance of change;
- material change summary;
- lifecycle state; and
- current/historical distinction.

Exact representation belongs to Schemas.

## No Silent Overwrite

Material governed history must not be silently overwritten.

`Update ≠ Erasure`

`Current ≠ Only state that ever existed`

Prior governed versions remain distinguishable where material to interpretation, provenance, evaluation, or institutional history.

## Versioning vs. Lifecycle

Versioning governs revisions of the same canonical object.

Lifecycle governs institutional status.

`New Version ≠ Automatic Lifecycle Transition`

`Lifecycle Transition ≠ Automatic New Canonical Object`

Supersession connects a new canonical object to the prior object.

## Versioning vs. Publication

Publication identifies which governed version is publicly represented.

`Publication ≠ Version Identity`

Publishing a newer version does not erase earlier governed versions.

Detailed current/historical publication behavior belongs to Publication architecture.

## What Versioning Does Not Establish

`New Version ≠ Active`

`New Version ≠ Published`

`New Version ≠ Supported`

`Higher Version ≠ More Authoritative`

`Latest Version ≠ Universal Truth`

`Version Identity ≠ Canonical Object Identity`

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Versioning → Established**

- canonical object vs. version identity → distinguished
- same-object revision boundary → established conceptually
- new-object boundary → established conceptually
- material assertion change → new Attestation
- material conclusion change → new Trust Statement
- supersession → preserves predecessor relationship
- no silent overwrite → required
- exact version syntax → deferred to Schemas
- machine materiality tests → deferred to Validation / Methodology
- production proof → pending
