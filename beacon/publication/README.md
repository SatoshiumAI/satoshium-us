# Satoshium Beacon — Publication Model

## Overview

The **Beacon Publication Model** defines when a valid Discovery Signal becomes publicly discoverable, what its public representation contains, and how Beacon distinguishes internal identification and review from public release.

Publication is not the act that creates a Discovery Signal.

A Beacon Discovery Signal may exist canonically, pass Validation, and enter an Active lifecycle state while remaining unpublished.

The governing principle is:

> **Publication makes discovery public. It does not make discovery authoritative beyond Beacon's own institutional role.**

A complementary rule is:

> **Discovery can exist before publication. Validation can precede publication. Publication is a governed institutional act.**

---

# Purpose

The Publication Model answers:

```text
When may a Discovery Signal become public?

What must be true before publication?

What does the public representation contain?

What remains internal or restricted?

How are later changes shown publicly?

How does Beacon distinguish identification, creation, validation, lifecycle state, and publication?
```

---

# Core Distinction

Beacon must distinguish the existence of a Discovery Signal from the public release of that signal.

Therefore:

```text
Canonical existence
≠
Validation
≠
Active lifecycle state
≠
Publication
```

These are separate institutional concepts.

---

# Publication State

The Beacon lifecycle architecture established a separate Publication State:

```text
Unpublished
Published
```

Publication State is intentionally separate from Lifecycle State.

---

# Lifecycle State

Canonical Beacon lifecycle states are:

```text
Draft
Active
Superseded
Resolved
Withdrawn
```

Lifecycle answers:

> **What institutional state is the Discovery Signal in?**

Publication answers:

> **Has the governed Beacon representation been publicly released?**

---

# Pre-Publication Sequence

The conceptual production sequence is:

```text
Candidate Discovery Identified
        ↓
Discovery Signal Created
        ↓
BEAC Identifier Assigned
        ↓
Draft / Unpublished
        ↓
Review & Validation
        ↓
Active / Unpublished
        ↓
Publication Decision
        ↓
Active / Published
```

Publication does not create the canonical Discovery Signal.

The signal already exists before public release.

---

# Identification

Identification is a pre-object condition.

Conceptually:

```text
Candidate Discovery Identified
```

At this point:

```text
no canonical Discovery Signal necessarily exists

no BEAC identifier necessarily exists

no public Beacon record exists
```

Identification alone does not create a public record.

---

# Creation

Canonical creation establishes the Discovery Signal.

At creation:

```text
canonical object exists

BEAC identifier is assigned

Lifecycle State → Draft

Publication State → Unpublished
```

Publication occurs later, if appropriate.

---

# Validation

Validation determines whether the Discovery Signal conforms to Beacon production architecture.

Validation evaluates areas including:

```text
identity

identifier

subject

Signal Type

source

provenance

Discovery Metadata

timestamps

status

version

references

relationships

schema conformity
```

A valid signal is eligible for further institutional progression.

However:

```text
Valid
≠
Published
```

---

# Publication

Publication is the governed institutional act that makes an eligible Beacon representation publicly discoverable.

Conceptually:

```text
Eligible Discovery Signal
        ↓
Publication Decision
        ↓
Published Beacon Representation
```

Publication changes:

```text
Publication State
→ Published
```

It does not create a new canonical identity.

---

# Publication Eligibility

A Discovery Signal should be eligible for publication only when:

```text
canonical identity exists

BEAC identifier conforms

required Entry Model components are present

applicable Validation has passed

Lifecycle State permits publication

provenance is sufficient for public review

authority boundaries are preserved

references are sufficiently attributable

relationships are sufficiently attributable

no governing restriction prevents public release
```

Eligibility permits a publication decision.

Eligibility does not itself publish the signal.

---

# Publication Decision

Beacon must make or record a governed publication decision before changing Publication State to:

```text
Published
```

Conceptually:

```text
Eligible
        ↓
Publication Decision
        ↓
Published
```

The exact publication approval role or mechanism remains unfrozen pending Methodology and production operation.

---

# Publication Is Not Validation

Validation and Publication perform different institutional functions.

```text
Validation
→ conformance gate

Publication
→ public-release act
```

A Discovery Signal may therefore be:

```text
Valid
Active
Unpublished
```

without contradiction.

---

# Public Representation

