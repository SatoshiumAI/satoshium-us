# Satoshium Certifier — Template Formats

**Path:** `/certifier/templates/formats/`  
**Institution:** Satoshium Certifier  
**Surface:** Template Format Documentation  
**Status:** Current repository documentation

## Purpose

This directory contains format-specific documentation for **Satoshium Certifier templates**.

It describes the supported presentation and serialization formats used when Certifier templates are expressed as human-readable, machine-readable, or portable artifacts.

The directory currently contains:

- `html.md`
- `json.md`
- `markdown.md`
- `pdf.md`
- `txt.md`

This README serves as the repository entry point for the format documentation set.

## Role of the Format Layer

The format layer documents how Certifier template content may be represented in different technical forms.

Formats are presentation or serialization mechanisms.

They do not independently define:

- certification authority;
- Certification Package semantics;
- certification decisions;
- Suite Standards;
- Suite Methodology; or
- downstream Suite object authority.

The underlying governed Certifier record remains authoritative according to its canonical object and institutional context.

## Current Format Documentation

### `html.md`

Documents HTML-oriented template representation.

HTML may be used for public-facing, human-readable Certifier artifacts or template outputs.

### `json.md`

Documents JSON-oriented template representation.

JSON may be used for structured, machine-readable Certifier artifacts, schema-compatible records, or interoperability.

### `markdown.md`

Documents Markdown-oriented template representation.

Markdown may be used for repository-native documentation, review records, templates, or human-readable source material.

### `pdf.md`

Documents PDF-oriented template representation.

PDF may be used for portable, fixed-layout presentation or archival distribution where appropriate.

### `txt.md`

Documents plain-text template representation.

Plain text may be used for minimal, portable, tool-independent representations or supporting outputs.

## Canonical Record Boundary

A representation format does not create a new canonical object merely because the same governed content appears in another format.

For example:

```text
Canonical Certifier Record
        ↓
Representation / Serialization
        ↓
HTML · JSON · Markdown · PDF · TXT
```

Where multiple representations refer to the same governed Certifier object, the canonical source and governing object relationship should remain explicit.

## Relationship to Certification Packages

The **Certification Package** remains Certifier's canonical operational record.

Format templates may support records derived from or associated with the Certification Package.

They do not replace it.

## Relationship to Generated Certifier Artifacts

Format documentation may support artifacts such as:

- Certification Process Reports (SCPR);
- Certification Receipts (SCR);
- Certified Records (SCRD);
- evidence-related outputs;
- template-based operational records; and
- repository documentation.

Each artifact should preserve its own canonical role and provenance.

## HTML / JSON Representation Discipline

Where HTML and JSON represent the same governed Certifier object, they should remain synchronized.

A serialization difference should not silently create a second semantic object.

For SCRD specifically:

```text
SCRD
├── HTML representation
└── JSON representation
```

The representations remain subordinate to the canonical Certification Package.

## Format Neutrality

The meaning of a governed Certifier record should not depend solely on presentation format.

A format may affect:

- readability;
- machine processing;
- transport;
- rendering;
- archival convenience; or
- interoperability.

It should not independently alter:

- certification outcome;
- institutional authority;
- object identity;
- lifecycle state; or
- provenance.

## Versioning

Format documentation and templates should be versioned when substantive structural changes occur.

Historical outputs should remain understandable relative to the template and format rules that existed when they were created.

Format evolution should avoid silently changing the meaning of previously issued records.

## Interoperability

Structured formats may support governed exchange with other Suite institutions.

Such exchange must preserve institutional boundaries.

For example:

- Registry may reference governed Certifier records.
- Chronicle may preserve chronology.
- Anchor may preserve Integrity References.
- Beacon may publish Discovery Signals / Discovery Metadata.
- Attestor may consume eligible governed inputs.
- Navigator may orchestrate workflows.

Formats facilitate exchange.

They do not transfer authority.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Repository Expectations

Changes to this directory should preserve:

1. format as representation rather than authority;
2. the Certification Package as Certifier's canonical operational record;
3. object identity across multiple representations;
4. provenance and version traceability;
5. synchronization where multiple formats represent the same governed object;
6. separation between Certifier records and downstream Suite objects; and
7. the rule that reference does not transfer authority.

## Reconciliation Note

This README documents the directory structure visible in the repository and the currently established Certifier architecture.

The five individual format documents have not been independently reconciled as part of this directory-level README pass.

Later file-by-file review should check for:

- stale canonical object names;
- old Attestor terminology;
- outdated Suite institution roles;
- representation language that implies duplicate canonical objects;
- format-specific authority claims; and
- outdated lifecycle or publication assumptions.

## Governing Principle

**Format defines representation; it does not redefine the governed Certifier object being represented.**
