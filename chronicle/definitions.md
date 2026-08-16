# Chronicle Definitions

## Purpose

This document defines key terms used throughout Satoshium Chronicle documentation, schemas, records, procedures, and related materials.

These definitions exist to promote consistency, clarity, interoperability, and shared understanding across Chronicle.

Where a term is governed by a Suite-wide standard, Chronicle should use the Suite meaning unless Chronicle defines a narrower institutional meaning that remains compatible with the Suite architecture.

---

## Chronicle

Satoshium Chronicle is the historical-preservation institution of the Satoshium Suite.

Its purpose is to preserve qualifying historical occurrences through canonical **Chronicle Entries** while maintaining durable historical context, authoritative references, sources, evidence relationships, provenance, verification, corrections, versions, and preservation state.

Chronicle is authoritative for its own historical-preservation records.

It does not replace the authority of Certifier, Registry, Atlas, Anchor, Beacon, Attestor, Navigator, or other Suite systems.

---

## Chronicle Entry

The canonical historical-preservation object of Chronicle.

A Chronicle Entry is Chronicle's structured record representing one qualifying historical occurrence.

The occurrence is what happened.

The Chronicle Entry is Chronicle's preservation record of that occurrence.

Conceptually:

```text
Occurrence
    ↓
Preservation Eligibility
    ↓
Chronicle Entry
```

---

## Occurrence

A historical event, action, change, decision, publication, milestone, lifecycle transition, governance development, or other thing that happened.

An Occurrence exists independently of Chronicle.

Chronicle does not create the underlying occurrence.

Chronicle may preserve it through a Chronicle Entry if it satisfies Preservation Eligibility.

---

## Event

A general term for an Occurrence.

Within Chronicle architecture, Event is not a separate canonical object.

Where structured classification is required, Chronicle should use **Event Type**.

---

## Event Type

A controlled classification describing the type of Occurrence represented by a Chronicle Entry.

Event Type specializes the Chronicle Entry without creating a separate canonical object.

Examples may eventually include:

* Certification Created
* Certification Renewed
* Certification Suspended
* Certification Revoked
* Certification Expired
* Registry Milestone
* Governance Change
* Public Release
* Other approved Event Types

Final values are governed through Chronicle Controlled Values.

---

## Event-Type Profile

A structural specialization of the Chronicle Base Schema for a particular Event Type or class of Occurrences.

An Event-Type Profile may define:

* Additional required fields
* Conditional fields
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

An Event-Type Profile does not create a competing canonical Chronicle object.

---

## Preservation Eligibility

Chronicle's institutional admission rule for historical preservation.

Preservation Eligibility answers:

> Should Chronicle preserve this occurrence?

An Occurrence should not become a Chronicle Entry merely because it happened.

Eligibility may be established through:

* An approved Event Type or preservation class
* Historical Significance
* Other approved Chronicle preservation rules

Preservation Eligibility is distinct from:

* Authority
* Evidence quality
* Verification state
* Validation state
* Publication state
* Operational importance in another Suite system

---

## Historical Significance

The substantive reason an Occurrence is historically important enough to merit Chronicle preservation.

Historical Significance answers:

> Why is this occurrence worth preserving?

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

Historical Significance should not automatically be reduced to a numeric score.

---

## Record

An architectural umbrella term for structured information created, maintained, or governed within Chronicle.

Record is not a second canonical object above or beside Chronicle Entry.

Chronicle-owned records may include:

* Chronicle Entries
* Source Records
* Evidence Records
* Verification Records
* Correction Records
* Provenance Records
* Relationship Records
* Version Records
* Other supporting records justified by operational need

Chronicle may also reference authoritative records owned by other Suite systems.

Those external records do not become Chronicle-owned merely because Chronicle references them.

---

## Supporting Record

A Chronicle-owned record that performs a distinct operational function in support of Chronicle Entries.

Examples may include:

* Source Record
* Evidence Record
* Verification Record
* Correction Record
* Provenance Record
* Relationship Record
* Version Record

Supporting Records do not compete with Chronicle Entry as the canonical historical-preservation object.

---

## Source

The origin of information referenced by Chronicle.

A Source answers:

> Where did the information come from?

A Source may be:

* A webpage
* A document
* A publication
* An archive
* A database
* A public record
* An institutional record
* A repository
* A dataset
* A statement
* An interview
* An authoritative Suite object
* Another approved source type

A Source does not automatically establish truth or Chronicle authority.

---

## Source Record

A supporting Chronicle-owned record used to document the origin, attribution, temporal context, location, provenance, archival state, limitations, and relationships of a Source.

A Source Record may reference an authoritative external object without assuming ownership or authority over that object.

---

## Source Type

A controlled classification describing what a Source is.

Examples may eventually include:

* Webpage
* Document
* Publication
* Archive
* Database
* Public Record
* Institutional Record
* Repository
* Dataset
* Statement
* Interview
* Other Approved Source

Final values are governed through Chronicle Controlled Values.

---

## Source Role

A controlled classification describing how a Source functions in relation to a Chronicle Entry or Evidence Record.

Potential roles may include:

* Primary Source
* Secondary Source
* Contextual Source
* Archival Source
* Authoritative Source
* Corroborating Source
* Reference Source

Source Type and Source Role are distinct concepts.

---

## Evidence

Material that bears on a Chronicle Entry, claim, or Occurrence.

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Corroborate
* Contextualize
* Limit confidence

Evidence answers:

> What material bears on the Entry or claim?

Evidence is distinct from Source and Provenance.

---

## Evidence Record

A supporting Chronicle-owned record describing the role, origin, integrity, limitations, provenance, and relationship of Evidence associated with a Chronicle Entry or claim.

An Evidence Record does not determine institutional authority by itself.

---

## Evidence Relationship

A controlled value describing how Evidence bears on a Chronicle Entry or claim.

Potential concepts may include:

* Supports
* Challenges
* Contradicts
* Clarifies
* Corroborates
* Contextualizes
* Limits Confidence

Final values are governed through Chronicle Controlled Values.

---

## Provenance

The documented origin and movement of information, records, Sources, Evidence, or other materials into Chronicle.

Provenance answers:

> How did the information originate, move, and enter Chronicle?

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

Provenance is distinct from Source.

Source identifies origin.

Provenance documents the path.

---

## Attribution

The identification of the creator, publisher, institution, system, person, or Source responsible for originating or distributing information.

Attribution supports traceability but does not by itself establish truth, reliability, or authority.

---

## Authority

The institutional responsibility assigned to a Suite system for its own objects, actions, determinations, and lifecycle.

Examples:

* Certifier is authoritative for Certification Packages and certification determinations.
* Registry is authoritative for SREG Registry Entries and Registry lifecycle.
* Anchor is authoritative for Integrity References.
* Beacon is authoritative for Discovery Signals and Discovery Metadata.
* Attestor is authoritative for Trust Statements and attestations.
* Navigator is authoritative for Workflow Definitions and orchestration.
* Chronicle is authoritative for Chronicle Entries and Chronicle historical-preservation state.

Reference does not transfer authority.

---

## Authoritative Record

A record that derives institutional authority from the system responsible for creating or governing it.

A Chronicle Entry may reference an Authoritative Record.

Chronicle does not become authoritative for that external record merely because it preserves historical context about it.

---

## Verification

The process of reviewing Chronicle's own historical representation using available authoritative references, Sources, Evidence, Provenance, relationships, temporal information, limitations, and other review procedures.

Verification may evaluate:

* Reference existence
* Source consistency
* Evidence relationships
* Provenance completeness
* Temporal consistency
* Relationship integrity
* Internal consistency
* Known limitations

Verification does not re-adjudicate a determination owned by another Suite system.

---

## Verification State

The current structured state or result of Chronicle Verification.

Final Verification State values have not yet been formally approved.

Earlier draft values such as:

* Unverified
* Under Review
* Partially Verified
* Verified
* Disputed

should not be treated as canonical Controlled Values until formally adopted.

---

## Validation

The process of determining whether a Chronicle-owned record conforms to applicable structural and procedural requirements.

Validation may include:

* Identifier integrity
* Schema conformance
* Required fields
* Controlled Values
* Relationship rules
* Provenance requirements
* Authoritative-reference requirements
* Version linkage
* Publication readiness

Verification and Validation are separate functions.

---

## Validation State

The structured state or result of Chronicle Validation.

