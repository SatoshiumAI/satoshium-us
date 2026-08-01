# Satoshium Registry

**Structure through records. Continuity through references.**

Satoshium Registry is the authoritative public catalog of institutional records created throughout the Satoshium Suite.

Registry exists to identify, classify, catalog, reference, connect, and preserve the discoverability of authoritative records produced by Satoshium institutions. It does not replace those records, duplicate their authority, or assume ownership over the work of the institutions that created them.

Registry implements the constitutional foundations of the Satoshium Suite through:

* Satoshium Suite Standards
* Satoshium Suite Methodology
* Satoshium Suite Interoperability
* Registry-specific rules, policies, procedures, schemas, and lifecycle controls
* The canonical Satoshium Registry Entry, or SREG

---

## Institutional Position

Registry operates within the Suite-wide implementation hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Suite Interoperability
  ↓
Registry Institutional Implementation
  ↓
Satoshium Registry Entry (SREG)
```

Suite Standards define the expectations that Registry must satisfy.

Suite Methodology defines the repeatable, reviewable, and maintainable approach used to apply those expectations.

Suite Interoperability defines how Registry exchanges references with other Suite institutions while preserving clear authority boundaries.

Registry institutional implementation translates those shared foundations into Registry rules, policies, schemas, lifecycle states, procedures, identifiers, relationships, and public catalog entries.

---

## Purpose

Satoshium institutions continuously create records, resources, certifications, attestations, historical events, discovery signals, integrity references, workflow definitions, jurisdiction intelligence, and other public artifacts.

Without a structured catalog, those records may become difficult to locate, classify, understand, connect, validate, and maintain over time.

Registry exists to answer fundamental questions:

* What authoritative record exists?
* Which institution created it?
* What type of record is it?
* Where is the authoritative source located?
* What is the Registry status of the catalog entry?
* What is the status of the source record?
* Which version is current?
* How does the record relate to other Suite records?
* Can the authoritative source be found and understood later?

Registry answers these questions through structured Satoshium Registry Entries.

---

## Core Mission

The mission of Satoshium Registry is to provide the durable public catalog that connects the Satoshium Suite while preserving institutional ownership, source authority, discoverability, continuity, and long-term interoperability.

Registry organizes relationships between authoritative records.

Registry does not create the authority contained within those records.

---

## Canonical Operational Hierarchy

Registry is organized around a four-layer operational model:

```text
Satoshium Registry
  ↓
Registry Entry (SREG)
  ↓
Registry Record Type
  ↓
Authoritative Source Record
```

### Satoshium Registry

The institution responsible for the Suite's public catalog and Registry operations.

### Registry Entry (SREG)

The canonical Registry operational object.

A SREG is an independently maintained Registry record that identifies, classifies, references, and connects an authoritative source record without taking authority away from the source institution.

### Registry Record Type

The controlled classification assigned to a SREG.

Record types organize entries into defined institutional categories and determine which record-type profile, requirements, and relationships apply.

### Authoritative Source Record

The record owned and maintained by the originating institution.

Examples include:

* Certification Package
* SCRD
* Atlas canonical jurisdiction record
* Chronicle historical event
* Anchor integrity reference
* Beacon discovery signal
* Attestor trust statement
* Navigator workflow definition
* Tool or institutional publication

Registry catalogs the source record.

Registry does not replace it.

---

## Authority Boundaries

Each Satoshium institution remains authoritative for the records it creates.

Registry is authoritative only for Registry-owned information, including:

* SREG identifiers
* Registry classifications
* Registry record types
* Registry lifecycle states
* Registry status
* Registry relationships
* Registry versions
* Registry corrections
* Registry publication history
* Registry catalog presentation

The originating institution remains authoritative for:

* source-record content
* source-record status
* source-record version
* certification outcomes
* attestations
* historical events
* integrity references
* discovery signals
* jurisdiction intelligence
* workflow definitions

An SREG may report or reference those source-controlled values, but Registry does not redefine them.

---

## Registry Scope

The initial operational Registry supports SREGs for:

* Tool Records
* Jurisdiction Records
* Media Records
* Certification Records
* Attestation Records
* Signal Records

Registry may also support additional controlled record types where those types are defined, documented, schema-compatible, and approved through Registry governance.

Potential additional types include:

* Historical Records
* Integrity Reference Records
* Discovery Records
* Workflow Records
* Schema Records
* Policy Records
* Governance Records
* Preservation Records

New record types must extend the Registry model without weakening existing identifiers, authority boundaries, interoperability, or schema compatibility.

---

## Registry Method

Registry applies Suite Methodology Principles through a repeatable institutional process:

```text
Identify or Receive Source Record
  ↓
