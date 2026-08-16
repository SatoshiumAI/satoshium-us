# Chronicle Event Type Framework

## Purpose

The Chronicle Event Type Framework defines how Satoshium Chronicle classifies the qualifying Occurrence represented by a Chronicle Entry.

This document establishes:

* Event Type as a classification system
* The relationship between Event Type and the canonical Chronicle Entry
* How Event Types are created
* How Event Types are governed
* How Event-Type Profiles extend the Chronicle Base Schema
* Why Chronicle should avoid prematurely defining every possible future event class
* Certification Event as the first operational Event-Type Profile

The Event Type Framework should remain intentionally narrow during early operational development.

---

## Core Principle

The canonical Chronicle object is the **Chronicle Entry**.

Event Type is not a separate canonical object.

Conceptually:

```text
Occurrence
    ↓
Preservation Eligibility
    ↓
Chronicle Entry
    ↓
Event Type Classification
```

Event Type answers:

> What kind of qualifying Occurrence does this Chronicle Entry represent?

It does not answer:

> What is the canonical record?

The canonical record remains the Chronicle Entry.

---

## Event Type

An Event Type is a governed classification applied to a Chronicle Entry.

It identifies the class of Occurrence represented by the Entry.

Event Type should support:

* Consistent historical classification
* Event-Type Profile selection
* Validation
* Discovery
* Grouping
* Interoperability
* Future machine-readable use
* Historical analysis

Event Type should use a Controlled Value rather than free-form text in production records.

---

## Event Type Is Not a Canonical Object

Chronicle should not create a second canonical object called:

* Chronicle Event
* Historical Event Record
* Event Object
* Event Record

The Occurrence exists independently in history.

The Chronicle Entry preserves it.

Event Type classifies it.

Conceptually:

```text
Occurrence = What happened
Chronicle Entry = Chronicle's preservation record
Event Type = Classification of the Occurrence
```

---

## Event Type Governance

Event Types should be governed deliberately.

They should not emerge through uncontrolled labeling.

A proposed Event Type should move through a governance process such as:

```text
Need Identified
    ↓
Preservation Relevance Confirmed
    ↓
Meaning Defined
    ↓
Overlap Reviewed
    ↓
Controlled Value Approved
    ↓
Event-Type Profile Evaluated
    ↓
Validation Rules Established
    ↓
Production Use
    ↓
Ongoing Maintenance
```

The exact approval process may evolve during Chronicle operational development.

---

## When to Create a New Event Type

A new Event Type should be created only when there is a real operational reason.

Potential justification may include:

* A recurring class of qualifying Occurrence
* A distinct historical meaning
* A distinct authoritative source requirement
* Different Evidence expectations
* Different Provenance requirements
* Different Relationship requirements
* Different Verification requirements
* Different Validation requirements
* A need for consistent public discovery

A new Event Type should not be created merely because a label sounds useful.

---

## Event Type Creation Criteria

A proposed Event Type should satisfy several conditions.

### Clear Meaning

The Event Type should have a concise and understandable definition.

### Distinct Scope

The Event Type should describe a class of Occurrence not already adequately represented by an approved type.

### Preservation Relevance

The class should plausibly contain Occurrences that satisfy Chronicle Preservation Eligibility.

### Operational Need

There should be a current or reasonably foreseeable operational use.

### Validation Value

The classification should enable meaningful rules, discovery, or structure.

### Governance Stability

The Event Type should be broad enough to remain useful but narrow enough to preserve clear meaning.

---

## Avoiding Duplicate Event Types

Chronicle should avoid:

* Synonyms
* Near-duplicates
* Event Types differing only stylistically
* Types better represented as Relationships
* Types better represented through Historical Context
* Types representing external lifecycle states without a historical preservation need
* Types created for one isolated Entry with no broader structural value

Before approving a new Event Type, Chronicle should review existing classifications.

---

## Event Type Naming

Event Type names should be:

* Clear
* Concise
* Institutionally meaningful
* Stable
* Human-readable
* Machine-compatible when converted into Controlled Values

The human-readable name and machine-readable Controlled Value may use different formatting while retaining the same meaning.

Final naming conventions should be established through Controlled Values development.

---

## Event-Type Profile

An Event-Type Profile is a structured specialization of the Chronicle Base Schema.

Conceptually:

```text
Chronicle Base Schema
        +
Event-Type Profile
        =
Specialized Chronicle Entry
```

The Profile does not create a new canonical object.

It adds rules applicable to a particular Event Type or approved group of Event Types.

---

## What an Event-Type Profile May Define

An Event-Type Profile may define:

* Additional Required fields
* Conditional fields
* Required authoritative references
* Required Source Record references
* Required Evidence
* Required Relationships
* Provenance minimums
* Verification requirements
* Validation rules
* Publication prerequisites
* Event-Type-specific Controlled Values

A Profile may strengthen requirements.

It should not remove the universal Required components defined by the Chronicle Entry Model.

---

# First Operational Event-Type Profile

## Certification Event

**Certification Event** is the first operational Event-Type Profile for Satoshium Chronicle.

