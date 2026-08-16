# Chronicle Controlled Values Registry

## Purpose

The Chronicle Controlled Values Registry defines canonical vocabularies for Chronicle fields where stable institutional meaning is required for:

* Interoperability
* Validation
* Schema conformance
* Machine readability
* Public discovery
* Historical consistency
* Cross-record comparison

Controlled Values should be used where unrestricted free text would create ambiguity, inconsistent semantics, or validation difficulty.

They should not replace narrative fields where historical nuance matters.

The governing principle is:

> Stable terms for interoperability. Free text for history.

---

# Role of Controlled Values

Controlled Values provide governed terminology for specific structured fields.

They help Chronicle answer questions such as:

* Which Event Type applies?
* What is the Entry's operational state?
* What kind of Source is this?
* What kind of Evidence is this?
* What relationship exists between these objects?
* What is the Verification State?
* What is the Publication State?
* What Lifecycle State applies?
* What kind of Correction occurred?

A Controlled Value should have one defined institutional meaning.

---

# Controlled Values Are Not Narrative

Chronicle should not force all historical information into enumerated values.

Free-text fields remain appropriate for:

* Event Representation
* Historical Context
* Historical-Significance rationale
* Evidence limitations
* Provenance notes
* Verification notes
* Correction rationale
* Publication notes
* Other explanatory context

Controlled Values should govern fields where stable semantics matter more than expressive range.

---

# Initial Controlled Value Sets

The initial Chronicle Controlled Values Registry contains the following value sets:

```text
Event Type
Entry Status
Source Type
Evidence Type
Relationship Type
Verification State
Publication State
Lifecycle State
Correction Type
```

These sets are sufficient to support the next stages of Chronicle operational development without attempting to define every future controlled vocabulary.

---

# 1. Event Type

## Purpose

Event Type classifies the qualifying Occurrence represented by a Chronicle Entry.

Event Type is required by the Chronicle Entry Model.

Event Type is classification.

It is not a separate canonical object.

---

## Initial Event Type Values

The initial operational Event Type family is Certification Event.

Working values:

```text
Certification Created
Certification Renewed
Certification Suspended
Certification Revoked
Certification Expired
```

These values support the first operational Certification Event-Type Profile.

They should remain intentionally narrow.

Additional Event Types should be added only when production experience demonstrates a real historical classification need.

---

## Machine Tokens

Potential machine-readable forms may include:

```text
certification_created
certification_renewed
certification_suspended
certification_revoked
certification_expired
```

The machine token and human-readable label must retain identical meaning.

---

# 2. Entry Status

## Purpose

Entry Status provides a concise operational summary of the Chronicle Entry when such a summary is useful.

Initial values may include:

```text
Draft
Under Review
Approved
Published
Superseded
Withdrawn
```

Potential machine tokens:

```text
draft
under_review
approved
published
superseded
withdrawn
```

---

## Entry Status Limitation

Entry Status must not collapse or replace more specific state systems.

Chronicle distinguishes:

```text
Entry Status
Verification State
Validation State
Publication State
Lifecycle State
Preservation State
```

These concepts may overlap in ordinary language but remain institutionally distinct.

If operational experience demonstrates that Entry Status merely duplicates Lifecycle State, Chronicle may later deprecate Entry Status rather than maintain redundant vocabularies.

---

# 3. Source Type

## Purpose

Source Type classifies what kind of Source Chronicle references.

Initial values:

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

Potential machine tokens:

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

---

## Source Type Is Not Source Role

Source Type answers:

> What is the Source?

Source Role answers:

> How does the Source function in this Entry?

These concepts should remain separate.

A Source may be:

```text
Source Type: Institutional Document
Source Role: Primary
```

The initial Source Role vocabulary may be developed later if required by schema or production use.

---

# 4. Evidence Type

## Purpose

Evidence Type classifies the form of material that bears on a Chronicle Entry or claim.

Initial values:

```text
Authoritative Evidence
Documentary Evidence
Repository Evidence
Archival Evidence
Machine-Generated Evidence
Testimonial Evidence
Contextual Evidence
Other
```

