# Queries

## Purpose

Queries represent questions, objectives, investigations, requests, or other expressions of intent that provide direction and context for discovery.

Beacon may receive queries directly or participate in Navigator-defined workflows that include discovery objectives.

Queries guide Beacon toward relevant Discovery Signals, sources, canonical objects, relationships, and discovery metadata.

Navigator retains Suite responsibility for workflow definition and orchestration.

Beacon retains responsibility for discovery and its Beacon-owned outputs.

---

## What Is a Query?

A query is an expression of discovery intent.

It communicates what a user or workflow is attempting to discover.

Queries may range from simple searches to complex investigations involving multiple sources, canonical objects, jurisdictions, institutions, or external information environments.

A query does not itself transfer institutional authority or define a new authoritative object.

---

## Why Queries Matter

Discovery begins with intent.

Queries help provide direction for exploration by allowing Beacon to:

* Identify relevant information
* Locate potential sources
* Surface Discovery Signals
* Locate canonical Suite objects
* Identify relationships
* Reduce unnecessary noise
* Preserve relevant discovery context
* Improve information accessibility

The clarity of the query can influence the usefulness of discovery.

---

## Types of Queries

### Search Queries

Requests intended to locate specific information.

Examples may include:

* Jurisdictions
* Sources
* Canonical objects
* Events
* Organizations
* Discovery Signals

---

### Research Queries

Requests intended to explore a topic more deeply.

Research queries may involve:

* Multiple sources
* Historical context
* Comparative analysis
* Related canonical objects
* Cross-institution references

---

### Investigative Queries

Requests intended to uncover relationships, patterns, or supporting information.

These queries may require:

* Cross-referencing sources or canonical objects
* Identifying source connections
* Reviewing Chronicle context
* Examining supporting evidence
* Tracing provenance or relationships

---

### Exploratory Queries

Requests without a narrowly defined objective.

Users or workflows may seek to:

* Learn
* Browse
* Discover
* Investigate emerging topics
* Explore relationships

---

## Query Components

A query may contain one or more elements.

### Subject

The primary topic or object of interest.

### Context

Additional information that narrows or explains the discovery objective.

### Scope

The boundaries of the request.

### Intent

The purpose behind the query.

### Constraints

Limitations such as time, geography, source type, canonical-object type, institution, or other discovery boundaries.

---

## Query Outcomes

Queries may contribute to Beacon outputs such as:

* Discovery Signals
* Discovery metadata
* Source references
* References to Atlas authoritative intelligence
* References to Certification Packages
* References to SREG records
* References to Chronicle Entries
* References to Integrity References
* References to Trust Statements
* External-source references
* Related discoveries and relationships
* Beacon results

Not all queries will produce meaningful results.

Discovery does not guarantee relevance, completeness, certification, integrity, or trust.

---

## Query Neutrality

Beacon seeks to perform discovery without predetermined conclusions.

Queries should support exploration rather than predetermine outcomes.

Discovery should assist users and workflows in finding relevant information without dictating what they should conclude.

Relevance should not be confused with authority.

---

## Relationship to Discovery

Queries provide intent for discovery.

Beacon processes that intent against available information and may publish Discovery Signals, discovery metadata, source references, and results.

A simplified flow may be represented as:

```text
Workflow / Query
      ↓
Beacon Discovery
      ↓
Discovery Signal / Metadata
      ↓
Result / Referenced Source or Canonical Object
```

---

## Relationship to Navigator

Navigator and Beacon have distinct but complementary institutional responsibilities.

Navigator owns:

* Workflow definition
* Workflow orchestration
* Coordination of multi-institution processes

Beacon owns:

* Discovery
* Discovery Signals
* Discovery metadata

Navigator may formulate, refine, route, or coordinate workflow objectives that require Beacon discovery.

Beacon may return Discovery Signals, discovery metadata, source references, and results for continued workflow processing.

**Navigator orchestrates. Beacon discovers and signals.**

A query may guide Beacon without transferring Navigator's orchestration responsibility to Beacon.

---

## Relationship to Signals

Queries influence which information becomes visible through discovery.

Different queries may surface different Discovery Signals from the same information environment.

Discovery Signals remain Beacon-owned objects regardless of whether the discovery was initiated directly or through a Navigator-defined workflow.

---

## Relationship to Sources

Queries may help identify:

* Authoritative sources
* Original sources
* Supporting sources
* Related sources
* Historical sources
* External sources
* Institution-owned canonical objects

Beacon should preserve source attribution, provenance, stable references, discovery context, and authority boundaries when presenting discovered information.

---

## Institutional Authority Boundary

A query does not alter the authority of the information it causes Beacon to discover.

The Suite institutional model remains:

* **Atlas → Authoritative Intelligence**
* **Navigator → Workflow Definition / Orchestration**
* **Beacon → Discovery Signal / Metadata**
* **Certifier → Certification Package**
* **Registry → SREG**
* **Chronicle → Chronicle Entry**
* **Anchor → Integrity Reference**
* **Attestor → Trust Statement**

Beacon may discover and reference these objects.

The originating institution retains authority over its canonical object.

**Reference does not transfer authority.**

---

## Query Principles

### Clarity

Clear discovery intent improves discovery.

### Transparency

Users and systems should understand how queries and workflow context influence results.

### Relevance

Queries should help focus discovery on useful information.

### Exploration

Queries should support learning, research, investigation, and discovery.

### Flexibility

Beacon should support a variety of discovery objectives and query types.

### Traceability

Discovery outputs should preserve sufficient context to understand the query or workflow objective that produced them.

### Authority Preservation

Queries and discovery outputs should not blur the institutional authority of referenced canonical objects.

---

## Future Development

Beacon query capabilities may include:

* Structured queries
* Advanced filtering
* Jurisdiction-specific queries
* Discovery Signal queries
* Historical queries
* Relationship mapping
* Cross-system queries
* Canonical-object queries
* Navigator workflow interfaces

Specific implementations may evolve as Beacon advances toward production.

---

## Status

Beacon query architecture is undergoing Suite alignment and production preparation ahead of its originally planned November 2026 development window.

This document establishes the governing conceptual relationship between queries, Navigator orchestration, and Beacon discovery. Operational query schemas, filtering methods, workflow interfaces, and technical specifications may continue to evolve while remaining aligned with Satoshium Suite Standards, Methodology, Interoperability, and Status conventions.
