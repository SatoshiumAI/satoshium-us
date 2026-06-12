# Registry Jurisdiction Records

## Overview

This document describes how jurisdiction records may be represented within Satoshium Registry.

Jurisdiction records provide structured references to geographic, governmental, political, and administrative entities.

Registry catalogs jurisdiction records to improve discoverability, continuity, and organization across jurisdiction-related information resources.

---

## Purpose

Jurisdiction records exist to answer questions such as:

- What jurisdiction is being referenced?
- What category of jurisdiction is it?
- What related resources exist?
- What media, certifications, or attestations are associated with it?
- How can related records be located?

Jurisdiction records provide a structured framework for answering these questions consistently.

---

## Relationship to Atlas

Jurisdiction records are expected to be closely associated with Atlas.

```text
Atlas
   ↓
Jurisdiction Resources
   ↓
Registry Jurisdiction Records
```

Atlas may create and maintain jurisdiction intelligence resources.

Registry catalogs and organizes those resources.

---

## Jurisdiction Categories

Jurisdiction records may be assigned to categories such as:

### Countries

National-level sovereign entities.

Examples:

- United States
- Canada
- Japan
- Australia

---

### States

Subnational entities within countries.

Examples:

- California
- Texas
- Florida
- New Hampshire

---

### Provinces

Administrative divisions commonly used in various countries.

Examples:

- Ontario
- Alberta
- British Columbia

---

### Territories

Territorial or dependent administrative entities.

---

### Regions

Geographic, administrative, or organizational regions.

---

### Future Categories

Additional jurisdiction categories may be introduced over time.

---

## Example Record Structure

A jurisdiction record may include:

```text
Identifier
Title
Status
Jurisdiction Type
Parent Jurisdiction
References
Related Records
```

Future schemas may expand these requirements.

---

## Example Metadata

| Field | Example |
|---------|---------|
| Record Type | Jurisdiction |
| Status | Active |
| Jurisdiction Type | State |
| Parent Jurisdiction | United States |
| Registry Identifier | JUR-US-CA-0001 |

---

## Related Registry Records

Jurisdiction records may be linked to:

- Tool Records
- Media Records
- Certification Records
- Attestation Records
- Historical Records
- Reference Records

Cross-references improve discoverability and continuity.

---

## Jurisdiction Hierarchy

Jurisdictions may be represented hierarchically.

Example:

```text
World
 └── United States
      └── California
```

Hierarchical structures improve navigation and organization.

---

## Record Lifecycle

Jurisdiction records may move through stages such as:

```text
Created
    ↓
Cataloged
    ↓
Referenced
    ↓
Maintained
    ↓
Preserved
```

Lifecycle management may expand in future Registry versions.

---

## Future Development

Future jurisdiction capabilities may include:

- Expanded geographic hierarchies
- Regional classifications
- Cross-jurisdiction relationships
- Atlas interoperability enhancements
- Historical jurisdiction tracking

Future enhancements should remain aligned with Registry's organizational mission.

---

## Registry Notes

Registry records jurisdiction information.

Registry does not create jurisdictions, define legal boundaries, or establish governmental authority.

Registry provides organizational structure for jurisdiction-related records and references.

---

## Guiding Statement

> Jurisdictions define places.
>
> Registry provides the structure needed to reference those places consistently.
