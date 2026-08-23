# Chronicle Correction Record Schema

## Purpose

The Chronicle Correction Record Schema defines the Chronicle-owned supporting structure used to document Corrections to Chronicle-owned records.

A Correction Record explains:

> Why did Chronicle change its own record?

A Correction Record must preserve enough information for future reviewers to reconstruct:

* what Chronicle originally recorded
* what Chronicle corrected
* why the Correction was necessary
* when the Correction occurred
* which fields were affected
* which Version resulted

Chronicle Corrections improve accuracy without erasing institutional history.

The governing principle is:

> Correct visibly. Version materially. Preserve every substantive state.

---

# Canonical Role

A Chronicle Correction Record is a **supporting Chronicle-owned record**.

It is not the canonical historical-preservation object.

The canonical Chronicle object remains:

```text
Chronicle Entry
```

A Correction Record may affect:

* Chronicle Entry
* Source Record
* Evidence Record
* another Chronicle-owned supporting record

It does not correct authoritative external Suite objects.

Conceptually:

```text
Chronicle-Owned Record
        ↓
Issue Identified
        ↓
Correction Record
        ↓
Corrected State
        ↓
New Version when Material
        ↓
Reverification / Revalidation where Required
```

---

# Correction and Versioning

Correction and Versioning are related but distinct.

## Correction

Answers:

> Why did Chronicle change the record?

## Version

Answers:

> What is the resulting preserved state?

Conceptually:

```text
Correction
    ↓
Explains change
    ↓
New Version where material
    ↓
Preserves resulting state
```

A Formal Correction and a new Version often occur together.

They are not the same concept.

---

# No Silent Historical Rewriting

Chronicle must not silently rewrite substantive historical content.

Material changes involving:

* Event Date
* Event Type
* Historical Context
* Source identity
* Evidence
* Provenance
* Relationships
* authoritative references
* Verification limitations
* publication-significant meaning

must leave explicit Correction and/or Version lineage.

The rule is:

> A changed record must leave evidence that it changed.

---

# Supporting Schema Status

This specification defines Chronicle's human-readable supporting architecture for a
formal Correction Record when Chronicle materially corrects one of its own records.

The canonical human-readable file is:

```text
correction-record-schema.md
```

`CHR-2026-0001 Entry Version 1` established Chronicle's first production Correction
baseline with no formal Correction lineage. `CHR-VAL-010 — Correction and Version
Consistency` was therefore Not Applicable for that initial Entry Version.

A machine-readable implementation:

```text
correction-record-schema.json
```

should remain deferred until Chronicle performs and preserves its first real production
Correction Record.

---

# Universal Required Fields

Every formal Chronicle Correction Record should contain:

```text
correction_id
schema_id
schema_version
correction_record_version

title
correction_type

affected_record_reference
affected_fields

original_information
corrected_information

correction_date
reason

resulting_version_reference

created_at
```

These are the minimum requirements for a formal Correction Record.

---

# Identity Fields

## `correction_id`

Stable unique identifier assigned to the Correction Record.

**Requirement:** Required.

The final Correction Record identifier namespace remains to be formally established.

Until approved, implementation should not invent a permanent namespace casually.

The identifier should remain:

* unique
* stable
* non-reusable
* independent of Correction Type
* independent of publication state
* independent of Verification State
* independent of Version

---

## `schema_id`

Stable identifier for the Correction Record Schema.

**Requirement:** Required.

Initial value:

```text
chronicle-correction-record
```

---

## `schema_version`

Version of the Correction Record Schema governing the record.

**Requirement:** Required.

Initial production convention:

```text
1.0.0
```

---

## `correction_record_version`

Sequential preserved Version of the Correction Record itself.

**Requirement:** Required.

Initial value:

```text
1
```

A Correction Record may itself require later Correction or Versioning if Chronicle discovers that the Correction Record contains a material defect.

---

# Human-Readable Identity

## `title`

Concise human-readable title describing the Correction.

**Requirement:** Required.

Example:

```text
Correction to Chronicle Event Date
```

---

# Correction Type

## `correction_type`

Controlled classification identifying the nature of the Correction.

**Requirement:** Required.

Approved Chronicle Correction Type values are:

```text
typographical
metadata
contextual
relationship
provenance
evidence
classification
substantive
```

