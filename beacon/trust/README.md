# Trust

## Purpose

Trust influences how information is interpreted, evaluated, and acted upon.

Beacon may help users and Suite workflows discover trust-related information, but Beacon does not determine what should be trusted.

Within the Satoshium Suite, Beacon owns Discovery Signals and discovery metadata.

Attestor owns Trust Statements and the Suite's trust-assessment function.

These responsibilities are related through governed references but remain institutionally distinct.

---

## Why Trust Matters

Discovery alone does not establish whether information is accurate, verified, certified, reliable, complete, or trustworthy.

Users and systems may seek to understand:

* Whether information has been verified or certified
* Whether supporting evidence exists
* Whether an authoritative Trust Statement exists
* Which sources support a trust-related assessment
* Which institution maintains the relevant canonical object
* Whether later information has changed the context

These questions require clear separation between discovery, certification and verification, and trust assessment.

---

## Discovery and Trust

Beacon performs discovery.

Beacon may discover:

* Trust Statements
* Trust-related Discovery Signals
* Supporting sources
* Certification Packages
* SREG records
* Chronicle Entries
* Integrity References
* External trust-related information

Beacon does not determine trust merely by surfacing this information.

Discovery and trust remain separate institutional functions.

---

## Trust Philosophy

Visibility should not be confused with validity.

Discovery should not be confused with verification.

Verification should not be confused with trust.

Trust should not be confused with truth.

These concepts may inform one another, but they are not interchangeable.

A Beacon reference to a Trust Statement does not make Beacon the authority for that statement.

**Reference does not transfer authority.**

---

## What Beacon Does

Beacon may:

* Publish Trust Signals as Discovery Signals
* Discover Attestor Trust Statements
* Surface attestation context
* Identify supporting sources
* Reference Certification Packages and other canonical objects
* Reveal relationships
* Preserve discovery metadata
* Preserve source attribution and provenance
* Improve trust-related information visibility

Beacon helps users and workflows locate information relevant to trust.

---

## What Beacon Does Not Do

Beacon does not:

* Issue Trust Statements
* Independently determine trust
* Verify claims
* Issue Certification Packages
* Register authoritative SREG records
* Create Chronicle authority
* Create Anchor Integrity References
* Inherit authority from referenced objects
* Endorse conclusions

These responsibilities remain with the appropriate Suite institutions.

---

## Trust Signals

A Trust Signal is a Beacon-owned Discovery Signal associated with trust-related information.

Examples may include discovery of:

* A Trust Statement
* Attestation context
* Supporting references
* Trust-statement updates
* Related Certification Packages
* Related Integrity References
* Relevant historical context
* External trust-related developments

A Trust Signal indicates relevance.

It is not itself a Trust Statement unless Attestor separately creates and owns such an object.

---

## Trust Sources

Trust-related discovery may reference information originating from:

* Attestor
* Certifier
* Registry
* Chronicle
* Anchor
* Atlas
* External sources

Beacon should preserve the source institution or provider, canonical identifier when available, provenance, discovery context, and relevant authority boundary.

External discovery does not convert an external source into a Suite institution or Suite-authoritative object.

---

## Trust and Verification

Certification and verification are not identical to trust assessment.

Certifier owns Certification Packages and certification/verification authority.

Attestor owns Trust Statements.

Beacon may discover and reference objects from both institutions without assuming either function.

A simplified distinction is:

```text
Certifier → Certification Package
Beacon    → Discovery Signal / Metadata
Attestor  → Trust Statement
```

---

## Relationship to Attestor

Attestor is the Suite institution responsible for Trust Statements.

Beacon may discover, reference, and signal the relevance of an Attestor Trust Statement.

Attestor remains authoritative for:

* The Trust Statement
* Its trust-assessment context
* Its lifecycle
* Its supporting attestation structure

Beacon remains authoritative only for its own Discovery Signals and discovery metadata.

The two institutions interoperate without transferring authority.

---

## Relationship to Certifier

Certifier owns Certification Packages and certification/verification authority.

Beacon may discover:

* Certification Packages
* Certification status
* Evidence references
* Verification metadata
* Relationships between certification and trust information

Beacon does not certify results or independently determine certification status.

Certifier remains authoritative for certification.

---

## Relationship to Sources

Trust-related discovery should preserve:

* Source attribution
* Source visibility
* Provenance
* Traceability
* Stable identifiers
* Discovery context
* Institutional authority

Users and systems should be able to understand where information originated and how to review the authoritative source or canonical object.

---

## Relationship to Signals

Discovery Signals may indicate that trust-related information deserves attention.

A Trust Signal may:

* Direct attention to a Trust Statement
* Trigger further investigation or workflow activity
* Reveal new supporting information
* Surface a relationship to another canonical object
* Indicate that relevant trust context has changed

Signals do not determine trust.

They identify information that may warrant review.

---

## Relationship to Navigator

Navigator owns workflow definition and orchestration.

A Navigator-defined workflow may require Beacon to discover trust-related information or locate a Trust Statement.

Beacon may return Discovery Signals, discovery metadata, source references, and results to that workflow.

Navigator orchestrates.

Beacon discovers and signals.

Attestor owns the Trust Statement.

---

## Trust Authority Boundary

Beacon owns the Discovery Signals and discovery metadata it publishes.

When Beacon references a Trust Statement, Attestor remains authoritative for that Trust Statement and its lifecycle.

The Suite institutional model remains:

* **Atlas → Authoritative Intelligence**
* **Navigator → Workflow Definition / Orchestration**
* **Beacon → Discovery Signal / Metadata**
* **Certifier → Certification Package**
* **Registry → SREG**
* **Chronicle → Chronicle Entry**
* **Anchor → Integrity Reference**
* **Attestor → Trust Statement**

Discovery does not become trust.

**Reference does not transfer authority.**

---

## Trust and User Judgment

Beacon supports informed exploration and review.

Human judgment may remain relevant to interpretation and decision-making, but Beacon's institutional boundary does not depend on individual judgment: Beacon performs discovery rather than trust assessment.

Where a governed Suite trust determination is required, Attestor is the institution responsible for the Trust Statement.

---

## Guiding Principles

### Transparency

Trust-related information and discovery context should remain visible.

### Attribution

Sources and originating institutions should remain identifiable.

### Provenance

Origin and relevant context should be preserved for review.

### Traceability

Trust-related discovery should support navigation back to sources and canonical objects.

### Stable References

Canonical identifiers and durable references should be preserved when available.

### Separation of Responsibilities

Discovery, certification and verification, and trust assessment remain distinct institutional functions.

### Neutrality

Discovery should not impose trust conclusions.

### Authority Preservation

Beacon does not inherit the authority of Trust Statements or other canonical objects it references.

---

## Long-Term Vision

As Beacon evolves, it may become an important discovery mechanism for locating Trust Statements and other trust-related information across Suite institutions and external environments.

Its role remains focused:

```text
Discover the information.
Publish the signal.
Preserve the source.
Reference the Trust Statement.
```

Attestor remains responsible for the Trust Statement.

Beacon remains responsible for discovery.

---

## Status

Beacon trust architecture is undergoing Suite alignment and production preparation ahead of its originally planned November 2026 development window.

This document establishes the governing conceptual boundary between Beacon discovery, Certifier certification and verification, and Attestor trust assessment. Operational Trust Signal schemas, metadata requirements, workflow interfaces, and interoperability mechanisms may continue to evolve while remaining aligned with Satoshium Suite Standards, Methodology, Interoperability, and Status conventions.
