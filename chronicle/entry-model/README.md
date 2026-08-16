# Chronicle Entry Model

## Purpose

The Chronicle Entry Model defines the canonical conceptual structure of a **Chronicle Entry** before that structure is translated into formal schemas.

This document answers:

> What logical components must a Chronicle Entry contain in order to function as Chronicle's canonical historical-preservation object?

The Entry Model is intentionally architectural rather than schema-specific.

It establishes:

* The major logical components of a Chronicle Entry
* The role of each component
* Which components are Required
* Which components are Conditional
* Which components are Optional
* How those components relate to Chronicle authority, preservation, verification, versioning, and publication
* The boundary between conceptual architecture and later schema implementation

The Entry Model should be settled before the Chronicle Base Schema is finalized.

---

## Canonical Object

The canonical object of Satoshium Chronicle is the **Chronicle Entry**.

The underlying Occurrence is what happened.

The Chronicle Entry is Chronicle's structured historical-preservation record representing that qualifying Occurrence.

Conceptually:

```text
Occurrence
    ↓
Preservation Eligibility
    ↓
Chronicle Entry
```

The Entry Model defines the conceptual anatomy of that canonical object.

It does not create a second object called a Chronicle Event.

---

## Entry Model Before Schema

The Entry Model and Chronicle Base Schema serve different purposes.

### Entry Model

Defines:

* What the Entry must mean
* Which logical components exist
* Why those components exist
* Which components are Required, Conditional, or Optional
* How components relate institutionally

### Chronicle Base Schema

Will later define:

* Field names
* Data types
* Required properties
* Conditional rules
* Controlled Values
* Identifier syntax
* Machine-readable validation
* Object nesting
* Reference structure
* Formal schema versioning

Conceptually:

```text
Entry Model
    ↓
Chronicle Base Schema
    ↓
Event-Type Profile
    ↓
Production Chronicle Entry
```

The schema implements the model.

The model should not be reduced to whatever happens to be convenient in the first schema draft.

---

## Requirement Classes

Every logical Entry component belongs to one of three requirement classes.

### Required

A Required component must be present in every production Chronicle Entry.

Required components define the minimum institutional meaning of the canonical object.

### Conditional

A Conditional component becomes required when an approved condition applies.

Conditions may arise from:

* Event Type
* Event-Type Profile
* Presence of Evidence
* Presence of Sources
* Existence of related records
* Existence of authoritative external objects
* Correction history
* Version history
* Publication requirements
* Other Chronicle rules

A component that is normally Conditional may become Required under a specific Event-Type Profile.

### Optional

An Optional component may be included when it adds meaningful historical or operational value but is not universally applicable.

Optional does not mean unimportant.

Optional means:

> Not required for every Chronicle Entry.

Optional components must not redefine the canonical object or bypass required institutional structure.

---

# Major Logical Components

## 1. Identity

**Requirement:** Required

Identity establishes the stable identity of the Chronicle Entry.

Conceptually, Identity should support:

* Chronicle Entry identifier
* Human-readable title or label
* Record type
* Governing schema identity
* Schema version
* Entry version

Identity must allow a Chronicle Entry to be distinguished from:

* Other Chronicle Entries
* Supporting Chronicle records
* Authoritative records owned by other Suite systems

The final identifier format remains to be established through Chronicle Identifier Architecture.

---

## 2. Event Representation

**Requirement:** Required

Event Representation describes the qualifying historical Occurrence preserved by the Entry.

It should answer:

> What happened?

The representation should be sufficiently precise to identify the historical action, change, state transition, milestone, decision, publication, governance development, or other qualifying Occurrence.

Event Representation is not the same as Event Type.

Event Representation describes the specific Occurrence.

Event Type classifies it.

---

## 3. Temporal Information

**Requirement:** Required

Temporal Information preserves the time associated with the underlying Occurrence and Chronicle's own recordkeeping actions.

At minimum, the model must distinguish:

* Event Date
* Entry Creation Date
* Publication Date where publication occurs
* Correction Date where correction occurs
* Version Date where version change occurs

Conceptually:

```text
Event Date
≠ Entry Creation Date
≠ Publication Date
≠ Correction Date
≠ Version Date
```

This distinction is especially important for retrospective preservation.

An Entry created years after an Occurrence must not imply that the Occurrence happened on the Entry creation date.

---

## 4. Event Type

