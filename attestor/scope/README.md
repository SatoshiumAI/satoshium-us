# Scope

## Purpose

The scope of Attestor defines the boundaries of the system, clarifying what Attestor is intended to do, what information it manages, and which responsibilities belong to other systems within the Satoshium ecosystem.

A clearly defined scope helps maintain consistency, transparency, interoperability, and separation of responsibilities.

---

## Mission Scope

Attestor focuses on trust-related information.

Its primary responsibilities include:

* Attestations
* Evidence relationships
* Reputation signals
* Trust-related records
* Corrections
* Accountability information
* Trust context preservation

Attestor exists to document trust-related information rather than determine objective truth.

---

## Core Scope Areas

### Attestations

Attestor manages structures for documenting statements made regarding:

* Identities
* Claims
* Records
* Events
* Qualifications
* Relationships
* Organizations

Attestations represent a foundational component of the system.

---

### Evidence

Attestor manages references to evidence associated with attestations and trust-related records.

Examples include:

* Documents
* Publications
* Records
* Certifications
* Historical materials
* Source references

Evidence helps provide context for interpretation.

---

### Reputation

Attestor may maintain reputation-related records and signals.

Examples include:

* Historical participation
* Prior attestations
* Reputation indicators
* Reputation events
* Trust-related observations

Reputation contributes context to trust evaluations.

---

### Trust Signals

Attestor may document trust-related signals associated with identities, organizations, records, or claims.

Trust signals may help users better understand trust-related context.

---

### Corrections and Retractions

Attestor supports:

* Corrections
* Amendments
* Revisions
* Retractions

Historical transparency remains an important objective.

---

### Accountability Records

Attestor may preserve information regarding:

* Attestors
* Contributors
* Correctors
* Record creators

Accountability supports transparency and reviewability.

---

## Information Within Scope

Examples of information generally within Attestor's scope include:

* Attestation records
* Evidence references
* Trust relationships
* Reputation information
* Source references
* Correction records
* Retraction records
* Confidence indicators
* Accountability records

These categories may evolve over time.

---

## Information Outside Scope

Certain responsibilities belong primarily to other systems.

Examples include:

* Identity management
* Verification operations
* Historical preservation
* Discovery services
* Record registry management
* Jurisdiction intelligence

Attestor may reference these systems but does not replace them.

---

## Relationship to Anchor

Anchor serves as the identity layer.

Anchor focuses on:

* Identity records
* Identity structures
* Identity governance

Attestor may reference identities maintained by Anchor.

A simplified distinction may be represented as:

```text id="a9t4qp"
Anchor → Identity
Attestor → Trust
```

---

## Relationship to Certifier

Certifier serves as the verification layer.

Certifier focuses on:

* Evidence evaluation
* Verification processes
* Certification outcomes

Attestor may reference verification results.

A simplified distinction may be represented as:

```text id="b6r2kw"
Certifier → Verification
Attestor → Trust Context
```

---

## Relationship to Registry

Registry serves as the record management layer.

Registry focuses on:

* Record organization
* Record storage
* Record classification

Attestor may create trust-related records that Registry helps manage.

---

## Relationship to Chronicle

Chronicle serves as the historical layer.

Chronicle focuses on:

* Historical preservation
* Event records
* Historical timelines

Attestor may contribute records that become part of the historical record.

---

## Relationship to Beacon

Beacon serves as the discovery layer.

Beacon focuses on:

* Discovery
* Search
* Information visibility
* Signal identification

Attestor focuses on trust-related information.

A simplified distinction may be represented as:

```text id="c3m8yu"
Beacon → Discovery
Attestor → Trust
```

---

## Relationship to Atlas

Atlas serves as the data layer.

Atlas focuses on:

* Jurisdiction intelligence
* Media intelligence
* Geographic information

Attestor may reference information originating from Atlas but does not manage Atlas content.

---

## Relationship to Navigator

Navigator serves as the query layer.

Navigator focuses on:

* Questions
* Exploration
* Query workflows

Attestor focuses on trust-related records and context.

---

## Scope Boundaries

Attestor seeks to answer questions such as:

* Who made this statement?
* What evidence may support it?
* What trust-related context exists?
* What reputation signals are available?
* What corrections have occurred?

Attestor generally does not seek to answer:

* Is this absolutely true?
* Which jurisdiction is best?
* What information should be discovered?
* What identity should exist?

These responsibilities belong elsewhere.

---

## Long-Term Scope

Future Attestor development may expand to include:

* Advanced trust frameworks
* Reputation systems
* Confidence models
* Governance structures
* Trust interoperability standards
* Distributed attestation networks

Specific implementations may evolve over time.

---

## Relationship to the Satoshium Suite

Attestor operates within a broader ecosystem:

```text id="d7n5zr"
Atlas      → Data
Navigator  → Query
Beacon     → Discovery
Certifier  → Verification
Registry   → Records
Chronicle  → History
Anchor     → Identity
Attestor   → Trust
```

Scope boundaries help preserve clarity across these systems.

---

## Guiding Statement

The scope of Attestor may be summarized as:

```text id="e4x1vk"
Attestor documents trust.

It does not define truth.
```

---

## Status

This scope document represents an initial conceptual framework and may evolve as Attestor matures and additional standards are developed.
