# Chronicle Versioning Policy

## Purpose

The Chronicle Versioning Policy defines how a canonical Chronicle Entry changes over time while preserving historical identity and prior record states.

The policy distinguishes:

* Editorial updates
* New Entry Versions
* Formal Corrections
* Superseding Entries
* Schema Version changes
* Historical immutability

Versioning exists so Chronicle can improve its historical record without erasing the record's own history.

The governing principle is:

> Correct forward. Preserve backward.

---

# Core Versioning Rule

A Chronicle Entry has one stable canonical identifier.

Material changes produce new Entry Versions beneath that identifier.

Conceptually:

```text
CHR-2026-0001
    Version 1
        ↓
    Version 2
        ↓
    Version 3
```

The identifier remains:

```text
CHR-2026-0001
```

unless a genuinely distinct qualifying Occurrence requires a separate Chronicle Entry.

---

# Versioning and Identity

The Identifier Specification establishes that Chronicle Entry identity is permanent.

Versioning must therefore preserve:

* Entry identifier
* Identity continuity
* Version lineage
* Prior substantive states
* Correction lineage
* Publication history

Versioning must not create a new Chronicle identifier merely because the same Entry changed.

---

# Entry Version vs. Schema Version

Entry Version and Schema Version are separate.

## Entry Version

Describes the state of a specific Chronicle Entry.

Example:

```text
Entry:
CHR-2026-0001

Entry Version:
2
```

## Schema Version

Describes the version of the schema used to structure the record.

Example:

```text
Schema:
Chronicle Base Schema

Schema Version:
1.1
```

A new Schema Version does not automatically require a new Entry identifier.

It may require migration or a new Entry Version depending on whether the record representation materially changes.

---

# Four Change Paths

Chronicle recognizes four principal change paths:

```text
Editorial Update
New Entry Version
Formal Correction
Superseding Entry
```

These paths solve different problems.

---

# 1. Editorial Update

An Editorial Update changes presentation without changing historical meaning.

Potential examples:

* Spelling
* Punctuation
* Formatting
* Accessibility text
* Broken hyperlink repair
* Minor display cleanup
* Non-substantive wording clarification
* Technical markup correction

An Editorial Update should not change:

* Event Date
* Event Type
* Historical meaning
* Authoritative reference
* Evidence relationship
* Provenance
* Relationship semantics
* Verification basis
* Material limitation
* Institutional interpretation

The rule is:

> If meaning changes, the update is not merely editorial.

---

# Editorial Update Traceability

Chronicle may choose to preserve a lightweight editorial-change log.

Not every typographical correction requires a new Entry Version.

However, once a change becomes material to institutional meaning, it moves out of the Editorial Update category.

The final Correction Procedure should define whether specific editorial changes require a Correction Record.

---

# 2. New Entry Version

A new Entry Version is required when a material change alters the same canonical Chronicle Entry.

Potential triggers include:

* Event Representation change
* Event Date change
* Event Type change
* Historical Context change
* Source reference change
* Evidence change
* Provenance change
* Relationship change
* Verification basis change
* Material limitation change
* Publication-relevant substantive change

A new Version preserves the old state.

---

# Materiality Test

The practical question is:

> Would a future reviewer reasonably need to know that the prior record said something materially different?

If yes, Chronicle should create a new Version.

---

# Version Example

```text
CHR-2026-0001
Version 1

Event Date:
2026-07-05
```

Later Chronicle determines the Event Date should be:

```text
2026-07-06
```

The change is historically material.

The appropriate response is:

```text
Correction:
Metadata or Substantive, depending on context

CHR-2026-0001
Version 2

Event Date:
2026-07-06
```

Version 1 remains preserved.

---

# 3. Formal Correction

A Formal Correction records why Chronicle changed its own record.

A Correction may address:

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

These Correction Types are governed through the Controlled Values Registry.

---

# Correction vs. Version

Correction and Version are related but distinct.

### Correction

Answers:

> Why did Chronicle change the record?

### Version

Answers:

> What is the new preserved state of the record?

Conceptually:

```text
Correction
    ↓
Explains change
    ↓
New Entry Version
    ↓
Preserves resulting state
```

---

# Minor Correction

A minor Correction may not require a new Entry Version when it does not materially change institutional meaning.

