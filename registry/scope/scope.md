# Satoshium Registry Scope

## Purpose

This document defines the institutional scope of Satoshium Registry within the Satoshium Suite.

Scope establishes:

- what Registry is designed to manage;
- which responsibilities belong to Registry;
- which records and relationships Registry may catalog;
- what Registry may validate within its own institutional authority;
- which activities remain the responsibility of other Suite institutions;
- how Registry may expand without weakening institutional separation.

Where a scope question depends on a Suite-wide expectation, the Satoshium Suite Standards, Methodology, and Interoperability architecture govern.

---

## Registry Scope Statement

Satoshium Registry is the authoritative public catalog of institutional records created throughout the Satoshium Suite.

Registry exists to:

- identify authoritative source records;
- assign stable Registry identifiers;
- create and maintain Satoshium Registry Entries, or SREGs;
- classify SREGs through controlled Registry Record Types;
- preserve source references;
- document relationships;
- maintain Registry status and lifecycle;
- preserve Registry versions and corrections;
- support human-readable and machine-readable publication;
- preserve long-term discoverability and interoperability.

Registry catalogs authoritative source records.

Registry does not replace those records or assume the authority of the institutions that created them.

---

## Constitutional Scope

Registry operates within the following institutional hierarchy:

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

### Suite Standards

Define the expectations Registry must satisfy.

### Suite Methodology

Defines shared implementation principles for documented, reviewable, repeatable, and maintainable institutional processes.

### Suite Interoperability

Defines how Registry exchanges identifiers, references, relationships, and metadata with other Suite institutions while preserving institutional boundaries.

### Registry Institutional Implementation

Defines Registry-specific rules, policies, procedures, schemas, identifiers, record types, lifecycle controls, versions, corrections, relationships, and publication practices.

---

## Canonical Operational Scope

Registry operates through the following hierarchy:

```text
Satoshium Registry
  ↓
Registry Entry (SREG)
  ↓
Registry Record Type
  ↓
Authoritative Source Record
```

Registry's primary operational responsibility is the creation and maintenance of the SREG.

Registry does not become the owner of the Authoritative Source Record merely because the source is cataloged.

---

## Included Within Scope

The following activities fall within the intended institutional scope of Registry.

---

### SREG Creation

Registry may create a SREG when an identifiable and registrable Authoritative Source Record exists.

SREG creation includes:

- assigning a Registry Identifier;
- identifying the Source Institution;
- identifying the Source Record;
- assigning a Registry Record Type;
- preserving source references;
- recording required metadata;
- creating Registry relationships;
- validating applicable Registry schemas;
- publishing the Registry Entry.

---

### Registry Identification

Registry assigns a stable Registry Identifier to every SREG.

The Registry Identifier identifies the SREG itself.

It does not replace:

- a Certification Identifier;
- a Certification Package identifier;
- an SCRD identifier;
- an Atlas resource identifier;
- a Chronicle event identifier;
- an attestation identifier;
- another Source-System Identifier.

---

### Source Identification

Registry may identify and preserve information necessary to distinguish the Authoritative Source Record.

This may include:

- Source Institution;
- Source-System Identifier;
- source title;
- source version;
- source status;
- source publication date;
- canonical source location;
- public reference;
- integrity reference.

Registry may report source-controlled values but does not redefine them.

---

### Registrability Determination

Registry may determine whether a proposed source record is eligible for cataloging.

Registrability review may consider whether:

- an identifiable source record exists;
- the Source Institution can be identified;
- the source has sufficient provenance;
- an approved Registry Record Type applies;
- required references are available;
- the SREG can satisfy applicable schema and policy requirements;
- publication would remain consistent with Suite Standards and institutional boundaries.

A determination of registrability does not constitute certification, attestation, endorsement, legal recognition, or substantive verification.

---

### Record Classification

Registry assigns SREGs to controlled Registry Record Types.

Initial supported Record Types include:

- Tool;
- Jurisdiction;
- Media;
- Certification;
- Attestation;
- Signal.

Additional Record Types may be introduced through documented Registry governance.

Classification supports:

- organization;
- discoverability;
- validation;
- schema application;
- relationship mapping;
- interoperability.

Classification does not create source authority.

---

### Cataloging

Registry publishes and maintains SREGs within the public Registry catalog.

Cataloging may include:

- human-readable Registry Entry pages;
- machine-readable SREG records;
- public catalog listings;
- Record Type indexes;
- relationship indexes;
- version histories;
- correction histories;
- archival listings.

---

### Reference Management