A published Discovery Signal should expose enough canonical information for a reviewer to:

```text
identify the signal

understand the discovery

identify the source

understand attribution

review relevant provenance

follow canonical references

understand applicable relationships

determine current lifecycle state

determine current version

recognize supersession or resolution when applicable
```

The public representation should normally include:

```text
BEAC identifier

signal subject

Signal Type

Lifecycle State

Publication State

current version

discovery summary or represented observation

source identity

reviewable public provenance

canonical references when applicable

relationships when applicable and publishable

relevant timestamps

supersession information when applicable

resolution information when applicable
```

---

# Public Canonical Identity

Publication must preserve the canonical identity assigned when the Discovery Signal was created.

Example:

```text
Internal canonical object
→ BEAC-2026-0001

Public representation
→ BEAC-2026-0001
```

Publication does not create:

```text
a second public identifier

a replacement identifier

a publication-only identity
```

---

# Public Record Path

The Beacon Identifier Standard established the conceptual public path:

```text
/beacon/records/BEAC-2026-0001/
```

This path represents the individual Beacon Discovery Signal.

The later Individual Discovery Signal architecture will define its production representation.

---

# Public Representation Is Not the Source Object

Beacon publishes its own Discovery Signal.

It does not publish a replacement canonical copy of another institution's object.

Conceptually:

```text
Beacon publishes
→ BEAC Discovery Signal

Beacon references
→ source-owned canonical object
```

The Suite-wide governing principle remains:

> **Reference does not transfer authority.**

---

# Source Attribution

Public references should preserve source ownership and native identity.

Example:

```text
Source Institution
→ Certifier

Source Object
→ SC-CERT-2026-0001

Beacon Object
→ BEAC-2026-0001
```

Beacon may expose the relationship.

It must not collapse those identities.

---

# No Authority Elevation

Public visibility does not increase the authority of the underlying source.

Therefore:

```text
Public visibility
≠
Certification

Public visibility
≠
Registration

Public visibility
≠
Historical authority

Public visibility
≠
Integrity verification

Public visibility
≠
Trust
```

Beacon publication establishes only that Beacon has publicly released its own governed Discovery Signal.

---

# Public Provenance

Published Discovery Signals should expose enough provenance for meaningful public review.

Public provenance should help establish:

```text
where Beacon's discovery came from

what Beacon observed

when Beacon observed it

what source supports the discovery

how the source is attributed
```

However, public provenance remains subject to legitimate disclosure restrictions.

---

# Internal Provenance vs. Public Provenance

Beacon may retain institutional provenance that is not appropriate for public release.

Therefore:

```text
Internal Provenance
→ information retained for institutional accountability

Public Provenance
→ information permitted and necessary for public review
```

These may overlap substantially.

They are not required to be identical.

The governing principle is:

> **Internal completeness and public disclosure are related, but not necessarily identical.**

---

# Restricted or Non-Public Information

A valid Discovery Signal may remain Unpublished when legitimate restrictions prevent public release.

Potential restrictions include:

```text
privacy

security

access limitations

source restrictions

institutional governance

insufficient public-review basis

other lawful or governed limitations
```

Therefore:

```text
Valid
≠
Public
```

and:

```text
Discoverable internally
≠
Publishable externally
```

---

# Unpublished Active Signal

Beacon may maintain an institutionally valid Active Discovery Signal that remains Unpublished.

Example:

```text
Lifecycle State
→ Active

Publication State
→ Unpublished
```

This is a valid Beacon state combination.

---

# Published Active Signal

After a governed publication act:

```text
Lifecycle State
→ Active

Publication State
→ Published
```

The Discovery Signal becomes publicly discoverable through Beacon's public representation.

---

# Publication of Versions

Versioning and Publication remain separate but connected.

A published signal may have:

```text
historically published versions

a current published version

superseded versions
```

Conceptually:

```text
BEAC-2026-0001 v1
→ Published historically

        ↓ superseded by

BEAC-2026-0001 v2
→ Current published representation
```

Earlier materially published versions should remain traceable where governance permits.

---

# Published + Superseded

A published Discovery Signal may later become Superseded.

Example:

```text
Lifecycle State
→ Superseded

Publication State
→ Published
```

The historical signal may remain publicly reviewable while clearly marked as no longer current.

---

# Published + Resolved