Examples may include:

* Typographical correction
* Punctuation correction
* Broken link update
* Non-substantive metadata formatting

The boundary should be explicitly defined in the Correction Procedure.

---

# Substantive Correction

A substantive Correction should ordinarily require:

1. Prior state preserved
2. Correction reason documented
3. Supporting Evidence or Source where applicable
4. New Entry Version
5. Reverification
6. Revalidation where required
7. Publication lineage updated

Chronicle must not silently rewrite the prior state.

---

# 4. Superseding Entry

A Superseding Entry is not the same as a new Version.

A Superseding Entry has its own Chronicle identifier.

Example:

```text
CHR-2026-0001
    ↓ Superseded By
CHR-2027-0042
```

This should occur only when there is a genuinely separate canonical Entry.

---

# When a Superseding Entry May Be Appropriate

A superseding Entry may be appropriate where:

* A distinct later Occurrence formally replaces an earlier institutional state
* A later canonical historical record is intentionally designated to replace another Entry for a defined purpose
* Duplicate-entry resolution requires one Entry to remain canonical while another is retained as superseded
* A legacy record cannot appropriately be represented as a Version of the same canonical Entry

Supersession should be rare.

---

# When Supersession Is Not Appropriate

A new Entry should not supersede an earlier Entry merely because:

* It is newer
* It contains more Sources
* It contains better Evidence
* It is better written
* Its schema is newer
* A Correction occurred
* Chronicle learned more about the same Occurrence

Those are usually Versioning situations.

---

# Distinct Occurrence Rule

The primary distinction is:

```text
Same canonical Occurrence / same Entry identity
→ New Version

Distinct qualifying Occurrence
→ New Chronicle Entry
```

Example:

```text
Certification Created
→ CHR-2026-0001

Certification Revoked
→ CHR-2026-0002
```

The revocation is not Version 2 of the creation Entry.

It is a separate Occurrence.

---

# Historical Immutability

Substantive historical Versions should be treated as immutable record states once published or otherwise institutionally established.

Immutability means:

* Prior substantive content is not overwritten
* Prior Version remains identifiable
* Prior Version remains traceable
* Correction lineage remains visible
* Publication history remains visible

It does not mean Chronicle can never improve the record.

Improvement happens through later Versions.

---

# Immutability Principle

> Preserve prior meaning. Add later meaning through lineage.

---

# No Silent Substantive Rewrite

Chronicle must not silently rewrite:

* Event Date
* Event Type
* Event Representation
* Historical Context
* Source identity
* Evidence basis
* Provenance
* Relationships
* Verification limitations
* Publication-significant representation

Material changes require traceability.

---

# Prior-State Preservation

Each substantive Entry Version should remain preserved in enough form that future reviewers can reconstruct:

* What the Entry said
* When that Version became effective
* What changed later
* Why it changed
* Which Correction applied
* What Verification State applied
* Which Schema Version governed it
* Whether it was published

---

# Version Numbering

The initial Chronicle approach should use simple sequential Version numbers:

```text
Version 1
Version 2
Version 3
```

Potential machine representation:

```text
1
2
3
```

Chronicle should not adopt semantic versioning for Entry content unless production use proves it necessary.

---

# Version Number Does Not Belong in Identifier

Avoid:

```text
CHR-2026-0001-V2
```

as the canonical identifier.

Instead:

```text
identifier:
CHR-2026-0001

entry_version:
2
```

Identity and Version remain separate.

---

# Version Lineage Requirements

A substantive Version should preserve at minimum:

```text
Entry Identifier
Entry Version
Prior Version
Version Effective Date
Change Summary
Reason for Change
Correction Reference when applicable
Verification State
Schema Version
Publication State
```

Additional fields may include:

* Reviewer
* Validation result
* Evidence added
* Sources added
* Provenance change
* Relationships changed

These should be added only where operational need requires them.

---

# Editorial Change Examples

## Spelling

Before:

```text
Certifcation
```

After:

```text
Certification
```

Likely Editorial Update.

---

## Formatting

Changing heading structure or HTML markup without changing meaning is likely Editorial.

---

## Link Repair

Replacing a dead URL with the correct archive URL may be Editorial if Source identity remains unchanged.

