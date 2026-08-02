# SREG-2026-0001

## Overview

The `registry/registered-items/SREG-2026-0001/` directory contains the complete public registration package for the inaugural Satoshium Registry Entry:

```text
SREG-2026-0001
```

This Registry Entry represents the certification preserved by:

```text
SC-CERT-2026-0001
```

The registered Source Record is the Certifier-owned Certification Package for the Atlas Jurisdiction Record — El Salvador.

---

## Directory Structure

```text
registry/
└── registered-items/
    └── SREG-2026-0001/
        ├── index.html
        ├── registry-entry.html
        ├── record.json
        └── README.md
```

Each file serves a distinct institutional role.

---

## `index.html`

The item-level `index.html` is the registration overview.

It summarizes:

- Registry Identifier;
- Registry Entry Version;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- registration date;
- Source Institution;
- Source-System Identifier;
- Authoritative Source Record;
- Source-Record Version;
- registered subject;
- source certification facts;
- source artifacts;
- Suite Standards and Methodology;
- authority boundaries;
- Registry Relationships;
- Validation;
- Registration History;
- notices and limitations;
- links to all canonical SREG artifacts.

The overview is not itself the canonical Registry Entry.

---

## `registry-entry.html`

The `registry-entry.html` file is the canonical human-readable Satoshium Registry Entry.

It is the actual SREG.

It should contain the complete Registry-owned representation of:

```text
SREG-2026-0001
```

At minimum, it should preserve:

- Registry Identifier;
- Registry Entry Version;
- Registry Record Type;
- Registry Status;
- Registry Lifecycle State;
- registration date;
- title;
- description;
- Source Institution;
- Source Authority;
- Authoritative Source Record;
- Source-System Identifier;
- Source-Record Version;
- canonical source URL;
- related source artifacts;
- registered subject;
- Registry Relationships;
- provenance;
- Validation;
- Publication;
- Versioning;
- Corrections;
- History;
- notices;
- limitations;
- canonical Registry URLs.

---

## `record.json`

The `record.json` file is the canonical machine-readable representation of the SREG.

It should remain materially aligned with `registry-entry.html`.

```text
registry-entry.html
        ↕
record.json
```

The two representations should not contain conflicting Registry facts.

The JSON record should use:

- the SREG Base Schema;
- the Certification Record-Type Profile;
- governed Controlled Values;
- canonical Registry field names;
- current Registry Entry Version;
- current Source-Record Version;
- canonical Registry and source references.

---

## `README.md`

This file documents:

- the purpose of the SREG directory;
- file responsibilities;
- authority boundaries;
- source relationships;
- identifiers;
- versions;
- Validation;
- Publication;
- Corrections;
- History;
- maintenance requirements;
- related institutional pages.

---

## Registry Identity

```text
Registry Identifier: SREG-2026-0001
Registry Entry Version: 1.0
Registry Record Type: Certification
Registry Status: Active
Registry Lifecycle State: Published
Registration Date: August 2, 2026
```

The Registry Identifier is permanent, unique, and non-reused.

It remains stable across future Registry Entry Versions.

---

## Source Identity

```text
Source Institution: Satoshium Certifier
Source-System Identifier: SC-CERT-2026-0001
Authoritative Source Record: Certification Package
Source-Record Version: 1.1
```

The Source-System Identifier remains under Certifier authority.

It does not replace the Registry Identifier.

---

## Canonical Registry Position

```text
Satoshium Registry
  ↓
SREG-2026-0001
  ↓
Registry Record Type: Certification
  ↓
Certification Package SC-CERT-2026-0001
```

Registry owns the SREG and its Registry-controlled representation.

Certifier owns the Certification Package and certification decision.

---

## Registered Subject

The registered certification concerns:

```text
Atlas Jurisdiction Record — El Salvador
```

The subject is maintained by Satoshium Atlas.

The subject record is available at:

```text
https://satoshium.us/atlas/jurisdiction-intelligence-engine/global/countries/el-salvador/
```

The certification applies to the subject state reviewed on July 5, 2026.

---

## Source Certification Facts

The Certifier source record establishes:

```text
Certification Outcome: Certified
Certification Status: Issued · Active
Certification Class: Operational
Confidence Posture: Supported
Decision Authority: Satoshium Certifier
Package Version: 1.1
Certification Date: July 5, 2026
```

These remain source-domain certification facts.

They are not Registry Status or Registry Lifecycle State values.

---

## Authoritative Source Record

The Authoritative Source Record is:

```text
Certification Package SC-CERT-2026-0001
```

The Certification Package is Certifier’s canonical operational record for the certification.

It governs the interpretation of the generated certification artifacts.

---

## Related Certifier Artifacts

Related Certifier artifacts include:

- Certification Process Report;
- Certification Receipt;
- Certified Record HTML;
- Certified Record JSON.

