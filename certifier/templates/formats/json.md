# JSON Format Template

This document defines the JSON formatting principles, recommendations, and conventions used by the Satoshium Certifier framework.

JSON serves as the primary structured data format for certification records, evidence references, registry entries, receipts, reports, and future subsystem interoperability.

While HTML and Markdown are optimized for human consumption, JSON is optimized for consistency, validation, automation, and machine-readable exchange.

---

# Purpose

The purpose of the JSON format is to provide a structured representation of Certifier artifacts that can be:

* Parsed
* Validated
* Stored
* Indexed
* Queried
* Transmitted
* Preserved
* Automated

JSON provides the foundational data format for Certifier records.

---

# Format Philosophy

Certifier operates at two levels:

```text
Human Readable
      ↓
Markdown
HTML
TXT

Machine Readable
      ↓
JSON
```

JSON is considered the preferred format for structured interoperability.

Human-facing formats may be generated from JSON records whenever practical.

---

# Design Principles

JSON records should be:

* Consistent
* Predictable
* Structured
* Extensible
* Portable
* Versioned
* Machine-readable

The objective is long-term usability rather than short-term convenience.

---

# Why JSON

JSON was selected because it is:

* Widely supported
* Human-readable
* Machine-readable
* Language independent
* Easily validated
* Suitable for APIs
* Suitable for archival storage

JSON provides a practical balance between readability and interoperability.

---

# Relationship to Schemas

JSON records should conform to applicable Certifier schemas.

Example:

```text
schemas/
└── certification-schema.json
```

Relationship:

```text
Schema
    ↓
Validation
    ↓
JSON Record
```

Schemas define structure.

JSON implements structure.

---

# Core Record Example

Example Certification Record:

```json
{
  "record_id": "SCRD-2026-000001",
  "target_name": "Atlas Initial Build Phase",
  "target_type": "tool",
  "certification_class": "verified",
  "status": "pass",
  "lifecycle_state": "certified",
  "certification_date": "2026-07-25"
}
```

This example demonstrates a simplified Certification Record.

---

# Receipt Example

Example Certification Receipt:

```json
{
  "receipt_id": "SCR-2026-000001",
  "record_id": "SCRD-2026-000001",
  "target_name": "Atlas Initial Build Phase",
  "certification_class": "verified",
  "status": "pass",
  "date_issued": "2026-07-25"
}
```

---

# Report Example

Example Certification Report Reference:

```json
{
  "report_id": "SCPR-2026-000001",
  "record_id": "SCRD-2026-000001",
  "target_name": "Atlas Initial Build Phase",
  "review_method": "human-ai-assisted",
  "determination": "pass"
}
```

---

# Evidence Example

Example Evidence Reference:

```json
{
  "evidence_id": "SEV-2026-000001",
  "evidence_type": "screenshot",
  "file_name": "atlas-homepage.png",
  "related_record": "SCRD-2026-000001"
}
```

---

# Naming Conventions

Property names should use:

```text
snake_case
```

Example:

```json
{
  "record_id": "SCRD-2026-000001",
  "target_name": "Atlas Initial Build Phase"
}
```

Avoid:

```json
{
  "RecordID": "SCRD-2026-000001",
  "TargetName": "Atlas Initial Build Phase"
}
```

Consistency improves interoperability.

---

# Required Fields

Required fields should be defined by the applicable schema.

Examples may include:

```json
{
  "record_id": "",
  "target_name": "",
  "target_type": "",
  "status": ""
}
```

Validation requirements should originate from schema definitions rather than individual JSON records.

---

# Date Format

Dates should use ISO 8601 whenever practical.

Example:

```json
{
  "certification_date": "2026-07-25"
}
```

Timestamp example:

```json
{
  "created_at": "2026-07-25T15:30:00Z"
}
```

Standardized dates improve portability and consistency.

---

# Identifier Format

Identifiers should preserve Certifier naming conventions.

Examples:

```json
{
  "record_id": "SCRD-2026-000001",
  "receipt_id": "SCR-2026-000001",
  "report_id": "SCPR-2026-000001",
  "registry_id": "SREG-2026-000001"
}
```

Stable identifiers improve traceability.

---

# Versioning

Structured records should support version tracking.

Example:

```json
{
  "version": "1.0"
}
```

Versioning improves compatibility across future Certifier revisions.

---

# Relationship to HTML

JSON and HTML serve different purposes.

```text
JSON
-----
Structured Data

HTML
-----
Presentation Layer
```

Relationship:

```text
JSON Record
      ↓
HTML Rendering
```

The content remains the same.

The presentation differs.

---

# Relationship to Markdown

Markdown is optimized for authoring.

JSON is optimized for structure.

Example workflow:

```text
Markdown
     ↓
JSON Record
     ↓
HTML Publication
```

Multiple representations may coexist for the same certification activity.

---

# Relationship to Registry

Registry interoperability is expected to rely heavily on JSON.

Examples include:

* Registry exports
* Registry imports
* Search indexes
* Metadata catalogs
* Record exchanges

JSON provides a natural exchange format.

---

# Relationship to Anchor

Future Anchor integrations may preserve hashes associated with JSON records.

Example:

```text
JSON Record
      ↓
SHA-256 Hash
      ↓
Anchor Reference
```

Structured records simplify preservation and integrity verification.

---

# Relationship to Attestor

Future Attestor workflows may validate JSON-based certification records.

Shared data structures improve consistency across systems.

Example:

```text
JSON Record
      ↓
Attestation Review
      ↓
Attestation Record
```

---

# Long-Term Vision

JSON is expected to become the primary structured data format used throughout the Certifier ecosystem.

While reports, receipts, and standards may be viewed as documents, JSON records provide the underlying structured representation required for:

* Automation
* Validation
* Discovery
* Preservation
* Interoperability

As Registry, Anchor, Attestor, and future subsystems emerge, JSON is likely to become the common language connecting them.

The objective is simple:

A certification record should be understandable by software as easily as it is by people.

---

# Related Formats

See:

```text
templates/formats/html.md
templates/formats/markdown.md
templates/formats/txt.md
templates/formats/pdf.md
```

for additional format guidance.

---

# Guiding Statement

> Markdown authors.
>
> HTML publishes.
>
> JSON structures.
>
> The JSON format exists to make certification records consistent, portable, and machine-readable.
