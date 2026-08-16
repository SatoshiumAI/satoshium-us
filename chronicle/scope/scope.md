# Chronicle Scope

## Purpose

This document defines the intended institutional and operational scope of Satoshium Chronicle.

Chronicle exists to preserve **qualifying historical occurrences** through canonical **Chronicle Entries** while maintaining the context, authoritative references, Sources, Evidence relationships, Provenance, Verification, Corrections, Versions, and historical continuity needed for future review.

The purpose of Scope is to establish clear boundaries around:

* What Chronicle is responsible for
* What Chronicle may preserve
* What Chronicle may reference
* What belongs to another Suite system
* What Chronicle explicitly does not do

Scope should remain consistent with the Satoshium Suite Standards, Methodology, Schemas Standard, Evidence Standard, and Interoperability architecture.

---

## Canonical Scope Principle

Chronicle has one canonical historical-preservation object:

> Chronicle Entry

The Occurrence is what happened.

The Chronicle Entry is Chronicle's structured historical-preservation record representing that qualifying Occurrence.

Conceptually:

```text
Occurrence
    ↓
Preservation Eligibility
    ↓
Chronicle Entry
```

Chronicle should not create competing canonical objects for events, publications, milestones, decisions, observations, or similar historical subjects.

Those concepts should be represented through Event Type classifications and, where necessary, Event-Type Profiles.

---

## In Scope

Chronicle may support the following functions.

### Preservation Eligibility

Determining whether an Occurrence qualifies for Chronicle preservation.

Preservation Eligibility asks:

> Should Chronicle preserve this occurrence?

Eligibility may be established through:

* An approved Event Type or preservation class
* Historical Significance
* Other approved Chronicle preservation rules

Chronicle is selective by design.

Not every Suite action, record, status change, or operational event belongs in Chronicle.

---

### Chronicle Entries

Creating and maintaining canonical Chronicle Entries that represent qualifying historical Occurrences.

A Chronicle Entry may preserve:

* Historical context
* Temporal information
* Originating system
* Authoritative references
* Sources
* Evidence relationships
* Provenance
* Relationships
* Verification state
* Validation state
* Correction lineage
* Version lineage
* Publication state
* Preservation state

---

### Historical Significance

Documenting why an Occurrence is important enough to preserve when Historical Significance forms part of the Preservation Eligibility basis.

Potential significance factors may include:

* Institutional change
* Lifecycle significance
* First or last occurrence
* Major milestone
* Governance change
* Material architectural change
* Relationship significance
* Evidentiary or interpretive importance
* Historical continuity value

---

### Source Attribution

Documenting where information originated.

Chronicle may maintain Source Records that preserve:

* Creator
* Publisher
* Source Type
* Source Role
* Creation date
* Publication date
* Access date
* Capture date
* Source location
* Archive references
* Limitations
* Provenance
* Preservation state

A Source Record supports Chronicle Entries.

It does not become a second canonical historical object.

---

### Evidence Context

Maintaining structured Evidence Records and Evidence relationships where appropriate.

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Corroborate
* Contextualize
* Limit confidence

Chronicle may preserve Evidence relationships without treating all Evidence as authoritative.

---

### Provenance

Documenting how information, Sources, Evidence, authoritative records, or other materials originated, moved, and entered Chronicle.

Provenance may include:

* Originating institution
* Source path
* Acquisition method
* Access method
* Capture method
* Transfer history
* Archive path
* Preservation history
* Related authoritative record

Provenance is distinct from Source and Evidence.

---

### Verification

Reviewing Chronicle's own historical representation.

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

### Validation

Determining whether a Chronicle-owned record conforms to applicable structural and procedural requirements.

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

---

### Corrections

Documenting changes to Chronicle-owned records.

Corrections may address:

* Factual errors
* Metadata defects
* Source errors
* Evidence updates
* Provenance issues
* Relationship errors
* Clarifications
* Other documented defects

Substantive Corrections should preserve prior state and version lineage.

