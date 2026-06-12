# Registry Entry Template

This template provides a standardized structure for creating Registry Entries within the Satoshium ecosystem.

A Registry Entry serves as a discoverable catalog record describing a certified artifact, certification event, attestation record, preservation record, or other registered item.

Registry Entries are intended to provide concise, searchable, and durable references that connect users to supporting records.

Registry Entries are not replacements for Certification Reports or Certification Receipts.

They serve as the discovery layer.

---

# Registry Information

## Registry Identifier

```text
SREG-YYYY-NNNNNN
```

Example:

```text
SREG-2026-000001
```

---

## Registry Version

```text
1.0
```

---

## Entry Date

```text
YYYY-MM-DD
```

Example:

```text
2026-07-25
```

---

# Registered Item

## Item Name

```text
Atlas Initial Build Phase
```

---

## Item Type

Examples:

```text
Page
Report
Service
Workflow
Dataset
Tool
Certification
Attestation
Standard
```

---

## Item Description

Provide a concise description of the registered item.

Example:

```text
Initial public implementation of the Satoshium Atlas jurisdiction intelligence framework.
```

---

# Registration Classification

## Registry Category

Examples:

```text
Certification
Attestation
Standard
Evidence
Reference
Historical
```

---

## Certification Class

Optional.

Examples:

```text
Informational
Operational
Verified
```

---

## Determination Status

Optional.

Examples:

```text
Pass
Conditional Pass
Fail
Revoked
```

---

## Lifecycle State

Examples:

```text
Created
Reviewed
Certified
Expired
Revoked
Archived
```

---

# Certification References

## Certification Record

```text
SCRD-2026-000001
```

(Optional)

---

## Certification Report

```text
SCPR-2026-000001
```

(Optional)

---

## Certification Receipt

```text
SCR-2026-000001
```

(Optional)

---

# Standard References

## Standard Identifier

Example:

```text
STD-ATLAS-001
```

---

## Standard Name

Example:

```text
Atlas Initial Build Standard v1.0
```

---

# Registration Summary

Provide a concise description of why the item is registered.

Example:

```text
The Atlas Initial Build Phase was reviewed under the Atlas Initial Build Standard v1.0 and granted Verified certification status.
```

---

# Registry Metadata

## Date Registered

```text
YYYY-MM-DD
```

Example:

```text
2026-07-25
```

---

## Registered By

Example:

```text
Satoshium Registry
```

---

## Registry Scope

Examples:

```text
Public
Internal
Historical
Archived
```

---

# Discoverability Information

## Keywords

Examples:

```text
Atlas
Certification
Jurisdiction Intelligence
Verified
Satoshium
```

---

## Tags

Examples:

```text
atlas
verified
certification
tool
```

---

## Related Records

Examples:

```text
SCRD-2026-000001
SCR-2026-000001
SCPR-2026-000001
```

---

# External References

Optional.

Examples:

```text
https://satoshium.us/atlas/
```

```text
https://satoshium.us/certifier/
```

---

# Evidence References

Optional.

Examples:

```text
SEV-2026-000001
SEV-2026-000002
SEV-2026-000003
```

---

# Integrity References

## Hash Algorithm

Example:

```text
SHA-256
```

---

## Registry Hash

Optional.

Example:

```text
3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

---

# Future References

Optional.

## Anchor Reference

```text
ANCH-2026-000001
```

---

## Attestation Reference

```text
SATR-2026-000001
```

---

## Chronicle Reference

```text
SCHR-2026-000001
```

(Optional future identifier.)

---

# Public Registry Statement

Example:

```text
This Registry Entry serves as a discoverable reference to the registered item and its associated records.

Registry inclusion does not replace supporting reports, receipts, evidence, or standards.

Users should consult referenced records for additional detail.
```

---

# Notes

Optional.

Document additional information relevant to discovery, classification, or historical context.

Example:

```text
This entry represents the first certified subsystem within the Satoshium ecosystem.
```

---

# Example Registry Entry

```text
Registry ID:
SREG-2026-000001

Item:
Atlas Initial Build Phase

Type:
Tool

Certification Class:
Verified

Status:
Pass

Date Registered:
2026-07-25

Report:
SCPR-2026-000001

Receipt:
SCR-2026-000001
```

---

# Registry Lifecycle

```text
Certification
       ↓
Receipt
       ↓
Registry Entry
       ↓
Discovery
       ↓
Attestation
```

The Registry Entry serves as the public catalog record within that process.

---

# Guiding Statement

> Reports explain.
>
> Receipts summarize.
>
> Registry Entries organize.
>
> A Registry Entry exists to make certification records discoverable, referenceable, and understandable.