If the replacement changes Source identity or Provenance materially, it may require a new Version.

---

# Material Change Examples

## Event-Date Correction

Changing:

```text
2026-07-05
```

to:

```text
2026-07-06
```

is ordinarily material.

Likely response:

```text
Formal Correction
New Entry Version
Reverification
Revalidation where required
```

---

## Event-Type Correction

Changing:

```text
Certification Created
```

to:

```text
Certification Renewed
```

is material.

Likely response:

```text
Classification Correction
New Entry Version
Reverification
```

The Chronicle identifier remains unchanged.

---

## Relationship Change

Changing:

```text
Related To
```

to:

```text
Supersedes
```

is material because it changes institutional meaning.

Likely response:

```text
Relationship Correction
New Entry Version
Reverification
```

---

## Provenance Change

Adding a missing transformation step may be material if it affects trust or interpretation.

The impact should determine whether a Version is required.

---

## Evidence Change

Adding or removing material Evidence may require a new Version when it changes:

* Historical interpretation
* Verification basis
* Limitations
* Confidence in the representation

---

# Correction Types and Versioning

The current Controlled Values include:

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

These do not automatically determine Versioning behavior.

For example:

```text
Metadata Correction
```

could be minor or material.

Materiality remains the deciding factor.

---

# Versioning and Verification

Material Versions should trigger Reverification.

The Verification Procedure should review the new Version independently enough to determine whether the prior Verification result remains valid.

Example:

```text
Version 1
Verification State: Verified

Material Correction
    ↓

Version 2
Verification State: In Review
    ↓

Reverification
    ↓

Verification State: Verified with Limitations
```

Prior Verification history remains preserved.

---

# Versioning and Validation

A material Version may require Revalidation.

Revalidation is particularly appropriate when changes affect:

* Required fields
* Controlled Values
* Relationship structure
* Provenance
* Event-Type Profile conformance
* Schema conformance
* Publication prerequisites

Not every Editorial Update needs full Revalidation.

---

# Versioning and Publication

Publication should identify the current public Version.

Chronicle should preserve publication history such as:

```text
Version 1
Published 2026-09-03

Version 2
Published 2026-09-18
```

Publication of Version 2 must not erase the fact that Version 1 was previously public.

---

# Versioning and Publication State

Each Version may have relevant publication metadata.

However, Publication State belongs to the Entry's current record state, not the immutable identity itself.

The final schema should avoid creating confusing duplicate state models.

---

# Versioning and Lifecycle

Versioning occurs within the Entry Lifecycle.

Conceptually:

```text
Active Entry
    ↓
Material change identified
    ↓
Correction / Versioning
    ↓
Reverification
    ↓
Revalidation where required
    ↓
Maintained / Republished
```

A new Version does not ordinarily create a new lifecycle identity.

---

# Versioning and Supersession

Supersession may occur between:

* Distinct Chronicle Entries
* Legacy and canonical records
* Duplicate Entries where one must remain canonical

Supersession should preserve both identifiers.

The Relationship Model governs:

```text
Supersedes
Superseded By
```

---

# Duplicate Entry Resolution

If Chronicle discovers that two identifiers represent the same Occurrence:

```text
CHR-2026-0007
CHR-2026-0012
```

Chronicle must not:

* Delete one silently
* Reuse one identifier
* Collapse identity history without trace

A later procedure may designate one canonical Entry and mark the other as:

* Superseded
* Withdrawn
* Duplicate

depending on the final Status and Controlled Values architecture.

The Relationship or Correction history should preserve what happened.

---

# Versioning and Historical Preservation

Historical preservation requires more than keeping the current Version.

Chronicle should preserve:

* Prior substantive Versions
* Correction history
* Version dates
* Verification history
* Publication history
* Relationship changes
* Source changes
* Provenance changes
* Evidence changes
* Schema context

This allows future reviewers to reconstruct institutional evolution.

---

# Version Storage

The final implementation may preserve prior Versions through:

* Immutable files
* Version directories
* Repository history
* Structured JSON snapshots
* Archival storage
* Content-addressed objects
* Other durable methods

The policy defines the institutional requirement.

The storage implementation may evolve.

---

# Version Integrity

Where practical, Chronicle may preserve integrity information for Version states.