Final Validation State values remain to be defined through Chronicle Controlled Values and Validation rules.

---

## Correction

A documented change to a Chronicle-owned record intended to improve accuracy, clarity, context, provenance, references, relationships, or completeness.

Corrections apply to Chronicle's own record.

Chronicle does not use Corrections to modify authoritative objects owned by another Suite system.

Substantive Corrections should preserve traceable prior state or version lineage.

---

## Correction Record

A supporting Chronicle-owned record documenting a Correction.

A Correction Record may preserve:

* The affected Chronicle record
* The identified issue
* Correction type
* Prior state
* Corrected state
* Reason
* Evidence
* Authoritative references
* Provenance
* Verification
* Validation
* Prior-version linkage
* Resulting-version linkage
* Publication information

---

## Version

A preserved state within the lineage of a Chronicle-owned record.

Versioning allows substantive changes to remain traceable over time.

Record versioning is distinct from Schema Versioning.

---

## Schema Version

The version of a schema governing the structure of a Chronicle-owned record.

A record may remain governed by an older Schema Version even after a newer schema is introduced.

---

## Record Version

A preserved state of a Chronicle-owned record within its historical lineage.

A Record Version may change without changing the governing Schema Version.

---

## Historical Record

A general phrase for a preserved representation of historical information.

Within Chronicle, the precise canonical object for preserved qualifying Occurrences is the **Chronicle Entry**.

The phrase Historical Record should not be used to create a second canonical object.

---

## Historical Context

Information that helps explain the circumstances surrounding an Occurrence or Chronicle Entry.

Historical Context may include:

* Time
* Location
* Participants
* Institutional conditions
* Related Occurrences
* Related Suite objects
* Relevant Sources
* Relevant Evidence
* Later historical developments

Historical Context should remain distinguishable from authoritative facts and interpretation.

---

## Corroboration

The process of comparing multiple independent Sources, Evidence items, or records to determine whether they support a consistent historical representation.

Corroboration may strengthen confidence but does not automatically establish institutional authority or absolute truth.

---

## Authenticity

The degree to which a Source, Evidence item, record, or artifact is believed or demonstrated to be genuine and unaltered.

Authenticity may be evaluated through:

* Provenance
* Integrity information
* Signatures
* Checksums
* Chain of custody
* Corroboration
* Authoritative references

Authenticity is distinct from relevance, sufficiency, and authority.

---

## Integrity

The condition in which a Chronicle-owned record, Source reference, Evidence item, or preserved artifact remains consistent, complete, traceable, and resistant to undetected alteration.

Integrity mechanisms may include:

* Checksums
* Signatures
* Version lineage
* Provenance
* Integrity References
* Archival preservation

Integrity does not by itself establish truth or institutional authority.

---

## Preservation

The process of maintaining qualifying historical information, relationships, provenance, references, corrections, and versions so they remain available for future review and understanding.

Chronicle favors preservation over silent deletion where practical.

Preservation does not mean every activity must become a Chronicle Entry.

---

## Preservation State

The current preservation or archival condition of a Chronicle-owned record, Source, Evidence item, or referenced material.

Potential concepts may include:

* Available
* Archived
* Preserved Copy
* Referenced Only
* Unavailable
* Superseded

Final values are governed through Chronicle Controlled Values.

Preservation State is distinct from:

* Verification State
* Validation State
* Publication State
* Lifecycle State

---

## Traceability

The ability to reconstruct relationships among:

* Chronicle Entries
* Authoritative Records
* Sources
* Evidence
* Provenance
* Verification
* Validation
* Corrections
* Versions
* Publication history

Traceability supports historical continuity and reviewability.

---

## Transparency

The principle that Chronicle-owned records, references, provenance, evidence relationships, limitations, corrections, versions, and status should remain understandable and reviewable whenever practical.

Transparency does not replace institutional authority.

---

## Confidence

A contextual assessment of how strongly available information supports Chronicle's historical representation.

Confidence may change as:

* New Evidence appears
* Sources become available or unavailable
* Provenance improves
* Contradictions emerge
* Authoritative records change
* Chronicle Corrections occur

Confidence should not be confused with Validation or institutional authority.

---

## Reviewer

