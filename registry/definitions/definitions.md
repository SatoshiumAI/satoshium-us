# Satoshium Registry Definitions

This document defines the controlled institutional terminology used throughout Satoshium Registry.

These definitions support consistent human-readable documentation, machine-readable schemas, Registry policies, lifecycle controls, interoperability, and long-term preservation across the Satoshium Suite.

Where a Registry term overlaps with a Suite-wide term, the Satoshium Suite Standards and Terminology Standard govern. Registry definitions provide the institution-specific implementation of those shared terms.

---

# Satoshium Registry

**Satoshium Registry** is the authoritative public catalog of institutional records created throughout the Satoshium Suite.

Registry identifies, classifies, references, connects, and preserves the discoverability of authoritative source records.

Registry does not replace source records or inherit the authority of the institutions that created them.

Registry is authoritative for Registry-owned information, including SREG identifiers, Registry classifications, Registry status, Registry lifecycle states, Registry relationships, Registry versions, and Registry corrections.

---

# Registry Institution

The **Registry Institution** is the Satoshium Suite institution responsible for operating and maintaining Satoshium Registry.

Its responsibilities include:

- creating and maintaining SREGs;
- assigning Registry identifiers;
- managing Registry record types;
- validating Registry schemas;
- preserving Registry relationships;
- maintaining Registry lifecycle and version history;
- publishing Registry records;
- preserving Registry continuity.

The Registry Institution does not assume ownership of authoritative source records.

---

# Satoshium Registry Entry

A **Satoshium Registry Entry**, abbreviated **SREG**, is the canonical operational object of Satoshium Registry.

A SREG is an independently maintained Registry record that identifies, classifies, references, and connects an authoritative source record.

A SREG may include:

- Registry identifier;
- Registry record type;
- title;
- source institution;
- source-record identifier;
- source-record version;
- source-record status;
- Registry status;
- Registry lifecycle state;
- Registry entry version;
- schema version;
- public references;
- relationships;
- registration date;
- update date;
- correction history;
- supersession information;
- archival information.

A SREG does not replace the authoritative source record.

---

# Registry Record

A **Registry Record** is a general term for information formally maintained by Registry.

In operational use, the canonical Registry Record is the SREG.

The term should not be used to imply that Registry owns the authoritative source record being cataloged.

---

# Registry Entry

A **Registry Entry** is the human-readable or machine-readable published representation of a SREG.

A Registry Entry may be presented as:

- an HTML page;
- a JSON record;
- a structured data file;
- an API response;
- a catalog listing;
- another approved Registry publication format.

The underlying operational object remains the SREG.

---

# Authoritative Source Record

An **Authoritative Source Record** is the record created, owned, and maintained by the originating institution.

Examples include:

- Certification Package;
- SCRD;
- Atlas canonical jurisdiction record;
- Chronicle historical event;
- Anchor integrity reference;
- Beacon discovery signal;
- Attestor trust statement;
- Navigator workflow definition;
- tool publication;
- media resource.

Registry catalogs the Authoritative Source Record through a SREG.

The originating institution remains authoritative for its content, status, version, and meaning.

---

# Source Institution

A **Source Institution** is the institution that creates and maintains the Authoritative Source Record referenced by a SREG.

Examples include:

- Atlas;
- Certifier;
- Chronicle;
- Anchor;
- Beacon;
- Attestor;
- Navigator;
- another recognized Satoshium Suite institution.

The Source Institution retains authority over the Source Record.

---

# Source-System Identifier

A **Source-System Identifier** is an identifier assigned by the originating institution to its own record.

A Source-System Identifier is distinct from a Registry Identifier.

Examples include:

- Certification Identifier;
- Certification Package identifier;
- SCRD identifier;
- Atlas resource identifier;
- attestation identifier;
- Chronicle event identifier.

A SREG should preserve the Source-System Identifier whenever one exists.

---

# Registry Identifier

A **Registry Identifier** is a stable and unique value assigned by Registry to a SREG.

The Registry Identifier identifies the SREG itself.

It does not replace or redefine the Source-System Identifier.

A Registry Identifier should remain:

- unique within Registry;
- stable over time;
- publicly referenceable;
- preserved through correction, supersession, revocation, and archival.

---

# Registry Record Type

A **Registry Record Type** is the controlled primary classification assigned to a SREG.

Record Types organize SREGs according to the kind of Authoritative Source Record being cataloged.

Initial supported Record Types include:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal.

Additional types may be added through documented Registry governance.

---

# Record-Type Profile

A **Record-Type Profile** is a Registry schema extension that defines additional requirements for a specific Registry Record Type.

