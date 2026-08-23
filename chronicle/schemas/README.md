# Chronicle Schemas

## Purpose

Satoshium Chronicle Schemas define the structural and machine-readable contracts used to represent canonical Chronicle Entries and supporting Chronicle-owned records.

Schemas provide the structural language required for:

* Consistency
* Validation
* Interoperability
* Provenance
* Traceability
* Versioning
* Publication readiness
* Long-term historical preservation

The canonical historical-preservation object of Chronicle is the **Chronicle Entry**.

Chronicle schemas exist to support that object and the supporting records required to preserve its Sources, Evidence, Provenance, Relationships, Verification, Corrections, Versions, Publication state, and historical lineage.

Schemas organize Chronicle-owned information.

They do not determine historical conclusions or absorb authority belonging to another Satoshium Suite institution.

---

# Production Schema Architecture

Phase VII — Production Schemas is complete.

Chronicle's Base Schema and first Event-Type Profile have now moved beyond schema
definition and have been exercised through the first canonical production Entry.

The core production schema artifacts are:

```text
chronicle-base-schema.md
chronicle-base-schema.json
```

Together they define the canonical Chronicle Base Schema.

Conceptually:

```text
chronicle-base-schema.md
→ Human-readable production specification

chronicle-base-schema.json
→ Machine-readable production contract
```

The machine-readable schema must remain consistent with the human-readable institutional specification.

---

# Suite Alignment

Chronicle Schemas operate within the broader Satoshium Suite architecture.

They should align with Suite-wide expectations for:

* Stable objects
* Canonical terminology
* Required and conditional fields
* Controlled Values
* Durable identifiers and references
* Reference-based interoperability
* Provenance and traceability
* Validation-ready records
* Schema Versioning and evolution
* Preservation of prior schema states
* Documented procedures
* Clear institutional authority boundaries

Chronicle does not redefine or duplicate authoritative objects owned by:

* Certifier
* Registry
* Atlas
* Anchor
* Beacon
* Attestor
* Navigator
* Other Suite institutions

Reference does not transfer authority.

---

# Why Schemas Matter

Historical preservation becomes more reliable when records follow explicit, stable structures.

Without consistent schemas:

* Information becomes difficult to compare.
* Relationships become ambiguous.
* Provenance becomes harder to reconstruct.
* Verification becomes inconsistent.
* Validation becomes unreliable.
* Cross-system references become fragile.
* Corrections and Version lineage become difficult to preserve.
* Historical records become harder to interpret across time and technology.

Schemas provide the structural foundation required to keep Chronicle Entries durable, reviewable, machine-readable, interoperable, and historically reconstructable.

---

# Canonical Schema Model

Chronicle uses one canonical historical-preservation object:

> Chronicle Entry

The structural model centers on one **Chronicle Base Schema**.

Conceptually:

```text
Occurrence
    ↓
Preservation Eligibility
    ↓
Chronicle Base Schema
    +
Applicable Event-Type Profile
    ↓
Chronicle Entry
```

Supporting Chronicle schemas exist only where a distinct Chronicle-owned operational function requires separate structure.

They do not create competing canonical Chronicle objects.

---

# Chronicle Base Schema

The **Chronicle Base Schema** defines the universal structure shared by all production Chronicle Entries.

Human-readable artifact:

```text
chronicle-base-schema.md
```

Machine-readable artifact:

```text
chronicle-base-schema.json
```

The Base Schema follows one governing rule:

> Universal means universal.

A field should not be Required by the Base Schema unless every production Chronicle Entry needs it.

---

# Universal Base Schema Structure

The production Base Schema currently requires:

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

These fields define the minimum canonical Chronicle Entry.

---

# Conditional Base Schema Structure

The Base Schema also supports conditional fields that become required only when a defined condition applies.

Current conditional fields include:

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

An Event-Type Profile may strengthen these requirements.

A Profile may not remove universal Base Schema requirements.

---

# Concepts Intentionally Not Universal

The production Base Schema does not universally require:

