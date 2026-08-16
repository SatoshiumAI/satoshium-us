# Chronicle Corrections

## Purpose

Chronicle Corrections preserve the integrity, transparency, and historical lineage of Chronicle's own preservation records.

As new Evidence emerges, Sources become available, errors are identified, Relationships are corrected, Provenance improves, or Historical Context changes, Chronicle may need to correct its own representation of a preserved Occurrence.

Chronicle does not use Corrections to alter authoritative records owned by Certifier, Registry, Anchor, Beacon, Attestor, Navigator, Atlas, or another Suite system.

Rather than silently replacing prior Chronicle states, Chronicle uses transparent, traceable, Version-aware Correction.

The governing principle is:

> Correct forward. Preserve backward.

---

# Suite Alignment

Chronicle Corrections operate within the Satoshium Suite architecture.

Corrections should follow Suite-wide expectations for:

* Stable and durable objects
* Clear institutional authority boundaries
* Reference-based interoperability
* Evidence handling
* Provenance and traceability
* Structured records and schema discipline
* Controlled Values
* Version preservation
* Validation-ready workflows
* Documented and repeatable procedures
* Historical immutability of prior substantive states

Chronicle corrects its own preservation record.

It does not replace, supersede, or reinterpret the authority of another Suite system.

---

# Core Correction Rule

Chronicle must not silently rewrite substantive historical content.

A formal Correction should record:

```text
Original information
Corrected information
Correction date
Reason
Affected fields
Resulting Version
```

Where applicable, the Correction should also preserve:

* Correction Type
* Supporting Source
* Supporting Evidence
* Prior Version
* Verification impact
* Validation impact
* Publication impact
* Reviewer or review mechanism
* Relationship to the affected Entry or supporting record

---

# Why Corrections Exist

Corrections may be required when Chronicle discovers:

* Typographical defects
* Metadata errors
* Event-date errors
* Event-Type misclassification
* Incorrect Source references
* Incorrect authoritative identifiers
* Evidence errors
* Provenance defects
* Relationship errors
* Missing or inaccurate Historical Context
* Material omissions
* Substantive historical inaccuracies

A Correction applies to Chronicle's own representation.

---

# Required Correction Record

Every formal Chronicle Correction should preserve the following minimum information.

## Original Information

The prior value, statement, Relationship, classification, reference, or other state being corrected.

## Corrected Information

The replacement value or corrected representation.

## Correction Date

The date Chronicle formally applied or approved the Correction.

## Reason

Why the Correction was necessary.

## Affected Fields

The specific Chronicle fields or supporting-record fields changed.

## Resulting Version

The Entry Version or supporting-record Version produced by the Correction when Versioning is required.

---

# Preserve Historical Lineage

Prior substantive Chronicle states should remain preserved.

A future reviewer should be able to determine:

* What Chronicle originally recorded
* What was later found to be wrong or incomplete
* What changed
* Why it changed
* When it changed
* Which fields changed
* Which Version contains the corrected state
* Which prior Version was affected
* Which Verification result applied before and after the change

Chronicle should improve accuracy without creating an ahistorical appearance of perfection.

---

# Transparency

Corrections should remain visible, attributable, and understandable.

A Correction should not hide the fact that an earlier representation existed.

Conceptually:

```text
Prior State
    ↓
Correction
    ↓
Corrected State
    ↓
Resulting Version
```

---

# Authority Boundaries

A Chronicle Correction applies only to Chronicle-owned records.

Chronicle may correct:

* Chronicle Entry content
* Chronicle metadata
* Chronicle Source references
* Chronicle Evidence references
* Chronicle Provenance
* Chronicle Relationships
* Chronicle Historical Context
* Chronicle classifications
* Chronicle supporting records

Chronicle does not correct the authoritative external object itself.

---

# Corrections to Authoritative References

Chronicle may correct its own reference to an authoritative record when:

* Identifier was wrong
* Originating system was wrong
* Description was inaccurate
* Relationship Type was wrong
* Target object was wrong

