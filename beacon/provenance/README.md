# Satoshium Beacon — Discovery Provenance

## Overview

**Discovery Provenance** defines how Satoshium Beacon preserves the evidentiary path behind a Beacon-owned **Discovery Signal**.

It establishes how Beacon documents:

```text
where the signal came from
what was observed
when it was observed
how the information was encountered
what source or authoritative object supports the discovery
```

Beacon's canonical production object remains:

```text
Discovery Signal
```

with canonical identifier:

```text
BEAC-YYYY-NNNN
```

Provenance makes that object reviewable.

It does not make Beacon the source, transfer source authority to Beacon, or independently establish truth, verification, certification, integrity, or trust.

The Suite-wide governing principle remains:

> **Reference does not transfer authority.**

---

# Purpose

Discovery Provenance answers four foundational questions:

```text
Where did this signal come from?

What exactly was observed?

When was it observed?

What source or authoritative object supports it?
```

A Beacon Discovery Signal should not require a reviewer to accept an unexplained discovery assertion.

Its path back to the supporting source should remain visible.

---

# Institutional Principle

The core provenance relationship is:

```text
Signal
→ attributable observation

Observation
→ traceable source

Source
→ preserved identity

Supporting basis
→ reviewable
```

Conceptually:

```text
Source / Authoritative Object
        ↓
Observation
        ↓
Discovery Context
        ↓
Beacon Discovery Signal
        ↓
Preserved Provenance
```

The goal is reconstructability.

A later reviewer should be able to understand the basis on which Beacon created the Discovery Signal.

---

# Provenance Requirements

Every production Discovery Signal requires a sufficient provenance basis.

The core architectural concerns are:

```text
Source Identity
Observed Information
Observation Time
Observation Method
Observation Context
Supporting Basis
```

Additional provenance information may include:

```text
Discovery Actor
Workflow Reference
Re-Observation
Indirect Source Lineage
```

when relevant.

---

# 1. Source Identity

Provenance begins with an attributable source.

Expected source information includes:

```text
source name
source kind
source institution when applicable
source-native identifier when available
source object type when relevant
reviewable source location when available
```

Beacon should preserve the source's own identity.

It should not create a replacement Beacon identity merely because Beacon references the source.

Examples of institution-owned source identifiers include:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
```

A Beacon Discovery Signal referring to one of these objects retains its own separate identity:

```text
BEAC-2026-0001
```

---

# 2. Observed Information

Provenance must preserve enough information to understand what Beacon actually observed.

The observation may concern:

```text
fact
state
change
relationship
record
event
publication
other relevant information
```

The provenance record should preserve:

```text
the observed information
relevant source context
observed source status when material
the specific object, portion, event, or condition supporting the discovery when practical
```

The observation should not silently expand beyond what the source supports.

Conceptually:

```text
Observed:
A source changed from State A to State B.

Not automatically established:
Every broader conclusion that might be inferred from that change.
```

Provenance documents the observation.

Interpretation must remain distinguishable from the observed basis.

---

# 3. Observation Time

Beacon must preserve when the underlying information was observed.

The primary architectural timestamp is:

```text
observed_at
```

Observation time is distinct from:

```text
source publication time
canonical Discovery Signal creation time
Beacon publication time
later re-observation time
```

These temporal meanings must not be silently substituted for one another.

---

# Temporal Provenance

The architectural distinctions are:

```text
source_published_at
→ when the source says the source was published

observed_at
→ when Beacon observed the information

created_at
→ when the canonical Discovery Signal was created

published_at
→ when the Beacon Discovery Signal was publicly published