```text
preservation_eligibility
preservation_basis
historical_significance
originating_system
entry_status
validation_state
tags
jurisdiction
```

These concepts remain available through:

* pre-Entry procedure
* Historical Context
* Event-Type Profiles
* supporting records
* future schema evolution

where operational need justifies them.

---

# Preservation Eligibility and the Base Schema

Preservation Eligibility occurs before ordinary production Entry creation.

It asks:

> Should Chronicle preserve this Occurrence?

A production Chronicle Entry exists because the Occurrence has already passed that institutional admission decision.

Therefore Preservation Eligibility is not required as an ordinary universal field inside every production Entry.

Eligibility history may remain preserved through procedure, review artifacts, Historical Context, or a future dedicated record where justified.

---

# Event-Type Profiles

Event-Type Profiles specialize the Base Schema for specific classes of preserved Occurrences.

Conceptually:

```text
Chronicle Base Schema
        +
Event-Type Profile
        =
Specialized Chronicle Entry
```

A Profile may:

* Require additional fields
* Make conditional Base Schema fields Required
* Restrict Event Type values
* Require authoritative references
* Require Source or Evidence patterns
* Strengthen Provenance requirements
* Constrain Relationships
* Add Validation rules
* Add publication prerequisites

An Event-Type Profile does not create a second canonical Chronicle object.

---

# First Production Event-Type Profile

The first production Event-Type Profile is:

```text
Certification Event-Type Profile
```

Production Profile directory:

```text
/chronicle/schemas/certification-event-profile/
```

Profile package:

```text
certification-event-profile/
├── index.html
├── certification-event-profile.md
└── certification-event-profile.json
```

The Profile requires or strengthens:

* Approved Certification Event Types
* `event_type_profile = certification-event-profile`
* `originating_system = certifier`
* Non-null certification Event Date / time
* Authoritative Certification Package reference
* Certification-specific Provenance
* Certification-specific Historical Context
* Related SREG reference where a corresponding Registry Entry exists and is materially relevant
* Certification-specific Validation requirements

These requirements belong in the Profile rather than the universal Base Schema.

Conceptually:

```text
Chronicle Base Schema
        +
Certification Event-Type Profile
        =
Certification-related Chronicle Entry
```

---

# Controlled Values

Controlled Values are governed separately from structural schema definitions where practical.

Production schemas should use approved Chronicle vocabularies rather than inventing local enumerations.

Current Base-Schema-relevant Controlled Values include:

---

## Event Type

```text
certification_created
certification_renewed
certification_suspended
certification_revoked
certification_expired
```

---

## Verification State

```text
not_reviewed
in_review
verified
verified_with_limitations
unresolved
```

Human-readable labels:

```text
Not Reviewed
In Review
Verified
Verified with Limitations
Unresolved
```

---

## Lifecycle State

```text
draft
active
superseded
withdrawn
preserved
```

Human-readable labels:

```text
Draft
Active
Superseded
Withdrawn
Preserved
```

---

## Publication State

```text
not_published
pending_publication
published
withdrawn_from_publication
```

Human-readable labels:

```text
Not Published
Pending Publication
Published
Withdrawn from Publication
```

---

## Relationship Type

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

Supporting schemas may use additional Controlled Value sets.

---

# No Generic Entry Status

Chronicle does not use a generic `entry_status` as a canonical production field.

The production architecture keeps these systems distinct:

```text
Lifecycle State
Verification State
Publication State
```

A generic Entry Status would duplicate or blur those defined meanings.

---

# Validation Result

The Base Schema is designed to be Validated, but does not embed a universal:

```text
validation_state
```

or:

```text
validation_result
```

Production Chronicle Validation produces `PASS / FAIL` for the exact Entry Version
evaluated. Full Validation detail is preserved through a Version-specific Validation
artifact rather than promoted into a universal Base Schema field.

```text
Schema ≠ Verification ≠ Validation ≠ Publication
```

---

# Identifier Architecture

The canonical Chronicle Entry identifier is:

```text
CHR-YYYY-NNNN
```

Example:

```text
CHR-2026-0001
```

Rules include:

* `CHR` identifies the Chronicle Entry namespace.
* `YYYY` represents identifier assignment year.
* `NNNN` is the annual zero-padded sequence.
* Identifiers are permanent.
* Identifiers are never reused.
* Entry Versions do not change the identifier.
* Event Type is not encoded in the identifier.

Initial validation pattern:

```text
^CHR-[0-9]{4}-[0-9]{4}$
```

Pattern validation does not by itself establish issuance or uniqueness.

---

# Schema Identity

Production Chronicle Entries distinguish:

```text
schema_id
schema_version
entry_version
```

These answer different questions.

## `schema_id`

Which schema governs this record?

Initial value:

```text
chronicle-entry
```

## `schema_version`

Which Version of that schema governs the record?

Initial value:

```text
1.0.0
```

## `entry_version`

Which preserved state of this Chronicle Entry is represented?

Example:

```text
1
```

These concepts must not be collapsed.

---

# Current Schema Architecture

The current Chronicle schema family includes:

---

## Chronicle Base Schema

Files:

```text
chronicle-base-schema.md
chronicle-base-schema.json
```

Status:

```text
Phase VII production Base Schema
```

The Markdown file defines the institutional specification.

The JSON file defines the machine-readable contract.

---

## Source Record Schema

File:

```text
source-record-schema.md
```

Role:

Supporting Chronicle-owned structure for documenting Source identity, attribution, Provenance, archival context, limitations, and relationships.

Status:

```text
Phase VII reconciled supporting schema specification
```

The Source Record Schema is aligned to the current Source architecture, approved Source Types, Provenance Model, Versioning, Corrections, and authority boundaries.

---

## Evidence Record Schema

File:

```text
evidence-record-schema.md
```

Role:

Supporting Chronicle-owned structure for representing Evidence bearing on Chronicle Entries or claims.

Status:

```text
Phase VII reconciled supporting schema specification
```

The Evidence Record Schema is aligned to the approved Evidence Types, Provenance Model, Entry / claim linkage, Versioning, Corrections, limitations, and integrity architecture while Evidence Relationship values remain intentionally provisional.

---

## Correction Record Schema

File:

```text
correction-record-schema.md
```

Role:

Supporting Chronicle-owned structure for documenting Corrections to Chronicle-owned records.

Status:

```text
Phase VII reconciled supporting schema specification
```

The Correction Record Schema is aligned to the Versioning Policy, approved Correction Types, authority boundaries, and the mandatory Correction lineage minimum.

---

# Supporting Schema Categories

The current human-readable supporting specifications are:

```text
source-record-schema.md
evidence-record-schema.md
correction-record-schema.md
```

They define possible Chronicle-owned supporting records **only when independent
structure is operationally justified**.

`CHR-2026-0001` required none of those separate supporting records. Direct references,
Entry-level Provenance, Relationships, and Version-specific procedural artifacts were
sufficient.

Additional supporting schemas must not be created merely for architectural symmetry.
Schema and object proliferation should be avoided.

---

# Source Record Schema Direction

The Source Record Schema should align with the approved Source Type vocabulary:

```text
Authoritative Record
Institutional Document
Web Page
Repository Record
Dataset
Archive
Statement
Other
```

Source Role remains a candidate future Controlled Value set.

The Source schema should preserve:

* identity
* attribution
* Source Type
* location / stable reference
* relevant dates
* Provenance
* limitations
* archival context
* relationships
* Version lineage

---

# Evidence Record Schema Direction

The Evidence Record Schema should align with the approved Evidence Type vocabulary:

```text
Authoritative Evidence
Documentary Evidence
Repository Evidence
Archival Evidence
Machine-Generated Evidence
Testimonial Evidence
Contextual Evidence
Other
```

Evidence Relationship remains a candidate future Controlled Value set.

Candidate semantics include:

```text
Supports
Challenges
Contradicts
Clarifies
Corroborates
Contextualizes
Limits Confidence
```

Evidence Type and Evidence Relationship must remain distinct.

---

# Correction Record Schema Direction

The Correction Record Schema should align with approved Correction Types:

```text
Typographical
Metadata
Contextual
Relationship
Provenance
Evidence
Classification
Substantive
```

Every formal Correction should preserve:

```text
Original information
Corrected information
Correction date
Reason
Affected fields
Resulting Version
```

No silent substantive historical rewriting is permitted.

---

# Required, Conditional, and Optional Fields

Chronicle schemas should distinguish explicitly among:

## Required

Fields that must be present for a record to conform.

## Conditional

Fields required when a defined condition applies.

## Optional

Fields that improve context or discovery but are not institutionally necessary in all records.

These designations should be represented both in human-readable specifications and machine-readable schemas.

---

# Relationship Between Schemas

Chronicle schemas form a layered architecture.

Conceptually:

```text
Chronicle Base Schema
        ↓
Chronicle Entry
        ├── Source Records
        ├── Evidence Records
        ├── Correction Records
        └── Other supporting structures where justified
```

Event-Type Profiles specialize the Base Schema.

Supporting schemas describe distinct Chronicle-owned supporting functions.

They do not become canonical historical objects.

---

# Reference-Based Interoperability

Chronicle schemas support durable references to authoritative objects maintained by other Suite institutions.

Examples include:

* Certification Packages
* SREG Registry Entries
* Integrity References
* Discovery Signals
* Discovery Metadata
* Trust Statements
* Workflow Definitions
* Atlas records

Chronicle does not copy those objects' internal schema structures into Chronicle merely to make them usable.

The governing rule remains:

> Reference does not transfer authority.

---

# Schema, Verification, Validation, and Publication

These functions remain distinct.

## Schema

Defines structure.

## Verification

Reviews Chronicle's historical representation.

## Validation

Determines structural and procedural conformance.

## Publication

Determines whether the record enters public production use.

Conceptually:

```text
Schema ≠ Verification ≠ Validation ≠ Publication
```

---

# Schema Versioning

Every production Chronicle record should remain associated with the Schema Version that governed it.

Schema evolution should define:

* Schema identity
* Version number
* Compatibility classification
* Breaking changes
* Deprecation
* Migration
* Validation behavior
* Historical preservation
* Prior-Version documentation

Older Chronicle records must remain interpretable under the Schema Version that originally governed them.

---

# Compatibility

Schema changes should be classified according to their operational effect.

## Backward-Compatible Changes

Potential examples:

* New Optional field
* Documentation clarification
* New Event-Type Profile
* Expanded non-breaking metadata
* New allowed controlled value where semantics remain compatible

## Breaking Changes

Potential examples:

* Removing a Required field
* Renaming a Required field
* Changing field meaning
* Changing field type
* Making an Optional field Required
* Changing identifier semantics
* Changing Version semantics

Breaking changes require an explicit Schema Version change and migration guidance.

---

# Record Versioning vs. Schema Versioning

These concepts are separate.

```text
schema_version
```

identifies the structural specification.

```text
entry_version
```

identifies the preserved state of a Chronicle Entry.

A Chronicle Entry may advance to a new Entry Version without changing Schema Version.

A Schema may advance while older Entries remain preserved under an earlier Schema Version.

---

# Validation Expectations

Production Chronicle Entries are Validated against:

* Chronicle Base Schema
* Applicable Event-Type Profile
* Identifier rules
* Required and Conditional fields
* Controlled Values
* Relationship rules
* Provenance requirements
* Authoritative-reference requirements
* Versioning rules
* Publication prerequisites

Validation should be machine-readable wherever practical.

---

# Machine-Readable Specifications

Chronicle Phase VII now includes machine-readable production implementations for:

```text
chronicle-base-schema.json

certification-event-profile/
└── certification-event-profile.json
```

The Certification Event-Type Profile composes with the Chronicle Base Schema rather than duplicating it.

Conceptually:

```text
chronicle-base-schema.json
        +
certification-event-profile.json
        =
Certification-related Chronicle Entry Validation
```

Future machine-readable supporting schemas may include:

```text
source-record-schema.json
evidence-record-schema.json
correction-record-schema.json
```

