# Satoshium Beacon — Records

## Overview

The **Beacon Records** page is Satoshium Beacon's human-facing records of published canonical Discovery Signals.

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

> **Beacon Records makes published Discovery Signals findable without becoming another canonical object.**

---

# Purpose

Beacon Records answers:

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

Beacon Records is an index over Beacon-owned canonical objects.

Conceptually:

```text
Discovery Signal
→ canonical Beacon object

Record Listing
→ human-facing index representation
```

Therefore:

```text
Record Listing
≠
second canonical object
```

Beacon Records catalogs Beacon Discovery Signals.

It does not create, replace, duplicate, or independently govern them.

---

# Records Scope

Beacon Records is intended to expose Discovery Signals whose Publication State is:

```text
Published
```

Conceptually:

```text
Published Beacon Discovery Signals
        ↓
/beacon/records/
        ↓
Human-Facing Beacon Records Index
```

Draft, internal, restricted, or otherwise Unpublished signals should not appear in Beacon Records by default.

---

# Discovery Signal vs. Record Listing

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

## Record Listing

The Record Listing is a concise index representation of that canonical object.

Its purpose is to help a user:

```text
find

identify

distinguish

navigate to
```

the Discovery Signal.

The Record Listing does not replace the Discovery Signal.

---

# Canonical Record Path

Published Discovery Signals are expected to resolve through stable record paths based on their canonical BEAC identifiers.

Conceptually:

```text
/beacon/records/BEAC-2026-0001/
```

The next Phase II architecture will define the individual Discovery Signal representation at that path.

---

# Records-Level Fields

Each public Record Listing should expose enough information to identify and distinguish the Discovery Signal without reproducing the entire canonical record.

Expected records-level information includes:

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

Beacon Records must preserve the canonical Beacon identifier exactly.

Example:

```text
BEAC-2026-0001
```

Beacon Records must not create:

```text
a separate records-page identifier

a public-only identifier

a replacement identifier
```

The BEAC identifier remains the stable identity of the canonical Discovery Signal.

---

# Subject / Title

Beacon Records should provide a concise human-readable indication of what the Discovery Signal concerns.

This is a discovery aid.

It does not replace the fuller subject representation contained within the individual canonical record.

---

# Signal Type

Record Listings should expose the primary Beacon Signal Type.

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

Beacon Records must not collapse these classifications.

---

# Lifecycle State

Beacon Records should expose the current lifecycle state of the Discovery Signal.

Canonical lifecycle states are:

```text
Draft
Active
Superseded
Resolved
Withdrawn
```

Public Record Listings will normally concern Published signals whose relevant public lifecycle state may be:

```text
Active

Superseded

Resolved

Withdrawn
```

Draft signals should not ordinarily appear in the public Register.

---

# Publication State

Public Records inclusion normally requires:

```text
Publication State
→ Published
```

Beacon Records may expose Publication State explicitly when useful.

At minimum, inclusion itself should remain consistent with Beacon publication governance.

---

# Current Version

Beacon Records should identify the current governed version of each listed Discovery Signal.

Conceptually:

```text
BEAC-2026-0001

Current Version
→ 2
```

Historical version detail belongs with the individual Discovery Signal representation rather than becoming separate canonical Beacon objects.

---

# Source / Source Institution

Registry-level source information should provide concise attribution where appropriate.

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

Beacon Records should preserve source ownership.

It must not imply that Beacon owns the referenced source object.

---

# Published At

Beacon Records may expose:

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

Every Record Listing should resolve to the individual canonical Beacon record.

Example:

```text
/beacon/records/BEAC-2026-0001/
```

Beacon Records provides the discovery index.

The individual record provides the fuller Beacon representation.

---

# Record Summary

A Record Listing may provide concise discovery context.

Conceptually:

```text
Record Summary
→ navigation and discovery aid

Individual Record
→ fuller canonical Beacon representation
```

Record summaries should remain concise enough that Beacon Records does not become an uncontrolled duplicate of the canonical record.

---

# No Canonical Duplication

Beacon Records should index enough information to make Discovery Signals understandable and findable.

It should then point to the individual Beacon record for canonical detail.

The governing approach is:

> **Index enough to discover. Link to the canonical record for authority and detail.**

---

# Current and Historical Signals

Beacon Records should distinguish current published signals from signals whose lifecycle state later changes.

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

Where a replacement exists, Beacon Records or the individual record should make that relationship discoverable.

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

Beacon Records must not silently treat a previously published signal as though it never existed.

Exact public display mechanics remain subject to Methodology and production use.

---

# Version Visibility

Beacon Records should expose the current version without treating every version as a separate canonical Beacon object.

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

Beacon Records indexes Beacon Discovery Signals even when those signals reference canonical objects belonging to other Suite institutions.

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

A future Record Listing might conceptually expose:

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

As Beacon production volume grows, Beacon Records may support human-facing filtering or organization by governed fields such as:

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

# Records Ordering

Initial ordering may remain simple and deterministic.

Potential approaches include:

```text
canonical identifier

publication chronology
```

Exact production ordering remains unfrozen until actual Beacon records exist.

---

# Search

Future Beacon Records search may help users locate published Discovery Signals by:

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

# Records Inclusion Rule

The conceptual public Records inclusion rule is:

```text
Canonical Discovery Signal exists
+
Publication State = Published
+
Public representation remains permitted
=
Eligible for public Records inclusion
```