**Requirement:** Required

Event Type classifies the Occurrence represented by the Entry.

Event Type should use an approved Controlled Value.

The Event Type may determine whether an Event-Type Profile applies.

Potential future Event Types may include certification lifecycle events, Registry milestones, governance developments, Suite releases, institutional milestones, and other approved historical classes.

Final Event Type values remain subject to Controlled Values development.

---

## 5. Historical Context

**Requirement:** Required

Historical Context explains why the Occurrence matters and provides the surrounding information needed to understand it.

Historical Context may include:

* Institutional context
* Relevant prior events
* Relevant later events
* Historical Significance
* Participants
* Jurisdiction or location
* Governance context
* Operational context
* Relationship to Suite development
* Relevant limitations

Historical Context should help future reviewers understand the Entry without turning Chronicle into an unrestricted narrative system.

---

## 6. Source Record References

**Requirement:** Conditional

Source Record References connect the Chronicle Entry to Chronicle Source Records.

They should be present when Source Records are used to establish:

* Origin
* Attribution
* Context
* Publication history
* Archival history
* Supporting information

Source Record References may become Required through an Event-Type Profile.

A Source Record remains a supporting Chronicle-owned record.

It is not part of the canonical object hierarchy above Chronicle Entry.

---

## 7. Relationships

**Requirement:** Conditional

Relationships connect the Chronicle Entry to other relevant objects.

Potential relationship targets may include:

* Other Chronicle Entries
* Source Records
* Evidence Records
* Correction Records
* Prior or resulting Versions
* Certification Packages
* SREG Registry Entries
* Integrity References
* Discovery Signals
* Trust Statements
* Workflow Definitions
* Atlas records
* Other approved authoritative or external objects

Relationships should use approved Controlled Values.

Relationships must not imply unsupported causation or transfer institutional authority.

---

## 8. Provenance

**Requirement:** Required

Provenance documents how the information supporting the Chronicle Entry originated, moved, was accessed, and entered Chronicle.

Provenance may include:

* Originating system
* Originating institution
* Source path
* Acquisition method
* Access method
* Capture method
* Transfer history
* Archival path
* Preservation history
* Related authoritative record

Provenance is distinct from Source.

Source answers:

> Where did the information come from?

Provenance answers:

> How did the information get here?

Every production Chronicle Entry should contain enough Provenance to make its origin and construction traceable.

---

## 9. Evidence

**Requirement:** Conditional

Evidence connects the Entry to material that bears on its historical representation.

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Corroborate
* Contextualize
* Limit confidence

Evidence may be represented through Evidence Records or other approved structures.

Evidence becomes Required when:

* An Event-Type Profile requires it
* Verification relies on it
* Historical claims require evidentiary support
* A Correction relies on new Evidence
* Chronicle rules otherwise require it

The absence of Evidence should not automatically mean the Occurrence is ineligible for preservation if authoritative records or other valid historical bases exist.

---

## 10. Verification

**Requirement:** Required

Verification records Chronicle's review of its own historical representation.

Verification may include:

* Verification State
* Reviewer or reviewing process
* Authoritative-reference consistency
* Source consistency
* Evidence review
* Provenance review
* Temporal consistency
* Relationship integrity
* Known limitations
* Contradictions
* Corroboration

Verification does not re-adjudicate another Suite system's authoritative determination.

Every production Chronicle Entry should have an explicit Verification state, even if that state reflects unresolved or incomplete review.

Final Verification State values remain to be defined.

---

## 11. Version

**Requirement:** Required

Version identifies the preserved state of a Chronicle Entry.

Every Entry should have an Entry Version.

Versioning supports:

* Correction lineage
* Material updates
* Historical reconstruction
* Prior-state preservation
* Publication history
* Long-term traceability

Entry Version is distinct from Schema Version.

Conceptually:

```text
Entry Version ≠ Schema Version
```

---

## 12. Correction History

**Requirement:** Conditional

Correction History connects the Entry to Chronicle Corrections when the Entry has been materially changed.

Correction History may include:

* Correction Record references
* Prior Version
* Resulting Version
* Correction reason
* Corrected fields
* Supporting Evidence
* Approval information
* Publication information

If no Correction has occurred, Correction History may be absent.

When a substantive Correction occurs, Correction History becomes Required.

Chronicle should not silently rewrite material historical content.

---

## 13. Publication State

