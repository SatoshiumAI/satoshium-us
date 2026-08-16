# Chronicle Source Record Schema

## Purpose

The Chronicle Source Record Schema defines the Chronicle-owned supporting structure used to identify, describe, reference, and preserve Sources used by Satoshium Chronicle.

A Source Record answers the institutional question:

> Where did this information come from?

A Source Record preserves enough structured information to make a Source identifiable, attributable, traceable, reviewable, and historically durable.

A Source Record is not the canonical Chronicle historical object.

The canonical object remains the **Chronicle Entry**.

A Source Record also does not become authoritative merely because Chronicle preserves or references it.

The governing principle is:

> Identify the Source. Preserve the reference. Trace the path. Keep authority visible.

---

# Canonical Role

A Chronicle Source Record is a **supporting Chronicle-owned record**.

Conceptually:

```text
Chronicle Entry
      ↓
Source Reference
      ↓
Source Record
      ↓
Evidence / Provenance / Verification Context
```

A Source Record exists when Chronicle needs more structure than a simple direct Source reference can provide.

Examples include situations requiring:

* structured Source identity
* attribution
* archival context
* material limitations
* Provenance
* reuse across Entries
* integrity metadata
* Version lineage
* public Source discovery
* Validation

A direct external reference may be sufficient when those additional requirements are unnecessary.

---

# Source, Evidence, Provenance, and Verification

These concepts remain distinct.

## Source

Answers:

> Where did the information come from?

## Evidence

Answers:

> What material bears on the Chronicle Entry or claim?

## Provenance

Answers:

> How did the information or Evidence originate, move, and enter Chronicle?

## Verification

Answers:

> Has Chronicle reviewed the relevant aspects of its own historical representation and supporting references?

Conceptually:

```text
Source ≠ Evidence ≠ Provenance ≠ Verification
```

A Source Record should not duplicate Evidence or Provenance structures unnecessarily.

---

# Source Contexts

Chronicle recognizes three operational Source contexts.

## Authoritative Source Record

A Chronicle Source Record documenting an authoritative object or institutional Source.

The Source Record itself does not become the authority.

Authority remains with the originating institution or system.

---

## Supporting Source

A Source used for:

* context
* corroboration
* background
* attribution
* interpretation
* temporal detail
* historical understanding

A Supporting Source may be highly useful without being authoritative for the underlying institutional action.

---

## Referenced External Source

A Source outside Chronicle, and possibly outside the Suite, referenced directly where a separate Source Record would add little operational value.

A direct reference may be sufficient when the Source is:

* stable
* narrowly used
* easily identifiable
* adequately attributable
* not in need of independent Chronicle lifecycle treatment

---

# Production Status

This specification defines the Phase VII production architecture for Chronicle Source Records.

The current canonical human-readable file is:

```text
source-record-schema.md
```

A future machine-readable implementation may be created as:

```text
source-record-schema.json
```

only after the production field boundary is exercised against a real Chronicle Entry and Source Record.

---

# Field Architecture

The Source Record Schema distinguishes:

```text
Required
Conditional
Optional
```

A field should not be Required unless every production Source Record needs it.

---

# Universal Required Fields

Every production Chronicle Source Record should contain:

```text
source_id
schema_id
schema_version
source_record_version

title
source_type

provenance

created_at
```

These form the minimum Source Record identity and traceability structure.

---

# Identity Fields

## `source_id`

Stable unique identifier assigned to the Chronicle Source Record.

**Requirement:** Required.

The final Source Record identifier namespace remains to be formally established.

Until that identifier architecture is approved, production implementation should not invent a permanent namespace casually.

The Source Record identifier must remain:

* stable
* unique
* non-reusable
* independent of Source Type
* independent of publication or verification state

---

## `schema_id`

Stable identifier for the Source Record Schema.

**Requirement:** Required.

Initial value:

```text
chronicle-source-record
```

---

## `schema_version`

Version of the Source Record Schema governing the record.

**Requirement:** Required.

Initial production convention:

```text
1.0.0
```

Schema Version is distinct from Source Record Version.

