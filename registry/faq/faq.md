# Satoshium Registry FAQ

## Frequently Asked Questions

This document answers common questions about the role, authority, structure, operation, and interoperability of Satoshium Registry within the Satoshium Suite.

Where a Registry answer depends on a Suite-wide rule, the applicable Satoshium Suite Standards, Methodology, and Interoperability architecture govern.

---

### What is Satoshium Registry?

Satoshium Registry is the authoritative public catalog of institutional records created throughout the Satoshium Suite.

Registry identifies, classifies, references, connects, and preserves the discoverability of authoritative source records through the canonical Satoshium Registry Entry, or SREG.

Registry does not replace the records created by other institutions.

---

### Why does Registry exist?

Registry exists because authoritative records can become difficult to locate, distinguish, connect, and preserve when they are distributed across multiple institutions, repositories, pages, schemas, and publication systems.

Registry provides:

- stable identification;
- controlled classification;
- structured references;
- public discoverability;
- relationship mapping;
- lifecycle continuity;
- version history;
- long-term catalog preservation.

---

### How does Registry fit within the Satoshium Suite?

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

Suite Standards define shared expectations.

Suite Methodology defines repeatable implementation principles.

Suite Interoperability defines how institutions exchange references while preserving authority boundaries.

Registry applies those foundations through its own rules, policies, procedures, schemas, lifecycle, and public entries.

---

### Does Registry create authority?

No.

Registry does not create authority merely by cataloging a record.

Authority remains with the institution that created and maintains the authoritative source record.

Registry is authoritative only for Registry-owned information, including:

- Registry identifiers;
- Registry record types;
- Registry status;
- Registry lifecycle states;
- Registry relationships;
- Registry versions;
- Registry corrections;
- Registry publication history.

---

### What is a Satoshium Registry Entry?

A Satoshium Registry Entry, abbreviated SREG, is Registry's canonical operational object.

A SREG identifies, classifies, references, and connects an authoritative source record.

A SREG may contain:

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
- references;
- relationships;
- registration and update dates;
- correction, supersession, revocation, or archival history.

---

### What is the relationship between Registry, SREG, Record Type, and Source Record?

Registry uses the following canonical hierarchy:

```text
Satoshium Registry
  ↓
Registry Entry (SREG)
  ↓
Registry Record Type
  ↓
Authoritative Source Record
```

Registry is the institution.

The SREG is the canonical Registry object.

The Registry Record Type is the controlled classification assigned to the SREG.

The Authoritative Source Record is the record owned by the originating institution.

---

### What is an Authoritative Source Record?

An Authoritative Source Record is the record created and maintained by the originating institution.

Examples include:

- a Certification Package;
- an SCRD;
- an Atlas canonical jurisdiction record;
- a Chronicle Entry;
- an Anchor integrity reference;
- a Beacon discovery signal;
- an Attestor trust statement;
- a Navigator workflow definition;
- a tool publication;
- a media resource.

Registry catalogs the source record but does not replace it.

---

### What is a Registry Record?

Registry Record is a general term for information formally maintained by Registry.

In operational use, the canonical Registry Record is the SREG.

The term should not be interpreted to mean that Registry owns the authoritative source record being cataloged.

---

### What is a Registry Entry?

A Registry Entry is the published human-readable or machine-readable representation of a SREG.

A Registry Entry may appear as:

- an HTML page;
- a JSON file;
- an API response;
- a structured catalog listing;
- another approved Registry publication format.

---

### Is Registry the same as Certifier?

No.

Certifier evaluates subjects under applicable standards and methodology and creates certification artifacts.

Registry creates SREGs that catalog those authoritative certification records.

A typical certification path is:

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

The Certification Package and SCRD remain Certifier-owned records.

The SREG remains Registry's catalog entry.

---

### Is Registry the same as Atlas?

No.

Atlas creates jurisdiction intelligence, canonical jurisdiction records, evidence resources, and machine-readable Atlas packages.

Registry may create Jurisdiction SREGs or other applicable entries that catalog Atlas records.

Atlas remains authoritative for Atlas content.

---

### Is Registry the same as Chronicle?

No.

Chronicle preserves qualifying historical Occurrences through canonical Chronicle Entries and institutional chronology.

Registry may catalog or cross-reference Chronicle Entries, but Chronicle remains authoritative for Chronicle-owned historical-preservation records.

---

### Is Registry the same as Anchor?

No.

Anchor creates and preserves integrity references, hashes, timestamps, signatures, and durable verification points.

Registry may reference those integrity records within a SREG.

Registry does not replace Anchor's integrity function.

---

### Is Registry the same as Beacon?

No.

Beacon creates discovery signals and discovery metadata.

Registry organizes authoritative records and preserves structured discoverability.

The institutions may interoperate, but they retain separate canonical objects and responsibilities.

---

### Is Registry the same as Attestor?

No.

Attestor creates trust statements, attestations, validations, and supporting verification references.

Registry may catalog those outputs through Attestation SREGs.

Registration does not itself create an attestation.

---

### Is Registry the same as Navigator?