**Requirement:** Required

Publication State identifies the Entry's state within Chronicle's publication process.

Publication State must remain distinct from:

* Verification State
* Validation State
* Lifecycle State
* Preservation State
* Status of the underlying external object

An Entry may exist before public publication.

The final Publication State vocabulary remains to be established through Controlled Values.

---

## 14. Lifecycle / Status

**Requirement:** Required

Lifecycle / Status represents the institutional state of the Chronicle Entry within Chronicle.

This must remain separate from the lifecycle of the underlying object represented by the Entry.

For example:

A Chronicle Entry preserving a revoked certification may itself be a valid, published, active historical record.

The certification lifecycle state and the Chronicle Entry lifecycle state are different concepts.

Potential Chronicle Entry lifecycle concepts may include:

* Draft
* Under Review
* Validated
* Approved
* Published
* Corrected
* Superseded
* Preserved

These are working concepts only.

Final values remain subject to Lifecycle and Controlled Values development.

---

# Required Component Set

Every production Chronicle Entry should include:

```text
Identity
Event Representation
Temporal Information
Event Type
Historical Context
Provenance
Verification
Version
Publication State
Lifecycle / Status
```

These components represent the conceptual minimum needed for a Chronicle Entry to remain:

* Identifiable
* Understandable
* Temporally grounded
* Classified
* Historically meaningful
* Traceable
* Reviewable
* Version-aware
* Publication-aware
* Institutionally stateful

---

# Conditional Component Set

The following components become Required when applicable:

```text
Source Record References
Relationships
Evidence
Correction History
```

### Source Record References

Required when Source Records support or contextualize the Entry or when an Event-Type Profile requires them.

### Relationships

Required when relevant historical or authoritative relationships exist and are necessary to understand the Entry or satisfy an Event-Type Profile.

### Evidence

Required when Chronicle Verification, Event-Type rules, historical claims, or Corrections depend on evidentiary support.

### Correction History

Required when the Entry has undergone a substantive Correction.

---

# Optional Components

Optional components may be added when historically or operationally useful.

Potential examples may include:

* Public summary
* Supplemental notes
* Interpretive notes
* Archival annotations
* Display metadata
* Discovery metadata
* Supplemental chronology
* Additional contextual references
* Presentation-oriented metadata

These are not yet formal Chronicle components.

They should be introduced only when operational need is demonstrated.

Optional components must not:

* Replace Required components
* Bypass Validation
* Create competing canonical objects
* Override authority boundaries
* Introduce uncontrolled semantics into production records

---

# Authority Within the Entry

A Chronicle Entry may reference records from other Suite systems.

Examples include:

```text
Certifier → Certification Package
Registry  → SREG Registry Entry
Anchor    → Integrity Reference
Beacon    → Discovery Signal / Discovery Metadata
Attestor  → Trust Statement
Navigator → Workflow Definition
Atlas     → Atlas authoritative records
```

Chronicle owns the Chronicle Entry.

The originating Suite system owns the authoritative external object.

Conceptually:

> Reference does not transfer authority.

---

# Event Representation vs. Authority

The Chronicle Entry represents the historical Occurrence.

It does not replace the authoritative object that established the Occurrence.

Example:

```text
Certification Created
        ↓
Certifier creates authoritative Certification Package
        ↓
Chronicle preserves qualifying Occurrence
        ↓
Chronicle Entry references Certification Package
```

Chronicle may describe the historical significance and context of the certification event.

Certifier remains authoritative for the certification determination.

---

# Entry Model and Preservation Eligibility

The Entry Model applies only after an Occurrence has qualified for preservation.

Conceptually:

```text
Occurrence
    ↓
Preservation Eligibility
    ↓
Entry Model
    ↓
Chronicle Entry
```

The Entry Model does not itself decide whether an Occurrence belongs in Chronicle.

That decision belongs to Preservation Eligibility rules.

---

# Entry Model and Event-Type Profiles

The Base Entry Model defines universal logical components.

Event-Type Profiles may specialize that model.

An Event-Type Profile may:

* Add Required components
* Add required fields within a component
* Require specific authoritative references
* Require specific Source Records
* Require Evidence
* Require particular Relationships
* Add Provenance requirements
* Add Verification requirements
* Add Validation rules

An Event-Type Profile may strengthen requirements.

It should not remove the universal Required components of the Entry Model.