An individual, role, organization, system, or process responsible for reviewing Chronicle information according to an approved Chronicle procedure.

Reviewer should not be treated as a universal actor role where a more precise role is required.

Potential distinct roles may eventually include:

* Creator
* Reviewer
* Verifier
* Validator
* Approver
* Publisher

---

## Repository

A collection of Chronicle documentation, schemas, records, code, supporting materials, or archival artifacts maintained within a defined storage or publication environment.

Repository is an implementation/storage concept, not a Chronicle canonical object.

---

## Schema

A structured definition describing how a Chronicle-owned record is organized and represented.

Chronicle schema architecture centers on the **Chronicle Base Schema** for Chronicle Entry.

Supporting schemas may define Source Records, Evidence Records, Correction Records, or other operational structures where justified.

---

## Chronicle Base Schema

The common structural definition governing canonical Chronicle Entries.

The Base Schema should contain universal Entry fields only.

Specialized requirements should be added through Event-Type Profiles.

---

## Controlled Value

An approved enumerated term used in Chronicle structured records where consistency, interoperability, validation, or machine readability requires a governed vocabulary.

Potential Controlled Value domains include:

* Event Type
* Source Type
* Source Role
* Evidence Type
* Evidence Relationship
* Relationship Type
* Verification State
* Validation State
* Entry Status
* Publication State
* Correction Type
* Preservation State
* Originating System

---

## Relationship

A structured connection between a Chronicle Entry, supporting Chronicle record, Authoritative Record, or other referenced object.

Relationships may describe concepts such as:

* References
* Originated From
* Registered As
* Anchored By
* Attested By
* Precedes
* Follows
* Related To
* Superseded By
* Corrected By
* Version Of

Final relationship values are governed through Chronicle Controlled Values.

A Relationship should not imply unsupported causation or transfer institutional authority.

---

## Lifecycle

The defined sequence of institutional states or procedures through which a Chronicle-owned record progresses over time.

A Chronicle Entry lifecycle may include:

* Occurrence identified
* Preservation Eligibility assessed
* Entry drafted
* Identifier assigned
* Authoritative references established
* Sources, Evidence, and Provenance documented
* Relationships established
* Verification performed
* Validation performed
* Publication approved
* Entry published
* Entry maintained
* Correction or Versioning applied
* Historical preservation maintained

Supporting records may have different lifecycles.

Lifecycle State, Publication State, Verification State, Validation State, and Preservation State should remain distinct where they represent different institutional concepts.

---

## Publication

The institutional process by which a Chronicle-owned record is approved and made publicly available.

Publication occurs only after applicable structural, procedural, Verification, Validation, and approval requirements are satisfied.

Publication does not itself create authority over the underlying Occurrence.

---

## Publication State

The current state of a Chronicle-owned record within the publication process.

Final Publication State values remain to be defined through Chronicle Controlled Values.

---

## Retrospective Preservation

The preservation of an Occurrence after the historical event has already occurred and later context establishes Preservation Eligibility.

Retrospective Preservation must preserve the distinction between:

* Event Date
* Entry Creation Date
* Publication Date
* Correction or Version Dates

Retrospective Preservation should not rewrite the date of the underlying Occurrence.

---

## Historical Continuity

The preservation of relationships, context, provenance, correction lineage, version lineage, and temporal order across Chronicle history.

Historical Continuity allows future reviewers to understand how Satoshium developed and how Chronicle's own historical representation evolved.

---

## Timeline

A downstream historical-discovery view that organizes published Chronicle Entries chronologically.

Timeline is not a separate canonical historical object.

The Chronicle Entry remains canonical.

---

## Institutional Memory

The durable preservation of historically significant context, relationships, decisions, milestones, records, and changes needed to understand Satoshium over time.

Chronicle serves as the Suite's historical-preservation memory layer while each Suite system remains authoritative for its own objects.

---

## Guiding Principle

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

**Active pre-operational terminology specification.**

This document has been reconciled with the current Chronicle Purpose, Entries, Records, Sources, Evidence, Verification, Corrections, Schemas, Integration, Historical Preservation, Certification Events, and Status architecture.

Final Controlled Values, identifier terminology, lifecycle states, publication states, verification states, validation states, and relationship vocabulary may evolve as Chronicle operational development continues.