It represents qualifying historical Occurrences associated with the lifecycle of a Certifier Certification Package.

The authoritative relationship is:

```text
Certifier
    ↓
Certification Package
    ↓
Qualifying Certification Occurrence
    ↓
Chronicle Entry
    ↓
Certification Event-Type Profile
```

Certifier remains authoritative for:

* Certification evaluation
* Certification determination
* Certification Package
* Certification lifecycle
* Certification status

Chronicle remains authoritative for:

* Chronicle Entry identity
* Chronicle historical representation
* Chronicle Provenance
* Chronicle Relationships
* Chronicle Verification
* Chronicle Validation
* Chronicle Corrections
* Chronicle Versions
* Chronicle publication state
* Chronicle preservation state

Reference does not transfer authority.

---

## Initial Certification Event Types

The first operational category should remain narrow.

Potential initial Certification Event classifications may include:

```text
Certification Created
Certification Renewed
Certification Suspended
Certification Revoked
Certification Expired
```

These are working operational concepts until formally approved through Controlled Values.

Additional certification Event Types should be introduced only when real certification history requires them.

---

## Certification Created

Represents a qualifying historical Occurrence in which Certifier creates or issues a certification.

Chronicle should preserve the historical Occurrence only when Preservation Eligibility is satisfied.

The Chronicle Entry should reference the authoritative Certification Package.

---

## Certification Renewed

Represents a qualifying renewal or continuation milestone within the certification lifecycle.

Not every administrative renewal must necessarily become a Chronicle Entry.

Preservation Eligibility still applies.

---

## Certification Suspended

Represents a qualifying suspension Occurrence.

Certifier remains authoritative for the suspension decision and certification state.

Chronicle preserves the historical significance of the suspension when eligible.

---

## Certification Revoked

Represents a qualifying revocation Occurrence.

The Chronicle Entry should not independently declare that certification revoked.

It should reference the authoritative Certifier record establishing the revocation.

---

## Certification Expired

Represents a qualifying expiration Occurrence.

Expiration may be preserved when the event has historical value under Chronicle rules.

Routine expiration without historical significance may not require preservation.

---

# Initial Event Type Categories

Chronicle should define only the minimum categories needed for operational use.

At the beginning of Phase III:

```text
Operational Event-Type Category:
Certification Event
```

This does not imply that Certification Event will remain the only category.

It means Chronicle should avoid defining future categories without actual operational evidence.

---

## Future Categories

Future Chronicle operations may eventually justify classifications associated with:

* Registry
* Anchor
* Beacon
* Attestor
* Navigator
* Atlas
* Governance
* Public releases
* Institutional milestones
* Architectural transitions
* Other historically significant Suite developments

These should remain undeclared or provisional until an actual use case requires them.

---

## Why Chronicle Should Start Narrow

Premature taxonomy design creates several risks:

* Duplicate Event Types
* Unclear boundaries
* Unused classifications
* Inconsistent future records
* Validation complexity
* Migration burden
* Semantic drift
* Overlap with Relationships
* Overlap with Historical Context
* Overlap with external system lifecycle states

Chronicle should expand its Event Type vocabulary from production experience.

Conceptually:

> Start narrow. Govern carefully. Expand from operational evidence.

---

# Event Type and Preservation Eligibility

Event Type and Preservation Eligibility are distinct.

### Event Type

Answers:

> What kind of Occurrence is this?

### Preservation Eligibility

Answers:

> Should Chronicle preserve this Occurrence?

An Occurrence may match an approved Event Type and still fail Preservation Eligibility.

For example:

A routine certification lifecycle action may technically fit a certification classification but may not be historically significant enough to preserve.

Conversely, an unusual Occurrence may initially lack a mature Event Type and still be historically important enough to justify later classification work.

---

## Event Type as an Eligibility Path

An approved Event Type may provide one recognized path toward Preservation Eligibility.

Chronicle may establish rules where:

```text
Approved Event Type
        +
Required Preservation Conditions
        =
Preservation Eligible
```

The exact rules remain to be established during operational development.

Event Type alone should not automatically guarantee preservation unless Chronicle explicitly approves such a rule.

---

# Event Type and Historical Significance

Event Type classifies.

Historical Significance explains importance.

Two Entries may share the same Event Type but have very different historical significance.

Example:

```text
Entry A:
Event Type → Certification Created
Historical Context → First Satoshium certification

Entry B:
Event Type → Certification Created
Historical Context → Routine later certification
```

The same classification does not imply equal historical importance.

---

# Event Type and Historical Context

Historical Context should not be encoded entirely into Event Type names.

Chronicle should avoid classifications such as:

```text
First Important Certification Created During Major Expansion
```

when the correct architecture is:

```text
Event Type → Certification Created
Historical Context → First certification during major expansion
Historical Significance → First / Institutional Milestone
```

This keeps Event Types reusable and stable.

---

# Event Type and Relationships

Relationships and Event Types serve different functions.

### Event Type

Classifies the Occurrence.

### Relationship

Describes how records or objects connect.

Examples:

