# Frequently Asked Questions (FAQ)

## What is Satoshium Certifier?

Satoshium Certifier is the operational certification implementation of the Satoshium Suite. It reviews defined Certification Subjects against applicable Suite Standards and Suite Methodology, evaluates supporting Evidence, reaches certification determinations, and preserves the result through a canonical Certification Package.

Certifier is authoritative for its own certification actions, Certification Packages, Certification Classes, lifecycle, and generated certification artifacts.

Its purpose is not merely to record information, but to preserve how a subject was reviewed, what evidence was considered, what determination was reached, and how that result can be independently reviewed later.

---

## What does Certifier certify?

Certifier supports certification of defined digital subjects such as:

* Pages
* Reports
* Services
* Workflows
* Datasets
* Tools

Additional subject categories may be introduced through documented Certifier and Suite governance.

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

## What is a Certification Package?

The Certification Package is Certifier's canonical operational record for a certification.

It preserves the Certification Subject, certification boundary, governing Standards, applied Methodology, Evidence Inventory, evaluation, determination, Certification Class, lifecycle information, and generated artifact relationships.

Reports, receipts, certified records, and downstream Suite references derive from the Certification Package.

Reference does not transfer authority: the subject system retains authority over the subject it owns.

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

Certifier may use evidence appropriate to the applicable Standard and Certification Subject, including:

* Canonical records
* Reports
* Structured data
* URLs and durable references
* Screenshots or captures
* Hashes and integrity metadata
* Notes and review observations
* Supporting institutional artifacts

Evidence requirements are governed by the applicable Suite Standards and Certifier methodology rather than by a single universal evidence list.

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

## What are Certification Outcome, Certification Status, and Lifecycle State?

These concepts describe different parts of a certification record.

**Certification Outcome** records the determination reached by Certifier for the defined review.

Example:

```text
Certified
```

**Certification Status** communicates the current certification-domain condition of that issued certification.

Example:

```text
Issued · Active
```

**Lifecycle State** describes where the certification record exists in its broader institutional lifecycle.

These concepts should not be collapsed into one generic status field.

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

## What are SCPR, SCR, and SCRD?

Certifier uses several generated artifact forms derived from the canonical Certification Package:

```text
SCPR
Certification Process Report

SCR
Certification Receipt

SCRD
Satoshium Certified Record
```

The SCPR preserves the detailed review process and reasoning.

The SCR provides a concise public-facing certification receipt.

The SCRD provides the certified-record representation in human-readable and, where published, machine-readable form.

These artifacts must remain traceable to and materially consistent with the canonical Certification Package.

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

Satoshium Registry is the Suite institution responsible for canonical registration, durable SREG identity, classification, provenance, validation, publication, and public discovery of registered institutional records.

Certifier creates and owns the certification record.

Registry may create a SREG that catalogs that Certification Package while Certifier retains certification authority.

---

## What is Chronicle?

Satoshium Chronicle is the Suite institution responsible for preserving qualifying historical Occurrences through canonical Chronicle Entries.

A qualifying certification Occurrence may be preserved by Chronicle, but Chronicle does not own or re-adjudicate the certification action. Certifier remains authoritative for the Certification Package and determination.

---

## What is Anchor?

Satoshium Anchor is the Suite institution designed to preserve integrity references, hashes, timestamps, signatures, and durable verification points.

Anchor supports integrity without replacing Certifier's authority over certification records.

---

## What is Attestor?

Satoshium Attestor is the Suite institution designed to support attestations, trust statements, and independent verification of selected claims and relationships.

Attestation does not replace Certifier's certification authority.

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
Beacon
   ↓
Attestor
   ↓
Navigator
```

Atlas creates information.

Certifier reviews information.

Registry catalogs authoritative records through SREGs.

Chronicle preserves qualifying historical memory.

Anchor preserves integrity references.

Beacon supports discovery signals and metadata.

Attestor supports attestations and trust statements.

Navigator coordinates workflows and cross-system activity.

Together they form a connected Suite while preserving independent institutional authority.

A production example now exists:

```text
Atlas Jurisdiction Record — El Salvador
        ↓
SC-CERT-2026-0001
        ↓
SREG-2026-0001
        ↓
CHR-2026-0001
```

Each system owns its own object. Reference does not transfer authority.

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
