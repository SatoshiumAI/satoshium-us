# Chronicle Source Record Schema

## Purpose

The Chronicle Source Record Schema defines the structure used to represent sources referenced or maintained by Satoshium Chronicle.

A Source Record identifies where information originated and preserves the context needed to trace that information back to its source.

Sources may contain or lead to:

* Evidence
* Claims
* Statements
* Records
* Publications
* Observations
* Metadata
* Archival material
* Authoritative Suite objects
* Other historical context

A source does not determine truth merely because Chronicle references it.

The Source Record exists to preserve origin, attribution, access context, provenance, archival state, and relationships so the information used by Chronicle can be reviewed, compared, verified, challenged, corrected, and preserved over time.

---

## Suite Alignment

Chronicle Source Records should align with the Satoshium Suite Standards, Methodology, Schemas Standard, Evidence Standard, and Interoperability principles.

The schema should support:

* Stable identifiers
* Clear source attribution
* Provenance and traceability
* Durable references
* Archival preservation
* Source limitations
* Structured relationships
* Validation-ready records
* Version preservation
* Reference-based interoperability
* Clear authority boundaries

Chronicle should not create a competing source-authority model where another Suite system already owns the authoritative object.

---

## Canonical Role

A Source Record is a **supporting Chronicle-owned record**.

It is not the canonical historical-preservation object.

The canonical Chronicle object remains the **Chronicle Entry**.

Conceptually:

```text
Chronicle Entry
      ↓
Source Relationship
      ↓
Source Record
      ↓
Evidence / Provenance / Verification Context
```

A Source Record exists to document where information came from and how Chronicle can trace it.

---

## Source, Evidence, and Provenance

Source, Evidence, and Provenance are related but distinct.

### Source

Answers:

> Where did the information come from?

### Evidence

Answers:

> What material bears on the Chronicle Entry, claim, or occurrence?

Evidence may support, challenge, contradict, clarify, corroborate, contextualize, or limit confidence.

### Provenance

Answers:

> How did the information or evidence originate, move, and enter Chronicle?

A single source may contain multiple evidence items.

A single evidence item may depend on one or more sources.

A Source Record should not be used as a substitute for Evidence or Provenance Records where those functions require separate structure.

---

## Schema Overview

A Chronicle Source Record should answer:

* What is the source?
* What type of source is it?
* Where is it located?
* Who or what created or published it?
* When was it created or published?
* When was it accessed or captured?
* How did Chronicle obtain or preserve the source?
* Which Chronicle Entries rely on it?
* Which Evidence Records derive from or relate to it?
* Is the source itself an authoritative Suite object?
* What limitations or conflicts are known?
* What archival or integrity information is available?
* Has Chronicle verified aspects of the source?
* Has the Source Record passed structural validation?

---

# Field Architecture

The exact production identifier format, controlled values, and required/conditional designations remain subject to Chronicle Identifier Architecture, Controlled Values, Validation Rules, Provenance Model, Source procedures, and Publication Standard.

The structure below is an operational architectural draft.

---

## Identity Fields

### `source_id`

Stable unique identifier assigned to the Chronicle Source Record.

**Status:** Required in production.

The final identifier format is not yet settled.

Example placeholder:

```text
<SOURCE-IDENTIFIER>
```

Legacy examples such as `SRC-000001` should not be treated as canonical.

---

### `schema_version`

Version of the Source Record Schema governing the record.

**Status:** Required.

Example:

```text
1.0.0
```

Schema version and Source Record version should remain distinct concepts.

---

### `title`

Concise human-readable title describing the source.

**Status:** Required.

Example:

```text
Satoshium Chronicle Public Launch Page
```

---

### `description`

Brief factual description of the source.

**Status:** Required.

Example:

```text
Public Satoshium webpage documenting the Chronicle launch.
```

---

## Source Classification Fields

### `source_type`

Controlled classification identifying the type of source.

**Status:** Required.

Possible working concepts may include:

```text
webpage
document
publication
archive
database
public_record
institutional_record
statement
interview
broadcast
repository
dataset
social_post
authoritative_suite_record
other_approved
```

