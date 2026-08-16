# Chronicle Correction Record Schema

## Purpose

The Chronicle Correction Record Schema defines the structure used to document corrections to Chronicle-owned records.

Corrections may address factual errors, metadata defects, incomplete references, provenance issues, relationship errors, evidence updates, or other documented problems within Chronicle's own historical-preservation record.

Chronicle corrections are intended to improve accuracy, transparency, traceability, and historical continuity while preserving prior substantive states.

Chronicle does **not** use correction records to alter authoritative objects owned by Certifier, Registry, Atlas, Anchor, Beacon, Attestor, Navigator, or another Suite system.

If an originating Suite system changes its own authoritative object, Chronicle may preserve that later occurrence and update its own references according to Chronicle rules.

---

## Suite Alignment

Chronicle Correction Records should align with the Satoshium Suite Standards, Methodology, Schemas Standard, Evidence Standard, and Interoperability principles.

The schema should support:

* Stable identifiers
* Clear authority boundaries
* Reference-based interoperability
* Provenance and traceability
* Evidence-aware review
* Validation-ready structure
* Version preservation
* Durable correction lineage
* Structured publication state
* Repeatable correction procedures

---

## Canonical Role

A Correction Record is a **supporting Chronicle-owned record**.

It is not the canonical historical-preservation object.

The canonical Chronicle object remains the **Chronicle Entry**.

A Correction Record documents a change to a Chronicle Entry or another Chronicle-owned supporting record.

Conceptually:

```text
Chronicle Record
      ↓
Issue Identified
      ↓
Correction Review
      ↓
Correction Record
      ↓
Versioned / Corrected Chronicle State
      ↓
Validation
      ↓
Publication / Preservation
```

---

## Schema Overview

A Chronicle Correction Record should answer:

* Which Chronicle-owned record is affected?
* What issue was identified?
* What changed?
* Why was the change necessary?
* Which prior state or field value is affected?
* What evidence or authoritative references support the correction?
* Who or what initiated the correction?
* Who or what reviewed it?
* Was the correction validated?
* Which corrected or versioned state resulted?
* When was the correction created and published?
* How can a reviewer reconstruct the prior and corrected states?

---

# Field Architecture

The exact production identifier format, controlled values, and required/conditional designations remain subject to Chronicle Identifier Architecture, Controlled Values, Validation Rules, Versioning Policy, and Publication Standard.

The structure below is an operational architectural draft.

---

## Identity Fields

### `correction_id`

Stable unique identifier assigned to the Correction Record.

**Status:** Required in production.

The final identifier format is not yet settled.

Example placeholder:

```text
<CORRECTION-IDENTIFIER>
```

Legacy examples such as `COR-000001` should not be treated as canonical.

---

### `schema_version`

Version of the Correction Record Schema governing the record.

**Status:** Required.

Example:

```text
1.0.0
```

Schema version and correction-record version should remain distinct concepts.

---

### `title`

Concise human-readable title describing the correction.

**Status:** Required.

Example:

```text
Correction to Chronicle Event Date
```

---

## Correction Classification Fields

### `correction_type`

Controlled classification describing the nature of the correction.

**Status:** Required.

Potential working concepts may include:

```text
factual
clarification
evidence_update
source_update
provenance_update
relationship_update
metadata
administrative
reclassification
substantive
```

These values are illustrative only until Chronicle Controlled Values are approved.

---

### `correction_scope`

Indicates whether the correction is:

* Non-substantive
* Substantive

**Status:** Expected to become required.

This distinction matters because substantive corrections should preserve a traceable versioned state.

---

## Affected Record Fields

### `affected_record_reference`

Stable reference to the Chronicle-owned record being corrected.

**Status:** Required.

Example placeholder:

```text
<CHRONICLE-ENTRY-OR-SUPPORTING-RECORD-ID>
```

A Correction Record should not use this field to imply that Chronicle owns an external Suite object.

---

### `affected_record_type`

Controlled classification of the affected Chronicle-owned record.

**Status:** Required or conditional.

Possible working values may include:

* Chronicle Entry
* Evidence Record
* Verification Record
* Provenance Record
* Relationship Record
* Other approved Chronicle support record

---

### `affected_fields`

Structured list of fields, relationships, or components affected by the correction.

**Status:** Required for substantive corrections and recommended otherwise.

Example:

```yaml
affected_fields:
  - event_date
  - historical_context
```

---

## Issue and Rationale Fields

### `issue_summary`

Brief description of the identified problem.

**Status:** Required.

Example:

```text
The event date in the published Chronicle Entry did not match the authoritative source record.
```

---

### `reason`

Detailed explanation of why the correction is necessary.

**Status:** Required.

---

### `impact`

Description of the effect of the correction on Chronicle's historical representation.

**Status:** Recommended.

The correction should indicate whether it:

* Changes historical meaning
* Changes temporal ordering
* Changes authoritative references
* Changes provenance
* Changes relationships
* Changes verification state
* Is purely editorial or administrative

---

## Change Documentation Fields

### `previous_state`

Structured representation or durable reference to the prior value or prior Chronicle state.

**Status:** Required for substantive corrections.

Example:

```text
2026-09-02
```

Where practical, Chronicle should prefer durable references to preserved prior versions rather than copying large prior records into the Correction Record.

---

### `corrected_state`

Structured representation or durable reference to the corrected value or new Chronicle state.

**Status:** Required.

Example:

```text
2026-09-01
```

---

### `change_summary`

Human-readable explanation of the change.

**Status:** Required.

Example:

```text
Event date corrected to match the authoritative publication record.
```

---

## Version Lineage Fields

### `prior_version_reference`

Reference to the prior preserved Chronicle state affected by the correction.

**Status:** Required for substantive corrections where versioning applies.

---

### `resulting_version_reference`

Reference to the corrected or newly versioned Chronicle state.

**Status:** Required for substantive corrections where versioning applies.

---

### `version_effect`

Controlled value describing the correction's effect on version lineage.

Possible working concepts:

```text
no_new_version
new_version
superseding_state
```

These values remain provisional.

---

## Temporal Fields

### `identified_at`

Date and time the issue was identified.

**Status:** Recommended.

---

### `correction_created_at`

Date and time the Correction Record was created.

**Status:** Required.

---

### `reviewed_at`

Date and time correction review was completed.

**Status:** Conditional.

---

### `validated_at`

Date and time correction validation was completed.

**Status:** Conditional.

---

### `published_at`

Date and time the correction or corrected state was published.

**Status:** Conditional until publication.

---

## Initiation and Review Fields

### `initiated_by`

Entity, role, process, or system that initiated the correction.

**Status:** Recommended.

Chronicle should eventually distinguish actor roles through controlled values rather than using one generic `author` field.

---

### `reviewed_by`

Entity, role, process, or system responsible for correction review.

**Status:** Conditional.

---

### `approved_by`

Entity, role, process, or system responsible for approval where Chronicle procedure requires approval.

**Status:** Conditional.

---

## Source and Evidence Fields

### `source_references`

References to sources relevant to the correction.

**Status:** Conditional.

---

### `evidence_references`

References to evidence supporting, challenging, or contextualizing the correction.

**Status:** Conditional.

Evidence should align with the Suite Evidence Standard.

---

### `authoritative_record_references`

References to authoritative Suite objects that establish the external fact, action, or state relevant to the correction.

**Status:** Required when the correction depends on an authoritative external record.

Examples may include:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Trust Statement
* Workflow Definition
* Atlas record

Chronicle references these objects but does not correct them.

---

## Provenance Fields

### `provenance`

Structured information describing how the correction issue, evidence, sources, and authoritative references entered Chronicle.

**Status:** Recommended and expected to become required for substantive corrections.

---

## Relationship Fields

### `related_entry_references`

References to Chronicle Entries related to the correction.

**Status:** Conditional.

---

### `related_correction_references`

References to other Correction Records connected to the same issue or lineage.

**Status:** Conditional.

---

### `relationship_updates`

Structured relationships added, removed, or modified by the correction.

**Status:** Conditional.

Relationship changes should use Chronicle controlled relationship values.

---

## Verification Fields

### `verification_state`

Chronicle verification state associated with the correction.

**Status:** Conditional.

The final values remain to be defined.

Verification reviews the support, consistency, evidence, references, provenance, and historical representation involved in the correction.

---

### `verification_references`

References to Chronicle verification records or activities.

**Status:** Conditional.

---

## Validation Fields

### `validation_state`

State or result of Chronicle correction validation.

**Status:** Required before publication of a substantive correction.

Validation may include:

* Identifier integrity
* Schema conformance
* Required fields
* Controlled values
* Affected-record reference integrity
* Prior-version linkage
* Resulting-version linkage
* Authoritative-reference checks
* Evidence and provenance requirements
* Publication readiness

---

### `validation_references`

References to validation records or results where Chronicle preserves them separately.

**Status:** Conditional.

---

## Lifecycle and Publication Fields

### `correction_status`

Current Chronicle lifecycle state of the Correction Record.

**Status:** Required.

The final controlled values remain to be defined.

Legacy values such as:

```text
draft
active
superseded
archived
```

should not be treated as canonical.

---

### `publication_state`

Current publication state of the Correction Record.

**Status:** Required for production use.

Lifecycle state and publication state should remain distinct where they represent different concepts.

---

## Deprecated Legacy Fields

The following concepts from the original draft should not be carried forward unchanged:

### `affected_record`

Deprecated in favor of:

```text
affected_record_reference
```

to make the reference nature explicit.

### `previous_value`

Deprecated as the only prior-state model.

Use:

```text
previous_state
```

or a durable prior-version reference where appropriate.

