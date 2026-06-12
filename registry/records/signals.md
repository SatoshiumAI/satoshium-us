# Registry Signal Records

## Overview

This document describes how signal records may be represented within Satoshium Registry.

Signal records provide structured references to formal signals, announcements, declarations, markers, observations, and other notable informational artifacts preserved within the ecosystem.

Registry catalogs signal records to improve discoverability, continuity, organization, and long-term preservation.

---

## Purpose

Signal records exist to answer questions such as:

- What signal was issued?
- When was the signal recorded?
- What information did the signal communicate?
- What records are associated with the signal?
- How can the signal be found later?

Signal records provide a consistent framework for answering these questions.

---

## What Is a Signal?

A signal is an intentional informational artifact preserved for future reference.

Signals may document:

- Discoveries
- Announcements
- Milestones
- Questions
- Observations
- Historical markers
- Ecosystem developments

Signals do not necessarily provide conclusions.

They may simply preserve evidence that information existed at a particular point in time.

---

## Relationship to the Ecosystem

Signal records may originate from multiple areas of the ecosystem.

Examples include:

```text
Atlas
Certifier
Registry
Chronicle
Anchor
Attestor
```

Registry catalogs and organizes those signals.

---

## Potential Signal Categories

### Discovery Signals

Signals documenting discoveries or observations.

---

### Historical Signals

Signals preserving notable milestones or events.

---

### Development Signals

Signals associated with ecosystem growth and development.

---

### Public Signals

Signals intended for public review and reference.

---

### Reference Signals

Signals preserved primarily for continuity and future discoverability.

---

## Example Record Structure

A signal record may include:

```text
Identifier
Title
Status
Signal Type
Date
Description
References
Related Records
```

Future schemas may expand these requirements.

---

## Example Metadata

| Field | Example |
|---------|---------|
| Record Type | Signal |
| Status | Active |
| Signal Type | Historical |
| Date | 2026-08-01 |
| Registry Identifier | SIG-0001 |

---

## Related Registry Records

Signal records may be linked to:

- Tool Records
- Jurisdiction Records
- Media Records
- Certification Records
- Attestation Records
- Historical Records

Cross-references improve discoverability and continuity.

---

## Signal Relationships

Signals often act as connectors between records.

Example:

```text
Event
  ↓
Signal
  ↓
Historical Record
```

or

```text
Discovery
    ↓
Signal
    ↓
Reference Record
```

Registry helps preserve these relationships.

---

## Record Lifecycle

Signal records may move through stages such as:

```text
Created
    ↓
Cataloged
    ↓
Referenced
    ↓
Preserved
```

Lifecycle management may expand in future Registry versions.

---

## Future Development

Future signal capabilities may include:

- Signal classifications
- Signal hierarchies
- Discovery frameworks
- Historical relationships
- Preservation references
- Cross-system interoperability

Future enhancements should remain aligned with Registry's organizational mission.

---

## Registry Notes

Registry records signals.

Registry does not determine the significance of a signal.

Registry provides organizational structure so signals remain discoverable and understandable over time.

---

## Guiding Statement

> A signal may be small.
>
> A signal may be significant.
>
> Registry exists to preserve the possibility that future generations can decide the difference.
