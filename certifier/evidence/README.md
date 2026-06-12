# Evidence

This directory contains evidence used to support certification activities within the Satoshium Certifier framework.

Evidence forms the factual foundation of certification.

Certification records, reports, receipts, and determinations should be supported by evidence sufficient to explain how conclusions were reached and to allow future reviewers to understand the basis of those conclusions.

The Evidence directory serves as the primary repository for evidence references and supporting materials associated with certification activities.

---

# Purpose

The purpose of the Evidence directory is to:

* Preserve supporting materials
* Improve transparency
* Support certification determinations
* Enable future review
* Facilitate auditing
* Support historical preservation
* Strengthen trust through documentation

Evidence helps answer questions such as:

* What was reviewed?
* What condition was it in?
* What observations were made?
* What records were preserved?
* What information supported the determination?

---

# Evidence Philosophy

Certifier follows a simple principle:

> Certification should be supported by reviewable evidence.

Evidence does not guarantee correctness.

Evidence provides visibility into the review process.

The objective is not perfection.

The objective is transparency.

Future reviewers should be able to understand:

* What was examined
* What evidence existed
* What conclusions were reached
* Why certification decisions were made

---

# Evidence Categories

Version 1.0 of Certifier defines four primary evidence categories:

```text
evidence/
├── screenshots/
├── hashes/
├── notes/
└── archived/
```

Each category serves a distinct purpose.

---

# Screenshots

Location:

```text
evidence/screenshots/
```

Screenshots preserve visual evidence of certification targets and related activities.

Examples include:

* Public webpages
* Interfaces
* Workflows
* Reports
* Certification outputs
* Milestone events

Screenshots answer:

> What did the target look like at the time of review?

---

# Hashes

Location:

```text
evidence/hashes/
```

Hashes provide integrity references for certification artifacts.

Examples include:

* Report hashes
* Receipt hashes
* Evidence package hashes
* Screenshot hashes
* Dataset hashes

Hashes answer:

> Is this the same artifact that was originally reviewed?

---

# Notes

Location:

```text
evidence/notes/
```

Notes preserve observations, assumptions, limitations, clarifications, and reviewer reasoning.

Examples include:

* Review observations
* Findings
* Recommendations
* Scope notes
* Assumptions
* Limitations

Notes answer:

> Why was the determination reached?

---

# Archived Evidence

Location:

```text
evidence/archived/
```

Archived evidence preserves historical materials that are no longer active but remain important for transparency and historical review.

Examples include:

* Superseded evidence
* Expired certification evidence
* Revoked certification evidence
* Legacy records
* Historical certification packages

Archived evidence answers:

> What existed in the past?

---

# Evidence Relationships

The evidence categories work together to create a complete certification record.

Example:

```text
Screenshot
     ↓
Observation Note
     ↓
Certification Report
     ↓
Certification Receipt
```

Another example:

```text
Evidence Package
     ↓
Hash Record
     ↓
Anchor Preservation
```

Each evidence type contributes a different perspective.

---

# Evidence Lifecycle

Evidence may progress through several stages.

```text
Collected
     ↓
Referenced
     ↓
Used in Review
     ↓
Preserved
     ↓
Archived
```

Evidence should remain traceable throughout its lifecycle whenever practical.

---

# Evidence Quality Principles

Evidence should be:

## Relevant

Directly related to the certification activity.

---

## Traceable

Linked to identifiable targets and certification records.

---

## Understandable

Readable and interpretable by future reviewers.

---

## Preserved

Retained whenever practical.

---

## Verifiable

Capable of independent review or validation.

---

## Proportionate

Appropriate for the certification class and certification target.

---

# Evidence and Certification Classes

Evidence expectations generally increase as certification classes advance.

| Certification Class | Typical Evidence Expectations                                                |
| ------------------- | ---------------------------------------------------------------------------- |
| Informational       | Basic documentation and references                                           |
| Operational         | Documentation plus operational evidence                                      |
| Verified            | Documentation, operational evidence, notes, and supporting integrity records |

The applicable certification standard ultimately determines evidence requirements.

---

# Evidence and Determinations

Evidence supports certification determinations.

Typical relationship:

```text
Evidence
     ↓
Review
     ↓
Finding
     ↓
Determination
```

Evidence informs the determination but does not automatically dictate the outcome.

Review and judgment remain important components of the certification process.

---

# Evidence and Future Subsystems

The Evidence directory is designed to support future interoperability throughout the Satoshium ecosystem.

Examples include:

## Atlas

Provides certification targets and supporting records.

## Registry

Catalogs certified records and evidence references.

## Chronicle

Records significant certification milestones.

## Anchor

Preserves hashes and integrity references.

## Attestor

Supports future independent verification.

---

# Preservation Philosophy

Whenever practical:

* Preserve rather than delete.
* Archive rather than discard.
* Document rather than assume.

Historical evidence may become valuable long after a certification event has concluded.

Preservation supports trust.

---

# Long-Term Vision

The Evidence directory serves as the factual backbone of Certifier.

Certification reports explain conclusions.

Certification receipts summarize outcomes.

Evidence preserves the materials that support those outcomes.

As the Satoshium ecosystem evolves, evidence may become one of the most valuable long-term assets because it allows future reviewers to reconstruct certification activities long after they occurred.

The goal is not merely certification.

The goal is reviewable history.

---

# Related Documentation

For additional information, see:

```text
docs/evidence-model.md
docs/status-definitions.md
docs/certification-lifecycle.md
docs/workflow-diagram.md
```

---

# Guiding Statement

> Screenshots preserve what was seen.
>
> Hashes preserve integrity.
>
> Notes preserve reasoning.
>
> Archives preserve history.
>
> Together they form the evidence upon which certification is built.
