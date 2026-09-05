# Discovery Metadata

## Purpose

Discovery Metadata is Beacon-owned structured information used to help users, applications, and workflows locate, organize, filter, interpret, and trace discoverable information.

It provides context for discovery without replacing the source or canonical object being referenced.

Beacon owns its Discovery Signals and discovery metadata.

The originating institution retains authority for its canonical objects.

**Reference does not transfer authority.**

---

## Institutional Role

Beacon is the Satoshium Suite institution for **Discovery & Signals**.

Discovery Metadata supports that responsibility by describing:

* What was discovered
* What kind of information it is
* Where it came from
* Which institution or external source provided it
* Which canonical object it references
* Why it may be relevant
* How it relates to other information
* When it was discovered or last observed
* Which authority boundary applies

Metadata improves discovery while preserving provenance, traceability, context, and institutional ownership.

---

## What Discovery Metadata Is

Discovery Metadata is structured descriptive information associated with Beacon discovery.

It may describe:

* Discovery Signals
* Sources
* Canonical-object references
* Relationships
* Discovery results
* Index entries
* Workflow context
* External information

Discovery Metadata helps users and systems understand discovered information before or while navigating to its authoritative source.

---

## What Discovery Metadata Is Not

Discovery Metadata is not automatically:

* Authoritative Intelligence
* A Certification Package
* An SREG record
* A Chronicle Entry
* An Integrity Reference
* A Trust Statement
* A certification decision
* A verification conclusion
* A trust determination

Metadata may reference these objects.

It does not replace them.

---

## Canonical Suite Model

Discovery Metadata operates within the current Satoshium Suite institutional model:

* **Atlas → Authoritative Intelligence**
* **Navigator → Workflow Definition / Orchestration**
* **Beacon → Discovery Signal / Metadata**
* **Certifier → Certification Package**
* **Registry → SREG**
* **Chronicle → Chronicle Entry**
* **Anchor → Integrity Reference**
* **Attestor → Trust Statement**

Each institution retains authority over its own canonical responsibilities and objects.

---

## Conceptual Metadata Fields

Beacon Discovery Metadata may include fields such as:

* Discovery Identifier
* Signal Type
* Subject
* Source Institution
* External Source
* Canonical Object Type
* Canonical Object Identifier
* Related Certification Package
* Related SREG
* Related Chronicle Entry
* Related Integrity Reference
* Related Trust Statement
* Provenance
* Discovery Context
* Relevant Status
* Classification
* Jurisdiction
* Relationships
* Public Reference
* Publication Date
* Discovery Date
* Last Observed
* Version
* Supersession Information

These fields are conceptual and may be refined through future operational schemas.

---

## Discovery Identifier

A Discovery Identifier provides a stable reference for a Beacon discovery object or metadata context.

Stable identifiers improve:

* Traceability
* Cross-reference integrity
* Machine readability
* Version tracking
* Interoperability
* Long-term accessibility

Operational identifier conventions may be defined as Beacon advances toward production.

---

## Source Institution

Discovery Metadata should identify the originating Suite institution whenever a canonical Suite object is referenced.

Examples include:

* Atlas
* Certifier
* Registry
* Chronicle
* Anchor
* Attestor

Navigator may also provide workflow context when discovery occurs within a Navigator-defined process.

The source institution field helps preserve institutional authority.

---

## Canonical Object References

Beacon may preserve references to canonical Suite objects such as:

* Atlas Authoritative Intelligence
* Certifier Certification Packages
* Registry SREG records
* Chronicle Entries
* Anchor Integrity References
* Attestor Trust Statements

Where available, the canonical identifier should be preserved.

Beacon should point to the authoritative object rather than silently reproducing it as a competing object.

---

## Provenance

Provenance records where discovered information originated and how it entered the Beacon discovery context.

Useful provenance may include:

* Source institution
* External provider
* Canonical identifier
* Public reference
* Discovery method
* Observation time
* Related workflow
* Prior version or superseded reference

Provenance supports reviewability and traceability.

---

## Discovery Context

Discovery Context explains why information was surfaced.

Context may include:

* User query
* Research objective
* Investigation
* Navigator-defined workflow
* Signal relationship
* Jurisdiction
* Subject
* Classification
* Event or change
* Related canonical object

Context helps distinguish relevance from authority.

---

## Status Metadata

Beacon may preserve relevant status information observed from an authoritative source.

For example, a Discovery Signal may reference an authoritative certification status maintained by Certifier.

Beacon may record the observed status as discovery metadata.

It does not independently create or redefine that status.

---

## Relationships

Discovery Metadata may preserve relationships among:

* Discovery Signals
* Atlas intelligence
* Certification Packages
* SREG records
* Chronicle Entries
* Integrity References
* Trust Statements
* Sources
* Navigator workflow context
* External information

