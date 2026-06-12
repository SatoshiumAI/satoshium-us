# Registry Media Records

## Overview

This document describes how media records may be represented within Satoshium Registry.

Media records provide structured references to videos, images, thumbnails, graphics, audio resources, documents, media pages, and future media assets.

Registry catalogs media resources to improve discoverability, continuity, organization, and long-term reference management.

---

## Purpose

Media records exist to answer questions such as:

- What media resource exists?
- What category does it belong to?
- What jurisdiction or tool is it associated with?
- What related records exist?
- Where can the media be found?

Media records provide a consistent framework for answering these questions.

---

## Relationship to the Ecosystem

Media records may originate from multiple areas of the Satoshium ecosystem.

Examples include:

```text
Atlas
Certifier
Registry
Chronicle
Anchor
Attestor
```

Registry serves as the organizational layer connecting these media resources.

---

## Media Categories

Media records may be assigned to categories such as:

### Videos

Examples:

- Orientation videos
- Educational videos
- Demonstration videos
- Project updates

---

### Images

Examples:

- Graphics
- Illustrations
- Diagrams
- Visual assets

---

### Thumbnails

Examples:

- YouTube thumbnails
- Media preview images
- Social media images

---

### Audio

Examples:

- Podcasts
- Recordings
- Audio briefings

---

### Documents

Examples:

- PDFs
- Reports
- Publications
- Reference materials

---

### Media Pages

Examples:

- Landing pages
- Orientation pages
- Media collections
- Resource hubs

---

## Example Record Structure

A media record may include:

```text
Identifier
Title
Status
Media Type
Associated Resource
References
Related Records
```

Future schemas may expand these requirements.

---

## Example Metadata

| Field | Example |
|---------|---------|
| Record Type | Media |
| Status | Active |
| Media Type | Video |
| Associated Resource | Atlas |
| Registry Identifier | MED-0001 |

---

## Related Registry Records

Media records may be linked to:

- Tool Records
- Jurisdiction Records
- Certification Records
- Attestation Records
- Historical Records
- Reference Records

Cross-references improve discoverability and continuity.

---

## Media Relationships

A media record may be associated with:

```text
Tool
  ↓
Media
  ↓
Jurisdiction
```

or

```text
Jurisdiction
  ↓
Media
  ↓
Certification
```

Registry helps document these relationships.

---

## Record Lifecycle

Media records may move through stages such as:

```text
Created
    ↓
Cataloged
    ↓
Published
    ↓
Referenced
    ↓
Preserved
```

Lifecycle management may expand in future Registry versions.

---

## Future Development

Future media capabilities may include:

- Expanded metadata standards
- Media hierarchies
- Relationship mapping
- Preservation references
- Certification relationships
- Attestation relationships

Future enhancements should remain aligned with Registry's organizational mission.

---

## Registry Notes

Registry records information about media resources.

Registry does not necessarily host media resources directly.

Registry provides organizational structure and discoverability for media-related records and references.

---

## Guiding Statement

> Media communicates information.
>
> Registry helps ensure that information remains discoverable over time.
