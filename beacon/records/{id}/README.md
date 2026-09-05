# Satoshium Beacon — Record

## Overview

A **Beacon Record** is the canonical public HTML representation of one published Satoshium Beacon Discovery Signal.

Beacon Records uses the following hierarchy:

```text
/beacon/records/
→ Beacon Records
→ human-facing index of published Discovery Signals

/beacon/records/{id}/
→ Beacon Record
→ public representation of one canonical Discovery Signal
```

The governing principle is:

> **The Record represents the Discovery Signal. It does not replace it.**

The canonical institutional object remains the **Discovery Signal**.

A Beacon Record is its governed public representation.

---

# Route Architecture

The architectural route is:

```text
/beacon/records/{id}/
```

Within the GitHub repository, `{id}` is currently a **literal architectural directory name** used to represent the future per-record route pattern.

Accordingly, GitHub may display:

```text
beacon/records/{id}/
```

and a browser may encode the braces when that literal template directory is opened:

```text
/beacon/records/%7Bid%7D/
```

That encoded URL is a development/template artifact.

It is **not** the intended permanent URL of a production Beacon Record.

Once an actual Discovery Signal exists, the production route should use the canonical BEAC identifier itself:

```text
/beacon/records/BEAC-2026-0001/
```

Therefore:

```text
{id}
→ architectural placeholder

BEAC-2026-0001
→ future canonical production identifier

/beacon/records/BEAC-2026-0001/
→ future permanent production Record path
```

No production `BEAC-2026-0001` is claimed at this stage.

---

# Purpose

An individual Beacon Record should allow a reviewer to determine:

```text
Which Discovery Signal is this?

What is its canonical BEAC identifier?

What did Beacon discover?

What Signal Type applies?

What source was observed?

How was the discovery established and preserved?

What canonical references are involved?

What relationships are represented?

What is the current lifecycle state?

What is the publication state?

What version is current?

What historical context affects interpretation?
```

---

# Canonical Object vs. Public Representation

The architecture distinguishes the institutional object from its HTML representation.

```text
Discovery Signal
→ canonical Beacon-owned institutional object

Beacon Record
→ canonical public HTML representation of that object
```

Therefore:

```text
Beacon Record page
≠
second canonical object
```

The page does not create a new institutional object merely by representing the Discovery Signal publicly.

---

# Canonical Identity

Each production Discovery Signal receives a stable BEAC identifier under the Beacon Identifier Standard.

Pattern:

```text
BEAC-YYYY-NNNN
```

Conceptual first-production example:

```text
BEAC-2026-0001
```

The same identifier anchors the public Record location:

```text
/beacon/records/BEAC-2026-0001/
```

The Beacon Record does not receive:

```text
a separate HTML identifier

a separate public-record identifier

a separate Records identifier
```

The BEAC identifier remains the canonical identity of the Discovery Signal.

---

# Stable Record Path

The permanent public path should be based on the canonical BEAC identifier.

Conceptually:

```text
Canonical Discovery Signal
→ BEAC-2026-0001

Permanent public representation
→ /beacon/records/BEAC-2026-0001/
```

The stable path is tied to canonical identity rather than a particular version.

A governed version change therefore does not require a new canonical Record path.

---

# Discovery Signal Entry Model

The Beacon Record should represent the components established by the Discovery Signal Entry Model.

Conceptually:

```text
Identity
→ Subject
→ Signal Type
→ Source
→ Provenance
→ Canonical References
→ Discovery Metadata
→ Timestamps
→ Version
→ Status
→ Relationships
```

The HTML representation should make those components understandable without creating a competing object model.

---

# Public Record Components

A production Beacon Record is expected to expose, as applicable:

```text
BEAC Identifier

Subject

Signal Type

Discovery Summary

Source Identity

Source Institution / Publisher

Source Native Identifier

Provenance

Canonical References

Discovery Metadata

Lifecycle State

Publication State

Current Version

Timestamps

Relationships

Version History

Supersession / Resolution / Withdrawal Context
```

Exact production labels and ordering remain subject to Beacon Discovery Methodology and first production use.

---

# Subject

The Record should clearly identify what the Discovery Signal concerns.

The subject should provide enough context for human review without overstating Beacon's authority over the underlying source information.

---

# Signal Type

Each Record should expose the Discovery Signal's primary governed Signal Type.

Current architectural Signal Types are:

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

Signal Type remains distinct from Source Object Type.

For example:

```text
Signal Type
→ Certification

Source Object Type
→ Certification Package
```

