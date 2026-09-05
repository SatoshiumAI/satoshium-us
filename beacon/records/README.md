# Satoshium Beacon — Discovery Signals Register

## Overview

The **Discovery Signals Register** is Satoshium Beacon's human-facing index of published canonical Discovery Signals.

It provides a stable public location where users can:

```text
locate published Beacon Discovery Signals

identify their BEAC identifiers

understand their Signal Types

see their current lifecycle state

identify their current version

review concise source attribution

follow each entry to the individual Beacon record
```

The governing principle is:

> **The Register makes Beacon's published objects findable without becoming another object itself.**

---

# Purpose

The Discovery Signals Register answers:

```text
What Discovery Signals has Beacon published?

What is each signal's BEAC identifier?

What kind of discovery does each signal represent?

What is its current lifecycle state?

What is its current version?

What source or source institution is relevant?

Where is the individual canonical Beacon record?
```

---

# Institutional Boundary

The Discovery Signals Register is an index over Beacon-owned canonical objects.

Conceptually:

```text
Discovery Signal
→ canonical Beacon object

Register Entry
→ human-facing index representation
```

Therefore:

```text
Register Entry
≠
second canonical object
```

The Register catalogs Beacon Discovery Signals.

It does not create, replace, duplicate, or independently govern them.

---

# Register Scope

The public Discovery Signals Register is intended to expose Discovery Signals whose Publication State is:

```text
Published
```

Conceptually:

```text
Published Beacon Discovery Signals
        ↓
/beacon/records/
        ↓
Human-Facing Discovery Index
```

Draft, internal, restricted, or otherwise Unpublished signals should not appear in the public Register by default.

---

# Discovery Signal vs. Register Entry

## Discovery Signal

The Discovery Signal is the canonical Beacon production object.

Example:

```text
BEAC-2026-0001
```

Beacon owns:

```text
the Discovery Signal

the BEAC identifier

the Discovery Metadata

the lifecycle state

the publication state

the version history

the provenance

the Beacon-governed relationships
```

## Register Entry

The Register entry is a concise index representation of that canonical object.

Its purpose is to help a user:

```text
find

identify

distinguish

navigate to
```

the Discovery Signal.

The Register entry does not replace the Discovery Signal.

---

# Canonical Record Path

Published Discovery Signals are expected to resolve through stable record paths based on their canonical BEAC identifiers.

Conceptually:

```text
/beacon/records/BEAC-2026-0001/
```

The next Phase II architecture will define the individual Discovery Signal representation at that path.

---

# Register-Level Fields

Each public Register entry should expose enough information to identify and distinguish the Discovery Signal without reproducing the entire canonical record.

Expected register-level information includes:

```text
BEAC Identifier

Subject / Title

Signal Type

Lifecycle State

Publication State

Current Version

Source / Source Institution

Published At

Record Link
```

Exact production labels remain subject to the first individual record and production operation.

---

# BEAC Identifier

The Register must preserve the canonical Beacon identifier exactly.

Example:

```text
BEAC-2026-0001
```

The Register must not create:

```text
a separate register identifier

a public-only identifier

a replacement identifier
```

The BEAC identifier remains the stable identity of the canonical Discovery Signal.

---

# Subject / Title

The Register should provide a concise human-readable indication of what the Discovery Signal concerns.

This is a discovery aid.

It does not replace the fuller subject representation contained within the individual canonical record.

---

# Signal Type

Register entries should expose the primary Beacon Signal Type.

The current architectural Signal Types are:

```text
Information

Jurisdiction

Certification

Registry

Historical

Integrity

Trust

Relationship
```

Signal Type helps users understand the nature of the discovery.

---

# Source Object Type

Signal Type and Source Object Type remain distinct.

Example:

```text
Beacon Signal Type
→ Certification

Source Object Type
→ Certification Package
```

The Register must not collapse these classifications.

---

# Lifecycle State

The Register should expose the current lifecycle state of the Discovery Signal.

Canonical lifecycle states are:

```text
Draft
Active
Superseded
Resolved
Withdrawn
```

Public Register entries will normally concern Published signals whose relevant public lifecycle state may be:

```text
Active

Superseded

Resolved

Withdrawn
```

Draft signals should not ordinarily appear in the public Register.

---

# Publication State

Public Register inclusion normally requires:

```text
Publication State
→ Published
```

The Register may expose Publication State explicitly when useful.

At minimum, inclusion itself should remain consistent with Beacon publication governance.

---

# Current Version

The Register should identify the current governed version of each listed Discovery Signal.

Conceptually:

```text
BEAC-2026-0001

Current Version
→ 2
```

Historical version detail belongs with the individual Discovery Signal representation rather than becoming separate canonical Register objects.

---

# Source / Source Institution

Register-level source information should provide concise attribution where appropriate.

Examples may include:

```text
Certifier

Registry

Chronicle

Anchor

Atlas

Attestor

external source
```

The Register should preserve source ownership.

It must not imply that Beacon owns the referenced source object.

---

# Published At

The Register may expose:

```text
published_at
```

to show when the Beacon representation became publicly discoverable.

Publication time remains distinct from:

```text
observed_at

created_at

other source-native timestamps
```

---

# Record Link

Every Register entry should resolve to the individual canonical Beacon record.

Example:

```text
/beacon/records/BEAC-2026-0001/
```

The Register provides the discovery index.

The individual record provides the fuller Beacon representation.

---

# Register Summary

A Register entry may provide concise discovery context.

Conceptually:

```text
Register Summary
→ navigation and discovery aid

Individual Record
→ fuller canonical Beacon representation
```

Register summaries should remain concise enough that the Register does not become an uncontrolled duplicate of the canonical record.

---

# No Canonical Duplication

The Register should index enough information to make Discovery Signals understandable and findable.

It should then point to the individual Beacon record for canonical detail.

The governing approach is:

> **Index enough to discover. Link to the canonical record for authority and detail.**

---

# Current and Historical Signals

The Register should distinguish current published signals from signals whose lifecycle state later changes.

Examples:

```text
Active / Published
→ current institutional discovery

Superseded / Published
→ historical signal replaced for current use

Resolved / Published
→ historical signal whose discovery condition reached a governed conclusion

Withdrawn / Published
→ historical publication with withdrawal state preserved where governance permits
```

---

# Active Signals

Active Published Discovery Signals should be readily discoverable as current Beacon objects.

Conceptually:

```text
Lifecycle State
→ Active

Publication State
→ Published
```

---

# Superseded Signals

A Superseded Published signal should remain traceable when governance permits.

Where a replacement exists, the Register or individual record should make that relationship discoverable.

Conceptually:

```text
BEAC-2026-0001
→ Superseded

Superseded By
→ BEAC-2026-0002
```

The earlier signal remains part of Beacon's institutional history.

---

# Resolved Signals

Resolved Published signals may remain publicly discoverable as historical Beacon objects.

Conceptually:

```text
Lifecycle State
→ Resolved

Publication State
→ Published
```

Resolution does not erase prior publication.

---

# Withdrawn Signals

Previously published Withdrawn signals should preserve the historical fact of publication and governed withdrawal to the extent permitted.

The Register must not silently treat a previously published signal as though it never existed.

Exact public display mechanics remain subject to Methodology and production use.

---

# Version Visibility

The Register should expose the current version without treating every version as a separate canonical Register object.

Conceptually:

```text
BEAC-2026-0001
Current Version → 2
        ↓
Individual Record
        ↓
Governed Version History
```

Versioning remains governed by:

```text
/beacon/versioning/
```

---

# Authority Boundary

The Register indexes Beacon Discovery Signals even when those signals reference canonical objects belonging to other Suite institutions.

For example:

```text
BEAC-2026-0001
→ Beacon Discovery Signal

SC-CERT-2026-0001
→ Certifier Certification Package

SREG-2026-0001
→ Registry record
```

The governing principle remains:

> **Reference does not transfer authority.**

---

# Cross-Suite Example

A future Register entry might conceptually expose:

```text
BEAC Identifier
→ BEAC-2026-0001

Signal Type
→ Certification

Source Reference
→ SC-CERT-2026-0001

Related Reference
→ SREG-2026-0001

Record
→ /beacon/records/BEAC-2026-0001/
```

