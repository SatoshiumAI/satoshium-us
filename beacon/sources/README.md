# Sources

## Purpose

Sources provide the origin, authority, context, attribution, and provenance behind information surfaced through Beacon.

Beacon uses source references to help users and Suite workflows understand where information originated, which institution or external source maintains it, and how it relates to Discovery Signals, canonical objects, and other information.

Beacon seeks to improve visibility while preserving source attribution, provenance, traceability, stable references, discovery context, and institutional authority.

---

## What Is a Source?

A source is the origin or authoritative location of information referenced through discovery.

Sources may include:

* Atlas authoritative intelligence
* Certifier Certification Packages
* Registry SREG records
* Chronicle Entries
* Anchor Integrity References
* Attestor Trust Statements
* Documents and publications
* Research materials and datasets
* Government and public records
* Media references
* Open-source repositories
* Other external information environments

A source provides context and a review pathway for discovery.

---

## Source Authority Boundary

Beacon owns the Discovery Signals and discovery metadata it publishes.

Beacon does not become authoritative for a source or canonical object merely because it discovers, indexes, surfaces, or references it.

The originating institution or external source remains responsible for the information it maintains.

**Reference does not transfer authority.**

---

## Why Sources Matter

Information without attribution or provenance is difficult to review.

Sources help users and systems understand:

* Origin
* Source institution or external provider
* Canonical identifier, when available
* Context
* Ownership or institutional responsibility
* Authorship or publication history
* Supporting evidence
* Relevant status
* Relationships to other objects

Discovery becomes more useful when source information remains visible and traceable.

---

## Source Philosophy

Beacon does not seek to replace sources or assume their authority.

Beacon helps users and Suite workflows discover them.

The purpose of discovery is not merely to surface information, but to preserve the ability to trace information back to its origin or authoritative canonical object.

Source visibility and authority preservation are core Beacon principles.

---

## Types of Sources

### Atlas Sources

Authoritative intelligence originating from Atlas.

Examples:

* Jurisdiction intelligence
* Media intelligence
* Profiles
* Supporting references
* Related Atlas information

Atlas retains authority over the intelligence it maintains.

---

### Certifier Sources

Information originating from Certifier.

Examples:

* Certification Packages
* Certification status
* Evidence references
* Verification metadata
* Certification-related relationships

Certifier retains certification and verification authority.

---

### Registry Sources

Information originating from Registry.

Examples:

* SREG records
* Record metadata
* Stable identifiers
* Record histories
* Lifecycle information
* Record relationships

Registry retains authority over its registered records.

---

### Chronicle Sources

Information originating from Chronicle.

Examples:

* Chronicle Entries
* Qualifying Occurrences
* Historical source references
* Timelines
* Preserved historical context

Chronicle retains authority over its historical record.

---

### Anchor Sources

Information originating from Anchor.

Examples:

* Integrity References
* Anchoring relationships
* Integrity evidence
* Integrity metadata

Anchor retains authority over its Integrity References.

---

### Attestor Sources

Information originating from Attestor.

Examples:

* Trust Statements
* Attestation context
* Supporting references
* Trust metadata

Attestor retains authority over its Trust Statements.

---

### External Sources

Information originating outside the Satoshium Suite.

Examples:

* Government publications
* Research institutions
* Academic materials
* Public records
* News organizations
* Open data repositories
* Open-source repositories
* Third-party systems

External discovery does not make an external source a Suite institution or convert its information into a Suite-authoritative object.

---

## Source Attributes

Source references may preserve attributes such as:

* Source identity
* Source institution or provider
* Canonical identifier
* Origin
* Scope
* Format
* Accessibility
* Publication or record date
* Relevant status
* Version
* Provenance
* Discovery context
* Relationships

Different sources may provide different perspectives or institutional functions concerning the same subject.

---

## Source Attribution

Whenever practical, Beacon should preserve:

* Source identity
* Source origin
* Source institution or provider
* Canonical identifier, when available
* Publication or record information
* Related references
* Provenance
* Discovery context
* Relevant authority boundary

Users and systems should be able to determine where information originated and how to review it.

---

