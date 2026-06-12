# Satoshium Certifier

# Evidence Model

**Version:** 1.0
**Status:** Draft
**Subsystem:** Satoshium Certifier
**Created:** July 2026
**Author:** Satoshium

---

# Overview

The Evidence Model defines how Satoshium Certifier identifies, collects, references, preserves, and evaluates evidence used during certification activities.

Evidence is the foundation of certification.

Without evidence, certification becomes opinion.

Without structure, evidence becomes difficult to inspect.

Without preservation, certification history becomes incomplete.

The Evidence Model exists to ensure that certification determinations are supported by documented, reviewable, and traceable materials.

---

# Purpose

The purpose of the Evidence Model is to define:

* What qualifies as evidence.
* How evidence should be described.
* How evidence should be referenced.
* How evidence should support certification decisions.
* How evidence should be preserved for future review.

Certifier does not require every certification record to contain every evidence type.

Instead, evidence requirements should be proportional to the target type, certification class, applicable standard, and intended reliance.

---

# Evidence Philosophy

Certifier follows a simple principle:

> Certification should be supported by evidence sufficient to understand why the determination was made.

Evidence does not need to prove perfection.

Evidence needs to support reviewability.

A future reviewer should be able to examine the certification record and understand:

* What was reviewed
* What materials were considered
* What condition the target was in
* What findings were made
* Why the certification outcome was reached

---

# Core Evidence Types

Version 1.0 of the Evidence Model defines five core evidence types:

1. Screenshots
2. Reports
3. URLs
4. Hashes
5. Notes

Additional evidence types may be added in future versions.

---

# Evidence Type: Screenshots

## Definition

A screenshot is a visual capture of a digital artifact, interface, page, tool, workflow, or output at a specific point in time.

---

## Purpose

Screenshots provide visual evidence of appearance, availability, layout, structure, and public presentation.

They are especially useful for certification targets such as:

* Pages
* Tools
* Services
* Workflows
* Public-facing interfaces

---

## Recommended Uses

Screenshots may be used to document:

* Public page appearance
* Completed interface states
* Confirmation screens
* Published outputs
* Error-free rendering
* Navigation structure
* Public availability

---

## Suggested Metadata

Each screenshot evidence item should include:

```text
evidence_id:
evidence_type: screenshot
file_name:
file_path:
captured_at:
captured_by:
target_url:
description:
notes:
```

---

## Preservation Notes

Screenshots should be stored in a durable location whenever practical.

File names should be descriptive and may include:

```text
target-name_YYYY-MM-DD_status.png
```

Example:

```text
atlas-initial-build_2026-07-25_verified.png
```

---

# Evidence Type: Reports

## Definition

A report is a structured document describing findings, review results, analysis, certification criteria, evidence considered, and determinations reached.

---

## Purpose

Reports provide narrative and structured support for certification outcomes.

They explain the reasoning behind the certification determination.

Reports are especially useful for:

* Certification reviews
* Atlas evaluations
* Workflow assessments
* Dataset evaluations
* Tool reviews
* SOU evidence packages

---

## Recommended Uses

Reports may document:

* Review scope
* Applicable standard
* Criteria applied
* Findings
* Exceptions
* Limitations
* Determination
* Supporting evidence

---

## Suggested Metadata

Each report evidence item should include:

```text
evidence_id:
evidence_type: report
report_name:
report_path:
report_url:
created_at:
created_by:
related_certification_record:
description:
notes:
```

---

## Preservation Notes

Reports should be preserved in human-readable formats whenever practical.

Recommended formats include:

```text
.md
.txt
.pdf
.html
.json
```

Markdown and plain text are preferred for long-term portability.

---

# Evidence Type: URLs

## Definition

A URL is a reference to a web-accessible resource that supports a certification review.

---

## Purpose

URLs provide location-based evidence that a target or supporting resource existed at a specific accessible location.

URLs are especially useful for:

* Published pages
* Public documentation
* GitHub repositories
* Public reports
* Certification receipts
* Registry entries

---

## Recommended Uses

URLs may document:

* Canonical page locations
* Source repository locations
* Published certification records
* Public evidence references
* Related documentation

---

## Suggested Metadata

Each URL evidence item should include:

```text
evidence_id:
evidence_type: url
url:
title:
accessed_at:
accessed_by:
description:
status_at_review:
notes:
```

---

## Preservation Notes

URLs are useful but fragile.

Web resources may change, move, or disappear.

For important certification events, URLs should be paired with additional evidence such as:

* Screenshots
* Reports
* Hashes
* Archived copies
* Repository records

A URL alone should rarely be the only evidence for a high-reliance certification.

---

# Evidence Type: Hashes

## Definition

A hash is a cryptographic digest generated from a file, record, dataset, or other digital artifact.