This does not make the three objects one object.

Certifier continues to own:

```text
SC-CERT-2026-0001
```

Registry continues to own:

```text
SREG-2026-0001
```

Beacon owns:

```text
BEAC-2026-0001
```

---

# Discovery and Filtering

As Beacon production volume grows, the Register may support human-facing filtering or organization by governed fields such as:

```text
Signal Type

Lifecycle State

Source Institution

Publication date

Current vs. historical status
```

Filtering is a presentation capability.

It does not alter:

```text
canonical identity

lifecycle state

publication state

version

authority
```

---

# Register Ordering

Initial ordering may remain simple and deterministic.

Potential approaches include:

```text
canonical identifier

publication chronology
```

Exact production ordering remains unfrozen until actual Beacon records exist.

---

# Search

Future Register search may help users locate published Discovery Signals by:

```text
subject

BEAC identifier

Signal Type

source

source institution
```

Search improves discoverability.

It does not change:

```text
publication eligibility

institutional state

authority
```

---

# Register Inclusion Rule

The conceptual public Register inclusion rule is:

```text
Canonical Discovery Signal exists
+
Publication State = Published
+
Public representation remains permitted
=
Eligible for public Register inclusion
```

Lifecycle state affects how the signal is represented.

It does not necessarily erase the historical fact of publication.

---

# Unpublished Signals

Unpublished Discovery Signals should not appear in the public Register by default.

For example:

```text
Lifecycle State
→ Active

Publication State
→ Unpublished
```

does not create a public Register entry.

---

# Restricted Signals

A valid Discovery Signal may remain outside the public Register when publication or continuing public representation is restricted by governance.

Potential reasons may include:

```text
privacy

security

source restrictions

access limitations

institutional governance

other legitimate restrictions
```

---

# No Register-Based Authority

Register inclusion establishes:

```text
Beacon has published this Discovery Signal
under its governed architecture.
```

Register inclusion does not independently establish:

```text
truth of the underlying source assertion

Certification

Registry standing

historical significance

Integrity verification

Trust
```

The Register must not become a mechanism for authority laundering.

---

# Register Integrity

Register entries should remain consistent with the canonical Discovery Signals they index.

Conceptually:

```text
Identifier matches
+
Signal Type matches
+
Lifecycle State matches
+
Current Version matches
+
Publication State matches
+
Record Link resolves correctly
=
Register-Level Conformance
```

The Register should never silently contradict the canonical Beacon record.

---

# Register Correction

If a Register summary is incorrect while the underlying canonical Discovery Signal is correct, the index representation may be corrected without unnecessarily versioning the Discovery Signal itself.

This distinguishes:

```text
Register presentation error
```

from:

```text
canonical Discovery Signal error
```

The latter is governed by Beacon Versioning & Supersession.

---

# Canonical Change

If the Discovery Signal itself changes materially:

```text
Versioning & Supersession
→ governs the canonical change
```

The Register then reflects the resulting current canonical state.

The Register does not independently create that change.

---

# Conceptual Register Entry

A conceptual Register representation is:

```yaml
register_entry:
  beac_identifier: ""
  subject: ""
  signal_type: ""
  lifecycle_state: ""
  publication_state: ""
  current_version: ""
  source_summary: ""
  published_at: ""
  record_location: ""
```

This is architectural only.

The Register entry is:

```text
an index representation
```

not:

```text
a new canonical object

a frozen machine-readable schema
```

---

# Production Register

As of September 5, 2026:

> **No production Discovery Signals have been published yet.**

This is intentional.

Beacon remains:

```text
Continuing Development
```

and its first production Discovery Signal has not yet been created.

Therefore the production Register is:

```text
Empty by design
```

The architecture exists before production evidence exists.

No placeholder `BEAC-2026-0001` should be presented as though it were an actual production signal.

---

# Relationship to Publication

The Publication Model determines whether a Discovery Signal is eligible to appear in the public Register.

Conceptually:

```text
Publication State = Published
        ↓
eligible for public Register inclusion
```

subject to continuing governance and disclosure rules.

---

# Relationship to Versioning

Versioning determines the current governed representation of the Discovery Signal.

