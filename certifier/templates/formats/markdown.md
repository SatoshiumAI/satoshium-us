# Markdown Format Template

This document defines the Markdown formatting principles, recommendations, and conventions used by the Satoshium Certifier framework.

Markdown serves as the primary authoring format for Certifier documentation, standards, reports, receipts, templates, and supporting records.

Markdown was selected because it is lightweight, human-readable, version-control friendly, and broadly supported throughout modern publishing and software ecosystems.

---

# Purpose

The purpose of the Markdown format is to provide a simple and durable format for creating and maintaining Certifier artifacts.

Typical uses include:

* Certification Reports
* Certification Receipts
* Standards Documentation
* Registry Records
* Evidence Notes
* Templates
* Repository Documentation
* Historical Records

Markdown is intended to be both easy to write and easy to preserve.

---

# Format Philosophy

Certifier distinguishes between:

```text
Authoring
    ↓
Markdown

Structured Data
    ↓
JSON

Publication
    ↓
HTML
PDF
TXT
```

Markdown serves as the preferred authoring layer.

Many Certifier artifacts may originate in Markdown before being rendered into other formats.

---

# Why Markdown

Markdown was selected because it is:

* Human-readable
* Plain text
* Version-control friendly
* Platform independent
* Easy to archive
* Easy to render
* Widely supported

Markdown remains useful even when specialized software becomes unavailable.

---

# Recommended Document Structure

Most Certifier documents should follow a consistent structure.

Example:

```markdown
# Document Title

## Overview

...

## Purpose

...

## Content

...

## Long-Term Vision

...

## Guiding Statement

> Example statement.
```

Consistency improves readability and maintainability.

---

# Heading Structure

Use logical heading levels.

Recommended pattern:

```markdown
# Title

## Major Section

### Subsection

#### Detail
```

Avoid skipping heading levels whenever practical.

Preferred:

```markdown
# Title

## Section

### Subsection
```

Avoid:

```markdown
# Title

#### Subsection
```

---

# Lists

Use unordered lists for collections of related items.

Example:

```markdown
- Item One
- Item Two
- Item Three
```

Use ordered lists when sequence matters.

Example:

```markdown
1. Review
2. Evidence
3. Certification
4. Receipt
```

---

# Tables

Tables may be used when structured comparison improves readability.

Example:

```markdown
| Class | Description |
|---------|---------|
| Informational | Documented |
| Operational | Functional |
| Verified | Reviewed |
```

Tables should remain simple and readable.

---

# Code Blocks

Use fenced code blocks for:

* Examples
* Templates
* JSON
* Workflows
* File structures

Example:

````markdown
```json
{
  "record_id": "SCRD-2026-000001"
}
```
````

Code blocks should include language identifiers whenever practical.

---

# File Structure Examples

Repository structures should use fenced text blocks.

Example:

```text
certifier/
├── docs/
├── schemas/
├── standards/
└── templates/
```

This improves readability and consistency.

---

# Quotes

Blockquotes may be used for:

* Principles
* Definitions
* Guidance
* Guiding Statements

Example:

```markdown
> Certification should be supported by reviewable evidence.
```

Quotes should be used sparingly and intentionally.

---

# Identifier References

Identifiers should be written consistently.

Examples:

```text
SCRD-2026-000001
SCR-2026-000001
SCPR-2026-000001
SREG-2026-000001
```

Consistent identifiers improve traceability.

---

# Naming Conventions

Markdown files should generally use:

```text
lowercase-with-hyphens.md
```

Examples:

```text
certifier-overview.md
certification-philosophy.md
status-definitions.md
```

Avoid:

```text
CertifierOverview.md
MyFile.md
Document_Final_V2.md
```

Consistency improves maintainability.

---

# Relationship to JSON

Markdown and JSON serve different purposes.

```text
Markdown
---------
Human Authoring

JSON
---------
Machine Structure
```

Relationship:

```text
Markdown
     ↓
Structured Record
     ↓
JSON
```

The content may be identical while the representation differs.

---

# Relationship to HTML

Markdown often serves as the source for HTML publication.

Example workflow:

```text
Markdown
     ↓
HTML
```

This allows a single source document to support multiple output formats.

---

# Relationship to PDF

Many PDF outputs may originate from Markdown documents.

Example workflow:

```text
Markdown
     ↓
PDF
```

Markdown therefore serves as an effective preservation and publishing format.

---

# Relationship to Reports

Certification Reports are expected to be authored primarily in Markdown.

Example:

```text
reports/
└── certification-report-2026-000001.md
```

Markdown provides a balance between readability and portability.

---

# Relationship to Receipts

Certification Receipts may also be authored in Markdown.

Example:

```text
receipts/
└── receipt-2026-000001.md
```

Alternative renderings may later be generated in HTML or PDF.

---

# Relationship to Standards

Certification Standards are expected to be maintained primarily as Markdown documents.

Examples:

```text
standards/
└── atlas-initial-build-standard-v1.md
```

Markdown simplifies review, revision, and version control.

---

# Preservation Philosophy

Markdown is fundamentally plain text.

This provides significant preservation benefits.

Markdown documents remain readable:

* Without specialized software
* Across operating systems
* Across platforms
* Across decades

This aligns with Certifier's emphasis on long-term accessibility and historical preservation.

---

# Long-Term Vision

Markdown is expected to become the primary authoring language of Certifier.

Documentation, standards, reports, receipts, registry records, and historical references may all originate as Markdown documents.

As the Satoshium ecosystem expands, Markdown may serve as the common authoring layer connecting:

* Atlas
* Certifier
* Registry
* Chronicle
* Anchor
* Attestor

The objective is simple:

A certification record should remain understandable long after the software used to create it has changed.

---

# Related Formats

See:

```text
templates/formats/json.md
templates/formats/html.md
templates/formats/txt.md
templates/formats/pdf.md
```

for additional format guidance.

---

# Guiding Statement

> JSON structures.
>
> HTML publishes.
>
> Markdown authors.
>
> The Markdown format exists to create durable, portable, and human-readable certification records.