Relationships improve navigation and interoperability while preserving institutional separation.

---

## Filtering

Discovery Metadata may support filtering by attributes such as:

* Status
* Jurisdiction
* Institution
* Canonical object type
* Classification
* Source
* Date
* Category
* Signal type
* Relationship
* Version

Filtering changes how information is discovered or presented.

It does not change the underlying canonical object.

---

## Classification

Classification metadata helps organize discovered information into meaningful categories.

Classification should describe the discovery context without altering the source information or transferring authority to Beacon.

Controlled vocabularies and canonical terminology may be defined as Beacon metadata schemas mature.

---

## Machine Discovery

Structured Discovery Metadata may support future:

* Machine-readable discovery
* Federated search
* Beacon indexes
* APIs
* Metadata feeds
* Intelligent assistants
* Relationship discovery
* Notification services
* Navigator workflow interfaces
* Cross-institution discovery

Machine discovery should preserve the same provenance and authority boundaries required for human-facing discovery.

---

## Relationship to Navigator

Navigator owns **Workflow Definition / Orchestration**.

A Navigator-defined workflow may supply discovery context to Beacon.

Beacon may preserve appropriate workflow context within its Discovery Metadata while retaining ownership of its Discovery Signals and metadata.

Navigator orchestrates.

Beacon discovers, signals, and describes.

---

## External Sources

Beacon may create Discovery Metadata for attributable external information.

External metadata may preserve:

* Source identity
* Provider
* Public reference
* Provenance
* Publication date
* Discovery date
* Context
* Relationships
* Last observed information

Discovery does not make an external source a Satoshium Suite institution.

Metadata does not convert external information into a Suite-authoritative canonical object.

---

## Metadata Authority Boundary

Discovery Metadata is a Beacon-owned object layer.

It may describe or reference information maintained elsewhere, but it does not become the authoritative canonical object and does not transfer that object's authority to Beacon.

```text
Beacon owns the discovery metadata.
The originating institution owns its canonical object.
The external source remains external.
```

**Reference does not transfer authority.**

---

## Versioning and Supersession

Discovery Metadata may change as Beacon observes new information.

Future operational models should support appropriate mechanisms for:

* Version identification
* Update timestamps
* Last-observed timestamps
* Supersession
* Corrections
* Relationship changes
* Source changes

Updates to Beacon metadata should not rewrite the lifecycle of a referenced canonical object.

---

## Interoperability Principles

### Attribution

The source of discovered information should remain identifiable.

### Provenance

Origin and discovery context should be preserved.

### Traceability

Users and systems should be able to navigate back to referenced sources and canonical objects.

### Stable References

Canonical identifiers should be preserved whenever available.

### Canonical Terminology

Metadata should use Suite-defined terms consistently.

### Portability

Structured metadata should support use across interfaces and systems.

### Version Awareness

Changes to discovery metadata should remain reviewable.

### Authority Preservation

Metadata does not acquire the authority of the object it describes.

---

## Discovery Flow

A generalized metadata flow may be represented as:

```text
Workflow / Query
      ↓
Beacon Discovery
      ↓
Discovery Signal / Metadata
      ↓
Referenced Source or Canonical Object
      ↓
Review / Navigation / Continued Workflow
```

This is an interoperability model rather than a mandatory linear sequence for every discovery action.

---

## Discovery Philosophy

Discovery becomes more useful and reviewable when metadata remains:

* Clear
* Stable
* Attributable
* Traceable
* Portable
* Version-aware
* Interoperable

Beacon helps users and workflows discover information.

Discovery Metadata preserves enough context to understand what was discovered, where it came from, how it relates to other objects, and where authority remains.

```text
Discovery Signals identify relevance.
Metadata preserves context and relationships.
Canonical objects preserve institutional authority.
```

**Reference does not transfer authority.**

---

## Future Metadata Architecture

Future Beacon development may define:

* Canonical Discovery Metadata schemas
* Required and optional metadata fields
* Validation rules
* Shared reference conventions
* Controlled vocabularies
* Semantic relationships
* Machine-readable discovery feeds
* APIs
* Indexing conventions
* Versioning rules
* Supersession behavior
* Navigator workflow interfaces
* Cross-institution metadata exchange

These mechanisms should remain aligned with Satoshium Suite Standards, Methodology, Interoperability, and canonical terminology.

---

## Status

Beacon Discovery Metadata architecture is undergoing Suite alignment and production preparation ahead of its originally planned November 2026 development window.

This document establishes the governing conceptual model for Discovery Metadata. Operational schemas, validation rules, identifiers, required fields, exchange formats, versioning behavior, and workflow interfaces may continue to evolve.

Beacon should not be considered operational solely because its Discovery Metadata architecture or documentation is complete. Operational status requires the architecture to be proven through actual institutional use.