A Record-Type Profile supplements the SREG Base Schema.

It does not replace the common SREG structure.

---

# Classification

**Classification** is the Registry process of assigning a SREG to a defined Registry Record Type and, where applicable, additional controlled subtypes or classifications.

Classification supports:

- organization;
- discoverability;
- validation;
- schema application;
- relationship mapping;
- interoperability.

Classification does not create source authority.

---

# Category

A **Category** is a broad organizational grouping used for public navigation, presentation, or descriptive organization.

A Category may correspond to a Registry Record Type, but the terms are not always interchangeable.

Registry Record Type is the controlled operational classification.

Category may be used as a broader public-facing organizational label.

---

# Registrability

**Registrability** is the condition of being eligible for inclusion in Registry.

A record may be registrable when:

- an identifiable source record exists;
- a source institution can be identified;
- the source has sufficient authority or provenance;
- the record fits an approved Registry Record Type;
- required references are available;
- the SREG can satisfy applicable schema and policy requirements.

Registrability does not imply certification, endorsement, or approval.

---

# Registration

**Registration** is the formal Registry action through which a SREG is created, assigned a Registry Identifier, validated, and entered into the public catalog.

Registration applies to the SREG.

It does not transfer ownership of the Authoritative Source Record.

---

# Reference

A **Reference** is a structured connection from a SREG to another resource.

A Reference may identify:

- an Authoritative Source Record;
- a public webpage;
- a repository;
- a schema;
- a report;
- a certification artifact;
- an evidence resource;
- an integrity reference;
- a historical record;
- an external resource.

References should be durable, attributable, and understandable.

---

# Source Reference

A **Source Reference** is the Registry-maintained reference that identifies the Authoritative Source Record cataloged by a SREG.

The Source Reference should preserve enough information to locate and distinguish the source record over time.

---

# Public Reference

A **Public Reference** is a publicly accessible location or identifier through which a SREG or Source Record may be discovered.

A Public Reference may include:

- canonical URL;
- repository location;
- public record page;
- machine-readable file;
- API endpoint;
- persistent identifier.

---

# Relationship

A **Relationship** is a structured connection between a SREG and another Registry Entry, Source Record, institution, schema, event, integrity reference, signal, attestation, or related object.

Relationships should use controlled relationship types where possible.

---

# Cross-Reference

A **Cross-Reference** is a relationship connecting two or more SREGs or related Registry objects.

Cross-References support navigation, context, provenance, and interoperability.

---

# Relationship Type

A **Relationship Type** is a controlled term defining the meaning of a relationship.

Examples may include:

- references;
- derived from;
- certified by;
- attested by;
- anchored by;
- supersedes;
- superseded by;
- related to;
- generated from;
- discovered through;
- archived with.

Relationship Types should be defined consistently across Registry schemas and documentation.

---

# Schema

A **Schema** is a formal definition of the structure, fields, value types, constraints, and validation rules applicable to a Registry object.

Registry schemas implement the Satoshium Suite Schema Standard.

---

# Registry Schema Specification

The **Registry Schema Specification** defines Registry-wide requirements for:

- SREG structure;
- identifiers;
- required fields;
- controlled terminology;
- relationships;
- lifecycle values;
- status values;
- versions;
- validation;
- compatibility;
- schema evolution.

---

# SREG Base Schema

The **SREG Base Schema** defines the common machine-readable structure required for all SREGs.

Record-Type Profiles extend the SREG Base Schema with type-specific requirements.

---

# Metadata

**Metadata** is structured descriptive information associated with a SREG or Source Record.

Registry Metadata may include:

- identifier;
- title;
- record type;
- source institution;
- source identifier;
- source status;
- Registry status;
- lifecycle state;
- version;
- dates;
- references;
- relationships;
- schema version;
- correction history.

Registry Metadata should distinguish between Registry-owned values and source-reported values.

---

# Registry-Owned Metadata

**Registry-Owned Metadata** is information created and maintained by Registry.

Examples include:

- Registry Identifier;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- Registry relationships;
- Registry correction history;
- Registry publication dates.

---

# Source-Reported Metadata

**Source-Reported Metadata** is information obtained from or attributed to the Source Institution.

Examples include:

- Source-System Identifier;
- source title;
- source version;
- source status;
- certification outcome;
- attestation result;
- source publication date.

Registry may catalog Source-Reported Metadata but does not redefine it.

---

# Registry Status

**Registry Status** describes the current institutional condition of a SREG within Registry.

Registry Status is distinct from:

- Certification Status;
- Certification Outcome;
- Attestation Status;
- source-record status;
- Source Institution status.