No.

Navigator defines and coordinates workflows across one or more Suite institutions.

Registry may catalog workflow definitions or participate in coordinated processes, but Navigator remains responsible for workflow orchestration.

---

### What kinds of records can Registry catalog?

Initial supported Registry Record Types include:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal.

Additional controlled Record Types may be added through documented Registry governance.

Potential future types may include:

- Historical;
- Integrity Reference;
- Discovery;
- Workflow;
- Schema;
- Policy;
- Governance;
- Preservation.

---

### What is a Registry Record Type?

A Registry Record Type is the controlled primary classification assigned to a SREG.

The Record Type determines how the entry is organized, which profile applies, and what additional fields or relationships may be required.

A Record Type does not create authority over the source record.

---

### What is a Record-Type Profile?

A Record-Type Profile is a schema extension that adds type-specific requirements to the common SREG structure.

For example, a Certification Record may require fields that do not apply to a Media Record.

All profiles extend the shared SREG Base Schema.

---

### What is classification?

Classification is the process of assigning a SREG to an approved Registry Record Type and, where applicable, additional controlled subtypes.

Classification improves:

- organization;
- discoverability;
- validation;
- schema application;
- relationship mapping;
- interoperability.

---

### What is registrability?

Registrability is the condition of being eligible for inclusion in Registry.

A source record may be registrable when:

- an identifiable source record exists;
- the source institution can be identified;
- sufficient provenance is available;
- the record fits an approved Record Type;
- required references exist;
- the proposed SREG can satisfy applicable schema and policy requirements.

Registrability does not imply certification, endorsement, or legal approval.

---

### What is registration?

Registration is the formal Registry action through which a SREG is created, assigned a Registry Identifier, validated, and entered into the public catalog.

Registration applies to the SREG.

It does not transfer ownership of the source record.

---

### What is a Registry Identifier?

A Registry Identifier is a stable and unique value assigned by Registry to a SREG.

It identifies the SREG itself.

It does not replace:

- a Certification Identifier;
- a Certification Package identifier;
- an SCRD identifier;
- an Atlas resource identifier;
- an attestation identifier;
- another source-system identifier.

---

### What is a Source-System Identifier?

A Source-System Identifier is an identifier assigned by the originating institution to its own record.

A SREG should preserve the Source-System Identifier whenever one exists.

Registry and source identifiers remain distinct.

---

### What is a schema?

A schema is a formal definition of the structure, fields, value types, constraints, and validation rules applicable to a Registry object.

Registry schemas implement the Satoshium Suite Schema Standard.

---

### How are Registry schemas organized?

Registry follows this schema hierarchy:

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

The Registry Schema Specification defines institution-wide requirements.

The SREG Base Schema defines common fields.

Record-Type Profiles add type-specific requirements.

Published JSON records are validated instances.

---

### Are Registry records human-readable and machine-readable?

Yes.

Registry is intended to publish both:

- human-readable Registry Entry pages; and
- machine-readable SREG records.

The two forms should describe the same Registry object consistently.

---

### What is metadata?

Metadata is structured descriptive information associated with a SREG or source record.

Registry-owned metadata may include:

- Registry Identifier;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- Registry relationships;
- Registry publication dates.

Source-reported metadata may include:

- source identifier;
- source version;
- source status;
- certification outcome;
- source publication date.

---

### What is the difference between Registry Status and source-record status?

Registry Status describes the condition of the SREG within Registry.

Source-record status describes the condition of the authoritative source record as determined by the source institution.

They are separate.

For example:

```text
Certification Outcome: Certified
Certification Status: Revoked
Registry Status: Active
```

In that case, the SREG may remain publicly active as a historical catalog entry while accurately reporting that the certification itself has been revoked.

---

### What lifecycle states can a SREG have?

Initial Registry lifecycle states include:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

These states are not necessarily a single mandatory linear sequence.

Permitted transitions depend on the reason for change and the condition of both the SREG and the source record.

---

### Can Registry records change over time?

Yes.

A SREG may be:

- updated;
- corrected;
- superseded;
- revoked;
- archived;
- migrated to a newer schema;
- expanded with additional relationships or references.

Material changes should remain documented and versioned.

---

### Does Registry preserve history?

Yes.

Registry preserves historical continuity through:

- prior SREG versions;
- correction history;
- supersession records;
- revocation records;
- archival records;
- historical references;
- durable relationships;
- source and version metadata.

Archived does not mean deleted.

---

### What is a Registry correction?

A Registry correction is a documented change to Registry-owned information.

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

Registry corrections must not silently rewrite the authoritative source record.

---

### What happens when the source record changes?

Registry may update the SREG to reflect the new source version, status, location, or related metadata.

The Registry update should remain distinguishable from the source change.

Registry should preserve:

- the prior SREG version;
- the source version previously referenced;
- the date and reason for the update;
- the new source reference;
- any resulting relationship or lifecycle changes.

---

### Can Registry reference external resources?

Yes.

Registry may reference:

- documents;
- websites;
- repositories;
- reports;
- datasets;
- media;
- certifications;
- attestations;
- historical records;
- public records;
- other external resources.