Registry may create and preserve structured references to:

- Authoritative Source Records;
- public webpages;
- repositories;
- schemas;
- reports;
- Certification Packages;
- SCRDs;
- Atlas resources;
- historical events;
- integrity references;
- discovery signals;
- trust statements;
- workflow definitions;
- external resources.

References should remain attributable, understandable, and durable whenever practical.

---

### Relationship Mapping

Registry may document typed relationships among:

- SREGs;
- Source Records;
- Source Institutions;
- schemas;
- certifications;
- attestations;
- historical events;
- integrity references;
- discovery signals;
- workflows;
- policies;
- related public resources.

Relationship Types may include:

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

---

### Registry Metadata Management

Registry may create and maintain Registry-owned metadata, including:

- Registry Identifier;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- Registry schema version;
- Registry relationships;
- registration date;
- update date;
- correction history;
- supersession information;
- revocation information;
- archival information.

Registry may also catalog source-reported metadata, provided the source and authority remain clear.

---

### Registry Status Management

Registry may assign and maintain Registry Status values describing the institutional condition of a SREG.

Registry Status remains separate from:

- Certification Outcome;
- Certification Status;
- Attestation Status;
- Source-Record Status;
- Source Institution status.

Registry may preserve an active SREG even when the source record becomes revoked, expired, retired, or superseded, provided the SREG accurately reports that condition.

---

### Registry Lifecycle Management

Registry may maintain the lifecycle of a SREG through states such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

Lifecycle states are not necessarily a single mandatory linear sequence.

Registry may define permitted transitions, entry conditions, exit conditions, version events, correction events, and terminal conditions.

---

### Registry Versioning

Registry may define and preserve:

- Registry specification versions;
- SREG schema versions;
- Record-Type Profile versions;
- individual SREG versions;
- Registry policy versions;
- Registry procedure versions.

Registry must preserve the distinction between Registry-controlled versions and Source-Record versions.

---

### Registry Corrections

Registry may correct Registry-owned information.

Corrections may address:

- identifiers;
- titles;
- classifications;
- references;
- relationships;
- dates;
- versions;
- source locations;
- Registry Status;
- formatting;
- structural errors;
- schema compliance.

Material corrections should preserve:

- what changed;
- why it changed;
- when it changed;
- which version was affected;
- which version replaced it.

Registry must not silently rewrite the content or authority of the Source Record.

---

### Supersession

Registry may supersede a SREG or SREG version when a newer Registry object replaces it.

The superseded entry or version should remain preserved for continuity unless a documented legal, security, privacy, or integrity reason requires restricted handling.

---

### Revocation

Registry may revoke a SREG from active Registry recognition for a documented reason, including:

- material Registry error;
- invalid registration;
- loss of source authority;
- misclassification;
- irreparable reference failure;
- institutional reversal;
- another approved governance reason.

Revocation does not require deletion.

---

### Archival

Registry may archive SREGs that are no longer in active operational use.

Archival should preserve:

- Registry Identifier;
- historical context;
- prior versions;
- source references;
- relationships;
- correction history;
- supersession or revocation information.

Archived does not mean deleted.

---

### Historical Continuity

Registry may preserve continuity across:

- prior SREG versions;
- superseded entries;
- revoked entries;
- archived entries;
- source-record changes;
- schema migrations;
- Record Type changes;
- institutional transitions;
- historical milestones.

Registry preserves the public path back to authority.

---

### Schema Definition and Maintenance

Registry may define and maintain:

- Registry Schema Specification;
- SREG Base Schema;
- Record-Type Profiles;
- validation requirements;
- controlled values;
- relationship structures;
- lifecycle values;
- versioning structures;
- correction structures.

Registry schemas implement the Satoshium Suite Schema Standard.

---

### Machine-Readable Publication

Registry may publish machine-readable artifacts, including:

- SREG JSON records;
- JSON Schema;
- manifests;
- indexes;
- API responses;
- validation outputs;
- relationship maps.

Machine-readable records should remain consistent with human-readable Registry Entries.

---

### Human-Readable Publication

Registry may publish:

- Registry Entry pages;
- Record Type pages;
- public catalog indexes;
- institutional documentation;
- lifecycle history;
- correction history;
- relationship summaries;
- source-reference summaries.

---

### Registry Validation

Registry may validate whether a SREG satisfies Registry requirements.

Registry validation may confirm:

- required fields;
- valid Registry Identifier;
- valid Record Type;
- Source Institution;
- Source-System Identifier;
- source reference;
- permitted values;
- relationship structure;
- schema compliance;
- version metadata;
- publication requirements.