---

## `source_record_version`

Sequential preserved Version of the same Chronicle Source Record.

**Requirement:** Required.

Initial value:

```text
1
```

Material changes should advance the Source Record Version when they alter institutional meaning or review context.

Examples may include:

* changed Source identity
* changed attribution
* changed Provenance
* changed archival representation
* material limitation discovery
* changed authoritative reference

---

# Human-Readable Identity

## `title`

Concise human-readable title identifying the Source.

**Requirement:** Required.

Example:

```text
Satoshium Chronicle Public Launch Page
```

---

## `description`

Brief factual description of the Source.

**Requirement:** Conditional.

Required when the title alone does not adequately explain what the Source is.

---

# Source Type

## `source_type`

Controlled classification identifying the type of Source.

**Requirement:** Required.

Approved Chronicle Source Type values are:

```text
authoritative_record
institutional_document
web_page
repository_record
dataset
archive
statement
other
```

Human-readable labels:

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

Rules:

* Source Type describes what kind of Source this is.
* Source Type does not establish institutional authority by itself.
* Source Type does not replace Source Role.
* `other` should be used only when no approved value accurately fits.
* Repeated use of `other` should trigger Controlled Values review.

---

# Source Role

## `source_role`

Describes the Source's role in relation to an Entry, claim, Evidence item, or historical representation.

**Requirement:** Conditional.

Source Role is **not yet a frozen Controlled Value set**.

Candidate concepts include:

```text
authoritative
supporting
primary
secondary
contextual
archival
corroborating
reference
```

These terms remain provisional.

Source Role should become a formal Controlled Value set only when production use demonstrates a stable need.

Source Type and Source Role must remain distinct.

---

# Creator and Publisher

## `creator`

Entity, person, organization, institution, or system responsible for creating the Source.

**Requirement:** Conditional.

Required when known and materially relevant.

---

## `publisher`

Entity, person, organization, institution, or system responsible for publishing or distributing the Source.

**Requirement:** Conditional.

Creator and publisher may be the same.

They should not be assumed to be identical.

---

# Source Reference and Location

## `stable_reference`

Stable identifier, canonical reference, archive identifier, repository identifier, government record number, dataset identifier, DOI-like identifier, commit reference, or other durable Source identity.

**Requirement:** Conditional.

Preferred over a bare URL where available.

Examples may include:

```text
SC-CERT-2026-0001
SREG-2026-0001
repository commit
archive identifier
dataset identifier
```

---

## `source_location`

Location where the Source can be accessed.

**Requirement:** Conditional.

May include:

```text
https://...
repository://...
archive://...
```

A URL is a location.

It is not necessarily the Source's identity.

---

## `archive_reference`

Reference to an archived or preserved representation of the Source.

**Requirement:** Conditional.

Required when:

* the original Source is unstable
* the original Source is unavailable
* Chronicle relies on an archived representation
* long-term reviewability depends on the archive

---

## `authoritative_record_reference`

Reference to an authoritative external or Suite object when the Source itself corresponds to such a record.

**Requirement:** Conditional.

Examples may include:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Trust Statement
* Workflow Definition
* Atlas record

Rules:

* Chronicle references the object.
* Chronicle does not duplicate its authoritative schema.
* Chronicle does not inherit its institutional authority.

---

# Temporal Fields

Temporal fields should remain distinct.

## `original_created_at`

Date or timestamp associated with creation of the Source.

**Requirement:** Conditional.

---

## `published_at`

Date or timestamp associated with publication or release of the Source.

**Requirement:** Conditional.

---

## `accessed_at`

Date or timestamp when Chronicle accessed the Source.

**Requirement:** Conditional.

Required for mutable Sources where later review needs to know when Chronicle observed the Source.

---

## `captured_at`

Date or timestamp when Chronicle captured, archived, downloaded, exported, or otherwise preserved the Source.

**Requirement:** Conditional.

These timestamps should not be collapsed into one generic access timestamp.

---

## `created_at`

Date and time Chronicle created the Source Record.

**Requirement:** Required.

This is Chronicle record time.

