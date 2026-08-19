# Chronicle Base Schema

## Purpose

The Chronicle Base Schema defines the universal structural contract for the canonical historical-preservation object of Satoshium Chronicle: the **Chronicle Entry**.

A Chronicle Entry represents one qualifying historical Occurrence that Chronicle has admitted for preservation.

The Base Schema defines only the fields and structures that apply across Chronicle Entries generally.

Event-Type-specific requirements belong in **Event-Type Profiles**.

The Base Schema does not duplicate or redefine authoritative objects owned by Certifier, Registry, Atlas, Anchor, Beacon, Attestor, Navigator, or another Suite institution.

The governing principle is:

> One canonical Entry. One universal Base Schema. Specialized requirements belong in Profiles.

---

# Canonical Object

The canonical Chronicle object is:

```text
Chronicle Entry
```

Conceptually:

```text
Occurrence
    ↓
Preservation Eligibility
    ↓
Chronicle Entry
```

The Occurrence is what happened.

The Chronicle Entry is Chronicle's structured historical-preservation record representing that qualifying Occurrence.

Chronicle does not create separate canonical objects for:

* certification history
* publication history
* milestone history
* governance history
* observation history
* registry history
* anchoring history
* attestation history

Those distinctions belong in **Event Type** and, where needed, an **Event-Type Profile**.

---

# Base Schema Boundary

The Chronicle Base Schema contains:

## Universal Required Fields

Fields every production Chronicle Entry must contain.

## Universal Conditional Fields

Fields supported by the Base Schema but required only when a defined condition applies.

## Profile-Specific Fields

Fields that do not belong in the Base Schema and must be introduced only through an Event-Type Profile.

This separation protects Chronicle from schema proliferation and prevents Event-Type-specific assumptions from becoming universal institutional requirements.

---

# Universal Required Fields

Every production Chronicle Entry must contain the following universal fields.

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

# Identity

## `entry_id`

Stable canonical identifier assigned to the Chronicle Entry.

**Requirement:** Required.

Canonical format:

```text
CHR-YYYY-NNNN
```

Example:

```text
CHR-2026-0001
```

Rules:

* `CHR` is the Chronicle Entry namespace.
* `YYYY` is the identifier assignment year.
* `NNNN` is the zero-padded annual sequence.
* The identifier is permanent.
* The identifier is never reused.
* The identifier does not encode Event Type, originating system, Verification State, Publication State, Lifecycle State, jurisdiction, or Version.
* Corrections and Entry Versions do not change `entry_id`.

Initial validation pattern:

```text
^CHR-[0-9]{4}-[0-9]{4}$
```

Pattern conformance alone does not establish issuance or uniqueness.

---

## `schema_id`

Stable identifier for the schema governing the record.

**Requirement:** Required.

Initial canonical value:

```text
chronicle-entry
```

This distinguishes schema identity from schema Version.

---

## `schema_version`

Version of the Chronicle Base Schema governing the Entry.

**Requirement:** Required.

Initial production convention:

```text
1.0.0
```

The exact Version may advance through later schema governance.

Every production Entry must remain associated with the schema Version that governed it.

---

## `entry_version`

Sequential Version of the Chronicle Entry.

**Requirement:** Required.

Initial representation:

```text
1
```

Later substantive states may become:

```text
2
3
4
```

Rules:

* Entry Version is distinct from Schema Version.
* Entry Version does not appear inside `entry_id`.
* Prior substantive Versions remain historically preserved.
* Material Corrections ordinarily create a new Entry Version.
* Editorial Updates may not require a new Entry Version.

---

# Event Representation

## `title`

Concise human-readable title describing the preserved Occurrence.

**Requirement:** Required.

The title should identify the historical subject without introducing unsupported interpretation.

Example:

```text
Creation of SC-CERT-2026-0001
```

The example is illustrative only; Certification-specific requirements belong in the Certification Event-Type Profile.

---

## `summary`

Brief factual summary of the preserved Occurrence.

**Requirement:** Required.

The summary should state what Chronicle is preserving in a concise reviewable form.

It should not replace:

* Historical Context
* Source Records
* Evidence
* Provenance
* Authoritative references

