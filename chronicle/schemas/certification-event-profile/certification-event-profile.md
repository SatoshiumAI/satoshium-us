# Chronicle Certification Event-Type Profile

## Purpose

The Chronicle Certification Event-Type Profile defines the certification-specific requirements applied to Satoshium Chronicle Entries that preserve qualifying certification-related Occurrences.

The Profile specializes the Chronicle Base Schema.

It does not create a separate canonical object.

The canonical Chronicle object remains:

```text
Chronicle Entry
```

Conceptually:

```text
Chronicle Base Schema
        +
Certification Event-Type Profile
        =
Certification-related Chronicle Entry
```

The governing principle is:

> Certifier establishes certification authority. Chronicle preserves the historical record of what occurred.

---

# Institutional Boundary

The Certification Event-Type Profile preserves the authority boundaries of the Satoshium Suite.

## Certifier

Certifier remains authoritative for:

* Certification Packages
* Certification determinations
* Certification lifecycle actions
* Certification status
* Certification evidence and findings
* Certification-specific validation and procedural requirements

## Registry

Registry remains authoritative for:

* SREG Registry Entries
* Registration and cataloging
* Registry metadata
* Registry lifecycle state
* Registry record relationships

## Chronicle

Chronicle is authoritative for:

* Chronicle Entries
* Chronicle Historical Context
* Chronicle Provenance
* Chronicle Relationships
* Chronicle Verification
* Chronicle Corrections
* Chronicle Versions
* Chronicle Publication State

Chronicle owns the historical-preservation record representing the qualifying certification Occurrence.

Chronicle does not own the certification action itself.

---

# Profile Identity

The Profile identifier is:

```text
certification-event-profile
```

Initial Profile Version:

```text
1.0.0
```

Canonical Profile directory:

```text
https://satoshium.us/chronicle/schemas/certification-event-profile/
```

Production artifact family:

```text
/chronicle/schemas/certification-event-profile/
├── index.html
├── certification-event-profile.md
└── certification-event-profile.json
```

The Profile should be represented in production Chronicle Entries through:

```text
event_type_profile: certification-event-profile
```

The Profile Version should remain governed separately from:

```text
Chronicle Base Schema Version
Chronicle Entry Version
```

---

# Governing Base Schema

This Profile applies to Chronicle Entries governed by:

```text
schema_id: chronicle-entry
schema_version: 1.0.0
```

The human-readable Base Schema is:

```text
/chronicle/schemas/chronicle-base-schema.md
```

The machine-readable Base Schema is:

```text
/chronicle/schemas/chronicle-base-schema.json
```

The Profile may strengthen or specialize Base Schema requirements.

It may not remove universal Base Schema requirements.

---

# Applicable Event Types

The Certification Event-Type Profile applies only to the currently approved certification-related Chronicle Event Types.

Human-readable values:

```text
Certification Created
Certification Renewed
Certification Suspended
Certification Revoked
Certification Expired
```

Machine-readable values:

```text
certification_created
certification_renewed
certification_suspended
certification_revoked
certification_expired
```

Additional certification Event Types must not be added directly to this Profile without prior approval through Chronicle Event Type and Controlled Values governance.

---

# Profile Required Fields

A Chronicle Entry governed by this Profile must satisfy every universal Chronicle Base Schema requirement.

In addition, the Profile requires:

```text
event_type_profile
originating_system
authoritative_record_references
```

and strengthens:

```text
event_type
event_date
historical_context
provenance
```

A related Registry reference is conditionally required when a corresponding SREG exists and is materially relevant.

---

# `event_type_profile`

Identifies the Event-Type Profile governing the Chronicle Entry.

**Requirement:** Required.

Required value:

```text
certification-event-profile
```

The value should remain stable across Chronicle Entry Versions unless Profile governance requires migration to a later Profile Version.

---

# `event_type`

Classifies the certification-related Occurrence represented by the Chronicle Entry.

**Requirement:** Required.

Allowed values:

```text
certification_created
certification_renewed
certification_suspended
certification_revoked
certification_expired
```

Rules:

* Event Type classifies the Occurrence.
* Event Type does not define Chronicle Entry identity.
* Event Type does not transfer Certifier authority to Chronicle.
* Event Type must correspond to an authoritative certification action or state recognized by Certifier.
* A correction to Event Type does not change `entry_id`.
* A distinct later certification Occurrence ordinarily receives a new Chronicle Entry.

---

# `event_date`

Represents the date or timestamp of the authoritative certification Occurrence.

**Requirement:** Required.

For this Profile, `event_date` must not be `null`.

The Event Date should be determinable from an authoritative Certifier record or another sufficiently authoritative certification reference.

Chronicle must preserve the distinction among:

```text
Certification Event Date
Chronicle Entry Creation Date
Source Retrieval Date
Chronicle Publication Date
Correction Date
Version Date
```

These timestamps must not be collapsed into one field.

Where the exact certification Event Date cannot be established, the Entry should not silently substitute Chronicle record time.

The issue should instead be handled through Chronicle Verification, limitations, or future approved uncertainty structures.

---

# `originating_system`

Identifies the system that originated the authoritative certification action represented by the Occurrence.

**Requirement:** Required.

Required value:

```text
certifier
```

Rules:

* `originating_system` is required by this Profile.
* It remains Conditional in the universal Chronicle Base Schema.
* It identifies Certifier as the originator of the authoritative action.
* It does not mean Chronicle owns Certifier's authority.
* It should not be used to encode certification status or Certification Package contents.

---

# `authoritative_record_references`

References the authoritative Certifier record establishing the represented certification Occurrence.

**Requirement:** Required.

Every Chronicle Entry governed by this Profile must include at least one authoritative Certifier reference sufficient to identify the relevant Certification Package or authoritative certification record.

The primary expected reference is:

```text
Certification Package identifier
```

Example:

```text
SC-CERT-2026-0001
```

Where represented as a structured reference, the reference should identify Certifier and the relevant record type.

Conceptually:

```text
Chronicle Entry
        ↓
references
        ↓
Authoritative Certification Package
```

Rules:

* Chronicle must not copy the Certification Package merely to satisfy this requirement.
* Reference does not transfer authority.
* Certifier remains authoritative for the Certification Package.
* The Chronicle Entry should preserve a durable identifier or canonical reference wherever available.

---

# Authoritative Certification Identifier

The authoritative certification identifier is represented through:

```text
authoritative_record_references
```

rather than through a duplicate universal field such as:

```text
certification_id
```

This avoids unnecessary duplication and preserves the Base Schema reference architecture.

The Profile requires that the authoritative certification reference be sufficient to identify the Certifier-owned record.

---

# Related Registry Reference

A certification-related Chronicle Entry may have a related SREG Registry Entry.

Examples may include:

```text
SREG-2026-0001
```

A related Registry reference is:

**Requirement:** Conditional.

It becomes Required when:

```text
A corresponding SREG Registry Entry exists
        +
The SREG is materially relevant to the Chronicle Entry
```

The related SREG may be represented through:

```text
relationships
```

or another approved Base Schema reference structure where appropriate.

Relationship Type must reflect the actual institutional relationship.

For the first production Entry, the materially relevant Registry relationship is:

```text
related_to
```

The primary Certifier authority is represented through `authoritative_record_references` and Provenance rather than duplicated as a Relationship.

Rules:

* Registry remains authoritative for the SREG.
* The SREG does not replace the Certification Package.
* Chronicle should not require an SREG merely because the Event Type is certification-related.
* The absence of an SREG does not invalidate an otherwise valid certification-related Chronicle Entry.

---

# `historical_context`

Preserves Chronicle's explanation of the certification Occurrence within the historical record.

**Requirement:** Required by Base Schema and strengthened by this Profile.

Certification-related Historical Context should be sufficient to explain:

* What certification Occurrence occurred
* Why the Occurrence is historically relevant
* How it relates to prior or later certification history where material
* Its institutional place within the Satoshium Suite
* Relevant Registry context where applicable
* Material uncertainty or limitations

Historical Context must remain distinguishable from:

```text
Certification Package contents
Certification findings
Certification evidence
Certifier determination logic
```

Chronicle should not restate authoritative Certifier conclusions merely to make the Entry appear more complete.

---

# `provenance`

Preserves how the information used by Chronicle originated, was accessed, and entered the Chronicle Entry.

**Requirement:** Required by Base Schema and strengthened by this Profile.

Minimum required Provenance for a certification-related Chronicle Entry should include:

```text
origin
acquisition_method
retrieved_at
authoritative_record_reference
```

For this Profile:

```text
origin
```

should identify Certifier or the authoritative Certifier environment associated with the represented record.

The `authoritative_record_reference` should identify the relevant Certification Package or authoritative certification record.

Material limitations must be preserved when applicable.

Conceptually:

```text
Certifier
        ↓
Authoritative Certification Package
        ↓
Chronicle access / acquisition
        ↓
Chronicle Provenance
        ↓
Chronicle Entry
```

---

# Source References

Separate Source references are Conditional.

They should be used when Chronicle relies on Sources beyond the authoritative Certifier record or when separately identified Source structure improves traceability.

Possible examples:

* Public certification page
* Repository record
* Institutional document
* Archived page
* Public metadata record

A Source does not replace the authoritative Certification Package.

---

# Evidence References

Evidence references are Conditional.

Certification-related Chronicle Entries may reference Evidence that:

* Supports
* Challenges
* Contradicts
* Clarifies
* Corroborates
* Contextualizes
* Limits confidence

Chronicle Evidence should support review of Chronicle's historical representation.

It should not be used to re-adjudicate Certifier's certification determination.

---

# Relationships

Relationships are Conditional but may become required when materially necessary to represent the certification Occurrence accurately.

Applicable general Relationship Types may include:

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

Potential certification-history uses include:

```text
Certification Created
        precedes
Certification Renewed

Certification Suspended
        precedes
Certification Reinstatement
```

where such later Event Types are formally approved.

Relationships must not imply causation or authority transfer unless explicitly governed.

---

# Certification Event Context

Certification Event Context is represented primarily through:

```text
historical_context
```

rather than through a duplicate field such as:

```text
certification_event_context
```

The Profile may strengthen Historical Context expectations without creating unnecessary parallel fields.

This preserves the Base Schema principle:

> Universal structure should be reused where it already expresses the required meaning.

---

# Verification Requirements

Chronicle Verification reviews Chronicle's own certification-related historical representation.

Verification should examine, where applicable:

* Chronicle Entry identity consistency
* Event Type correctness
* Event Date consistency
* `originating_system` consistency
* Authoritative Certification Package existence
* Authoritative identifier consistency
* Registry reference consistency
* Relationship integrity
* Provenance completeness
* Source availability
* Evidence availability
* Historical Context support
* Material limitations

Chronicle Verification does not:

* Certify
* Renew
* Suspend
* Revoke
* Expire
* Reaffirm
* Reissue
* Re-adjudicate Certifier findings

The governing principle is:

> Verify the Chronicle record. Respect Certifier authority.

---

# Validation Requirements

A production Chronicle Entry governed by this Profile is validated against:

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
        +
Publication Prerequisites
```

The machine-readable Profile should enforce, at minimum:

* Base Schema conformance
* `event_type_profile = certification-event-profile`
* approved certification Event Type
* non-null `event_date`
* `originating_system = certifier`
* presence of `authoritative_record_references`
* minimum one authoritative reference
* certification-specific Provenance requirements

The related Registry reference should be validated only when the operational condition requiring it applies.

Validation does not replace Verification.

---

# Publication Requirements

This Profile does not independently redefine Chronicle Publication State.

Certification-related Chronicle Entries inherit Base Schema Publication State values:

```text
not_published
pending_publication
published
withdrawn_from_publication
```

Certification-related Entries follow Chronicle's established Publication Gate after Verification and Validation. CHR-VAL-011 tests Publication Readiness; the separate Publication Gate makes the institutional approval decision.

The Profile does not duplicate Certifier publication rules.

---

# Corrections and Versioning

Certification-related Chronicle Entries follow Chronicle Correction and Versioning rules.

If Chronicle's representation is materially wrong:

```text
Correction
        ↓
New Entry Version where material
```

If Certifier performs a distinct later authoritative action:

```text
New certification Occurrence
        ↓
Preservation Eligibility
        ↓
New Chronicle Entry
```

Examples:

```text
Certification Created
        ↓
later Certification Renewed
```

should ordinarily represent distinct Occurrences rather than Versions of one Entry.

The Chronicle Entry identifier remains permanent across Versions of the same canonical Entry.

---

# What the Profile Does Not Duplicate

The Certification Event-Type Profile does not reproduce or redefine:

```text
Certification Package schema
Certification findings
Certification evidence body
Certifier validation structures
Certification status mechanics
Certification lifecycle procedures
Certification determination logic
Certifier publication architecture
```

Chronicle should preserve references rather than duplicate authoritative Certifier structures.

---

# Preservation Eligibility

Use of the Certification Event-Type Profile does not itself establish Preservation Eligibility.

The sequence remains:

```text
Certification Occurrence
        ↓
Preservation Eligibility
        ↓
Chronicle Entry
        ↓
Certification Event-Type Profile
```

An approved Event Type may support predictable admission rules, but Profile applicability and Preservation Eligibility remain distinct concepts.

---

# Machine-Readable Profile

The machine-readable production implementation is published as:

```text
/chronicle/schemas/certification-event-profile/certification-event-profile.json
```

Canonical URI:

```text
https://satoshium.us/chronicle/schemas/certification-event-profile/certification-event-profile.json
```

The JSON Profile composes with:

```text
/chronicle/schemas/chronicle-base-schema.json
```

rather than duplicating the Base Schema.

Conceptually:

```text
chronicle-base-schema.json
        +
certification-event-profile.json
        =
