# Satoshium Certifier — Methodology

**Path:** `/certifier/methodology/`  
**Institution:** Satoshium Certifier  
**Surface:** Methodology  
**Status:** Current repository documentation

## Purpose

This directory documents how **Satoshium Certifier applies the Satoshium Suite Methodology** to conduct evidence-based certification reviews, create Certification Packages, issue certification decisions, and generate Certifier artifacts.

The public page for this directory is:

- `index.html`

This README documents the operational relationship between Suite Methodology and Certifier. It does not redefine Suite Methodology itself.

## Governing Boundary

The enduring Suite relationship is:

> **Standards define expectations. Methodology defines implementation. Certifier performs certification.**

Accordingly:

- Suite Standards define what is expected.
- Suite Methodology defines how the governed review process is performed.
- Certifier applies those governing layers to a Certification Subject.
- Certifier records the result in the canonical Certification Package.

Certifier does not independently redefine the Suite Methodology.

## Operational Methodology Flow

The current Certifier methodology is represented at a high level as:

```text
Certification Subject
        ↓
Scope and Standards
        ↓
Evidence
        ↓
Certification Package
        ↓
Evaluation and Decision
        ↓
SCPR · SCR · SCRD
        ↓
Governed Suite Relationships
```

The Certification Package remains Certifier's canonical operational record.

## Step 1 — Identify Certification Subject

Identify the artifact, record, dataset, workflow, service, subsystem, tool, or other governed object being reviewed.

The Certification Subject must be sufficiently defined to establish:

- object identity;
- institutional ownership;
- certification boundary; and
- review context.

Selection as a Certification Subject does not transfer source authority to Certifier.

## Step 2 — Define Scope and Standards

Establish:

- review boundaries;
- exclusions;
- applicable Suite Standards;
- applicable Suite Methodology sections;
- assumptions; and
- known limitations.

Scope determines what the certification does and does not address.

## Step 3 — Collect and Organize Evidence

Gather the evidence needed to support the certification review.

Evidence may include:

- URLs;
- screenshots;
- reports;
- source materials;
- metadata;
- supporting documentation; and
- Evidence Records.

Evidence remains factual support.

It does not independently create the certification decision.

## Step 4 — Create Certification Package

Assemble the canonical Certification Package.

The Certification Package may preserve:

- Certification Subject;
- scope;
- applicable standards;
- applicable methodology;
- evidence inventory;
- findings;
- assessment;
- decision;
- generated artifacts; and
- certification history.

The Certification Package is Certifier's canonical operational record.

## Step 5 — Evaluate and Document Findings

Evaluate the preserved evidence against the applicable standards and methodology.

Document:

- observations;
- findings;
- limitations;
- reasoning;
- confidence posture where applicable; and
- certification assessment.

Evaluation remains distinct from downstream Attestor rule-constrained evaluation.

## Step 6 — Issue Decision and Certifier Artifacts

Certifier issues the certification decision and generates its own related artifacts, including:

- **SCPR** — Certification Process Report
- **SCR** — Certification Receipt
- **SCRD HTML**
- **SCRD JSON**

Certifier may also prepare or expose governed references used by other Suite institutions.

It does not generate or own the downstream canonical objects of Registry, Chronicle, Anchor, Beacon, Attestor, or Navigator.

## Relationship to Suite Standards

Suite Standards define the expectations applied during certification.

This Certifier methodology surface should remain aligned with those standards but must not become a competing standards authority.

## Relationship to Suite Methodology

Suite Methodology is the governing process layer.

This directory documents how Certifier operationally applies that process.

The distinction is:

```text
Suite Methodology
→ governs implementation

Certifier Methodology Surface
→ documents Certifier's application of that implementation
```

## Relationship to Evidence

Evidence supports Certifier evaluation.

The methodology should preserve distinctions among:

- evidence collection;
- Evidence Records;
- Evidence Inventory;
- Evidence Mapping;
- Evidence Review;
- evaluation;
- findings;
- certification decision.

Evidence does not automatically dictate the outcome.

## Relationship to Registry

Registry may create a Satoshium Registry Entry / SREG referencing a governed Certifier or source object.

Certifier does not own the Registry Entry.

## Relationship to Chronicle

Chronicle may preserve a Chronicle Entry associated with significant certification chronology.

Certifier does not own the Chronicle Entry.

## Relationship to Anchor

Anchor may preserve an Integrity Reference associated with a Certifier artifact.

Certifier does not own the Integrity Reference.

## Relationship to Beacon

Beacon may publish Discovery Signals / Discovery Metadata associated with governed records.

Certifier does not own Beacon discovery objects.

## Relationship to Attestor

Attestor is operational and institutionally distinct from Certifier.

Its canonical flow is:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

Certifier methodology should not conflate:

- certification evaluation;
- Attestor evaluation;
- certification outcome;
- Attestation; or
- Trust Statement.

## Relationship to Navigator

Navigator defines and orchestrates workflows.

Navigator may consume or route governed Certifier records without owning the certification decision.

## Authority Discipline

This directory should preserve the following distinctions:

- Suite Methodology ≠ Certifier-owned methodology
- Evidence ≠ Evaluation
- Evaluation ≠ Certification Decision
- Certification Decision ≠ Attestation
- Certification Decision ≠ Trust Statement
- Certification Package ≠ downstream Suite object
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Historical and Version Discipline

Earlier Certifier documentation may have framed methodology as a Certifier-owned rule system.

Current architecture supersedes that framing.

Historical records may remain historically accurate, but current-state documentation should preserve the Suite-wide model in which Methodology governs implementation and Certifier performs certification.

## Repository Expectations

Changes to this directory should preserve:

1. Suite Methodology as the governing implementation layer;
2. Certifier as the operational certification institution;
3. the Certification Package as Certifier's canonical operational record;
4. evidence/evaluation/decision distinctions;
5. separation between Certifier and Attestor evaluation;
6. separation between Certifier artifacts and downstream Suite objects;
7. current Suite object terminology; and
8. the rule that reference does not transfer authority.

## Governing Principle

**Suite Methodology defines how certification review is performed; Certifier applies that methodology and preserves the resulting certification record.**
