# Satoshium Certifier — Trust Model

**Path:** `/certifier/trust-model/`  
**Institution:** Satoshium Certifier  
**Surface:** Trust Model / Trust-Related Certification Context  
**Status:** Current repository documentation

## Purpose

This directory documents how Satoshium Certifier makes certification outcomes reviewable through evidence, Suite Standards, Suite Methodology, the canonical Certification Package, generated artifacts, and governed Suite relationships.

The public page for this directory is:

- `index.html`

The term **Trust Model** is retained as the existing public surface name.

Current architecture requires that its meaning remain bounded:

**Certifier establishes reviewable certification context. Attestor owns governed Attestation, Rule-Constrained Evaluation, and Trust Statement.**

## Governing Boundary

Certifier does not issue a universal trust conclusion.

Certifier performs certification.

Its governing relationship is:

```text
Suite Standards
        ↓
Suite Methodology
        ↓
Evidence Review
        ↓
Certification Package
        ↓
Certification Decision
        ↓
SCPR · SCR · SCRD
```

The Certification Package remains Certifier's canonical operational record.

## Reviewable Certification Context

Certifier supports confidence in certification by preserving:

- evidence;
- source references;
- methodology application;
- review findings;
- limitations;
- decision reasoning;
- Certification Package provenance;
- public artifacts; and
- governed Suite relationships.

These elements make certification reviewable.

They do not independently become an Attestor Trust Statement.

## Evidence

Reviewable certification begins with evidence.

Certification conclusions should remain traceable to:

- Evidence Records;
- Evidence Inventory;
- source materials;
- supporting references;
- integrity material;
- documented findings; and
- review context.

Evidence supports evaluation.

Evidence does not independently create the certification decision.

## Transparent Methodology

Suite Methodology defines how certification review is performed.

Certifier applies that methodology to the Certification Subject and preserves the reasoning behind the resulting certification decision.

The enduring rule remains:

> **Standards define expectations. Methodology defines implementation. Certifier performs certification.**

## Generated Artifacts

The canonical Certification Package may generate Certifier artifacts including:

- **SCPR** — Certification Process Report;
- **SCR** — Certification Receipt;
- **SCRD HTML**; and
- **SCRD JSON**.

These artifacts communicate or preserve parts of the certification result.

They do not replace the Certification Package.

## Governed Suite Relationships

Certification records may participate in governed relationships with other Suite institutions.

Current institutional roles include:

- **Registry** → Satoshium Registry Entry / SREG
- **Chronicle** → Chronicle Entry / CHR
- **Anchor** → Integrity Reference / ANCH
- **Beacon** → Discovery Signal / Discovery Metadata
- **Attestor** → Attestation / ATT and Trust Statement / TRST
- **Navigator** → Workflow Definition / Orchestration

These relationships may strengthen discoverability, chronology, integrity, interoperability, or downstream evaluation.

They do not transfer Certifier authority.

## Attestor Boundary

Attestor is operational and institutionally distinct from Certifier.

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

Therefore:

- Certification Outcome ≠ Trust Statement
- Certification Class ≠ Trust Statement
- Certifier Confidence Posture ≠ Trust Statement
- SCR ≠ Attestation
- SCRD ≠ Attestation
- Certification Package ≠ Attestation
- Certifier Evaluation ≠ Attestor Rule-Constrained Evaluation

Attestor may consume eligible governed Certifier outputs.

That consumption does not convert Certifier artifacts into Attestor objects.

## Trust Production Terminology

Earlier Certifier material used phrases such as:

- produces trust;
- reviewable trust;
- trust production;
- attestation-ready;
- verification support.

Those phrases should now be interpreted carefully.

Current-state architecture should prefer language such as:

- reviewable certification;
- certification confidence;
- reviewable certification context;
- governed Attestor interoperability; and
- downstream Attestor evaluation where eligible.

The term **Trust Statement** should remain reserved for the governed Attestor object unless a different Suite-wide definition is explicitly established.

## Public Verification

Certification Receipts and Certified Records allow users to confirm:

- what was certified;
- when certification occurred;
- the certification result;
- applicable class or status; and
- where supporting records can be reviewed.

Public verification of certification does not equal an Attestor Trust Statement.

## Long-Term Preservation

Governed Suite institutions extend the durability and usability of certification records through distinct responsibilities:

- Registry catalogs governed records;
- Chronicle preserves chronology;
- Anchor preserves integrity references;
- Beacon supports discovery;
- Attestor performs governed assertion/evaluation/trust operations;
- Navigator orchestrates workflows.

No one downstream relationship replaces the Certification Package as Certifier's canonical operational record.

## Atlas Trust Context

Atlas certification may include trust-related dimensions, signals, metadata, evidence, currency, completeness, traceability, or reproducibility as part of the certification context.

Those Atlas dimensions remain distinct from Attestor Trust Statements.

A Certifier review of Atlas trust-related characteristics does not make Certifier the Suite's trust authority.

## Relationship to the Suite Trust Standard

The public Trust Model links to the Suite Trust Standard.

That standard may govern trust-related expectations relevant to certification.

Its precise relationship to mature Attestor Trust Statements should remain subject to Suite Reconciliation.

Certifier should apply Suite-level expectations without redefining Attestor's canonical trust objects.

## Authority Discipline

This directory should preserve the following distinctions:

- Certification ≠ Attestation
- Certification Evaluation ≠ Attestor Evaluation
- Certification Outcome ≠ Trust Statement
- Certification Class ≠ Trust Statement
- Confidence Posture ≠ Trust Statement
- Reviewable Certification Context ≠ Universal Trust
- Evidence ≠ Trust Statement
- Registry Entry ≠ Certification Decision
- Integrity Reference ≠ Certification Decision
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Suite Reconciliation Considerations

This page deserves explicit Suite Reconciliation because its historical name and language overlap directly with Attestor.

The following should be resolved then:

1. whether **Trust Model** remains the preferred name for this Certifier surface;
2. whether Certifier should instead describe a **Certification Confidence Model**, **Reviewability Model**, or another bounded concept;
3. the precise role of the Suite Trust Standard relative to Attestor;
4. whether Certifier confidence posture should remain part of certification classes or evaluation;
5. how Atlas trust dimensions relate to Certifier review and Attestor Trust Statements; and
6. whether any current use of “trust” in Certifier documentation implies authority that now belongs to Attestor.

These are architectural questions and should not be decided solely through README reconciliation.

## Repository Expectations

Changes to this directory should preserve:

1. Certifier as certification authority;
2. the Certification Package as Certifier's canonical operational record;
3. evidence-based and reviewable certification;
4. separation between certification and Attestor trust operations;
5. current Suite object terminology;
6. governed cross-institution relationships;
7. historical terminology where intentionally preserved; and
8. the rule that reference does not transfer authority.

## Governing Principle

**Certifier makes certification reviewable; Attestor owns governed Attestation, Rule-Constrained Evaluation, and Trust Statement.**