Example:

```text
Incorrect Chronicle reference:
SC-CERT-2026-0002

Correct reference:
SC-CERT-2026-0001
```

Chronicle corrects the reference.

It does not alter the Certification Package.

---

# Correction Types

Correction Type should use the Chronicle Controlled Values Registry.

The canonical initial values are:

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

These replace older free-form correction taxonomies for Chronicle production use.

---

## Typographical

Corrects spelling, punctuation, or similar presentation defects without changing institutional meaning.

Examples:

* Misspelling
* Punctuation
* Minor grammar defect
* Typographic formatting

A new Entry Version is usually not required unless the change unexpectedly affects meaning.

---

## Metadata

Corrects structured metadata.

Examples:

* Identifier reference
* Date field
* Display metadata
* Source metadata
* Publication metadata

Materiality determines whether a new Version is required.

---

## Contextual

Corrects or improves Historical Context.

A Contextual Correction may be minor or material.

A new Entry Version is required when the change materially alters historical interpretation.

---

## Relationship

Corrects:

* Relationship Type
* Direction
* Target
* Source
* Relationship rationale
* Historical sequence

Material Relationship Corrections ordinarily require a new Version and Reverification.

---

## Provenance

Corrects:

* Origin
* Acquisition method
* Retrieval date
* Transfer history
* Transformation
* Archive path
* Provenance limitation

Material Provenance Corrections may require a new Version.

---

## Evidence

Corrects:

* Evidence identity
* Evidence Type
* Source reference
* Entry or claim linkage
* Evidence limitation
* Evidence availability
* Integrity information

Material Evidence Corrections may require a new Version and Reverification.

---

## Classification

Corrects Event Type or another controlled classification.

Example:

```text
Before:
Certification Created

After:
Certification Renewed
```

The Chronicle identifier remains unchanged.

A Classification Correction ordinarily requires a new Entry Version.

---

## Substantive

Corrects material historical meaning.

Substantive Corrections ordinarily require:

1. Prior state preserved
2. Correction reason documented
3. Supporting Source or Evidence reviewed
4. New Entry Version
5. Reverification
6. Revalidation where required
7. Publication lineage updated

---

# Correction vs. Version

Correction and Versioning are related but distinct.

## Correction

Answers:

> Why did Chronicle change its record?

## Version

Answers:

> What is the resulting preserved state of the record?

Conceptually:

```text
Correction
    ↓
Explains the change
    ↓
New Version
    ↓
Preserves the resulting state
```

A Formal Correction and new Version often occur together.

They are not the same object or concept.

---

# Editorial Update vs. Formal Correction

Some changes may be handled as Editorial Updates rather than Formal Corrections.

Potential Editorial Updates include:

* Spelling
* Punctuation
* Formatting
* Accessibility text
* Broken-link repair
* Technical markup repair

The key rule is:

> If institutional or historical meaning changes, the change is not merely editorial.

A material change must enter Correction and Version lineage.

---

# Materiality Rule

The principal Versioning question is:

> Would a future reviewer reasonably need to know that the prior Chronicle record said something materially different?

If yes:

```text
Preserve prior state
Create Formal Correction
Create new Version
```

where applicable.

---

# Minor Corrections

Minor Corrections may include:

* Typographical fixes
* Non-substantive formatting
* Broken-link repair
* Minor metadata cleanup
* Presentation clarification

A simplified Correction process may be used if historical meaning does not change.

The final Production Procedure should define the exact threshold.

---

# Substantive Corrections

Substantive Corrections affect historical or institutional meaning.

Potential examples:

* Event Date changes
* Event Type changes
* Authoritative reference changes
* Material Source changes
* Evidence changes
* Provenance changes
* Relationship changes
* Historical Context changes
* Material limitation changes

The required path is ordinarily:

```text
Issue Identified
    ↓
Authority Boundary Checked
    ↓
Correction Type Assigned
    ↓
Sources / Evidence Reviewed
    ↓
Original State Preserved
    ↓
Corrected State Prepared
    ↓
Materiality Assessed
    ↓
New Version Created
    ↓
Reverification
    ↓
Revalidation where Required
    ↓
Publication Updated
    ↓
Lineage Preserved
```

