# HTML Format Template

This document defines the HTML formatting principles, recommendations, and conventions used by the Satoshium Certifier framework.

HTML serves as one of the primary presentation formats for certification artifacts and supports publication, sharing, indexing, archival, and future interoperability.

While certification records may originate in structured formats such as JSON or Markdown, HTML provides a widely supported format for public display and long-term accessibility.

---

# Purpose

The purpose of the HTML format is to provide a human-readable representation of Certifier artifacts suitable for web publication and browser-based viewing.

Typical uses include:

* Certification Reports
* Certification Receipts
* Registry Entries
* Evidence Summaries
* Standards Documentation
* Public Certification Records

HTML provides a portable and broadly accessible presentation format.

---

# Format Philosophy

Certifier distinguishes between:

```text
Data
  ↓
Structure
  ↓
Presentation
```

Example:

```text
JSON
  ↓
HTML
```

The underlying certification record remains unchanged.

HTML controls presentation.

---

# Design Principles

HTML representations should be:

* Readable
* Accessible
* Portable
* Searchable
* Printable
* Archivable

Whenever practical, HTML outputs should avoid unnecessary complexity.

Certifier favors clarity over visual decoration.

---

# Recommended Document Structure

A typical HTML document should contain:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Certification Receipt</title>
</head>
<body>

    <header>
        ...
    </header>

    <main>
        ...
    </main>

    <footer>
        ...
    </footer>

</body>
</html>
```

This structure promotes consistency across Certifier outputs.

---

# Recommended Metadata

HTML artifacts should include metadata whenever practical.

Examples:

```html
<meta name="generator" content="Satoshium Certifier">
<meta name="record-id" content="SCRD-2026-000001">
<meta name="certification-class" content="Verified">
<meta name="status" content="Pass">
<meta name="date-certified" content="2026-07-25">
```

Metadata supports interoperability and future automation.

---

# Certification Receipt Example

Example structure:

```html
<article>

<h1>Certification Receipt</h1>

<p><strong>Receipt ID:</strong> SCR-2026-000001</p>

<p><strong>Target:</strong> Atlas Initial Build Phase</p>

<p><strong>Class:</strong> Verified</p>

<p><strong>Status:</strong> Pass</p>

<p><strong>Date:</strong> 2026-07-25</p>

</article>
```

This example illustrates a simple public-facing certification receipt.

---

# Certification Report Example

Example structure:

```html
<article>

<h1>Certification Report</h1>

<section>
<h2>Executive Summary</h2>
<p>...</p>
</section>

<section>
<h2>Evidence Reviewed</h2>
<p>...</p>
</section>

<section>
<h2>Findings</h2>
<p>...</p>
</section>

<section>
<h2>Determination</h2>
<p>Pass</p>
</section>

</article>
```

Reports may contain substantially more detail than receipts.

---

# Registry Entry Example

Example structure:

```html
<article>

<h1>Registry Entry</h1>

<p><strong>Registry ID:</strong> SREG-2026-000001</p>

<p><strong>Target:</strong> Atlas Initial Build Phase</p>

<p><strong>Certification Class:</strong> Verified</p>

<p><strong>Status:</strong> Pass</p>

</article>
```

Registry entries should remain concise and discoverable.

---

# Accessibility Recommendations

Whenever practical:

* Use semantic HTML elements.
* Use meaningful headings.
* Preserve logical document structure.
* Avoid conveying meaning solely through color.
* Support keyboard navigation.
* Support screen readers.

Accessibility improves long-term usability.

---

# Styling Philosophy

HTML formatting should remain independent of visual styling whenever practical.

Recommended separation:

```text
Content
    ↓
HTML

Presentation
    ↓
CSS
```

This improves portability and maintainability.

---

# Print Compatibility

Certification artifacts may eventually be:

* Printed
* Archived
* Submitted as supporting evidence
* Preserved as historical records

HTML outputs should therefore remain reasonably printable without requiring extensive modification.

---

# Searchability

HTML outputs should support indexing and discovery.

Benefits include:

* Search engine indexing
* Registry discovery
* Internal repository search
* Historical research

Readable content improves discoverability.

---

# Relationship to JSON

JSON and HTML serve different purposes.

Example:

```text
JSON
-----
Machine-readable

HTML
-----
Human-readable
```

Relationship:

```text
Certification Record
        ↓
JSON
        ↓
HTML Rendering
```

Both may describe the same certification activity.

---

# Relationship to Markdown

Many Certifier artifacts may originate in Markdown.

Example workflow:

```text
Markdown
     ↓
HTML
```

This allows documentation and reports to be published in multiple formats while preserving content consistency.

---

# Relationship to Registry

Registry may eventually publish certification records as HTML pages.

Examples:

* Certification Receipts
* Registry Entries
* Public Reports
* Certification Indexes

HTML provides a natural publication format.

---

# Relationship to Atlas

Atlas certification activities may become the first major consumers of HTML outputs.

Examples include:

* Atlas certification receipts
* Atlas certification reports
* Atlas Registry entries

These artifacts may be published as standalone HTML pages.

---

# Long-Term Vision

HTML is expected to become one of the primary public-facing formats used by Certifier.

While JSON supports structured interoperability and Markdown supports authoring, HTML provides broad accessibility and publication capabilities.

As the Satoshium ecosystem expands, HTML may serve as the preferred format for:

* Public certification records
* Registry publication
* Historical archives
* Standards publication
* Future subsystem interoperability

The objective is simple:

A certification record should be understandable in any modern web browser.

---

# Related Formats

See:

```text
templates/formats/json.md
templates/formats/markdown.md
templates/formats/txt.md
templates/formats/pdf.md
```

for additional format guidance.

---

# Guiding Statement

> JSON structures.
>
> Markdown authors.
>
> HTML publishes.
>
> The HTML format exists to make certification records accessible, portable, and visible.
