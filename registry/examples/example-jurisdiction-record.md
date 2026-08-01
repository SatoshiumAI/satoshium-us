# Example Jurisdiction Record

> **Example Status:** Illustrative only.  
> This document is not an official Satoshium Registry Entry, has not been assigned a production Registry Identifier, and has not been published as an operational SREG.

---

## Example Purpose

This example demonstrates how a jurisdiction-related Authoritative Source Record may be represented within Satoshium Registry.

It is intended to illustrate:

- the SREG model;
- Registry Record Type assignment;
- Source Institution and Source Record separation;
- Registry Identifier and Source-System Identifier separation;
- Registry Status and Source-Record Status separation;
- typed relationships;
- version metadata;
- public references;
- jurisdiction-specific fields.

This example does not establish an authoritative Registry record for California.

---

## Constitutional Position

This example follows the Satoshium Suite implementation hierarchy:

```text
Suite Standards
  ↓
Suite Methodology
  ↓
Suite Interoperability
  ↓
Registry Institutional Implementation
  ↓
Example SREG
```

The example illustrates Registry implementation.

It does not create Registry authority, Atlas authority, certification, attestation, verification, legal recognition, or governmental status.

---

## Canonical Operational Hierarchy

```text
Satoshium Registry
  ↓
Registry Entry (SREG)
  ↓
Jurisdiction Record Type
  ↓
Atlas Authoritative Source Record
```

Registry would create and maintain the SREG.

Atlas would remain authoritative for the referenced jurisdiction intelligence and machine-readable jurisdiction record.

---

## Example Registry Entry

| Field | Example Value |
|---|---|
| Example Status | Illustrative only |
| Registry Record Type | Jurisdiction |
| Proposed Registry Identifier | EXAMPLE-SREG-JUR-US-CA-0001 |
| Title | California |
| Source Institution | Satoshium Atlas |
| Source-System Identifier | Example only; not assigned |
| Authoritative Source Record | Example Atlas canonical jurisdiction record for California |
| Source-Record Version | Example only |
| Source-Record Status | Example: Active |
| Registry Status | Example: Active |
| Registry Lifecycle State | Example: Active |
| Registry Entry Version | 0.1.0-example |
| Schema Version | Example draft |
| Registration Date | Not registered |
| Last Updated | 2026-08-01 |
| Publication Status | Example only |

The identifier `EXAMPLE-SREG-JUR-US-CA-0001` is a reserved illustrative value and must not be interpreted as an official Registry Identifier.

---

## Jurisdiction Classification

```text
Jurisdiction
└── Country
    └── United States
        └── State
            └── California
```

### Primary Registry Record Type

**Jurisdiction**

### Jurisdiction Class

**U.S. State**

### Parent Jurisdiction

**United States of America**

### Jurisdiction Name

**California**

This classification is illustrative and should be validated against the applicable Jurisdiction Record-Type Profile before operational use.

---

## Source Institution

**Satoshium Atlas**

Atlas is the Suite institution responsible for jurisdiction intelligence, canonical jurisdiction records, evidence resources, and machine-readable Atlas packages.

Registry may catalog an Atlas jurisdiction record through a Jurisdiction SREG.

Registry does not replace Atlas authority.

---

## Authoritative Source Record

The Authoritative Source Record for an operational California Jurisdiction SREG would be the applicable Atlas canonical jurisdiction record or Atlas package.

An operational SREG should preserve:

- Atlas source identifier;
- canonical Atlas URL or repository location;
- Atlas record version;
- Atlas record status;
- Atlas generation manifest reference;
- related Atlas package references;
- applicable evidence or media references.

This example does not assign or invent those production values.

---

## Registry Identifier

An operational Jurisdiction SREG would receive a stable Registry Identifier assigned by Satoshium Registry.

The Registry Identifier would identify the SREG itself.

It would not replace:

- the Atlas source identifier;
- an Atlas package identifier;
- a jurisdiction code;
- an external government identifier;
- an ISO code;
- another source-controlled identifier.

---

## Source-System Identifier

The Source-System Identifier would be assigned and controlled by Atlas.

Registry would preserve that identifier within the SREG.

The Source-System Identifier and Registry Identifier must remain distinct.

---

## Registry Status and Source-Record Status

Registry Status and Source-Record Status are separate values.

Example:

```text
Source-Record Status: Active
Registry Status: Active
```

A future source change could produce a different combination:

```text
Source-Record Status: Superseded
Registry Status: Active
```

In that case, Registry could preserve the SREG as an active historical catalog entry while accurately reporting that the Atlas Source Record had been superseded.

---

## Lifecycle

An operational Jurisdiction SREG may move through Registry lifecycle states such as:

- Pending Registration;
- Registered;
- Active;
- Updated;
- Superseded;
- Revoked;
- Archived.

This example uses:

**Registry Lifecycle State:** Example: Active

This is illustrative only and does not indicate actual registration.

---

## Versions

An operational Jurisdiction SREG should distinguish among:

- Registry specification version;
- SREG schema version;
- Jurisdiction Record-Type Profile version;
- Registry Entry Version;
- Atlas Source-Record version;
- Atlas package version;
- applicable Suite Standards version.

For this example:

| Version Layer | Example Value |
|---|---|
| Registry Entry Version | 0.1.0-example |
| SREG Schema Version | Example draft |
| Jurisdiction Profile Version | Example draft |
| Source-Record Version | Example only |

---

## Public References