---

# Event Type

## `event_type`

Controlled classification identifying the type of Occurrence represented by the Entry.

**Requirement:** Required.

Values must come from the Chronicle Controlled Values Registry.

Initial approved Event Type values include:

```text
certification_created
certification_renewed
certification_suspended
certification_revoked
certification_expired
```

These values are initial production values, not the full future Chronicle taxonomy.

Rules:

* Event Type classifies the Occurrence.
* Event Type does not define canonical Entry identity.
* Event Type does not determine Preservation Eligibility by itself unless an explicit rule says otherwise.
* Event Type does not transfer authority.
* Correcting Event Type does not change `entry_id`.
* Event-Type-specific requirements belong in Profiles.

---

# Temporal Information

## `event_date`

Date or timestamp associated with the historical Occurrence.

**Requirement:** Required when determinable.

If exact temporal precision cannot be established, the production schema may later support an approved structured uncertainty representation.

Chronicle must preserve the distinction among:

```text
Event Date
Entry Creation Date
Source Publication Date
Source Retrieval Date
Publication Date
Correction Date
Version Effective Date
```

These dates must not be collapsed into one ambiguous timestamp.

---

## `entry_created_at`

Date and time Chronicle created the Entry.

**Requirement:** Required.

Recommended representation:

```text
RFC 3339 / ISO 8601 timestamp
```

Example:

```text
2026-09-01T12:30:00Z
```

This is Chronicle record time, not Event time.

---

# Historical Context

## `historical_context`

Structured or narrative context needed to understand the Occurrence within the historical record.

**Requirement:** Required.

Historical Context should:

* Explain the Occurrence in context.
* Remain distinguishable from authoritative Source material.
* Remain distinguishable from Evidence.
* Avoid unsupported causal claims.
* Avoid transferring authority to Chronicle.
* Disclose material uncertainty where relevant.
* Support later historical understanding.

Historical Context may include significance where useful, but a separate universal `historical_significance` field is not required by the Base Schema.

---

# Provenance

## `provenance`

Structured information explaining how the information used in the Entry originated, moved, was accessed, and entered Chronicle.

**Requirement:** Required.

Every production Entry must preserve, at minimum:

```text
origin
acquisition_method
retrieved_at
```

and, when available or applicable:

```text
source_reference
authoritative_record_reference
limitations
```

The universal minimum reflects the Chronicle Provenance Model:

```text
Origin
Acquisition / Access Method
Capture / Retrieval Date
Source or Authoritative Record Reference when available
Provenance Limitations when applicable
```

Provenance must not be reduced to a generic Source field.

Conceptually:

```text
Source = Where information came from.
Evidence = What bears on the Entry or claim.
Provenance = How that information entered Chronicle.
```

---

# Verification State

## `verification_state`

Current Chronicle Verification State for the Entry Version.

**Requirement:** Required.

Approved Controlled Values:

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

Verification reviews Chronicle's own historical representation.

Verification does not re-adjudicate authority belonging to another Suite institution.

---

# Lifecycle State

## `lifecycle_state`

Current Lifecycle State of the Chronicle Entry.

**Requirement:** Required.

Approved Controlled Values:

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

Lifecycle State describes the Entry's broader institutional journey.

It is distinct from:

* Verification State
* Publication State
* Entry Status

`Preserved` remains subject to production review for long-term necessity.

---

# Publication State

## `publication_state`

Current Publication State of the Chronicle Entry.

**Requirement:** Required.

Approved Controlled Values:

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

Publication State does not determine Lifecycle State or Verification State.

---

# Universal Conditional Fields

The following fields are supported by the Chronicle Base Schema but are not universally required.

They become required only when their defined condition applies.

---

## `event_type_profile`

Reference to the Event-Type Profile governing the Entry.

**Requirement:** Conditional.

Required when the Event Type has an approved Event-Type Profile.

Example:

```text
certification-event-profile
```

The Profile may add constraints and required fields.

It does not create a second canonical object.

---

## `originating_system`

System or institution that originated the authoritative action represented by the Occurrence when that distinction is required by an Event-Type Profile.

**Requirement:** Conditional.

