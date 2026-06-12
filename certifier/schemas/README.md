# Schemas

This directory contains structured schema definitions used by the Satoshium Certifier framework.

Schemas provide the machine-readable foundation for certification records, reports, receipts, evidence references, registry entries, and future interoperability activities.

While documentation explains how Certifier works, schemas define how Certifier records are structured.

---

# Purpose

The purpose of the schemas directory is to provide standardized data structures that support consistency, validation, interoperability, automation, and long-term preservation.

Schemas help ensure that certification records remain:

* Consistent
* Predictable
* Portable
* Machine-readable
* Extensible
* Interoperable

Schemas transform certification concepts into structured records that software systems can understand and process.

---

# Schema Philosophy

Certifier operates at two levels:

```text id="c7k4zj"
Human Understanding
        ↓
Machine Understanding
```

Documentation supports human understanding.

Schemas support machine understanding.

Both are necessary.

A certification framework should be understandable by people while remaining usable by software systems.

---

# What Belongs Here

Examples of schema types include:

## Certification Records

Structured representations of certification events.

Examples:

```text id="mq5r4d"
certification-schema.json
```

---

## Receipt Schemas

Future structured definitions for certification receipts.

Examples:

```text id="n4z3gf"
receipt-schema.json
```

---

## Report Schemas

Future structured definitions for certification reports.

Examples:

```text id="q8w2bx"
report-schema.json
```

---

## Evidence Schemas

Future structured definitions for evidence references.

Examples:

```text id="y6h1ta"
evidence-schema.json
```

---

## Registry Schemas

Future structured definitions supporting Registry interoperability.

Examples:

```text id="t9k7uv"
registry-entry-schema.json
```

---

## Attestation Schemas

Future structured definitions supporting Attestor interoperability.

Examples:

```text id="r3p8lo"
attestation-schema.json
```

---

# Current Schema

Version 1.0 currently defines:

```text id="u4f6mj"
certification-schema.json
```

This schema serves as the foundational structure for Certification Records.

The Certification Schema defines:

* Record identifiers
* Certification targets
* Certification classes
* Lifecycle states
* Status values
* Review metadata
* Evidence references
* Determinations
* Outputs
* Historical events

The Certification Schema serves as the core structured record within Certifier.

---

# Why Schemas Matter

Schemas provide several important benefits.

## Consistency

Every certification record follows the same structure.

---

## Validation

Records can be validated against defined requirements.

---

## Interoperability

Subsystems can exchange information reliably.

---

## Automation

Future systems may create, review, catalog, preserve, or verify records automatically.

---

## Preservation

Structured records remain understandable over long periods of time.

---

# Relationship to Documentation

Documentation explains concepts.

Schemas define structure.

Example:

```text id="g5u9wa"
certification-lifecycle.md
          ↓
Lifecycle Fields
          ↓
certification-schema.json
```

Documentation provides meaning.

Schemas provide implementation.

---

# Relationship to Reports

Reports are human-readable.

Schemas are machine-readable.

Example:

```text id="s7n3fy"
Certification Report
          ↓
Narrative Review
```

versus

```text id="z1c6pj"
Certification Schema
          ↓
Structured Record
```

Both describe the same certification activity from different perspectives.

---

# Relationship to Receipts

Future receipt generation may be driven by schema data.

Example:

```text id="j4r8dk"
Certification Record
          ↓
Receipt Generation
          ↓
Certification Receipt
```

In this model, the schema serves as the authoritative source record.

---

# Relationship to Registry

Registry interoperability depends heavily upon structured data.

Example:

```text id="x2v5bn"
Certification Schema
          ↓
Registry Entry
          ↓
Discovery
```

Shared schemas help ensure consistency between Certifier and Registry.

---

# Relationship to Anchor

Future Anchor integrations may preserve hashes associated with schema-based records.

Example:

```text id="h6t4qy"
Certification Record
          ↓
Hash
          ↓
Anchor Record
```

Structured schemas improve integrity verification and preservation workflows.

---

# Relationship to Attestor

Attestor may eventually validate structured records generated from Certifier schemas.

Example:

```text id="n8y7ro"
Certification Schema
          ↓
Attestation Review
          ↓
Attestation Record
```

Shared structures improve verification reliability.

---

# Suggested Future Structure

As Certifier evolves, this directory may contain:

```text id="k3w1zu"
schemas/
├── certification-schema.json
├── receipt-schema.json
├── report-schema.json
├── evidence-schema.json
├── registry-schema.json
├── attestation-schema.json
└── archive/
```

Additional schemas may be added as subsystem capabilities expand.

---

# Versioning

Schemas should be versioned whenever significant changes occur.

Recommended approach:

```text id="d9x6gl"
certification-schema-v1.json
certification-schema-v2.json
```

or

```text id="m5r8hq"
{
  "version": "1.0"
}
```

within the schema itself.

Versioning supports backward compatibility and historical preservation.

---

# Long-Term Vision

The schemas directory serves as the structural foundation of Certifier.

Documentation defines principles.

Reports explain decisions.

Receipts summarize outcomes.

Schemas provide the structured framework that allows systems to store, exchange, validate, preserve, and understand certification records.

As the Satoshium ecosystem grows, schemas may become one of the most important interoperability layers connecting Certifier, Registry, Chronicle, Anchor, Attestor, and future subsystems.

The goal is simple:

A certification record should be understandable by both people and machines.

---

# Related Documentation

For additional information, see:

```text id="v7j2mk"
docs/certification-schema.json
docs/workflow-diagram.md
docs/interoperability.md
docs/report-template.md
docs/receipt-template.md
```

Note: The primary schema file is located within this directory.

---

# Guiding Statement

> Documentation explains.
>
> Reports describe.
>
> Receipts summarize.
>
> Schemas structure.
>
> The schemas directory exists to give Certifier a machine-readable foundation.
