# Chronicle Base Schema

## Purpose

The Chronicle Base Schema defines the common structural model for the canonical historical-preservation object of Satoshium Chronicle: the **Chronicle Entry**.

A Chronicle Entry represents one qualifying historical occurrence that has satisfied Chronicle Preservation Eligibility.

The Base Schema provides the universal structure shared by production Chronicle Entries while supporting:

* Stable identity
* Event or occurrence classification
* Temporal integrity
* Authoritative Suite references
* Historical context
* Relationships
* Provenance
* Evidence references
* Verification and validation
* Status
* Correction and version lineage
* Publication
* Long-term preservation

The Base Schema does not duplicate or redefine authoritative records owned by Certifier, Registry, Atlas, Anchor, Beacon, Attestor, Navigator, or another Suite system.

---

## Suite Alignment

The Chronicle Base Schema should implement the Satoshium Suite Standards, Methodology, Schemas Standard, and Interoperability principles within Chronicle.

The schema should support:

* Stable and durable objects
* Canonical terminology
* Machine-readable records
* Required and conditional fields
* Controlled values
* Durable identifiers and references
* Reference-based interoperability
* Provenance and traceability
* Validation-ready structures
* Schema versioning and evolution
* Historical preservation of prior schema states

Chronicle should reference authoritative Suite objects rather than copying their internal schemas into Chronicle.

---

## Canonical Object

The Chronicle Entry is the canonical Chronicle object.

The occurrence is what happened.

The Chronicle Entry is Chronicle's structured preservation record of that qualifying occurrence.

Conceptually:

```text
Occurrence
    ↓
Preservation Eligibility
    ↓
Chronicle Entry
```

The schema should not create separate canonical objects for event entries, publication entries, observation entries, milestone entries, investigation entries, or similar historical subjects.

Those distinctions belong in controlled classifications such as **Event Type** and, where needed, specialized **Event-Type Profiles**.

---

## Base Schema and Event-Type Profiles

The Chronicle Base Schema contains only fields that apply across Chronicle Entries generally.

Specialized occurrence classes may extend the Base Schema through Event-Type Profiles.

Conceptually:

```text
Chronicle Base Schema
        +
Event-Type Profile
        =
Specialized Chronicle Entry
```

The first anticipated Event-Type Profile is the **Certification Event-Type Profile**.

That profile may add certification-specific requirements such as:

* Certifier as originating system
* Certification event type
* Authoritative Certification Package reference
* Related SREG reference
* Certification-specific relationship rules
* Certification-specific validation requirements

An Event-Type Profile extends the Base Schema.

It does not create a second canonical Chronicle object.

---

## Schema Questions

Every Chronicle Entry should be able to answer, directly or through structured references:

* What occurrence is being preserved?
* What type of occurrence is it?
* When did the occurrence happen?
* When did Chronicle create the Entry?
* Why did the occurrence qualify for preservation?
* Which system or institution originated the occurrence?
* Which authoritative record establishes the underlying action or state?
* Which sources and evidence provide context?
* What provenance explains how information entered Chronicle?
* Which related Chronicle Entries or Suite objects provide historical context?
* What is the current verification state?
* Has the Entry passed validation?
* What is the publication state?
* Which schema version governs the Entry?
* Has the Entry been corrected or versioned?

---

# Field Architecture

The exact production field names and identifier format remain subject to the Chronicle Identifier Architecture, Controlled Values, Validation Rules, and Publication Standard.

The fields below define the **working structural model**, not a final frozen production schema.

---

## Identity Fields

### `entry_id`

Stable unique identifier assigned to the Chronicle Entry.

**Status:** Required in production.

The final identifier format is not yet settled and should not be assumed by this specification.

Example placeholder:

```text
<CHRONICLE-IDENTIFIER>
```

Do not treat legacy examples such as `CHR-ENTRY-000001` as canonical.

---

### `schema_version`

Version of the Chronicle Base Schema governing the Entry.

**Status:** Required in production.

Example:

```text
1.0.0
```

The final versioning convention will be governed by Chronicle schema-versioning rules.

---

### `title`

Concise human-readable title describing the preserved occurrence.

**Status:** Required.

Example:

```text
Creation of SC-CERT-2026-0001
```

---

### `summary`

Brief factual summary of the preserved occurrence.

**Status:** Required.

Example:

```text
Satoshium Certifier created the authoritative Certification Package identified as SC-CERT-2026-0001 on July 5, 2026.
```

---

## Occurrence Classification Fields

### `event_type`

Controlled classification identifying the type of occurrence represented by the Entry.

**Status:** Required.

The allowed values should come from Chronicle Controlled Values or the applicable Event-Type Profile.

Example:

```text
certification_created
```

Legacy `entry_type` values such as:

```text
event
publication
observation
decision
milestone
investigation
correction
reference
```

should not be treated as the canonical classification model.

Chronicle uses one canonical Entry object and classifies the represented occurrence.

---

### `event_type_profile`

Reference to the Event-Type Profile governing the Entry, when applicable.

**Status:** Conditional.

Example:

```text
certification-event-profile
```

---

## Preservation Eligibility Fields