Potential machine tokens:

```text
authoritative_evidence
documentary_evidence
repository_evidence
archival_evidence
machine_generated_evidence
testimonial_evidence
contextual_evidence
other
```

---

## Evidence Type Is Not Evidence Relationship

Evidence Type answers:

> What kind of Evidence is this?

Evidence Relationship answers:

> How does this Evidence bear on the Entry or claim?

Potential Evidence Relationship values may later include:

```text
Supports
Challenges
Contradicts
Clarifies
Corroborates
Contextualizes
Limits Confidence
```

Evidence Relationship may require its own Controlled Value set during schema development.

It is intentionally not frozen here unless operational need requires it.

---

# 5. Relationship Type

## Purpose

Relationship Type defines the semantic connection between a Chronicle Entry and another object.

Initial values:

```text
References
Related To
Derived From
Supersedes
Superseded By
Corrects
Corrected By
Precedes
Follows
```

Potential machine tokens:

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

## Relationship Direction

Some Relationship Types are directional.

Examples:

```text
Supersedes
Superseded By

Corrects
Corrected By

Precedes
Follows
```

Chronicle should define direction explicitly rather than relying on interpretation.

---

## Relationship Integrity

Relationship Type must not imply facts unsupported by the underlying records.

For example:

```text
Related To
```

should not be replaced by:

```text
Caused By
```

unless causation is genuinely established and Chronicle later approves such a relationship.

Controlled Values should constrain semantic overreach.

---

# 6. Verification State

## Purpose

Verification State represents Chronicle's review state for its own historical representation.

Initial values:

```text
Not Reviewed
In Review
Verified
Verified with Limitations
Unresolved
```

Potential machine tokens:

```text
not_reviewed
in_review
verified
verified_with_limitations
unresolved
```

---

## Verified

`Verified` means Chronicle completed the applicable Verification process and found the Entry's historical representation sufficiently supported under current Chronicle rules.

It does not mean:

* Universal truth
* Certifier certification
* External attestation
* Absolute certainty

---

## Verified with Limitations

`Verified with Limitations` means Chronicle completed applicable review but material limitations remain visible.

Potential limitations may include:

* Missing Source
* Incomplete Provenance
* Conflicting Evidence
* Archival-only material
* Uncertain temporal detail
* Other documented limitation

---

## Unresolved

`Unresolved` means a material historical issue remains open.

An Entry may still require preservation because unresolved history can itself be historically important.

Publication rules should later determine whether and under what conditions an Unresolved Entry may be published.

---

# 7. Publication State

## Purpose

Publication State represents the Chronicle record's position within the controlled publication process.

Initial values:

```text
Not Published
Pending Publication
Published
Withdrawn from Publication
```

Potential machine tokens:

```text
not_published
pending_publication
published
withdrawn_from_publication
```

---

## Publication State Is Distinct

Publication State must remain distinct from:

* Entry Status
* Verification State
* Validation State
* Lifecycle State
* Preservation State

A record may be:

```text
Verification State: Verified
Publication State: Not Published
```

without contradiction.

---

# 8. Lifecycle State

## Purpose

Lifecycle State represents the institutional lifecycle state of the Chronicle Entry itself.

Initial values:

```text
Draft
Active
Superseded
Withdrawn
Preserved
```

Potential machine tokens:

```text
draft
active
superseded
withdrawn
preserved
```

---

## Lifecycle State Does Not Represent External Object Status

Chronicle Entry Lifecycle State must not inherit the lifecycle of the external authoritative object.

Example:

```text
Certification Status:
Revoked

Chronicle Entry Lifecycle State:
Active
```

The Chronicle Entry may remain an active historical record preserving a revoked certification event.

---

## Preserved

`Preserved` should be used only if Chronicle later determines that preservation itself needs a lifecycle endpoint distinct from active publication.

If this distinction proves unnecessary, Lifecycle vocabulary may be simplified.

Controlled Values should be refined from production experience rather than preserved merely because they were initially proposed.

---

# 9. Correction Type

## Purpose

