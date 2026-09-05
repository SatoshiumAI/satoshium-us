# Signals

## Purpose

Discovery Signals are Beacon-owned objects that document observations, events, changes, indicators, updates, relationships, or other information identified through discovery and considered relevant for attention.

Beacon publishes Discovery Signals and related discovery metadata while preserving source visibility, attribution, provenance, traceability, stable references, context, and institutional authority.

A Discovery Signal may point to an authoritative Suite object or an external source.

The signal belongs to Beacon.

The referenced object remains under the authority of its originating institution or source.

**Reference does not transfer authority.**

---

## What Is a Discovery Signal?

A Discovery Signal is a Beacon-owned discovery object indicating that information may be relevant.

Signals may emerge from:

* Authoritative Atlas intelligence
* Certification Packages
* SREG records
* Chronicle Entries
* Integrity References
* Trust Statements
* Publications and research
* Government and public sources
* External information environments
* Emerging developments and relationships

A Discovery Signal is not a conclusion.

It identifies information that may deserve review, investigation, or follow-up.

---

## Why Signals Matter

Modern information environments contain more information than any individual or workflow can reasonably process.

Not all information is equally relevant.

Discovery Signals provide a structured mechanism for directing attention toward information that may matter while maintaining a traceable connection to its source.

---

## Signal Philosophy

A Discovery Signal is not certification.

A Discovery Signal is not registration.

A Discovery Signal is not historical authority.

A Discovery Signal is not an Integrity Reference.

A Discovery Signal is not a Trust Statement.

A Discovery Signal does not inherit the authority of the object it references.

It indicates that information may be relevant.

Beacon seeks to improve visibility, not impose conclusions.

---

## Types of Discovery Signals

### Information Signals

New or updated information that may be relevant.

Examples:

* Publications
* Reports
* Research
* Announcements
* External-source updates

---

### Jurisdiction Signals

Developments associated with jurisdictions or authoritative Atlas intelligence.

Examples:

* Regulatory changes
* Policy updates
* Legislative activity
* Economic developments

---

### Certification Signals

Discovery Signals associated with Certification Packages or certification status maintained by Certifier.

Examples may include discovery of:

* Certified status
* Updated certification information
* Expired certification status
* Revoked certification status
* Pending certification information

Certifier remains authoritative for certification status.

Beacon may signal the status but does not determine it.

---

### Registry Signals

Discovery Signals associated with SREG records.

Examples:

* Record creation
* Record modification
* Record correction
* Lifecycle changes
* Relationship activity

Registry remains authoritative for the SREG record and its lifecycle state.

---

### Historical Signals

Discovery Signals associated with Chronicle Entries or relevant historical context.

Examples:

* New Chronicle Entries
* Historical milestones
* Source updates
* Evidence-related developments
* Relationships to preserved Occurrences

Chronicle remains authoritative for its historical record.

---

### Integrity Signals

Discovery Signals associated with Anchor Integrity References or integrity-related relationships.

Examples:

* Discovery of an Integrity Reference
* Anchoring relationships
* Integrity-reference updates
* Related integrity evidence or metadata

Anchor remains authoritative for its Integrity References.

---

### Trust Signals

Discovery Signals associated with Attestor Trust Statements or trust-related context.

Examples:

* Discovery of a Trust Statement
* Attestation context
* Supporting references
* Trust-statement updates

Attestor remains authoritative for its Trust Statements.

Beacon does not determine trust by surfacing them.

---

### Relationship Signals

Connections identified between sources, Discovery Signals, or canonical objects.

Examples:

* Shared sources
* Cross-institution references
* Historical relationships
* Jurisdiction relationships
* Canonical-object relationships

Relationship discovery should preserve the identifiers, provenance, and authority of the referenced objects.

---

## Signal Lifecycle

Discovery Signals may move through several stages.

### Identification

Potentially relevant information becomes visible.

### Discovery Signal

Beacon represents the discovery as a Discovery Signal with appropriate metadata and source references.

### Review

A user, workflow, or relevant Suite institution may review the signal and its referenced information.

