# Satoshium Beacon — Versioning & Supersession

## Overview

The **Beacon Versioning & Supersession** architecture defines how Satoshium Beacon preserves canonical identity, historical discovery state, and current institutional meaning when Discovery Signals change over time.

Discovery is inherently temporal.

A source may change. An authoritative object may change status. Beacon may discover new information. A relationship may change. A previously published signal may become obsolete.

Beacon must be able to represent those changes without rewriting what was previously observed.

The governing principle is:

> **Discovery changes. History must not.**

A complementary operational rule is:

> **Preserve the observation. Preserve the change. Preserve which representation is current.**

---

# Purpose

Versioning & Supersession answers:

```text
When does a Discovery Signal need a new version?

When should a signal be superseded?

When should a new BEAC object be created instead?

What happens when a source changes?

What happens when authoritative status changes?

What happens when a published signal becomes obsolete?

How does Beacon preserve historical institutional state?
```

---

# Temporal Principle

Beacon records discovery at a point in time.

A later observation may change Beacon's current understanding without invalidating the historical fact that the earlier observation occurred.

Therefore:

```text
What Beacon observed then
≠
What Beacon observes now
```

Both may be institutionally important.

Beacon must preserve the distinction.

---

# Canonical Identity and Version Are Separate

Beacon's canonical identifier identifies the Discovery Signal.

Example:

```text
BEAC-2026-0001
```

Version identifies a governed representation of that same canonical signal.

Conceptually:

```text
Canonical Identifier
→ BEAC-2026-0001

Version
→ governed revision of BEAC-2026-0001
```

The BEAC identifier remains stable across revisions of the same Discovery Signal.

Version information must not replace or be embedded into the canonical identifier.

---

# New Version

A new version is appropriate when the canonical Discovery Signal remains the same institutional object but its representation changes materially.

Examples may include:

```text
Discovery Metadata materially corrected or expanded

Provenance materially corrected or expanded

Canonical reference corrected

Relationship representation changed

Discovery assertion materially corrected

Later observation updates current context without creating a distinct discovery subject

Source context materially changes while the same discovery remains under review
```

The key question is:

> **Is this still the same canonical discovery?**

If yes, a new version may be appropriate.

---

# New Discovery Signal

A new BEAC identifier is appropriate when the later discovery is institutionally distinct rather than merely a revision of the earlier Discovery Signal.

Examples may include:

```text
new discovery subject

new independent occurrence

materially different discovered relationship

distinct observation that should stand as its own canonical record

different institutional discovery requiring its own lifecycle

separate discovery that should remain independently reviewable
```

Conceptually:

```text
Same discovery
→ new version may be appropriate

Distinct discovery
→ new BEAC object
```

---

# Versioning Decision

A conceptual decision model is:

```text
Same canonical discovery subject?
        ↓ yes

Does the change materially alter
the Beacon representation?
        ↓ yes

New Version
```

Alternatively:

```text
Distinct discovery subject
or independently meaningful discovery?
        ↓ yes

New Discovery Signal
New BEAC Identifier
```

The later Beacon Discovery Methodology will define the operational review used to make this determination.

---

# Minor Changes

Not every change should create a new institutional version.

Potential non-material changes include:

```text
formatting corrections

presentation-only changes

accessibility improvements that do not alter meaning

technical corrections outside canonical content

other non-substantive editorial changes
```

Exact materiality thresholds remain subject to Methodology and production proof.

---

# Material Changes

A material change affects the institutional meaning, evidence, interpretation, or reviewability of a Discovery Signal.

Examples include:

```text
changed discovery assertion

changed provenance basis

changed canonical reference

changed relationship meaning

changed source context

material correction

material update to current discovery state
```

Material institutional content should not be silently overwritten.

---

# Conceptual Version Chain

A Beacon signal may progress through multiple governed representations.

Conceptually:

```text
BEAC-2026-0001 · Version 1
        ↓ revised by

BEAC-2026-0001 · Version 2
        ↓ revised by

BEAC-2026-0001 · Version 3
```

The canonical identity remains:

```text
BEAC-2026-0001
```

Earlier versions remain part of the institutional history.

Version 3 becoming current does not erase Versions 1 or 2.

---

# Current Version

Beacon should identify which version currently represents the canonical Discovery Signal.

Therefore:

```text
Canonical Identity
→ stable

Current Version
→ may change
```

The current version is the representation Beacon presently treats as governing for that canonical Discovery Signal.

---

# Historical Versions

Earlier versions should remain traceable.

Where applicable, historical versions should preserve:

```text
prior content

prior Discovery Metadata

prior provenance

prior references

prior relationships

prior lifecycle context

timestamps

relationship to later versions
```

The governing distinction is:

> **Current does not mean only. Historical does not mean deleted.**