Lifecycle state affects how the signal is represented.

It does not necessarily erase the historical fact of publication.

---

# Unpublished Signals

Unpublished Discovery Signals should not appear in Beacon Records by default.

For example:

```text
Lifecycle State
→ Active

Publication State
→ Unpublished
```

does not create a public Records listing.

---

# Restricted Signals

A valid Discovery Signal may remain outside Beacon Records when publication or continuing public representation is restricted by governance.

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

# No Records-Based Authority

Records inclusion establishes:

```text
Beacon has published this Discovery Signal
under its governed architecture.
```

Records inclusion does not independently establish:

```text
truth of the underlying source assertion

Certification

Registry standing

historical significance

Integrity verification

Trust
```

Beacon Records must not become a mechanism for authority laundering.

---

# Records Integrity

Record Listings should remain consistent with the canonical Discovery Signals they index.

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
Records-Level Conformance
```

Beacon Records should never silently contradict the canonical Beacon record.

---

# Records Correction

If a Record Summary is incorrect while the underlying canonical Discovery Signal is correct, the index representation may be corrected without unnecessarily versioning the Discovery Signal itself.

This distinguishes:

```text
Records presentation error
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

Beacon Records then reflects the resulting current canonical state.

Beacon Records does not independently create that change.

---

# Conceptual Record Listing

A conceptual Records representation is:

```yaml
record_listing:
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

The Record Listing is:

```text
an index representation
```

not:

```text
a new canonical object

a frozen machine-readable schema
```

---

# Production Records

As of September 5, 2026:

> **No production Discovery Signals have been published yet.**

This is intentional.

Beacon remains:

```text
Continuing Development
```

and its first production Discovery Signal has not yet been created.

Therefore the production Records page is:

```text
Empty by design
```

The architecture exists before production evidence exists.

No placeholder `BEAC-2026-0001` should be presented as though it were an actual production signal.

---

# Relationship to Publication

The Publication Model determines whether a Discovery Signal is eligible to appear in Beacon Records.

Conceptually:

```text
Publication State = Published
        ↓
eligible for public Records inclusion
```

subject to continuing governance and disclosure rules.

---

# Relationship to Versioning

Versioning determines the current governed representation of the Discovery Signal.

Beacon Records reflects:

```text
current version
```

while the individual record preserves fuller historical version context.

---

# Relationship to Authority

Beacon Records catalogs Beacon-owned objects.

It must preserve ownership of every referenced source or canonical object.

Beacon Records does not transfer source authority to Beacon.

---

# Relationship to Validation

The Records representation should remain consistent with the validated canonical Discovery Signal it summarizes.

Validation applies to the canonical Beacon object.

Records-level conformance ensures the index accurately represents that object.

---

# Relationship to Relationships

Beacon Records may expose concise relationship information when useful for discovery.

Full governed relationship context belongs with the individual Discovery Signal.

Records presentation must preserve endpoint ownership and attribution.

---

# Relationship to Schemas

Future machine-readable Records or index representations may expose fields such as:

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

No separate canonical Records object schema is established at this stage.

---

# Relationship to Methodology

Beacon Records defines how published Beacon objects are surfaced at the records-index level.

Beacon Discovery Methodology will later define operational processes for:

```text
records inclusion

records correction

historical-state presentation

withdrawal handling

publication changes

quality review
```

---

# What Is Now Established

The following architectural decisions are established:

```text
Beacon Records is Beacon's human-facing records of published canonical Discovery Signals.

Beacon Records catalogs Discovery Signals.

Beacon Records does not create Discovery Signals.

A Record Listing is an index representation, not a second canonical object.

Public Records inclusion normally requires Publication State = Published.

Unpublished signals remain outside Beacon Records by default.

Each Record Listing preserves the canonical BEAC identifier.

Record Listings provide concise discovery context.

Record Listings point to individual canonical Beacon records.

Beacon Records should expose current Lifecycle State.

Beacon Records should expose current version.

Published Superseded signals may remain historically discoverable where governance permits.

Published Resolved signals may remain historically discoverable.

Published Withdrawn signals should preserve historical publication where governance permits.

Signal Type and Source Object Type remain distinct.

Source ownership remains preserved.

Reference does not transfer authority.

Records inclusion does not independently establish truth, Certification, Registry standing, Integrity, or Trust.

Record summaries must remain consistent with canonical Discovery Signals.

Records presentation errors and canonical object errors are distinct.

The initial production Records page is intentionally empty.
```

---

# What Remains Unfrozen

The following implementation details remain pending:

```text
exact production Records field labels

default ordering

filtering controls

search behavior

pagination if production scale requires it

historical-state display details

Withdrawn-record visibility mechanics

Records correction mechanics

machine-readable Records/index representation

additional summary fields after production experience
```

These should be informed by:

```text
Individual Discovery Signal architecture

Beacon Discovery Methodology

first production Discovery Signal

actual production Records use
```

rather than frozen before evidence exists.

---

# Governing Rules

Beacon Records follows these rules:

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

Do not treat Records inclusion as authority beyond Beacon's institutional role.
```

The governing principle is:

> **Beacon Records makes published Discovery Signals findable without becoming another canonical object.**

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
Beacon Records → Defined

Individual Discovery Signal → Next

First Production Discovery Signal → Not yet created
Production Records → Empty by design
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

12. Beacon Records
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
