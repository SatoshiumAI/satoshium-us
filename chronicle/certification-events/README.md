# Chronicle Certification Events

## Purpose

Chronicle Certification Events define the certification-related historical Occurrences that Satoshium Chronicle may preserve through canonical **Chronicle Entries**.

The **Certification Event-Type Profile** governs Chronicle Entries that represent qualifying certification-related Occurrences.

Chronicle does not create, replace, or reinterpret certifications.

Certifier remains authoritative for:

* Certification Packages
* Certification determinations
* Certification lifecycle actions
* Certification status

Chronicle owns the historical-preservation record representing the qualifying certification Occurrence.

The purpose of this specification is to explain how the Certification Event-Type Profile specializes the Chronicle Base Schema while preserving the authority boundaries established by the Satoshium Suite.

---

## Suite Alignment

Certification Events operate within the Satoshium Suite architecture.

They follow Suite-wide expectations for:

* Stable terminology
* Clear institutional authority boundaries
* Reference-based interoperability
* Structured records
* Durable references
* Repeatable procedures
* Schema discipline
* Version-aware preservation
* Validation-ready workflows

Chronicle references authoritative Suite objects rather than duplicating, replacing, or reinterpreting them.

---

## Core Institutional Distinction

The participating Suite systems retain independent authority over their own objects and actions.

### Certifier

Certifier is authoritative for:

* Certification Packages
* Certification determinations
* Certification lifecycle actions
* Certification status

### Registry

Registry is authoritative for:

* SREG Registry Entries
* Registration and cataloging
* Registry lifecycle state
* Registry record relationships

### Chronicle

Chronicle is authoritative for:

* Chronicle Entries
* Historical Context preserved by Chronicle
* Chronicle Relationships
* Chronicle Provenance
* Chronicle Verification
* Chronicle Corrections
* Chronicle Versions
* Chronicle Publication State

Chronicle preserves qualifying certification-related Occurrences without assuming the authority of Certifier or Registry.

The governing distinction is:

```text
Certifier
  owns the authoritative certification action and Certification Package.

Registry
  owns the related catalog record when an SREG exists.

Chronicle
  owns the historical-preservation record representing the qualifying Occurrence.
```

---

## Historical Model

A certification-related Occurrence is the historical action or state transition established by Certifier.

Chronicle may preserve that Occurrence through a Chronicle Entry when it satisfies Chronicle Preservation Eligibility.

A certification-related Chronicle Entry should make clear:

* What happened
* When it happened
* Which system originated the authoritative action
* Which authoritative Certification Package establishes the Occurrence
* Which related Suite records provide context
* What Historical Context Chronicle preserves

The Occurrence itself is not a Chronicle-owned object.

The Chronicle Entry is Chronicle's canonical historical-preservation record representing that Occurrence.

Conceptually:

```text
Certification Occurrence
        ↓
Preservation Eligibility
        ↓
Chronicle Entry
        +
Certification Event-Type Profile
```

---

## Certification Event-Type Profile

The **Certification Event-Type Profile** is Chronicle's first production Event-Type Profile.

It specializes the Chronicle Base Schema for certification-related Occurrences.

Conceptually:

```text
Chronicle Base Schema
        +
Certification Event-Type Profile
        =
Certification-related Chronicle Entry
```

The Profile may:

* Restrict Event Type to approved certification Event Types
* Require `event_type_profile`
* Require a determinable certification Event Date / time
* Require Certifier as the originating system
* Require an authoritative Certification Package reference
* Strengthen certification-specific Provenance requirements
* Require certification-specific Historical Context
* Require or constrain Relationships
* Require a related Registry reference when a corresponding SREG exists and is materially relevant
* Add certification-specific Validation requirements

The Profile does **not** create a separate canonical Certification Event object.

The canonical object remains the Chronicle Entry.

---

## Certification Event Types

The Certification Event-Type Profile applies to the currently approved certification-related Event Types:

* Certification Created
* Certification Renewed
* Certification Suspended
* Certification Revoked
* Certification Expired

Machine-readable values:

```text
certification_created
certification_renewed
certification_suspended
certification_revoked
certification_expired
```

Additional certification Event Types may be introduced only when they correspond to authoritative Certifier actions or states and are approved through Chronicle Event Type and Controlled Values governance.

Anchor, Attestor, Beacon, Registry, or other Suite-system activity should not be reclassified as certification authority.

Those Occurrences should use their own Event-Type Profiles where appropriate.

