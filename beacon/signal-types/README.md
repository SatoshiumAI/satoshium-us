# Satoshium Beacon — Discovery Signal Types

## Overview

The **Discovery Signal Types** architecture defines the governed classification model used to describe what kind of discovery a Beacon-owned **Discovery Signal** represents.

This is the second component of:

```text
Beacon Phase II — Production Architecture
```

The Discovery Signal Entry Model established:

```text
Signal Type
```

as a structural component of the canonical Beacon object.

This architecture establishes the initial classifications that may occupy that component.

---

## Purpose

Signal Type exists to classify the nature of a discovery.

It does not determine the authority of the underlying information.

The core distinction is:

```text
Signal Type
→ what kind of discovery Beacon is recording

Source Object Type
→ what the referenced source object is

Source Status
→ authoritative state maintained by the source institution
```

These concepts may be related.

They are not interchangeable.

---

## Institutional Context

Beacon remains the Satoshium Suite institution for:

```text
Discovery & Signals
```

Its canonical responsibility is:

```text
Discovery Signal / Metadata
```

The current Suite institutional model remains:

```text
Atlas
→ Authoritative Intelligence

Navigator
→ Workflow Definition / Orchestration

Beacon
→ Discovery Signal / Metadata

Certifier
→ Certification Package

Registry
→ SREG

Chronicle
→ Chronicle Entry

Anchor
→ Integrity Reference

Attestor
→ Trust Statement
```

Beacon may classify discoveries associated with these institutions without acquiring their authority.

> **Reference does not transfer authority.**

---

## Initial Signal-Type Architecture

Phase I established several recurring discovery categories.

Phase II carries forward the following initial architectural classification set:

```text
Information
Jurisdiction
Certification
Registry
Historical
Integrity
Trust
Relationship
```

These eight classifications define Beacon's initial architectural vocabulary.

Their final machine-readable enum values, schema constraints, validation behavior, extensibility rules, and production requirements remain subject to later Phase II work.

---

## 1. Information Signal

An **Information Signal** identifies information whose discovery is relevant enough to preserve as a Beacon Discovery Signal but whose primary discovery meaning is not better represented by a more specialized governed type.

Potential uses include:

```text
general information discovery
relevant update
relevant observation
attributable external information
attributable internal information
```

An Information Signal must still preserve:

```text
source
provenance
discovery context
authority boundary
```

Information should not become an uncontrolled catch-all category.

Where a more precise governed Signal Type applies, that type should be preferred.

---

## 2. Jurisdiction Signal

A **Jurisdiction Signal** identifies discovery associated with:

```text
a jurisdiction
jurisdictional conditions
jurisdiction-related intelligence
jurisdiction-relevant external information
```

A Jurisdiction Signal may reference:

```text
Atlas Authoritative Intelligence
```

or attributable external sources.

Beacon may signal jurisdiction relevance.

Atlas remains authoritative for Atlas-owned intelligence.

```text
Jurisdiction Signal
≠
Atlas Authoritative Intelligence
```

---

## 3. Certification Signal

A **Certification Signal** identifies certification-related information observed from an authoritative source.

It may reference:

```text
Certification Package
related SREG
certification evidence reference
certification status
certification-related change
```

Certification Signals may use the specialized architecture documented at:

```text
/beacon/certification-signals/
```

The institutional boundary remains:

```text
Certifier
→ owns certification authority
→ owns Certification Packages

Beacon
→ owns Discovery Signals
→ owns Discovery Metadata
```

Therefore:

```text
Certification Signal
≠
Certification Package
```

---

## 4. Registry Signal

A **Registry Signal** identifies discovery associated with Registry-owned records, registration activity, catalog state, or other relevant Registry information.

It may reference:

```text
SREG
registration state
Registry lifecycle information
Registry relationships
```

Beacon may signal Registry information.

Registry remains authoritative for:

```text
SREG
```

A Registry Signal does not:

```text
register an object
alter registration
replace an SREG
transfer Registry authority
```

---

## 5. Historical Signal

A **Historical Signal** identifies discovery associated with historically preserved material or a relevant Chronicle Entry.

It may:

```text
reference a Chronicle Entry
identify historical relevance
connect discovery to a preserved Occurrence
surface historical context
```

A Historical Signal does not determine:

```text
Preservation Eligibility
historical authority
Chronicle lifecycle
Chronicle publication
```

Chronicle remains responsible for historical preservation.

```text
Historical Signal
≠
Chronicle Entry
```

---

## 6. Integrity Signal

An **Integrity Signal** identifies discovery associated with integrity information or an Anchor-owned Integrity Reference.

It may:

```text
reference an Integrity Reference
surface integrity-related context
surface relevant verification information
identify an integrity-related discovery
```

Beacon does not perform Anchor Verification merely by publishing an Integrity Signal.

Anchor remains responsible for:

```text
Integrity Reference
integrity-preservation process
Anchor Verification
```

Therefore:

```text
Integrity Signal
≠
Integrity Reference
```

---

## 7. Trust Signal

A **Trust Signal** identifies discovery associated with trust-related information or an Attestor-owned Trust Statement.

It may:

```text
reference a Trust Statement
surface trust-related context
identify a trust-related observation
identify a trust-related change
```

A Trust Signal does not itself constitute:

```text
trust assessment
Trust Statement
Attestor authority
```

The governing distinction is:

```text
Beacon
→ Trust Signal

Attestor
→ Trust Statement
```

Therefore:

```text
Trust Signal
≠
Trust Statement
```

---

## 8. Relationship Signal

A **Relationship Signal** identifies a meaningful discovered relationship between governed objects, institutions, sources, subjects, or other entities.

It should preserve:

```text
relationship endpoints
relationship provenance
discovery context
supporting source
```

A Relationship Signal may connect:

```text
Suite objects
Suite institutions
external references
subjects
other Discovery Signals
```

Beacon should not manufacture a relationship merely because two objects appear related.

The relationship basis should be:

```text
attributable
traceable
reviewable
```

---

## Signal Type vs. Source Object Type

Signal Type must remain distinct from Source Object Type.

For example:

```text
Source Object
→ ANCH-2026-0001
→ Integrity Reference
```

may support:

```text
Integrity Signal
```

when the discovery concerns integrity information.

The same source object might instead participate in:

```text
Relationship Signal
```

when the discovery concerns its governed relationship to another object.

Therefore:

```text
Source Object Type
does not automatically determine
Discovery Signal Type
```

The Signal Type should describe the primary discovery meaning being preserved by Beacon.

---

## Specialized Signal Profiles

A general Signal Type may support a specialized profile when additional controlled semantics are required.

The first established example is:

```text
Certification Signal
        ↓
/beacon/certification-signals/
```

A specialized profile may refine:

```text
metadata
permitted values
required references
interpretation rules
validation requirements
```

without changing the institutional ownership of the Discovery Signal.

The object remains:

```text
Beacon-owned Discovery Signal
```

---

## Multiple Relevant Classifications

A discovery may appear relevant to more than one Signal Type.

The current architectural preference is:

```text
one primary governed Signal Type
```

The primary type should express the signal's principal discovery meaning.

Secondary context should normally be preserved through:

```text
canonical references
Discovery Metadata
relationships
source information
```

rather than uncontrolled multi-classification.

Whether production will permit formal secondary classifications remains intentionally unfrozen.

That decision should be made only if later schema, validation, or production work demonstrates a need.

---

## Type Assignment Requirements

A Signal Type should eventually be assignable only when sufficient evidence and context support the classification.

Expected principles include:

```text
Type must come from governed vocabulary.

Source must be attributable.

Classification must match discovery context.

Specialized profiles must satisfy their own requirements.

Type must not imply unsupported authority.
```

The exact validation rules remain pending until:

```text
/beacon/validation/
```

---

## What Signal Type Does Not Establish

A Discovery Signal classification does not independently establish:

```text
truth
certification
registration
historical significance
integrity verification
trust
source authority
publication eligibility
```

Signal Type classifies Beacon's discovery object.

Other Suite institutions retain their own canonical responsibilities.

Later Beacon processes determine whether a Discovery Signal itself satisfies production and publication requirements.

---

## Controlled Vocabulary Posture

The eight initial architectural types are:

```text
Information
Jurisdiction
Certification
Registry
Historical
Integrity
Trust
Relationship
```

Current posture:

```text
Architectural Types
→ established

Machine-Readable Enum Values
→ not yet frozen

Aliases
→ not yet frozen

Extensibility Rules
→ not yet frozen

Schema Enforcement
→ pending

Validation Enforcement
→ pending

Production Proof
→ pending
```

This preserves the distinction between:

```text
architectural classification
```

and:

```text
production-controlled vocabulary
```

---

## Extensibility Principle

The initial eight Signal Types should not be treated as an invitation to add categories whenever a new discovery appears.

A new Signal Type should be considered only when existing types cannot accurately represent a recurring and institutionally meaningful discovery class.

The preferred sequence is:

```text
new discovery need
        ↓
evaluate existing types
        ↓
use metadata / relationships if sufficient
        ↓
identify genuine classification gap
        ↓
govern new type explicitly
```

This helps prevent uncontrolled vocabulary growth.

---

## Authority Boundary

A Signal Type describes Beacon's Discovery Signal.

It does not transfer source authority.

The following distinctions remain explicit:

```text
Certification Signal
≠
Certification Package

Registry Signal
≠
SREG

Historical Signal
≠
Chronicle Entry

Integrity Signal
≠
Integrity Reference

Trust Signal
≠
Trust Statement
```

Likewise:

```text
Jurisdiction Signal
≠
Atlas Authoritative Intelligence
```

The governing rule remains:

> **Reference does not transfer authority.**

---

## Relationship to the Entry Model

The Discovery Signal Entry Model established:

```text
Identity
        ↓
Subject
        ↓
Signal Type
        ↓
Source
        ↓
Provenance
        ↓
Canonical References
        ↓
Discovery Metadata
        ↓
Timestamps
        ↓
Version
        ↓
Status
        ↓
Relationships
```

This architecture now defines the initial meaning of:

```text
Signal Type
```

within that model.

Later Phase II work may refine the controlled implementation without silently changing the institutional meaning established here.

---

## Relationship to Discovery Metadata

Signal Type provides the primary classification.

Discovery Metadata preserves additional context.

Conceptually:

```text
Signal Type
→ primary discovery classification

Discovery Metadata
→ supporting context, filtering, interpretation, and traceability
```

Metadata should not be used to create uncontrolled substitute Signal Types.

Likewise, Signal Type should not be overloaded with information that belongs in metadata.

---

## Relationship to Validation

Later Validation architecture should determine whether:

```text
the Signal Type is permitted
the classification is structurally valid
required source information exists
required provenance exists
specialized profile requirements are satisfied
the type conflicts with other signal attributes
```

This page defines the classification architecture.

It does not yet define those validation rules.

---

## Current Status

As of September 5, 2026:

```text
Institution → Beacon
Suite Role → Discovery & Signals
Canonical Responsibility → Discovery Signal / Metadata
Status → Continuing Development
Phase → Phase II — Production Architecture

Discovery Signal Entry Model → Defined
Discovery Signal Types → Defined

Initial Architectural Types → 8
Machine-Readable Vocabulary → Not yet frozen
Schema Enforcement → Pending
Validation Enforcement → Pending
Production Proof → Pending
First Production Discovery Signal → Not yet created
Operational → No
```

---

## Phase II Progress

```text
1. Discovery Signal Entry Model
   → COMPLETE

2. Discovery Signal Types
   → COMPLETE

3. Discovery Signal Lifecycle
   → NEXT

4. Beacon Identifier Standard

5. Beacon Schemas

6. Validation

7. Discovery Provenance

8. Authority & Reference Model

9. Relationship Model

10. Versioning & Supersession

11. Publication Model

12. Discovery Signals Register

13. Individual Discovery Signal

14. Beacon Discovery Methodology

15. Production Model / First Operation
```

---

## Governing Principles

Discovery Signal Types follow these principles:

```text
Classify the discovery, not the authority.

Prefer precise governed types.

Do not use Information as an uncontrolled catch-all.

Preserve source identity.

Preserve provenance.

Use metadata and relationships for secondary context.

Add new types only when a genuine classification gap is proven.

Do not let classification manufacture institutional meaning.
```

Above all:

> **Reference does not transfer authority.**

---

## Next Phase II Step

The next production-architecture page is:

```text
/beacon/lifecycle/
```

Its purpose is to define how a Beacon Discovery Signal moves through governed institutional states over time.

---

## Last Updated

September 5, 2026