last_observed_at
→ the most recent governed re-observation when applicable
```

Therefore:

```text
Source Time
≠
Observation Time
≠
Creation Time
≠
Publication Time
```

These timestamps may sometimes coincide.

Their meanings remain separate even when their values are identical.

---

# 4. Observation Method

Provenance should preserve how Beacon encountered the information.

Potential architectural methods include:

```text
Manual Review
Search
Index Lookup
Relationship Mapping
Cross-System Discovery
Navigator-Directed Workflow
Other attributable discovery process
```

These are architectural examples.

The final controlled Observation Method vocabulary remains subject to:

```text
Beacon Discovery Methodology
production implementation
production proof
```

The purpose of the field is reproducibility and transparency, not technological detail for its own sake.

---

# 5. Observation Context

Observation Context explains why and under what discovery circumstances Beacon observed the source.

Relevant context may include:

```text
discovery objective
search context
review context
workflow context
jurisdiction
domain
query reference
investigation reference
other material discovery circumstances
```

Context should make the observation understandable.

It should not turn every discovery activity into a separate canonical Beacon object.

---

# 6. Supporting Basis

Provenance must identify a reviewable basis supporting the Discovery Signal.

The supporting basis may include:

```text
canonical source identifier
Source Reference
public source location
repository location
supporting canonical object
supporting publication
other attributable reference
```

The objective is reviewability.

To the extent the source permits, another reviewer should be able to locate and examine the basis Beacon relied upon.

---

# Source vs. Provenance

Source and Provenance are related but not interchangeable.

## Source

Source answers:

> **What information source or canonical object is being referenced?**

## Provenance

Provenance answers:

> **How did Beacon encounter, observe, attribute, and preserve the discovery from that source?**

Conceptually:

```text
Source
→ identity and origin

Provenance
→ discovery lineage
```

The Source Reference Schema supports the source component.

Discovery Provenance governs the lineage surrounding that source.

---

# Canonical Suite Sources

Beacon may preserve provenance to canonical objects owned by other Satoshium Suite institutions.

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
→ Workflow Definition / Orchestration reference
```

Beacon may discover, reference, and preserve provenance to these objects.

Beacon does not acquire their institutional authority.

---

# External Sources

Beacon may also discover information outside the Satoshium Suite.

Examples include:

```text
government records
research publications
public datasets
institutional publications
public documents
other attributable sources
```

An external source remains external.

Discovery does not convert it into:

```text
a Suite institution
a Suite canonical object
Beacon-owned authority
```

Beacon's responsibility is to preserve the source relationship accurately.

---

# Canonical Reference Preservation

When provenance depends upon another Suite canonical object, Beacon should preserve that object's native institutional identity.

Example:

```text
Beacon Discovery Signal
BEAC-2026-0001

        ↓ supported by / references

Anchor Integrity Reference
ANCH-2026-0001
```

The identifiers have separate meanings.

```text
BEAC-2026-0001
→ identifies the Beacon Discovery Signal

ANCH-2026-0001
→ identifies the Anchor Integrity Reference
```

Neither identifier absorbs the other.

---

# Direct Provenance

**Direct Provenance** exists when Beacon observes the relevant source or authoritative object itself.

Conceptually:

```text
Source Object
        ↓
directly observed by Beacon
        ↓
Observation
        ↓
Discovery Signal
```

Direct observation is preferable when the authoritative or original source is reasonably available.

Direct provenance does not mean Beacon owns the source.

It means Beacon's observation path reaches the represented source directly.

---

# Indirect Provenance

**Indirect Provenance** exists when Beacon encounters information through an intermediary.

Conceptually:

```text
Original / Authoritative Source
        ↓
referenced by
        ↓
Intermediary Source
        ↓
observed by Beacon
        ↓
Discovery Signal
```

When provenance is indirect:

```text
the intermediary should remain visible
the source Beacon actually observed should remain visible
the upstream source should remain separately attributable when known
```

Beacon should not represent indirect observation as direct observation.

---

# Provenance Depth

Beacon should preserve enough provenance depth to support meaningful review.

It should not imply that every information lineage can always be reconstructed indefinitely.

The minimum architectural objective is:

```text
Identify the source Beacon actually observed.

And, when materially available:

Identify the authoritative or original object on which that source relies.
```

Provenance depth may differ by:

```text
Signal Type
source type
availability
workflow
production requirements
```

Exact depth requirements remain subject to Beacon Discovery Methodology and production proof.

---

# Discovery Actor

When institutionally relevant, provenance may preserve the actor or process responsible for the discovery.

Examples include:

```text
human reviewer
Beacon process
Navigator-directed workflow
other governed process
```

Actor attribution may support:

```text
accountability
reproducibility
review
audit
```

However, actor information should be preserved only to the degree justified by:

```text
institutional need
privacy
security
accountability
```

The final actor-identity rules remain unfrozen.

---

# Workflow Provenance