### `preservation_eligibility`

Structured indication that the occurrence satisfied Chronicle Preservation Eligibility.

**Status:** Required in production.

The exact controlled values and representation remain to be defined.

Possible future concepts may include:

```text
eligible
not_eligible
reassessed_eligible
```

These values are illustrative only and are not yet canonical.

---

### `preservation_basis`

Reason the occurrence qualified for preservation.

**Status:** Required or conditional depending on final rules.

Potential bases may include:

* Approved preservation class
* Historical Significance
* Retrospective reassessment
* Other approved Chronicle rule

The final controlled values remain to be defined.

---

### `historical_significance`

Structured or narrative explanation of why the occurrence is historically relevant when Historical Significance is part of the preservation basis.

**Status:** Conditional.

This field should not be reduced to an artificial numeric significance score.

---

## Temporal Fields

### `event_date`

Date or timestamp associated with the historical occurrence itself.

**Status:** Required when determinable.

Example:

```text
2026-07-05
```

Chronicle should preserve the distinction between event time and Chronicle record-maintenance time.

---

### `entry_created_at`

Date and time Chronicle created the Entry.

**Status:** Required.

Example:

```text
2026-09-01T12:30:00Z
```

---

### `published_at`

Date and time the Entry was publicly published.

**Status:** Conditional until publication.

---

### `updated_at`

Most recent non-historical maintenance timestamp for the current Entry state.

**Status:** Conditional.

This field should not replace correction or version lineage.

---

## Origin and Authority Fields

### `originating_system`

Controlled identifier for the Suite system, institution, or external source associated with the occurrence.

**Status:** Required where applicable.

Examples may include:

```text
certifier
registry
anchor
beacon
attestor
navigator
atlas
```

Final values must come from Chronicle Controlled Values.

---

### `authoritative_record_references`

Durable references to authoritative Suite objects or institutional records that establish the underlying action, state, or occurrence.

**Status:** Required when an authoritative record exists.

Examples may include:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Trust Statement
* Workflow Definition
* Atlas record

Chronicle references these objects.

Chronicle does not duplicate or redefine them.

---

## Historical Context Fields

### `description`

Extended factual narrative describing the occurrence.

**Status:** Optional or recommended depending on Event-Type Profile.

---

### `historical_context`

Context needed to understand the occurrence within the broader historical sequence.

**Status:** Recommended and may become required for selected Event-Type Profiles.

This field should remain distinguishable from authoritative facts and source material.

---

## Source and Evidence Fields

### `source_references`

References to sources used to establish or contextualize the Chronicle Entry.

**Status:** Conditional.

Sources identify where information originated.

---

### `evidence_references`

References to evidence records or evidence items relevant to the Entry.

**Status:** Conditional.

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Contextualize

The evidence relationship should be explicit where practical.

---

## Provenance Fields

### `provenance`

Structured information describing where the Entry's information came from and how it entered Chronicle.

**Status:** Expected to become required in production.

Provenance may include:

* Originating system
* Source path
* Acquisition or observation method
* Record creation context
* Evidence origin
* Archival reference
* Preservation information

The final provenance structure will be governed by the Chronicle Provenance Model.

---

## Relationship Fields

### `relationships`

Structured relationships between the Entry and:

* Other Chronicle Entries
* Authoritative Suite objects
* Supporting Chronicle records
* Related historical occurrences

**Status:** Conditional.

Relationship values should use Chronicle Controlled Values.

Possible concepts may include:

```text
references
originated_from
registered_as
anchored_by
attested_by
precedes
follows
related_to
superseded_by
corrected_by
version_of
```

These are working concepts only until controlled values are formally approved.

Chronicle relationships should not imply unsupported causation or transfer institutional authority.

---

## Verification Fields

### `verification_state`

Current Chronicle verification state.

**Status:** Required or conditional according to final lifecycle rules.

The final controlled values remain to be defined.

Legacy examples such as:

```text
unverified
under_review
partially_verified
verified
disputed
```

should be treated as historical draft vocabulary, not approved controlled values.

---

### `verification_references`

References to Chronicle verification records or activities.

**Status:** Conditional.

Chronicle verification reviews Chronicle's own historical representation.

It does not re-adjudicate determinations made by another Suite system.

---

## Validation Fields

### `validation_state`

State or result of Chronicle validation.

**Status:** Required before production publication.

Validation concerns structural and procedural conformance.

It may include:

* Identifier integrity
* Schema conformance
* Required fields
* Controlled values
* Authoritative references
* Relationship integrity
* Provenance requirements
* Version linkage
* Publication readiness

Verification and Validation are separate functions.

---

### `validation_references`

References to validation results or records where Chronicle preserves them separately.

**Status:** Conditional.

---

## Lifecycle and Publication Fields

### `entry_status`

Current Chronicle lifecycle state.

**Status:** Required.

The final controlled values remain to be defined.

Legacy values such as:

```text
draft
active
archived
superseded
corrected
```

should not be assumed to be canonical.

---

### `publication_state`

Current publication state of the Entry.

**Status:** Required for production use.

The final values remain to be defined.

Lifecycle state and publication state should remain separate where they represent different institutional concepts.