Registry Status values must be defined through Registry policy and schema.

---

# Source-Record Status

**Source-Record Status** describes the current condition of the Authoritative Source Record as determined by the Source Institution.

Registry may report or reference this status but does not control it.

---

# Lifecycle State

A **Lifecycle State** describes the operational stage of a SREG within Registry.

Initial lifecycle states include:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

Lifecycle states are not necessarily a single mandatory linear sequence.

---

# Pending Registration

**Pending Registration** is the state in which a proposed Registry Entry has been identified but has not yet been formally registered.

---

# Registered

**Registered** is the state in which a SREG has been created and assigned a Registry Identifier.

---

# Active

**Active** is the state in which a SREG is the current discoverable Registry representation of its referenced Source Record.

---

# Updated

**Updated** is the state or event indicating that Registry-owned information associated with a SREG has been revised.

An update may reflect:

- corrected references;
- new relationships;
- changed source metadata;
- improved classification;
- structural correction;
- schema migration.

---

# Superseded

**Superseded** describes a SREG or SREG version that has been replaced by a newer entry or version while remaining preserved for continuity.

---

# Revoked

**Revoked** describes a SREG withdrawn from active Registry recognition because of material error, invalidation, loss of source authority, reversal, or another documented reason.

Revocation does not require deletion.

---

# Archived

**Archived** describes a SREG no longer in active operational use but preserved as part of Registry history.

Archived does not mean deleted.

---

# Version

A **Version** is a formally identified state of a document, schema, record, profile, or Source Record.

Registry distinguishes among:

- Suite Standards version;
- Suite Methodology version;
- Registry specification version;
- SREG schema version;
- Record-Type Profile version;
- individual SREG version;
- Source-Record version.

These version layers are not interchangeable.

---

# Registry Entry Version

A **Registry Entry Version** identifies a particular published state of a SREG.

A new Registry Entry Version may be created when Registry-owned information changes materially.

---

# Source-Record Version

A **Source-Record Version** identifies a particular version of the Authoritative Source Record as determined by the Source Institution.

A Source-Record Version may change without changing the SREG schema version.

---

# Schema Version

A **Schema Version** identifies the formal version of the schema used to validate a Registry object.

Older SREGs may remain preserved under earlier schema versions.

---

# Correction

A **Correction** is a documented change to Registry-owned information intended to improve accuracy, consistency, structure, or compliance.

Corrections may address:

- identifiers;
- titles;
- classifications;
- references;
- relationships;
- dates;
- versions;
- status values;
- formatting;
- schema compliance.

Registry corrections do not rewrite Source Record authority.

---

# Correction History

**Correction History** is the preserved record of material corrections made to a SREG.

Correction History should identify:

- what changed;
- why it changed;
- when it changed;
- which version was affected;
- which version replaced it.

---

# Supersession

**Supersession** is the formal replacement of a SREG or SREG version by a newer Registry object while preserving the earlier object for continuity.

---

# Revocation Record

A **Revocation Record** is the documented Registry explanation for withdrawing a SREG from active recognition.

It should preserve the reason, date, authority, affected version, and resulting lifecycle condition.

---

# Archival Record

An **Archival Record** is the preserved documentation associated with moving a SREG into archival status.

It should preserve discoverability, historical context, and prior relationships.

---

# Historical Reference

A **Historical Reference** is a structured connection to a prior record, version, event, milestone, correction, supersession, revocation, or archival action.

Historical References support continuity over time.

---

# Preservation

**Preservation** is the practice of maintaining Registry records, references, relationships, versions, and historical context for future discovery and review.

Preservation does not require Registry to duplicate every Source Record.

Registry may preserve the path, identity, metadata, relationships, integrity references, and historical record necessary to locate and understand the authoritative source.

---

# Discoverability

**Discoverability** is the ability to locate, identify, distinguish, and understand a Registry Entry or referenced Source Record efficiently.

Registry supports discoverability through:

- stable identifiers;
- controlled Record Types;
- structured metadata;
- public references;
- relationships;
- machine-readable schemas;
- human-readable pages;
- preserved history.

---

# Continuity

**Continuity** is the preservation of identity, relationships, versions, references, provenance, and historical context across time.

Continuity is a primary Registry objective.

---

# Provenance

**Provenance** is the documented origin and history of a SREG or Source Record.

Provenance may include:

- Source Institution;
- Source-System Identifier;
- creation date;
- publication history;
- version history;
- correction history;
- supersession history;
- related evidence or integrity references.

---

# Authority

**Authority** is the institutional responsibility to create, maintain, interpret, and control a record or value.

Registry authority applies to Registry-owned objects and metadata.

