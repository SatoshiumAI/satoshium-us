# Satoshium Beacon — Relationship Model

## Overview

The **Beacon Relationship Model** defines how Satoshium Beacon represents governed connections between:

```text
Discovery Signals
Suite canonical objects
sources
external objects
versions
superseding objects
Navigator workflows
other relevant endpoints
```

The model exists so Beacon can preserve meaningful connections without collapsing independently owned objects into a single record.

Its governing principle is:

> **Relationship connects objects. It does not merge them.**

The Suite-wide authority principle remains:

> **Reference does not transfer authority.**

---

# Purpose

The Relationship Model answers:

```text
What objects may a Discovery Signal relate to?

What does the relationship mean?

Which direction does the relationship run?

What evidence or provenance supports it?

Who owns each endpoint?

Does the relationship represent a source assertion or a Beacon determination?
```

Relationships are therefore governed institutional connections rather than generic hyperlinks.

---

# Architectural Dependency

The Relationship Model follows the Authority & Reference Model deliberately.

The dependency is:

```text
Authority
→ determines who owns each object and determination

Relationship
→ defines how those independently owned objects may be connected
```

Beacon should not define a relationship without preserving the identity and ownership of its endpoints.

---

# Canonical Example

A Beacon Discovery Signal may reference both a Certification Package and a related Registry record.

Conceptually:

```text
Certifier
SC-CERT-2026-0001
        ↓
   referenced by
        ↓
Beacon
BEAC-2026-0001
        ↓
   also references
        ↓
Registry
SREG-2026-0001
```

These remain:

```text
three canonical objects
three institutional identities
three separately governed responsibilities
```

They do not become one composite record merely because Beacon connects them.

---

# Relationship Endpoints

Every governed relationship must identify its endpoints.

Potential endpoints include:

```text
Beacon Discovery Signal

another Beacon Discovery Signal

Suite canonical object

external source

external object

Navigator workflow reference

Beacon version

superseding Beacon object or version
```

When available, each endpoint should preserve:

```text
native identifier
institutional owner
native object type
source location or canonical reference
```

---

# Relationship Meaning

A relationship must explain why its endpoints are connected.

The meaning should be:

```text
explicit
reviewable
supported
appropriately attributed
consistent with institutional authority
```

A simple technical link is not automatically an institutional relationship.

The governing posture is:

> **A link without governed meaning is not yet an institutional relationship.**

---

# Initial Relationship Classes

The Phase II architecture recognizes the following initial relationship classes.

## Source

Connects a Discovery Signal to the source Beacon actually observed.

Conceptually:

```text
Discovery Signal
→ observed from
→ Source
```

This relationship is foundational to Discovery Provenance.

---

## Canonical Object

Connects a Discovery Signal to a Suite-owned canonical object relevant to the discovery.

Example:

```text
BEAC-2026-0001
→ references
→ ANCH-2026-0001
```

The referenced object remains owned by its originating institution.

---

## Related Signal

Connects one Beacon Discovery Signal to another Beacon Discovery Signal when their discovery contexts are materially related.

Example:

```text
BEAC-2026-0001
↔ related to ↔
BEAC-2026-0002
```

Related signals remain independent canonical objects.

A related-signal relationship does not imply:

```text
same identity
same version
supersession
duplication
```

unless another governed relationship explicitly establishes that meaning.

---

## Version

Connects governed versions of the same Beacon Discovery Signal identity.

Conceptually:

```text
BEAC-2026-0001 · Version 1
        ↓
followed by
        ↓
BEAC-2026-0001 · Version 2
```

Exact version mechanics are governed by the later:

```text
/beacon/versioning/
```

architecture.

---

## Supersession

Connects an earlier Beacon signal or version to the later signal or version that carries the current discovery context.

Conceptually:

```text
Earlier Signal
→ superseded by
→ Later Signal / Version
```

Supersession preserves institutional history.

It does not delete the earlier object.

---

## Workflow

Connects Beacon discovery activity or a Discovery Signal to Navigator workflow context when that context is material.

Conceptually:

```text
Navigator
→ owns Workflow Definition / Orchestration

Beacon
→ owns Discovery Signal

Relationship
→ preserves Beacon's participation in the workflow
```

Beacon does not duplicate Navigator's workflow authority.

---

## External

Connects a Beacon Discovery Signal to a non-Suite source or object.

Conceptually:

```text
BEAC Discovery Signal
→ references
→ External Source / Object
```

The external endpoint remains external.

Beacon owns only:

```text
its Discovery Signal
its reference
its relationship representation
its discovery provenance
```

---

# Architectural Status of Relationship Classes

The initial classes are:

```text
Source
Canonical Object
Related Signal
Version
Supersession
Workflow
External
```

These are established architectural categories.

The exact machine-readable relationship-type vocabulary remains subject to:

```text
Versioning
Publication
Methodology
production implementation
production proof
```

---

# Relationship Direction

Direction matters when relationship meaning is asymmetric.

Examples:

```text
Discovery Signal
→ observed from
→ Source

Discovery Signal
→ references
→ Canonical Object

Earlier Signal
→ superseded by
→ Later Signal
```

A reverse relationship may sometimes be derived for navigation.

That does not mean the governed relationship itself is automatically symmetric.

---

# Directional Relationships

Potential directional meanings include:

```text
observed from
references
supersedes
superseded by
derived through workflow
```

The source and target endpoints matter.

Reversing them may change the meaning.

---

# Symmetric Relationships

Some relationships may be conceptually mutual.

Example:

```text
related to
```

However, symmetry should be established by the governed Relationship Type.

It should not be inferred merely because a user interface displays both endpoints.

---

# Relationship Basis

Every production relationship requires a reviewable basis.

Conceptually:

```text
Endpoint A identified
+
Endpoint B identified
+
Relationship meaning stated
+
Provenance or supporting basis present
+
Authority boundary preserved
=
Relationship eligible for Validation
```

A relationship should not be represented merely because two objects appear contextually similar.

---

# Observed Relationships

Beacon may preserve a relationship explicitly represented by a source.

Conceptually:

```text
Source
→ states A is related to B

Beacon
→ observes the source relationship

Discovery Signal
→ preserves the relationship with attribution
```

In this case, the source remains responsible for the source-owned assertion.

Beacon is responsible for accurately representing what it observed.

---

# Beacon-Determined Relationships

Beacon may also represent a relationship determined within its own discovery function.

This is permissible when:

```text
the endpoints are identifiable
the basis is reviewable
the relationship is within Beacon's discovery responsibility
the relationship does not claim authority belonging elsewhere
the relationship is clearly identifiable as a Beacon determination
```

Beacon must not present its own inferred relationship as though another institution established it.

---

# Relationship Attribution

The model must distinguish:

```text
Source-Attributed Relationship
```

from:

```text
Beacon-Determined Relationship
```

Example of source attribution:

```text
Registry represents this connection.
```

Example of Beacon determination:

```text
Beacon discovered and represents this connection based on the preserved supporting basis.
```

This distinction protects institutional authority.

---

# Multiple References

A single Discovery Signal may reference multiple independently owned objects when the discovery legitimately connects them.

Example:

```text
                 BEAC-2026-0001
                  /           \
                 /             \
SC-CERT-2026-0001             SREG-2026-0001
```

The Discovery Signal may preserve the relevant relationship among these objects.

The objects remain separate.

---

# No Object Collapse

Multiple references do not automatically create a new composite canonical object.

Therefore:

```text
Certification Package
+
SREG
+
Discovery Signal
≠
one canonical record
```

The canonical objects remain independently:

```text
identified
owned
versioned
governed
authoritative within their own institutional domains
```

---

# Cross-Suite Relationship Example

The current production-proven Suite sequence provides a useful example.

Canonical objects include:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
```

Beacon may later create:

```text
BEAC-2026-0001
```

that discovers or references one or more of these objects.

Beacon may preserve their relevant connections.

Beacon must not imply that:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
BEAC-2026-0001
```

are one object moving through five systems.

They are separate institution-owned objects connected by governed relationships and provenance.

---

# Signal Type vs. Relationship Type

Signal Type and Relationship Type are separate concepts.

## Signal Type

Answers:

> **What kind of discovery does this Beacon object represent?**

Current architectural Signal Types are:

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

## Relationship Type

Answers:

> **How are these two endpoints connected?**

A Discovery Signal may contain multiple relationships while retaining one primary Signal Type.

---

# Relationship Signal

The **Relationship** Signal Type is used when the discovered relationship itself is the primary subject of the Discovery Signal.

Conceptually:

```text
Subject
→ the discovered connection

Signal Type
→ Relationship

Endpoints
→ Object A + Object B

Provenance
→ basis supporting the connection
```