### Follow-Up

The signal may lead to additional discovery, investigation, certification review, registration activity, historical review, integrity review, trust review, or other appropriate action.

### Supersession or Resolution

A signal may be superseded, resolved, archived, or linked to later information.

Its lifecycle should preserve provenance and historical traceability.

---

## Signal Sources

Discovery Signals may reference information originating from:

* Atlas
* Certifier
* Registry
* Chronicle
* Anchor
* Attestor
* Navigator-directed workflows
* Public sources
* Research sources
* Government sources
* Other external information environments

External discovery does not convert an external source into a Suite institution or a Suite-authoritative object.

---

## Signal Attributes

Discovery Signals may include or reference attributes such as:

* Discovery identifier
* Signal type
* Subject
* Source institution or external source
* Canonical object identifier
* Provenance
* Discovery context
* Relevant status
* Relationships
* Discovery time
* Source time
* Version or supersession information

Specific schema requirements may be refined as Beacon advances toward production.

---

## Signal Prioritization

Not all Discovery Signals require equal attention.

Beacon implementations may support:

* Signal ranking
* Signal grouping
* Signal filtering
* Signal categorization
* Signal monitoring

Prioritization should assist discovery without converting relevance into truth, certification, integrity, or trust authority.

---

## Relationship to Discovery

Discovery is the process through which Beacon identifies potentially relevant information.

Discovery Signals are a primary Beacon-owned output of that process.

A simplified flow may be represented as:

```text
Workflow / Query
      ↓
   Discovery
      ↓
Discovery Signal / Metadata
      ↓
Referenced Source or Canonical Object
```

Navigator may define or orchestrate a workflow requiring discovery.

Beacon performs discovery and publishes the corresponding signal or metadata.

---

## Relationship to Sources

Discovery Signals should remain connected to their sources.

Users and systems should be able to determine:

* Where the information originated
* Which institution or external source maintains it
* Which canonical identifier applies, when available
* How the signal was identified
* What discovery context was preserved
* How the source may be reviewed

Source visibility, attribution, provenance, and traceability are core Beacon principles.

---

## Relationship to Results

Discovery Signals may contribute to Beacon results.

Multiple signals may appear within a single result.

A single signal may contribute to multiple results or workflows.

A result does not replace the Discovery Signal or the authoritative source it references.

---

## Institutional Authority Boundary

Beacon owns the Discovery Signals and discovery metadata it publishes.

Other Suite institutions retain authority over their canonical objects:

* **Atlas → Authoritative Intelligence**
* **Navigator → Workflow Definition / Orchestration**
* **Beacon → Discovery Signal / Metadata**
* **Certifier → Certification Package**
* **Registry → SREG**
* **Chronicle → Chronicle Entry**
* **Anchor → Integrity Reference**
* **Attestor → Trust Statement**

Beacon may discover, index, surface, or reference these objects.

It does not duplicate their institutional authority.

---

## Guiding Principles

### Visibility

Potentially relevant information should be easier to find.

### Transparency

Signal origins and discovery context should remain visible.

### Attribution

Sources and originating institutions should remain identifiable.

### Provenance

Signals should preserve sufficient origin and context for review.

### Traceability

Signals should support navigation back to their referenced sources and canonical objects.

### Neutrality

Signals should support exploration without imposing conclusions.

### Authority Preservation

Discovery does not transfer authority from the institution or source responsible for the referenced information.

---

## Long-Term Vision

As Beacon evolves, Discovery Signals may become a primary mechanism through which users and Suite workflows discover relevant developments across Satoshium institutions and external information environments.

Signals direct attention.

Discovery finds the signal.

Authority remains with the source.

---

## Status

Beacon signal architecture is undergoing Suite alignment and production preparation ahead of its originally planned November 2026 development window.

This document establishes the governing conceptual model for Beacon-owned Discovery Signals. Operational schemas, lifecycle rules, prioritization methods, and exchange formats may continue to evolve while remaining aligned with Satoshium Suite Standards, Methodology, Interoperability, and Status conventions.