Certification-related Chronicle Entry Validation
```

The machine-readable Profile must not introduce requirements that contradict this human-readable specification.

---

# Profile Versioning

The Certification Event-Type Profile has its own Version.

Initial Version:

```text
1.0.0
```

Profile evolution should preserve:

* Profile identity
* Profile Version
* compatibility classification
* deprecation history
* migration guidance
* historical interpretability
* validation behavior

A Profile Version change does not automatically require a Chronicle Entry Version change unless the Entry itself materially changes.

---

# First Production Application

The Certification Event-Type Profile Version 1.0.0 has now been exercised through the first canonical production Chronicle Entry:

```text
CHR-2026-0001
```

Production application:

```yaml
entry_id: CHR-2026-0001
schema_id: chronicle-entry
schema_version: 1.0.0
entry_version: 1

title: Creation of SC-CERT-2026-0001

summary: >
  Satoshium Certifier issued the authoritative Certification Package
  SC-CERT-2026-0001 on July 5, 2026, establishing the inaugural
  Operational certification of the Satoshium Atlas Jurisdiction Record
  — El Salvador.

event_type: certification_created
event_date: 2026-07-05

event_type_profile: certification-event-profile
originating_system: certifier

authoritative_record_references:
  - reference: SC-CERT-2026-0001
    system: certifier
    record_type: Certification Package
    url: https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/

relationships:
  - type: related_to
    target: SREG-2026-0001
    target_system: registry
    context: Registry Entry cataloging SC-CERT-2026-0001.

  - type: references
    target: Atlas Jurisdiction Record — El Salvador
    target_system: atlas
    context: Authoritative Atlas subject record evaluated by SC-CERT-2026-0001.

provenance:
  origin: Satoshium Certifier
  acquisition_method: production_review_of_authoritative_and_supporting_suite_records
  retrieved_at: 2026-08-22T08:06:00-07:00
  authoritative_record_reference:
    reference: SC-CERT-2026-0001
    system: certifier
    record_type: Certification Package
    url: https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/

verification_state: verified
lifecycle_state: active
publication_state: published

entry_created_at: 2026-08-22T08:06:00-07:00
published_at: 2026-08-22T08:38:00-07:00
```

Production review confirmed:

```text
Base Schema conformance: PASS
Certification Event-Type Profile conformance: PASS
Chronicle Validation: PASS
CHR-VAL-011 Publication Readiness: PASS
Publication Gate: APPROVED
Publication: published
```

The Profile therefore has a production precedent, not merely an illustrative example.

---

# Required / Conditional Summary

## Inherited Required Base Schema Fields

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

## Additional Profile Requirements

```text
event_type_profile
originating_system
authoritative_record_references
```

## Profile Constraints

```text
event_type_profile = certification-event-profile

originating_system = certifier

event_type =
  certification_created
  certification_renewed
  certification_suspended
  certification_revoked
  certification_expired

event_date = non-null date or date-time

authoritative_record_references =
  minimum one authoritative Certifier reference
```

## Conditional Certification Requirements

```text
related Registry reference
source_references
evidence_references
relationships
limitations
```

---

# Design Principles

## Base Schema First

The Profile extends the Base Schema rather than replacing it.

## Chronicle Entry Remains Canonical

There is no separate canonical Certification Event record.

## Certifier Retains Authority

Chronicle references Certifier rather than recreating certification authority.

## Require Only Certification-Specific Structure

Do not duplicate universal Base Schema fields under new names.

## Reference the Package

Do not copy the Certification Package.

## Registry Remains Separate

A related SREG provides catalog context but remains Registry-owned.

## Event Date Means Occurrence Time

Do not substitute Chronicle creation or publication time.

## Provenance Remains Explicit

Preserve how Chronicle obtained the authoritative information.

## Verification Is Chronicle-Specific

Verify Chronicle's representation, not Certifier's determination.

## Preserve Version Lineage

Material Chronicle changes remain traceable.

---

# Guiding Principle

> Certifier establishes certification authority. Chronicle preserves the historical record of what occurred.

And operationally:

> Base Schema defines the Chronicle Entry. The Certification Event-Type Profile supplies only the certification-specific requirements.

---

## Status

**Phase VII production Certification Event-Type Profile specification.**

This document defines the human-readable production requirements for Chronicle Entries representing qualifying certification-related Occurrences.

It is published as part of:

```text
/chronicle/schemas/certification-event-profile/
```

with:

```text
index.html
certification-event-profile.md
certification-event-profile.json
```

It is aligned with:

* Chronicle Base Schema
* Chronicle Entry Model
* Event Types
* Preservation Eligibility
* Identifiers
* Controlled Values
* Relationships
* Provenance
* Sources
* Evidence
* Verification
* Lifecycle
* Versioning
* Corrections
* Suite authority boundaries

The human-readable and machine-readable Profile artifacts are established.

Phase VII two-layer Profile Validation completed with PASS, and the same Base + Profile stack subsequently governed `CHR-2026-0001` in production on August 22, 2026.

Production application confirmed that no Profile schema change was required.
