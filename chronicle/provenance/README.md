# Chronicle Provenance Model

## Purpose

The Chronicle Provenance Model defines how Satoshium Chronicle records:

* Where information originated
* How Chronicle accessed or acquired it
* How the information moved between systems
* Whether the material was transformed
* How it entered the historical record
* What preservation path exists
* What provenance limitations remain

Provenance is a required logical component of every production Chronicle Entry.

The core question is:

> How did this information get here?

The governing principle is:

> Preserve origin. Preserve path. Preserve limitations.

---

# Provenance in the Chronicle Architecture

Provenance sits between raw information origin and Chronicle's historical representation.

Conceptually:

```text
Origin
    ↓
Source / Authoritative Record / Evidence
    ↓
Access / Acquisition
    ↓
Transfer / Capture / Transformation
    ↓
Chronicle
    ↓
Verification
    ↓
Historical Preservation
```

Provenance documents the path.

Verification reviews the historical representation built from that path.

---

# Provenance Is Required

The Chronicle Entry Model defines Provenance as:

```text
Provenance [Required]
```

Every production Chronicle Entry must contain sufficient provenance to make the origin and acquisition of its underlying historical information traceable.

This does not require identical provenance depth for every Entry.

The minimum baseline is universal.

Additional detail is conditional on:

* Event Type
* Event-Type Profile
* Source quality
* Evidence sensitivity
* Historical importance
* Integrity risk
* Transformation
* Archival complexity
* Verification needs

---

# Core Distinctions

Chronicle must distinguish Provenance from Sources, Evidence, and Verification.

---

## Source

Source answers:

> Where did the information come from?

Examples:

* Certification Package
* SREG Registry Entry
* Institutional document
* Repository object
* Webpage
* Dataset
* Archive
* Statement

A Source identifies an origin object or publication.

---

## Evidence

Evidence answers:

> What material bears on the Entry or claim?

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Corroborate
* Contextualize
* Limit confidence

Evidence describes historical or evidentiary function.

---

## Provenance

Provenance answers:

> How did this information get here?

It records the route from origin into Chronicle.

---

## Verification

Verification answers:

> Has Chronicle adequately reviewed its own historical representation?

Verification may inspect:

* Sources
* Evidence
* Provenance
* Authoritative references
* Temporal consistency
* Relationships
* Limitations

Verification consumes Provenance.

It is not itself Provenance.

---

# Core Formula

Conceptually:

```text
Source = Origin object
Evidence = Material bearing on the Entry
Provenance = Information path
Verification = Review of Chronicle's representation
```

These concepts must not be collapsed.

---

# Minimum Production Provenance

Every production Chronicle Entry must include enough provenance to establish a minimum traceability baseline.

The initial minimum provenance components are:

```text
Origin
Acquisition / Access Method
Capture / Retrieval Date
Source or Authoritative Record Reference when available
Provenance Limitations when applicable
```

These requirements apply to every production Entry.

---

# 1. Origin

## Requirement

Required.

Origin identifies the system, institution, repository, person, Source, authoritative record, or other entity from which the historical information originated.

Potential examples:

```text
Satoshium Certifier
Satoshium Registry
GitHub repository
Satoshium public website
Institutional archive
External government publication
Individual statement
```

Origin should be sufficiently precise to support later review.

---

# 2. Acquisition / Access Method

## Requirement

Required.

Chronicle should record how it obtained or accessed the information.

Potential methods may include:

```text
Direct authoritative-system reference
Public webpage access
Repository access
File receipt
API retrieval
Archive retrieval
Manual submission
System export
Database query
Other documented method
```

The final controlled vocabulary should be developed only if repeated production use demonstrates the need.

---

# 3. Capture / Retrieval Date

## Requirement

Required.

Chronicle should record when it accessed, captured, retrieved, or received the information.

This date is distinct from:

* Event Date
* Source creation date
* Source publication date
* Entry creation date
* Publication date

Example:

```text
Source Publication Date:
2026-07-05

Chronicle Retrieval Date:
2026-09-03
```

Both may matter.

---

# 4. Source or Authoritative Record Reference

## Requirement

Required when available.

The provenance path should connect to a stable reference where one exists.

Examples:

```text
SC-CERT-2026-0001
SREG-2026-0001
Repository commit identifier
Document URI
Archive identifier
Source Record identifier
Public URL
```

If no stable reference exists, Chronicle should preserve the best available identifying information and note the limitation.

---

# 5. Provenance Limitations

## Requirement

Required when applicable.

Chronicle should explicitly preserve known weaknesses or gaps in the provenance chain.