A published Discovery Signal may remain public after resolution.

Example:

```text
Lifecycle State
→ Resolved

Publication State
→ Published
```

Publication does not require perpetual Active status.

---

# Published + Withdrawn

A published signal may later become Withdrawn.

Withdrawal requires careful handling because the historical fact of prior publication may itself be institutionally relevant.

Beacon should not silently erase prior publication.

Where governance permits, the public record should preserve:

```text
the fact of withdrawal

the governed withdrawal state

the reason for withdrawal

the prior publication history

the relevant timestamps
```

Exact withdrawal-display rules remain unfrozen pending Methodology and production use.

---

# No Silent Unpublication

Once a Discovery Signal has been publicly released, later institutional change should not ordinarily make that historical publication disappear without explanation.

The governing posture is:

```text
Preserve public history
where governance permits.
```

Supersession, resolution, withdrawal, or correction should be represented rather than hidden through silent deletion.

---

# Correction Notice

Material corrections to a published signal should remain reviewable.

Potential mechanisms may include:

```text
version history

correction notice

change summary

supersession relationship

other governed public mechanism
```

The exact public correction format remains unfrozen.

The governing rule is:

> **Correct the record without pretending the earlier record never existed.**

---

# Publication Timestamp

Publication time is distinct from other Beacon timestamps.

Examples:

```text
observed_at
→ when Beacon observed the source

created_at
→ when the Discovery Signal was created

published_at
→ when the Beacon representation became public
```

These timestamps must not be silently substituted for one another.

---

# Public Relationships

Relationships may be publicly represented when:

```text
relationship meaning is governed

endpoints are sufficiently identifiable

attribution is preserved

provenance is sufficient

authority boundaries are preserved

disclosure is permitted
```

Relationship publication does not alter endpoint ownership.

---

# Restricted Relationships

A relationship may remain internally represented even when public disclosure is restricted.

For example:

```text
relationship exists internally

one endpoint is restricted

public disclosure is prohibited
```

Therefore:

```text
Relationship validity
≠
automatic public disclosure
```

---

# Discovery Signals Register

Published Discovery Signals will ultimately be surfaced through:

```text
/beacon/records/
```

The Discovery Signals Register will provide the public register-level view of Beacon's published canonical objects.

Conceptually:

```text
/beacon/records/
→ public register of published Beacon signals
```

Individual records will use paths such as:

```text
/beacon/records/BEAC-2026-0001/
```

The Register and Individual Discovery Signal architectures follow later in Phase II.

---

# Publication and Search

Public Beacon discovery should operate on published Beacon representations rather than exposing internal Draft or restricted records by default.

Conceptually:

```text
Internal Beacon discovery space
→ may include governed non-public information

Public Beacon discovery space
→ exposes Published representations
```

This preserves the publication boundary.

---

# Publication and Indexes

Beacon indexes may expose published Discovery Signals while preserving:

```text
Publication State

Lifecycle State

current version

historical status

supersession state

applicable disclosure restrictions
```

An index must not silently expose internal records merely because Beacon knows they exist.

---

# Conceptual Publication Structure

A conceptual publication representation is:

```yaml
publication:
  state: ""
  published_at: ""
  published_version: ""
  public_record_location: ""
  publication_basis: ""
  restrictions: []
  historical_notice: ""
```

This is architectural only.

Exact machine-readable property names and publication-decision mechanics remain unfrozen.

---

# Minimum Publication Gate

The conceptual minimum Publication Gate is:

```text
Canonical Signal exists
+
Validation passed
+
Lifecycle permits publication
+
Public provenance sufficient
+
Authority boundaries preserved
+
References / relationships publishable
+
No governing restriction prevents release
+
Publication decision made
=
Eligible Published Discovery Signal
```

---

# Relationship to Validation

Validation determines whether a Discovery Signal conforms to Beacon architecture.

Publication determines whether an eligible representation becomes public.

Therefore:

```text
Validation
→ institutional conformance

Publication
→ governed public release
```

Validation does not automatically cause publication.

---

# Relationship to Versioning

Versioning preserves changing representations over time.

Publication records which representation was publicly released and which representation is currently public.

Conceptually:

```text
Versioning
→ preserves representations and transitions

Publication
→ governs public exposure of those representations
```

---

# Relationship to Authority

Publication does not expand Beacon's institutional authority.