These values are illustrative only until Chronicle Controlled Values are formally approved.

The Source Record Schema should not assume that all legacy categories remain canonical.

---

### `source_role`

Controlled value describing the source's role in relation to the Chronicle Entry or Evidence Record.

**Status:** Conditional.

Potential working concepts may include:

```text
primary_source
secondary_source
contextual_source
archival_source
authoritative_source
corroborating_source
reference_source
```

These values remain provisional.

Source type and source role should remain distinct concepts.

---

## Creator and Publisher Fields

### `creator`

Entity, person, organization, institution, or system that created the source.

**Status:** Conditional.

---

### `publisher`

Entity, person, organization, institution, or system that published or distributed the source.

**Status:** Conditional.

Creator and publisher may be the same entity but should not be assumed to be identical.

---

## Temporal Fields

### `original_created_at`

Date or timestamp associated with creation of the source, when known.

**Status:** Conditional.

---

### `published_at`

Date or timestamp associated with publication or release of the source, when applicable.

**Status:** Conditional.

---

### `accessed_at`

Date or timestamp when Chronicle or another documented process accessed the source.

**Status:** Conditional.

---

### `captured_at`

Date or timestamp when Chronicle or another documented process captured or archived the source.

**Status:** Conditional.

These timestamps should remain distinct where the events differ.

Legacy use of one universal `access_timestamp` should not collapse creation, publication, access, and capture into a single concept.

---

## Location and Reference Fields

### `source_location`

Durable location or reference where the source can be found.

**Status:** Required when a location or reference exists.

Examples may include:

```text
https://...
repository://...
archive://...
```

The final permitted formats should be governed by Chronicle reference rules.

---

### `archive_reference`

Reference to an archived or preserved representation of the source.

**Status:** Conditional.

---

### `authoritative_record_reference`

Reference to an authoritative Suite object when the source itself is an authoritative institutional record.

**Status:** Conditional.

Examples may include:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Trust Statement
* Workflow Definition
* Atlas record

Chronicle may reference such objects as sources while preserving their distinct institutional authority.

---

## Provenance Fields

### `provenance`

Structured information describing how the source originated, moved, was discovered, accessed, captured, archived, and entered Chronicle.

**Status:** Expected to become required in production.

Provenance may include:

* Originating institution
* Discovery method
* Acquisition path
* Access method
* Capture method
* Archive path
* Transfer history
* Preservation history
* Related authoritative record

The final structure will be governed by the Chronicle Provenance Model.

---

## Relationship Fields

### `related_entry_references`

References to Chronicle Entries associated with the source.

**Status:** Required when the Source Record supports or contextualizes a Chronicle Entry.

---

### `related_evidence_references`

References to Evidence Records derived from or associated with the source.

**Status:** Conditional.

---

### `related_correction_references`

References to Correction Records involving this Source Record or its relationship to Chronicle.

**Status:** Conditional.

---

### `related_source_references`

References to related Source Records.

**Status:** Conditional.

Relationships should use Chronicle controlled relationship values where direction or meaning matters.

---

## Source Reliability and Limitations

### `reliability_notes`

Structured or narrative notes regarding reliability, conflicts, context, or known weaknesses.

**Status:** Conditional.

This field should not be treated as an institutional truth determination.

---

### `limitations`

Structured or narrative description of known source limitations.

**Status:** Required when material limitations exist.

Examples may include:

* Incomplete
* Stale
* Unavailable
* Archived copy only
* Ambiguous authorship
* Broken reference
* Conflicting publication date
* Secondary or derivative source
* Missing provenance
* Context-limited
* Altered or reformatted representation

Source limitations should remain visible over time.

---

## Integrity and Preservation Fields

### `checksum`

Cryptographic checksum or digest for preserved source material where available.

**Status:** Optional or conditional.

Example:

```text
sha256:<HASH>
```

---

### `digital_signature_reference`

Reference to a digital signature, attestation, or signature-verification artifact.

**Status:** Conditional.

---

### `preservation_status`

Controlled value describing the source's preservation condition.

