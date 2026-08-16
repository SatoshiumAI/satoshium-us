# Chronicle FAQ

## What is Chronicle?

Satoshium Chronicle is the historical-preservation institution of the Satoshium Suite.

It exists to preserve qualifying historical occurrences through canonical **Chronicle Entries** while maintaining the context, provenance, evidence relationships, authoritative references, corrections, versions, and historical continuity needed for future review.

Chronicle does not preserve every activity or operational record.

---

## Why does Chronicle exist?

Information, context, and institutional memory can become fragmented, altered, hidden, unavailable, or difficult to interpret over time.

Chronicle exists to preserve historically significant context so future reviewers can understand:

* What happened
* When it happened
* Which authority established it
* Which Sources existed
* Which Evidence was available
* How the information entered Chronicle
* How the occurrence related to other history
* How Chronicle's own record changed over time

---

## Does Chronicle determine truth?

No.

Chronicle does not claim universal or absolute truth authority.

Chronicle preserves its own structured historical representation of qualifying occurrences.

Verification may review Chronicle's representation using Sources, Evidence, Provenance, authoritative references, temporal information, and relationships.

Other Suite systems remain authoritative for their own objects and determinations.

---

## What is a Chronicle Entry?

A **Chronicle Entry** is the canonical historical-preservation object of Chronicle.

The Occurrence is what happened.

The Chronicle Entry is Chronicle's structured preservation record representing that qualifying Occurrence.

Conceptually:

```text
Occurrence
    ↓
Preservation Eligibility
    ↓
Chronicle Entry
```

Chronicle does not create separate canonical objects for events, publications, milestones, decisions, or observations.

Those are represented through Event Type classifications and, where needed, Event-Type Profiles.

---

## What is an Occurrence?

An Occurrence is a historical event, action, change, decision, publication, milestone, lifecycle transition, governance development, or other thing that happened.

Occurrences exist independently of Chronicle.

Chronicle may preserve an Occurrence through a Chronicle Entry if it satisfies Preservation Eligibility.

---

## What is Preservation Eligibility?

Preservation Eligibility is Chronicle's admission rule for historical preservation.

It asks:

> Should Chronicle preserve this occurrence?

An Occurrence does not become a Chronicle Entry merely because it happened.

Eligibility may be established through:

* An approved Event Type or preservation class
* Historical Significance
* Other approved Chronicle preservation rules

---

## What is Historical Significance?

Historical Significance explains why an Occurrence is important enough to preserve.

Potential factors may include:

* Institutional change
* Lifecycle significance
* First or last occurrence
* Major milestone
* Governance change
* Material architectural change
* Relationship significance
* Evidentiary or interpretive importance
* Historical continuity value

Historical Significance is one possible basis for Preservation Eligibility.

---

## What is the difference between a Source, Evidence, and Provenance?

These concepts are related but distinct.

A **Source** answers:

> Where did the information come from?

**Evidence** answers:

> What material bears on the Chronicle Entry or claim?

Evidence may support, challenge, contradict, clarify, corroborate, contextualize, or limit confidence.

**Provenance** answers:

> How did the information or Evidence originate, move, and enter Chronicle?

In simple terms:

```text
Source     = Where information came from
Evidence   = What bears on the Entry or claim
Provenance = How the information got here
```

---

## What is Verification?

Verification is Chronicle's review of its own historical representation.

Verification may examine:

* Authoritative references
* Source consistency
* Evidence relationships
* Provenance
* Temporal consistency
* Relationship integrity
* Known limitations
* Internal consistency

Verification does not re-adjudicate a determination owned by another Suite system.

---

## What is Validation?

Validation determines whether a Chronicle-owned record conforms to applicable structural and procedural requirements.

Validation may include:

* Identifier integrity
* Schema conformance
* Required fields
* Controlled Values
* Relationship rules
* Provenance requirements
* Version linkage
* Publication readiness

Verification and Validation are separate functions.

```text
Verification ≠ Validation
```

---

## What are Corrections?

Corrections are documented changes to Chronicle-owned records.

They may address:

* Factual errors
* Metadata defects
* Provenance issues
* Relationship errors
* Evidence updates
* Reference errors
* Clarifications
* Other documented problems

Chronicle Corrections do not alter authoritative records owned by another Suite system.

---

## Why preserve corrections?

Historical transparency improves when reviewers can reconstruct how Chronicle's own record changed over time.

Chronicle favors visible, version-aware corrections over silent overwriting.

Where appropriate:

* Prior states remain preserved
* Correction rationale remains visible
* Resulting versions remain linked
* Historical relationships remain traceable

---

## What types of occurrences can Chronicle preserve?

Chronicle may preserve qualifying Occurrences involving:

* Certification lifecycle events
* Registry milestones
* Governance changes
* Public releases
* Anchor events
* Attestation events
* Beacon events
* Navigator workflow milestones
* Atlas-related developments
* Institutional milestones
* Other approved Event Types

Chronicle does not automatically preserve every occurrence.

Preservation Eligibility applies first.

---

## Can Chronicle preserve conflicting information?

Yes.

Historical records may contain uncertainty, disagreement, conflicting sources, disputed evidence, or incomplete provenance.

Chronicle may preserve those limitations transparently.

Conflicting information does not automatically disqualify an Occurrence from preservation.

---

## Is Chronicle a database?

Not necessarily.

Chronicle is a historical-preservation institution and framework.

Its implementation may use:

* Databases
* Repositories
* Static records
* Archives
* Distributed storage
* Other technologies

The technology may change.

The canonical object and institutional function should remain stable.

---

## Is Chronicle a certification system?

No.

Certification authority belongs to **Certifier**.

Chronicle may preserve qualifying historical occurrences related to certification, but it does not create or replace the authoritative Certification Package.

