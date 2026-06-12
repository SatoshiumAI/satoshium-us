# Templates

This directory contains templates used by the Satoshium Certifier framework.

Templates provide reusable structures, examples, and implementation guidance for creating Certifier artifacts.

Templates help ensure consistency across certification activities while reducing ambiguity and duplication.

They serve as the practical bridge between Certifier documentation and Certifier operations.

---

# Purpose

The purpose of the templates directory is to provide standardized starting points for creating certification-related artifacts.

Templates help answer questions such as:

* How should a Certification Report be structured?
* What should a Certification Receipt contain?
* How should a Registry Entry be formatted?
* What fields belong in a Certification Record?
* How should records be rendered for different output formats?

Templates promote consistency, repeatability, and interoperability.

---

# Template Philosophy

Certifier operates through multiple layers:

```text
Documentation
      ↓
Standards
      ↓
Schemas
      ↓
Templates
      ↓
Implementation
```

Documentation explains concepts.

Standards define requirements.

Schemas define structure.

Templates demonstrate usage.

Implementation produces actual records.

Templates exist to make implementation easier.

---

# Template Categories

Version 1.0 separates templates into two primary categories:

```text
templates/
├── records/
└── formats/
```

Each category serves a different purpose.

---

# Record Templates

Record Templates define the structure of Certifier artifacts.

These templates focus on the content being created.

Examples include:

```text
templates/records/
├── certification-record-template.json
├── certification-report-template.md
├── certification-receipt-template.md
├── registry-entry-template.md
└── attestation-template.md
```

Record templates answer:

> What information should this artifact contain?

---

# Format Templates

Format Templates define how Certifier artifacts may be rendered, exchanged, stored, or published.

Examples include:

```text
templates/formats/
├── json.md
├── markdown.md
├── html.md
├── txt.md
└── pdf.md
```

Format templates answer:

> How should this artifact be presented?

---

# Example Relationship

A Certification Receipt may exist as:

```text
Certification Receipt
        ↓
Record Template
```

and then be rendered as:

```text
JSON
Markdown
HTML
TXT
PDF
```

using Format Templates.

The content remains the same.

The presentation changes.

---

# Why Templates Matter

Templates provide several benefits.

## Consistency

Different contributors can produce similar outputs.

---

## Efficiency

Common structures do not need to be recreated repeatedly.

---

## Quality

Templates encourage complete and properly structured records.

---

## Training

New contributors can learn by example.

---

## Automation

Future software systems may generate records directly from templates.

---

# Relationship to Schemas

Schemas and templates serve different purposes.

Example:

```text
Schema
--------
Defines required fields.

Template
--------
Demonstrates usage of those fields.
```

Relationship:

```text
Schema
     ↓
Template
     ↓
Record
```

Schemas define structure.

Templates demonstrate implementation.

---

# Relationship to Standards

Standards define requirements.

Templates help implement those requirements.

Relationship:

```text
Standard
     ↓
Template
     ↓
Certification Activity
```

Templates should align with applicable standards whenever practical.

---

# Relationship to Reports

Certification Reports may be generated using report templates.

Examples:

```text
certification-report-template.md
```

Templates help ensure consistency across review activities.

---

# Relationship to Receipts

Certification Receipts may be generated using receipt templates.

Examples:

```text
certification-receipt-template.md
```

Templates help create consistent public-facing certification outputs.

---

# Relationship to Registry

Registry-ready records may be generated from Registry Entry Templates.

This promotes consistency between Certifier and future Registry implementations.

---

# Relationship to Atlas

Atlas is expected to become the first major source of real-world template usage.

Examples may include:

* Atlas Initial Build Certification
* Atlas Workflow Certification
* Atlas Service Certification

These activities may become reference implementations for future Certifier templates.

---

# Suggested Structure

Version 1.0 recommends:

```text
templates/
├── README.md
│
├── records/
│   ├── certification-record-template.json
│   ├── certification-report-template.md
│   ├── certification-receipt-template.md
│   ├── registry-entry-template.md
│   └── attestation-template.md
│
└── formats/
    ├── json.md
    ├── markdown.md
    ├── html.md
    ├── txt.md
    └── pdf.md
```

Additional template categories may be introduced as Certifier evolves.

---

# Long-Term Vision

The templates directory serves as the implementation library of Certifier.

Documentation explains.

Standards define.

Schemas structure.

Templates demonstrate.

As the ecosystem expands, templates may support:

* Manual certification activities
* Automated certification workflows
* Registry integration
* Anchor preservation workflows
* Attestation processes
* Future subsystem interoperability

The goal is simple:

A contributor should be able to open a template and immediately understand how to create a valid Certifier artifact.

---

# Related Documentation

For additional information, see:

```text
docs/certification-philosophy.md
docs/workflow-diagram.md
docs/interoperability.md
schemas/certification-schema.json
```

---

# Guiding Statement

> Documentation explains.
>
> Standards define.
>
> Schemas structure.
>
> Templates demonstrate.
>
> The templates directory exists to transform concepts into usable artifacts.