Confirm Source Institution and Authority
  ↓
Determine Registrability
  ↓
Assign Registry Record Type
  ↓
Assign Registry Identifier
  ↓
Create Source and Relationship References
  ↓
Construct SREG
  ↓
Validate Schema and Terminology
  ↓
Publish
  ↓
Maintain Lifecycle, Versions, Corrections, and Archival Continuity
```

This method is separate from the certification workflow.

Certifier determines certification outcomes.

Registry determines whether and how an authoritative record is cataloged.

---

## Satoshium Registry Entry

The SREG is Registry's canonical operational object.

Every SREG should preserve, at minimum, the following conceptual information:

* Registry identifier
* Registry record type
* title or recognized name
* source institution
* authoritative source record
* source-record identifier
* source-record version
* source-record status
* Registry status
* Registry lifecycle state
* Registry entry version
* applicable schema version
* public references
* relationships
* registration date
* last updated date
* correction history
* supersession information
* archival information

The final machine-readable schema defines the authoritative field names, validation requirements, permitted values, and structural rules.

---

## Registry Identifiers

Every SREG must receive a stable Registry identifier.

A Registry identifier identifies the SREG itself.

It does not replace:

* a Certification Identifier
* a Certification Package identifier
* an SCRD identifier
* an Atlas resource identifier
* an attestation identifier
* a source-system identifier
* a source-record identifier

Registry identifiers must remain stable, unique within Registry, publicly referenceable, and preserved through the lifecycle of the SREG.

---

## Registry Record Types

Each SREG belongs to one primary Registry Record Type.

Record types support:

* classification
* schema application
* discoverability
* relationship mapping
* validation
* controlled expansion
* cross-system interoperability

A record type describes the kind of authoritative source record being cataloged.

A record type does not determine the authority of that source record.

---

## Registry Status and Source Status

Registry Status and source-record status are separate.

For example:

```text
Certification Outcome: Certified
Certification Status: Active
Registry Status: Active
```

A certification may later become revoked while its SREG remains publicly available as an active historical catalog entry that accurately reports the source status as revoked.

Registry therefore preserves both:

* the current institutional condition of the SREG; and
* the reported or referenced condition of the authoritative source record.

---

## Registry Lifecycle

A SREG may move through defined Registry lifecycle states.

Core states include:

* Pending Registration
* Registered
* Active
* Updated
* Superseded
* Revoked
* Archived

These states are not necessarily a single mandatory linear sequence.

Permitted transitions depend on the reason for change, the condition of the SREG, and the condition of the authoritative source record.

### Pending Registration

The proposed entry has been identified but has not yet been formally entered into Registry.

### Registered

The SREG has been created and assigned a Registry identifier.

### Active

The SREG is the current discoverable Registry representation of the referenced source record.

### Updated

The SREG has been revised to reflect corrected references, additional relationships, metadata improvements, source changes, or Registry-maintained changes.

### Superseded

The SREG or a specific SREG version has been replaced by a newer entry or version while remaining preserved for continuity.

### Revoked

The SREG has been withdrawn from active Registry recognition because of invalidation, material error, loss of source authority, reversal, or another documented reason.

### Archived

The SREG is no longer in active operational use but remains preserved as part of Registry history.

Archived does not mean deleted.

---

## Versions

Registry distinguishes among multiple version layers:

* Suite Standards version
* Suite Methodology version
* Registry specification version
* SREG schema version
* record-type profile version
* individual SREG version
* source-record version

These versions must not be treated as interchangeable.

A source record may change without the SREG schema changing.

A SREG may be corrected without the source record changing.

A schema may evolve while older SREGs remain preserved under their original schema version.

---

## Corrections

Registry corrections apply to Registry-owned information.

Corrections may address:

* identifiers
* titles
* classifications
* references
* relationships
* dates
* version metadata
* source locations
* Registry status
* formatting
* structural errors
* schema compliance

Corrections should preserve continuity and transparency.

Major corrections should document what changed, why it changed, when it changed, and which version superseded the earlier version.

Registry must not silently rewrite the content or authority of a source record.

If the source record changes, Registry should update its reference and reported metadata while preserving the distinction between the source change and the Registry update.

---

## Schemas

Registry schemas implement the Satoshium Suite Schema Standard.

The schema architecture consists of:

```text
Suite Schema Standard
  ↓