Potential limitations include:

* Original unavailable
* Accessed through archive only
* Unknown creator
* Unknown publication date
* Incomplete custody history
* Transcription involved
* Source converted from another format
* Broken original link
* Uncertain capture history
* Third-party copy
* Missing integrity metadata

A limitation should not be hidden merely because it complicates the record.

---

# Minimum Provenance Example

A simple production Entry may record:

```text
Origin:
Satoshium Certifier

Authoritative Object:
SC-CERT-2026-0001

Access Method:
Direct repository reference

Retrieval Date:
2026-09-03

Limitations:
None known
```

This may be sufficient for a straightforward authoritative Suite record.

---

# Expanded Provenance

Some Entries require more detail.

Expanded Provenance may include:

* Transfer history
* Transformation history
* Custody path
* Archive path
* Preservation history
* Integrity metadata
* Hashes
* Signatures
* Timestamps
* Export information
* Import process
* Conversion tools
* Manual transcription
* Reviewer notes
* Provenance relationships

Expanded Provenance should be proportional to the historical and integrity needs of the Entry.

---

# Provenance Is Not Always Chain of Custody

Chronicle Provenance is broader than forensic chain of custody.

Chain of custody may be appropriate for:

* Sensitive Evidence
* Disputed records
* High-integrity artifacts
* Manual transfer processes
* Legal or evidentiary materials

But every Chronicle Entry does not require courtroom-style custody documentation.

Chronicle should avoid unnecessary procedural complexity where a direct authoritative reference already provides strong traceability.

---

# Provenance and Authoritative Suite Objects

When Chronicle references an authoritative Suite object, Provenance should identify:

1. Originating Suite system
2. Authoritative object identifier
3. Access or retrieval method
4. Access or retrieval date
5. Any transformation or intermediary copy
6. Known limitations

Example:

```text
Originating System:
Certifier

Authoritative Object:
SC-CERT-2026-0001

Access Method:
Direct repository access

Retrieval Date:
2026-09-03

Transformation:
None

Limitations:
None known
```

---

# Authority Boundary

Provenance identifies origin.

It does not transfer authority.

Example:

```text
Origin:
Certifier

Chronicle Entry:
CHR-2026-0001
```

Certifier remains authoritative for the Certification Package.

Chronicle remains authoritative for the Chronicle Entry.

Conceptually:

> Provenance explains origin. It does not reassign authority.

---

# Provenance and Source Records

A Source Record may hold structured information about a Source.

The Chronicle Entry may reference that Source Record.

Provenance may then describe:

* How Chronicle discovered the Source
* How Chronicle accessed it
* When it was accessed
* Whether it was archived
* Whether it was transformed
* How it entered the Entry

Conceptually:

```text
Source Record
    ↓
Provenance Path
    ↓
Chronicle Entry
```

---

# Provenance and Evidence

Evidence may have its own Provenance.

Example:

```text
Evidence:
Archived certification notice

Evidence function:
Corroborates certification date

Provenance:
Captured from official public page through archive on 2026-09-04
```

The evidentiary function and provenance path remain distinct.

---

# Provenance Quality and Evidence Quality

These dimensions should not be treated as identical.

An Evidence item may be:

* Highly persuasive but poorly documented in provenance
* Weakly persuasive but perfectly documented in provenance
* Authentic but contextually limited
* Well-provenanced but non-authoritative

Chronicle should preserve these distinctions.

---

# Provenance and Verification

Verification should review whether the recorded Provenance is sufficient for the historical claims being made.

Verification may ask:

* Is the origin identifiable?
* Does the referenced Source exist?
* Is the retrieval method plausible?
* Are dates internally consistent?
* Were transformations disclosed?
* Are material limitations visible?
* Does the provenance path support Chronicle's representation?

Verification may conclude:

```text
Verified
Verified with Limitations
Unresolved
```

depending partly on Provenance quality.

---

# Verification Does Not Manufacture Provenance

If the provenance chain is incomplete, Verification should record that limitation.

Verification must not convert uncertainty into certainty.

Conceptually:

> Unknown does not become known by review.

---

# Provenance and Relationships

Relationships connect objects.

Provenance explains paths.

Example:

```text
CHR-2026-0001
References
SC-CERT-2026-0001
```

is a Relationship.

The Provenance may explain:

```text
SC-CERT-2026-0001 accessed directly from the Certifier repository on 2026-09-03.
```

Relationship and Provenance should not be merged merely because they concern the same object.

---

# Provenance and `Derived From`

The Relationship Type:

```text
Derived From
```

may be used where one record is materially based on another.