It is not Source creation time.

---

# Provenance

## `provenance`

Structured information describing how the Source originated, was discovered, accessed, captured, transferred, transformed, archived, and entered Chronicle.

**Requirement:** Required.

Every production Source Record should preserve, at minimum:

```text
origin
acquisition_method
retrieved_at
```

and, when applicable:

```text
source_reference
authoritative_record_reference
limitations
```

Expanded Provenance may include:

* discovery method
* capture method
* transfer history
* transformation history
* archive path
* preservation history
* integrity metadata

The Provenance Model governs meaning.

The Source Record Schema should not redefine that model independently.

---

# Entry Linkage

## `related_entry_references`

References to Chronicle Entries associated with the Source.

**Requirement:** Conditional.

Required when the Source Record exists because one or more Chronicle Entries rely upon it.

A Source Record may be reused across multiple Entries.

---

# Evidence Linkage

## `related_evidence_references`

References to Evidence Records or Evidence items associated with the Source.

**Requirement:** Conditional.

A Source may contain or produce multiple Evidence items.

The Source Record should not flatten those Evidence items into the Source itself.

---

# Correction Linkage

## `related_correction_references`

References to Correction Records affecting this Source Record or its relationship to Chronicle.

**Requirement:** Conditional.

Required when a formal Correction applies.

---

# Related Sources

## `related_source_references`

References to other Source Records.

**Requirement:** Conditional.

Where structured Relationship semantics matter, approved Chronicle Relationship Types should be used.

---

# Limitations

## `limitations`

Structured or narrative description of known Source limitations.

**Requirement:** Conditional.

Required when material limitations exist.

Examples may include:

* incomplete
* stale
* unavailable
* archived copy only
* ambiguous authorship
* broken reference
* conflicting publication date
* derivative
* missing Provenance
* context-limited
* altered or reformatted representation

Limitations are part of the historical record.

They should not be hidden merely because the Source remains useful.

---

# Reliability Notes

## `reliability_notes`

Narrative or structured observations relevant to Source reliability.

**Requirement:** Optional.

This field should not become a universal truth score.

Chronicle should avoid unsupported numerical reliability scoring unless later Suite standards explicitly require it.

---

# Integrity Metadata

## `checksum`

Cryptographic checksum or digest for preserved Source material.

**Requirement:** Optional / Conditional.

Example:

```text
sha256:<HASH>
```

---

## `digital_signature_reference`

Reference to a signature or signature-verification artifact.

**Requirement:** Conditional.

---

## `integrity_metadata`

Other integrity information relevant to the Source.

**Requirement:** Optional / Conditional.

May include:

* repository commit
* timestamp
* immutable object identifier
* Anchor Integrity Reference
* content hash
* file metadata

Integrity metadata supports reviewability.

It does not replace Provenance or authority.

---

# Preservation Information

## `preservation_notes`

Information describing archival state, capture method, long-term accessibility, or preservation limitations.

**Requirement:** Conditional.

A separate Controlled Preservation State is **not yet frozen** for Source Records.

Therefore the schema should not invent a production `preservation_status` vocabulary at this stage.

If production experience demonstrates the need, Preservation State can later be added through schema evolution.

---

# Verification

## `verification_state`

Chronicle Verification State associated with the Source Record where Chronicle separately reviews Source-level questions.

**Requirement:** Conditional.

Approved values:

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

Source-level Verification may review:

* Source existence
* attribution
* creator / publisher identity
* publication date
* access consistency
* archive consistency
* Provenance
* limitations
* reference integrity

Verification does not convert the Source into Chronicle authority.

---

## `verification_references`

References to separately preserved Verification activity or records.

**Requirement:** Conditional.

Whether a distinct Verification Record is required remains subject to later production architecture.

---

# Validation

The Source Record Schema is designed for Validation.

It does not presently require a universal embedded:

```text
validation_state
```

The Validation Procedure should determine where validation results are preserved.

Validation may test:

* Source Record identifier integrity
* schema conformance
* required fields
* Controlled Values
* reference integrity
* Provenance requirements
* Entry linkage
* Evidence linkage
* Version linkage
* publication prerequisites

