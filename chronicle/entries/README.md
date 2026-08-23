# Chronicle Entries

## Purpose

A Chronicle Entry is the canonical historical-preservation object of Satoshium Chronicle.

Each Entry represents one qualifying historical Occurrence that Chronicle has determined should be preserved as part of the historical record.

Chronicle Entries preserve the historical representation, temporal context, authoritative references, Sources, Evidence where applicable, Provenance, Relationships, Verification, Validation context, publication lineage, Corrections, and Entry Versions needed for future historical review.

Chronicle preserves history without assuming authority over the underlying actions or records established by another Satoshium Suite institution.

---

## Suite Alignment

Chronicle Entries operate within the Satoshium Suite architecture.

They follow Suite-wide expectations for:

```text
Stable canonical objects
Clear institutional authority boundaries
Canonical terminology
Structured schemas
Durable identifiers and references
Reference-based interoperability
Evidence handling
Provenance and traceability
Verification
Validation
Version preservation
Correction lineage
Publication controls
Documented and repeatable procedures
```

Chronicle references authoritative Suite objects instead of duplicating, replacing, or reinterpreting them.

The governing principle is:

> Reference does not transfer authority.

---

## Canonical Object

The canonical Chronicle object is:

```text
Chronicle Entry
```

The Entry is not the historical Occurrence itself.

The distinction is:

```text
Occurrence
  what happened

Chronicle Entry
  Chronicle's structured historical-preservation
  record representing that qualifying Occurrence
```

Chronicle does not create a separate canonical object merely because an Event Type or Event-Type Profile applies.

The model remains:

```text
One Chronicle Entry
        +
Event Type
        +
Event-Type Profile where applicable
```

---

## Authority Boundary

A Chronicle Entry is authoritative only as Chronicle's historical-preservation record.

Other Suite institutions remain authoritative for their own canonical objects and institutional functions.

Examples include:

```text
Certifier
  Certification Packages
  certification determinations
  certification lifecycle
  certification status

Registry
  SREG Registry Entries
  registration
  cataloging
  Registry metadata
  Registry lifecycle

Anchor
  Integrity References

Beacon
  Discovery Signals
  Discovery Metadata

Attestor
  Trust Statements
  Attestations

Navigator
  Workflow Definitions

Atlas
  Atlas records
  jurisdiction data
  source intelligence
  Evidence
  metadata
  source material
```

Chronicle may preserve the historical Occurrence and reference these objects.

Chronicle does not absorb their authority.

---

## What Is an Entry?

A Chronicle Entry is a structured, identifiable, version-aware historical-preservation record representing one qualifying Occurrence.

An Occurrence may involve:

```text
Certification activity
Registry milestones
Publications
Decisions
Governance changes
Announcements
Institutional milestones
Anchor activity
Attestation activity
Significant releases
Investigations
Observations
Other historically preservable developments
```

These are not separate canonical Entry objects.

Each qualifying Occurrence uses the same Chronicle Entry model and is classified through Event Type and, where applicable, an Event-Type Profile.

---

## Preservation Eligibility

An Occurrence does not become a Chronicle Entry merely because it happened.

Chronicle first determines whether the Occurrence qualifies for historical preservation.

Preservation Eligibility asks:

> Should Chronicle preserve this Occurrence?

Eligibility may be established through:

```text
Automatic Preservation
Discretionary Preservation
Retrospective Preservation
```

as governed by Chronicle rules.

Historical Significance explains why the Occurrence matters.

Preservation Eligibility is the institutional determination that the Occurrence belongs in Chronicle.

Preservation Eligibility remains distinct from:

```text
Evidence sufficiency
Authority
Verification
Validation
Publication
```

An Occurrence may be Preservation Eligible even while its drafted Entry still requires additional Evidence, Verification, correction, or Validation.

---

## Historical Significance

Historical Significance describes why an Occurrence matters to the development, state, institutional relationships, decisions, milestones, or historical continuity of Satoshium.

Potential significance factors include:

```text
Institutional change
Lifecycle significance
First or last occurrence
Major milestone
Material architectural change
Relationship significance
Evidentiary or interpretive importance
Historical continuity value
```

Historical Significance belongs primarily to Preservation Eligibility and Historical Context.

It is not a numerical Validation score.

---

## Core Principles

### History First

Chronicle preserves qualifying historical memory.

Interpretation may evolve, but the historical lineage of Chronicle's own record should remain reviewable.

### Time Matters

Chronicle distinguishes among:

```text
Event Date
Entry creation date / time
retrieval date / time
publication date / time
Correction date
Entry Version state
```

Occurrence time and Chronicle record-maintenance time must not be conflated.

### Evidence Matters

Evidence may support, challenge, or contextualize Chronicle's representation.

Evidence does not replace the authoritative Suite object that established an underlying action or determination.

A Source may also have evidentiary value without requiring a duplicate Evidence object or Evidence reference.

### Provenance Matters

Chronicle preserves how information entered the Entry.

Minimum Provenance includes:

```text
Origin
Acquisition / Access Method
Capture / Retrieval Date
Source or Authoritative Record Reference where required
Material Provenance Limitations where applicable
```

### Transparency Matters

Chronicle distinguishes among:

```text
Authoritative fact
Source material
Evidence
Historical Context
Verification
Validation
Interpretation
Known limitation
Unknown information
```

Interpretation must not be presented as authoritative fact.

### Authority Matters

Chronicle preserves history without assuming another institution's authority.

---

## Governing Production Structure

The production Chronicle Entry structure is governed by:

```text
Chronicle Base Schema
        +
Applicable Event-Type Profile
        +
Controlled Values
        +
Chronicle institutional rules
```

The current Base Schema is:

```text
/chronicle/schemas/chronicle-base-schema.json
```

The first production Event-Type Profile is:

```text
/chronicle/schemas/certification-event-profile/
```

The Base Schema defines universal Chronicle Entry structure.

An Event-Type Profile specializes that structure for a governed Event Type without creating a second canonical object.

---

## Universal Entry Fields

The Chronicle Base Schema governs universal fields including:

```text
entry_id
schema_id
schema_version
entry_version
title
summary
event_type
event_date
historical_context
provenance
verification_state
lifecycle_state
publication_state
entry_created_at
```

Conditional fields may include:

```text
event_type_profile
originating_system
authoritative_record_references
source_references
evidence_references
relationships
correction_references
prior_version_reference
published_at
updated_at
limitations
```

Required, Conditional, and Optional treatment is governed by the Base Schema and applicable Event-Type Profile.

---

## Identifier

Every production Chronicle Entry receives a permanent Chronicle identifier in the form:

```text
CHR-YYYY-NNNN
```

Example:

```text
CHR-2026-0001
```

The `YYYY` component represents the Chronicle identifier assignment year.

It does not represent the Event Date.

The identifier:

```text
must be unique
must never be reused
remains stable across Entry Versions
does not encode Event Type
does not encode Verification State
does not encode Lifecycle State
does not encode Publication State
```

A simulated or dry-run identifier is not assigned, reserved, or consumed merely because it was used for testing.

---

## Event Type

Event Type is the controlled classification describing the Occurrence represented by the Entry.

Event Type does not replace permanent Entry identity.

For the initial certification Event-Type family:

```text
certification_created
certification_renewed
certification_suspended
certification_revoked
certification_expired
```

---

## Event-Type Profiles

An Event-Type Profile adds requirements for a particular class of preserved Occurrence without replacing the Chronicle Base Schema.

The first production Profile is:

```text
certification-event-profile
Version 1.0.0
```

It requires, among other things:

```text
event_type_profile = certification-event-profile
originating_system = certifier
approved certification Event Type
non-null event_date
authoritative_record_references
at least one structured Certifier authoritative reference
Certification-specific Provenance
conditional Registry relationship when one exists
and is materially relevant
```

The Profile does not duplicate Certification Package contents.

---

## Production Entry Package

Chronicle uses a deliberately minimal production package for each published Entry.

The initial production convention is:

```text
/chronicle/entries/CHR-YYYY-NNNN/
│
├── index.html
├── record.json
├── README.md
├── CHR-YYYY-NNNN-vN-validation.md
└── CHR-YYYY-NNNN-vN-publication-gate.md
```

### `index.html`

Official human-readable Chronicle Entry.

### `record.json`

Official machine-readable Chronicle Entry governed by the applicable Chronicle schema stack.

### `README.md`

Institutional and repository documentation for the Entry package.

The canonical Chronicle Entry remains the coordinated:

```text
index.html
record.json
README.md
```

representation.

The production convention now also preserves durable Entry-Version procedural artifacts:

```text
CHR-YYYY-NNNN-vN-validation.md
CHR-YYYY-NNNN-vN-publication-gate.md
```

These procedural artifacts are associated with a specific Entry Version. They are not
separate Chronicle Entries, do not receive independent Chronicle identifiers, and do
not create independent lifecycles.

Chronicle does not automatically create separate Verification, Source, Evidence,
Provenance, Correction, or Version artifacts inside every Entry directory. Supporting
artifacts are created only when their additional structure provides durable institutional value.

The governing principle remains:

> Minimum necessary structure first.

---

## Entry Production Procedure

Chronicle Entries follow the formal Chronicle Entry Production Procedure.

The canonical production sequence is:

```text
Identify Occurrence
        ↓
Assess Preservation Eligibility
        ↓
Collect Authoritative References
        ↓
Classify Event Type
        ↓
Select Event-Type Profile
        ↓
Assign Chronicle Identifier
        ↓
Create Entry
        ↓
Establish Relationships
        ↓
Record Sources / Evidence / Provenance
        ↓
Perform Verification
        ↓
Perform Validation
        ↓
Publication Gate
        ↓
Approve / Withhold Publication
        ↓
Publish when approved
        ↓
Preserve
```

Steps may loop or return to earlier stages when correction, failure, new information, or Versioning requires additional work.

---

## Verification

Chronicle Verification reviews Chronicle's own historical representation.

Verification asks:

> Is Chronicle's historical representation adequately supported and internally reviewable?

Verification may review:

```text
Entry identity
Occurrence
authoritative references
Sources
Evidence
Event Date
Relationships
Provenance
Historical Context
material limitations
temporal consistency
authority boundaries
```

Approved Verification States are:

```text
not_reviewed
in_review
verified
verified_with_limitations
unresolved
```

Verification does not re-adjudicate another institution's authoritative determination.

---

## Validation

Validation evaluates the current Chronicle Entry Version against the institutional and machine-readable requirements governing it.

Validation asks:

> Does this Chronicle Entry conform to the requirements governing this Entry Version?

Chronicle Validation uses:

```text
CHR-VAL-001
through
CHR-VAL-014
```

The overall result is:

```text
PASS
or
FAIL
```

There is no universal `validation_state` field in the Chronicle Base Schema.

Validation is preserved as a result tied to the exact Entry Version reviewed rather than as another canonical Entry state system.

---

## CHR-VAL-011 and Publication Gate

Chronicle keeps Validation readiness and publication approval separate.

The distinction is:

```text
CHR-VAL-011 — Publication Readiness
  tests whether publication prerequisites
  are satisfied from a Validation standpoint.

Chronicle Publication Gate
  makes the separate institutional decision
  to approve or withhold Publication.
```

Therefore:

```text
Validation PASS
        ≠
Approved for Publication
        ≠
Published
```

The formal Publication Gate is:

```text
Required Verification State
        +
Validation PASS
        +
Required Authoritative References
        +
Publication Prerequisites
        =
Eligible for Publication
```

---

## Entry States

Chronicle does not use a generic Entry Status field to collapse distinct state systems.

The governing state systems are:

```text
Lifecycle State
Verification State
Publication State
```

These answer different institutional questions.

Validation remains separate:

```text
Validation Result
  PASS / FAIL
```

and applies to a specific Entry Version.

---

## Lifecycle State

Approved Lifecycle State values include:

```text
draft
active
superseded
withdrawn
preserved
```