---

# Supersession

Supersession is used when an earlier signal or version should no longer be treated as the current representation and a later representation replaces it for current use.

Conceptually:

```text
Earlier Signal / Version
        ↓
superseded by
        ↓
Later Signal / Version
```

Supersession preserves the earlier institutional record while clearly identifying the representation that should now be used.

---

# Version Supersession

A later version may supersede an earlier version under the same BEAC identifier.

Example:

```text
BEAC-2026-0001 v1
        ↓
superseded by
        ↓
BEAC-2026-0001 v2
```

This represents revision of the same canonical Discovery Signal.

---

# Signal Supersession

A distinct Discovery Signal may supersede an earlier Discovery Signal when the later discovery is institutionally separate but replaces the earlier signal for current discovery use.

Example:

```text
BEAC-2026-0001
        ↓
superseded by
        ↓
BEAC-2026-0002
```

The two BEAC identifiers remain distinct.

The supersession relationship explains their current institutional relationship.

---

# Lifecycle and Supersession

**Superseded** is already a canonical Beacon lifecycle state.

The canonical lifecycle architecture includes:

```text
Draft
→ Active
→ Superseded / Resolved / Withdrawn
```

When a signal enters:

```text
Superseded
```

Beacon should identify the governed replacement when one exists.

The replacement may be:

```text
a later version of the same BEAC identity

or

a distinct BEAC Discovery Signal
```

depending on the nature of the change.

---

# Resolved vs. Superseded

These lifecycle outcomes are not interchangeable.

## Resolved

```text
The discovery condition has reached a governed conclusion
or no longer requires active discovery treatment.
```

## Superseded

```text
A later representation replaces the earlier representation for current use.
```

Therefore:

```text
Resolved
≠
Superseded
```

---

# Withdrawn vs. Superseded

Withdrawal also differs from supersession.

## Withdrawn

```text
Beacon removes its own signal from active institutional standing
for a governed reason.
```

## Superseded

```text
Another governed representation replaces it.
```

Withdrawal does not necessarily imply that a replacement exists.

---

# When a Source Changes

A source change creates a later observation.

It does not rewrite the earlier observation.

Conceptually:

```text
Source State A
        ↓
observed at Time 1
        ↓
Beacon historical observation preserved
```

Later:

```text
Source State B
        ↓
observed at Time 2
        ↓
Beacon records later observation
```

Beacon then determines whether the later observation requires:

```text
re-observation metadata

new version

new Discovery Signal

supersession

resolution

withdrawal
```

---

# Source Content Changes

If source content materially changes, Beacon should preserve the original observation and evaluate the later state separately.

The later observation may result in:

```text
updated Discovery Metadata

updated provenance

new version

new Discovery Signal

supersession

resolution
```

The earlier observation must not be rewritten as though the later source state had always existed.

---

# Source Availability Changes

A source may:

```text
move

become temporarily unavailable

become permanently unavailable

change location

be replaced

be superseded
```

Beacon should not silently delete the historical reference.

Where possible, Beacon should preserve:

```text
original source identity

original source location

original provenance

original observation

later availability condition

replacement location when attributable
```

A material change may require a new version.

---

# When Authoritative Status Changes

A referenced Suite institution may change:

```text
lifecycle

status

version

standing

publication state

other institution-owned state
```

of its own canonical object.

Conceptually:

```text
Source Institution
→ changes its own object

Beacon
→ later observes that source-owned change

Beacon
→ determines whether its own Discovery Signal requires revision
```

Beacon does not perform the source institution's status change.

Beacon records its own later observation of that change.

---

# Authority Boundary

Versioning does not transfer authority.

Beacon versions:

```text
Beacon Discovery Signals
```

Source institutions version or modify:

```text
their own canonical objects
```

Therefore:

```text
Beacon version
≠
source-object version
```

A Beacon signal may preserve source-native version information.

That does not make Beacon the authority over the source version.

---

# Reference Does Not Transfer Authority

If a source object's authoritative status changes, Beacon may update the attributed source status it observed.

The distinction remains:

```text
Beacon reports the change.

Beacon does not own the change.
```

This continues the governing Authority & Reference Model.

---

# Obsolete Published Signals

Publication does not freeze a Discovery Signal forever.

A published signal may later become obsolete.

Beacon should preserve:

```text
the historically published representation

the reason it is no longer current

the later version or signal when applicable

the supersession, resolution, or withdrawal relationship

relevant timestamps

supporting provenance
```

The governing rule is:

> **Obsolete does not mean erased.**

---

# Publication State and Lifecycle State

Publication State and Lifecycle State remain separate dimensions.

For example:

```text
Publication State
→ Published

Lifecycle State
→ Superseded
```

This is valid.

