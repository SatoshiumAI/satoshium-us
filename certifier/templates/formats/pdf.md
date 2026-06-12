# PDF Format Template

This document defines the PDF formatting principles, recommendations, and conventions used by the Satoshium Certifier framework.

PDF serves as a portable document format intended for distribution, archival, preservation, printing, evidence packages, and long-term recordkeeping.

While Markdown serves as the preferred authoring format and JSON serves as the preferred structured data format, PDF provides a stable presentation format suitable for sharing and preservation.

---

# Purpose

The purpose of the PDF format is to provide a portable and consistent representation of Certifier artifacts.

Typical uses include:

* Certification Reports
* Certification Receipts
* Certification Packages
* Standards Documentation
* Evidence Bundles
* Registry Exports
* Historical Records
* Supporting Documentation
* Statement of Use (SOU) Evidence

PDF is intended to preserve appearance and formatting across systems and platforms.

---

# Format Philosophy

Certifier distinguishes between:

```text id="rh6pxj"
Authoring
    ↓
Markdown

Structured Data
    ↓
JSON

Publication
    ↓
HTML

Preservation
    ↓
PDF
```

PDF serves as the preferred preservation and distribution format.

---

# Why PDF

PDF was selected because it is:

* Portable
* Widely supported
* Printable
* Shareable
* Archivable
* Platform independent
* Presentation stable

A PDF document generally appears the same regardless of operating system, browser, or software environment.

---

# Typical PDF Outputs

Examples include:

## Certification Reports

Formal review records prepared for preservation or distribution.

Examples:

```text id="24s6f5"
certification-report-2026-000001.pdf
```

---

## Certification Receipts

Portable certification summaries.

Examples:

```text id="4wpl2s"
receipt-2026-000001.pdf
```

---

## Certification Packages

Combined certification artifacts.

Examples:

```text id="r8wwt4"
atlas-initial-build-certification-package.pdf
```

A package may include:

* Receipt
* Report
* Evidence Summary
* References

---

## Standards Publications

Published certification standards.

Examples:

```text id="rmy6uk"
atlas-initial-build-standard-v1.pdf
```

---

## Registry Exports

Portable Registry records.

Examples:

```text id="4frh34"
verified-records-export.pdf
```

---

# Design Principles

PDF outputs should be:

* Readable
* Consistent
* Printable
* Professional
* Accessible
* Archivable

The objective is clarity and durability.

---

# Recommended Document Elements

When practical, PDF artifacts should include:

* Title
* Identifier
* Version
* Date
* Author or Generator
* Classification Information
* Page Numbers
* References
* Disclaimer

These elements improve traceability and preservation value.

---

# Suggested Metadata

PDF documents should preserve metadata whenever practical.

Examples:

```text id="h1o3hu"
Title
Author
Subject
Keywords
Version
Creation Date
Record Identifier
```

Metadata improves discovery and archival management.

---

# Identifier Preservation

Identifiers should remain visible within PDF outputs.

Examples:

```text id="qst4vk"
SCRD-2026-000001
SCR-2026-000001
SCPR-2026-000001
SREG-2026-000001
```

Identifiers improve traceability and future reference.

---

# Relationship to Markdown

Most Certifier PDF artifacts are expected to originate from Markdown.

Example workflow:

```text id="3f5jlwm"
Markdown
     ↓
PDF
```

Markdown remains the preferred authoring format.

PDF becomes the preservation format.

---

# Relationship to JSON

JSON may serve as the structured source for PDF generation.

Example workflow:

```text id="w6y8vd"
JSON Record
      ↓
Rendered Report
      ↓
PDF
```

JSON provides structure.

PDF provides presentation.

---

# Relationship to HTML

Some PDF artifacts may originate from HTML.

Example workflow:

```text id="it6v8s"
HTML
    ↓
PDF
```

This is especially useful for published reports and Registry entries.

---

# Relationship to Evidence

PDF may be used to package evidence references.

Examples include:

* Screenshot indexes
* Evidence summaries
* Hash listings
* Certification appendices

Evidence should remain traceable to original sources whenever practical.

---

# Relationship to Registry

Registry may eventually support PDF exports.

Examples:

* Registry catalogs
* Certification summaries
* Historical certification indexes

PDF exports provide a portable snapshot of Registry records.

---

# Relationship to Chronicle

Significant milestones may eventually be preserved as PDF records.

Examples:

* Atlas Initial Build Certification
* Certifier Launch
* First Verified Certification
* Major Standards Releases

PDF provides durable historical documentation.

---

# Relationship to Anchor

Future Anchor integrations may preserve hashes associated with PDF artifacts.

Example:

```text id="h6l7v9"
PDF
 ↓
SHA-256 Hash
 ↓
Anchor Record
```

This supports integrity verification and long-term preservation.

---

# Relationship to Attestor

Future Attestor activities may review or validate PDF certification artifacts.

Examples:

* Certification Reports
* Certification Receipts
* Certification Packages

Portable documents simplify independent review.

---

# Accessibility Recommendations

Whenever practical:

* Use searchable text.
* Avoid image-only documents.
* Preserve document structure.
* Support screen readers.
* Include meaningful titles and headings.

Accessibility improves long-term usability.

---

# Preservation Philosophy

PDF is intended to support long-term preservation.

Whenever practical:

* Preserve source documents.
* Preserve identifiers.
* Preserve metadata.
* Preserve references.
* Preserve revision history.

PDF should supplement source records rather than replace them.

---

# Relationship to SOU Activities

PDF may become particularly useful for future trademark and Statement of Use activities.

Examples include:

* Service documentation
* Certification reports
* Operational evidence packages
* Historical records
* Public-facing outputs

Portable and printable records may simplify future documentation efforts.

---

# Long-Term Vision

PDF is expected to serve as the primary preservation and distribution format for Certifier.

Markdown creates.

JSON structures.

HTML publishes.

PDF preserves.

As the Satoshium ecosystem expands, PDF may become the preferred format for archival records, certification packages, Registry exports, evidence bundles, and historical documentation.

The objective is simple:

A certification record should remain portable, readable, and preservable for decades.

---

# Related Formats

See:

```text id="t3d4k5"
templates/formats/markdown.md
templates/formats/json.md
templates/formats/html.md
templates/formats/txt.md
```

for additional format guidance.

---

# Guiding Statement

> Markdown authors.
>
> JSON structures.
>
> HTML publishes.
>
> PDF preserves.
>
> The PDF format exists to create durable and portable certification records.