Those supporting JSON schemas should be created only after their human-readable specifications are exercised against real production supporting records.

---

# Current Files

The current `/chronicle/schemas/` family is:

```text
README.md
index.html

chronicle-base-schema.md
chronicle-base-schema.json
chronicle-entry-schema.md

certification-event-profile/
├── index.html
├── certification-event-profile.md
└── certification-event-profile.json

source-record-schema.md
evidence-record-schema.md
correction-record-schema.md
```

The former `chronicle-entry-schema.md` filename is retained only as a historical compatibility pointer.

The canonical Base Schema remains:

```text
chronicle-base-schema.md
chronicle-base-schema.json
```

The deprecated compatibility file must not contain a second competing Base Schema.

---

# Production Sequence Proven

The schema architecture has now completed the transition from definition to production use:

```text
Chronicle Base Schema
        ↓
Certification Event-Type Profile
        ↓
Phase VII Two-Layer Validation PASS
        ↓
Chronicle Validation Architecture
        ↓
Operational Dry Run PASS
        ↓
CHR-2026-0001
        ↓
Production Validation PASS
        ↓
Publication Gate APPROVED
        ↓
Published
```

The supporting Source, Evidence, and Correction specifications remain available for
future use, but they are not mandatory layers in every Entry package.

---

# Design Principles

## Canonical Object First

Schema architecture centers on Chronicle Entry.

## Universal Means Universal

The Base Schema contains only universal Entry requirements.

## Profiles Specialize

Event-Type-specific requirements belong in Event-Type Profiles.

## Supporting Schemas Stay Supporting

Source, Evidence, and Correction Records do not become canonical historical objects.

## Controlled Meaning

Enumerated semantics use approved Controlled Values.

## Reference, Do Not Duplicate

External authoritative objects remain referenced.

## Stable Identity

Entry identity remains permanent across Versions.

## Preserve Prior States

Substantive record states and schema states remain historically interpretable.

## Validation Readiness

Schemas should support machine validation.

## Long-Term Compatibility

Older Chronicle records must remain readable and understandable.

---

# Current Production Position

Chronicle's core schema stack is operational.

`CHR-2026-0001` demonstrated that the Base Schema and Certification Event-Type Profile
can govern a real published Chronicle Entry without requiring separate Source, Evidence,
or Correction objects.

Supporting JSON schemas remain intentionally deferred:

```text
source-record-schema.json
evidence-record-schema.json
correction-record-schema.json
```

They should be created only after real production supporting records demonstrate a
stable machine-readable need.

---

# First Production Schema Precedent

The first canonical production Entry established the following schema precedent:

```text
CHR-2026-0001
Base Schema 1.0.0
Certification Event-Type Profile 1.0.0
Verification: verified
Validation: PASS
Publication Gate: APPROVED
Publication State: published
```

Its five-file production package used:

```text
index.html
record.json
README.md
CHR-2026-0001-v1-validation.md
CHR-2026-0001-v1-publication-gate.md
```

The Validation and Publication Gate files are durable Entry-Version procedural artifacts,
not new canonical objects.

---

# Guiding Principle

> The schema defines the fields. The Entry Model defines what the record must mean.

And operationally:

> One Entry. One Base Schema. Profiles specialize without multiplying canonical objects.

---

## Status

**Operational Chronicle Schemas specification.**

The Chronicle Base Schema exists in both human-readable and machine-readable production forms:

```text
chronicle-base-schema.md
chronicle-base-schema.json
```

Chronicle's first production Event-Type Profile is published through:

```text
/chronicle/schemas/certification-event-profile/
├── index.html
├── certification-event-profile.md
└── certification-event-profile.json
```

The Source Record Schema, Evidence Record Schema, and Correction Record Schema are Phase VII reconciled Chronicle-owned supporting schema specifications.

Two-layer Profile Validation, Chronicle Validation, the Production Procedure, and the first production Chronicle Entry are complete.

The schema family remains governed by explicit compatibility, Versioning, Validation, Controlled Values, authority boundaries, and preservation of prior states.