Correction Type classifies the nature of a change to a Chronicle-owned record.

Initial values:

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

Potential machine tokens:

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

## Typographical

Corrects spelling, punctuation, or similar presentation defects without changing institutional meaning.

---

## Metadata

Corrects structured metadata without materially changing the historical representation.

---

## Contextual

Corrects or improves Historical Context.

Depending on materiality, a Contextual Correction may require a new Entry Version.

---

## Relationship

Corrects or changes a structured Relationship.

---

## Provenance

Corrects or improves Provenance.

---

## Evidence

Corrects Evidence references, Evidence classification, or Evidence-related representation.

---

## Classification

Corrects Event Type or another controlled classification.

Because Event Type is not encoded into the identifier, a classification correction does not require a new Chronicle Entry identifier.

---

## Substantive

Changes material historical meaning.

Substantive Corrections should require preserved prior state and explicit Version lineage.

---

# Candidate Future Controlled Value Sets

Chronicle may later require additional registries.

Potential candidates include:

```text
Source Role
Evidence Relationship
Validation State
Preservation State
Eligibility Decision State
Historical Significance Factor
Automatic Preservation Class
Provenance Method
Publication Method
Reviewer Role
Correction Severity
```

These are not yet canonical Controlled Value sets.

They should be created only when operational work demonstrates a real need.

---

# Controlled Value Governance

A new Controlled Value should follow a governed process.

Conceptually:

```text
Need Identified
    ↓
Existing Values Reviewed
    ↓
Meaning Defined
    ↓
Overlap Checked
    ↓
Value Approved
    ↓
Machine Token Assigned
    ↓
Registry Version Updated
    ↓
Schema / Validation Updated
    ↓
Production Use
```

---

# New Value Criteria

A new value should be added only when:

* Existing values are insufficient
* The distinction has operational meaning
* The value can be defined clearly
* The value will improve consistency
* The value is likely to be reused
* The value does not merely encode narrative nuance better handled in free text

---

# Avoiding Vocabulary Inflation

Chronicle should avoid creating values for every possible nuance.

For example, instead of:

```text
Verified
Mostly Verified
Nearly Verified
Highly Verified
Partially Verified
Provisionally Verified
```

Chronicle should prefer a smaller set with explanatory notes.

Controlled vocabularies should clarify meaning, not manufacture artificial precision.

---

# One Value, One Meaning

Each Controlled Value should have one stable institutional meaning.

Different values should not be used as stylistic synonyms.

Avoid:

```text
Published
Public
Released
Live
```

if all are intended to mean the same institutional state.

Choose one canonical term.

---

# Human-Readable Labels and Machine Tokens

A Controlled Value may have:

* Human-readable label
* Machine-readable token

Example:

```text
Human label:
Verified with Limitations

Machine token:
verified_with_limitations
```

Both forms represent the same value.

Machine tokens should be:

* Lowercase
* Stable
* ASCII-safe
* Predictable
* Free of presentation punctuation where practical

Snake case is a reasonable initial convention.

---

# Canonical Storage

Machine-readable production records should ordinarily store the machine token.

Public interfaces may display the human-readable label.

Example:

```json
{
  "verification_state": "verified_with_limitations"
}
```

Public display:

```text
Verified with Limitations
```

The final schema implementation will determine exact representation.

---

# Versioning

The Controlled Values Registry should eventually carry a registry Version.

This is distinct from:

* Chronicle Entry Version
* Schema Version
* Event-Type Profile Version

A record should be interpretable according to the vocabulary in effect under its governing schema or profile.

---

# Semantic Stability

The meaning of an existing Controlled Value must not silently change.

If a value's meaning materially changes, Chronicle should consider:

* Clarification without semantic change
* Deprecation
* Replacement
* New value
* Migration
* Registry Version change

Historical records must remain interpretable.

---

# Deprecation

Deprecated values should remain documented.

A deprecation record should preserve:

* Deprecated label
* Deprecated machine token
* Meaning
* Reason for deprecation
* Effective date
* Replacement value where applicable
* Migration guidance if required

Existing historical records should not become unintelligible because a vocabulary evolved.