## Source Relationships

Sources and canonical objects may connect to other sources or objects.

Examples may include:

* Supporting sources
* Contradicting sources
* Historical sources
* Related SREG records
* Related Chronicle Entries
* Related Certification Packages
* Related Integrity References
* Related Trust Statements
* Derived publications
* Cross-institution references

Beacon may surface these relationships while preserving the identifiers, provenance, and authority of the referenced information.

---

## Source Transparency

Discovery should not obscure origin.

Users and systems should be able to understand:

* Which source produced or maintains information
* Which institution retains authority
* How the source was discovered
* Which sources support a Discovery Signal or result
* Which sources relate to other canonical objects
* How the source can be reviewed

Transparency improves discoverability, reviewability, and understanding.

---

## Source Accessibility

Sources should be discoverable whenever practical and permitted.

Beacon implementations may support:

* Source indexing
* Source categorization
* Source filtering
* Source mapping
* Source relationship discovery
* Canonical-object linking

Specific implementations may evolve as Beacon advances toward production.

---

## Relationship to Discovery Signals

Discovery Signals commonly reference sources or canonical objects.

A Discovery Signal without source context may provide limited review value.

Beacon should preserve enough source information to explain why a signal exists and where the referenced information can be examined.

A simplified relationship may be represented as:

```text
Source / Canonical Object
          ↓
       Discovery
          ↓
Discovery Signal / Metadata
```

The signal belongs to Beacon.

Authority over the referenced information remains with its source.

---

## Relationship to Discovery

Discovery may begin with a source, identify a source, or produce a reference to a source.

Beacon may help users and workflows:

* Locate sources
* Compare sources
* Organize source references
* Explore source relationships
* Trace Discovery Signals to their origin
* Navigate to authoritative canonical objects

Beacon makes sources discoverable without replacing them.

---

## Relationship to Results

Beacon results may contain references to one or more sources, canonical objects, or Discovery Signals.

Users should be able to trace results back to supporting or authoritative source material whenever practical.

This supports:

* Investigation
* Certification review
* Historical review
* Integrity review
* Trust review
* Future research

A Beacon result does not become authoritative merely because it presents authoritative source information.

---

## Relationship to Suite Authority

Sources may originate from multiple Suite institutions, each with a distinct canonical object:

* **Atlas → Authoritative Intelligence**
* **Navigator → Workflow Definition / Orchestration**
* **Beacon → Discovery Signal / Metadata**
* **Certifier → Certification Package**
* **Registry → SREG**
* **Chronicle → Chronicle Entry**
* **Anchor → Integrity Reference**
* **Attestor → Trust Statement**

Navigator may orchestrate workflows that cause Beacon to discover or retrieve sources, but Navigator does not replace the authority of the source institution.

Beacon preserves the relationship between discovery and authority.

---

## Guiding Principles

### Attribution

Sources and originating institutions should remain identifiable.

### Provenance

Origin and relevant context should be preserved for review.

### Transparency

Source relationships and authority boundaries should remain visible.

### Traceability

Information should support navigation back to its source or canonical object.

### Stable References

Canonical identifiers and durable source references should be preserved when available.

### Accessibility

Sources should be discoverable whenever practical and permitted.

### Neutrality

Source documentation should not imply endorsement or authority beyond what the source actually holds.

### Authority Preservation

Discovery does not transfer authority from the institution or source responsible for the referenced information.

---

## Long-Term Vision

As Beacon evolves, sources may form part of a broader discovery network connecting Discovery Signals, authoritative intelligence, Certification Packages, SREG records, Chronicle Entries, Integrity References, Trust Statements, external information, and cross-institution relationships.

Beacon helps users and workflows find information.

Sources preserve where that information came from.

Authority remains with the source.

---

## Status

Beacon source architecture is undergoing Suite alignment and production preparation ahead of its originally planned November 2026 development window.

This document establishes the governing conceptual model for Beacon source handling. Operational schemas, source-reference requirements, provenance rules, indexing methods, and interoperability mechanisms may continue to evolve while remaining aligned with Satoshium Suite Standards, Methodology, Interoperability, and Status conventions.