---

# Discovery Summary

The Record should provide a concise human-readable representation of what Beacon discovered.

The summary should remain faithful to:

```text
the observed information

the source

the preserved provenance

Beacon's institutional role
```

It must not convert discovery into an unsupported claim of truth, certification, integrity, or trust.

---

# Source

The Beacon Record should identify the source Beacon actually observed.

Source information may include:

```text
Source Identity

Source Institution / Publisher

Native Identifier

Source Object Type

Source Location

Source-Native Status
```

when relevant and publishable.

Beacon owns the Discovery Signal.

The source institution or external source continues to own its own object and determinations.

---

# Provenance

The public Record should preserve enough provenance for meaningful review.

Conceptually:

```text
Source / Authoritative Object
        ↓
Observation
        ↓
Discovery Context
        ↓
Beacon Discovery Signal
        ↓
Preserved Public Provenance
```

Relevant provenance may include:

```text
observation time

observation method

observation context

supporting basis

discovery actor or process
```

Public provenance may be a governed subset of internal Beacon provenance where legitimate restrictions apply.

---

# Canonical References

A Beacon Record may reference canonical objects belonging to other Satoshium Suite institutions.

Examples include:

```text
Atlas
→ Authoritative Intelligence

Certifier
→ Certification Package

Registry
→ SREG

Chronicle
→ Chronicle Entry

Anchor
→ Integrity Reference

Attestor
→ Trust Statement

Navigator
→ Workflow Definition / Orchestration
```

Every referenced object retains:

```text
its native identifier

its native object type

its institutional owner

its own authority
```

---

# Authority Boundary

The governing principle remains:

> **Reference does not transfer authority.**

The Beacon Record is authoritative for Beacon's own published representation of its Discovery Signal.

It is not independently authoritative for source-owned determinations merely because those determinations appear as references.

Conceptually:

```text
Beacon
→ owns BEAC Discovery Signal

Certifier
→ owns Certification Package

Registry
→ owns SREG

Chronicle
→ owns Chronicle Entry

Anchor
→ owns Integrity Reference

Attestor
→ owns Trust Statement
```

The Record preserves these boundaries.

---

# Beacon-Owned Information

Beacon may authoritatively represent its own:

```text
BEAC identifier

Discovery Signal

Signal Type

Discovery Metadata

Beacon provenance

Lifecycle State

Publication State

Version history

Supersession information

Beacon-governed relationships

Beacon Validation determinations
```

---

# Source-Owned Information

Source institutions or external sources retain ownership of:

```text
source canonical identity

source-native object type

source-native status

source institutional determinations

source-native version information

external assertions

external authorship
```

Beacon's publication does not transfer those responsibilities.

---

# Lifecycle State

The Record should expose the current lifecycle state.

Canonical Beacon lifecycle states are:

```text
Draft

Active

Superseded

Resolved

Withdrawn
```

A public production Record will normally represent a Discovery Signal whose Publication State is Published.

Relevant public combinations include:

```text
Active / Published

Superseded / Published

Resolved / Published

Withdrawn / Published
```

---

# Publication State

Lifecycle State and Publication State remain separate.

Publication states are:

```text
Unpublished

Published
```

The normal public Record route represents:

```text
Publication State
→ Published
```

An otherwise valid Unpublished Discovery Signal does not receive a publicly discoverable production Record by default.

---

# Versioning

Canonical identity and version remain separate.

Conceptually:

```text
BEAC-2026-0001
→ canonical identity

Version 1
Version 2
Version 3
→ governed representations of that same Discovery Signal
```

The stable Record path remains:

```text
/beacon/records/BEAC-2026-0001/
```

The BEAC identifier does not change merely because the canonical object receives a new governed version.

---

# Historical Versions

Historical versions should remain traceable where governance permits.

The governing principles are:

```text
Current
≠
only

Historical
≠
deleted
```

No material canonical history should be silently overwritten.

---

# Superseded Records

If a published Discovery Signal becomes Superseded, its Record should preserve that institutional state.

Where a replacement exists, the relationship should be discoverable.

Conceptually:

```text
BEAC-2026-0001
→ Superseded

Superseded By
→ BEAC-2026-0002
```

The earlier object remains part of Beacon's institutional history.

---

# Resolved Records

A published Discovery Signal that becomes Resolved may remain publicly reviewable.

The Record should preserve:

```text
the original discovery

the prior publication

the current Resolved state

the relevant resolution context
```