Conceptually:

```text
Schema ≠ Verification ≠ Validation
```

---

# Lifecycle

A separate production `source_status` field is not yet required.

Chronicle's currently approved Lifecycle State values were established for Chronicle Entries:

```text
Draft
Active
Superseded
Withdrawn
Preserved
```

They should not automatically be applied to Source Records without operational evidence that the same state model fits.

The Source Record lifecycle may still conceptually include:

```text
identified
structured
reviewed
validated
used
maintained
corrected / versioned
preserved
```

But those process stages should not be prematurely converted into Controlled Values.

---

# Publication

## `publication_state`

Publication State of the Source Record when Source Records themselves are independently published.

**Requirement:** Conditional.

Approved Chronicle Publication State values are:

```text
not_published
pending_publication
published
withdrawn_from_publication
```

Not every Source Record must be public merely because an associated Chronicle Entry is public.

---

## `published_record_at`

Date and time the Source Record itself was published by Chronicle.

**Requirement:** Conditional.

Required when `publication_state` is:

```text
published
```

This field is distinct from the Source's own `published_at`.

---

# Versioning

## `source_record_version`

Sequential Version of the Source Record.

**Requirement:** Required.

Material Source Record changes should create a new Version when a future reviewer would reasonably need to know that the prior Source Record said something materially different.

Examples:

* Source attribution changes
* Source identity changes
* Provenance changes
* archive representation changes
* material limitation changes
* authoritative-reference changes

---

## `prior_version_reference`

Reference to the immediately prior preserved Source Record Version.

**Requirement:** Conditional.

Required for Version 2 and later when prior Version linkage is represented directly.

Prior substantive Source Record states should remain preserved.

---

# Corrections

A Source Record may be corrected through Chronicle's Correction architecture.

Material Corrections should preserve:

```text
Original information
Corrected information
Correction date
Reason
Affected fields
Resulting Version
```

Chronicle must not silently rewrite material Source identity, attribution, Provenance, limitations, or archival context.

---

# Discovery Fields

## `tags`

Optional discovery metadata.

**Requirement:** Optional.

Tags should not replace Source Type or later approved Source Role values.

---

## `jurisdiction`

Geographic, legal, organizational, or operational scope associated with the Source.

**Requirement:** Optional / Conditional.

Where important, Chronicle should prefer stable identifiers or authoritative references over ambiguous free text.

---

# Fields Intentionally Not Frozen

The following concepts remain intentionally provisional:

```text
source_role
preservation_state
validation_state location
source_record identifier namespace
```

They should not be turned into production Controlled Values merely to make the schema appear complete.

Production experience should determine whether they are necessary.

---

# Deprecated Legacy Concepts

The following older draft concepts should not govern production Source Records.

## Legacy Source Type vocabulary

Do not use older ad hoc values such as:

```text
webpage
document
publication
database
public_record
interview
broadcast
social_post
authoritative_suite_record
other_approved
```

unless they map to an approved Source Type.

Use the current Controlled Values instead.

---

## `access_timestamp`

Deprecated as an ambiguous universal time field.

Use:

```text
original_created_at
published_at
accessed_at
captured_at
created_at
```

according to meaning.

---

## `verification_status`

Deprecated.

Use:

```text
verification_state
```

---

## Generic `version`

Deprecated.

Use:

```text
schema_version
source_record_version
```

---

## Universal `author`

Deprecated.

Use explicit fields such as:

```text
creator
publisher
```

where applicable.

---

# Production Example

The following example demonstrates the current production architecture.

The Source Record identifier remains illustrative until its namespace is formally established.

```yaml
source_id: <SOURCE-IDENTIFIER>
schema_id: chronicle-source-record
schema_version: 1.0.0
source_record_version: 1

title: Satoshium Chronicle Public Launch Page

description: >
  Public Satoshium webpage documenting Chronicle.

source_type: web_page

creator: Satoshium
publisher: Satoshium

published_at: 2026-09-01T00:00:00Z
accessed_at: 2026-09-01T09:00:00Z
captured_at: 2026-09-01T09:05:00Z

source_location: https://example.com/chronicle

provenance:
  origin: satoshium_web
  acquisition_method: direct_web_access
  retrieved_at: 2026-09-01T09:00:00Z

related_entry_references:
  - CHR-2026-0001

verification_state: not_reviewed

publication_state: not_published

created_at: 2026-09-01T09:10:00Z
```