Registry Schema Specification
  ↓
SREG Base Schema
  ↓
Record-Type Profiles
  ↓
Published SREG JSON Records
```

### Registry Schema Specification

Defines Registry-wide structure, terminology, identifiers, metadata rules, validation expectations, versioning, and compatibility.

### SREG Base Schema

Defines the common fields required across Registry entries.

### Record-Type Profiles

Define additional requirements for Tool, Jurisdiction, Media, Certification, Attestation, Signal, and other supported record types.

### Published SREG Records

Provide machine-readable instances of Registry entries.

Registry schemas should support:

* human readability
* machine readability
* stable identifiers
* controlled terminology
* validation
* schema evolution
* version preservation
* relationship mapping
* cross-system references
* long-term interoperability

---

## Policies

Registry policies define how Registry requirements are implemented.

Policies may govern:

* registrability
* identifier assignment
* record classification
* source-authority confirmation
* source-reference validation
* schema validation
* relationship creation
* publication
* versioning
* corrections
* supersession
* revocation
* archival
* record-type extension
* governance
* interoperability

Registry Rules define institutional expectations.

Registry Policies define implementation requirements.

Registry Procedures define the repeatable operational steps used to carry out those requirements.

---

## Relationship to the Satoshium Suite

Registry operates as one institution within the broader Satoshium Suite.

Each institution retains a distinct responsibility and canonical object.

### Atlas

Creates jurisdiction intelligence, canonical jurisdiction records, evidence resources, and machine-readable Atlas packages.

### Certifier

Evaluates subjects and creates certifications, including the canonical Certification Package and related artifacts such as the SCPR, SCR, and SCRD.

### Registry

Creates SREGs that catalog authoritative institutional records and preserve their discoverability and relationships.

### Chronicle

Creates and preserves historical events and institutional chronology.

### Anchor

Creates and preserves integrity references, hashes, timestamps, signatures, and durable verification points.

### Beacon

Creates discovery signals and discovery metadata that help records be found, interpreted, and distributed.

### Attestor

Creates trust statements, attestations, validations, and supporting verification references.

### Navigator

Creates workflow definitions and coordinates cross-system operational activity.

---

## Interoperability

Registry follows the Suite Interoperability model:

* each institution owns its own canonical object;
* each institution preserves its own responsibility;
* systems reference authoritative records instead of replacing them;
* shared identifiers and schemas support cross-system understanding;
* public relationships remain traceable;
* interoperability does not merge institutional authority.

Example certification relationship:

```text
Atlas Resource
  ↓
Certifier Evaluation
  ↓
Certification Package
  ↓
SCRD
  ↓
