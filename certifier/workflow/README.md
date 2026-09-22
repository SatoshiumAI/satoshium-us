# Satoshium Certifier — Workflow

**Path:** `/certifier/workflow/`  
**Institution:** Satoshium Certifier  
**Surface:** Workflow  
**Status:** Current repository documentation

## Purpose

This directory documents the operational workflow used by **Satoshium Certifier** when applying Suite Standards and Suite Methodology to a defined Certification Subject.

The public page for this directory is:

- `index.html`

This README documents the current workflow sequence, canonical record boundary, generated artifacts, downstream Suite relationships, and the distinctions that must remain intact across evaluation, lifecycle, and Attestor interoperability.

## Workflow Role

Workflow is the operational backbone of Certifier.

The enduring relationship is:

> **Standards define expectations. Methodology defines implementation. Certifier performs certification.**

The workflow applies those governing layers in a repeatable sequence.

## Canonical Workflow

The current Certifier workflow is:

```text
Certification Subject
        ↓
Evidence Inventory
        ↓
Certification Package
        ↓
Evaluation & Certification Decision
        ↓
SCPR · SCR · SCRD HTML / JSON
        ↓
Governed Suite Relationships
```

The **Certification Package** remains Certifier's canonical operational record.

Generated artifacts derive from that Package.

## Step 1 — Certification Subject

The workflow begins by identifying and bounding the object considered for certification.

A Certification Subject may include an artifact, record, workflow, service, dataset, tool, page, subsystem, or other governed object.

The subject should be sufficiently bounded so that:

- evidence can be collected;
- standards can be applied;
- scope can be understood;
- evaluation can be reproduced; and
- the resulting certification can be reviewed later.

Selection as a Certification Subject does not transfer source authority to Certifier.

## Step 2 — Evidence Assembly

Evidence is collected, organized, preserved, and associated with the Certification Package.

The Evidence Inventory forms part of the canonical certification record.

Evidence may include:

- URLs;
- screenshots;
- reports;
- metadata;
- source records;
- supporting documentation;
- hashes; and
- preserved references.

Evidence supports evaluation.

Evidence does not independently create the certification decision.

## Step 3 — Certification Package

The Certification Package is Certifier's canonical operational record.

It preserves the certification context including:

- Certification Subject;
- scope;
- applicable Suite Standards;
- applicable Suite Methodology;
- evidence;
- review notes;
- assessment;
- certification decision;
- generated artifacts; and
- certification history.

Generated artifacts should derive from the Certification Package rather than redefining the certification independently.

## Step 4 — Evaluation and Certification Decision

Certifier evaluates the evidence against the applicable Suite Standards using Suite Methodology.

The Certification Package should preserve:

- findings;
- limitations;
- confidence posture where applicable;
- review rationale; and
- certification decision.

Public artifacts should be generated only after the certification decision has been finalized.

## Evaluation vs Lifecycle

The workflow should preserve a clear distinction between:

- evaluation outcome;
- certification decision;
- certification status; and
- lifecycle state.

Terms such as `Pass`, `Conditional Pass`, and `Fail` may represent evaluation or certification outcomes.

Terms such as `Expired`, `Renewed`, or `Revoked` may represent lifecycle or status conditions.

The exact category boundary should be governed by Suite Standards and Suite Methodology and reviewed during Suite Reconciliation where ambiguity remains.

## Step 5 — Generated Artifacts

After the decision is finalized, the Certification Package may generate Certifier artifacts including:

- **SCPR** — Certification Process Report
- **SCR** — Certification Receipt
- **SCRD HTML**
- **SCRD JSON**

These artifacts support public review, verification of certification, indexing, preservation, and interoperability.

They do not replace the Certification Package.

## Step 6 — Governed Suite Relationships

After Certifier artifacts are generated, other Suite institutions may interact with those records under their own governed responsibilities.

Current relationships include:

- **Registry** → catalogs through SREG
- **Chronicle** → preserves chronology through CHR
- **Anchor** → preserves integrity through ANCH
- **Beacon** → publishes Discovery Signals / Discovery Metadata
- **Attestor** → may consume eligible governed inputs to produce ATT / TRST
- **Navigator** → defines and orchestrates workflows

These downstream relationships must not alter the underlying certification itself.

## Registry Boundary

Registry owns the Satoshium Registry Entry / SREG.

Certifier may expose governed records or references suitable for Registry consumption.

Registry does not become Certifier's source authority.

## Chronicle Boundary

Chronicle owns Chronicle Entries.

Chronicle preserves chronology.

It does not replace the Certification Package or certification decision.

## Anchor Boundary

Anchor owns Integrity References.

Anchor preserves integrity without becoming certification authority.

## Beacon Boundary

Beacon owns Discovery Signals / Discovery Metadata.

Discovery does not change certification status or authority.

## Attestor Boundary

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

Attestor does not simply “verify” Certifier records in a generic sense.

Current documentation should preserve the distinction between:

- Certifier evaluation;
- certification decision;
- Attestation;
- Attestor rule-constrained evaluation; and
- Trust Statement.

## Navigator Boundary

Navigator defines and orchestrates workflows.

Navigator may consume certified records without becoming the certification authority.

## Workflow Outputs

Current workflow outputs include:

- Certification Package;
- Evidence Inventory;
- SCPR;
- SCR;
- SCRD HTML;
- SCRD JSON; and
- governed Suite relationships.

Downstream Suite objects remain owned by their respective institutions.

## Reproducibility and Reviewability

A consistent workflow should make certification:

- reproducible;
- understandable;
- auditable;
- reviewable;
- preservable; and
- interoperable.

The goal is not “repeatable trust.”

The goal is **repeatable, reviewable certification**.

## Authority Discipline

This directory should preserve the following distinctions:

- Workflow ≠ Authority
- Evidence ≠ Evaluation
- Evaluation ≠ Certification Decision
- Certification Decision ≠ Lifecycle State
- Certification Decision ≠ Attestation
- Certification Decision ≠ Trust Statement
- Generated Artifact ≠ Certification Package
- SREG ≠ Source Record
- CHR ≠ Certification Record
- ANCH ≠ Certification Authority
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Suite Reconciliation Considerations

The following should be reviewed during Suite Reconciliation rather than redesigned in this README pass:

1. the exact boundary among evaluation outcome, certification decision, certification status, and lifecycle state;
2. whether any workflow step should explicitly include Profile or Scope before Evidence Inventory;
3. whether downstream Suite relationships should be modeled as a single terminal workflow stage or as separate institution-specific integrations; and
4. how Certifier confidence posture should remain bounded from Attestor Trust Statements.

## Repository Expectations

Changes to this directory should preserve:

1. the Certification Package as Certifier's canonical operational record;
2. Suite Standards as the expectations layer;
3. Suite Methodology as the implementation layer;
4. evidence/evaluation/decision distinctions;
5. lifecycle separation;
6. current Suite object terminology;
7. separation between Certifier and Attestor authority;
8. downstream institutional ownership; and
9. the rule that reference does not transfer authority.

## Governing Principle

**Certifier workflow makes certification repeatable and reviewable while preserving the authority boundaries of every Suite institution it touches.**