This example does not establish a permanent Source Record identifier format.

---

# Source Record Creation Test

A separate Source Record should ordinarily be created when one or more of the following are true:

* structured identity is required
* attribution is material
* limitations are material
* Provenance is complex
* the Source is reused across Entries
* archival context matters
* integrity metadata matters
* independent Versioning is required
* an Event-Type Profile requires it
* Validation requires it
* public Source discovery is needed

Otherwise a direct Source reference may be sufficient.

---

# Source Record Lifecycle

A generalized operational path may be:

```text
Source Identified
      ↓
Need for Source Record Assessed
      ↓
Source Record Created
      ↓
Source Type Assigned
      ↓
Attribution / Dates / References Recorded
      ↓
Provenance Recorded
      ↓
Entry / Evidence Linkage Established
      ↓
Limitations / Integrity Recorded
      ↓
Verification where Applicable
      ↓
Validation
      ↓
Use / Publication / Maintenance
      ↓
Correction / Versioning when Necessary
      ↓
Historical Preservation
```

Not every Source Record will require public publication or separate Verification.

---

# Authority Boundary

Chronicle Source Records document Sources.

They do not replace institutional authority.

Examples:

* Certification Package remains authoritative within Certifier.
* SREG Registry Entry remains authoritative within Registry.
* Integrity Reference remains authoritative within Anchor.
* Trust Statement remains authoritative within Attestor.
* Workflow Definition remains authoritative within Navigator.
* Atlas records remain authoritative within Atlas.

Chronicle may document those objects through Source Records.

Authority remains where it originated.

---

# Validation Expectations

A production Source Record should ultimately be validated against:

* Source Record Schema
* Source Record identifier rules
* required fields
* Source Type Controlled Values
* reference integrity
* Provenance requirements
* related Entry references
* related Evidence references
* Versioning rules
* publication prerequisites

Source Role should not be validated against a frozen vocabulary until Source Role is formally governed.

---

# Schema Versioning and Compatibility

Every production Source Record should remain associated with the Source Record Schema Version that governed it.

Schema evolution should preserve:

* Schema identity
* Schema Version
* compatibility classification
* deprecation history
* migration guidance
* Validation behavior
* historical interpretability

Older Source Records should remain understandable under the schema Version that originally governed them.

---

# Design Principles

## Source Identity First

A Source Record exists to identify and trace a Source.

## Source ≠ Evidence

Source and Evidence remain distinct.

## Provenance Is Required

A Source Record without information-path traceability is institutionally incomplete.

## Stable Reference Over Bare URL

Prefer durable identity where possible.

## Authority Remains External

Chronicle does not become authoritative for an external object by documenting it.

## Controlled Source Types

Production Source Type values come from the Controlled Values Registry.

## Source Role Remains Provisional

Do not freeze Source Role prematurely.

## Preserve Limitations

Uncertainty and Source weakness remain visible.

## Preserve Prior States

Material Source Record changes remain Versioned and traceable.

---

# Guiding Principle

> Identify the Source. Preserve the reference. Trace the path. Keep authority visible.

---

## Status

**Phase VII reconciled Chronicle Source Record Schema specification.**

The Source Record Schema is now aligned with:

* Chronicle Base Schema
* Source architecture
* Controlled Values Registry
* Provenance Model
* Relationship Model
* Verification Procedure
* Versioning Policy
* Corrections
* authority boundaries

The approved Source Type vocabulary is incorporated.

Source Role, Source Record identifier namespace, Preservation State, and the location of Validation results remain intentionally unresolved pending operational evidence.

A machine-readable `source-record-schema.json` should be created only after this human-readable specification is tested against the first production Source Record.