Lifecycle State describes the Entry's Chronicle lifecycle condition.

---

## Publication State

Approved Publication State values include:

```text
not_published
pending_publication
published
withdrawn_from_publication
```

Publication State describes the Entry's public production condition.

When:

```text
publication_state = published
```

the Base Schema requires:

```text
published_at
```

---

## Relationships

Chronicle Entries may connect to other Chronicle Entries, Suite records, or relevant external objects using approved Relationship Types:

```text
references
related_to
derived_from
supersedes
superseded_by
corrects
corrected_by
precedes
follows
```

Relationships preserve connection without transferring authority.

Important distinctions include:

```text
Precedes ≠ Causes
Supersedes ≠ Deletes
References ≠ Owns
Related To ≠ Authoritative For
```

A Relationship should exist only when it adds reliable historical meaning.

---

## Sources and Evidence

Chronicle preserves the distinction:

```text
Source
  where information came from

Evidence
  material bearing on the Entry or claim

Authoritative Record
  object owned by the institution
  that established the underlying action

Provenance
  how information originated,
  moved, was accessed,
  and entered Chronicle
```

Chronicle should use actual published identifiers where they exist.

Where no formal identifier exists, Chronicle should use a descriptive reference and durable URL rather than inventing an identifier.

---

## Corrections and Versioning

Chronicle may correct its own Entries when errors, new Evidence, corrected Provenance, changed Relationships, improved sourcing, or additional context justify change.

No silent substantive rewriting is permitted.

A material Correction should preserve:

```text
Original information
Corrected information
Correction date
Reason
Affected fields
Resulting Entry Version
```

The governing distinction is:

```text
Correction
  explains why Chronicle changed its record.

Version
  preserves the resulting state.
```

The governing principle is:

> Correct forward. Preserve backward.

---

## Entry Version

A material change affecting the same canonical Chronicle Entry creates a new Entry Version when required.

Example:

```text
CHR-2026-0001
Entry Version 1
        ↓
Material Correction
        ↓
CHR-2026-0001
Entry Version 2
```

The permanent Entry identifier remains unchanged.

Entry Version is distinct from Schema Version.

---

## New Chronicle Entry

A distinct qualifying Occurrence receives a new Chronicle Entry.

Chronicle should not force a later Occurrence into a Version of an earlier Entry merely because the Occurrences are related.

For example:

```text
Certification Created
```

and a later:

```text
Certification Revoked
```

would ordinarily represent distinct qualifying Occurrences and therefore distinct Chronicle Entries.

---

## Publication

A Chronicle Entry becomes a published production record only after completion of the applicable production procedure and successful Publication Gate.

Publication requires:

```text
Preservation Eligibility
valid Chronicle identifier
required Entry fields
required authoritative references
sufficient Provenance
required Verification State
Validation PASS
publication prerequisites
Publication Gate approval
```

Publication then records the appropriate production state and publication timestamp.

Human-readable and machine-readable official representations must remain materially consistent.

---

## Public Entry Collection

The canonical public collection is:

```text
/chronicle/entries/
```

Individual published Entries use stable canonical locations under:

```text
/chronicle/entries/CHR-YYYY-NNNN/
```

Chronicle does not create a redundant parallel collection such as:

```text
Preserved Events
```

unless future operational experience demonstrates a genuinely different institutional function.

---

## Timeline and Historical Discovery

Published Chronicle Entries may later be surfaced through Timeline or other discovery mechanisms.

Timeline is downstream discovery.

It should derive from published Chronicle Entries rather than become an independent record system.

The canonical historical object remains:

```text
Chronicle Entry
```

---

## Preservation

Chronicle favors durable preservation over deletion.

Historical preservation should maintain:

```text
Entry identity
Entry Version lineage
Correction lineage
Relationships
Provenance
authoritative references
material limitations
Validation context
Publication history
prior material states
```

Publication is a milestone within preservation.

It is not the end of Chronicle responsibility.

---

## Maintenance After Publication

Post-publication triggers may include:

```text
new Evidence
new Source
authoritative-record change
new related Occurrence
Relationship change
Provenance correction
factual correction
classification correction
schema migration
Event-Type Profile migration
publication defect
```

The maintenance path is:

```text
Published Entry
        ↓
New Information / Defect
        ↓
Materiality Review
        ↓
Editorial Update
or
Formal Correction
or
New Entry Version
or
New Chronicle Entry
        ↓
Reverification where required
        ↓
Revalidation
        ↓
Publication decision
        ↓
Republish / Maintain / Withdraw
        ↓
Preserve prior material state
```

---

## Operational Dry Run

The first end-to-end Chronicle operational dry run used:

```text
SC-CERT-2026-0001
```

with simulated candidate:

```text
CHR-2026-0001
```

The dry run exercised:

```text
Occurrence identification
Preservation Eligibility
authoritative-reference collection
Event Type classification
Event-Type Profile selection
candidate identifier handling
Entry construction
Relationships
Sources / Evidence / Provenance
Verification
CHR-VAL Validation
Publication Gate
```

The overall result was:

```text
PASS
```

The dry run did not:

```text
assign or reserve CHR-2026-0001
create a production Chronicle Entry
publish a Chronicle Entry
change another Suite institution's authoritative record
```

No architecture redesign was required.

---

## First Production Application

The first production Chronicle Entry is:

```text
CHR-2026-0001
```

It preserves the qualifying historical Occurrence associated with:

```text
SC-CERT-2026-0001
```

and the materially relevant Registry Entry:

```text
SREG-2026-0001
```

The governing specialization is:

```text
Chronicle Base Schema v1.0.0
        +
Certification Event-Type Profile v1.0.0
```

Production review on August 22, 2026 completed:

```text
Preservation Eligibility:
ELIGIBLE

Formal Verification:
VERIFIED

Formal CHR-VAL Validation:
PASS

CHR-VAL-011 Publication Readiness:
PASS

Publication Gate:
APPROVED

Lifecycle State:
active

Publication State:
published

Published At:
2026-08-22T08:38:00-07:00
```

The canonical Entry is published at:

```text
/chronicle/entries/CHR-2026-0001/
```

---

## Production Package Convention

The first production Entry established the current reusable directory convention:

```text
/chronicle/entries/CHR-2026-0001/
│
├── index.html
├── record.json
├── README.md
├── CHR-2026-0001-v1-validation.md
└── CHR-2026-0001-v1-publication-gate.md
```

The first three files form the coordinated canonical Entry representation.

The Validation and Publication Gate files preserve the durable procedural review trail
for Entry Version 1 without becoming separate Chronicle objects.

Future production experience may justify additional supporting artifacts, but Chronicle
continues to apply:

> Minimum necessary structure first.

---

## Guiding Principles

> Events happen. Suite systems establish authority. Chronicle preserves qualifying historical memory.

> Reference does not transfer authority.

> Schema defines structure. Verification reviews representation. Validation tests conformance. Publication determines public production state.

> Correct forward. Preserve backward.

> Minimum necessary structure first.

> Operational implementation, publication, and completion — not rediscovery.

---

## Status

**Chronicle Entries are operational in production.**

The `/chronicle/entries/` area is Chronicle's canonical public production collection.

The Chronicle Base Schema, Certification Event-Type Profile, Identifier architecture,
Controlled Values, Relationship model, Provenance model, Verification architecture,
Validation Rules, Validation Sequence, Publication Gate, Correction rules, Versioning
model, and Entry Production Procedure are established.

The first end-to-end operational dry run completed with:

```text
PASS
```

The first canonical production Entry is:

```text
CHR-2026-0001
```

Current production state:

```text
Entry Version:
1

Lifecycle State:
active

Verification State:
verified

Formal CHR-VAL Validation:
PASS

CHR-VAL-011 Publication Readiness:
PASS

Publication Gate:
APPROVED

Publication State:
published

Published At:
2026-08-22T08:38:00-07:00
```

Chronicle's current work is post-publication maintenance, institutional-page reconciliation,
reciprocal Suite interoperability, and continued production use.
