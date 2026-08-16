# Chronicle Entry Lifecycle

## Purpose

The Chronicle Entry Lifecycle defines the complete institutional journey of a canonical Chronicle Entry.

The lifecycle begins when a potentially qualifying Occurrence is identified and continues through:

* Preservation Eligibility
* Entry drafting
* Source linking
* Evidence and Provenance assembly
* Verification
* Validation
* Publication
* Maintenance
* Correction
* Versioning
* Reverification
* Withdrawal or Supersession where applicable
* Long-term historical preservation

The lifecycle exists because a Chronicle Entry is not merely a static published page.

It is a durable institutional record with a history of its own.

The governing principle is:

> Create carefully. Review explicitly. Maintain visibly. Preserve the lineage.

---

# Lifecycle Model

The initial conceptual sequence is:

```text
Occurrence Identified
        ↓
Preservation Eligibility Assessed
        ↓
Entry Drafted
        ↓
Sources / Authoritative References Linked
        ↓
Evidence / Provenance / Relationships Assembled
        ↓
Verification Performed
        ↓
Validation Performed
        ↓
Entry Published
        ↓
Entry Maintained
        ↓
Corrected / Versioned if Necessary
        ↓
Historically Preserved
```

This is the institutional model.

It should not be interpreted as a rigid software workflow in which every Entry can move only once in one direction.

---

# Lifecycle Is Iterative

Published Entries may return to review.

Example:

```text
Published Entry
      ↓
New Evidence
      ↓
Correction
      ↓
New Entry Version
      ↓
Reverification
      ↓
Revalidation where required
      ↓
Republished / Maintained
```

The lifecycle therefore contains loops.

Correction and Versioning are ordinary lifecycle functions.

---

# Stage 1 — Occurrence Identified

A potentially meaningful Occurrence is discovered or reported.

Examples may include:

* Certification created
* Certification revoked
* Registry action
* Governance change
* First publication
* Milestone
* Architectural change
* Other qualifying historical development

At this stage Chronicle has not yet decided to create a canonical Entry.

---

# Stage 2 — Preservation Eligibility Assessed

Chronicle applies the Preservation Eligibility Model.

The governing question is:

> Should Chronicle preserve this Occurrence?

Possible conceptual outcomes include:

```text
Eligible
Not Eligible
Deferred
```

These remain conceptual until formally governed as Controlled Values.

An Occurrence should not become a production Chronicle Entry merely because it was detected.

---

# Stage 3 — Entry Drafted

Once Chronicle proceeds with preservation, a draft Chronicle Entry is created.

The Entry should conform conceptually to:

* Chronicle Entry Model
* Chronicle Identifier Specification
* Event Type Framework
* Applicable Event-Type Profile
* Chronicle Rules

The canonical object remains:

```text
Chronicle Entry
```

No separate Chronicle Event object is created.

---

# Identifier Assignment and Lifecycle

The Identifier Specification establishes:

```text
CHR-YYYY-NNNN
```

The exact procedural moment of canonical identifier assignment remains subject to Production Procedure design.

However:

> A canonical CHR identifier should not be assigned before Preservation Eligibility is established.

If an identifier is reserved and later abandoned, it remains consumed and must not be reused.

---

# Stage 4 — Sources and Authoritative References Linked

Chronicle should identify and link the Sources needed to support the Entry.

This may include:

* Authoritative Source Records
* Supporting Sources
* Referenced External Sources
* Authoritative Suite objects
* SREG Registry Entries
* Repository records
* Archival Sources

The Source architecture governs whether a separate Source Record is required or a direct reference is sufficient.

---

# Stage 5 — Evidence, Provenance, and Relationships Assembled

Before ordinary production review, Chronicle should assemble enough supporting architecture to make the Entry reviewable.

This may include:

## Evidence

Material bearing on the Entry or claim.

## Provenance

How information originated, moved, and entered Chronicle.

## Relationships

How the Entry connects to:

* Authoritative records
* Source Records
* Other Chronicle Entries
* Related Occurrences
* Registry Entries
* Originating systems

## Historical Context

Narrative context explaining the Occurrence and its significance.

## Limitations

Known uncertainty, missing material, conflicting Evidence, or incomplete Provenance.

---

# Stage 6 — Verification Performed

Chronicle applies the Verification Procedure.

