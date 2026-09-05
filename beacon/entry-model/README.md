# Satoshium Beacon — Discovery Signal Entry Model

## Overview

The **Discovery Signal Entry Model** defines the canonical structure of a Beacon-owned **Discovery Signal**.

This page begins **Beacon Phase II — Production Architecture** by establishing the object that later work on Signal Types, Lifecycle, Identifiers, Schemas, Validation, Provenance, Authority, Relationships, Versioning, Publication, Methodology, and Production will govern.

The Entry Model answers the first Phase II question:

```text
What exactly does Beacon create?
```

Beacon's canonical production object is:

```text
Discovery Signal
```

supported by:

```text
Discovery Metadata
```

---

## Purpose

Beacon cannot define production rules until it defines the object those rules govern.

The Entry Model establishes the canonical object boundary for a Discovery Signal and identifies the major structural components required to describe:

- identity
- subject
- signal type
- source
- provenance
- canonical-object references
- discovery metadata
- timestamps
- version
- status
- relationships
- institutional ownership

This page defines those components at the architectural level.

It does **not** prematurely freeze downstream production rules that belong to later Phase II work.

---

## Canonical Responsibility

Beacon's institutional responsibility remains:

```text
Beacon
→ Discovery & Signals
```

Its canonical responsibility is centered on:

```text
Discovery Signal / Metadata
```

A Discovery Signal is owned by Beacon.

Discovery Metadata is owned by Beacon.

A referenced canonical object remains owned by its originating Suite institution.

An external source remains external.

The governing rule is:

> **Reference does not transfer authority.**

---

## Canonical Entry Structure

The Discovery Signal Entry Model is organized conceptually as:

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

This sequence describes the major structural components of the object.

It is not intended to impose a mandatory processing order.

---

## 1. Identity

Identity distinguishes one Beacon Discovery Signal from every other Beacon object.

Conceptual identity elements include:

```text
Beacon Discovery Signal Identifier
Human-readable title or label
Beacon institutional ownership
Object Type → Discovery Signal
```

The final identifier syntax is intentionally not frozen by the Entry Model.

Identifier rules belong to the later:

```text
/beacon/identifiers/
```

architecture.

---

## 2. Subject

Subject identifies what the Discovery Signal is about.

Conceptual subject information may include:

```text
Subject name or description
Subject type or classification
Relevant jurisdiction
Relevant system
Relevant entity
Relevant record
Relevant event
Relevant artifact
Subject identifier when one exists
```

The Subject identifies the focus of discovery.

It does not establish Beacon authority over that subject.

---

## 3. Signal Type

Signal Type classifies the nature of the discovery represented by the Beacon object.

Conceptual categories may include:

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

Other governed categories may emerge through production architecture.

These values are not frozen by the Entry Model.

The controlled production vocabulary belongs to:

```text
/beacon/signal-types/
```

---

## 4. Source

Source identifies where the discovered information originated.

Conceptual source information may include:

```text
Source Institution
External Source
Source Name
Source Identifier
Source Object Type
Canonical Source Location
Public Source Location
```

Source visibility is essential because discovery must preserve the path to authority.

Beacon may discover information from another institution.

That does not make Beacon authoritative for the source object.

---

## 5. Provenance

Provenance preserves the traceable path between the Discovery Signal and the information that caused the signal to exist.

Conceptual provenance information may include:

```text
Observed Source
Observation Context
Observation Method or Mechanism
Supporting Reference
Discovery Actor or Process
```

where appropriate.

Provenance should make a Discovery Signal reviewable rather than merely assertive.

The dedicated:

```text
/beacon/provenance/
```

phase will define the production provenance model.

---

## 6. Canonical-Object References

A Discovery Signal may reference canonical objects owned by other Satoshium Suite institutions.

Examples include:

```text
Atlas
→ Authoritative Intelligence

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

Navigator
→ Workflow Definition / Orchestration context
```

A canonical reference establishes a governed connection.

It does not transfer ownership or authority.

```text
Beacon reference
≠
Beacon ownership of referenced object
```

---

## 7. Discovery Metadata

Discovery Metadata preserves context needed to interpret, filter, trace, organize, and rediscover the signal.

Conceptual metadata may include:

```text
Discovery Context
Classification
Relevant Status
Jurisdiction Context
Domain Context
Search Context
Workflow Context
Keywords
Tags
Controlled Values
Relationship Metadata
```

Discovery Metadata supports the Discovery Signal.

It does not replace the source or canonical object.

The broader metadata architecture is documented at:

```text
/beacon/discovery-metadata/
```

---

## 8. Timestamps

Time must distinguish the observation of information from the creation, modification, and publication of the Beacon object itself.

Conceptual timestamps may include:

```text
Discovered At / Observed At
Created At
Updated At
Published At
Last Observed
```

Not every timestamp will necessarily apply to every signal.

Exact requirements and semantics remain subject to later Lifecycle, Versioning, and Publication architecture.

---

## 9. Version

Version identifies the governed state of a Discovery Signal over time.

Conceptual version information may include:

```text
Signal Version
Previous Version
Supersession Information
```

The Entry Model establishes Version as a structural concern without defining its final semantics.

Those rules belong to:

```text
/beacon/versioning/
```

---

## 10. Status

Status records the current institutional state of the Discovery Signal.

Potential status dimensions include:

```text
Lifecycle State
Publication State
Resolution State
Supersession State
```

The Entry Model does not freeze the controlled status vocabulary.

Lifecycle states belong to:

```text
/beacon/lifecycle/
```

Publication states belong to:

```text
/beacon/publication/
```

---

## 11. Relationships

Relationships connect a Discovery Signal to other relevant objects or contexts.

Potential relationship categories include:

```text
Source Relationship
Canonical-Object Relationship
Related-Signal Relationship
Version Relationship
Supersession Relationship
Workflow Relationship
```

Other governed relationships may become necessary.

The production relationship vocabulary should remain minimal until real architecture and production demonstrate what Beacon actually requires.

Relationship rules will be defined at:

```text
/beacon/relationships/
```

---

## 12. Institutional Ownership

Institutional ownership is a required architectural boundary of every Beacon Discovery Signal.

The Entry Model preserves:

```text
Beacon
→ owns the Discovery Signal

Beacon
→ owns Discovery Metadata

Source Institution
→ owns its canonical object

External Source
→ remains external
```

Discovery connects responsibilities.

It does not collapse them.

---

## Conceptual Discovery Signal Skeleton

The Entry Model may be represented conceptually as:

```json
{
  "discovery_signal": {
    "identity": {},
    "subject": {},
    "signal_type": "",
    "source": {},
    "provenance": {},
    "canonical_references": [],
    "discovery_metadata": {},
    "timestamps": {},
    "version": {},
    "status": {},
    "relationships": []
  }
}
```

This is an **architectural skeleton**.

It is not yet the production Beacon schema.

The following remain unfrozen:

```text
exact field names
required properties
controlled values
data types
schema constraints
validation rules
identifier patterns
relationship vocabulary
status vocabulary
```

Those decisions belong to their respective Phase II architecture.

---

## Expected Core Components

At the Entry Model stage, the following are expected to form the core of a production Discovery Signal:

```text
Identity
Subject
Signal Type
Source
Provenance
Discovery Metadata
Timestamps
Version
Status
```

This expectation remains subject to later schema and validation review.

---

## Potentially Conditional Components

Some structural components may be conditional rather than universally required.

These may include:

```text
Canonical-Object References
External References
Relationships
Supersession Data
Navigator Workflow Context
```

A production schema should not require meaningless values merely to populate every possible field.

Conditional structures should exist when the signal actually requires them.

---

## What the Entry Model Does Not Decide

The Entry Model deliberately does not finalize:

```text
Beacon identifier syntax
Discovery Signal controlled types
Lifecycle states
Publication states
Production JSON schema
Validation rules
Provenance requirements
Relationship vocabulary
Versioning semantics
Publication procedure
First production Discovery Signal
```

These questions belong to later Phase II architecture.

The governing development discipline is:

> **Define the object first. Freeze downstream rules only when their dedicated architecture is reviewed.**

---

## Authority Boundary

A Discovery Signal may describe or reference information whose authority exists outside Beacon.

Beacon's act of discovery does not alter that authority.

```text
Beacon owns the signal.
The source owns the source object.
Discovery preserves the connection.
```

Therefore:

> **Reference does not transfer authority.**

---

## Relationship to the Satoshium Suite

The Entry Model preserves the current canonical institutional model:

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

Each institution retains responsibility for its own canonical objects.

Beacon provides discovery without becoming a substitute for those institutions.

---

## Phase II Dependency Path

The Discovery Signal Entry Model is the dependency foundation for the remaining Beacon production architecture.

The current Phase II sequence is:

```text
Discovery Signal Entry Model
        ↓
Discovery Signal Types
        ↓
Discovery Signal Lifecycle
        ↓
Beacon Identifier Standard
        ↓
Beacon Schemas
        ↓
Validation
        ↓
Discovery Provenance
        ↓
Authority & Reference Model
        ↓
Relationship Model
        ↓
Versioning & Supersession
        ↓
Publication Model
        ↓
Discovery Signals Register
        ↓
Individual Discovery Signal
        ↓
Beacon Discovery Methodology
        ↓
Production Model / First Operation
```

Later pages may refine the Entry Model.

They should do so explicitly rather than silently redefine Beacon's canonical object.

---

## Current Status

As of September 5, 2026:

```text
Institution → Beacon
Suite Role → Discovery & Signals
Canonical Responsibility → Discovery Signal / Metadata
Status → Continuing Development
Phase → Phase II — Production Architecture
Entry Model → Defined at architectural level
Production Schema → Not yet frozen
First Production Discovery Signal → Not yet created
Operational → No
```

Beacon remains in Continuing Development.

The Entry Model establishes the first production-architecture dependency.

It does not establish operational status.

---

## Governing Principles

The Discovery Signal Entry Model follows these principles:

```text
Define the object before defining the machinery around it.

Preserve source visibility.

Preserve provenance.

Preserve canonical identifiers.

Keep institutional ownership explicit.

Do not manufacture authority through discovery.

Freeze only what dedicated architecture or production proves necessary.
```

Above all:

> **Reference does not transfer authority.**

---

## Next Phase II Step

The next production-architecture page is:

```text
/beacon/signal-types/
```

Its purpose is to establish the governed vocabulary of Discovery Signal types Beacon recognizes without prematurely creating categories that production does not require.

---

## Last Updated

September 5, 2026