Potential methods include:

* Hashes
* Repository commits
* Anchor Integrity References
* Timestamps
* Immutable archive snapshots

These are supporting mechanisms.

They do not replace Version lineage metadata.

---

# Schema Migration

A Schema migration may change how an Entry is represented without changing its historical meaning.

If migration is purely structural, Chronicle may not need a substantive Entry Version.

However, the migration should remain traceable.

If the migration changes meaning or interpretation, a new Entry Version is required.

---

# Controlled Values Changes

A Controlled Value may later be deprecated or replaced.

Historical Entry Versions should remain interpretable under the vocabulary that governed them.

Chronicle should not silently rewrite old Versions merely to make them appear current.

Migration should preserve semantic history.

---

# Retrospective Corrections

Chronicle may discover an error years after publication.

Time elapsed does not eliminate the need for traceability.

A retrospective Correction should preserve:

* Original Version
* Correction date
* Reason
* Supporting material
* New Version
* Reverification

---

# Versioning Decision Test

Before changing a Chronicle Entry, ask:

### Question 1

Does the change alter historical or institutional meaning?

If no:

```text
Editorial Update may be sufficient.
```

If yes, continue.

### Question 2

Is Chronicle correcting an error in its own record?

If yes:

```text
Formal Correction
+ New Version if material
```

### Question 3

Is this still the same canonical Chronicle Entry?

If yes:

```text
New Entry Version
```

If no:

### Question 4

Is this a distinct qualifying Occurrence?

If yes:

```text
New Chronicle Entry
```

Then determine whether a Relationship such as:

```text
Precedes
Follows
Supersedes
Superseded By
Related To
```

is appropriate.

---

# Decision Summary

```text
Presentation-only change
→ Editorial Update

Material change to same Entry
→ New Entry Version

Error in Chronicle-owned record
→ Formal Correction
→ New Version if material

Distinct qualifying Occurrence
→ New Chronicle Entry

Formal institutional replacement between Entries
→ Supersedes / Superseded By
```

---

# Versioning Validation Expectations

Future Validation should confirm, where applicable:

1. Entry Version is present and valid.
2. Version sequence is valid.
3. Prior Version reference is valid.
4. Entry identifier remains unchanged.
5. Correction reference exists when required.
6. Material change summary is present.
7. Verification requirements are satisfied.
8. Schema Version is identified.
9. Publication lineage is consistent.
10. Supersession Relationships are valid.
11. Event-Type Profile requirements are satisfied.

---

# Versioning Policy Principle

Versioning should make Chronicle more trustworthy because it allows correction without historical amnesia.

A future reviewer should be able to answer:

* What did Chronicle originally say?
* What changed?
* Why did it change?
* Which Version is current?
* Which Verification applied?
* Was the prior Version public?
* Does another Entry supersede it?

---

# Guiding Principle

> A trustworthy historical record remembers its own revisions.

And operationally:

> Correct forward. Preserve backward.

---

## Relationship to Other Chronicle Documentation

The Chronicle Versioning Policy should remain aligned with:

* Entry Model
* Preservation Eligibility
* Chronicle Rules
* Identifier Specification
* Controlled Values Registry
* Relationship Model
* Provenance Model
* Sources
* Evidence
* Verification Procedure
* Lifecycle
* Corrections
* Status
* Schemas
* Validation
* Publication Procedure

Versioning is the mechanism that preserves continuity of the canonical Entry while allowing Chronicle's representation to evolve responsibly.

---

## Next Operational Dependencies

The Versioning Policy directly informs:

* Corrections Procedure
* Status reconciliation
* Lifecycle transition rules
* Chronicle Base Schema
* Certification Event-Type Profile
* Validation
* Production Procedure
* Publication history
* First production Chronicle Entry

The first production Entry should test the editorial/material boundary and the practical storage of prior Versions.

---

## Status

**Active pre-operational Chronicle Versioning Policy specification.**

The core distinctions are established:

```text
Editorial Update
New Entry Version
Formal Correction
Superseding Entry
```

The exact minor-correction threshold, public prior-Version presentation, Version storage implementation, schema-migration treatment, duplicate-entry resolution, and automated Version validation should be finalized through later Phase VI and production-development work.