**Status:** Expected to become required.

Potential working concepts may include:

```text
available
archived
captured_copy
referenced_only
unavailable
superseded
preserved_copy
```

These values remain provisional.

---

### `preservation_notes`

Notes describing archival state, capture method, source availability, preservation limitations, or long-term accessibility.

**Status:** Conditional.

---

## Verification Fields

### `verification_state`

Current Chronicle verification state relating to the Source Record.

**Status:** Conditional.

The final controlled values remain to be defined.

Legacy values such as:

```text
unverified
under_review
partially_verified
verified
disputed
unavailable
```

should be treated as historical draft vocabulary, not approved controlled values.

---

### `verification_references`

References to Chronicle verification records or activities.

**Status:** Conditional.

Verification may review:

* Source existence
* Attribution
* Creator or publisher identity
* Publication date
* Access or capture consistency
* Archival consistency
* Provenance
* Relationship integrity
* Internal consistency
* Source limitations

Verification does not convert the source into Chronicle authority.

---

## Validation Fields

### `validation_state`

State or result of Chronicle Source Record validation.

**Status:** Required before production publication or operational use where validation is required.

Validation may include:

* Identifier integrity
* Schema conformance
* Required fields
* Controlled values
* Source-location integrity
* Archive-reference integrity
* Related-entry integrity
* Provenance requirements
* Preservation-status requirements
* Version linkage
* Publication readiness

Verification and Validation are separate functions.

---

### `validation_references`

References to validation records or results where Chronicle preserves them separately.

**Status:** Conditional.

---

## Lifecycle and Publication Fields

### `source_status`

Current lifecycle state of the Chronicle Source Record.

**Status:** Required.

The final controlled values remain to be defined.

Legacy values such as:

```text
draft
active
archived
superseded
unavailable
```

should not be assumed to be canonical.

---

### `publication_state`

Current publication state of the Source Record.

**Status:** Conditional or required depending on Chronicle publication architecture.

Not every source reference or preserved source should necessarily be public.

---

## Versioning Fields

### `source_record_version`

Version or preserved state of the Chronicle Source Record.

**Status:** Required if Chronicle adopts explicit Source Record versioning.

---

### `prior_version_reference`

Reference to the prior Source Record state where applicable.

**Status:** Conditional.

Material changes to source location, provenance, limitations, preservation status, or attribution should remain traceable.

---

## Discovery Fields

### `tags`

Optional discovery metadata.

**Status:** Optional.

Tags should not replace controlled source type or source role values.

---

### `jurisdiction`

Optional geographic, organizational, legal, or operational scope associated with the source.

**Status:** Conditional.

Where jurisdiction matters, Chronicle should prefer controlled or authoritative references over ambiguous free text.

---

## Deprecated Legacy Fields

The following concepts from the original draft should not be carried forward unchanged:

### `access_timestamp`

Deprecated as a universal temporal field.

Use more precise timestamps such as:

* `original_created_at`
* `published_at`
* `accessed_at`
* `captured_at`

### `verification_status`

Deprecated in favor of:

```text
verification_state
```

once controlled values are settled.

### `verification_reference`

Deprecated in favor of:

```text
verification_references
```

to support one or more verification records.

### `author`

Deprecated as a universal field.

Use explicit actor-role fields where needed.

### Generic `version`

Deprecated as ambiguous.

Use:

* `schema_version`
* `source_record_version`

as separate concepts.

---

# Working Example

The following is conceptual only and does not establish final identifiers, controlled values, or production field names.

```yaml
source_id: <SOURCE-IDENTIFIER>
schema_version: 1.0.0

title: Satoshium Chronicle Public Launch Page

description: >
  Public Satoshium webpage documenting the Chronicle launch.

source_type: webpage
source_role: primary_source

creator: Satoshium
publisher: Satoshium

published_at: 2026-09-01T00:00:00Z
accessed_at: 2026-09-01T09:00:00Z
captured_at: 2026-09-01T09:05:00Z

source_location: https://example.com/chronicle
archive_reference: <ARCHIVE-REFERENCE>

provenance:
  acquisition_method: direct_web_access
  capture_method: archival_capture

related_entry_references:
  - <CHRONICLE-ENTRY-ID>

related_evidence_references:
  - <EVIDENCE-RECORD-ID>

limitations: []

preservation_status: <CONTROLLED-VALUE>
verification_state: <CONTROLLED-VALUE>
validation_state: <CONTROLLED-VALUE>
source_status: <CONTROLLED-VALUE>
publication_state: <CONTROLLED-VALUE>

source_record_version: <VERSION>
```