---

# No Silent Historical Rewriting

Chronicle must not silently alter substantive historical content.

This prohibition applies to material changes involving:

* Event Representation
* Event Date
* Event Type
* Historical Context
* Sources
* Authoritative references
* Evidence
* Provenance
* Relationships
* Verification limitations
* Publication-significant meaning

A changed record must leave evidence that it changed.

---

# Historical Immutability

Once a substantive Entry Version has been published or otherwise established as an institutional record state, it should remain historically immutable.

Chronicle should not overwrite that state.

Instead:

```text
Version 1
    ↓
Correction
    ↓
Version 2
```

Version 1 remains preserved.

---

# Resulting Version

When a Correction is material, the Correction Record should identify the resulting Version.

Example:

```text
Entry:
CHR-2026-0001

Prior Version:
1

Correction:
Event Date corrected

Resulting Version:
2
```

The Entry identifier remains stable.

---

# Correction Date

Correction Date should remain distinct from:

* Event Date
* Entry Creation Date
* Source Publication Date
* Source Retrieval Date
* Version Effective Date
* Publication Date

Chronicle should preserve these temporal distinctions.

---

# Affected Fields

A Formal Correction should identify the fields changed.

Example:

```text
Affected Fields:
event_date
historical_context
source_references
```

This improves:

* Reviewability
* Validation
* Version comparison
* Auditability
* Public transparency

---

# Reason for Correction

The reason should explain why Chronicle changed the record.

Potential reasons may include:

* Incorrect original value
* New authoritative Source
* New Evidence
* Misclassification
* Broken reference
* Provenance discovery
* Relationship error
* Historical-context clarification
* Duplicate-record discovery

Reason should not be reduced to a vague label when material historical meaning changed.

---

# Supporting Sources and Evidence

Material Corrections should be supported by Sources, Evidence, authoritative records, or other verifiable information whenever available.

Chronicle should preserve enough support to allow future reviewers to understand why the change was justified.

---

# Corrections Triggered by External Changes

Another Suite system may change its own authoritative record.

Chronicle should determine whether the external change requires:

```text
A Correction to Chronicle's existing representation
```

or:

```text
A distinct later qualifying Occurrence
→ New Chronicle Entry
```

Example:

A Certification Package is revoked.

If revocation is a distinct qualifying Occurrence, Chronicle should ordinarily create a new Chronicle Entry rather than rewrite the original certification-created Entry.

---

# Correction and Preservation Eligibility

A later external change may itself require Preservation Eligibility assessment.

Chronicle should not automatically convert every authoritative-system update into a Correction.

The key question is:

> Is Chronicle's existing record wrong, or did something new happen?

If Chronicle's record is wrong:

```text
Correction
```

If something new happened:

```text
New Occurrence
→ Preservation Eligibility
→ New Chronicle Entry
```

---

# Corrections and Verification

Verification and Correction remain separate.

## Verification

Reviews Chronicle's historical representation.

## Correction

Changes Chronicle's own record when a documented issue warrants change.

A material Correction should ordinarily trigger Reverification.

Example:

```text
Version 1
Verification State: Verified

Correction
    ↓

Version 2
Verification State: In Review
    ↓

Reverification
```

Prior Verification history remains preserved.

---

# Corrections and Validation

Substantive Corrections should be validated before publication.

Validation may include:

* Identifier integrity
* Schema conformance
* Controlled Values
* Required fields
* Authoritative reference checks
* Relationship integrity
* Provenance completeness
* Evidence linkage
* Version linkage
* Correction linkage
* Publication readiness

Not every Editorial Update requires full Revalidation.

---

# Corrections and Lifecycle

Correction is part of the normal Chronicle Entry Lifecycle.

Conceptually:

```text
Active Entry
    ↓
Issue Identified
    ↓
Correction
    ↓
New Version where Required
    ↓
Reverification
    ↓
Revalidation where Required
    ↓
Maintained / Republished
```

Correction does not create a new canonical identity unless the underlying issue actually reflects a distinct qualifying Occurrence.

---

# Corrections and Relationships

Corrections may change structured Relationships.

Relevant Relationship Types include:

```text
Corrects
Corrected By
Supersedes
Superseded By
```

These should be used according to the Chronicle Relationship Model.

---

# Correction Lineage

Correction lineage should allow future reviewers to reconstruct:

```text
Prior Version
Correction
Affected Fields
Corrected Version
Verification Result
Publication History
```

This lineage should remain durable.

---

# Duplicate Entry Corrections

If Chronicle discovers two identifiers represent the same Occurrence, it should not:

* Delete one silently
* Recycle an identifier
* Merge records without trace

A later duplicate-resolution procedure may use:

* Correction
* Withdrawal
* Supersession
* Canonical-reference Relationships

The identity history must remain preserved.

---

# Record Preservation

Chronicle favors Correction and Version preservation over deletion.

When practical:

* Original Chronicle states remain preserved
* Corrected states identify prior states
* Correction Records reference affected Entries
* Historical Relationships remain auditable
* Published substantive changes remain reviewable
* Authoritative external Suite records remain referenced rather than duplicated

---

# Deletion

Deletion should be rare.

Potential reasons may include:

* Legal requirement
* Privacy requirement
* Security requirement
* Integrity failure
* Operational necessity

Deletion should not be used as a substitute for Correction.

A deletion requirement should preserve as much lawful institutional lineage as possible.

---

# Correction Record Structure

A future Correction Record schema should include, at minimum:

```text
Correction Type
Affected Entry / Record
Original Information
Corrected Information
Correction Date
Reason
Affected Fields
Prior Version
Resulting Version
Supporting Sources
Supporting Evidence
Verification Impact
Validation Impact
Publication Impact
```

Some fields may be Conditional.

The Base Schema and Correction Record Schema should define exact implementation.

---

# Correction Validation Expectations

Future Validation should confirm, where applicable:

1. Correction Type is approved.
2. Affected record exists.
3. Original information is preserved.
4. Corrected information is present.
5. Correction date is valid.
6. Reason is present.
7. Affected fields are identified.
8. Prior Version is valid.
9. Resulting Version is valid when required.
10. Supporting references are valid.
11. Verification impact is recorded where required.
12. Publication lineage is consistent.
13. Authority boundaries are preserved.

---

# Correction Philosophy

Chronicle does not correct history by erasing its own mistakes.

It corrects its own historical representation transparently.

The record should become more accurate while retaining evidence of how Chronicle's understanding changed.

---

# Guiding Principle

> Preserve what Chronicle said. Preserve why Chronicle changed it.

And operationally:

> Correct visibly. Version materially. Preserve every substantive state.

---

## Relationship to Other Chronicle Documentation

Chronicle Corrections should remain aligned with:

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
* Versioning Policy
* Status
* Schemas
* Validation
* Publication Procedure

Corrections provide the transparent change mechanism within the Chronicle Entry Lifecycle.

---

## Next Operational Dependencies

The Correction model directly informs:

* Correction Record Schema
* Status reconciliation
* Lifecycle transition rules
* Chronicle Base Schema
* Certification Event-Type Profile
* Validation
* Production Procedure
* Publication history
* First production Chronicle Entry

The first production Correction should test the boundary between Editorial Update and Formal Correction and confirm that prior states remain practically retrievable.

---

## Status

**Active pre-operational Chronicle Corrections specification.**

The core requirements are now established:

```text
Original information
Corrected information
Correction date
Reason
Affected fields
Resulting Version
```

Correction Type is governed through the Chronicle Controlled Values Registry.

The exact minor-correction threshold, Correction Record identifier architecture, public Correction presentation, deletion handling, duplicate resolution, and automated Correction validation remain subject to later Phase VI and production-development work.
