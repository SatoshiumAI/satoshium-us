# Registry Examples

## Overview

The `registry/examples/` directory contains non-authoritative sample materials used to demonstrate how Satoshium Registry concepts, schemas, classifications, relationships, and publication structures may be implemented.

The examples directory does not require an `index.html` file.

Its primary institutional artifact is this `README.md`, supported by individual example documents.

Examples are instructional and illustrative. They do not become official Registry Entries, or SREGs, unless they are separately processed, validated, assigned a Registry Identifier, and published through the approved Registry institutional workflow.

---

## Constitutional Position

Registry Examples operate beneath the Satoshium Suite constitutional architecture:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Suite Interoperability
  ↓
Registry Institutional Implementation
  ↓
Registry Examples
```

Examples may demonstrate how Registry requirements are applied, but they do not replace:

- Suite Standards;
- Registry Rules;
- Registry Policies;
- Registry Procedures;
- Registry Schema Specification;
- SREG Base Schema;
- Record-Type Profiles;
- approved operational Registry records.

Examples explain implementation.

They do not create authority.

---

## Purpose

The examples directory supports practical understanding of the Registry model.

Examples may be used to:

- demonstrate SREG structure;
- illustrate Registry Record Types;
- show how source authority is preserved;
- explain Registry Identifier and Source-System Identifier separation;
- demonstrate Registry Status and Source-Record Status separation;
- illustrate public references and relationships;
- support schema development;
- support validation testing;
- clarify lifecycle and correction behavior;
- demonstrate human-readable documentation;
- provide implementation guidance;
- reduce ambiguity before operational publication.

Examples transform abstract institutional requirements into visible, reviewable forms.

---

## Example Status

Every file in this directory should be treated as one of the following:

### Illustrative Example

A conceptual sample used to explain Registry structure.

### Schema Example

A sample object used to demonstrate expected fields, data types, constraints, or validation behavior.

### Workflow Example

A sample showing how a proposed record may move through identification, classification, validation, publication, update, correction, supersession, revocation, or archival.

### Interoperability Example

A sample showing how a SREG may reference records created by Atlas, Certifier, Chronicle, Anchor, Beacon, Attestor, Navigator, or another approved source.

### Test Fixture

A machine-readable sample used for schema or software validation.

Unless explicitly designated otherwise, all files in this directory are illustrative examples.

---

## Current Directory Structure

```text
registry/
└── examples/
    ├── README.md
    ├── example-jurisdiction-record.md
    ├── example-media-record.md
    └── example-tool-record.md
```

No `index.html` file is required for this directory.

The directory README serves as the primary explanation of purpose, authority, and intended use.

---

## Current Example Files

### `example-tool-record.md`

Demonstrates how a tool, platform component, service, application, framework, or Suite institution may be described as a Registry example.

A Tool example may illustrate:

- Registry Record Type;
- source institution;
- source record;
- public reference;
- operational status;
- related systems;
- version metadata;
- Registry relationships.

### `example-jurisdiction-record.md`

Demonstrates how a jurisdiction-related source record may be represented.

A Jurisdiction example may illustrate:

- country, state, territory, region, or other jurisdiction classification;
- Atlas as a Source Institution;
- Atlas canonical jurisdiction records;
- source identifiers;
- jurisdiction metadata;
- related certification or media references;
- Registry relationships.

### `example-media-record.md`

Demonstrates how a media resource may be represented.

A Media example may illustrate:

- media type;
- title;
- creator or Source Institution;
- public location;
- publication date;
- related jurisdiction, tool, certification, or event;
- source status;
- Registry relationships.

---

## Relationship to the SREG Model

A complete operational SREG follows the canonical Registry hierarchy:

```text
Satoshium Registry
  ↓
Registry Entry (SREG)
  ↓
Registry Record Type
  ↓
Authoritative Source Record
```

Examples may demonstrate this structure, but an example is not automatically a SREG.

An official SREG requires:

- a registrable Authoritative Source Record;
- an identified Source Institution;
- an approved Registry Record Type;
- a Registry Identifier;
- applicable schema validation;
- required relationships and references;
- Registry Status;
- lifecycle information;
- approved publication.

---

## Authority Boundaries

Examples must preserve the distinction between Registry-owned information and source-controlled information.

### Registry-Owned Information

Examples may illustrate:

- Registry Identifier;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- Registry Entry Version;
- Registry relationships;
- Registry correction history;
- Registry publication metadata.

### Source-Controlled Information

Examples may reference:

- Source-System Identifier;
- source-record title;
- source-record version;
- source-record status;
- Certification Outcome;
- Certification Status;
- attestation result;
- historical event content;
- integrity reference;
- discovery signal;
- jurisdiction intelligence;
- workflow definition.

Examples must not imply that Registry controls source-owned values.

---

## Example Record Types

Current examples focus on:

- Tool Records;
- Jurisdiction Records;
- Media Records.

Future examples may include:

- Certification Records;
- Attestation Records;
- Signal Records;
- Historical Records;
- Integrity Reference Records;
- Discovery Records;
- Workflow Records;
- Schema Records;
- Policy Records;
- Governance Records;
- Preservation Records.

New examples should correspond to approved or proposed Registry Record Types and should identify their status clearly.

---

## Example Construction Principles

A Registry example should:

- identify itself as an example;
- state that it is non-authoritative;
- identify the proposed Registry Record Type;
- distinguish Registry Identifier from Source-System Identifier;
- identify the Source Institution;
- identify the Authoritative Source Record;
- distinguish Registry Status from Source-Record Status;
- preserve version distinctions;
- use controlled terminology;
- include public references where appropriate;
- demonstrate typed relationships where appropriate;
- remain consistent with the Entry Model;
- remain consistent with the applicable schema draft or published schema;
- avoid implying registration, certification, attestation, verification, or ownership.

---

## Suggested Example Header

Each Markdown example should begin with a clear notice similar to:

```markdown
> **Example Status:** Illustrative only.  
> This document is not an official SREG and has not been registered,
> validated, or published as an operational Registry Entry.
```

This notice helps prevent confusion between examples and production records.

---

## Suggested Example Structure

A human-readable example may use the following structure:

```text
Example Status
Record Type
Proposed Registry Identifier
Title
Source Institution
Source-System Identifier
Authoritative Source Record
Source-Record Version
Source-Record Status
Registry Status
Registry Lifecycle State
Registry Entry Version
Schema Version
Public References
Relationships
Registration Date
Last Updated
Notes
```

The exact fields should follow the applicable Registry Schema Specification and Record-Type Profile.

---

## Identifiers in Examples

Examples may use clearly fictional or reserved identifiers.

Example identifiers should:

- be visibly non-production;
- avoid collision with official Registry Identifiers;
- avoid implying that registration has occurred;
- use a documented placeholder convention.

Examples should not assign realistic official identifiers unless the identifier has been expressly reserved for testing.

---

## Schema Alignment

Examples should align with the Registry schema hierarchy:

```text
Suite Schema Standard
  ↓