```text
Event Type:
Certification Created

Relationships:
References Certification Package
Registered As SREG Registry Entry
Precedes Later Certification Renewal
Related To Chronicle Entry X
```

Relationships should not become Event Types.

---

# Event Type and External Lifecycle States

External Suite systems may have their own lifecycle states.

Chronicle should not automatically copy those states into its Event Type vocabulary.

A lifecycle state becomes historically meaningful to Chronicle only when it represents a qualifying Occurrence.

Example:

```text
External state:
Certification Status = Revoked

Historical Occurrence:
Certification Revoked

Chronicle Event Type:
Certification Revoked
```

The historical classification and operational external state remain separate concepts.

---

# Event Type and the Chronicle Entry Model

Event Type is one Required logical component of every Chronicle Entry.

The Entry Model requires:

```text
Event Type [Required]
```

The specific Controlled Value should identify the approved classification.

The Event-Type Profile selected by that classification may then strengthen other Entry requirements.

---

# Event Type and the Chronicle Base Schema

The Base Schema should contain a universal Event Type field or structure.

The schema should not hard-code every Event-Type-specific requirement into the universal Base Schema.

Instead:

```text
Base Schema
    ↓
Event Type
    ↓
Applicable Event-Type Profile
    ↓
Additional Requirements
```

This allows Chronicle to expand classification without destabilizing the universal Entry structure.

---

# Event Type and Validation

Validation should eventually confirm:

* Event Type is present
* Event Type is an approved Controlled Value
* The correct Event-Type Profile is applied
* Profile-specific Required fields are present
* Required authoritative references exist
* Required Relationships exist
* Required Evidence or Provenance rules are satisfied
* Deprecated Event Types are handled correctly

These rules remain to be finalized during Chronicle Validation development.

---

# Event Type Change Control

Event Types may evolve.

Potential governance actions include:

* Add
* Rename
* Clarify
* Deprecate
* Replace
* Split
* Merge

Changes should preserve historical interpretability.

Production Entries should retain the Event Type and schema context under which they were created unless a formal migration is approved.

---

## Deprecation

Deprecated Event Types should not simply disappear.

Chronicle should preserve:

* Original value
* Deprecation reason
* Replacement value where applicable
* Effective date
* Compatibility guidance
* Migration guidance where required

Historical records must remain understandable.

---

# Event Type Versioning

Event Type definitions or vocabularies may require versioning.

Vocabulary versioning is distinct from:

* Chronicle Entry Version
* Schema Version
* Event-Type Profile Version

These concepts should remain separately identifiable where operationally necessary.

---

# Discovery

Event Type should support future historical discovery.

Potential discovery uses include:

* Filter Entries by Event Type
* Browse certification history
* Compare similar lifecycle Occurrences
* Build Timeline groupings
* Generate machine-readable historical indexes

Discovery should consume Event Type.

Discovery should not define Event Type.

---

# Governance Principle

The Event Type Framework should remain conservative.

Chronicle should not attempt to anticipate every possible Satoshium Event Type.

Instead:

1. Encounter a real preservation need.
2. Determine whether existing Event Types are sufficient.
3. Define a new Event Type only if necessary.
4. Govern it as a Controlled Value.
5. Create an Event-Type Profile only if specialized structure is required.
6. Validate its use in production.
7. Expand only from operational evidence.

---

# Event Type Framework Summary

The conceptual model is:

```text
Chronicle Entry
│
├── Event Type [Required]
│      ↓
│   Controlled Value
│      ↓
│   Event-Type Profile when applicable
│
├── Historical Context
├── Authoritative References
├── Sources / Evidence / Provenance
├── Relationships
├── Verification
├── Validation
└── Preservation
```

Event Type classifies the Chronicle Entry.

It does not replace it.

---

## Framework Principle

> Event Type classifies the history.  
> Chronicle Entry preserves it.

And operationally:

> Start narrow. Govern carefully. Expand from operational evidence.

---

## Relationship to Other Chronicle Documentation

The Event Type Framework should remain aligned with:

* Purpose
* Scope
* Definitions
* Entries
* Entry Model
* Records
* Schemas
* Integration
* Historical Preservation
* Certification Events
* Trust Model
* Status

The framework establishes the classification layer that will later feed Controlled Values, Event-Type Profiles, Validation, production procedures, and public discovery.

---

## Next Operational Dependencies

The Event Type Framework informs later work on:

* Identifier Architecture
* Controlled Values
* Relationships
* Provenance
* Lifecycle
* Chronicle Base Schema
* Certification Event-Type Profile
* Validation
* Production Procedure
* First production Chronicle Entry

The full Certification Event-Type Profile should be formalized after the necessary underlying identifier, controlled-value, relationship, and provenance architecture is sufficiently settled.

---

## Status

**Active pre-operational Event Type Framework specification.**

Certification Event is established as the first operational Event-Type Profile direction.

The final Event Type Controlled Values, profile schema, identifier rules, validation rules, lifecycle semantics, and future Event Type categories remain intentionally limited or unresolved until their dedicated operational-development steps.
