# Satoshium Certifier — Governance

**Path:** `/certifier/governance/`  
**Institution:** Satoshium Certifier  
**Surface:** Governance  
**Status:** Current repository documentation

## Purpose

This directory contains the **Satoshium Certifier Governance** surface.

Governance explains how Certifier is maintained as the Suite's operational certification implementation while remaining aligned with Suite Standards and Suite Methodology.

The public page for this directory is:

- `index.html`

This README documents the governance role, stewardship responsibilities, revision discipline, record-preservation expectations, and institutional boundaries of Certifier governance.

## Governance Role

Certifier governance is the operational stewardship layer for Certifier.

It helps preserve:

- implementation coherence;
- version control;
- record integrity;
- evidence traceability;
- artifact consistency;
- historical reviewability; and
- alignment with Suite Standards and Suite Methodology.

Governance does not independently define Suite-wide certification rules.

## Governing Relationship

The enduring relationship remains:

```text
Suite Standards
        ↓
Suite Methodology
        ↓
Certifier Governance
        ↓
Certification Package
        ↓
Generated Certifier Artifacts
        ↓
Governed Suite Relationships
```

The established rule remains:

> **Standards define expectations. Methodology defines implementation. Certifier performs certification.**

Governance preserves the coherence of that implementation.

## Suite Alignment

Suite Standards define certification expectations.

Suite Methodology defines the repeatable certification process.

Certifier governance ensures that:

- public pages;
- schemas;
- templates;
- workflows;
- artifact formats;
- evidence models;
- status definitions; and
- generated outputs

remain aligned with those governing layers.

## Revision Control

Substantive changes to Certifier should be versioned, recorded, or preserved as appropriate.

Revision control may apply to:

- certification pages;
- schemas;
- templates;
- artifact formats;
- evidence models;
- workflows;
- definitions;
- status models; and
- operational references.

Historical meaning should remain recoverable when current architecture evolves.

## Record Preservation

Certifier favors preservation over deletion.

Where practical, superseded, expired, revoked, archived, corrected, or replaced certification materials should remain reviewable.

Preservation supports:

- historical reconstruction;
- auditability;
- provenance;
- comparison across versions; and
- understanding of prior certification decisions.

## Decision Integrity

Certification decisions should remain traceable to:

- Certification Subject;
- Scope;
- applicable Suite Standards;
- applied Suite Methodology;
- Evidence Records;
- findings;
- limitations;
- evaluation;
- assessment;
- Certification Class where applicable; and
- the canonical Certification Package.

The Certification Package remains Certifier's canonical operational record.

## Artifact Stewardship

Governance maintains the relationship between the Certification Package and generated Certifier artifacts.

Current Certifier artifacts include:

- **SCPR** — Certification Process Report
- **SCR** — Certification Receipt
- **SCRD HTML**
- **SCRD JSON**
- **SEV** — Evidence Record

Governed downstream Suite relationships may include:

- **SREG** — Satoshium Registry Entry
- **CHR** — Chronicle Entry
- **ANCH** — Integrity Reference
- **ATT** — Attestation
- **TRST** — Trust Statement

These downstream objects remain owned by their respective Suite institutions.

## Relationship to Registry

Registry owns the Satoshium Registry Entry / SREG.

Certifier governance should preserve the reference relationship without implying that Certifier owns Registry objects.

## Relationship to Chronicle

Chronicle owns Chronicle Entries.

Chronicle preserves governed chronology associated with certification activity.

Chronicle does not replace the Certification Package or certification decision.

## Relationship to Anchor

Anchor owns Integrity References.

Anchor may preserve integrity relationships associated with Certifier artifacts without becoming the certification authority.

## Relationship to Beacon

Beacon owns Discovery Signals / Discovery Metadata.

Beacon may make governed certification records discoverable without changing their authority.

## Relationship to Attestor

Attestor is operational and institutionally distinct from Certifier.

The current Attestor architecture is:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

Certifier governance should preserve the distinction between:

- certification decision;
- certification outcome;
- Certification Class;
- Attestation; and
- Trust Statement.

Legacy `SATR` terminology should not be used as the current Attestor object model.

## Relationship to Navigator

Navigator defines and orchestrates workflows.

Governance should preserve Certifier compatibility with Navigator without transferring Certifier authority over certification decisions.

## Authority Discipline

This directory should preserve the following distinctions:

- Governance ≠ Suite Standards
- Governance ≠ Suite Methodology
- Governance ≠ Certification Decision
- Certification Package ≠ downstream Suite object
- Revision ≠ deletion
- Correction ≠ supersession
- Reference ≠ derivation
- Reference ≠ support
- Connection ≠ identity
- Certification Decision ≠ Attestation
- Certification Decision ≠ Trust Statement

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Historical and Version Discipline

Certifier may evolve.

Governance should ensure that older records remain understandable in the context of the architecture and terminology that existed when they were created.

Historical terminology may remain preserved where accurate.

Current-state pages should use current canonical Suite object names.

## Suite Reconciliation Considerations

The following should be reviewed during Suite Reconciliation rather than redesigned in this README pass:

1. whether governance should own any explicit version registry or governance record;
2. how correction, supersession, and versioning should be represented consistently across Certifier;
3. whether artifact stewardship should be formalized as a governed Certifier control; and
4. how Certifier governance should reference Suite-wide governance without duplicating it.

## Repository Expectations

Changes to this directory should preserve:

1. Certifier as the operational certification institution;
2. Suite Standards as the expectations layer;
3. Suite Methodology as the implementation layer;
4. the Certification Package as canonical operational record;
5. revision and preservation discipline;
6. current Suite object terminology;
7. separation between institutional authorities;
8. historical reviewability; and
9. the rule that reference does not transfer authority.

## Governing Principle

**Governance preserves Certifier coherence over time without replacing Suite Standards, Suite Methodology, or the authority of other Suite institutions.**
