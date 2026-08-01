# Satoshium Registry Changelog

All notable changes to Satoshium Registry are documented in this file.

This changelog is inspired by **Keep a Changelog** and adapted for the institutional architecture of the Satoshium Suite.

Registry changes should distinguish among:

* constitutional alignment;
* institutional documentation;
* operational implementation;
* schemas and machine-readable artifacts;
* Registry Entry changes;
* record-type changes;
* lifecycle and status changes;
* interoperability changes;
* corrections and preservation actions.

---

## Changelog Principles

This changelog records meaningful changes affecting the Registry institution and its canonical operational object, the **Satoshium Registry Entry**, or **SREG**.

Changes should preserve the distinction between:

* Suite Standards and Registry implementation;
* Suite Methodology and Registry procedures;
* Suite Interoperability and Registry integrations;
* Registry-owned records and authoritative source records;
* Registry status and source-record status;
* SREG versions and source-record versions.

Registry does not use this changelog to rewrite or replace the history of originating institutions.

Source-system changes should be referenced where relevant, while Registry changes should remain clearly identified as Registry-owned changes.

---

## Change Categories

Registry releases may use the following categories.

### Added

New institutional documents, schemas, policies, procedures, record types, SREG fields, public pages, relationships, interoperability mappings, or published Registry Entries.

### Changed

Revisions to existing Registry structures, terminology, lifecycle rules, status models, schemas, procedures, documentation, or public presentation.

### Deprecated

Registry structures, fields, record types, procedures, schemas, or references that remain temporarily supported but are scheduled for retirement.

### Removed

Registry structures or references that have been formally withdrawn after documented deprecation, supersession, or governance review.

### Fixed

Corrections to Registry-owned documentation, metadata, identifiers, classifications, references, relationships, schemas, validation logic, or public presentation.

### Security

Changes addressing integrity, access, validation, provenance, tampering, dependency, or publication risks.

### Interoperability

Changes affecting the exchange, reference, interpretation, or mapping of records between Registry and other Satoshium Suite institutions.

### Preservation

Changes affecting version retention, correction history, supersession, revocation, archival continuity, or durable public references.

---

## [Unreleased] — August 2026 Operational Development

### Constitutional Alignment

- Reconciled the Registry foundation with the completed Satoshium Suite constitutional hierarchy.
- Established the governing implementation sequence:

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

- Confirmed that the July Registry architecture remains valid but requires post-Suite institutional reconciliation before operational completion.
- Confirmed that Registry does not own or replace authoritative records created by other Suite institutions.
- Confirmed that each originating institution remains authoritative for its own canonical objects and source records.
- Confirmed that Registry is authoritative only for Registry-owned information and Registry operations.

### Institutional Architecture

- Established the canonical Registry hierarchy:

```text
Satoshium Registry
  ↓
Registry Entry (SREG)
  ↓
Registry Record Type
  ↓
Authoritative Source Record
```

- Confirmed the SREG as Registry's canonical operational object.
- Defined Registry Record Type as the controlled classification assigned to a SREG.
- Defined Authoritative Source Record as the record owned and maintained by the originating institution.
- Clarified that Registry catalogs authoritative records through independent SREGs rather than duplicating or absorbing source authority.
- Clarified that Registry Entry and Registry Record terminology must be reconciled around the SREG model.

### Documentation

- Recreated the Registry public landing page within the Suite Standards, Methodology, Interoperability, and institutional implementation framework.
- Recreated the Registry repository `README.md` as a Suite-aligned institutional overview.
- Recreated the Registry licensing-context document to distinguish open-source licensing, institutional authority, source-record ownership, schema reuse, official Registry status, and trademark rights.
- Began systematic reconstruction of the Registry foundational Markdown documents.
- Established the requirement that all recreated Registry documents be complete, publication-ready, and suitable for immediate repository inclusion.
- Established the August practice of reconciling foundational documents before producing operational artifacts.

### Methodology

- Defined a Registry-specific institutional method separate from the certification workflow:

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

- Clarified that Suite Methodology provides shared implementation principles while Registry procedures define Registry-specific operations.
- Clarified that Certifier determines certification outcomes while Registry determines whether and how an authoritative record is cataloged.

### Interoperability

- Aligned Registry with the Suite institutional-object model:

  - Atlas → jurisdiction intelligence and canonical jurisdiction resources
  - Certifier → Certification Package and related certification artifacts
  - Registry → SREG
  - Chronicle → historical event
  - Anchor → integrity reference
  - Beacon → discovery signal or discovery metadata
  - Attestor → trust statement or attestation
  - Navigator → workflow definition

- Preserved the certification integration path:

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

- Clarified that the Certification Package remains Certifier's canonical certification object.
- Clarified that the SCRD remains a Certifier-owned certified record.
- Clarified that the SREG remains Registry's canonical catalog entry.
- Clarified that Registry interoperability extends beyond certifications to all supported authoritative source-record types.

### Schemas and Machine Readability

- Established the intended Registry schema hierarchy:

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

- Confirmed that Registry schemas must support human readability, machine readability, stable identifiers, controlled terminology, validation, versioning, relationship mapping, and long-term interoperability.
- Confirmed that record-type profiles should extend a common SREG base structure rather than create unrelated record systems.
- Confirmed that official machine-readable field names and validation requirements will be defined by the published Registry schema.

### Identifiers and Versions

- Confirmed that every SREG requires a stable Registry identifier.
- Clarified that a Registry identifier identifies the SREG and does not replace a source-system identifier.
- Established the need to distinguish among:

  - Suite Standards version
  - Suite Methodology version
  - Registry specification version
  - SREG schema version
  - record-type profile version
  - individual SREG version
  - source-record version

- Confirmed that version layers must remain independently traceable.

### Status and Lifecycle