This field is supported by the Base Schema but is not universally required.

Example:

```text
certifier
```

For certification-related Chronicle Entries, the Certification Event-Type Profile may require:

```text
originating_system: certifier
```

Rules:

* `originating_system` identifies the system responsible for the authoritative action represented by the Occurrence.
* It does not transfer authority to Chronicle.
* It should not be inferred when the originating institution cannot be established.
* It becomes Required only when an applicable Event-Type Profile says so.
* It does not appear inside `entry_id`.

---

## `authoritative_record_references`

Durable references to authoritative external or Suite-owned records associated with the represented Occurrence.

**Requirement:** Conditional.

Required when an authoritative record exists and is materially relevant to the Entry.

Examples may include:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Trust Statement
* Workflow Definition
* Atlas record

Rules:

* Chronicle references authoritative objects.
* Chronicle does not duplicate their internal schemas.
* Chronicle does not assume their authority.
* Reference does not transfer authority.

---

## `source_references`

References to Source Records or referenced external Sources used by the Entry.

**Requirement:** Conditional.

Required when Chronicle uses separately identified Sources beyond what is represented directly in Provenance or authoritative references.

Source requirements may be strengthened by an Event-Type Profile.

---

## `evidence_references`

References to Evidence Records or Evidence items bearing on the Entry or a claim.

**Requirement:** Conditional.

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Corroborate
* Contextualize
* Limit confidence

Evidence relationship semantics should remain explicit where implemented.

---

## `relationships`

Structured Relationships connecting the Entry to other Chronicle Entries, authoritative records, or supporting records.

**Requirement:** Conditional.

Approved general Relationship Types include:

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

Rules:

* Relationship does not transfer authority.
* Relationship does not imply causation unless explicitly governed.
* Direction must be preserved where applicable.
* Relationship Type remains distinct from Event Type.

---

## `correction_references`

References to Chronicle Correction Records affecting the Entry.

**Requirement:** Conditional.

Required when a formal Correction applies.

Correction lineage must preserve:

```text
Original information
Corrected information
Correction date
Reason
Affected fields
Resulting Version
```

---

## `prior_version_reference`

Reference to the immediately prior preserved Entry Version.

**Requirement:** Conditional.

Required for Entry Version 2 and later where prior Version linkage is represented directly in the Entry.

The canonical `entry_id` remains unchanged.

---

## `published_at`

Date and time the Entry Version was published.

**Requirement:** Conditional.

Required when `publication_state` is:

```text
published
```

or when publication history requires the timestamp to remain preserved.

---

## `updated_at`

Timestamp for the most recent non-historical maintenance action affecting the current representation.

**Requirement:** Conditional.

This field must not substitute for:

* Correction Date
* Version Effective Date
* Event Date
* Publication Date

---

## `limitations`

Material limitations affecting Chronicle's current historical representation.

**Requirement:** Conditional.

Required when material limitations exist.

Limitations may involve:

* Sources
* Evidence
* Provenance
* Dates
* Relationships
* Historical Context
* Availability
* Verification

Limitations must remain visible when material.

---

# Fields Not Universal to the Base Schema

The following concepts should not be universal required Base Schema fields.

---

## Preservation Eligibility Result

A production Entry exists because Preservation Eligibility has already been established.

Therefore the Base Schema does not universally require:

```text
preservation_eligibility
preservation_basis
```

Eligibility decision history may be preserved through operational procedure, review records, Historical Context, or a later dedicated structure if production use demonstrates the need.

---

## Historical Significance as a Standalone Required Field

Historical Significance remains central to Preservation Eligibility.

However, not every Entry requires a separate universal machine field named:

```text
historical_significance
```

Where material, significance may be preserved through Historical Context or a Profile-specific structure.

---

## Originating System as Universally Required

A Suite-originating system may be highly relevant for some Event Types.

It is not universal to every possible Chronicle Entry.

The Base Schema therefore supports:

```text
originating_system
```

as a **Conditional** field.

Example:

```text
originating_system: certifier
```

is expected to be required by the Certification Event-Type Profile rather than by the universal Base Schema.

---

## Generic Entry Status

