# Satoshium Certifier — Standards

**Path:** `/certifier/standards/`  
**Institution:** Satoshium Certifier  
**Surface:** Standards  
**Status:** Current repository documentation

## Purpose

This directory documents how **Satoshium Certifier applies Satoshium Suite Standards** as the governing expectations for certification review.

The public page for this directory is:

- `index.html`

This README documents the relationship between Suite Standards and Certifier, the standards categories currently referenced by Certifier, versioning and preservation expectations, and the institutional boundaries that must remain intact.

## Governing Boundary

Suite Standards are Suite-level governing expectations.

Certifier does not independently own the certification rule layer.

The enduring relationship is:

```text
Suite Standards
        ↓
Suite Methodology
        ↓
Satoshium Certifier
        ↓
Certification Package
        ↓
Generated Certifier Artifacts
```

The established rule remains:

> **Standards define expectations. Methodology defines implementation. Certifier performs certification.**

## Suite Standards

Suite Standards define the expectations applied across certification activity.

Current standards-related domains may include:

- certification;
- evidence;
- governance;
- interoperability;
- schemas;
- terminology;
- scoring / evaluation;
- versioning; and
- trust-related certification context.

Certifier applies these standards.

It does not replace them.

## Certifier Implementation

Certifier serves as the Suite's operational certification implementation.

It applies Suite Standards and Suite Methodology to a defined Certification Subject and preserves the resulting certification record.

The Certification Package remains Certifier's canonical operational record.

## Certification Standard

The Certification Standard defines the expectations applicable to a certification review.

Those expectations may include:

- scope;
- applicable standards;
- evidence sufficiency;
- evaluation logic;
- Certification Class;
- certification decision; and
- certification history.

The standard defines expectations.

The Certification Package records how those expectations were applied to a specific certification.

## Evidence Standard

The Evidence Standard defines expectations for factual materials supporting certification review.

Evidence may include:

- source references;
- documentation;
- reports;
- screenshots;
- inventories;
- mappings;
- hashes;
- notes; and
- preserved context.

Evidence supports evaluation.

Evidence does not independently create the certification decision.

## Trust Standard

The current Standards surface includes a **Trust Standard**.

Within Certifier, that standard should remain bounded to trust-related certification context and reviewability.

It must not be interpreted as replacing Satoshium Attestor's canonical trust architecture.

Attestor remains responsible for:

```text
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

A Certifier standard, certification outcome, confidence posture, or Certification Class is not an Attestor Trust Statement.

## Interoperability Standards

Interoperability Standards help ensure that Certifier outputs can participate in governed Suite relationships.

Current institutional roles include:

- **Registry** — Satoshium Registry Entry / SREG
- **Chronicle** — Chronicle Entry
- **Anchor** — Integrity Reference
- **Beacon** — Discovery Signal / Discovery Metadata
- **Attestor** — Attestation / Trust Statement
- **Navigator** — workflow definition / orchestration

Interoperability does not transfer source authority.

## Schema Standards

Schema Standards govern structured representation expectations for certification records and interoperability.

They may apply to:

- Certification Packages;
- SCRD JSON;
- evidence inventories;
- generated artifacts; and
- governed Suite references.

Schema does not create certification authority.

## Versioning Standards

Standards should preserve the relationship among:

- certification records;
- standards versions;
- methodology versions;
- review dates;
- generated artifacts;
- revisions;
- renewals;
- revocations; and
- archived states.

Historical certifications should remain understandable in the context of the standards that governed them when issued.

## Operational Standards Flow

At a high level:

```text
Certification Subject
        ↓
Applicable Suite Standards
        ↓
Suite Methodology
        ↓
Evidence Review
        ↓
Certification Package
        ↓
Evaluation + Certification Decision
        ↓
SCPR · SCR · SCRD
        ↓