Beacon remains authoritative only for its own:

```text
Discovery Signals

Discovery Metadata

Beacon lifecycle state

Beacon Publication State

Beacon provenance

Beacon Validation determinations

Beacon versions

Beacon-governed relationships
```

Referenced objects retain their source-owned authority.

---

# Relationship to Provenance

Public provenance must remain sufficient for meaningful review while respecting legitimate disclosure constraints.

The Publication Model therefore governs:

```text
what provenance may be publicly exposed
```

while the Discovery Provenance architecture governs:

```text
what provenance Beacon preserves institutionally
```

---

# Relationship to Relationships

The Relationship Model defines governed connections.

The Publication Model determines whether those relationship representations may be publicly exposed.

A valid internal relationship may remain non-public.

---

# Relationship to Schemas

Beacon schemas will eventually represent publication information such as:

```text
Publication State

published_at

published version

public record location

publication basis

restrictions

historical notice
```

Exact machine-readable structures remain pending production implementation.

---

# Relationship to Methodology

The Publication Model defines the institutional publication architecture.

Beacon Discovery Methodology will define how Beacon operationally determines:

```text
publication eligibility

publication review

publication approval

restriction handling

correction handling

withdrawal handling

historical-publication preservation
```

---

# What Is Now Established

The following architectural decisions are established:

```text
Canonical existence and publication are separate.

Identification is a pre-object condition.

Identification does not create a public record.

Creation assigns canonical identity before publication.

A newly created signal begins Unpublished.

Validation does not automatically publish a signal.

Publication is a governed institutional act.

Publication State is separate from Lifecycle State.

Active Discovery Signals may remain Unpublished.

Published representations retain the canonical BEAC identifier.

Publication does not create a second public identity.

Public representations expose Beacon Discovery Signals, not replacement copies of source-owned canonical objects.

Public source references preserve native identity and attribution.

Publication does not elevate source authority.

Public provenance must be sufficient for review.

Internal provenance and public provenance need not be identical.

Valid information may remain non-public.

Internally discoverable information may remain non-public.

Published historical versions should remain traceable where governance permits.

Published Superseded signals may remain publicly reviewable.

Published Resolved signals may remain publicly reviewable.

Prior publication should not be silently erased.

Material corrections should remain publicly reviewable.

Publication timestamps remain distinct from observation and creation timestamps.

Relationship validity does not automatically imply public disclosure.

Public discoverability should default to Published Beacon representations.
```

---

# What Remains Unfrozen

The following implementation details remain pending:

```text
exact publication approval role or mechanism

machine-readable publication property names

formal publication-basis vocabulary

public provenance minimums by Signal Type

restriction classifications

withdrawal display mechanics

correction-notice format

historical-version public navigation

public indexing behavior for Superseded signals

public indexing behavior for Resolved signals

public indexing behavior for Withdrawn signals

whether any valid Signal Types are non-public by default
```

These should be resolved through:

```text
Discovery Signals Register

Individual Discovery Signal architecture

Beacon Discovery Methodology

first production operation

production evidence
```

rather than frozen prematurely.

---

# Governing Rules

Beacon Publication follows these rules:

```text
Identify before creation when necessary.

Create before publication.

Assign canonical identity before publication.

Validate before publication eligibility.

Publish only through a governed decision.

Preserve canonical identity.

Preserve attribution.

Preserve authority boundaries.

Expose enough provenance for public review.

Respect legitimate disclosure restrictions.

Preserve public history when later state changes.

Do not silently expose internal records.

Do not silently erase prior publication.
```

The governing principle is:

> **Publication makes discovery public. It does not make discovery authoritative beyond Beacon's own institutional role.**

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
Publication Model → Defined

Discovery Signals Register → Next
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
    → COMPLETE

12. Discovery Signals Register
    → NEXT

13. Individual Discovery Signal

14. Beacon Discovery Methodology

15. Production Model / First Operation
```

---

# Next Phase II Step

The next production-architecture page is:

```text
/beacon/records/
```

The **Discovery Signals Register** will define how Beacon publicly catalogs its canonical Discovery Signals, what register-level fields are exposed, how published signals are located and distinguished by lifecycle/version state, and how the Register points to individual Beacon records without becoming a separate authority over those signals.

---

## Last Updated

September 5, 2026