SREG
```

The Certification Package remains Certifier's canonical certification object.

The SCRD remains Certifier's canonical certified record.

The SREG remains Registry's canonical catalog entry.

---

## Evidence and Trust References

Registry may catalog or preserve references to evidence, attestations, trust statements, integrity references, and verification locations.

Registry does not independently evaluate certification evidence or issue trust determinations merely by cataloging them.

Registry validation is limited to Registry responsibilities, such as:

* confirming that the referenced source exists;
* confirming the source institution;
* confirming the source identifier;
* confirming that the entry is classifiable;
* confirming schema compliance;
* confirming that references and relationships are structurally valid.

Certifier evaluates certification evidence.

Attestor creates attestations and trust statements.

Anchor preserves integrity references.

Registry catalogs the resulting authoritative records and their relationships.

---

## Repository Structure

The Registry repository should support both institutional documentation and operational publication.

```text
registry/
├── README.md
├── REGISTRY.md
├── PURPOSE.md
├── SCOPE.md
├── STATUS.md
├── DEFINITIONS.md
├── RECORD-TYPES.md
├── REGISTRY-RULES.md
├── CHANGELOG.md
├── schemas/
│   ├── sreg.schema.json
│   └── record-types/
├── policies/
├── procedures/
├── records/
├── examples/
├── docs/
└── assets/
```

Directory names and publication paths may evolve through documented Registry governance, but the separation between institutional documentation, schemas, policies, procedures, records, examples, and assets should remain clear.

---

## Documentation

Core Registry documentation includes:

* `README.md`
* `REGISTRY.md`
* `PURPOSE.md`
* `SCOPE.md`
* `STATUS.md`
* `DEFINITIONS.md`
* `RECORD-TYPES.md`
* `REGISTRY-RULES.md`
* `CHANGELOG.md`

Operational implementation may also include:

* Registry Schema Specification
* SREG Base Schema
* Record-Type Profiles
* Registry Policies
* Registry Procedures
* Identifier Specification
* Lifecycle Specification
* Relationship Specification
* Interoperability Mapping
* Published SREG records
* Human-readable Registry entry pages

---

## Current Status

**Development Cycle:** August 2026  
**Institutional Condition:** Operational Development and Publication  
**Foundation:** Constitutionally reconciled with Suite Standards, Suite Methodology, and Suite Interoperability

The July Registry architecture established the institutional foundation.

The August development cycle transforms that foundation into a complete operational Registry implementation.

Current priorities include:

* finalizing the SREG specification;
* completing Registry record types;
* publishing Registry schemas;
* completing Registry policies and procedures;
* implementing identifiers;
* implementing lifecycle transitions;
* implementing versions and corrections;
* implementing relationships;
* publishing machine-readable Registry artifacts;
* creating initial SREG records;
* completing cross-institutional interoperability;
* preparing Registry for operational completion.

The objective is for Registry to stand beside Atlas and Certifier as a completed operational institution within the Satoshium Suite.

---

## Guiding Principles

Registry is governed by the following institutional principles:

* Authority remains with the originating institution.
* Registry catalogs rather than replaces.
* SREG is Registry's canonical operational object.
* Every SREG references an authoritative source record.
* Registry identifiers identify Registry entries.
* Record types are controlled classifications.
* Registry status is separate from source status.
* Registry corrections apply to Registry-owned information.
* Versions must remain distinguishable.
* References should remain durable.
* Relationships should remain traceable.
* Schemas should remain machine-readable and human-understandable.
* Historical continuity should be preserved.
* Interoperability should strengthen institutional separation.
* Documentation should replace assumption.
* Preservation should not erase provenance.

---

## Disclaimer

Satoshium Registry is an informational public-record and catalog framework.

A SREG documents Registry identifiers, classifications, references, relationships, versions, lifecycle information, and status metadata based on authoritative source records and available information at the time of registration or update.

A Registry Entry does not by itself create:

* ownership
* legal rights
* certification
* attestation
* verification
* source authority
* intellectual-property rights
* financial standing
* regulatory approval
* historical truth

Those forms of authority remain with the applicable originating institution, source record, governing authority, or responsible external system.

---

## Guiding Statement

> Institutions create authoritative records.
>
> Registry creates the path back to them.
>
> SREG preserves identity, classification, relationships, and continuity.
>
> The source retains authority.
>
> The Registry preserves discovery.