The Register reflects:

```text
current version
```

while the individual record preserves fuller historical version context.

---

# Relationship to Authority

The Register catalogs Beacon-owned objects.

It must preserve ownership of every referenced source or canonical object.

The Register does not transfer source authority to Beacon.

---

# Relationship to Validation

The Register representation should remain consistent with the validated canonical Discovery Signal it summarizes.

Validation applies to the canonical Beacon object.

Register-level conformance ensures the index accurately represents that object.

---

# Relationship to Relationships

The Register may expose concise relationship information when useful for discovery.

Full governed relationship context belongs with the individual Discovery Signal.

Register presentation must preserve endpoint ownership and attribution.

---

# Relationship to Schemas

Future machine-readable Register or index representations may expose fields such as:

```text
BEAC identifier

subject

Signal Type

Lifecycle State

Publication State

current version

source summary

published_at

record location
```

No separate canonical Register object schema is established at this stage.

---

# Relationship to Methodology

The Discovery Signals Register defines how published Beacon objects are surfaced at the register level.

Beacon Discovery Methodology will later define operational processes for:

```text
register inclusion

register correction

historical-state presentation

withdrawal handling

publication changes

quality review
```

---

# What Is Now Established

The following architectural decisions are established:

```text
The Discovery Signals Register is Beacon's human-facing index of published canonical Discovery Signals.

The Register catalogs Discovery Signals.

The Register does not create Discovery Signals.

A Register entry is an index representation, not a second canonical object.

Public Register inclusion normally requires Publication State = Published.

Unpublished signals remain outside the public Register by default.

Each Register entry preserves the canonical BEAC identifier.

Register entries provide concise discovery context.

Register entries point to individual canonical Beacon records.

The Register should expose current Lifecycle State.

The Register should expose current version.

Published Superseded signals may remain historically discoverable where governance permits.

Published Resolved signals may remain historically discoverable.

Published Withdrawn signals should preserve historical publication where governance permits.

Signal Type and Source Object Type remain distinct.

Source ownership remains preserved.

Reference does not transfer authority.

Register inclusion does not independently establish truth, Certification, Registry standing, Integrity, or Trust.

Register summaries must remain consistent with canonical Discovery Signals.

Register presentation errors and canonical object errors are distinct.

The initial production Register is intentionally empty.
```

---

# What Remains Unfrozen

The following implementation details remain pending:

```text
exact production Register field labels

default ordering

filtering controls

search behavior

pagination if production scale requires it

historical-state display details

Withdrawn-record visibility mechanics

Register correction mechanics

machine-readable Register/index representation

additional summary fields after production experience
```

These should be informed by:

```text
Individual Discovery Signal architecture

Beacon Discovery Methodology

first production Discovery Signal

actual production Register use
```

rather than frozen before evidence exists.

---

# Governing Rules

The Discovery Signals Register follows these rules:

```text
Index only what publication governance permits.

Preserve the canonical BEAC identifier.

Summarize without duplicating canonical authority.

Preserve Lifecycle State.

Preserve current-version context.

Preserve source attribution.

Preserve authority boundaries.

Point users to the individual Beacon record.

Preserve historical discoverability where governance permits.

Do not expose Unpublished signals by default.

Do not treat Register inclusion as authority beyond Beacon's institutional role.
```

The governing principle is:

> **The Register makes Beacon's published objects findable without becoming another object itself.**

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
Discovery Signals Register → Defined

Individual Discovery Signal → Next

First Production Discovery Signal → Not yet created
Production Register → Empty by design
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
    → COMPLETE

13. Individual Discovery Signal
    → NEXT

14. Beacon Discovery Methodology

15. Production Model / First Operation
```

---

# Next Phase II Step

The next production-architecture step is the individual Discovery Signal representation:

```text
/beacon/records/{id}/
```

This architecture will define what a user sees when opening a specific published Beacon Discovery Signal, including its canonical identity, subject, Signal Type, source, provenance, references, relationships, lifecycle, publication state, version, and historical context.

The architecture should be established before creating the first actual production object:

```text
BEAC-2026-0001
```

---

## Last Updated

September 5, 2026