These artifacts derive from and remain subordinate to the Certification Package.

They support registration but do not replace the Certification Package as the Authoritative Source Record.

---

## Source Artifact References

### Certification Package

```text
https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/
```

### Certification Process Report

```text
https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/reports/certification-process-report/
```

### Certified Record HTML

```text
https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/records/certified-record/
```

### Certified Record JSON

```text
https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/records/certified-record/scrd_json.json
```

---

## Governing Suite Framework

The source certification identifies the following Suite-level framework:

```text
Satoshium Suite Standards v1.0
Satoshium Suite Methodology v1.0
```

Relevant links:

```text
https://satoshium.us/suite/standards/
https://satoshium.us/suite/methodology/
```

The source certification also identifies:

- Certification Standard v1.0;
- Evidence Standard v1.0;
- Trust Standard v1.0;
- Scoring Standard v1.0;
- Certification Lifecycle;
- Certification Workflow;
- Evaluation Criteria;
- Evidence Requirements;
- Certification Logic;
- Decision Process.

---

## Authority Boundaries

### Satoshium Registry

Registry owns:

- SREG-2026-0001;
- Registry Identifier;
- Registry Record Type;
- Registry Entry Version;
- Registry Status;
- Registry Lifecycle State;
- Registry Relationships;
- Registry Validation;
- Registry Publication;
- Registry Corrections;
- Registry History;
- Registry Catalog presentation.

### Satoshium Certifier

Certifier owns:

- Certification Package SC-CERT-2026-0001;
- certification outcome;
- certification class;
- certification status;
- certification scope;
- certification evidence;
- certification reasoning;
- SCPR;
- SCR;
- SCRD HTML;
- SCRD JSON;
- other Certifier-created certification artifacts.

### Satoshium Atlas

Atlas owns:

- Atlas Jurisdiction Record — El Salvador;
- underlying jurisdiction intelligence;
- Atlas identifiers;
- Atlas versions;
- Atlas generation manifests;
- Atlas source-domain methodology.

### Suite Standards

Suite Standards defines the governing expectations.

### Suite Methodology

Suite Methodology defines the repeatable implementation process.

```text
Certifier certifies.
Registry registers.
Atlas retains subject authority.
```

---

## Registry Relationships

The initial Registry Relationships include:

```text
SREG-2026-0001
  registers
Certification Package SC-CERT-2026-0001
```

```text
SREG-2026-0001
  is sourced from
Satoshium Certifier
```

```text
Certification Package SC-CERT-2026-0001
  certifies
Atlas Jurisdiction Record — El Salvador
```

```text
Atlas Jurisdiction Record — El Salvador
  is maintained by
Satoshium Atlas
```

```text
Certification Process Report
  derives from
Certification Package SC-CERT-2026-0001
```

```text
Certified Record HTML and JSON
  derive from
Certification Package SC-CERT-2026-0001
```

---

## Registrability

SREG-2026-0001 is registrable because:

- the Source Institution is identifiable;
- the Authoritative Source Record is publicly resolvable;
- the Source-System Identifier is stable;
- the object fits the Certification Registry Record Type;
- source provenance is sufficient;
- the registration preserves institutional authority boundaries;
- the certification has durable public and historical value;
- the source artifacts support Registry traceability.

---

## Provenance

The provenance chain is:

```text
Satoshium Atlas
  ↓
Atlas Jurisdiction Record — El Salvador
  ↓ evaluated by
Satoshium Certifier
  ↓
Certification Package SC-CERT-2026-0001
  ↓ registered by
Satoshium Registry
  ↓
SREG-2026-0001
```

Registry preserves this chain without transferring source ownership or authority.

---

## Validation

The initial Registry Validation should confirm:

- Registry Identifier is valid;
- Registry Record Type is Certification;
- Source Institution is identified;
- Source Authority is sufficient;
- Authoritative Source Record resolves;
- Source-System Identifier is preserved;
- Source-Record Version is identified;
- registered subject is identified;
- provenance is sufficient;
- Registry Relationships are valid;
- Registry, Certifier, and Atlas authority boundaries remain clear;
- `registry-entry.html` and `record.json` agree;
- notices and limitations are represented;
- Publication requirements are satisfied.

Registry Validation confirms Registry conformance.

It does not repeat or replace Certifier’s certification evaluation.

---

## Publication

Publication of SREG-2026-0001 should establish:

- official Registry recognition;
- canonical Registry Identifier resolution;
- current Registry Entry Version;
- canonical human-readable Registry Entry;
- canonical machine-readable record;
- public source and provenance references;
- Registry Status;
- Registry Lifecycle State;
- notices and limitations;
- Registered Items inclusion;
- future Catalog inclusion.

Publication does not establish:

- certification authority;
- Source-Record ownership;
- Source-Record truth;
- endorsement;
- affiliation;
- governmental approval;
- regulatory approval.

---

## Versioning