Registry validation is structural and institutional.

It does not necessarily verify the substantive truth of the Source Record.

---

### Registry Policy and Procedure

Registry may create and maintain policies and procedures governing:

- registrability;
- identifier assignment;
- classification;
- source-authority confirmation;
- reference validation;
- schema validation;
- relationship creation;
- publication;
- lifecycle;
- versioning;
- corrections;
- supersession;
- revocation;
- archival;
- Record Type extension;
- governance;
- interoperability.

Registry Rules define expectations.

Registry Policies define implementation requirements.

Registry Procedures define repeatable operational steps.

---

### Registry Governance

Registry may govern changes to:

- Registry Rules;
- Policies;
- Procedures;
- schemas;
- Record Types;
- identifier formats;
- lifecycle states;
- status values;
- relationship types;
- publication structures;
- interoperability mappings.

Governance should preserve transparency, version control, historical continuity, and public referenceability.

---

### Suite Interoperability

Registry may interoperate with:

- Atlas;
- Certifier;
- Chronicle;
- Anchor;
- Beacon;
- Attestor;
- Navigator;
- future Suite institutions.

Interoperability may include:

- source identifiers;
- Registry identifiers;
- canonical references;
- status mappings;
- relationship mappings;
- schema references;
- integrity references;
- version metadata;
- public discovery information.

Interoperability connects institutional objects without merging institutional authority.

---

### External References

Registry may reference external records, organizations, governments, institutions, publications, technologies, datasets, services, or media.

External reference does not imply:

- ownership;
- endorsement;
- sponsorship;
- affiliation;
- certification;
- verification;
- legal recognition.

Registry must preserve the distinction between Registry-authored metadata and third-party content.

---

## Outside Scope

The following activities fall outside the intended institutional scope of Registry unless a future Suite-wide constitutional change expressly assigns them to Registry.

---

### Certification

Registry does not evaluate subjects for certification and does not issue certification outcomes.

Certification belongs to Certifier.

Registry may catalog:

- Certification Packages;
- SCPRs;
- SCRs;
- SCRDs;
- certification statuses;
- certification relationships.

Cataloging a certification record is not certification.

---

### Certification Evidence Evaluation

Registry does not determine whether certification evidence is sufficient, persuasive, complete, or compliant with certification requirements.

Certifier evaluates certification evidence.

Registry may catalog evidence references and preserve relationships to evidence-bearing records.

---

### Attestation Creation

Registry does not create trust statements or attestations merely by registering a record.

Attestation belongs to Attestor or another recognized attesting authority.

Registry may catalog Attestation Records.

---

### Substantive Verification

Registry does not independently verify the substantive truth of every Source Record.

Registry may validate Registry structure, source attribution, identifiers, references, and schema compliance.

That institutional validation is not the same as substantive verification.

---

### Integrity Anchoring

Registry does not serve as the primary institution for creating hashes, timestamps, signatures, or integrity anchors.

Anchor owns that responsibility.

Registry may reference Anchor records and preserve their relationship to SREGs.

---

### Historical Event Creation

Registry does not serve as the primary institution for creating and interpreting historical events or institutional chronology.

Chronicle owns that responsibility.

Registry may catalog Chronicle records and preserve related references.

---

### Discovery Signal Creation

Registry does not create discovery signals as its primary institutional function.

Beacon owns discovery signals and discovery metadata.

Registry may catalog Beacon outputs or use them to support public discovery.

---

### Workflow Orchestration

Registry does not own cross-institutional workflow coordination as its primary responsibility.

Navigator owns workflow definitions and orchestration.

Registry may participate in workflows and catalog Workflow Records.

---

### Jurisdiction Intelligence Creation

Registry does not create Atlas jurisdiction intelligence.

Atlas owns jurisdiction research, jurisdiction records, evidence resources, and machine-readable Atlas packages.

Registry may catalog Atlas Resources.

---

### Source-Record Ownership

Registry does not acquire ownership of a Source Record by cataloging it.

The Source Institution or applicable rights holder retains ownership and authority.

---

### Source-Record Modification

Registry does not silently edit, rewrite, or replace a Source Record.

Registry may update the SREG to reflect a source change while preserving the distinction between:

- the source change;
- the Registry update.

---

### Ownership Determination

Registry does not determine ownership, title, intellectual-property rights, custody, or legal possession.

A SREG does not create ownership rights.

---

### Legal Authority

Registry is not, by itself:

- a governmental registry;
- a court record;
- a regulatory filing system;
- a title office;
- a licensing authority;
- a legal evidence repository;
- a public-record office established by law.

A SREG does not create legal rights or governmental recognition.

---

### Regulatory Approval

Registry does not grant regulatory approval, compliance status, licensure, accreditation, or governmental authorization.

---

### Truth Determination

Registry does not independently determine objective truth merely by cataloging a claim or record.

Registry preserves structured attribution, provenance, references, and relationships.

Truth claims remain subject to the authority and methods of the originating institution or appropriate verifying body.

---

### Endorsement

Registry inclusion does not imply endorsement, sponsorship, recommendation, approval, or affiliation.

---

### Guarantee of Availability

Registry cannot guarantee that every external Source Record will remain publicly available forever.

Registry may preserve metadata, references, integrity information, and historical context to support continuity.

---

### Universal Preservation of Source Content

Registry is not required to duplicate and preserve the full content of every Source Record.

Registry's primary obligation is to preserve the structured path back to authority.

Where approved copies, snapshots, hashes, manifests, or archival records are appropriate, they should be governed by applicable policy and institutional responsibility.

---

### Trademark Authorization

Registry publication does not grant permission to use Satoshium trademarks, Registry branding, institutional seals, certification marks, or protected visual identity.

---

## Scope Boundaries

Registry's institutional boundaries may be summarized as follows:

- Registry catalogs rather than certifies.
- Registry references rather than replaces.
- Registry validates structure rather than determining universal truth.
- Registry preserves relationships rather than absorbing institutional authority.
- Registry maintains SREGs rather than owning every Source Record.
- Registry records source status rather than controlling it.
- Registry preserves discovery rather than guaranteeing source permanence.
- Registry supports interoperability rather than merging institutions.

These boundaries protect the constitutional separation of responsibilities across the Satoshium Suite.

---

## Scope of Registry Authority

Registry authority extends to:

- the SREG;
- the Registry Identifier;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- Registry schemas;
- Registry relationships;
- Registry corrections;
- Registry publication history;
- Registry catalog organization.

Registry authority does not extend to:

- Certification Outcomes;
- Source-Record content;
- Source-Record ownership;
- Source-Record version decisions;
- Attestation conclusions;
- Chronicle historical interpretation;
- Anchor integrity determinations;
- Beacon discovery conclusions;
- Atlas jurisdiction intelligence;
- Navigator workflow authority.

---

## Scope of Preservation

Registry preservation includes:

- stable Registry identity;
- source attribution;
- source references;
- relationship history;
- Registry versions;
- correction history;
- supersession history;
- revocation history;
- archival continuity;
- schema references;
- public discoverability.

Registry preservation does not necessarily include permanent custody of the complete Source Record.

---

## Scope of Interoperability

Registry interoperability includes the ability to:

- reference authoritative institutional objects;
- preserve source identifiers;
- map relationships;
- expose machine-readable records;
- maintain compatible terminology;
- preserve version distinctions;
- identify canonical public locations;
- support workflow handoffs;
- support discovery and integrity references.

Interoperability does not grant Registry authority over the connected institution.

---

## Future Expansion

Registry is designed to evolve through documented governance.

Future expansion may include:

- additional Record Types;
- additional Record-Type Profiles;
- expanded schemas;
- new relationship types;
- new validation tools;
- distributed publication;
- additional preservation mechanisms;
- API services;
- search and discovery functions;
- automation;
- AI-assisted cataloging;
- broader external interoperability.

Future expansion must remain consistent with:

- Suite Standards;
- Suite Methodology;
- Suite Interoperability;
- Registry's cataloging mission;
- institutional separation;
- source authority;
- version preservation;
- transparent governance.

Expansion should strengthen Registry's function without converting Registry into Certifier, Chronicle, Anchor, Beacon, Attestor, Navigator, Atlas, or another Suite institution.

---

## Scope Summary

Registry exists to answer:

- What authoritative record exists?
- Which institution created it?
- What Registry Entry catalogs it?
- What Registry Record Type applies?
- What is its Registry Identifier?
- What is its Source-System Identifier?
- Where is the authoritative source located?
- What is the Registry Status?
- What is the Source-Record Status?
- Which versions exist?
- What is related to it?
- What changed?
- How can it be found later?

The scope of Registry is defined by those questions and by the constitutional principle that the source retains authority.

---

## Guiding Statement

> Institutions create authoritative records.
>
> Registry identifies, classifies, references, and connects them.
>
> Registry does not replace their authority.
>
> Registry preserves the path back to the source.