---

# Entry Model and Validation

The Entry Model establishes conceptual requirements.

Validation will later determine whether a production record satisfies their formal implementation.

Conceptually:

```text
Conceptual Requirement
        ↓
Schema Requirement
        ↓
Validation Rule
        ↓
Production Conformance
```

The Entry Model itself is not a Validation engine.

---

# Entry Model and Retrospective Preservation

The model must support Entries created after the underlying Occurrence.

Retrospective preservation requires clear separation among:

* Event Date
* Entry Creation Date
* Publication Date
* Version Dates
* Correction Dates

The historical record must preserve when the Occurrence happened, not merely when Chronicle learned about or recorded it.

---

# Entry Model and Corrections

Chronicle preserves Corrections as part of its own historical record.

When a substantive Correction changes an Entry:

```text
Entry Version N
    ↓
Correction Record
    ↓
Entry Version N+1
```

The prior substantive state should remain traceable.

Correction history is therefore Conditional at Entry creation but mandatory once a substantive Correction exists.

---

# Entry Model and Publication

A Chronicle Entry may exist internally before public publication.

The model must therefore distinguish:

* Existence
* Verification
* Validation
* Approval
* Publication
* Preservation

These concepts should not be compressed into one status field.

---

# Entry Model and Lifecycle

Chronicle Entry Lifecycle describes the state of Chronicle's own record.

It does not describe the lifecycle of the external object represented by the Entry.

Example:

```text
Certification Status: Revoked
Chronicle Entry Status: Published / Preserved
```

This distinction prevents Chronicle from inheriting external lifecycle semantics incorrectly.

---

# Entry Model and Historical Continuity

The Entry Model should allow future reviewers to reconstruct:

* What happened
* When it happened
* Why Chronicle preserved it
* Which Event Type applied
* Which authority established the underlying object or state
* Which Sources existed
* Which Evidence was available
* How information entered Chronicle
* Which Relationships existed
* What Verification occurred
* Which Version is being reviewed
* Whether Corrections occurred
* When the Entry became public
* What institutional state the Entry holds

A Chronicle Entry should remain understandable even when surrounding technologies change.

---

# Conceptual Entry Anatomy

The canonical conceptual anatomy can be summarized as:

```text
Chronicle Entry
│
├── Identity [Required]
├── Event Representation [Required]
├── Temporal Information [Required]
├── Event Type [Required]
├── Historical Context [Required]
│
├── Source Record References [Conditional]
├── Relationships [Conditional]
├── Provenance [Required]
├── Evidence [Conditional]
│
├── Verification [Required]
├── Version [Required]
├── Correction History [Conditional]
│
├── Publication State [Required]
└── Lifecycle / Status [Required]
```

Optional extensions may be added only where they provide legitimate historical or operational value.

---

# Entry Model Principle

Every Chronicle Entry should contain enough structure to remain:

* Identifiable
* Historically understandable
* Temporally accurate
* Institutionally bounded
* Traceable
* Evidence-aware
* Provenance-aware
* Reviewable
* Correctable
* Versioned
* Publication-aware
* Preservable

Conceptually:

> The schema defines the fields.  
> The Entry Model defines what the record must mean.

---

## Relationship to Other Chronicle Documentation

The Chronicle Entry Model should remain aligned with:

* Purpose
* Scope
* Definitions
* Entries
* Records
* Sources
* Evidence
* Verification
* Corrections
* Schemas
* Integration
* Historical Preservation
* Trust Model
* FAQ
* Status

The Entry Model becomes the conceptual bridge between the completed Foundation and the formal operational schema work that follows.

---

## Future Development

The Entry Model will inform later Chronicle work including:

* Event Types
* Identifier Architecture
* Controlled Values
* Relationships
* Provenance
* Verification rules
* Lifecycle rules
* Versioning
* Corrections
* Chronicle Base Schema
* Event-Type Profiles
* Validation
* Production Procedure
* First production Chronicle Entry

The model should be revised only when later operational work reveals a genuine architectural requirement.

---

## Status

**Active pre-operational Chronicle Entry Model specification.**

This document defines the conceptual structure of the canonical Chronicle Entry before final schema implementation.

Field names, identifier syntax, Controlled Values, final lifecycle states, Verification states, Publication states, validation rules, and machine-readable schema structures remain intentionally unresolved until their dedicated operational-development steps.