This should not replace descriptive Provenance when the derivation process itself matters.

Example:

```text
Relationship:
Chronicle Source Record Derived From archived HTML page

Provenance:
Archived HTML captured via archive service, converted to text, reviewed manually
```

---

# Transfer History

Transfer history is Conditional.

It should be recorded when information moved through meaningful intermediaries.

Example:

```text
Original institutional PDF
    ↓
Downloaded copy
    ↓
Repository archive
    ↓
Chronicle
```

If Chronicle accesses the authoritative original directly, detailed transfer history may not be necessary.

---

# Transformation History

Transformation should be recorded when the form of information changes in a way that may affect interpretation.

Examples:

* PDF converted to text
* HTML archived
* Structured JSON generated from document
* Screenshot captured
* Audio transcribed
* Data exported from database
* File normalized
* Encoding converted

Chronicle should identify transformations that materially affect trust, interpretation, or reproducibility.

---

# Manual Transcription

If information is manually transcribed, Provenance should disclose that fact.

Manual transcription introduces potential error.

The record may require:

* Reviewer confirmation
* Source reference
* Original artifact preservation
* Comparison check

depending on significance.

---

# Summaries and Derived Narrative

Chronicle may create narrative historical context from multiple Sources.

Provenance should allow future reviewers to determine which Sources informed the narrative.

Chronicle should not imply that its narrative wording appeared verbatim in the Source unless that is true.

---

# Archive Provenance

If the original Source is no longer available, Chronicle may rely on an archive.

Provenance should identify:

* Original Source when known
* Archive service or repository
* Archived capture date where known
* Chronicle access date
* Limitations

Example:

```text
Original:
Satoshium webpage

Archive:
Institutional snapshot

Original capture:
2026-07-05

Chronicle retrieval:
2026-09-10

Limitation:
Original live page no longer available
```

---

# Broken Links

A broken public link does not erase provenance.

Chronicle should preserve:

* Last known URL
* Archive reference
* Source Record
* Retrieval history
* Integrity information where available
* Limitation note

Historical traceability should survive link decay.

---

# Integrity Metadata

Integrity metadata is Optional or Conditional.

Potential fields may include:

* SHA-256 hash
* Other checksum
* Digital signature
* Timestamp
* Immutable content identifier
* Repository commit
* Anchor reference

Integrity metadata should be used when it materially strengthens traceability or authenticity.

Chronicle should not require cryptographic metadata for every Source merely for appearance of rigor.

---

# Provenance and Anchor

Future integration with Anchor may allow Chronicle to preserve Integrity References associated with Sources, Evidence, or Chronicle records.

Anchor remains authoritative for Integrity References.

Chronicle may reference them as part of Provenance or preservation history.

---

# Provenance and Preservation

Provenance should survive long-term preservation.

If Chronicle migrates storage systems, formats, repositories, or publication infrastructure, the preservation process should not erase the origin history of the underlying material.

Future preservation provenance may record:

```text
Original storage
Migration
New storage
Integrity check
Migration date
```

---

# Provenance and Versioning

Provenance may change when:

* A better Source is found
* An authoritative reference is added
* A broken link is replaced by an archive reference
* A transformation error is discovered
* Custody information is clarified
* Integrity metadata becomes available

Material provenance changes may require:

* New Entry Version
* Supporting record Version
* Correction Record
* Verification update

depending on impact.

---

# Provenance and Corrections

A Provenance Correction may be required when Chronicle discovers:

* Wrong origin
* Incorrect Source attribution
* Incorrect retrieval date
* Missing transformation
* Incorrect archive path
* Incorrect authoritative reference

The Chronicle Controlled Values Registry currently includes:

```text
Provenance
```

as a Correction Type.

---

# Provenance and Retrospective Preservation

Retrospective Entries may have more complex Provenance.

Example:

```text
Occurrence:
2024

Source archived:
2025

Chronicle Entry created:
2026
```

The Provenance should preserve the temporal chain rather than imply contemporaneous collection.

---

# Provenance and Event-Type Profiles

Event-Type Profiles may require enhanced Provenance.

For example, the Certification Event-Type Profile may require:

* Certifier as originating system
* Certification Package identifier
* Direct or archived retrieval method
* Retrieval date
* Related Registry reference when applicable

The Base Model defines universal minimums.

Profiles may strengthen them.

---

# Provenance Controlled Values

Chronicle may later require Controlled Values for:

* Acquisition Method
* Capture Method
* Transformation Type
* Provenance Status
* Custody Type
* Archive Type

These should not be frozen until production demonstrates a need.