Human-readable labels:

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

Rules:

* Correction Type describes what kind of Correction occurred.
* Correction Type does not by itself determine whether a new Version is required.
* Materiality determines Versioning behavior.
* `substantive` should be used when the Correction changes material historical meaning.

---

# Affected Record

## `affected_record_reference`

Stable reference to the Chronicle-owned record being corrected.

**Requirement:** Required.

Examples:

```text
CHR-2026-0001
<SOURCE-RECORD-ID>
<EVIDENCE-RECORD-ID>
```

This field must not imply Chronicle ownership of an external authoritative object.

---

## `affected_record_type`

Classification of the affected Chronicle-owned record.

**Requirement:** Conditional.

Recommended values may include:

```text
chronicle_entry
source_record
evidence_record
correction_record
other_chronicle_record
```

These values should be treated as schema-level structural labels unless later formalized through Controlled Values.

---

## `affected_fields`

Structured list of fields, Relationships, or record components changed by the Correction.

**Requirement:** Required.

Example:

```yaml
affected_fields:
  - event_date
  - historical_context
```

A Formal Correction should not be considered complete if reviewers cannot determine what part of the record changed.

---

# Original Information

## `original_information`

Structured representation or durable reference to the original information being corrected.

**Requirement:** Required.

This may contain:

* prior field value
* prior statement
* prior Relationship
* prior classification
* prior Source reference
* prior Provenance statement

Where practical, Chronicle should preserve a durable reference to the prior Version instead of duplicating an entire prior record inside the Correction Record.

---

# Corrected Information

## `corrected_information`

Structured representation or durable reference to the corrected information.

**Requirement:** Required.

This should identify the new value, statement, Relationship, classification, reference, or state resulting from the Correction.

---

# Correction Date

## `correction_date`

Date or timestamp when Chronicle formally applied or approved the Correction.

**Requirement:** Required.

Correction Date must remain distinct from:

* Event Date
* Entry Creation Date
* Source Publication Date
* Source Retrieval Date
* Version Effective Date
* Publication Date

---

# Reason

## `reason`

Explanation of why the Correction was necessary.

**Requirement:** Required.

The reason should describe:

* the issue identified
* why the prior representation was incorrect, incomplete, or misleading
* the basis for the corrected representation

Material Corrections should not use vague reasons where a specific rationale can be preserved.

---

# Resulting Version

## `resulting_version_reference`

Reference to the corrected or newly Versioned Chronicle-owned record state.

**Requirement:** Required for formal Corrections.

For a material Entry Correction, this should identify the resulting Entry Version.

Example:

```text
CHR-2026-0001 / Version 2
```

For a minor Correction that does not create a new Version, the field may reference the current record state while `version_effect` indicates no new Version.

---

# Prior Version

## `prior_version_reference`

Reference to the prior preserved state affected by the Correction.

**Requirement:** Conditional.

Required whenever the affected record has explicit Version lineage.

For substantive Chronicle Entry Corrections, this should ordinarily be present.

---

# Version Effect

## `version_effect`

Describes the Correction's effect on Version lineage.

**Requirement:** Conditional.

Candidate values:

```text
no_new_version
new_version
```

A separate `superseding_state` value is not recommended here.

Supersession between distinct Entries belongs in the Relationship Model and Lifecycle architecture.

These values may remain schema-local until production use demonstrates a need for formal Controlled Values.

---

# Materiality

## `materiality`

Indicates whether the Correction changes institutional or historical meaning.

**Requirement:** Conditional.

Recommended structural values:

```text
non_substantive
substantive
```

This distinction supports the Versioning Policy.

However, materiality should not become a substitute for Correction Type.

Example:

```text
correction_type: metadata
materiality: substantive
```

is possible if a metadata change alters historical meaning.

---

# Issue Summary

## `issue_summary`

Brief factual description of the problem Chronicle identified.

**Requirement:** Conditional.

Recommended for any Correction where the `reason` is lengthy or where a concise review label improves usability.

---

# Change Summary

## `change_summary`

Human-readable explanation of what changed.

**Requirement:** Conditional.

Recommended for substantive Corrections and public Correction presentation.

---

# Impact

## `impact`

Description of the Correction's effect on Chronicle's representation.

**Requirement:** Conditional.

May describe whether the Correction affects:

* historical meaning
* temporal ordering
* classification
* authoritative references
* Provenance
* Relationships
* Evidence
* Verification
* publication

---

# Source References

## `source_references`

References to Sources relevant to the Correction.

**Requirement:** Conditional.

Required when Source material is part of the basis for the Correction.

---

# Evidence References

## `evidence_references`

References to Evidence relevant to the Correction.

**Requirement:** Conditional.

Required when Evidence supports, challenges, clarifies, or otherwise bears on the Correction.

Evidence Type and Evidence Relationship remain governed by Chronicle Evidence architecture.

---

# Authoritative Record References

## `authoritative_record_references`

References to authoritative Suite or institutional objects relevant to the Correction.

**Requirement:** Conditional.

Required when the Correction depends materially on an authoritative external record.

Examples:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Trust Statement
* Workflow Definition
* Atlas record

Chronicle references these objects.

Chronicle does not correct them.

---

# Provenance

## `provenance`

Structured information explaining how the issue, supporting Sources, Evidence, and authoritative references entered Chronicle.

**Requirement:** Conditional.

Required for substantive Corrections where Provenance materially affects reviewability.

Minimum applicable Provenance should align with the Chronicle Provenance Model.

---

# Relationship Updates

## `relationship_updates`

Structured description of Relationships added, removed, or corrected.

**Requirement:** Conditional.

Required when the Correction changes Relationship semantics.

Relevant Controlled Relationship Types include:

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

---

# Related Entries

## `related_entry_references`

References to Chronicle Entries materially related to the Correction.

**Requirement:** Conditional.

---

# Related Corrections

## `related_correction_references`

References to other Correction Records associated with the same issue, lineage, or later correction.

**Requirement:** Conditional.

---

# Verification Impact

## `verification_state`

Chronicle Verification State associated with the corrected record where applicable.

**Requirement:** Conditional.

Approved values:

```text
not_reviewed
in_review
verified
verified_with_limitations
unresolved
```

A material Correction should ordinarily trigger Reverification.

Example:

```text
Version 1
verification_state: verified

Correction
    ↓

Version 2
verification_state: in_review
```

---

## `verification_references`

References to Verification activity or records associated with the Correction.

**Requirement:** Conditional.

---

# Validation

The Correction Record Schema is designed for Validation.

It does not presently require a universal embedded:

```text
validation_state
```

Chronicle's production Validation architecture establishes Version-specific Validation
for Chronicle Entries. Validation-result storage for an independently governed
Correction Record remains undefined until a production Correction Record exists.

Validation may test:

* Correction Record identifier integrity
* schema conformance
* Correction Type
* affected record reference
* affected fields
* original information
* corrected information
* Correction Date
* reason
* Version linkage
* Source / Evidence references
* Provenance
* publication prerequisites

Conceptually:

```text
Schema ≠ Verification ≠ Validation
```

---

# Publication

## `publication_state`

Publication State of the Correction Record when Chronicle independently publishes Correction Records.

**Requirement:** Conditional.

Approved values:

```text
not_published
pending_publication
published
withdrawn_from_publication
```

Not every Correction Record must necessarily be exposed independently if the Correction is represented through Entry Version history.

---

## `published_record_at`

Date and time Chronicle published the Correction Record.

**Requirement:** Conditional.

Required when:

```text
publication_state: published
```

---

# Correction Record Lifecycle

A separate `correction_status` field is not presently required.

The Lifecycle State vocabulary established for Chronicle Entries should not automatically be applied to Correction Records.

A Correction Record may conceptually move through:

```text
identified
documented
reviewed
validated
applied
published where applicable
preserved
```

These are process stages, not approved Correction Record Controlled Values.

---

# Actor Fields

## `initiated_by`

Entity, role, process, or system that initiated the Correction.

**Requirement:** Conditional.

---

## `reviewed_by`

Entity, role, process, or system responsible for Correction review.

**Requirement:** Conditional.

---

## `approved_by`

Entity, role, process, or system responsible for formal approval where procedure requires it.

**Requirement:** Conditional.

Actor roles should not be frozen into Controlled Values until operational procedure establishes stable role semantics.

---

# Additional Temporal Fields

## `identified_at`

Date and time the issue was identified.

**Requirement:** Conditional.

---

## `reviewed_at`