A historically published Discovery Signal may remain publicly reviewable while clearly marked as Superseded.

Similarly:

```text
Publication State
→ Published

Lifecycle State
→ Resolved
```

may also be valid.

Publication does not require perpetual Active status.

---

# No Silent Overwrite

Material institutional content should never be silently replaced in place.

Instead:

```text
Preserve prior representation
+
record the change
+
preserve the reason
+
identify the current representation
=
reviewable institutional history
```

Silent overwrite would destroy temporal evidence that Beacon is specifically designed to preserve.

---

# Correction

A **Correction** addresses an error in Beacon's own representation.

Conceptually:

```text
Error discovered
        ↓
Correction documented
        ↓
New version when material
```

Examples may include:

```text
incorrect reference

incorrect attribution

incorrect Discovery Metadata

incorrect relationship representation

incorrect provenance information
```

---

# Update

An **Update** reflects later information or observation rather than merely correcting an earlier Beacon error.

Conceptually:

```text
Earlier observation
→ remains historically preserved

Later information
→ changes current discovery context
```

Therefore:

```text
Correction
≠
Update
```

The distinction matters because one repairs Beacon's prior representation while the other reflects temporal change in the discovered environment.

---

# Reason for Change

Material revisions and supersession should preserve why the change occurred.

Potential architectural change reasons include:

```text
Correction

Source Update

Source Status Change

New Observation

Relationship Change

Provenance Correction

Superseding Discovery

Resolution

Withdrawal
```

The final controlled change-reason vocabulary remains unfrozen.

---

# Version Timestamps

Version history should preserve meaningful temporal distinctions.

Potential timestamps include:

```text
version created time

observation time supporting the change

effective/current time when required

publication time

supersession time
```

These timestamps must not be silently treated as interchangeable.

---

# Provenance Continuity

A new version should preserve the provenance supporting the earlier representation and separately identify provenance supporting the change.

Conceptually:

```text
Original Representation
→ Original Provenance

Changed Representation
→ New Supporting Provenance

Transition
→ Change Reason + Temporal Record
```

The governing principle is:

```text
Old basis remains reviewable.

New basis becomes reviewable.

The transition remains reviewable.
```

---

# Relationship Continuity

Relationships may also change over time.

Conceptually:

```text
Relationship at Time 1
        ↓
changed observation
        ↓
Relationship at Time 2
```

Beacon must not rewrite:

```text
Time 1
```

as though:

```text
Time 2
```

had always been true.

Earlier relationship representations should remain historically traceable.

---

# Version Validation

A material new version should pass applicable Beacon Validation before becoming the current Active representation.

Conceptually:

```text
Revised Draft
        ↓
Validation
        ↓
Current Active Version
```

Validation establishes conformance.

It does not erase the earlier version.

---

# Supersession Validation

A supersession should preserve enough information to review the transition.

This should include, when applicable:

```text
earlier object or version

superseding object or version

reason for supersession

effective transition time

supporting provenance

relationship between the two representations
```

---

# Conceptual Version Structure

A conceptual version representation is:

```yaml
version:
  canonical_identifier: ""
  version: ""
  previous_version: ""
  change_reason: ""
  change_summary: ""
  supporting_provenance: {}
  created_at: ""
  current: true
```

This is architectural only.

Exact machine-readable property names and version notation remain unfrozen.

---

# Conceptual Supersession Structure

A conceptual supersession representation is:

```yaml
supersession:
  superseded_object: {}
  superseding_object: {}
  reason: ""
  effective_at: ""
  provenance: {}
```

Supersession may operate:

```text
between versions of one BEAC identity
```

or:

```text
between distinct BEAC Discovery Signals
```

depending on the institutional nature of the change.

---

# Relationship to Lifecycle

Version and Lifecycle answer different questions.

```text
Version
→ Which governed representation of this canonical signal?

Lifecycle
→ What institutional state is the signal in?
```

For example:

```text
BEAC-2026-0001
Version 3
Lifecycle → Active
```

or:

```text
BEAC-2026-0001
Version 2
Lifecycle → Superseded
```

These concepts should remain separate.

---

# Relationship to Publication

Versioning preserves institutional history.

Publication governs public exposure.

Conceptually:

```text
Versioning
→ preserves representations and transitions

Publication
→ determines what is publicly released and how historical representations remain visible
```

The next Phase II architecture will formalize Publication.

---

# Relationship to Provenance

Provenance explains:

```text
what supported the original observation

what supported the later observation

what supported the correction or change
```

Versioning must preserve that continuity.

---

# Relationship to Authority

Beacon versions only its own canonical Discovery Signals.

Source institutions retain authority over:

```text
their own canonical objects

their own lifecycle changes

their own versions

their own authoritative status
```

Beacon may observe and attribute those changes.

It does not own them.

