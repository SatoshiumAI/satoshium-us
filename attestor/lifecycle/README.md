# Satoshium Attestor — Lifecycle

**Path:** `/attestor/lifecycle/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

Lifecycle defines how Attestor-owned objects move through governed existence:

- preparation;
- canonical Creation;
- review;
- active use;
- correction;
- supersession;
- withdrawal; and
- retirement.

Lifecycle preserves current and historical state without destroying identity, provenance, or lineage.

## Governing Principle

**State may change. Canonical identity and governed history remain traceable.**

## Canonical Lifecycle States

The Controlled Values architecture established:

- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

This page defines their institutional meaning.

### `draft`

A governed pre-active state used while an Attestation or Trust Statement is being prepared, reviewed, or completed.

### `active`

The current governed representation within the object's scope.

Active does not mean published, favorable, permanently correct, or immune from review.

### `superseded`

A newer governed object or version has replaced the prior object as the current representation.

The prior object remains historically identifiable.

### `withdrawn`

Attestor has affirmatively removed the object from current institutional reliance because continued active use is no longer appropriate.

### `retired`

The object has reached terminal non-current disposition through normal lifecycle management rather than necessarily because it was erroneous.

## Creation

Canonical Creation is the point at which an Attestor object becomes institutionally recognized and receives its canonical identifier.

`Preparation → No canonical object`

`Canonical Creation → Identifier assigned`

A created object may begin in `draft`.

`Creation ≠ Activation ≠ Publication`

## Review

Review is a governed lifecycle **activity**, not an initial lifecycle state.

Review may:

- confirm current state;
- cause correction;
- lead to supersession;
- lead to withdrawal;
- lead to retirement; or
- initiate a new evaluation.

Review may be initial, periodic, event-driven, or triggered by material change.

## Active vs. Inactive

`active` is canonical.

**inactive is not adopted as a canonical lifecycle value.**

Instead, inactive is a descriptive umbrella for distinct non-active states:

- `superseded`
- `withdrawn`
- `retired`

This preserves the reason an object is no longer current.

## Correction

Correction is a governed change process, not a lifecycle state.

`Prior State → Governed Change → Current State`

A bounded/non-substantive correction may be handled through versioning while preserving canonical object identity.

A substantive change to assertion, evaluation basis, scope, or conclusion may require a new canonical object that `supersedes` the prior object.

Exact materiality thresholds belong to Versioning.

`Correction ≠ Deletion`

## Supersession

`New Object → supersedes → Prior Object`

The successor may become active while the prior object becomes `superseded`.

Prior identity, provenance, relationships, and history remain preserved.

## Withdrawal vs. Retirement

These states are intentionally distinct.

- `withdrawn` → current reliance is affirmatively ended because continued active use is no longer appropriate.
- `retired` → normal terminal lifecycle disposition.

Neither erases the historical object.

## Lifecycle Triggers

Material triggers may include:

- source-state change;
- new eligible input;
- authority change;
- provenance defect or clarification;
- scope change;
- correction request;
- conflicting or contradictory information;
- evaluation-basis change; or
- applicable methodology/rule change.

A trigger requires review. It does not predetermine the resulting state.

`Trigger → Review, not automatic outcome`

## Lifecycle and Publication

Lifecycle and publication are independent.

Lifecycle:

`draft · active · superseded · withdrawn · retired`

Publication:

`unpublished · published`

Therefore:

`Active ≠ Published`

`Published ≠ Active forever`

A lifecycle transition does not automatically erase publication history.

## Historical Preservation

Lifecycle changes must preserve enough information to reconstruct material state history.

Attestor preserves, as applicable:

- prior state;
- current state;
- governed change;
- canonical identity;
- relationships;
- provenance;
- material reason/trigger; and
- successor relationship.

## What Lifecycle Does Not Establish

`Active ≠ True`

`Active ≠ Supported`

`Active ≠ Published`

`Active ≠ Validated`

`Superseded ≠ False`

`Withdrawn ≠ Historical Erasure`

`Retired ≠ Invalid`

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Lifecycle → Established**

- states → `draft`, `active`, `superseded`, `withdrawn`, `retired`
- Creation → canonical identity assignment
- Review → governed lifecycle activity
- Correction → governed change activity, not state
- inactive → descriptive umbrella, not canonical value
- supersession / withdrawal / retirement → distinguished
- historical preservation → required
- publication state → independent
- detailed version thresholds → deferred to Versioning
- production proof → pending
