# Satoshium Certifier — Evidence

**Path:** `/certifier/evidence/`  
**Institution:** Satoshium Certifier  
**Surface:** Evidence  
**Status:** Current repository documentation

## Purpose

This directory contains evidence and evidence-support documentation used by **Satoshium Certifier**.

Evidence is the factual foundation used when Certifier applies Suite Standards and Suite Methodology to a defined Certification Subject.

The public page for this directory is:

- `index.html`

This README documents the current evidence model, repository categories, preservation expectations, certification relationships, and Suite boundaries.

## Evidence Role

Evidence supports certification.

It does not independently create certification authority or determine the certification outcome.

The governing relationship is:

```text
Certification Subject
        ↓
Evidence Sources
        ↓
Evidence Records + Evidence Inventory
        ↓
Evidence Mapping
        ↓
Certification Package
        ↓
Evaluation + Certification Decision
        ↓
SCPR · SCR · SCRD
        ↓
Governed Suite References
```

The **Certification Package** remains Certifier's canonical operational record.

## Evidence Records

An **Evidence Record (SEV)** preserves factual material considered during certification.

Evidence Records may include:

- source references;
- observed facts;
- reviewer notes;
- screenshots;
- hashes;
- reports;
- metadata;
- supporting documentation;
- preserved URLs; and
- other materials associated with the Certification Package.

Evidence Records preserve what was available to Certifier during review.

## Evidence Inventory

The **Evidence Inventory** identifies and organizes the Evidence Records associated with a Certification Subject.

It becomes part of the Certification Package and preserves the set of materials available for evaluation.

The Evidence Inventory supports:

- completeness review;
- traceability;
- evidence enumeration;
- scope control; and
- reproducibility of the certification review.

## Evidence Mapping

**Evidence Mapping** connects Evidence Records to the certification context.

Mappings may connect evidence to:

- applicable Suite Standards;
- Suite Methodology steps;
- findings;
- limitations;
- confidence posture; and
- the resulting certification decision.

Evidence Mapping improves traceability without converting evidence itself into a certification conclusion.

## Evidence Review

**Evidence Review** records what Certifier:

- examined;
- accepted;
- limited;
- excluded;
- could not verify; or
- otherwise treated as relevant to the certification.

The review should explain how the available evidence supported or constrained the evaluation and certification decision.

## Repository Evidence Categories

The repository may preserve evidence in practical supporting categories including:

```text
evidence/
├── screenshots/
├── hashes/
├── notes/
└── archived/
```

These categories remain useful implementation and preservation structures beneath the broader Evidence Record model.

### Screenshots

Screenshots preserve visual evidence of certification subjects, interfaces, workflows, reports, outputs, and other observed conditions.

They help answer:

> What was visible at the time of review?

### Hashes

Hashes preserve integrity references for certification artifacts and evidence materials.

Examples may include:

- report hashes;
- receipt hashes;
- evidence-package hashes;
- screenshot hashes; and
- dataset hashes.

Hashes support later integrity comparison.

They do not by themselves create an Anchor Integrity Reference.

### Notes

Notes preserve observations, assumptions, limitations, clarifications, scope issues, and reviewer reasoning.

They help future reviewers understand why evidence was interpreted in a particular way.

### Archived Evidence

Archived evidence preserves superseded, expired, revoked, historical, or otherwise inactive materials that remain relevant to the certification record.

Historical evidence should generally remain reviewable when practical.

## Evidence Lifecycle

Evidence may move through stages such as:

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

The exact implementation may vary by certification, but evidence should remain traceable throughout its lifecycle.

## Evidence Quality Principles

Evidence should be:

### Relevant

Directly related to the Certification Subject or certification activity.

### Traceable

Linked to identifiable records, sources, and certification context.

### Understandable

Readable and interpretable by later reviewers.

### Preserved

Retained where practical to support historical review.

### Verifiable

Capable of independent inspection or validation where possible.

### Proportionate

Appropriate to the certification scope, class, and applicable requirements.

## Evidence and Certification Classes

Evidence expectations may differ by Certification Class.

The governing evidence requirements should come from the applicable Suite Standards and Suite Methodology rather than from this directory alone.

Any class-specific evidence expectations documented here should remain synchronized with the governing certification architecture.

## Evidence and Certification Decisions

Evidence informs evaluation.

The basic relationship is:

```text
Evidence
        ↓
Review
        ↓
Findings / Limitations
        ↓
Evaluation
        ↓
Certification Decision
```

Evidence does not automatically dictate the outcome.

Certifier remains responsible for the certification decision within the governed certification process.

## Integrity References

Hashes, timestamps, file references, and preserved URLs may provide source material for **Anchor Integrity References** where appropriate.

The boundary is:

```text
Evidence Integrity Material
≠
Anchor Integrity Reference
```

Anchor remains authoritative for Integrity References.

Certifier remains authoritative for the certification record.

## Chronicle Relationship

Evidence may retain historical importance after a certification changes, expires, is superseded, or is revoked.

Chronicle may preserve governed chronology associated with significant certification events.

Chronicle records when.

The Evidence directory preserves the underlying factual material and review context.

## Registry Relationship

Registry may create a Satoshium Registry Entry / SREG referencing a governed certification or source record.

Registry does not become the source authority for the evidence or Certification Package.

## Attestor Relationship

Attestor is operational and institutionally distinct from Certifier.

Eligible governed Certifier outputs may participate in Attestor's canonical flow:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

Evidence may be referenced by Attestor where permitted, but Certifier evidence does not itself become an Attestation or Trust Statement.

## Navigator Relationship

Navigator may define or orchestrate workflows that consume or route governed certification information.

Navigator does not own Certifier evidence or certification decisions.

## Beacon Relationship

Beacon may publish Discovery Signals / Discovery Metadata that make governed certification records discoverable.

Discovery does not alter evidence provenance or certification authority.

## Preservation Philosophy

Certifier favors preservation over deletion where practical.

Preferred discipline:

- preserve rather than delete;
- archive rather than discard;
- document rather than assume.

Historical evidence may remain valuable long after the original certification event because it allows future reviewers to reconstruct what was known, reviewed, relied upon, limited, or excluded.

## Authority Discipline

This directory should preserve the following distinctions:

- Evidence ≠ Certification Decision
- Evidence Record ≠ Certification Package
- Evidence Inventory ≠ Evaluation
- Evidence Mapping ≠ Finding
- Hash ≠ Anchor Integrity Reference
- Validation ≠ Evaluation
- Evaluation ≠ Attestation
- Certification Decision ≠ Trust Statement
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Related Documentation

Related Certifier documentation includes:

```text
/certifier/docs/evidence-model.md
/certifier/docs/status-definitions.md
/certifier/docs/certification-lifecycle.md
/certifier/docs/workflow-diagram.md
```

These documents should remain synchronized with the current public Evidence surface and governing Suite architecture.

## Repository Expectations

Changes to this directory should preserve:

1. evidence as factual support rather than certification authority;
2. the Certification Package as Certifier's canonical operational record;
3. Evidence Record, Inventory, Mapping, and Review distinctions;
4. evidence provenance and traceability;
5. preservation and archival discipline;
6. separation between Certifier evidence and Anchor Integrity References;
7. separation between Certifier evidence and Attestor objects;
8. current Suite object terminology; and
9. the rule that reference does not transfer authority.

## Governing Principle

**Evidence turns certification from assertion into a reviewable record while remaining distinct from the certification decision it supports.**
