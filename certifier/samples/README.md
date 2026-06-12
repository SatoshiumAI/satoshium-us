# Samples

This directory contains sample records, examples, demonstrations, and reference implementations used by the Satoshium Certifier framework.

Samples are intended to help users, contributors, reviewers, and future developers understand how Certifier operates in practice.

While standards define requirements and templates define structure, samples demonstrate real-world usage.

---

# Purpose

The purpose of the samples directory is to provide practical examples of Certifier artifacts and workflows.

Samples help answer questions such as:

* What does a Certification Report look like?
* What does a Certification Receipt look like?
* How is a certification record structured?
* How are standards applied?
* How are evidence records documented?
* What should a completed certification package contain?

Samples provide learning through example.

---

# Sample Philosophy

Certifier documentation describes how the framework operates.

Samples demonstrate how the framework is used.

Example relationship:

```text id="f4m2ya"
Standard
     ↓
Template
     ↓
Sample
```

Standards define expectations.

Templates provide structure.

Samples show implementation.

---

# What Belongs Here

Examples of sample materials include:

## Certification Reports

Example certification reports demonstrating report structure and content.

Examples:

```text id="3q9j7e"
sample-certification-report.md
atlas-certification-example.md
```

---

## Certification Receipts

Example receipts demonstrating public certification outputs.

Examples:

```text id="0y7kld"
sample-receipt.md
atlas-receipt-example.md
```

---

## Certification Records

Example certification records using the Certifier schema.

Examples:

```text id="5vc4ep"
sample-certification-record.json
```

---

## Evidence Packages

Example evidence collections.

Examples:

```text id="b2n5sz"
sample-evidence-package/
```

---

## Registry Entries

Example Registry-ready records.

Examples:

```text id="y9k3jx"
sample-registry-entry.md
```

---

## Complete Certification Packages

Example end-to-end certification events.

Examples:

```text id="xt5v1r"
atlas-initial-build-example/
```

This type of sample may include:

* Certification Record
* Certification Report
* Certification Receipt
* Evidence References
* Registry Entry

---

# Suggested Structure

```text id="k8y1dq"
samples/
├── reports/
├── receipts/
├── records/
├── evidence/
├── registry/
└── complete-packages/
```

Additional categories may be added as Certifier evolves.

---

# Educational Purpose

Samples are intended to support:

* Learning
* Documentation
* Onboarding
* Development
* Testing
* Demonstration
* Standard interpretation

Future contributors should be able to review sample materials and quickly understand how Certifier artifacts are expected to be structured.

---

# Example Learning Path

A new contributor might follow:

```text id="6wp1jm"
Overview
     ↓
Certification Philosophy
     ↓
Templates
     ↓
Samples
```

The sample materials provide practical context after the framework concepts have been introduced.

---

# Relationship to Templates

Templates define the official structure of Certifier artifacts.

Samples demonstrate completed implementations of those templates.

Example:

```text id="owg7ph"
receipt-template.md
        ↓
sample-receipt.md
```

```text id="7tr2ui"
report-template.md
        ↓
sample-certification-report.md
```

Templates provide the blueprint.

Samples provide the finished example.

---

# Relationship to Standards

Samples may demonstrate how certification standards are applied.

Example:

```text id="4k7mtm"
Certification Standard
          ↓
Review Process
          ↓
Sample Certification Report
```

This helps reviewers understand how standards translate into actual certification outcomes.

---

# Relationship to Atlas

Atlas is expected to become the first major source of sample certification materials.

Examples may include:

* Atlas Initial Build Certification
* Atlas Workflow Certification
* Atlas Service Certification
* Atlas Publication Workflow Review

These examples may serve as foundational reference implementations for future Certifier activities.

---

# Relationship to Testing

Samples may also be used for:

* Schema validation
* Documentation testing
* Process verification
* Demonstration environments

Samples should be clearly identified as examples when they do not represent actual certification events.

---

# Sample Naming Convention

Recommended format:

```text id="c5x3bo"
sample-[artifact-name].[extension]
```

Examples:

```text id="d7m4ku"
sample-receipt.md
sample-report.md
sample-registry-entry.md
sample-certification-record.json
```

For real-world examples:

```text id="q1s9te"
atlas-initial-build-report.md
atlas-initial-build-receipt.md
```

---

# Relationship to Future Subsystems

Sample materials may eventually demonstrate interoperability with:

* Atlas
* Registry
* Chronicle
* Anchor
* Attestor

As the ecosystem expands, examples may become increasingly valuable for documenting subsystem interactions.

---

# Long-Term Vision

The samples directory serves as the practical learning library of Certifier.

Documentation explains concepts.

Templates define structure.

Samples demonstrate implementation.

Years from now, future contributors should be able to review sample materials and quickly understand how certification activities were performed, documented, and preserved.

The objective is not merely to describe Certifier.

The objective is to show Certifier in action.

---

# Related Documentation

For additional information, see:

```text id="e7w6jk"
docs/receipt-template.md
docs/report-template.md
docs/workflow-diagram.md
docs/interoperability.md
schemas/certification-schema.json
```

---

# Guiding Statement

> Standards define.
>
> Templates structure.
>
> Samples demonstrate.
>
> The samples directory exists to show how Certifier works in practice.