---

# Replacement

When a Controlled Value is replaced, Chronicle should avoid silently rewriting historical records unless formal migration rules require it.

A historical Entry may retain the old value under the schema and registry version governing that record state.

---

# Controlled Values and Schemas

Schemas should reference the Controlled Values Registry rather than independently inventing vocabulary.

Conceptually:

```text
Controlled Values Registry
        ↓
Chronicle Base Schema
        ↓
Event-Type Profile
        ↓
Validation
```

This centralizes semantics.

---

# Controlled Values and Validation

Validation should eventually confirm:

* Value belongs to the correct value set
* Value is approved
* Value is valid for the applicable schema Version
* Value is valid for the Event-Type Profile
* Deprecated value handling is correct
* Human and machine forms are not confused
* Free text is not used where a Controlled Value is required

---

# Controlled Values and Interoperability

Stable Controlled Values improve interoperability because different Chronicle Entries use the same terms for the same meaning.

This enables:

* Machine filtering
* Cross-entry comparison
* Timeline grouping
* Search
* Analytics
* Event-Type Profile selection
* Relationship interpretation
* Validation
* Future Suite interoperability

---

# Controlled Values and Historical Preservation

Historical records must remain understandable even after vocabularies evolve.

Chronicle should therefore preserve enough version context to answer:

> What did this value mean when this record Version was created?

Vocabulary evolution must not erase historical semantics.

---

# Controlled Values and Free Text

Chronicle should use Controlled Values where institutional semantics must remain stable.

Chronicle should use free text where nuance matters.

Examples:

### Controlled

```text
Event Type
Verification State
Publication State
Relationship Type
Correction Type
```

### Free Text

```text
Event Representation
Historical Context
Historical-Significance Rationale
Evidence Limitations
Correction Rationale
```

This balance preserves both interoperability and historical meaning.

---

# Initial Registry Summary

## Event Type

```text
Certification Created
Certification Renewed
Certification Suspended
Certification Revoked
Certification Expired
```

## Entry Status

```text
Draft
Under Review
Approved
Published
Superseded
Withdrawn
```

## Source Type

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

## Evidence Type

```text
Authoritative Evidence
Documentary Evidence
Repository Evidence
Archival Evidence
Machine-Generated Evidence
Testimonial Evidence
Contextual Evidence
Other
```

## Relationship Type

```text
References
Related To
Derived From
Supersedes
Superseded By
Corrects
Corrected By
Precedes
Follows
```

## Verification State

```text
Not Reviewed
In Review
Verified
Verified with Limitations
Unresolved
```

## Publication State

```text
Not Published
Pending Publication
Published
Withdrawn from Publication
```

## Lifecycle State

```text
Draft
Active
Superseded
Withdrawn
Preserved
```

## Correction Type

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

---

# Registry Principle

> Control meaning where consistency matters.  
> Preserve flexibility where historical nuance matters.

And operationally:

> Stable terms for interoperability. Free text for history.

---

## Relationship to Other Chronicle Documentation

The Controlled Values Registry should remain aligned with:

* Definitions
* Entry Model
* Event Type Framework
* Preservation Eligibility
* Chronicle Rules
* Identifier Specification
* Sources
* Evidence
* Verification
* Corrections
* Schemas
* Integration
* Validation
* Production Procedure

Controlled Values form a key bridge between conceptual architecture and machine-validatable production records.

---

## Next Operational Dependencies

The Controlled Values Registry directly informs:

* Relationship Architecture
* Provenance
* Lifecycle
* Versioning
* Corrections
* Chronicle Base Schema
* Certification Event-Type Profile
* Validation
* Production Procedure
* First production Chronicle Entry

Production experience should be used to remove redundant values, clarify ambiguous values, and add only those vocabularies that prove necessary.

---

## Status

**Active pre-operational Chronicle Controlled Values Registry.**

The value sets and values in this document are the initial operational vocabulary for Phase IV development.

They should be treated as canonical working values for implementation planning, while remaining subject to controlled refinement before or during first production use where real operational evidence demonstrates a need.