Verification checks Chronicle's own representation.

It may verify:

* Entry identifier correctness
* Source Record existence
* Authoritative reference correctness
* Event-date consistency
* Relationship consistency
* Evidence availability
* Provenance consistency
* Historical Context support
* Material limitations

Verification does not re-adjudicate authority belonging to another institution.

---

# Verification State

The current Controlled Values are:

```text
Not Reviewed
In Review
Verified
Verified with Limitations
Unresolved
```

Verification State and Lifecycle State remain distinct.

Example:

```text
Lifecycle State:
Active

Verification State:
Verified with Limitations
```

This is valid.

---

# Stage 7 — Validation Performed

Validation determines whether the Chronicle Entry conforms to structural and procedural requirements.

Validation may review:

* Identifier format
* Required fields
* Controlled Values
* Schema conformance
* Event-Type Profile conformance
* Source references
* Relationship structure
* Provenance fields
* Evidence fields
* Version information
* Publication prerequisites

Conceptually:

```text
Verification = Does the historical representation hold together?
Validation = Does the record conform to the rules and structure?
```

These remain separate.

---

# Stage 8 — Entry Published

Publication occurs when Chronicle's publication requirements are satisfied.

Publication should be treated as a controlled lifecycle event.

Publication is not the final lifecycle stage.

A published Entry remains subject to:

* Maintenance
* Correction
* Versioning
* Reverification
* Revalidation
* Withdrawal
* Supersession
* Preservation

---

# Publication State

Publication State is separate from Lifecycle State.

Current Controlled Values include:

```text
Not Published
Pending Publication
Published
Withdrawn from Publication
```

Example:

```text
Lifecycle State:
Active

Publication State:
Published
```

or:

```text
Lifecycle State:
Active

Publication State:
Not Published
```

Both may be valid.

---

# Stage 9 — Entry Maintained

A Chronicle Entry should remain actively maintainable after publication.

Maintenance may include:

* Reference checks
* Archive maintenance
* Source availability updates
* Provenance additions
* Relationship updates
* Integrity checks
* Public-link maintenance
* Evidence availability updates
* Schema migration where required
* Correction review
* Version review

Maintenance should not silently alter historical meaning.

---

# Stage 10 — Correction and Versioning

A Chronicle Entry may require Correction when Chronicle discovers:

* Typographical error
* Metadata error
* Contextual error
* Relationship error
* Provenance error
* Evidence error
* Classification error
* Substantive historical error

Correction Type should use the Controlled Values Registry.

---

# Entry Versioning

Material changes should preserve Version lineage.

Conceptually:

```text
CHR-2026-0001
Version 1
      ↓
Correction
      ↓
CHR-2026-0001
Version 2
```

The canonical identifier remains unchanged.

Entry Version and Schema Version remain separate.

---

# Reverification

Material changes may trigger Reverification.

Potential triggers include:

* New Evidence
* New Source
* Event-Date correction
* Relationship change
* Provenance correction
* Historical Context correction
* Authoritative reference update
* Substantive Entry Version

A prior Verification result should remain historically traceable.

---

# Revalidation

A new Entry Version may require Revalidation where:

* Required fields changed
* Controlled Values changed
* Schema Version changed
* Event-Type Profile requirements changed
* Relationship structure changed
* Publication prerequisites changed

Not every minor Correction necessarily requires full Revalidation.

That threshold should be settled in Production Procedure.

---

# Stage 11 — Historically Preserved

Chronicle should retain durable historical memory of the Entry and its lineage.

Historical preservation should retain enough information to understand:

* Original Entry state
* Published state
* Correction history
* Version lineage
* Verification history
* Relationship history
* Source history
* Provenance history
* Withdrawal or Supersession
* Long-term preservation context

The current state matters.

The path to the current state also matters.

---

# Lifecycle State

Lifecycle State provides a compact controlled representation of the Entry's broader institutional position.

The initial Controlled Values are:

```text
Draft
Active
Superseded
Withdrawn
Preserved
```

These values do not encode every step in the lifecycle.

They summarize institutional position.

---

# Draft

`Draft` means the Chronicle Entry exists but remains under development.

A Draft Entry may still be:

```text
Verification State:
Not Reviewed
```

or:

```text
Verification State:
In Review
```

It will ordinarily not yet be in ordinary public production use.