The Base Schema does not presently require:

```text
entry_status
```

Chronicle already has:

```text
Lifecycle State
Verification State
Publication State
```

Entry Status remains under architectural review for redundancy.

If production use demonstrates a distinct need, it may later be added through schema evolution.

---

## Validation State

The Base Schema is designed to be validated.

It does not presently require a universal embedded:

```text
validation_state
```

The Validation Procedure should determine whether Validation results live:

* directly on the Entry,
* in publication metadata,
* in a Validation Record,
* or in another production artifact.

This preserves the distinction:

```text
Schema ≠ Verification ≠ Validation ≠ Publication
```

---

## Discovery Metadata

The Base Schema does not require:

```text
tags
jurisdiction
```

These may be added as Optional or Profile-specific fields where operationally justified.

Discovery metadata must not substitute for controlled classification.

---

# Event-Type Profiles

Event-Type Profiles specialize the Base Schema.

Conceptually:

```text
Chronicle Base Schema
        +
Event-Type Profile
        =
Specialized Chronicle Entry
```

A Profile may:

* Require additional fields.
* Make a conditional Base Schema field required.
* Restrict Event Type values.
* Require specific authoritative references.
* Require specific Source types.
* Require specific Evidence expectations.
* Strengthen Provenance requirements.
* Constrain Relationships.
* Add Validation rules.
* Add publication prerequisites.

A Profile may **not** remove universal Base Schema requirements.

The first production Profile is:

```text
Certification Event-Type Profile
```

---

# Base Schema Required / Conditional Summary

## Required

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

## Conditional

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

---

# Machine-Readable Structure

The production machine-readable implementation is published as:

```text
chronicle-base-schema.json
```

This Markdown document is the human-readable institutional specification.

Conceptually:

```text
chronicle-base-schema.md
→ Human-readable Base Schema specification

chronicle-base-schema.json
→ Machine-readable production contract
```

The machine-readable schema must not introduce fields or requirements that contradict this specification.

---

# Controlled Values

Production schemas must reference or implement approved Chronicle Controlled Values.

Schemas should not invent competing local vocabularies.

Current Base Schema-relevant Controlled Values include:

## Event Type

```text
certification_created
certification_renewed
certification_suspended
certification_revoked
certification_expired
```

## Verification State

```text
not_reviewed
in_review
verified
verified_with_limitations
unresolved
```

## Lifecycle State

```text
draft
active
superseded
withdrawn
preserved
```

## Publication State

```text
not_published
pending_publication
published
withdrawn_from_publication
```

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

Other Controlled Value sets are used by supporting schemas and Profiles.

---

# Schema Versioning

Every production Chronicle Entry must remain associated with the Base Schema Version that governed it.

Schema evolution should preserve:

* Schema identity
* Schema Version
* Compatibility classification
* Deprecation history
* Migration guidance
* Validation behavior
* Historical interpretability

Older Entries must remain understandable under the schema Version that originally governed them.

Schema evolution must not silently rewrite prior Chronicle Entry Versions.

---

# Compatibility

Schema changes should be classified according to operational effect.

## Backward-Compatible Change

Examples may include:

* Addition of a new Optional field
* Expansion of documentation
* Addition of a new Event-Type Profile
* Clarification that does not alter field meaning

## Potentially Breaking Change

Examples may include:

* Removing a field
* Renaming a required field
* Changing a field's meaning
* Changing a field type
* Making an Optional field Required
* Altering identifier semantics
* Altering Version semantics

Breaking changes should require:

* Explicit new Schema Version
* Migration guidance
* Historical preservation of prior Schema Versions
* Validation rules for older Entries

---

# Validation Expectations

A production Chronicle Entry should ultimately be validated against:

```text
Chronicle Base Schema
Applicable Event-Type Profile
Identifier rules
Controlled Values
Relationship rules
Provenance requirements
Authoritative-reference requirements
Versioning rules
Publication prerequisites
```

Validation should be machine-readable wherever practical.

Validation does not replace Verification.

A structurally valid Entry may still be:

```text
Verified with Limitations
Unresolved
```

A historically meaningful Entry may also fail structural Validation until corrected.

---