---

## Certification Created

A Chronicle Entry classified as **Certification Created** preserves the historical Occurrence in which Certifier created a new authoritative Certification Package.

Chronicle references the Certification Package and preserves Historical Context surrounding its creation.

Chronicle does not recreate or independently determine the certification.

---

## Certification Renewed

A Chronicle Entry classified as **Certification Renewed** preserves the historical Occurrence in which Certifier authoritatively renewed a certification according to the applicable certification rules and lifecycle model.

Chronicle preserves the Occurrence and references the authoritative certification record.

---

## Certification Suspended

A Chronicle Entry classified as **Certification Suspended** preserves the historical Occurrence in which Certifier authoritatively placed a certification into a suspended state.

Chronicle does not independently determine or impose suspension.

---

## Certification Revoked

A Chronicle Entry classified as **Certification Revoked** preserves the historical Occurrence in which Certifier authoritatively revoked a certification.

Chronicle preserves the Occurrence but does not create or reinterpret revocation authority.

---

## Certification Expired

A Chronicle Entry classified as **Certification Expired** preserves the historical Occurrence in which a certification reached an expired state under the applicable Certifier rules and lifecycle model.

Chronicle preserves the historical transition without independently determining expiration.

---

## Profile Requirements

The Certification Event-Type Profile inherits all universal Chronicle Base Schema requirements.

Universal Base Schema fields include:

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

The Profile then adds or strengthens certification-specific requirements.

Expected certification-specific requirements include:

```text
event_type_profile
originating_system
authoritative certification reference
certification-specific Historical Context
certification-specific Provenance
```

A related Registry reference becomes required when:

```text
A corresponding SREG exists
        +
That SREG is materially relevant to the Chronicle Entry
```

The Profile should not require a Registry identifier merely because the Event Type is certification-related.

---

## Authoritative Certification Reference

Every Chronicle Entry governed by the Certification Event-Type Profile should reference the authoritative Certification Package associated with the represented Occurrence.

The authoritative reference should identify the Certifier-owned record without copying its internal contents.

Conceptually:

```text
Chronicle Entry
        ↓
references
        ↓
Certification Package
```

The Certification Package remains authoritative within Certifier.

Chronicle preserves the historical relationship to that Package.

---

## Originating System

For the Certification Event-Type Profile:

```text
originating_system: certifier
```

is a certification-specific requirement.

This field is not universal to the Chronicle Base Schema because not every possible Chronicle Occurrence originates within a Suite system.

The Certification Event-Type Profile supplies that specialization.

---

## Event Date / Time

Certification Event Date / time should represent the date or timestamp of the authoritative Certifier Occurrence.

The Profile should require a determinable temporal value for normal production certification Entries.

Chronicle must preserve the distinction among:

```text
Certification Event Date
Chronicle Entry Creation Date
Source Retrieval Date
Chronicle Publication Date
Correction Date
Version Date
```

These timestamps must not be collapsed into one ambiguous field.

---

## Historical Context

Historical Context should explain the certification Occurrence within Satoshium institutional history.

It may describe:

* Why the Occurrence matters historically
* Its relationship to prior or later certification Occurrences
* Its place in Suite institutional development
* Related Registry history
* Relevant continuity or milestone context
* Material uncertainty or limitations

Historical Context must remain distinguishable from the Certification Package itself.

Chronicle should not restate Certifier findings merely to make the Entry appear more complete.

---

## Provenance

Certification-related Chronicle Entries inherit the Chronicle Provenance requirement.

The Profile may strengthen Provenance by requiring clear connection to:

```text
Certifier
        ↓
Authoritative Certification Package
        ↓
Chronicle acquisition / access method
        ↓
Chronicle Entry
```

At minimum, production Provenance should preserve:

* Origin
* Acquisition / Access Method
* Retrieval / Capture Date
* Authoritative Certification Package reference
* Material Provenance limitations where applicable

---

## Record References

Certification-related Chronicle Entries should reference the authoritative Certification Package produced by Certifier.

They may also reference related Suite or public records, including:

* SREG Registry Entries
* Receipts
* Public certification pages
* Attestations
* Integrity References
* Public archival references
* Other supporting Suite records

Referenced records remain authoritative within the systems that created them.

Chronicle uses these references to preserve context, Relationships, Provenance, and historical continuity.

---

## Relationship to Registry

Registry creates and maintains independent SREG Registry Entries that catalog records over time.

