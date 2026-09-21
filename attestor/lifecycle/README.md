# Satoshium Attestor — Lifecycle

**Path:** `/attestor/lifecycle/`  
**Institution:** Satoshium Attestor  
**Current Stage:** Operational Lifecycle  
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

A bounded non-material correction may preserve canonical object identity and version when the applicable Versioning determination permits it.

A material change to an Attestation assertion requires a new `ATT` object. A material change to a Trust Statement conclusion requires a new `TRST` object. Where a successor replaces a prior object as current, the applicable supersession relationship preserves continuity.

Materiality and version consequences must be explicitly governed rather than inferred from the existence of a correction alone.

`Correction ≠ Deletion`

`Correction ≠ Silent Overwrite`

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

## First Production Lifecycle Demonstration

The first controlled production operation exercised canonical Creation and lifecycle activation as separate governed acts.

Both canonical objects began as:

- `ATT-2026-0001` → `Draft · Unpublished · V1.0`
- `TRST-2026-0001` → `Draft · Unpublished · V1.0`

After governed Validation, Review, and Conformance, separate lifecycle activation decisions authorized:

- `ATT-2026-0001` → `draft` → `active`
- `TRST-2026-0001` → `draft` → `active`

At lifecycle activation:

- publication state remained `unpublished`;
- canonical identifiers remained unchanged;
- version remained `V1.0`;
- the Attestation assertion remained unchanged; and
- the Trust Statement conclusion remained unchanged.

Publication was authorized only afterward through separate publication decisions.

The production sequence therefore demonstrated:

`Canonical Creation ≠ Lifecycle Activation ≠ Publication`

**Lifecycle Activation → DEMONSTRATED IN PRODUCTION**

## Production Correction and Historical Preservation

The first production operation also exercised governed correction before final publication.

Early relationship serialization was corrected to structured relationship representation while preserving:

- canonical ATT and TRST identifiers;
- the substantive Attestation assertion;
- the substantive Trust Statement conclusion;
- production history; and
- historical representations.

For this bounded operation, the correction was determined to be non-material to canonical meaning and remained `V1.0`.

Therefore:

`Correction ≠ Deletion`

`Correction ≠ Historical Erasure`

`Correction ≠ Silent Mutation`

This result is not a universal rule that every correction preserves identity or version. Future corrections remain subject to explicit materiality, Versioning, correction, and supersession rules.

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

**Lifecycle → Established and Production-Proven**

- states → `draft`, `active`, `superseded`, `withdrawn`, `retired`
- Canonical Creation → exercised
- initial `draft` state → exercised
- Lifecycle Activation → exercised
- Review → governed lifecycle activity, not state
- Correction → governed change activity, not state
- inactive → descriptive umbrella, not canonical value
- Creation / Activation separation → demonstrated
- Lifecycle / Publication separation → demonstrated
- canonical identity preservation → demonstrated
- historical preservation → demonstrated
- bounded non-material correction → exercised
- supersession / withdrawal / retirement → established but not required by first production operation
- version consequences → governed through Versioning
- production proof → **ESTABLISHED**

## Continuing Lifecycle Governance

The first production operation demonstrates real lifecycle capability without collapsing distinct institutional acts.

It does not establish that:

- every created object will become active;
- every active object will be published;
- every correction is non-material;
- every correction preserves version;
- every correction preserves canonical identity; or
- supersession, withdrawal, and retirement have already been exercised.

Each future lifecycle transition remains a separate governed decision.

`Creation ≠ Activation ≠ Publication`

`Review ≠ Lifecycle State`

`Correction ≠ Lifecycle State`

`State Change ≠ Historical Erasure`