### `corrected_value`

Deprecated as the only corrected-state model.

Use:

```text
corrected_state
```

or a durable resulting-version reference where appropriate.

### `requested_by`

Deprecated as ambiguous.

Use:

```text
initiated_by
```

and distinguish review/approval roles separately.

### `author`

Deprecated as a universal actor field.

Use explicit actor-role fields where necessary.

### Generic `version`

Deprecated as ambiguous.

Use:

* `schema_version`
* prior-version references
* resulting-version references
* correction-record versioning if later required

---

# Working Example

The following is conceptual only and does not establish final identifiers, controlled values, or production field names.

```yaml
correction_id: <CORRECTION-IDENTIFIER>
schema_version: 1.0.0

title: Correction to Chronicle Event Date

correction_type: factual
correction_scope: substantive

affected_record_reference: <CHRONICLE-ENTRY-ID>
affected_record_type: chronicle_entry

affected_fields:
  - event_date

issue_summary: >
  The published Chronicle Entry used an event date that did not
  match the authoritative source record.

reason: >
  The authoritative publication record establishes the correct
  occurrence date as 2026-09-01.

previous_state:
  event_date: 2026-09-02

corrected_state:
  event_date: 2026-09-01

change_summary: >
  Event date corrected to match the authoritative publication record.

prior_version_reference: <PRIOR-ENTRY-VERSION>
resulting_version_reference: <CORRECTED-ENTRY-VERSION>

authoritative_record_references:
  - <AUTHORITATIVE-SOURCE-ID>

source_references: []
evidence_references: []

verification_state: <CONTROLLED-VALUE>
validation_state: <CONTROLLED-VALUE>

correction_status: <CONTROLLED-VALUE>
publication_state: <CONTROLLED-VALUE>

correction_created_at: <TIMESTAMP>
published_at: <TIMESTAMP>
```

This example intentionally avoids inventing final values that have not yet been architecturally approved.

---

## Correction Lifecycle

A substantive Chronicle correction should follow a documented and repeatable workflow.

Working lifecycle:

1. Issue identified
2. Scope and authority reviewed
3. Affected Chronicle record identified
4. Sources and evidence reviewed
5. Correction decision documented
6. Prior state linked or preserved
7. Corrected state prepared
8. Verification performed where applicable
9. Validation performed
10. Resulting version established
11. Correction published
12. Prior and corrected states preserved
13. Historical linkage maintained

Not every administrative correction will require every step.

The final workflow will be governed by Chronicle Corrections, Versioning, Validation, and Publication procedures.

---

## Authority Boundary

Chronicle Correction Records apply only to Chronicle-owned records.

Chronicle may correct:

* Chronicle Entry fields
* Chronicle metadata
* Chronicle references
* Chronicle provenance
* Chronicle relationships
* Chronicle verification state
* Chronicle publication metadata
* Chronicle supporting records

Chronicle does **not** correct:

* Certification Packages
* SREG Registry Entries
* Integrity References
* Discovery Signals
* Trust Statements
* Workflow Definitions
* Atlas records
* Other externally authoritative Suite objects

If one of those systems changes its own authoritative object, Chronicle may preserve the later occurrence and update its own references.

---

## Preservation Principles

Chronicle corrections should supplement and version the historical record rather than erase it.

Whenever practical:

* Prior substantive states remain preserved
* Corrected states remain traceable
* Correction rationale remains visible
* Evidence and authoritative references remain reviewable
* Version lineage remains intact
* Publication history remains reconstructable
* Historical relationships remain auditable

The objective is not to hide mistakes.

The objective is to preserve how Chronicle's own record changed.

---

## Design Goals

The Chronicle Correction Record Schema should:

* Preserve transparency
* Improve Chronicle accuracy
* Maintain authority boundaries
* Preserve prior states
* Support version lineage
* Maintain provenance
* Support evidence-aware review
* Support verification
* Support validation
* Maintain traceability
* Preserve historical continuity
* Avoid silent rewriting
* Remain machine-readable and durable

---

## Future Development

Future Chronicle Correction Schema work may include:

* Final Correction Record identifier architecture
* Controlled correction types
* Controlled correction scope values
* Structured field-level change operations
* Formal version-lineage schema
* Provenance requirements
* Correction validation rules
* Automated diff generation
* Digital signatures
* Integrity anchoring
* Multi-party review where institutionally justified
* Public correction discovery

---

## Status

**Architectural draft — not yet a frozen production schema.**

This document has been reconciled with the current Chronicle Corrections page, Chronicle Records architecture, Chronicle Base Schema direction, and Satoshium Suite Standards, Methodology, Schemas Standard, Evidence Standard, and Interoperability principles.

The final identifier format, controlled values, required/conditional/optional designations, versioning conventions, actor roles, validation rules, and publication requirements must be settled through the remaining Chronicle operational-development steps before this schema becomes production authoritative.