The initial versions are:

```text
Registry Entry Version: 1.0
Source-Record Version: 1.1
```

These versions remain distinct.

Additional version domains may include:

- SREG Base Schema Version;
- Certification Record-Type Profile Version;
- Controlled-Value Set Versions;
- Catalog Version;
- Suite Standards Version;
- Suite Methodology Version.

A new Registry Entry Version should be issued when material Registry-owned content changes.

---

## Corrections

A Registry Correction may address:

- Registry Identifier metadata;
- Registry classification;
- Registry Relationships;
- Registry provenance representation;
- Registry Status;
- Registry Lifecycle State;
- Registry Publication metadata;
- Registry History;
- notices;
- other Registry-owned fields.

A Source Correction remains under Certifier or Atlas authority, depending on the affected Source Record.

Material Corrections must not be silent.

A Correction should preserve:

- affected Registry Entry Version;
- prior value;
- corrected value;
- reason;
- Correction Authority;
- correction date;
- supporting evidence;
- resulting Registry Entry Version;
- historical resolution.

---

## Initial Registration History

### July 5, 2026

Satoshium Certifier issued the initial operational certification for the Atlas Jurisdiction Record — El Salvador.

### July 17, 2026

The Certification Package architecture was hardened and terminology reconciled across Certifier artifacts.

### August 2, 2026

SREG-2026-0001 was established as the inaugural operational Satoshium Registry Entry.

### Current Registry Entry Version

```text
1.0
```

---

## Notices and Limitations

- This SREG catalogs a certification record.
- It does not independently perform certification.
- The certification applies to the Atlas subject state reviewed on July 5, 2026.
- Future changes to the Atlas record may require renewed review or recertification.
- The certification does not independently certify every supporting Atlas file.
- Registration does not transfer authority away from Certifier or Atlas.
- The historical prototype assessment is preserved as source history.
- The authoritative certification class is Operational.
- Registry Validation is not Certification.
- Registered Items inclusion is not endorsement or affiliation.

---

## Certifier Correlation

Certifier’s Registry integration page documents the source institution’s relationship with Registry:

```text
https://satoshium.us/certifier/registry/
```

This SREG directory preserves the reciprocal Registry-side correlation.

---

## Registry Framework Dependencies

SREG-2026-0001 depends on:

- Registry Purpose;
- Registry Scope;
- Registry Definitions;
- Registry Records;
- Registry Record Types;
- Registry Rules;
- Registry Policies;
- Registry Procedures;
- Registry Governance;
- Registry Controlled Values;
- Registry Schemas;
- Registry Entry Model;
- Registry Source Authority;
- Registry Registrability;
- Registry Identifiers;
- Registry Relationships;
- Registry Provenance;
- Registry Validation;
- Registry Publication;
- Registry Versioning;
- Registry Corrections;
- Registry Status;
- Registry Lifecycle;
- Registry Catalog;
- Registry History;
- Registry Transparency;
- Registry Integration.

---

## Maintenance Requirements

When SREG-2026-0001 changes:

- update `index.html`;
- update `registry-entry.html`;
- update `record.json`;
- update this README when architecture or interpretation changes;
- preserve prior Registry Entry Versions;
- preserve Source-Record Version distinctions;
- verify all source URLs;
- verify all Registry URLs;
- verify `registry-entry.html` and `record.json` agree;
- verify Registry Status and Lifecycle values;
- verify Source Institution and Source Authority;
- verify Registry Relationships;
- verify provenance;
- update Validation;
- update Publication information;
- preserve Corrections;
- preserve History;
- update Registered Items metadata when needed;
- update Catalog indexes when needed;
- document material changes in Registry History or Changelog.

---

## Guiding Principles

- The Registry Entry is the SREG.
- The Certification Package is the Authoritative Source Record.
- The Source-System Identifier does not replace the Registry Identifier.
- Registry owns Registry-controlled representation.
- Certifier owns certification meaning and outcome.
- Atlas owns the underlying subject record.
- Registration must preserve Source Authority.
- Registry Validation must not be represented as Certification.
- Human-readable and machine-readable SREG representations must agree.
- Material Corrections must not be silent.
- Prior Registry Entry Versions must remain historically resolvable.
- Every SREG must preserve a durable path back to authority.

---

## Disclaimer

SREG-2026-0001 does not by itself establish:

- a new certification decision;
- a new certification outcome;
- a new attestation;
- endorsement;
- affiliation;
- Source Authority;
- Source-Record ownership;
- legal ownership;
- licensing rights;
- governmental authority;
- regulatory approval;
- permanent Source Record availability.

Those remain controlled by the applicable Source Institution, Certifier, Atlas, rights holder, governing authority, Source Record, Rule, Policy, Procedure, or external system.

---

## Guiding Statement

> Certifier certifies.
>
> Registry registers.
>
> Atlas retains subject authority.

