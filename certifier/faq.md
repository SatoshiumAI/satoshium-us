# Frequently Asked Questions (FAQ)

## What is Satoshium Certifier?

Satoshium Certifier is a standards-based certification framework designed to review digital artifacts, evaluate evidence, and produce structured records documenting certification outcomes.

Certifier serves as the trust layer of the Satoshium ecosystem.

Its purpose is not merely to record information, but to document how information, services, workflows, and other targets were reviewed.

---

## What does Certifier certify?

Version 1.0 supports certification of:

* Pages
* Reports
* Services
* Workflows
* Datasets
* Tools

Future versions may support additional target categories.

---

## What is a Certification Target?

A Certification Target is the item being reviewed.

Examples include:

* A webpage
* A published report
* A software tool
* A workflow
* A dataset
* A service

The target is the subject of the certification process.

---

## What is certification?

Certification is the process of reviewing a target against a documented standard, evaluating supporting evidence, and recording a determination.

Certification is intended to create a transparent and reviewable record of that process.

---

## Does certification guarantee correctness?

No.

Certification documents a review performed according to a defined standard and available evidence at a specific point in time.

Certification does not guarantee:

* Accuracy
* Completeness
* Future performance
* Regulatory compliance
* Legal validity

Certification records document review outcomes rather than absolute truth.

---

## What standards are used?

Certifier uses documented Certification Standards.

Standards define:

* Scope
* Requirements
* Evaluation criteria
* Evidence requirements
* Determination guidance

All certification activities should be traceable to an applicable standard.

---

## What evidence can be used?

Version 1.0 recognizes several evidence types:

* Screenshots
* Reports
* URLs
* Hashes
* Notes

Additional evidence categories may be introduced in future versions.

---

## What are Certification Classes?

Certification Classes communicate the level of certification granted.

Version 1.0 defines:

### Informational

The target exists and has been documented.

### Operational

The target exists, is documented, and demonstrates operation.

### Verified

The target has been reviewed against an established standard and is supported by documented evidence.

---

## What are Status Determinations?

Status Determinations communicate the outcome of a review.

Version 1.0 defines:

* Pass
* Conditional Pass
* Fail
* Revoked

These values describe the certification outcome.

---

## What is the difference between a Status and a Lifecycle State?

Status describes the determination reached during review.

Examples:

* Pass
* Conditional Pass
* Fail
* Revoked

Lifecycle State describes where the certification record exists within its lifecycle.

Examples:

* Created
* Reviewed
* Certified
* Expired
* Revoked
* Archived

The two concepts serve different purposes.

---

## What is a Certification Report?

A Certification Report is the detailed review record supporting a certification event.

Reports document:

* Evidence reviewed
* Findings
* Methodology
* Determinations
* Conditions
* Recommendations

Reports provide the reasoning behind certification outcomes.

---

## What is a Certification Receipt?

A Certification Receipt is a concise public-facing summary of a certification event.

Receipts provide proof that certification occurred while referencing supporting reports and records.

---

## What is the difference between a Report and a Receipt?

A simple way to think about it:

```text
Evidence
     ↓
Report
     ↓
Receipt
```

Evidence supports the review.

The Report explains the review.

The Receipt summarizes the review.

---

## Why are hashes used?

Hashes support integrity verification.

They help answer a simple question:

> Is this the same artifact that was originally reviewed?

Hashes do not prove correctness.

They help verify consistency.

---

## Why are notes considered evidence?

Notes preserve observations, assumptions, limitations, clarifications, and reviewer reasoning.

They help explain how findings and determinations were reached.

Notes preserve context that might otherwise be lost.

---

## Does Certifier require human review?

Not necessarily.

Version 1.0 supports:

* Human review
* AI-assisted review
* Human-AI-assisted review
* Automated review

The applicable standard determines the review requirements.

---

## Can AI perform certification?

AI may assist certification activities.

Examples include:

* Evidence collection
* Analysis
* Documentation
* Review support

However, AI-generated observations should not automatically be treated as authoritative conclusions.

Certification should remain transparent and reviewable.

---

## What is Registry?

Registry is a future Satoshium subsystem responsible for cataloging certification records and making them discoverable.

Certifier creates certification records.

Registry organizes them.

---

## What is Chronicle?

Chronicle is a future Satoshium subsystem focused on preserving historical records and milestones.

Certification events may become Chronicle entries.

---

## What is Anchor?

Anchor is a future Satoshium subsystem intended to preserve hashes, proof references, and integrity records.

Anchor supports long-term preservation.

---

## What is Attestor?

Attestor is a future Satoshium subsystem intended to support independent verification and attestation activities.

Attestor may provide additional trust through secondary review and confirmation.

---

## How does Certifier fit into Satoshium?

At a high level:

```text
Atlas
   ↓
Certifier
   ↓
Registry
   ↓
Chronicle
   ↓
Anchor
   ↓
Attestor
```

Atlas creates information.

Certifier reviews information.

Registry catalogs information.

Chronicle records history.

Anchor preserves integrity.

Attestor verifies claims.

Together they form a connected ecosystem.

---

## Is Certifier open source?

Yes.

Certifier is released under the MIT License unless otherwise specified.

See:

```text
LICENSE
```

for the governing license terms.

---

## What is the long-term vision of Certifier?

The long-term vision of Certifier is to create a transparent and durable framework for documenting review, evidence, certification, and trust across digital systems.

The objective is not simply to issue certifications.

The objective is to create certification records that remain understandable, reviewable, and useful years into the future.

---

## Where should I start?

New contributors are encouraged to begin with:

```text
README.md
docs/certifier-overview.md
docs/certification-philosophy.md
docs/workflow-diagram.md
```

These documents provide the best introduction to the Certifier framework.

---

## Guiding Statement

> Trust should not depend upon memory.
>
> Trust should not depend upon reputation.
>
> Trust should be supported by standards, evidence, and reviewable records.
>
> Satoshium Certifier exists to help preserve those records.