Hashes can help demonstrate that a specific item has not changed since the hash was generated.

---

## Purpose

Hashes provide integrity evidence.

They do not explain meaning, quality, or correctness.

They support the question:

> Is this the same artifact that was reviewed?

---

## Recommended Uses

Hashes may be used for:

* Certification reports
* JSON records
* Receipts
* Source files
* Datasets
* Screenshots
* Archived packages

---

## Suggested Metadata

Each hash evidence item should include:

```text
evidence_id:
evidence_type: hash
hash_algorithm:
hash_value:
hashed_item_name:
hashed_item_path:
generated_at:
generated_by:
description:
notes:
```

Recommended default algorithm:

```text
SHA-256
```

---

## Preservation Notes

Hashes are most useful when paired with the underlying file or artifact.

A hash without access to the original artifact provides limited value.

Future systems such as Anchor may use hashes as preservation or proof references.

---

# Evidence Type: Notes

## Definition

A note is a written observation, explanation, limitation, reviewer comment, or contextual statement created during certification.

---

## Purpose

Notes preserve human or AI-assisted observations that may not fit cleanly into structured fields.

Notes are especially useful for documenting:

* Exceptions
* Ambiguities
* Limitations
* Reviewer observations
* Contextual explanations
* Future follow-up items

---

## Recommended Uses

Notes may document:

* Why a criterion passed
* Why a criterion failed
* Why evidence was considered sufficient
* Known limitations
* Open questions
* Review assumptions

---

## Suggested Metadata

Each note evidence item should include:

```text
evidence_id:
evidence_type: note
created_at:
created_by:
note_type:
related_criterion:
note_text:
visibility:
```

Suggested note types:

```text
observation
limitation
exception
clarification
recommendation
```

---

## Preservation Notes

Notes should be written clearly enough that future reviewers can understand them without relying on memory or private context.

When possible, notes should avoid vague language such as:

```text
Looks good.
```

Preferred:

```text
Required navigation links were present and functional at the time of review.
```

---

# Evidence Quality Principles

Evidence should be evaluated according to the following principles:

## Relevance

Evidence should directly support the certification decision.

## Sufficiency

Evidence should be adequate for the certification class being granted.

## Traceability

Evidence should connect clearly to the target and review criteria.

## Durability

Evidence should remain accessible whenever practical.

## Clarity

Evidence should be understandable to future reviewers.

## Integrity

Evidence should preserve the state of the artifact as reviewed.

---

# Evidence Sufficiency by Certification Class

Evidence expectations may vary by certification class.

| Certification Class | Minimum Evidence Expectation                                                                 |
| ------------------- | -------------------------------------------------------------------------------------------- |
| Informational       | Basic documentation or descriptive evidence                                                  |
| Operational         | Documentation plus evidence of functionality                                                 |
| Verified            | Documentation, functionality evidence, review record, and supporting preservation references |

---

# Evidence and Lifecycle States

Evidence requirements may also vary by lifecycle state.

| Lifecycle State | Evidence Expectation                                   |
| --------------- | ------------------------------------------------------ |
| Created         | Basic target identification                            |
| Reviewed        | Review notes and criteria results                      |
| Certified       | Certification report, receipt, and supporting evidence |
| Rejected        | Review record and failure notes                        |
| Expired         | Expiration record and prior certification evidence     |
| Revoked         | Revocation explanation and supporting evidence         |
| Archived        | Preserved historical record                            |

---

# Evidence Record Example

```json
{
  "evidence_id": "ev-2026-07-25-001",
  "evidence_type": "screenshot",
  "evidence_name": "Atlas Initial Build Certification Screenshot",
  "evidence_description": "Screenshot showing the published Atlas certification record.",
  "evidence_url": "",
  "evidence_path": "evidence/screenshots/atlas-initial-build_2026-07-25_verified.png",
  "evidence_hash": "",
  "captured_at": "2026-07-25T00:00:00Z",
  "notes": "Screenshot captured as visual evidence of public certification status."
}
```

---

# Long-Term Vision

The Evidence Model is designed to support future expansion into Registry, Anchor, Attestor, and other Satoshium subsystems.

In future versions:

* Registry may catalog evidence references.
* Anchor may preserve hashes.
* Attestor may support independent witness statements.
* Chronicle may record certification milestones.
* AI agents may assist in evidence collection and evaluation.

The evidence model therefore serves as the factual backbone of Certifier.

---

# Revision History

| Version | Date      | Description                              |
| ------- | --------- | ---------------------------------------- |
| 1.0     | July 2026 | Initial Evidence Model document created. |

---

# Guiding Statement

> Certification without evidence is assertion.
>
> Certification with evidence becomes reviewable history.