Resolution does not erase history.

---

# Withdrawn Records

A previously published Discovery Signal that becomes Withdrawn should preserve the historical fact of publication and governed withdrawal where permitted.

Beacon should not silently make a previously published object appear never to have existed.

Exact withdrawal-display mechanics remain subject to Methodology and production use.

---

# Temporal Integrity

The Record should distinguish temporal facts rather than collapsing them.

Relevant timestamps may include:

```text
observed_at

created_at

published_at

version-created time

superseded_at

resolved_at

withdrawn_at
```

The architecture preserves the distinction:

```text
What Beacon observed then
≠
What Beacon observes now
```

A later observation must not silently rewrite an earlier one.

---

# Relationships

The Beacon Record may expose governed relationships when relevant and publishable.

A reviewable relationship should preserve:

```text
Endpoint A

relationship meaning

direction when meaningful

Endpoint B

attribution

supporting basis / provenance
```

Relationships connect objects.

They do not merge them.

---

# Cross-Suite Example

A future Beacon Record might conceptually show:

```text
Beacon Record
→ BEAC-2026-0001

Signal Type
→ Certification

Source Reference
→ SC-CERT-2026-0001
→ Owner: Certifier
→ Object Type: Certification Package

Related Reference
→ SREG-2026-0001
→ Owner: Registry
→ Object Type: SREG

Related Integrity Reference
→ ANCH-2026-0001
→ Owner: Anchor
→ Object Type: Integrity Reference
```

These remain separate institution-owned objects.

The example does not assert that `BEAC-2026-0001` currently exists.

---

# Public vs. Internal Representation

The public HTML Record need not expose every internal Beacon field.

Conceptually:

```text
Canonical Discovery Signal
        ↓
governed publication
        ↓
Public Beacon Record
```

Information may be withheld from the public representation because of legitimate:

```text
privacy restrictions

security restrictions

source restrictions

access restrictions

institutional governance
```

Such restrictions do not create a different canonical Discovery Signal.

---

# Human-Readable Representation

The HTML Record should make the institutional meaning of the Discovery Signal understandable to a human reviewer.

A reviewer should be able to determine:

```text
what the signal is

what was observed

where it came from

when it was observed

what Beacon claims

what Beacon does not claim

what other objects are referenced

which institution owns each referenced object

what version and lifecycle state are current
```

---

# Machine Alignment

The public HTML representation should remain consistent with Beacon's schemas and future machine-readable representations.

Conceptually:

```text
Canonical Discovery Signal
        ↓
HTML representation

Canonical Discovery Signal
        ↓
machine-readable representation
```

Neither representation becomes a separate institutional truth.

---

# Record Conformance

A public Beacon Record should remain consistent with the canonical Discovery Signal it represents.

Conceptually:

```text
Canonical BEAC identity matches
+
Signal content matches governed version
+
Lifecycle State matches
+
Publication State matches
+
Source attribution matches
+
Provenance remains reviewable
+
References preserve authority
+
Relationships preserve endpoint identity
=
Public Record Conformance
```

---

# Relationship to Beacon Records

The parent page:

```text
/beacon/records/
```

provides the human-facing index of published Discovery Signals.

The individual route:

```text
/beacon/records/{id}/
```

provides the canonical public HTML representation of one Discovery Signal.

Therefore:

```text
Beacon Records
→ find the signal

Beacon Record
→ review the signal
```

---

# Relationship to Publication

The Publication Model determines whether an individual Beacon Record becomes publicly available.

Conceptually:

```text
Canonical Discovery Signal
+
Validation conformance
+
Publication eligibility
+
governed publication decision
=
Published Beacon Record
```

Publication does not elevate source authority.

---

# Relationship to Validation

Beacon Validation evaluates conformance of the canonical Discovery Signal.

The public Record should accurately represent the validated and published Beacon object.

Validation does not independently establish:

```text
truth

Certification

Registry standing

historical significance

Integrity verification

Trust
```

---

# Relationship to Versioning & Supersession

Versioning governs material changes to the same Discovery Signal.

Supersession governs replacement relationships where applicable.

The individual Record should preserve enough historical context for a reviewer to determine which representation is current and what preceded it.

---

# Relationship to Provenance

Discovery Provenance provides the evidentiary path behind the Discovery Signal.

The Beacon Record provides the public representation of that provenance at a level sufficient for meaningful review and permitted disclosure.

---

# Relationship to Authority

The Authority & Reference Model determines how the Record represents referenced objects without transferring their authority to Beacon.