When Navigator orchestrates the discovery workflow, Beacon may preserve a Navigator workflow reference.

Conceptually:

```text
Navigator
→ Workflow Definition / Orchestration

Beacon
→ Discovery Observation / Discovery Signal

Provenance
→ preserves the connection
```

Beacon should reference the Navigator workflow rather than duplicate or redefine it.

Navigator retains workflow authority.

---

# Re-Observation

A source may be observed again after the original Discovery Signal is created.

A later observation may:

```text
confirm that the source remains available
confirm that the observed condition remains present
identify changed information
identify a changed source status
support an update
support supersession
support resolution
```

Re-observation does not automatically rewrite the original observation.

---

# Preserve Historical Basis

Beacon should preserve:

```text
what was observed originally
when it was observed
what supported that observation
what is observed later
how the later observation relates to the earlier one
```

Conceptually:

```text
Original Observation
→ preserved

Later Observation
→ separately preserved

Relationship
→ documented
```

This protects the historical basis of the Discovery Signal.

---

# Source Changes

A source may later:

```text
change
move
be superseded
be withdrawn
become unavailable
be archived
disappear
```

Those later conditions should not rewrite what Beacon observed earlier.

Beacon should, to the extent possible:

```text
preserve the original provenance
record later observations separately
preserve source-native supersession when attributable
preserve later availability information
avoid deleting historical provenance merely because the source changed
```

---

# Provenance and Verification

Provenance does not equal verification.

```text
Provenance
→ Where did the assertion come from?

Verification
→ What has a governed verification process established about it?
```

A source can be perfectly attributable and still contain incorrect information.

Therefore:

> **A well-provenanced false statement remains false.**

Provenance makes the origin reviewable.

It does not make the assertion true.

---

# Provenance and Trust

Provenance does not equal trust.

Beacon owns:

```text
Discovery Signal / Metadata
```

Attestor owns:

```text
Trust Statement
```

Therefore:

```text
Beacon
→ preserves discovery lineage

Attestor
→ produces Trust Statements
```

Traceability may inform later trust processes.

It is not itself a Trust Statement.

---

# Provenance and Certification

Provenance also does not equal certification.

If Beacon references:

```text
SC-CERT-2026-0001
```

the certification authority remains with Certifier.

Beacon may preserve:

```text
the identifier
the source institution
the object type
the observation
the relationship
```

Beacon does not recertify the object by referencing it.

---

# Provenance and Integrity

If Beacon references:

```text
ANCH-2026-0001
```

the Integrity Reference remains owned by Anchor.

Beacon's provenance may establish that:

```text
Beacon observed ANCH-2026-0001
```

It does not mean:

```text
Beacon performed Anchor Verification
```

---

# Minimum Provenance Gate

A Draft Discovery Signal should not pass Beacon Validation without sufficient provenance.

The minimum architectural gate is:

```text
Source identified
+
Observation described
+
Observation time preserved
+
Observation method preserved
+
Observation context sufficient
+
Supporting basis reviewable
=
Minimum Provenance Conformance
```

Validation consumes these provenance requirements.

---

# Conceptual Provenance Structure

A conceptual representation is:

```yaml
provenance:
  observed_source: {}
  observed_information: {}
  observed_at: ""
  observation_method: ""
  observation_context: {}
  supporting_reference: {}
  discovery_actor: {}
  workflow_reference: {}
```

This structure is architectural.

It is **not yet a frozen JSON property model**.

Exact machine-readable implementation remains subject to Schema refinement, Validation, and production proof.

---

# Relationship to Discovery Signal Schema

The canonical Discovery Signal Schema contains a Provenance component.

Conceptually:

```text
Discovery Signal Schema
→ represents provenance

Discovery Provenance Architecture
→ defines what provenance means
```

The two layers must remain aligned.

---

# Relationship to Validation

Provenance is a required Beacon Validation concern.

Conceptually:

```text
Discovery Provenance
→ defines the lineage requirements

Validation
→ confirms that required provenance is present and conformant
```

A Discovery Signal without sufficient provenance should not become Active.

---

# Relationship to Lifecycle

Provenance begins during the creation of the canonical Discovery Signal and remains relevant throughout its lifecycle.

Conceptually:

```text
Created
↓
Draft
↓
Provenance reviewed
↓
Validation
↓
Active
↓
Possible re-observation
↓
Update / Supersession / Resolution
```