Source authority remains with the originating institution.

---

# Institutional Separation

**Institutional Separation** is the principle that each Satoshium Suite institution retains responsibility for its own canonical objects, processes, and authority.

Interoperability should connect institutions without merging their responsibilities.

---

# Interoperability

**Interoperability** is the ability of Registry to exchange, reference, interpret, and preserve relationships with other Satoshium Suite institutions while maintaining institutional separation.

Registry interoperability may involve:

- Atlas;
- Certifier;
- Chronicle;
- Anchor;
- Beacon;
- Attestor;
- Navigator;
- future Suite institutions.

---

# Canonical Object

A **Canonical Object** is the primary authoritative operational object created by an institution.

Examples include:

- Certifier → Certification Package;
- Registry → SREG;
- Chronicle → Historical Event;
- Anchor → Integrity Reference;
- Beacon → Discovery Signal;
- Attestor → Trust Statement;
- Navigator → Workflow Definition.

A canonical object remains owned by the institution that creates it.

---

# Certification Package

A **Certification Package** is Certifier's canonical certification object.

Registry may catalog a Certification Package through a SREG.

Registry does not become authoritative for the certification by cataloging it.

---

# SCRD

An **SCRD** is a Certifier-owned structured certified record associated with a Certification Package.

Registry may reference an SCRD as a Source Record or related certification artifact.

---

# Atlas Resource

An **Atlas Resource** is an Atlas-owned jurisdiction intelligence record, package, manifest, evidence resource, or related machine-readable artifact.

Registry may catalog Atlas Resources through Jurisdiction or other applicable SREG types.

---

# Historical Event

A **Historical Event** is Chronicle's canonical object for preserving a significant occurrence, milestone, transition, or institutional event.

Registry may catalog or relate to Historical Events without replacing Chronicle authority.

---

# Integrity Reference

An **Integrity Reference** is an Anchor-owned record that preserves hashes, timestamps, signatures, or other durable verification points.

Registry may reference Integrity References within a SREG.

---

# Discovery Signal

A **Discovery Signal** is a Beacon-owned object that supports discovery, distribution, visibility, or contextual understanding.

Registry may catalog or relate to Discovery Signals.

---

# Trust Statement

A **Trust Statement** is an Attestor-owned object expressing an attestation, validation, trust assertion, or supporting verification statement.

Registry may catalog Trust Statements through Attestation SREGs.

---

# Workflow Definition

A **Workflow Definition** is a Navigator-owned object describing or coordinating a repeatable operational process across one or more Suite institutions.

Registry may catalog Workflow Definitions through an applicable SREG type.

---

# Validation

**Validation** is the process of determining whether a Registry object satisfies applicable Registry schema, terminology, policy, and structural requirements.

Registry validation may confirm:

- required fields;
- identifier format;
- source reference;
- Source Institution;
- Record Type;
- relationship structure;
- permitted values;
- schema compliance.

Registry validation does not constitute certification or attestation.

---

# Verification

**Verification** is the process of confirming a claim, record, identity, integrity reference, or other assertion through an appropriate authority or method.

Registry does not provide verification merely by cataloging a record.

---

# Certification

**Certification** is the formal outcome of evaluation performed by Certifier under applicable Suite Standards and Methodology.

Registry does not certify records.

---

# Attestation

**Attestation** is a statement or assertion created by Attestor or another recognized attesting authority.

Registry may catalog attestations but does not create attestation authority through registration alone.

---

# Policy

A **Registry Policy** defines implementation requirements governing Registry operations.

Policies may address:

- registrability;
- identifier assignment;
- classification;
- source validation;
- publication;
- lifecycle;
- versioning;
- corrections;
- revocation;
- archival;
- interoperability.

---

# Procedure

A **Registry Procedure** defines the repeatable operational steps used to implement a Registry Policy.

Procedures should be documented, reviewable, and reproducible.

---

# Registry Rule

A **Registry Rule** defines an institution-specific operating expectation subordinate to Satoshium Suite Standards.

Registry Rules establish what Registry must preserve or require.

Policies and Procedures define how those Rules are implemented.

---

# Governance

**Governance** is the documented process through which Registry rules, policies, schemas, Record Types, procedures, and institutional changes are reviewed, approved, versioned, and preserved.

---

# Publication

**Publication** is the formal release of a Registry object or document through an approved public Registry location or format.

Publication may include human-readable and machine-readable artifacts.

---

# Registry Principle

Registry exists to preserve the public path back to authoritative records.

Its central principle is:

> The source retains authority.
>
> Registry preserves identity, classification, relationships, and discovery.