A Discovery Signal containing relationships does not automatically become a Relationship Signal.

Therefore:

```text
Relationship Signal
≠
every Discovery Signal containing a relationship
```

---

# Version Relationships

Version relationships describe governed revisions under the same canonical Beacon identity.

Example:

```text
Identifier
→ BEAC-2026-0001

Version
→ 1

followed by

Identifier
→ BEAC-2026-0001

Version
→ 2
```

The canonical identifier remains stable.

Version remains separate from identity.

The Versioning & Supersession architecture will define the exact mechanics.

---

# Supersession Relationships

Supersession identifies the governed replacement for an earlier signal or version.

Conceptually:

```text
Earlier Signal / Version
        ↓
superseded by
        ↓
Later Signal / Version
```

The earlier institutional object remains traceable.

Supersession does not mean:

```text
deletion
identity reuse
historical erasure
```

---

# Relationship Persistence

A valid historical relationship should not silently disappear because:

```text
a source changes
a signal is superseded
a referenced object moves
a referenced object becomes unavailable
a later observation changes Beacon's understanding
```

Beacon should preserve:

```text
the earlier relationship
the provenance supporting it
the later changed condition
the relationship between earlier and later representations
```

Versioning or supersession should govern material changes to Beacon's relationship representation.

---

# External Relationships

Beacon may represent relationships to external sources or objects.

The external endpoint retains:

```text
external identity
external authorship
external status
external authority
```

Beacon retains:

```text
Discovery Signal
relationship representation
Discovery Metadata
provenance
Beacon lifecycle
```

External discovery does not create Suite authority.

---

# Restricted Relationships

A relationship may be discoverable without being freely publishable.

Publication may be limited by:

```text
privacy
security
access restrictions
source restrictions
institutional governance
other legitimate constraints
```

Therefore:

```text
Discovery capability
≠
unrestricted publication authority
```

The later Publication Model will govern those boundaries.

---

# Relationship Validation

A production relationship should fail Validation or require review when:

```text
an endpoint cannot be identified

relationship meaning is ambiguous

supporting basis is absent

the relationship exceeds Beacon authority

a source-attributed relationship is represented as Beacon-owned

a Beacon determination is represented as source-owned

the relationship collapses separate canonical objects

direction contradicts the represented meaning

the relationship conflicts with known source identity

the relationship lacks sufficient provenance
```

Relationship Validation protects both semantic integrity and institutional boundaries.

---

# Conceptual Relationship Structure

A conceptual representation is:

```yaml
relationship:
  relationship_type: ""
  source_endpoint: {}
  target_endpoint: {}
  direction: ""
  attribution: {}
  supporting_reference: {}
  provenance: {}
  status: ""
```

This structure is architectural.

It is **not yet a frozen machine-readable property model**.

Exact property names, enums, cardinality, and validation constraints remain subject to later architecture and production proof.

---

# Relationship to Authority

The Authority & Reference Model establishes:

```text
who owns each endpoint
who owns each determination
what authority remains with the source
```

The Relationship Model establishes:

```text
how those independently owned endpoints connect
```

Therefore:

```text
Authority
→ ownership boundary

Relationship
→ governed connection
```

---

# Relationship to Provenance

Discovery Provenance supplies the reviewable basis supporting a represented relationship.

Conceptually:

```text
Relationship
→ says how objects connect

Provenance
→ says why Beacon can support representing that connection
```

A relationship without sufficient provenance should not pass production Validation.

---

# Relationship to Validation

Validation evaluates whether:

```text
endpoints are valid
relationship meaning is governed
direction is coherent
attribution is preserved
authority boundaries are preserved
supporting basis exists
provenance is sufficient
```

Therefore:

```text
Relationship Model
→ defines relationship conformance

Validation
→ tests that conformance
```

---

# Relationship to Schemas

The canonical Discovery Signal Schema includes:

```text
relationships
```

as an architectural component.

The Relationship Model defines the meaning of that component.

Future machine-readable schema implementation may formalize:

```text
endpoint structures
relationship types
direction
attribution
supporting references
provenance links
```

---

# Relationship to Versioning

Relationship representations may change over time.

Examples include:

```text
new relationship discovered
relationship corrected
source relationship superseded
endpoint version changed
relationship no longer current
```

The next:

```text
/beacon/versioning/
```

architecture will determine how such changes affect:

```text
signal versions
supersession
historical preservation
current representation
```

---

# Relationship to Publication

A relationship that passes Validation is not automatically publishable.

Publication may impose additional requirements involving:

```text
privacy
security
access
source restrictions
institutional sensitivity
public representation
```

Therefore:

```text
Valid Relationship
≠
Automatically Published Relationship
```

---

# Relationship to Methodology

The Relationship Model defines what a governed Beacon relationship means.

Beacon Discovery Methodology will define how Beacon:

```text
discovers relationships
evaluates them
attributes them
reviews their basis
validates them
publishes them
corrects them
maintains them over time
```

---

# What Is Now Established

The following architectural decisions are established:

```text
Relationships connect independently owned objects without merging them.

Every governed relationship requires identifiable endpoints.

Endpoint identity must be preserved.

Endpoint ownership must be preserved.

Every relationship requires explicit meaning.

Relationship direction must be preserved when semantically meaningful.

Relationships require a reviewable supporting basis.

Relationships require sufficient provenance.

Source-attributed relationships and Beacon-determined relationships must remain distinguishable.

A Discovery Signal may reference multiple canonical objects.

Multiple references do not create a composite canonical object.

Signal Type and Relationship Type are separate concepts.

A Relationship Signal is appropriate when the relationship itself is the primary discovery subject.

A Discovery Signal containing relationships is not automatically a Relationship Signal.

Version and Supersession relationships preserve institutional history.

Historical relationships should remain traceable through later changes.

External endpoints remain external.

Valid discovery does not imply unrestricted publication.
```

---

# What Remains Unfrozen

The following implementation details remain pending:

```text
exact machine-readable relationship property names
final controlled Relationship Type vocabulary
formal inverse-relationship rules
formal symmetric-relationship rules
cardinality constraints
relationship identifiers if ever institutionally necessary
relationship lifecycle or status vocabulary
relationship correction mechanics
version-specific relationship mechanics
specialized relationship requirements by Signal Type
publication restrictions for sensitive relationships
automated relationship discovery rules
```

These should be frozen only where:

```text
Versioning
Publication
Methodology
production implementation
production evidence
```

demonstrate the need.

---

# Governing Rules

Beacon relationships follow these rules:

```text
Preserve each endpoint.

Preserve each owner.

Preserve native identity.

State the relationship.

Preserve direction where meaningful.

Preserve attribution.

Preserve the supporting basis.

Preserve provenance.

Distinguish observed relationships from Beacon determinations.

Never collapse objects merely because they are connected.
```

The Relationship Model principle is:

> **Relationship connects objects. It does not merge them.**

The Suite-wide authority principle remains:

> **Reference does not transfer authority.**

---

# Current Status

As of September 5, 2026:

```text
Institution → Beacon
Suite Role → Discovery & Signals
Canonical Responsibility → Discovery Signal / Metadata
Status → Continuing Development
Phase → Phase II — Production Architecture

Discovery Signal Entry Model → Defined
Discovery Signal Types → Defined
Discovery Signal Lifecycle → Defined
Beacon Identifier Standard → Defined
Beacon Schemas → Defined
Beacon Validation → Defined
Discovery Provenance → Defined
Authority & Reference Model → Defined
Relationship Model → Defined

Versioning & Supersession → Next
First Production Discovery Signal → Not yet created
Production Proof → Pending
Operational → No
```

---

# Phase II Progress

```text
1. Discovery Signal Entry Model
   → COMPLETE

2. Discovery Signal Types
   → COMPLETE

3. Discovery Signal Lifecycle
   → COMPLETE

4. Beacon Identifier Standard
   → COMPLETE

5. Beacon Schemas
   → COMPLETE

6. Validation
   → COMPLETE

7. Discovery Provenance
   → COMPLETE

8. Authority & Reference Model
   → COMPLETE

9. Relationship Model
   → COMPLETE

10. Versioning & Supersession
    → NEXT

11. Publication Model

12. Discovery Signals Register

13. Individual Discovery Signal

14. Beacon Discovery Methodology

15. Production Model / First Operation
```

---

# Next Phase II Step

The next production-architecture page is:

```text
/beacon/versioning/
```

The **Versioning & Supersession** architecture will define how Beacon preserves canonical identity while Discovery Signals evolve, how revisions are represented, when a signal or version is superseded, and how historical institutional state remains traceable.

---

## Last Updated

September 5, 2026