---

## Version and Correction Fields

### `entry_version`

Version or preserved state of the Chronicle Entry.

**Status:** Required if Chronicle adopts explicit Entry-level semantic versioning or state versioning.

The final convention remains to be defined.

---

### `prior_version_reference`

Reference to the prior preserved Entry state where applicable.

**Status:** Conditional.

---

### `correction_references`

References to Chronicle correction records affecting the Entry.

**Status:** Conditional.

Corrections apply to Chronicle's own record.

They do not modify authoritative records maintained by another Suite system.

---

## Optional Discovery Fields

### `tags`

Optional discovery metadata.

**Status:** Optional.

Tags should not replace controlled Event Types or relationships.

---

### `jurisdiction`

Optional geographic, organizational, legal, or operational scope where the occurrence requires it.

**Status:** Conditional.

Where jurisdiction is represented, Chronicle should prefer stable controlled or authoritative references over ambiguous free text.

---

## Deprecated Legacy Fields

The following concepts from the original draft should not be carried forward unchanged:

### `entry_type`

Deprecated as the primary occurrence model.

Use `event_type` or another approved controlled classification instead.

### `recorded_timestamp`

Deprecated as an ambiguous term.

Use specific timestamps such as:

* `event_date`
* `entry_created_at`
* `published_at`
* `updated_at`

### `author`

Deprecated as a universal field.

Chronicle should distinguish among:

* originating system
* record creator
* reviewer
* validator
* publisher

if and when those actor roles become operationally necessary.

### Generic `version`

Deprecated as ambiguous.

Use schema-specific and Entry-specific version concepts separately, such as:

* `schema_version`
* `entry_version`

---

# Working Example

The following is a **conceptual example only**.

It does not establish the final Chronicle identifier format, controlled values, or production schema.

```yaml
entry_id: <CHRONICLE-IDENTIFIER>
schema_version: 1.0.0

title: Creation of SC-CERT-2026-0001

summary: >
  Satoshium Certifier created the authoritative Certification
  Package identified as SC-CERT-2026-0001 on July 5, 2026.

event_type: certification_created
event_type_profile: certification-event-profile

preservation_eligibility: eligible
preservation_basis:
  - approved_event_type
  - historical_significance

historical_significance: >
  First production certification created by Satoshium Certifier.

event_date: 2026-07-05
entry_created_at: <CHRONICLE-CREATION-TIMESTAMP>

originating_system: certifier

authoritative_record_references:
  - SC-CERT-2026-0001

relationships:
  - type: registered_as
    target: SREG-2026-0001

source_references: []
evidence_references: []

verification_state: <CONTROLLED-VALUE>
validation_state: <CONTROLLED-VALUE>
entry_status: <CONTROLLED-VALUE>
publication_state: <CONTROLLED-VALUE>

entry_version: <VERSION>
```

This example intentionally avoids inventing final values that have not yet been architecturally approved.

---

## Validation Expectations

A production Chronicle Entry should ultimately be validated against:

* Chronicle Base Schema
* Applicable Event-Type Profile
* Chronicle Controlled Values
* Identifier rules
* Relationship rules
* Provenance requirements
* Required authoritative references
* Versioning requirements
* Publication requirements

A record may be historically meaningful but still fail structural validation.

A structurally valid Entry may also contain limited or disputed evidence.

---

## Schema Versioning and Compatibility

Every production Chronicle Entry should remain associated with the schema version that governed it.

Schema evolution should define:

* Version identity
* Backward compatibility
* Breaking changes
* Deprecation
* Migration
* Historical preservation
* Validation behavior for older Entries

Older Chronicle Entries should remain interpretable under the schema version that originally governed them.

Schema updates should not silently rewrite historical structures.

---

## Design Goals

The Chronicle Base Schema should:

* Preserve the canonical Chronicle Entry model
* Support historical context
* Maintain temporal integrity
* Preserve authority boundaries
* Support reference-based interoperability
* Support provenance
* Support evidence-aware review
* Support structured relationships
* Enable verification
* Enable validation
* Preserve correction and version lineage
* Support public publication
* Support long-term archival preservation
* Remain understandable to humans and machines
* Avoid unnecessary schema proliferation

---

## Future Development

Future Chronicle schema work may include:

* Final Chronicle Identifier Architecture
* Formal Chronicle Base Schema in machine-readable form
* Certification Event-Type Profile
* Controlled Values
* Evidence Record Schema
* Verification Record Schema
* Correction Record Schema
* Provenance structures
* Relationship structures
* Version structures
* Publication structures
* Automated validation
* Cryptographic integrity metadata
* Event-Type Profiles for additional Suite systems

---

## Status

**Architectural draft — not yet a frozen production schema.**

This document has been reconciled with the current Satoshium Suite Standards, Methodology, Schemas Standard, Interoperability architecture, and the Chronicle decisions establishing Chronicle Entry as the canonical object.

The final field names, identifier format, controlled values, required/conditional/optional designations, versioning conventions, validation rules, and Event-Type Profile structures must be settled through the remaining Chronicle operational-development steps before this schema becomes production authoritative.