Later lifecycle changes should preserve earlier provenance.

---

# Relationship to Versioning

Later versions may reflect new observations or corrected provenance.

Versioning must not silently overwrite the provenance basis of prior institutional history.

The later:

```text
/beacon/versioning/
```

architecture will define those mechanics.

---

# Relationship to Relationships

A Discovery Signal may assert or preserve a relationship.

Provenance should support the basis for that relationship.

The later:

```text
/beacon/relationships/
```

architecture will define the controlled Relationship Model.

Provenance should allow a reviewer to understand why Beacon represented the relationship.

---

# Relationship to Publication

Publication should not erase provenance.

A public Discovery Signal should retain sufficient source attribution and provenance for review, subject to legitimate:

```text
privacy
security
access
source restriction
```

constraints.

The later Publication Model will define the public-release rules.

---

# Relationship to Methodology

Discovery Provenance defines what lineage Beacon must preserve.

Beacon Discovery Methodology will define how that lineage is collected, reviewed, documented, and maintained.

```text
Provenance Architecture
→ what must be preserved

Methodology
→ how Beacon preserves it
```

---

# What Is Now Established

The following architectural decisions are established:

```text
Every production Discovery Signal requires a reviewable provenance basis.

Source identity must remain attributable.

Beacon must preserve what was actually observed.

Observation time is distinct from source publication, signal creation, and Beacon publication time.

Observation Method is a provenance concern.

Observation Context is a provenance concern.

A reviewable Supporting Basis is required.

Direct and Indirect Provenance must remain distinguishable.

Beacon should preserve the source it actually observed.

When materially available, Beacon should also preserve the authoritative or original source behind an intermediary.

Later source changes must not erase historical provenance.

Re-observation must not silently rewrite the original observation.

Provenance is required for Validation.

Provenance does not equal verification.

Provenance does not equal certification.

Provenance does not equal integrity verification.

Provenance does not equal trust.

Provenance does not establish truth.
```

---

# What Remains Unfrozen

The following implementation details remain pending:

```text
exact machine-readable provenance property names
controlled Observation Method vocabulary
minimum provenance depth by Signal Type
required citation or source-location formats
Discovery Actor privacy rules
Workflow Reference syntax
re-observation schema mechanics
unavailable-source preservation mechanics
provenance correction mechanics
automated provenance-capture requirements
whether cryptographic evidence becomes part of a provenance profile
```

These should be resolved only when later architecture or production evidence demonstrates the institutional need.

---

# Authority Boundary

Beacon's provenance responsibility is:

```text
prove where its signal came from
preserve what was observed
preserve when it was observed
preserve the supporting basis
preserve source identity
```

Beacon does not:

```text
become the source
inherit source authority
recertify a Certification Package
reregister an SREG
recreate a Chronicle Entry
perform Anchor Verification
create an Attestor Trust Statement
redefine a Navigator workflow
```

The governing principle remains:

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

Production Provenance Capture → Pending
Machine Provenance Enforcement → Pending
First Production Discovery Signal → Not yet created
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
   → NEXT

9. Relationship Model

10. Versioning & Supersession

11. Publication Model

12. Discovery Signals Register

13. Individual Discovery Signal

14. Beacon Discovery Methodology

15. Production Model / First Operation
```

---

# Governing Provenance Principles

Beacon Discovery Provenance follows these principles:

```text
Preserve the source.

Preserve what was observed.

Preserve when it was observed.

Preserve how it was observed.

Preserve why the observation occurred.

Preserve the supporting basis.

Distinguish direct from indirect observation.

Preserve historical lineage when sources change.

Do not confuse traceability with truth.

Do not convert attribution into authority.
```

The Discovery Provenance reflection is:

> **A discovery becomes reviewable when its path back to the source remains visible.**

The Suite-wide authority principle remains:

> **Reference does not transfer authority.**

---

# Next Phase II Step

The next production-architecture page is:

```text
/beacon/authority/
```

Its purpose is to define Beacon's **Authority & Reference Model**:

```text
what Beacon owns
what Beacon may reference
what authority remains with the source institution
how canonical references are represented
what Beacon must never claim by virtue of discovery alone
```

---

## Last Updated

September 5, 2026
