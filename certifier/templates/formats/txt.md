# TXT Format Template

This document defines the TXT formatting principles, recommendations, and conventions used by the Satoshium Certifier framework.

TXT serves as the simplest and most universally accessible format supported by Certifier.

Plain text prioritizes readability, portability, preservation, and independence from specialized software.

While TXT lacks the structure of JSON and the presentation capabilities of HTML and PDF, it provides a durable format suitable for long-term archival and basic record exchange.

---

# Purpose

The purpose of the TXT format is to provide a minimal, human-readable representation of Certifier artifacts.

Typical uses include:

* Archival records
* Registry exports
* Certification summaries
* Backup copies
* Preservation packages
* System-to-system exchange
* Historical recordkeeping
* Plain text evidence bundles

TXT emphasizes accessibility and longevity.

---

# Format Philosophy

Certifier distinguishes between:

```text id="z4q8mn"
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

Universal Fallback
    ↓
TXT
```

TXT serves as the simplest common denominator among all supported formats.

---

# Why TXT

TXT was selected because it is:

* Plain text
* Human-readable
* Software independent
* Platform independent
* Easy to preserve
* Easy to search
* Easy to export
* Universally supported

TXT files can be opened on virtually any computing system.

---

# Design Principles

TXT outputs should be:

* Readable
* Portable
* Searchable
* Simple
* Durable
* Self-contained

The objective is clarity rather than presentation.

---

# Character Encoding

UTF-8 should be used whenever practical.

Example:

```text id="s9v1wa"
Encoding: UTF-8
```

Consistent encoding improves portability and interoperability.

---

# Recommended Structure

TXT artifacts should use clear section headings.

Example:

```text id="x4m6kt"
CERTIFICATION RECEIPT

Receipt ID:
SCR-2026-000001

Target:
Atlas Initial Build Phase

Status:
Pass
```

Simple formatting improves readability.

---

# Heading Conventions

Major headings should be clearly visible.

Example:

```text id="n2p8yr"
CERTIFICATION REPORT
====================
```

or

```text id="8k3xvu"
CERTIFICATION REPORT

--------------------
```

Consistency improves readability.

---

# Certification Receipt Example

Example:

```text id="n4h7pq"
CERTIFICATION RECEIPT

Receipt ID:
SCR-2026-000001

Target:
Atlas Initial Build Phase

Certification Class:
Verified

Status:
Pass

Date:
2026-07-25
```

---

# Certification Report Example

Example:

```text id="7g1jwd"
CERTIFICATION REPORT

Report ID:
SCPR-2026-000001

Target:
Atlas Initial Build Phase

Review Method:
Human-AI-Assisted

Determination:
Pass
```

Reports may contain significantly more detail than receipts.

---

# Registry Entry Example

Example:

```text id="d6f9oe"
REGISTRY ENTRY

Registry ID:
SREG-2026-000001

Target:
Atlas Initial Build Phase

Status:
Pass
```

TXT Registry entries should remain concise.

---

# Identifier Preservation

Identifiers should remain visible and unchanged.

Examples:

```text id="4m1lbh"
SCRD-2026-000001
SCR-2026-000001
SCPR-2026-000001
SREG-2026-000001
```

Identifiers support traceability and long-term reference.

---

# Relationship to Markdown

Markdown often serves as the source for TXT exports.

Example workflow:

```text id="q2r7cs"
Markdown
     ↓
TXT
```

TXT removes formatting while preserving content.

---

# Relationship to JSON

JSON provides structure.

TXT provides readability.

Example:

```text id="6t9vwu"
JSON
-----
Structured Record

TXT
-----
Readable Record
```

Both may represent the same certification artifact.

---

# Relationship to HTML

HTML provides presentation.

TXT provides simplicity.

Example:

```text id="o5m8dy"
HTML
-----
Formatted

TXT
-----
Plain
```

TXT intentionally sacrifices presentation in favor of universality.

---

# Relationship to PDF

PDF preserves appearance.

TXT preserves content.

Example:

```text id="y8j3kg"
PDF
-----
Visual Preservation

TXT
-----
Text Preservation
```

Both serve preservation goals through different approaches.

---

# Relationship to Registry

Registry may eventually support TXT exports.

Examples:

* Registry snapshots
* Certification catalogs
* Historical indexes
* Record summaries

TXT provides a lightweight export format.

---

# Relationship to Chronicle

Historical records may be preserved in TXT format.

Examples include:

* Milestone summaries
* Certification timelines
* Registry snapshots

Plain text remains useful for historical preservation.

---

# Relationship to Anchor

Future Anchor integrations may preserve hashes associated with TXT artifacts.

Example:

```text id="f3n6tw"
TXT Record
     ↓
SHA-256 Hash
     ↓
Anchor Reference
```

TXT files are particularly suitable for integrity verification because they are simple and predictable.

---

# Relationship to Attestor

TXT artifacts may be reviewed, validated, or attested independently.

Their simplicity can make auditing easier.

Example:

```text id="u1p7zy"
TXT Record
     ↓
Review
     ↓
Attestation
```

---

# Searchability

TXT files are highly searchable.

Benefits include:

* Simple indexing
* Full-text search
* Archival retrieval
* Long-term accessibility

Searchability is one of the format's strongest advantages.

---

# Preservation Philosophy

TXT is one of the most durable digital formats available.

Plain text files remain readable:

* Across operating systems
* Across applications
* Across decades
* Across hardware generations

This aligns closely with Certifier's long-term preservation goals.

---

# Long-Term Vision

TXT serves as the universal fallback format of Certifier.

Markdown authors.

JSON structures.

HTML publishes.

PDF preserves appearance.

TXT preserves content.

As the Satoshium ecosystem evolves, TXT may become an important archival and interoperability format because of its simplicity, transparency, and durability.

The objective is simple:

A certification record should remain readable even in the absence of specialized software.

---

# Related Formats

See:

```text id="k9r4fd"
templates/formats/markdown.md
templates/formats/json.md
templates/formats/html.md
templates/formats/pdf.md
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
> PDF preserves appearance.
>
> TXT preserves content.
>
> The TXT format exists to ensure certification records remain readable across time.