---

## Is Chronicle a registry?

No.

Registration and catalog authority belong to **Registry**.

Chronicle may preserve qualifying Registry-related occurrences or reference SREG Registry Entries, but it does not replace Registry.

---

## How does Chronicle relate to Certifier?

Certifier remains authoritative for:

* Certification evaluation
* Certification determinations
* Certification lifecycle actions
* Certification status
* Certification Packages

Chronicle may preserve a qualifying certification occurrence by creating a Chronicle Entry that references the authoritative Certification Package.

Conceptually:

```text
Certifier → Certification Package
Chronicle → Chronicle Entry preserving a qualifying certification occurrence
```

---

## How does Chronicle relate to Registry?

Registry remains authoritative for:

* SREG Registry Entries
* Registration
* Cataloging
* Registry metadata
* Registry relationships
* Registry lifecycle state

Chronicle may reference Registry records and may preserve qualifying Registry milestones through Chronicle Entries.

Reference does not transfer authority.

---

## How does Chronicle relate to the rest of the Suite?

Chronicle may reference authoritative objects from:

* Atlas
* Certifier
* Registry
* Anchor
* Beacon
* Attestor
* Navigator

Each system remains authoritative for its own objects and responsibilities.

Chronicle preserves qualifying historical memory across those systems without absorbing their authority.

---

## What is an Event-Type Profile?

An Event-Type Profile is a specialization of the Chronicle Base Schema for a particular class of Occurrence.

It may define:

* Additional required fields
* Required authoritative references
* Relationship rules
* Evidence expectations
* Provenance requirements
* Verification requirements
* Validation requirements

Conceptually:

```text
Chronicle Base Schema + Event-Type Profile = Specialized Chronicle Entry
```

The first anticipated operational profile is the Certification Event-Type Profile.

---

## Can Verification results change?

Yes.

New Evidence, improved Provenance, new Sources, changed authoritative records, or better context may justify a new Verification State.

If Chronicle's own record changes materially, that change should remain traceable through correction or version lineage.

---

## Does Chronicle preserve deleted or unavailable information?

Not always.

Chronicle may not possess or be permitted to preserve every original artifact.

Where direct preservation is not possible, Chronicle may still preserve:

* Durable references
* Metadata
* Provenance
* Archive references
* Integrity information
* Preservation notes
* Historical relationships

A Source becoming unavailable does not automatically erase its historical role.

---

## Does a Chronicle Entry prove an event happened?

Not by itself.

A Chronicle Entry is Chronicle's historical-preservation record.

Its strength depends on:

* Authoritative references
* Sources
* Evidence
* Provenance
* Verification
* Known limitations
* Structural Validation

A Chronicle Entry should not be confused with certification, attestation, legal proof, or universal historical authority.

---

## Can Chronicle preserve history retrospectively?

Yes.

Historical importance may become clear only later.

Chronicle may preserve an Occurrence retrospectively when later context establishes Preservation Eligibility.

When this happens, Chronicle should distinguish:

* Event Date
* Entry Creation Date
* Publication Date
* Correction or Version Dates

Chronicle should not rewrite the original date of the Occurrence.

---

## Is Timeline the historical record?

No.

Timeline is intended to be a downstream discovery view of published Chronicle Entries.

The Chronicle Entry remains canonical.

Timeline is for chronological navigation and discovery, not a separate record system.

---

## What is Chronicle's long-term goal?

The long-term goal is to create a durable historical-preservation institution capable of maintaining Satoshium history across changing technologies, systems, organizations, and generations.

Future capabilities may include:

* Public historical archives
* Machine-readable Chronicle Entries
* Event-Type Profiles
* Public Timeline discovery
* Cross-Suite historical linking
* Automated Validation
* Cryptographic integrity verification
* Version-aware archival preservation
* Long-term Provenance retention
* Integrity anchoring where appropriate

---

## Is Chronicle operational now?

No.

Chronicle is currently in:

```text
Pre-Operational Architecture & Implementation Preparation
```

Its architectural foundation is substantially established, but production identifiers, Controlled Values, Validation rules, publication procedures, production procedures, and the first canonical production Chronicle Entry are still being completed.

September 2026 is intended as the operational-development cycle, not a guaranteed public launch date.

---

## What must happen before Chronicle is production operational?

Chronicle should not be considered operational until a qualifying Occurrence can move through the full institutional process.

Conceptually:

```text
Occurrence Identified
        ↓
Preservation Eligibility
        ↓
Chronicle Entry
        ↓
Authoritative References
Sources
Evidence
Provenance
Relationships
        ↓
Verification
        ↓
Validation
        ↓
Publication
        ↓
Maintenance / Versioning
        ↓
Historical Preservation
```

The first production Chronicle Entry should demonstrate that this process works coherently.

---

## What is Chronicle's guiding principle?

Chronicle seeks to preserve:

* What happened
* When it happened
* Which authority established it
* Which Sources existed
* Which Evidence was available
* How information entered Chronicle
* How the Occurrence related to other history
* How Chronicle's own Entry changed over time

The objective is not universal certainty.

The objective is durable, transparent, traceable, institutionally bounded historical preservation.

Conceptually:

> Events happen.  
> Suite systems establish authority.  
> Chronicle preserves qualifying historical memory.

---

## Status

**Active pre-operational FAQ.**

This FAQ has been reconciled with the current Chronicle Purpose, Entries, Records, Sources, Evidence, Verification, Corrections, Schemas, Integration, Certification Events, Historical Preservation, Definitions, and Status architecture.

Final Controlled Values, identifier terminology, lifecycle states, publication states, verification states, validation states, and relationship vocabulary may evolve as Chronicle operational development continues.
