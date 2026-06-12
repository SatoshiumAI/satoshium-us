# Certification Receipt Template

This template provides a standardized structure for creating Certification Receipts within the Satoshium Certifier framework.

A Certification Receipt serves as the public-facing summary of a certification event.

Receipts provide a concise and durable record documenting:

* What was certified
* What standard was applied
* What determination was reached
* When certification occurred
* Where supporting records can be found

Certification Receipts are intended to be understandable without requiring review of the complete Certification Report.

---

# Receipt Information

## Receipt Identifier

```text
SCR-YYYY-NNNNNN
```

Example:

```text
SCR-2026-000001
```

---

## Receipt Version

```text
1.0
```

---

## Date Issued

```text
YYYY-MM-DD
```

Example:

```text
2026-07-25
```

---

# Certification Record Reference

## Certification Record Identifier

```text
SCRD-2026-000001
```

---

## Certification Report Identifier

```text
SCPR-2026-000001
```

---

# Certification Target

## Target Name

```text
Atlas Initial Build Phase
```

---

## Target Type

Examples:

```text
Page
Report
Service
Workflow
Dataset
Tool
```

---

## Target Description

Provide a concise description of the certification target.

Example:

```text
The initial public implementation of the Satoshium Atlas jurisdiction intelligence framework.
```

---

# Certification Details

## Certification Class

Examples:

```text
Informational
Operational
Verified
```

---

## Determination Status

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

## Certification Date

```text
YYYY-MM-DD
```

Example:

```text
2026-07-25
```

---

# Standard Information

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

## Standard Version

Example:

```text
1.0
```

---

# Review Information

## Review Method

Examples:

```text
Human
AI-Assisted
Human-AI-Assisted
Automated
```

---

## Reviewer

Example:

```text
Satoshium Certifier
```

---

# Evidence Summary

## Evidence Types Reviewed

Examples:

```text
- Screenshots
- URLs
- Notes
- Reports
- Hash Records
```

---

## Evidence Summary

Example:

```text
Evidence reviewed included public Atlas pages, supporting documentation, workflow records, screenshots, and certification notes.
```

---

# Determination Summary

Provide a concise explanation of the certification outcome.

Example:

```text
The Atlas Initial Build Phase satisfied the requirements of the Atlas Initial Build Standard v1.0 and was granted Verified certification status.
```

---

# Conditions

Optional.

Document any conditions associated with certification.

Example:

```text
Certification remains valid while referenced resources remain publicly accessible and materially consistent with reviewed evidence.
```

---

# Limitations

Optional.

Example:

```text
Review was limited to publicly accessible resources available at the time of certification.
```

---

# References

## Certification Report

```text
SCPR-2026-000001
```

---

## Registry Entry

Optional.

```text
SREG-2026-000001
```

---

## Anchor Reference

Optional future reference.

```text
ANCH-2026-000001
```

---

## Attestation Reference

Optional future reference.

```text
SATR-2026-000001
```

---

# Integrity Information

## Hash Algorithm

Example:

```text
SHA-256
```

---

## Receipt Hash

Optional.

Example:

```text
3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

---

# Public Certification Statement

Example:

```text
This receipt documents that the identified certification target was reviewed under the referenced certification standard and received the determination specified within this record.

This receipt summarizes the certification event and should be interpreted alongside the corresponding Certification Report when additional detail is required.
```

---

# Disclaimer

Example:

```text
Certification reflects a review conducted according to the referenced standard and available evidence at the time of review.

Certification does not guarantee future performance, completeness, regulatory compliance, legal validity, or absolute correctness.
```

---

# Signature

Example:

```text
Satoshium Certifier
```

---

# Timestamp

Example:

```text
2026-07-25T18:00:00Z
```

---

# Example Receipt

```text
Receipt ID:
SCR-2026-000001

Certification Record:
SCRD-2026-000001

Target:
Atlas Initial Build Phase

Target Type:
Tool

Certification Class:
Verified

Status:
Pass

Certification Date:
2026-07-25

Standard:
Atlas Initial Build Standard v1.0

Report:
SCPR-2026-000001

Determination:
The Atlas Initial Build Phase satisfied all applicable certification requirements and was granted Verified certification status.
```

---

# Receipt Lifecycle

```text
Certification Review
         ↓
Certification Report
         ↓
Certification Receipt
         ↓
Registry Entry
         ↓
Attestation
```

The receipt serves as the public summary of the certification event.

---

# Guiding Statement

> Evidence supports the review.
>
> Reports explain the review.
>
> Receipts summarize the review.
>
> The Certification Receipt exists to provide durable and understandable proof that certification occurred.