Chronicle does not use Corrections to modify authoritative records owned by another Suite system.

---

### Historical Relationships

Maintaining structured relationships among:

* Chronicle Entries
* Source Records
* Evidence Records
* Correction Records
* Verification Records
* Provenance structures
* Versions
* Authoritative Suite objects

Relationships should use Controlled Values where direction or meaning matters.

Relationships should not imply unsupported causation or transfer institutional authority.

---

### Versioning

Preserving material prior states of Chronicle-owned records.

Versioning may apply to:

* Chronicle Entries
* Source Records
* Evidence Records
* Correction Records
* Other Chronicle supporting records

Record Versioning is distinct from Schema Versioning.

---

### Publication

Publishing validated Chronicle-owned records according to approved Publication procedures.

Publication does not create authority over the underlying Occurrence.

Publication State should remain distinct from Lifecycle State, Verification State, Validation State, and Preservation State.

---

### Historical Preservation

Maintaining Chronicle Entries and supporting context so future reviewers can understand:

* What happened
* When it happened
* Which authority established it
* Which Sources existed
* Which Evidence was available
* How information entered Chronicle
* How the Occurrence related to other history
* How Chronicle's own representation evolved

---

### Retrospective Preservation

Preserving an Occurrence after it happened when later context establishes Preservation Eligibility.

Retrospective preservation should preserve the distinction between:

* Event Date
* Entry Creation Date
* Publication Date
* Correction or Version Dates

Chronicle should never rewrite the date of the underlying Occurrence merely because preservation happened later.

---

### Historical Discovery

Supporting public discovery of published Chronicle Entries.

The `/chronicle/entries/` collection is intended to serve as the public production index for Chronicle Entries.

A future Timeline may organize published Entries chronologically.

Timeline remains downstream of Chronicle Entries.

---

### Long-Term Preservation

Supporting durable retention of Chronicle-owned records and references across time.

Future implementations may use:

* Repositories
* Archives
* Databases
* Static artifacts
* Distributed storage
* Cryptographic integrity mechanisms
* Integrity anchoring

Technology may evolve.

Chronicle's canonical object and preservation mission should remain stable.

---

## In-Scope Occurrence Classes

Chronicle may preserve qualifying Occurrences involving:

### Certification

Examples may include:

* Certification Created
* Certification Renewed
* Certification Suspended
* Certification Revoked
* Certification Expired
* Other approved certification milestones

Certifier remains authoritative for the Certification Package and certification lifecycle.

### Registry

Examples may include:

* Initial registration
* Material Registry lifecycle changes
* Major catalog milestones
* Significant relationship changes

Registry remains authoritative for SREG Registry Entries and Registry lifecycle.

### Anchor

Qualifying Anchor milestones or historical events associated with Integrity References.

### Beacon

Qualifying Discovery Signal or Discovery Metadata milestones.

### Attestor

Qualifying Trust Statement or attestation milestones.

### Navigator

Qualifying Workflow Definition or orchestration milestones.

### Atlas

Historically significant developments involving Atlas source intelligence, jurisdiction data, evidence, metadata, or other Atlas records.

### Governance and Institutional Development

Examples may include:

* Major governance changes
* Material standards changes
* Public launches
* Institutional milestones
* Firsts
* Lasts
* Major architectural transitions

The final Event Type vocabulary should be governed through Chronicle Controlled Values.

---

## Out of Scope

Chronicle is not intended to perform the following functions.

### Universal Activity Logging

Chronicle does not preserve every action, event, record, system process, validation run, metadata change, or administrative update.

Routine activity may be operationally important without being historically preservable.

Conceptually:

> Logs preserve activity.  
> Chronicle preserves history.

---

### Determine Universal or Absolute Truth

Chronicle does not establish universal truth.

It preserves its own structured historical representation and the context needed for future review.

---

### Replace Institutional Authority

Chronicle does not replace the authority of other Suite systems.

For example:

* Certifier remains authoritative for Certification Packages and certification determinations.
* Registry remains authoritative for SREG Registry Entries and Registry lifecycle.
* Anchor remains authoritative for Integrity References.
* Beacon remains authoritative for Discovery Signals and Discovery Metadata.
* Attestor remains authoritative for Trust Statements and attestations.
* Navigator remains authoritative for Workflow Definitions and orchestration.
* Atlas remains authoritative for its own source intelligence, jurisdiction data, evidence, metadata, and related records.

Chronicle remains authoritative for Chronicle Entries and Chronicle historical-preservation state.

---

### Correct External Authoritative Objects

Chronicle does not modify:

* Certification Packages
* SREG Registry Entries
* Integrity References
* Discovery Signals
* Trust Statements
* Workflow Definitions
* Atlas records
* Other external authoritative objects

If an originating system changes its own authoritative object, Chronicle may preserve the later Occurrence and update its own references.

---

### Function as a Certification System

Chronicle does not:

* Certify subjects
* Make certification determinations
* Establish certification status
* Replace Certification Packages

Those functions belong to Certifier.

---

### Function as a Registry

Chronicle does not:

* Create SREG Registry Entries
* Control Registry lifecycle
* Replace Registry catalog authority
* Act as the authoritative catalog for Suite records

Those functions belong to Registry.

---

### Function as an Attestation System

Chronicle does not issue Trust Statements merely by preserving an Occurrence.

Attestation authority belongs to Attestor.

---

### Function as an Anchoring System

Chronicle does not create Integrity References merely by recording that an anchor occurred.

Anchoring authority belongs to Anchor.

---

### Function as a Discovery-Signal System

Chronicle does not create Discovery Signals merely by preserving discovery-related history.

Discovery-signal authority belongs to Beacon.

---

### Function as a Workflow Orchestrator

Chronicle does not define or execute Workflow Definitions merely by preserving workflow history.

Workflow orchestration belongs to Navigator.

---

### Replace Atlas Source Intelligence

Chronicle may reference Atlas records and may preserve qualifying Atlas-related Occurrences.

It does not replace Atlas source intelligence, jurisdiction data, Evidence, metadata, or other Atlas responsibilities.

---

### Replace Human Historical Interpretation

Chronicle preserves structured historical context.

Researchers, reviewers, historians, readers, and future systems may interpret that history differently.

Chronicle should preserve the record without claiming exclusive interpretive authority.

---

### Moderate Opinion

Chronicle may preserve conflicting, disputed, or differing viewpoints where they are historically relevant.

Chronicle does not exist to resolve every disagreement or suppress noncanonical opinion.

---

### Guarantee Perpetual Availability

Chronicle seeks durable preservation.

It cannot guarantee that every external Source, Evidence item, archive, service, repository, or third-party dependency will remain permanently available.

Chronicle should preserve durable references, metadata, provenance, archival context, and limitations when direct preservation is not possible.

---

### Automatically Publish All Evidence or Sources

Not every Source or Evidence item should necessarily be publicly published.

Legal, privacy, licensing, security, contractual, or operational restrictions may affect publication.

Chronicle may preserve structured references or metadata without publicly reproducing the underlying material.

---

## Relationship to Other Systems

Chronicle participates in reference-based Suite interoperability.

### Certifier

Certifier remains authoritative for:

* Certification evaluation
* Certification determinations
* Certification lifecycle actions
* Certification status
* Certification Packages

Chronicle may preserve qualifying certification Occurrences through Chronicle Entries that reference the authoritative Certification Package.

### Registry

Registry remains authoritative for:

* SREG Registry Entries
* Registration
* Cataloging
* Registry metadata
* Registry relationships
* Registry lifecycle state

Chronicle may preserve qualifying Registry Occurrences or reference SREGs.

### Atlas

Atlas remains authoritative for its own source intelligence, jurisdiction data, evidence, metadata, and related records.

### Anchor

Anchor remains authoritative for Integrity References.

### Beacon

Beacon remains authoritative for Discovery Signals and Discovery Metadata.

