# Satoshium Certifier — Documentation Library

**Path:** `/certifier/docs/`  
**Institution:** Satoshium Certifier  
**Surface:** Certifier Documentation Library  
**Status:** Current repository documentation

## Purpose

This directory contains the supporting Markdown documentation for **Satoshium Certifier**.

These documents preserve explanatory, architectural, lifecycle, evidence, interoperability, template, status, and workflow material associated with Certifier.

The directory currently contains:

- `certification-classes.md`
- `certification-lifecycle.md`
- `certification-philosophy.md`
- `certification-targets.md`
- `certifier-overview.md`
- `evidence-model.md`
- `interoperability.md`
- `receipt-template.md`
- `report-template.md`
- `status-definitions.md`
- `workflow-diagram.md`

This README serves as the repository entry point for that documentation set.

## Institutional Boundary

Satoshium Certifier is the Suite institution responsible for certification.

The enduring architectural rule is:

> **Standards define expectations. Methodology defines implementation. Certifier performs certification.**

The canonical operational record produced by Certifier is the **Certification Package**.

Documentation in this directory supports understanding and implementation of Certifier.

It does not independently redefine Suite Standards, Suite Methodology, or the authority of other Suite institutions.

## Documentation Set

### `certifier-overview.md`

Overview documentation for Satoshium Certifier and its role within the Satoshium Suite.

### `certification-philosophy.md`

Documentation concerning the conceptual principles and philosophy underlying Certifier.

### `certification-targets.md`

Documentation concerning the kinds of subjects or operational objects that may participate in certification.

### `certification-classes.md`

Documentation concerning Certifier Certification Classes and their role in communicating certification outcomes.

### `certification-lifecycle.md`

Documentation concerning certification lifecycle stages and status progression.

### `evidence-model.md`

Documentation concerning the role and treatment of evidence within Certifier.

### `interoperability.md`

Documentation concerning Certifier relationships with other Satoshium Suite institutions and governed downstream references.

### `receipt-template.md`

Template documentation for Certification Receipt structures.

### `report-template.md`

Template documentation for certification-report structures.

### `status-definitions.md`

Documentation defining Certifier status terminology.

### `workflow-diagram.md`

Documentation describing or illustrating the Certifier workflow.

## Canonical Certifier Model

The current Certifier architecture should remain consistent with the following high-level relationship:

```text
Suite Standards
        ↓
Suite Methodology
        ↓
Certification Subject
        ↓
Certification Package
        ↓
Certification Decision
        ↓
Generated Certifier Artifacts
```

Generated Certifier artifacts may include:

- Certification Process Report (SCPR);
- Certification Receipt (SCR); and
- Certified Record (SCRD HTML / JSON).

The Certification Package remains Certifier's canonical operational record.

## Relationship to Suite Standards

Suite Standards define the expectations applied during certification.

Documents in `/certifier/docs/` may explain how Certifier uses those expectations, but Certifier documentation should not silently become the Suite-wide standards authority.

## Relationship to Suite Methodology

Suite Methodology defines implementation and repeatable process.

Certifier documentation may explain or visualize that process as it applies to certification, but it should remain aligned with the governing Suite Methodology.

## Evidence Boundary

Evidence supports certification evaluation.

Evidence does not independently create the certification decision.

Documentation in this directory should preserve distinctions among:

- evidence;
- evaluation;
- certification decision;
- certification outcome;
- lifecycle status; and
- downstream Suite references.

## Interoperability Boundary

Certifier outputs may participate in governed relationships with other Suite institutions.

Current Suite object boundaries include:

- **Registry** → Satoshium Registry Entry / SREG
- **Chronicle** → Chronicle Entry
- **Anchor** → Integrity Reference
- **Beacon** → Discovery Signal / Discovery Metadata
- **Attestor** → Attestation / Rule-Constrained Evaluation / Trust Statement
- **Navigator** → Workflow Definition / Orchestration

Certifier documentation should not imply that Certifier owns those downstream canonical objects.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Attestor Boundary

Certifier and Attestor are distinct institutions.

The current Attestor flow is:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

Certifier documentation should not use legacy Attestor terminology such as `SATR` as the current object model.

A Certification Class, certification outcome, or confidence posture is not an Attestor Trust Statement.

## Lifecycle and Status Discipline

Documentation in this directory should preserve distinctions among:

- certification creation;
- evaluation;
- decision;
- issuance;
- activation;
- publication;
- correction;
- supersession; and
- historical preservation.

Lifecycle terminology should remain consistent with the canonical Certification Package and Suite Methodology.

## Templates

Receipt and report templates should remain subordinate to the canonical Certification Package.

Templates define presentation or record structure.

They do not create certification authority.

Where production artifacts differ from older templates, current production architecture should govern current-state documentation while historical templates may remain preserved as historical material where appropriate.

## Repository Expectations

Changes to this directory should preserve:

1. Certifier as the certification institution;
2. the Certification Package as the canonical operational record;
3. Suite Standards as the expectations layer;
4. Suite Methodology as the implementation layer;
5. evidence/evaluation/decision distinctions;
6. current Suite object terminology;
7. separation between Certifier and Attestor authority;
8. historical terminology where intentionally preserved;
9. consistency across templates, lifecycle, status, workflow, and interoperability documentation; and
10. the rule that reference does not transfer authority.

## Reconciliation Note

This README documents the directory and the currently established Certifier architecture.

The individual Markdown files listed above should be reviewed separately during documentation reconciliation before assuming that every file already reflects the current architecture.

In particular, later file-by-file review should check for:

- legacy `SATR` terminology;
- legacy Chronicle or Anchor object names;
- stale Attestor status language;
- trust terminology that overlaps with Attestor;
- lifecycle/status conflation;
- outdated Suite institution roles; and
- historical terminology presented as current architecture.

## Governing Principle

**Certifier documentation explains the certification architecture that exists; it does not independently redesign Suite authority or redefine canonical objects.**