Chronicle may reference a Registry Entry when preserving a certification-related Occurrence.

Registry remains authoritative for:

* The SREG
* Registry metadata
* Registry lifecycle state
* Registry catalog relationships

Chronicle does not treat the Registry Entry as a substitute for the authoritative Certification Package.

The governing distinction is:

```text
Certifier owns the certification record.

Registry owns the catalog record.

Chronicle owns the historical-preservation record.
```

---

## What the Profile Does Not Duplicate

The Certification Event-Type Profile does not reproduce Certification Package contents.

Chronicle should not copy into the Profile or Chronicle Entry merely for completeness:

* Certification findings
* Certification determination logic
* Certification evidence body
* Certification Package schema
* Certifier lifecycle mechanics
* Certifier-owned validation structures
* Certifier-owned status determination logic

Those remain within Certifier.

Chronicle preserves references and historical meaning.

---

## Preservation Eligibility

Not every certification-related action automatically requires Chronicle preservation.

A certification-related Occurrence should be preserved only when it satisfies Chronicle Preservation Eligibility rules.

Preservation Eligibility is distinct from:

* Certification authority
* Evidence sufficiency
* Verification State
* Validation
* Publication

Historical Significance may support Preservation Eligibility but does not replace the formal eligibility mechanism.

---

## Verification

Chronicle Verification reviews Chronicle's own historical representation and references.

Verification may include:

* Confirmation that the referenced Certification Package exists
* Chronicle identifier consistency
* Event Date consistency
* Certifier-origin consistency
* Registry-reference consistency where applicable
* Relationship integrity
* Provenance completeness
* Supporting-record availability
* Material limitations

Chronicle Verification does not re-adjudicate the certification determination made by Certifier.

---

## Validation

The Certification Event-Type Profile should be machine-readable so that a production certification-related Chronicle Entry can ultimately be validated against:

```text
Chronicle Base Schema
        +
Certification Event-Type Profile
        +
Identifier Rules
        +
Controlled Values
        +
Relationship Rules
        +
Provenance Requirements
```

Validation confirms conformance.

Validation does not replace Chronicle Verification.

---

## Corrections and Versioning

If Chronicle later discovers an error in its own representation of a certification Occurrence, Chronicle may correct and Version its Chronicle Entry according to Chronicle Correction and Versioning rules.

Chronicle may correct:

* Event metadata
* References
* Historical Context
* Relationships
* Provenance
* Supporting information

Chronicle does not correct the underlying Certification Package.

If Certifier later performs a distinct certification action, Chronicle should determine whether that action constitutes a new qualifying Occurrence.

Conceptually:

```text
Chronicle's earlier representation was wrong
        ↓
Correction / New Version

Distinct later Certifier action occurred
        ↓
New Occurrence
        ↓
Preservation Eligibility
        ↓
New Chronicle Entry
```

---

## Public Role of This Directory

The `/chronicle/certification-events/` directory provides the public institutional explanation of Chronicle's Certification Event-Type Profile.

The formal Profile artifacts belong within the Chronicle schema architecture.

Expected production artifacts:

```text
/chronicle/schemas/certification-event-profile.md
/chronicle/schemas/certification-event-profile.json
```

The public Certification Events page explains the Profile.

The schema artifacts define and enforce it.

---

## Future Development

Remaining Certification Event-Type Profile work may include:

* Final human-readable Profile specification
* Machine-readable Profile implementation
* Certification-specific Validation testing
* First production Chronicle Entry
* Public Chronicle Entry discovery
* Timeline integration
* Additional certification Event Types where genuinely required

Future development should preserve the Suite authority boundaries established here.

---

## Guiding Principle

> Certifier establishes certification authority. Chronicle preserves the historical record of what occurred.

And operationally:

> Base Schema defines the Chronicle Entry. The Certification Event-Type Profile supplies only the certification-specific requirements.

---

## Status

**Phase VII Certification Event-Type Profile architecture — active production implementation.**

This README is reconciled with the current Chronicle Entry Model, Base Schema, Event Types, Preservation Eligibility, Identifiers, Controlled Values, Relationships, Provenance, Verification, Lifecycle, Versioning, Corrections, and Suite authority boundaries.

The Certification Event-Type Profile is no longer treated as a future conceptual layer.

The remaining implementation work is to publish the formal human-readable Profile, create its machine-readable JSON Schema implementation, validate that Profile architecture, and then apply it to the first production certification-related Chronicle Entry.