Narrative provenance may remain appropriate for low-complexity cases.

---

# Provenance Validation

Future Validation should confirm, at minimum:

1. Origin is present.
2. Acquisition or access method is present.
3. Capture or retrieval date is valid.
4. Source or authoritative reference is present when available and required.
5. Referenced identifiers conform to applicable identifier rules.
6. Known Provenance limitations are represented.
7. Required Event-Type Profile Provenance is present.
8. Transformations are disclosed when required.
9. Provenance is internally consistent with Source and Evidence records.
10. Provenance fields conform to the governing schema Version.

---

# Provenance Sufficiency

Provenance sufficiency should be proportional.

A direct authoritative Suite object may require relatively simple Provenance.

A disputed third-party document may require significantly more.

Chronicle should ask:

> Is the recorded provenance sufficient for a future reviewer to reconstruct how this information entered the historical record?

If yes, the Provenance may be sufficient.

---

# Provenance Limitations

Known limitations should remain explicit.

Potential standardized limitation concepts may later include:

```text
Original unavailable
Incomplete chain
Unknown creator
Unknown retrieval path
Archived copy only
Manual transcription
Third-party copy
Transformation applied
Integrity metadata unavailable
```

These should remain narrative or provisional until production demonstrates a need for Controlled Values.

---

# Broken or Incomplete Provenance

Incomplete Provenance does not automatically mean:

* The Occurrence is not historically significant
* The Source is false
* The Evidence is unusable
* The Entry cannot be preserved

It means the limitation should be visible and Verification should account for it.

Conceptually:

```text
Incomplete Provenance
    ↓
Visible Limitation
    ↓
Verification Assessment
```

---

# Provenance and Trust

Chronicle trust is reviewable.

Provenance contributes to trust by allowing reviewers to reconstruct the path behind the historical record.

The trust model therefore depends on:

```text
Authority
Sources
Evidence
Provenance
Verification
Validation
Corrections
Versions
Preservation
```

Provenance is one component.

It is not a universal trust score.

---

# Minimum Provenance Rule

Every production Chronicle Entry must record:

```text
Origin
Acquisition / Access Method
Capture / Retrieval Date
Source or Authoritative Record Reference when available
Known Provenance Limitations when applicable
```

An Event-Type Profile may require more.

It may not require less than the universal minimum without formal architectural revision.

---

# Production Example — Certification Event

A first production certification Entry might use:

```text
Chronicle Entry:
CHR-2026-0001

Event Type:
Certification Created

Originating System:
Certifier

Authoritative Object:
SC-CERT-2026-0001

Acquisition Method:
Direct repository access

Retrieval Date:
2026-09-XX

Transformation:
None

Related Registry Object:
SREG-2026-0001

Provenance Limitations:
None known
```

The exact production values remain subject to the actual first Entry and procedure.

---

# Model Summary

The conceptual Provenance structure is:

```text
Chronicle Entry
│
└── Provenance
    ├── Origin [Required]
    ├── Acquisition / Access Method [Required]
    ├── Capture / Retrieval Date [Required]
    ├── Source / Authoritative Reference [Required when available]
    ├── Transfer History [Conditional]
    ├── Transformation History [Conditional]
    ├── Preservation Path [Conditional]
    ├── Integrity Metadata [Optional / Conditional]
    └── Provenance Limitations [Required when applicable]
```

---

# Guiding Principle

> Provenance turns information into traceable history.

And operationally:

> Preserve origin. Preserve path. Preserve limitations.

---

## Relationship to Other Chronicle Documentation

The Chronicle Provenance Model should remain aligned with:

* Entry Model
* Preservation Eligibility
* Chronicle Rules
* Identifier Specification
* Controlled Values Registry
* Relationship Model
* Sources
* Evidence
* Verification
* Corrections
* Historical Preservation
* Trust Model
* Schemas
* Validation

Provenance provides the traceability architecture connecting supporting information to the canonical Chronicle Entry.

---

## Next Operational Dependencies

The Provenance Model directly informs:

* Supporting-record architecture
* Lifecycle
* Versioning
* Corrections
* Chronicle Base Schema
* Certification Event-Type Profile
* Validation
* Production Procedure
* First production Chronicle Entry

The first production Entry should test whether the universal minimum Provenance requirements are sufficient in practice.

---

## Status

**Active pre-operational Chronicle Provenance Model specification.**

The universal minimum Provenance baseline is established conceptually.

Acquisition-method vocabularies, transformation vocabularies, custody models, integrity requirements, and Event-Type-specific Provenance requirements remain intentionally limited until production use demonstrates a need.