The Beacon Record should always preserve:

```text
source identity

source ownership

source-native object type

reference meaning
```

---

# Relationship to Schemas

The public HTML Record should remain structurally compatible with Beacon's canonical Discovery Signal schema architecture.

No separate canonical object schema is created merely because the object is represented as HTML.

---

# Conceptual Public Record

A conceptual representation is:

```yaml
beacon_record:
  identifier: ""
  subject: ""
  signal_type: ""
  discovery_summary: ""

  source:
    institution: ""
    native_identifier: ""
    object_type: ""
    location: ""

  provenance:
    public_summary: ""
    supporting_basis: []

  canonical_references: []
  discovery_metadata: {}

  lifecycle_state: ""
  publication_state: ""
  current_version: ""

  timestamps:
    observed_at: ""
    created_at: ""
    published_at: ""

  relationships: []
  version_history: []
  historical_context: ""
```

This is architectural only.

`beacon_record` describes a public representation.

It does not establish a second canonical Beacon object type.

---

# First Production Record

As of September 5, 2026:

> **No production Beacon Record exists yet.**

The first production Discovery Signal has not yet been created.

The following remains a conceptual future pattern:

```text
First Discovery Signal
→ BEAC-2026-0001

First permanent Record page
→ /beacon/records/BEAC-2026-0001/
```

The `{id}` repository directory exists only to define the architecture before production.

Production proof must come from an actual governed Beacon operation.

---

# What Is Now Established

The following architectural decisions are established:

```text
Each published production Discovery Signal receives a permanent page beneath /beacon/records/.

The permanent path uses the canonical BEAC identifier.

The repository's {id} directory is an architectural placeholder.

The browser-encoded %7Bid%7D path is not a production Record URL.

The individual human-facing representation is called a Beacon Record.

Beacon Record is a representation, not a second canonical object type.

The canonical institutional object remains the Discovery Signal.

The BEAC identifier remains stable across governed versions of the same signal.

The public Record follows the Discovery Signal Entry Model.

The Record preserves source attribution and authority boundaries.

The Record preserves reviewable public provenance.

Signal Type remains distinct from Source Object Type.

Lifecycle State remains distinct from Publication State.

Historical versions remain traceable where governance permits.

Supersession, resolution, and withdrawal should remain historically reviewable where permitted.

Relationships preserve endpoint identity and ownership.

Public HTML and machine-readable representations should remain aligned.

No production BEAC object is claimed before the first governed Beacon operation.
```

---

# What Remains Unfrozen

The following implementation details remain pending:

```text
exact production field labels

exact field ordering

version-specific historical URL syntax

machine-readable companion format

public provenance depth by Signal Type

restricted-field presentation

correction-notice presentation

Superseded-state presentation

Resolved-state presentation

Withdrawn-state presentation

relationship display depth

production navigation behavior

exact first production Discovery Signal content
```

These should be informed by Beacon Discovery Methodology and actual production use.

---

# Governing Rules

Beacon Records follows these rules for individual Records:

```text
One Discovery Signal
→ one canonical BEAC identity.

One published Discovery Signal
→ one permanent canonical Record path.

Preserve source identity.

Preserve source attribution.

Preserve provenance.

Preserve authority boundaries.

Preserve Lifecycle State.

Preserve Publication State.

Preserve version context.

Preserve historical continuity.

Do not silently rewrite earlier observations.

Do not create a second canonical object merely for HTML presentation.

Do not treat publication as authority over referenced objects.
```

The governing principle is:

> **The Record represents the Discovery Signal. It does not replace it.**

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
Individual Beacon Record → Defined

Beacon Discovery Methodology → Next

First Production Discovery Signal → Not yet created
First Production Beacon Record → Not yet created
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

13. Individual Beacon Record
    → COMPLETE

14. Beacon Discovery Methodology
    → NEXT

15. Production Model / First Operation
```

---

# Next Phase II Step

The next production-architecture step is:

```text
/beacon/methodology/
```

**Beacon Discovery Methodology**

This will define the repeatable institutional process by which Beacon:

```text
identifies a candidate discovery

creates a Discovery Signal

assigns its BEAC identifier

preserves provenance

classifies the Signal Type

validates the canonical object

reviews authority and references

governs lifecycle state

makes a publication decision

publishes the Beacon Record

maintains the Record over time
```

That methodology should be established before the first actual production Discovery Signal is created.

---

## Last Updated

September 5, 2026