Registry Schema Specification
  ↓
SREG Base Schema
  ↓
Record-Type Profile
  ↓
Example Record
```

A schema example may intentionally demonstrate invalid data for testing, but that purpose must be clearly labeled.

Valid examples and invalid test fixtures should not be mixed without explanation.

---

## Human-Readable and Machine-Readable Examples

The examples directory may include both human-readable and machine-readable samples.

### Human-Readable Examples

May include:

- Markdown records;
- explanatory notes;
- lifecycle walkthroughs;
- relationship diagrams;
- correction examples.

### Machine-Readable Examples

May include:

- JSON SREG examples;
- schema-validation fixtures;
- Record-Type Profile examples;
- relationship maps;
- version-history objects;
- correction records.

Equivalent human-readable and machine-readable examples should remain consistent in meaning.

---

## Lifecycle Examples

Future lifecycle examples may demonstrate:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

Examples should show that these states are not necessarily a single mandatory linear sequence.

Lifecycle examples should also distinguish the condition of the SREG from the condition of the Source Record.

---

## Correction Examples

Future correction examples may demonstrate:

- editorial correction;
- metadata correction;
- structural correction;
- source-reference correction;
- material correction;
- administrative correction;
- supersession;
- revocation;
- archival.

A correction example should preserve:

- prior version;
- reason for change;
- affected fields;
- replacement version;
- source impact;
- publication impact.

---

## Interoperability Examples

Examples may demonstrate relationships such as:

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

Other examples may show:

- SREG → Chronicle Historical Event;
- SREG → Anchor Integrity Reference;
- SREG → Beacon Discovery Signal;
- SREG → Attestor Trust Statement;
- SREG → Navigator Workflow Definition;
- SREG → related SREG.

Interoperability examples must preserve institutional ownership.

---

## Intended Usage

Examples may be used for:

- learning Registry concepts;
- reviewing proposed structures;
- testing schemas;
- validating software;
- comparing Record-Type Profiles;
- demonstrating interoperability;
- developing policies and procedures;
- preparing future Registry Entries;
- documenting edge cases;
- evaluating correction and lifecycle behavior.

Examples should support implementation without being mistaken for production records.

---

## Relationship to Production Records

Examples are separate from operational Registry records.

Production SREGs must follow approved:

- Registry Rules;
- Registry Policies;
- Registry Procedures;
- Registry Schema Specification;
- SREG Base Schema;
- Record-Type Profile;
- identifier requirements;
- lifecycle requirements;
- publication requirements;
- governance controls.

An example becomes an official Registry Entry only through the approved Registry workflow.

---

## Repository Maintenance

When examples are added or changed:

- update this README when the directory structure changes;
- identify the example's status;
- identify the applicable Record Type;
- identify the schema or profile version used;
- preserve prior examples when they remain useful;
- document deprecated example formats;
- avoid silently changing examples that are used as test fixtures;
- keep related human-readable and machine-readable examples synchronized.

---

## Future Expansion

Future additions may include:

```text
examples/
├── README.md
├── example-tool-record.md
├── example-jurisdiction-record.md
├── example-media-record.md
├── example-certification-record.md
├── example-attestation-record.md
├── example-signal-record.md
├── lifecycle/
├── corrections/
├── relationships/
├── interoperability/
├── valid/
└── invalid/
```

This structure should be introduced only when the additional materials exist and the separation improves clarity.

---

## Disclaimer

Registry examples are informational and illustrative.

An example does not by itself create:

- an official SREG;
- registration;
- certification;
- attestation;
- verification;
- ownership;
- legal rights;
- government recognition;
- regulatory approval;
- endorsement;
- source authority.

Authority remains with the applicable Source Institution and Authoritative Source Record.

---

## Example Philosophy

Examples reduce ambiguity.

Rules establish expectations.

Policies define implementation requirements.

Procedures define repeatable actions.

Schemas define structure.

Examples demonstrate how those layers may work together.

---

## Guiding Statement

> Standards define expectations.
>
> Methodology defines implementation.
>
> Schemas define structure.
>
> Examples demonstrate.
>
> Registration creates the official SREG.