Date and time Correction review was completed.

**Requirement:** Conditional.

---

## `created_at`

Date and time Chronicle created the Correction Record.

**Requirement:** Required.

---

# Correction Record Versioning

## `correction_record_version`

Sequential Version of the Correction Record.

**Requirement:** Required.

If Chronicle later discovers that a Correction Record itself contains a material defect, that Correction Record should be corrected and Versioned rather than silently overwritten.

---

## `prior_correction_version_reference`

Reference to the immediately prior Correction Record Version.

**Requirement:** Conditional.

Required for Correction Record Version 2 and later where prior-Version linkage is represented directly.

---

# Required Correction Minimum

Every formal Correction must preserve:

```text
Original information
Corrected information
Correction date
Reason
Affected fields
Resulting Version
```

This is the institutional minimum.

A Correction Record missing these elements should not be treated as a complete formal Correction.

---

# Editorial Update vs. Formal Correction

Not every editorial change requires a Formal Correction Record.

Potential Editorial Updates may include:

* spelling
* punctuation
* formatting
* accessibility text
* technical markup repair
* broken-link repair where Source identity does not change

The governing test is:

> Does the change alter historical or institutional meaning?

If no:

```text
Editorial Update may be sufficient.
```

If yes:

```text
Formal Correction
+ New Version if material
```

---

# Substantive Correction Requirements

A substantive Correction should ordinarily require:

```text
Original state preserved
        ↓
Correction documented
        ↓
Sources / Evidence reviewed
        ↓
Corrected state prepared
        ↓
New Version created
        ↓
Reverification
        ↓
Revalidation where required
        ↓
Publication lineage updated
```

---

# External Authoritative Changes

If another Suite institution changes its own authoritative object, Chronicle must first ask:

> Is Chronicle's existing record wrong, or did something new happen?

If Chronicle's existing representation is wrong:

```text
Correction
```

If a distinct later Occurrence occurred:

```text
New Occurrence
→ Preservation Eligibility
→ New Chronicle Entry
```

Chronicle should not rewrite an earlier Entry merely because a later institutional event occurred.

---

# Superseding Entry vs. Correction

A Correction changes Chronicle's own representation of the same canonical record.

A superseding Entry is a separate canonical Entry.

Conceptually:

```text
Same Entry identity + material change
→ New Version

Distinct qualifying Occurrence
→ New Chronicle Entry

Formal institutional replacement between Entries
→ Supersedes / Superseded By
```

Supersession should not be modeled as a Correction Type.

---

# Deprecated Legacy Correction Types

The following older draft taxonomy should not govern production Correction Records:

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

Use the approved Controlled Values instead:

```text
typographical
metadata
contextual
relationship
provenance
evidence
classification
substantive
```

---

# Deprecated Legacy Fields

## `previous_state`

Deprecated as the canonical field name.

Use:

```text
original_information
```

or a durable prior-Version reference.

---

## `corrected_state`

Deprecated as the canonical field name.

Use:

```text
corrected_information
```

or a durable resulting-Version reference.

---

## `affected_record`

Deprecated.

Use:

```text
affected_record_reference
```

---

## `requested_by`

Deprecated as ambiguous.

Use:

```text
initiated_by
```

---

## Universal `author`

Deprecated.

Use explicit actor-role fields only where needed.

---

## Generic `version`

Deprecated.

Use:

```text
schema_version
correction_record_version
prior_version_reference
resulting_version_reference
```

according to meaning.

---

# Illustrative Supporting-Record Example

The following demonstrates the current human-readable Correction Record architecture.

It is **not** a Correction that occurred to `CHR-2026-0001`, and the dates and values
below remain illustrative. The example does not establish a permanent Correction Record
identifier namespace.

```yaml
correction_id: <CORRECTION-IDENTIFIER>
schema_id: chronicle-correction-record
schema_version: 1.0.0
correction_record_version: 1

title: Correction to Chronicle Event Date

correction_type: metadata
materiality: substantive

affected_record_reference: CHR-2026-0001
affected_record_type: chronicle_entry

affected_fields:
  - event_date

original_information:
  event_date: 2026-09-02

corrected_information:
  event_date: 2026-09-01

correction_date: 2026-09-10

reason: >
  The authoritative publication record establishes the correct
  Occurrence date as 2026-09-01.

prior_version_reference:
  entry_id: CHR-2026-0001
  entry_version: 1

resulting_version_reference:
  entry_id: CHR-2026-0001
  entry_version: 2

version_effect: new_version

authoritative_record_references:
  - <AUTHORITATIVE-RECORD-ID>

verification_state: in_review

created_at: 2026-09-10T16:00:00Z
```