Governed Suite Relationships
```

The generated Certifier artifacts remain downstream from the Certification Package.

## Relationship to Certification Classes

Certification Classes communicate the result of completed certification.

Standards define the expectations governing how a class may be assigned.

Certification Classes do not independently create certification authority.

## Relationship to Evaluation

Standards define expectations.

Evaluation applies documented reasoning to the evidence under those expectations.

The distinction is:

```text
Standard
≠
Evaluation

Evaluation
≠
Certification Decision
```

## Relationship to Evidence

Standards define evidence expectations.

Evidence provides factual support.

Evidence should remain traceable to:

- the Certification Subject;
- applicable standards;
- Suite Methodology;
- findings;
- limitations;
- evaluation; and
- certification decision.

## Relationship to Reports and Receipts

Generated Certifier artifacts communicate different aspects of the completed certification:

- **SCPR** — explains the review process and reasoning;
- **SCR** — provides concise public confirmation;
- **SCRD** — preserves the durable Certified Record.

All remain subordinate to the canonical Certification Package.

## Relationship to Registry

Registry may create a Satoshium Registry Entry / SREG referencing governed Certifier records.

Registry does not become the source authority for the standard or certification merely by referencing it.

## Relationship to Chronicle

Chronicle may preserve governed chronology concerning standards adoption, revision, certification events, or related milestones.

Chronicle records when.

It does not become standards authority.

## Relationship to Anchor

Anchor may preserve Integrity References associated with standards or certification artifacts.

Anchor preserves integrity.

It does not define the standard.

## Relationship to Beacon

Beacon may publish Discovery Signals / Discovery Metadata associated with standards or certification records.

Discovery does not alter standards authority.

## Relationship to Attestor

Attestor is operational and institutionally distinct from Certifier.

Standards may support governed interoperability with Attestor, but Certifier Standards should not define Attestor's canonical Attestation or Trust Statement semantics.

## Relationship to Navigator

Navigator may define or orchestrate workflows involving standards-governed Certifier activity.

Navigator does not become standards authority or certification authority through orchestration.

## Authority Discipline

This directory should preserve the following distinctions:

- Suite Standards ≠ Certifier-owned rule layer
- Standard ≠ Evaluation
- Evaluation ≠ Certification Decision
- Certification Decision ≠ Trust Statement
- Certification Class ≠ Trust Statement
- Schema ≠ Authority
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Historical and Version Discipline

Earlier Certifier documentation may describe the standards directory as Certifier's own rulebook or may refer to future Suite integrations.

Those descriptions may remain historically useful but should not govern current-state architecture.

Current documentation should reflect that:

- Suite Standards are Suite-level;
- Certifier applies them;
- Registry, Chronicle, Anchor, Beacon, Attestor, and Navigator are operational institutions; and
- current object terminology should be used for present-state references.

## Suite Reconciliation Considerations

The following matters should be reviewed during Suite Reconciliation rather than redesigned in this README pass:

1. the precise boundary of the **Trust Standard** relative to Attestor Trust Statements;
2. whether `Pass`, `Conditional Pass`, `Fail`, `Revoked`, and related terms belong to evaluation, certification decision, status, or lifecycle;
3. whether any Certifier-specific standards should remain separately named or be represented only as Suite Standards;
4. how schema requirements should be governed across Certifier and the broader Suite; and
5. how standards versioning should be represented consistently across historical certifications.

## Repository Expectations

Changes to this directory should preserve:

1. Suite Standards as the governing expectations layer;
2. Suite Methodology as the implementation layer;
3. Certifier as the operational certification institution;
4. the Certification Package as Certifier's canonical operational record;
5. evidence/evaluation/decision distinctions;
6. separation between Certifier trust-related terminology and Attestor Trust Statements;
7. current Suite object terminology;
8. standards versioning and historical traceability; and
9. the rule that reference does not transfer authority.

## Governing Principle

**Suite Standards define the expectations; Certifier applies them and preserves their application in reviewable certification records.**