---

# Active

`Active` means the Entry is an institutionally active Chronicle record.

An Active Entry may be:

* Published
* Not Published
* Verified
* Verified with Limitations
* Unresolved
* Under maintenance
* Under Correction
* Under Reverification

Active does not mean unchangeable.

---

# Superseded

`Superseded` means a later Chronicle-owned record state or Entry formally or materially replaced the earlier representation for a defined purpose.

Conceptually:

```text
Superseded ≠ Deleted
```

The earlier record remains historically meaningful.

A Supersedes / Superseded By Relationship should be used where appropriate.

---

# Withdrawn

`Withdrawn` means Chronicle removed the Entry from ordinary active use or publication while preserving its identity and history.

Withdrawal should preserve:

* Entry identifier
* Reason
* Effective date
* Prior Version
* Publication history
* Verification history
* Relationships
* Correction history

Identifiers are never recycled.

---

# Preserved

`Preserved` may represent an Entry whose active operational handling has ended or stabilized while the record remains retained as durable historical memory.

However, this value should remain under observation.

Production experience may show that:

* `Preserved` is useful as a Lifecycle State

or that:

* Preservation is better represented independently from Lifecycle State

If redundant, Chronicle should simplify rather than preserve unnecessary vocabulary.

---

# Lifecycle and Entry Status

Lifecycle State and Entry Status are different concepts.

## Lifecycle State

Answers:

> Where is the Entry in its broader institutional journey?

## Entry Status

Answers:

> What concise operational condition currently applies?

The Controlled Values Registry currently contains initial Entry Status values:

```text
Draft
Under Review
Approved
Published
Superseded
Withdrawn
```

There is significant conceptual overlap.

Production work should determine whether Entry Status adds useful information beyond:

* Lifecycle State
* Verification State
* Publication State

If Entry Status proves redundant, it should be deprecated.

---

# Lifecycle and Verification State

Lifecycle State does not describe Verification.

Example:

```text
Lifecycle State:
Active

Verification State:
Unresolved
```

This may be valid.

A historically important Entry can remain active while unresolved.

---

# Lifecycle and Publication State

Lifecycle State does not describe Publication.

Example:

```text
Lifecycle State:
Active

Publication State:
Pending Publication
```

also valid.

---

# Lifecycle and Preservation Eligibility

Preservation Eligibility occurs before ordinary Entry lifecycle handling.

Eligibility asks:

> Should Chronicle preserve the Occurrence?

Lifecycle asks:

> What institutional path does the Entry follow once Chronicle proceeds with preservation?

---

# Lifecycle and Preservation State

Preservation State, if later formalized, should describe the continuing archival or preservation condition of the Entry or supporting material.

It should not automatically be treated as identical to Lifecycle State.

This distinction remains open for production refinement.

---

# Lifecycle and Event Type

Event Type classifies the Occurrence.

Lifecycle describes the institutional journey of the Entry.

Example:

```text
Event Type:
Certification Revoked

Lifecycle State:
Active
```

No contradiction exists.

---

# Lifecycle and Identifier

The Chronicle identifier remains stable across lifecycle transitions.

Example:

```text
CHR-2026-0001
Draft
      ↓
Active
      ↓
Corrected
      ↓
Version 2
      ↓
Superseded
```

The identifier remains:

```text
CHR-2026-0001
```

unless a genuinely distinct qualifying Occurrence requires a new Entry.

---

# Lifecycle and Relationships

Lifecycle changes may create or modify Relationships.

Examples:

```text
Supersedes
Superseded By
Corrects
Corrected By
Precedes
Follows
```

Relationship semantics should remain explicit.

---

# Lifecycle and Corrections

Corrections should preserve prior state where material.

A Correction should not silently rewrite the historical record.

Conceptually:

```text
Existing Entry
    ↓
Correction identified
    ↓
Correction classified
    ↓
Prior state preserved
    ↓
New Version if material
    ↓
Reverification / Revalidation if required
```

---

# Lifecycle and Versioning

Versioning records substantive evolution of the same canonical Chronicle Entry.

Versioning is not a new Occurrence by itself.

However, a material institutional change associated with the Entry may itself become a separate qualifying Occurrence and receive its own Chronicle Entry.

This distinction should be assessed using Preservation Eligibility.

---

# Retrospective Preservation