- Confirmed that Registry Status is distinct from Certification Status, Certification Outcome, Attestation Status, and other source-record statuses.
- Confirmed that a SREG may remain publicly active as a historical catalog entry even when the referenced source record becomes revoked, expired, retired, or superseded.
- Retained the initial Registry lifecycle vocabulary:

  - Pending Registration
  - Registered
  - Active
  - Updated
  - Superseded
  - Revoked
  - Archived

- Clarified that lifecycle states are not necessarily a single mandatory linear sequence.
- Established the need for documented permitted transitions, version events, correction events, and terminal conditions.
- Confirmed that archived does not mean deleted.

### Corrections and Preservation

- Clarified that Registry corrections apply to Registry-owned information.
- Clarified that source-record changes must remain distinguishable from Registry-entry changes.
- Established the requirement to document material corrections, supersession, revocation, and archival actions.
- Confirmed that historical continuity should be preserved whenever practical.
- Confirmed that Registry must not silently rewrite source authority or source-record history.

### Policies and Procedures

- Confirmed the distinction:

  - Registry Rules define institutional expectations.
  - Registry Policies define implementation requirements.
  - Registry Procedures define repeatable operational steps.

- Identified required policy areas including:

  - registrability;
  - identifier assignment;
  - record classification;
  - source-authority confirmation;
  - reference validation;
  - schema validation;
  - relationship creation;
  - publication;
  - versioning;
  - corrections;
  - supersession;
  - revocation;
  - archival;
  - record-type extension;
  - governance;
  - interoperability.

### Current Development Objective

- Transform the constitutionally reconciled Registry foundation into a complete operational institution.
- Recreate all 11 foundational public pages and all foundational Markdown files before finalizing operational artifacts.
- Complete the SREG specification, Registry schemas, record types, policies, procedures, lifecycle transitions, identifiers, relationships, and public Registry artifacts.
- Publish initial machine-readable and human-readable SREG records.
- Prepare Registry to stand beside Atlas and Certifier as a completed operational Satoshium Suite institution.

---

## [0.1.0] — July 2026 Constitutional Foundation

### Added

- Initial Registry repository structure.
- Core Registry documentation framework.
- Registry public website framework.
- Initial record classification model.
- Initial Registry workflow definitions.
- Registry relationship mapping within the Satoshium ecosystem.
- Draft schemas, policies, and examples structure.
- Initial documentation for records, classifications, and references.
- Public Registry landing page.
- Public Purpose page.
- Public Records page.
- Public Record Types page.
- Public Rules page.
- Public Schemas page.
- Public Corrections page.
- Public Integration page.
- Public Entry Model page.
- Public Lifecycle page.
- Public Status page.
- Initial SREG concept.
- Initial distinction between Registry authority and source-system authority.
- Initial distinction between Registry Status and Certification Status.
- Initial certification integration path.
- Initial lifecycle and correction models.

### Architectural Outcome

- Established Registry as the public-record institution of the Satoshium ecosystem.
- Established that Registry catalogs records rather than creating their authority.
- Established the Registry Entry, or SREG, as the emerging canonical Registry object.
- Established the relationship:

```text
Certification Package
  ↓
SCRD
  ↓
SREG
```

- Established the layered Registry model:

```text
Registry
  ↓
Registry Entry
  ↓
Registry Record Type
  ↓
Source Record
```

### Development Condition

- Registry remained in constitutional and conceptual development.
- Schemas remained descriptive rather than operational.
- Policies and procedures remained incomplete.
- Machine-readable Registry artifacts were not yet published.
- Initial record populations were not yet implemented.
- Full alignment with Suite Standards, Suite Methodology, and Suite Interoperability had not yet occurred because those foundations were completed after the original Registry pages were created.

---

## Future Releases

Future releases may include the following changes when formally implemented.

### Added

- Published SREG specification.
- Stable Registry identifier specification.
- SREG base JSON Schema.
- record-type profiles.
- Registry policies.
- Registry procedures.
- relationship specification.
- lifecycle transition specification.
- versioning specification.
- correction specification.
- interoperability mappings.
- public SREG pages.
- machine-readable SREG JSON records.
- initial operational Registry catalog.
- additional controlled Registry record types.
- validation tools.
- preservation and archival artifacts.

### Changed

- Registry workflows.
- record-type definitions.
- lifecycle transitions.
- Registry status model.
- source-reference structures.
- relationship structures.
- schema versions.
- institutional documentation.
- public Registry presentation.

### Deprecated

- legacy Registry terminology.
- pre-SREG record models.
- superseded schema versions.
- obsolete status values.
- unsupported record-type structures.
- ambiguous authority language.

### Removed

- retired Registry structures.
- obsolete references.
- unsupported schema fields.
- deprecated terminology after the applicable transition period.

### Fixed

- documentation inconsistencies.
- schema inconsistencies.
- classification issues.
- broken references.
- identifier errors.
- status conflicts.
- relationship errors.
- terminology conflicts.
- source-authority ambiguities.

### Interoperability

- expanded Atlas integration.
- completed Certifier integration.
- Chronicle event references.
- Anchor integrity references.
- Beacon discovery metadata.
- Attestor trust-statement references.
- Navigator workflow coordination.
- cross-system identifier mapping.

### Preservation

- immutable release snapshots.
- superseded schema preservation.
- historical SREG versions.
- correction records.
- revocation records.
- archival records.
- durable source-reference preservation.

---

## Notes

Registry exists to preserve discoverability, continuity, and institutional relationships across the Satoshium Suite.

As the Suite evolves, this changelog records significant changes to Registry-owned structures, procedures, schemas, documentation, and operational artifacts.

Authoritative source-record history remains the responsibility of the originating institution.

Registry preserves the public path back to that authority.