This example does not establish a permanent Correction Record identifier format.

---

# First Production Baseline

`CHR-2026-0001 Entry Version 1` entered production with:

```text
Formal Correction: None
Prior Entry Version: None
CHR-VAL-010 — Correction and Version Consistency: N/A
```

That is a production baseline, not evidence that the Correction architecture is
unnecessary. When Chronicle later materially changes its own representation of the
same canonical Entry, the governing rule remains:

```text
Correction explains why.
Version preserves the resulting state.
```

A distinct later authoritative action is ordinarily assessed as a new Occurrence and
new Chronicle Entry rather than rewritten into the original Entry as a Correction.

---

# Correction Record Creation Test

A formal Correction Record should ordinarily be created when:

* Chronicle corrects a material historical field
* Chronicle changes Event Type
* Chronicle changes Event Date
* Chronicle changes a material Source reference
* Chronicle changes Evidence linkage
* Chronicle changes Provenance
* Chronicle changes a material Relationship
* Chronicle changes material Historical Context
* Chronicle needs to preserve Correction rationale
* Versioning requires traceable lineage

A simple Editorial Update may not require a separate Correction Record if historical meaning remains unchanged.

---

# Authority Boundary

Chronicle Correction Records may correct:

* Chronicle Entries
* Chronicle Source Records
* Chronicle Evidence Records
* Chronicle Correction Records
* other Chronicle-owned supporting records

They do **not** correct:

* Certification Packages
* SREG Registry Entries
* Integrity References
* Discovery Signals
* Trust Statements
* Workflow Definitions
* Atlas records
* other externally authoritative objects

Authority remains with the originating institution.

---

# Validation Expectations

When Chronicle creates a production Correction Record, it should be validated against:

* Correction Record Schema
* Correction Record identifier rules
* Correction Type Controlled Values
* affected-record integrity
* affected-field presence
* original-information presence
* corrected-information presence
* Correction Date
* reason
* prior-Version linkage where applicable
* resulting-Version linkage
* Source / Evidence reference integrity
* Provenance requirements
* publication prerequisites

---

# Schema Versioning and Compatibility

Every production Correction Record should remain associated with the Correction Record Schema Version that governed it.

Schema evolution should preserve:

* Schema identity
* Schema Version
* compatibility classification
* deprecation history
* migration guidance
* Validation behavior
* historical interpretability

Older Correction Records should remain understandable under the Schema Version that originally governed them.

---

# Design Principles

## Correct Chronicle-Owned Records Only

Authority boundaries remain explicit.

## Preserve Before and After

Original and corrected information both remain traceable.

## Correction ≠ Version

Correction explains the change; Version preserves the resulting state.

## Material Changes Need Lineage

No silent substantive rewrite.

## Controlled Correction Types

Production Correction Type values come from the Controlled Values Registry.

## Reverification Follows Material Change

Material Corrections ordinarily trigger Reverification.

## Preserve Prior States

Historical institutional states remain reviewable.

---

# Guiding Principle

> Preserve what Chronicle said. Preserve why Chronicle changed it.

And operationally:

> Correct visibly. Version materially. Preserve every substantive state.

---

## Status

**Chronicle supporting Correction Record Schema specification.**

The Correction Record Schema is now aligned with:

* Chronicle Base Schema
* Corrections architecture
* Controlled Values Registry
* Versioning Policy
* Lifecycle Model
* Relationship Model
* Provenance Model
* Source architecture
* Evidence architecture
* Verification Procedure
* authority boundaries

The approved Correction Type vocabulary and mandatory Correction minimum are incorporated.

Correction Record identifier namespace, actor-role vocabularies, supporting-record
Validation-result storage, and independent Correction Record publication requirements
remain intentionally unresolved pending a real production Correction.

No machine-readable `correction-record-schema.json` should be created merely for
symmetry. It should be introduced only after the first production Correction Record
demonstrates that the machine-readable contract is operationally necessary.