---

# Relationship to Relationships

The Relationship Model established governed connections between independently owned endpoints.

Versioning preserves how those relationship representations change over time.

A relationship may be:

```text
added

corrected

removed from the current representation

superseded

reinterpreted based on later evidence
```

Historical relationship state should remain traceable.

---

# Relationship to Schemas

Beacon schemas will eventually represent:

```text
canonical identifier

version

previous version

change reason

change summary

current-version status

supersession relationships

supporting provenance
```

Exact machine-readable structures remain pending production implementation.

---

# Relationship to Methodology

Versioning & Supersession defines the institutional rules.

Beacon Discovery Methodology will define how Beacon operationally determines:

```text
whether a change is material

whether a new version is required

whether a new BEAC object is required

whether supersession is appropriate

whether resolution is appropriate

whether withdrawal is appropriate

how corrections are reviewed

how later observations are incorporated
```

---

# What Is Now Established

The following architectural decisions are established:

```text
Canonical BEAC identity and version are separate.

The BEAC identifier remains stable across revisions of the same signal.

Material changes require reviewable version treatment.

Distinct discoveries require new BEAC objects rather than identifier reuse.

Earlier versions remain traceable.

Beacon should identify the current version.

Current does not mean only.

Historical does not mean deleted.

Supersession preserves rather than erases earlier institutional state.

Supersession may occur between versions or distinct signals.

Superseded is a canonical Beacon lifecycle state.

Resolved and Superseded are distinct.

Withdrawn and Superseded are distinct.

Source changes create later observations.

Later source states do not rewrite earlier observations.

Source-owned status changes remain source-owned and attributed.

Beacon versions only its own Discovery Signals.

Published signals may later become Superseded, Resolved, or Withdrawn.

Publication State and Lifecycle State remain separate.

Material institutional content must not be silently overwritten.

Corrections and later updates are conceptually distinct.

Material changes should preserve reason, timestamps, provenance, and continuity.

Historical relationship representations should remain traceable.
```

---

# What Remains Unfrozen

The following implementation details remain pending:

```text
exact version notation

machine-readable version property names

materiality threshold for mandatory new versions

controlled change-reason vocabulary

whether minor editorial revisions receive technical revision tracking

formal current-version pointer mechanics

version publication rules

correction notice format

supersession effective-time rules

whether some changes mandate a new BEAC identifier by Signal Type

machine-readable supersession mechanics
```

These should be resolved through:

```text
Publication Model

Beacon Discovery Methodology

first production operation

production evidence
```

rather than frozen prematurely.

---

# Governing Rules

Beacon Versioning & Supersession follows these rules:

```text
Preserve canonical identity.

Preserve every material representation.

Preserve what Beacon observed at each relevant time.

Preserve why the representation changed.

Preserve provenance supporting the change.

Preserve relationships across the transition.

Identify which representation is current.

Never silently rewrite institutional history.
```

The governing reflection is:

> **Discovery changes. History must not.**

---

# Current Status

As of September 5, 2026:

```text
Institution → Beacon
Suite Role → Discovery & Signals
Canonical Responsibility → Discovery Signal / Metadata
Status → Continuing Development
Phase → Phase II — Production Architecture

Discovery Signal Entry Model → Defined
Discovery Signal Types → Defined
Discovery Signal Lifecycle → Defined
Beacon Identifier Standard → Defined
Beacon Schemas → Defined
Beacon Validation → Defined
Discovery Provenance → Defined
Authority & Reference Model → Defined
Relationship Model → Defined
Versioning & Supersession → Defined

Publication Model → Next
First Production Discovery Signal → Not yet created
Production Proof → Pending
Operational → No
```

---

# Phase II Progress

```text
1. Discovery Signal Entry Model
   → COMPLETE

2. Discovery Signal Types
   → COMPLETE

3. Discovery Signal Lifecycle
   → COMPLETE

4. Beacon Identifier Standard
   → COMPLETE

5. Beacon Schemas
   → COMPLETE

6. Validation
   → COMPLETE

7. Discovery Provenance
   → COMPLETE

8. Authority & Reference Model
   → COMPLETE

9. Relationship Model
   → COMPLETE

10. Versioning & Supersession
    → COMPLETE

11. Publication Model
    → NEXT

12. Discovery Signals Register

13. Individual Discovery Signal

14. Beacon Discovery Methodology

15. Production Model / First Operation
```

---

# Next Phase II Step

The next production-architecture page is:

```text
/beacon/publication/
```

The **Publication Model** will define when a validated Discovery Signal becomes publicly available, what representation is published, how publication state differs from lifecycle state, how superseded and historical signals remain visible, and what restrictions may prevent otherwise valid discovery information from being publicly released.

---

## Last Updated

September 5, 2026