An operational SREG may preserve public references such as:

- canonical Atlas jurisdiction page;
- Atlas JSON record;
- Atlas package manifest;
- Registry HTML entry;
- Registry JSON entry;
- related media page;
- certification package;
- Chronicle event;
- Anchor integrity reference.

Example references should not be substituted for official publication locations.

---

## Relationships

An operational Jurisdiction SREG may include typed relationships such as:

### Source Relationship

```text
SREG → references → Atlas Jurisdiction Record
```

### Parent-Jurisdiction Relationship

```text
California SREG → part of → United States SREG
```

### Certification Relationship

```text
California SREG → related to → Certification SREG
```

### Media Relationship

```text
California SREG → related to → Media SREG
```

### Historical Relationship

```text
California SREG → related to → Chronicle Historical Event
```

### Integrity Relationship

```text
California SREG → anchored by → Anchor Integrity Reference
```

### Attestation Relationship

```text
California SREG → attested by → Attestor Trust Statement
```

These relationships are illustrative and require approved relationship types before operational use.

---

## Related Suite Records

### Atlas

Atlas may provide:

- canonical jurisdiction intelligence;
- jurisdiction JSON;
- generation manifest;
- evidence resources;
- media references;
- source metadata.

### Certifier

Certifier may create certification records related to the jurisdiction.

A certification relationship may follow:

```text
Atlas Jurisdiction Resource
  ↓
Certifier Evaluation
  ↓
Certification Package
  ↓
SCRD
  ↓
Certification SREG
```

### Chronicle

Chronicle may preserve historical events related to the jurisdiction or its treatment within the Suite.

### Anchor

Anchor may preserve integrity references associated with Atlas or Registry artifacts.

### Beacon

Beacon may publish discovery signals or metadata that help users locate jurisdiction records.

### Attestor

Attestor may create trust statements or attestations related to jurisdiction records.

### Navigator

Navigator may coordinate workflows involving Atlas, Certifier, Registry, or other institutions.

---

## Jurisdiction Metadata

The following fields illustrate jurisdiction-specific metadata that may appear in a Jurisdiction Record-Type Profile.

| Field | Example Value |
|---|---|
| Jurisdiction Name | California |
| Jurisdiction Class | U.S. State |
| Parent Jurisdiction | United States |
| Country Code | US |
| Subdivision Code | US-CA |
| Source Institution | Satoshium Atlas |
| Registry Record Type | Jurisdiction |
| Public Name | California |
| Registry Status | Example: Active |

These values are illustrative and do not define the final machine-readable schema.

---

## Human-Readable Representation

A human-readable operational Registry Entry may include:

- title;
- Registry Identifier;
- Record Type;
- Source Institution;
- source reference;
- Registry Status;
- Source-Record Status;
- version information;
- jurisdiction classification;
- related records;
- lifecycle history;
- correction history;
- public references.

---

## Machine-Readable Representation

A machine-readable Jurisdiction SREG may include:

- stable Registry Identifier;
- Record Type;
- source-system metadata;
- source reference;
- jurisdiction classification;
- status values;
- versions;
- relationships;
- lifecycle metadata;
- public references;
- validation metadata.

The final field names and constraints must follow:

```text
Suite Schema Standard
  ↓
Registry Schema Specification
  ↓
SREG Base Schema
  ↓
Jurisdiction Record-Type Profile
  ↓
Published Jurisdiction SREG
```

---

## Validation Expectations

Before an operational Jurisdiction SREG is published, Registry should confirm:

- the Source Institution is identified;
- the Authoritative Source Record exists;
- the Source-System Identifier is preserved when available;
- the proposed Registry Identifier is valid;
- the Jurisdiction Record Type is appropriate;
- the parent-jurisdiction relationship is valid;
- required public references exist;
- Registry Status and Source-Record Status are separate;
- version metadata is complete;
- the SREG satisfies the applicable schema;
- human-readable and machine-readable forms agree.

Registry validation does not independently certify the jurisdiction record.

---

## Correction Example

A future correction might address:

- an incorrect parent jurisdiction;
- a broken Atlas reference;
- an incorrect subdivision code;
- a classification error;
- an outdated Source-Record version;
- a missing relationship;
- schema nonconformance.

A material correction should preserve:

```text
Prior Example Version
  ↓
Documented Correction
  ↓
Replacement Example Version
```

For an operational SREG, correction history would be preserved under Registry policy and procedure.

---

## Production Requirements

This example must not be converted directly into a production SREG without:

- confirming the Authoritative Source Record;
- obtaining the real Atlas Source-System Identifier;
- assigning an official Registry Identifier;
- applying the published Jurisdiction Record-Type Profile;
- validating required fields and relationships;
- confirming Registry and source status values;
- publishing consistent human-readable and machine-readable artifacts;
- completing the approved Registry registration procedure.

---

## Example Record Disclaimer

This file is an illustrative example.

It does not constitute:

- an official SREG;
- an Atlas jurisdiction record;
- registration;
- certification;
- attestation;
- verification;
- government recognition;
- legal authority;
- ownership;
- endorsement.

California exists independently of this example.

Atlas would remain authoritative for Atlas jurisdiction intelligence.

Registry would remain authoritative only for an officially created and published SREG.

---

## Guiding Statement

> The jurisdiction exists independently.
>
> Atlas creates the authoritative jurisdiction resource.
>
> Registry creates the SREG that preserves the structured path back to it.