Chronicle allows retrospective Entries.

Example:

```text
Occurrence Date:
2024

Chronicle Entry created:
2026

Identifier assignment:
2026
```

The Entry follows the same lifecycle.

Chronicle should not alter the Event Date merely because the record was created later.

---

# Automatic and Discretionary Preservation

The Preservation Eligibility Model allows:

* Automatic Preservation
* Discretionary Preservation
* Retrospective Preservation

Lifecycle behavior after preservation admission should remain broadly consistent regardless of the eligibility path.

Profiles may impose specialized review requirements.

---

# Lifecycle Exceptions

Some Entries may require altered procedural order.

Examples:

* Emergency historical preservation
* Archive rescue
* Retrospective preservation
* Limited-source historical record
* Time-sensitive publication
* Migration of legacy records

Any exception should preserve the institutional requirements even if operational order differs.

For example, an urgent Entry might be published before full secondary review only if future Production Procedure explicitly allows such a path and preserves the outstanding review state.

No such exception is currently authorized by this Lifecycle Model.

---

# Historical Lifecycle Trace

Chronicle should eventually be able to reconstruct:

```text
Identified
Eligibility established
Draft created
Sources linked
Evidence assembled
Verification completed
Validation completed
Published
Corrected
Versioned
Reverified
Superseded / Withdrawn / Preserved
```

This history should be reviewable even if not every internal event is publicly displayed.

---

# Lifecycle Validation Expectations

Future Validation should confirm, where applicable:

1. Lifecycle State is an approved Controlled Value.
2. Lifecycle transition is permitted.
3. Required preceding institutional steps are complete.
4. Publication State is consistent with publication procedure.
5. Verification State requirements are satisfied.
6. Required Corrections are linked.
7. Entry Version is valid.
8. Supersession Relationships are valid.
9. Withdrawal reason is recorded where required.
10. Event-Type Profile lifecycle requirements are satisfied.

---

# Candidate Transition Model

A preliminary transition model may be:

```text
Draft
  ↓
Active
  ├──→ Withdrawn
  ├──→ Superseded
  └──→ Preserved
```

But this should not yet be treated as a frozen state machine.

Production experience must determine:

* Whether `Preserved` is necessary
* Whether `Active` is too broad
* Whether `Withdrawn` and `Superseded` are terminal
* Whether reactivation is allowed
* Whether Draft can be abandoned without becoming Withdrawn
* Whether an internal Reserved / Abandoned state is needed

These questions belong to later lifecycle and Status refinement.

---

# Lifecycle Principle

Chronicle should treat lifecycle history as part of institutional trust.

A durable record should allow future reviewers to understand:

* What the Entry currently says
* How it reached that state
* What changed
* Why it changed
* Which prior state existed
* Which review followed the change

---

# Guiding Principle

> A durable historical record preserves not only the Entry, but the path the Entry traveled.

And operationally:

> Create carefully. Review explicitly. Maintain visibly. Preserve the lineage.

---

## Relationship to Other Chronicle Documentation

The Chronicle Entry Lifecycle should remain aligned with:

* Entry Model
* Event Type Framework
* Preservation Eligibility
* Chronicle Rules
* Identifier Specification
* Controlled Values Registry
* Relationship Model
* Provenance Model
* Sources
* Evidence
* Verification Procedure
* Corrections
* Versioning
* Status
* Historical Preservation
* Schemas
* Validation
* Publication Procedure

Lifecycle connects these systems into the institutional journey of the canonical Entry.

---

## Next Operational Dependencies

The Lifecycle Model directly informs:

* Corrections
* Versioning
* Status reconciliation
* Publication State rules
* Chronicle Base Schema
* Certification Event-Type Profile
* Validation
* Production Procedure
* First production Chronicle Entry

The first production Entry should test whether the conceptual lifecycle is complete, proportionate, and free of redundant states.

---

## Status

**Active pre-operational Chronicle Entry Lifecycle specification.**

The complete conceptual lifecycle is established.

Initial Lifecycle State values are governed through the Controlled Values Registry:

```text
Draft
Active
Superseded
Withdrawn
Preserved
```

The final transition rules, relationship between Entry Status and Lifecycle State, role of Preserved, abandonment handling, reactivation rules, and publication gating should be finalized through later Phase VI and production-development work.