# Authority Boundary

The Chronicle Base Schema defines Chronicle-owned Entry structure only.

It does not redefine:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Discovery Metadata
* Trust Statement
* Workflow Definition
* Atlas record
* Other authoritative Suite objects

The governing rule remains:

> Reference does not transfer authority.

---

# Versioning and Corrections

The Base Schema supports the Chronicle Versioning Policy.

Rules:

* `entry_id` remains permanent.
* `entry_version` advances when substantive Entry state changes.
* Prior substantive Versions remain preserved.
* Formal Corrections remain traceable.
* No silent substantive rewrite is permitted.

Conceptually:

```text
CHR-2026-0001
Version 1
    ↓
Correction
    ↓
CHR-2026-0001
Version 2
```

A distinct qualifying Occurrence receives a new Chronicle Entry rather than a new Version of an unrelated Occurrence.

---

# Production Example

The following example demonstrates only universal Base Schema structure plus a small number of conditional references.

It does not define the Certification Event-Type Profile.

```yaml
entry_id: CHR-2026-0001
schema_id: chronicle-entry
schema_version: 1.0.0
entry_version: 1

title: Creation of SC-CERT-2026-0001

summary: >
  Satoshium Certifier created the authoritative Certification
  Package identified as SC-CERT-2026-0001 on July 5, 2026.

event_type: certification_created
event_date: 2026-07-05

historical_context: >
  Chronicle preserves this Occurrence as part of the documented
  institutional history of the Satoshium Suite.

provenance:
  origin: satoshium_certifier
  acquisition_method: direct_authoritative_record_reference
  retrieved_at: <TIMESTAMP>
  authoritative_record_reference: SC-CERT-2026-0001

verification_state: not_reviewed
lifecycle_state: draft
publication_state: not_published

entry_created_at: <TIMESTAMP>

event_type_profile: certification-event-profile

authoritative_record_references:
  - SC-CERT-2026-0001
```

Certification-specific requirements shown here must be governed by the Certification Event-Type Profile rather than by the Base Schema itself.

---

# Design Principles

## Canonical Object First

The schema centers on one canonical Chronicle Entry.

## Universal Means Universal

A field should not be Required by the Base Schema unless every production Chronicle Entry needs it.

## Profiles Specialize

Event-Type-specific requirements belong in Event-Type Profiles.

## Reference, Do Not Duplicate

Authoritative external objects remain referenced.

## Stable Identity

Entry identity remains permanent while Versions evolve.

## Preserve Prior States

Substantive historical states remain traceable.

## Controlled Meaning

Enumerated semantics use approved Controlled Values.

## Verification Is Distinct

Verification reviews Chronicle's representation.

## Validation Is Distinct

Validation checks conformance.

## Publication Is Distinct

Publication determines public-production state.

## Long-Term Interpretability

Older Entries and Schema Versions must remain understandable.

---

# Production Artifact Family

The Base Schema begins the Phase VII production schema family.

Current Base Schema artifacts:

```text
chronicle-base-schema.md
chronicle-base-schema.json
```

Current supporting human-readable schema specifications:

```text
source-record-schema.md
evidence-record-schema.md
correction-record-schema.md
```

Current Event-Type Profile work:

```text
Certification Event-Type Profile
```

The Certification Event-Type Profile specializes this Base Schema without altering its universal boundary.

---

# Guiding Principle

> The schema defines the fields. The Entry Model defines what the record must mean.

And operationally:

> One Entry. One Base Schema. Profiles specialize without multiplying canonical objects.

---

## Status

**Phase VII production Base Schema specification.**

This document defines the human-readable production boundary for the Chronicle Base Schema.

The canonical identifier format, initial Controlled Values, Lifecycle State, Verification State, Publication State, Versioning rules, Correction rules, Relationship Model, Provenance Model, and authority boundaries are incorporated.

The corresponding machine-readable implementation is published as:

```text
chronicle-base-schema.json
```

The Certification Event-Type Profile supplies Certification-specific requirements without altering the universal Base Schema boundary. The Base Schema now explicitly permits `originating_system` as a conditional extension point so applicable Profiles may require and constrain it without making it universal.