Registry does not necessarily own, control, endorse, or preserve the full content of those resources.

---

### Does Registry duplicate every source record?

No.

Registry's primary responsibility is to preserve the structured path back to authority.

A SREG may preserve:

- identity;
- source institution;
- source identifier;
- canonical reference;
- status metadata;
- version metadata;
- relationships;
- integrity references;
- historical continuity.

Registry may publish approved copies or supporting artifacts where appropriate, but duplication is not required for Registry authority.

---

### Does a Registry Entry prove authenticity?

No.

A Registry Entry alone does not prove:

- authenticity;
- certification;
- attestation;
- ownership;
- legal rights;
- government recognition;
- regulatory approval;
- endorsement.

Registry catalogs claims, records, and relationships according to defined structures.

Verification must come from the appropriate source, institution, integrity reference, certification, or attestation process.

---

### Does Registry certify records?

No.

Certifier performs certification.

Registry may catalog certification records, but registration is not certification.

---

### Does Registry verify records?

Registry validates Registry structure and references within its own institutional scope.

Registry may confirm that:

- a referenced source exists;
- the source institution is identified;
- the source identifier is present;
- the Record Type is valid;
- required fields exist;
- the SREG satisfies its schema.

That validation does not necessarily verify the substantive truth of the source record.

---

### What is the difference between validation and verification?

Validation determines whether a Registry object satisfies applicable Registry schema, terminology, policy, and structural requirements.

Verification confirms a claim, identity, record, or integrity assertion through an appropriate authority or method.

Registry validates SREGs.

Other institutions may perform certification, attestation, integrity verification, or substantive review.

---

### What are Registry Rules?

Registry Rules define institution-specific operating expectations subordinate to Satoshium Suite Standards.

They establish what Registry must preserve, require, or protect.

---

### What are Registry Policies?

Registry Policies define the implementation requirements used to apply Registry Rules.

Policies may govern:

- registrability;
- identifier assignment;
- classification;
- source-authority confirmation;
- reference validation;
- publication;
- lifecycle;
- versioning;
- corrections;
- supersession;
- revocation;
- archival;
- interoperability.

---

### What are Registry Procedures?

Registry Procedures define the repeatable operational steps used to implement Registry Policies.

Procedures should be documented, reviewable, and reproducible.

---

### What methodology does Registry use?

Registry uses a Registry-specific institutional method aligned with Suite Methodology Principles:

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

This method is separate from the Certifier evaluation workflow.

---

### How does Registry support interoperability?

Registry supports interoperability through:

- stable Registry identifiers;
- preserved source identifiers;
- controlled Record Types;
- shared terminology;
- machine-readable schemas;
- typed relationships;
- canonical references;
- version metadata;
- clear institutional ownership;
- cross-system mappings.

Interoperability connects institutions without merging their responsibilities.

The first production interoperability chain demonstrates this principle:

```text
Atlas Jurisdiction Record — El Salvador
  ↓ certified by
SC-CERT-2026-0001
  ↓ registered as
SREG-2026-0001
  ↓ historically preserved by
CHR-2026-0001
```

Registry owns the SREG. Certifier owns the certification. Atlas owns the subject record. Chronicle owns the Chronicle Entry.

Reference does not transfer authority.

---

### Is Registry decentralized?

Registry's current institutional implementation is focused on establishing the authoritative public catalog, SREG specification, schemas, policies, procedures, and interoperability model.

Future distribution, replication, or decentralized publication mechanisms may be considered through documented governance.

The current architecture should not be described as decentralized unless such mechanisms are formally implemented and published.

---

### Is Registry complete?

Yes. Registry is operational as a production Suite institution.

The inaugural production Registry Entry, `SREG-2026-0001`, was established and published on August 2, 2026 for Certification Package `SC-CERT-2026-0001`.

A post-publication quality review completed on August 14, 2026 confirmed alignment among the human-readable Registry Entry, machine-readable record, Registry schema architecture, authority boundaries, provenance, relationships, Validation, and Publication.

Registry remains subject to continued maintenance, new registrations, schema evolution, Corrections, Versioning, and interoperability hardening. Operational does not mean frozen.

---

### What is Registry's current development goal?

Registry's current goal is continued production operation and institutional hardening.

That includes:

- registering additional authoritative records when justified;
- maintaining SREG versions and lifecycle state;
- preserving Corrections and historical continuity;
- strengthening cross-Suite references;
- evolving schemas and Record-Type Profiles through governance;
- maintaining human-readable and machine-readable consistency;
- preserving public discoverability and the path back to authority.

---

### What is the ultimate goal of Registry?

The ultimate goal of Registry is to ensure that authoritative records remain:

- identifiable;
- discoverable;
- understandable;
- connected;
- versioned;
- traceable;
- historically preserved;
- interoperable across time.

Registry exists to preserve the public path back to authority.

---

## Guiding Statement

> Institutions create authoritative records.
>
> Registry creates the path back to them.
>
> The source retains authority.
>
> The SREG preserves discovery.