### Attestor

Attestor remains authoritative for Trust Statements and attestations.

### Navigator

Navigator remains authoritative for Workflow Definitions and orchestration.

### Chronicle

Chronicle remains authoritative for:

* Chronicle Entry identity
* Chronicle historical context
* Chronicle provenance
* Chronicle relationships
* Chronicle verification state
* Chronicle correction lineage
* Chronicle version lineage
* Chronicle publication state
* Chronicle preservation state

Reference does not transfer authority.

---

## Scope and Interoperability

Chronicle may reference authoritative objects from other Suite systems.

That reference may support:

* Historical context
* Provenance
* Evidence
* Verification
* Relationships
* Preservation Eligibility
* Event-Type-specific requirements

A referenced object does not become Chronicle-owned.

Chronicle should not duplicate the external object's internal schema unless an approved interoperability requirement specifically calls for a mapped representation.

---

## Scope and Evidence

Evidence preservation does not mean Chronicle must possess or publish every original artifact.

Where appropriate and permitted, Chronicle may preserve:

* Original material
* Archival copies
* Checksums
* Signature references
* Metadata
* Archive references
* Provenance
* Integrity notes
* Evidence relationships
* Limitations

Where direct preservation is not appropriate or possible, durable reference and preservation metadata may be sufficient.

---

## Scope and Preservation Eligibility

Preservation Eligibility is the principal institutional boundary that prevents Chronicle from becoming an unlimited historical dumping ground.

A record or event may be:

* Operationally important
* Evidentially strong
* Publicly visible
* Technically valid

and still not belong in Chronicle if it does not satisfy Preservation Eligibility.

Likewise, an historically significant Occurrence may qualify for preservation even if Evidence remains incomplete or disputed, provided Chronicle records those limitations transparently and follows applicable rules.

---

## Future Scope

Future Chronicle development may expand within the established preservation mission.

Potential capabilities may include:

* Additional Event-Type Profiles
* Machine-readable Chronicle Entries
* Public historical archives
* Public Timeline discovery
* Cross-Suite historical relationships
* Automated Validation
* Automated reference checking
* Expanded Provenance tracking
* Cryptographic integrity verification
* Integrity anchoring
* Long-term archival systems
* Distributed preservation mechanisms

Future expansion should preserve:

* Chronicle Entry as the canonical object
* Preservation Eligibility
* Clear Suite authority boundaries
* Reference-based interoperability
* Version-aware historical preservation

---

## Scope Summary

Chronicle preserves qualifying historical Occurrences through Chronicle Entries.

It may preserve or reference:

* Sources
* Evidence
* Provenance
* Authoritative Suite objects
* Verification
* Validation
* Corrections
* Versions
* Relationships
* Publication and preservation state

Chronicle does not preserve every activity.

It does not replace the authority of the systems it references.

It does not become Certifier, Registry, Anchor, Beacon, Attestor, Navigator, or Atlas.

Its institutional responsibility is narrower and clearer:

> Preserve qualifying historical memory in a structured, transparent, traceable, and Suite-aligned form.

---

## Guiding Principle

Chronicle answers:

> What happened?

> When did it happen?

> Which authority established it?

> Which Sources existed?

> Which Evidence was available?

> How did the information enter Chronicle?

> How did the Occurrence relate to other history?

> How did Chronicle's own Entry change over time?

Chronicle does not answer:

> What must everyone believe?

Conceptually:

> Events happen.  
> Suite systems establish authority.  
> Chronicle preserves qualifying historical memory.

---

## Status

**Active pre-operational scope specification.**

This document has been reconciled with the current Chronicle Purpose, Entries, Records, Sources, Evidence, Verification, Corrections, Schemas, Integration, Certification Events, Historical Preservation, Definitions, FAQ, and Status architecture.

Final Event Types, Controlled Values, identifiers, relationship vocabulary, lifecycle states, validation requirements, publication requirements, and Event-Type Profiles may evolve as Chronicle operational development continues.