This example intentionally avoids inventing final values that have not yet been architecturally approved.

---

## Source and Evidence Distinction

Sources and evidence remain separate concepts.

A Source Record identifies origin.

An Evidence Record describes material that bears on the Chronicle Entry or claim.

Examples:

* A webpage may be a source.
* A screenshot captured from that webpage may be evidence.
* A Certification Package may be an authoritative Suite source and may also provide strong evidentiary support.
* A news article may be a source containing multiple claims, quotations, images, or other evidence.

Chronicle should preserve the distinction instead of treating every source as evidence or every evidence item as a source.

---

## Source and Authority Distinction

Some sources are authoritative within another Suite system.

For example:

* A Certification Package is authoritative within Certifier for its certification determination.
* An SREG Registry Entry is authoritative within Registry for its catalog record.
* An Integrity Reference is authoritative within Anchor for anchoring.
* A Trust Statement is authoritative within Attestor for attestation.

Chronicle may reference these objects as sources.

Their authority comes from the originating system, not from Chronicle's Source Record.

A Source Record should preserve that distinction explicitly.

---

## Source Record Lifecycle

A generalized Source Record lifecycle may include:

1. Source identified
2. Source type and role classified
3. Creator and publisher documented
4. Temporal information recorded
5. Source location established
6. Provenance documented
7. Entry and Evidence relationships established
8. Limitations documented
9. Integrity or archival information recorded
10. Verification performed where applicable
11. Validation performed
12. Source Record published, retained privately, or otherwise applied according to Chronicle rules
13. Source Record maintained
14. Corrections or versioning applied when necessary
15. Preservation status maintained

Not every Source Record will require every step.

---

## Preservation Principles

Chronicle should preserve durable source references and source context whenever practical.

Where direct source preservation is appropriate and permitted:

* Original material should remain available
* Archive references should remain maintained
* Provenance should remain documented
* Integrity information should remain available
* Source limitations should remain visible
* Relationships to Entries and Evidence should remain intact
* Prior substantive Source Record states should remain traceable

Where direct preservation is not appropriate or possible, Chronicle should preserve enough durable reference, metadata, provenance, archival information, and preservation context to support future review.

A source becoming unavailable should not silently erase its historical role.

---

## Design Goals

The Chronicle Source Record Schema should:

* Preserve information origin
* Support attribution
* Maintain provenance
* Preserve source limitations
* Maintain archival context
* Support source/evidence distinction
* Preserve authority boundaries
* Support verification
* Support validation
* Maintain traceability
* Support version lineage
* Support long-term historical preservation
* Remain machine-readable and durable

---

## Future Development

Future Chronicle Source Schema work may include:

* Final Source Record identifier architecture
* Controlled source types
* Controlled source-role values
* Formal provenance structures
* Source validation rules
* Archival-reference structures
* Automated source capture
* Automated archive integration
* Integrity metadata
* Cryptographic timestamping
* Source availability monitoring
* Cross-system reference validation
* Public source discovery where appropriate

---

## Status

**Architectural draft — not yet a frozen production schema.**

This document has been reconciled with the current Chronicle Source architecture, Chronicle Evidence architecture, Chronicle Records model, Chronicle Base Schema direction, and Satoshium Suite Standards, Methodology, Schemas Standard, Evidence Standard, and Interoperability principles.

The final identifier format, controlled values, source-role vocabulary, provenance requirements, validation rules, preservation-status values, versioning conventions, and publication requirements must be settled through the remaining Chronicle operational-development steps before this schema becomes production authoritative.
