# Satoshium Certifier — Trust

**Path:** `/certifier/trust/`  
**Institution:** Satoshium Certifier  
**Surface:** Trust / Certification Confidence  
**Status:** Current repository documentation

## Purpose

This directory documents the public-facing trust-related context of **Satoshium Certifier**.

The existing public surface is named **Trust**, but current Suite architecture requires that its meaning remain bounded to **reviewable certification confidence** rather than Attestor-owned Trust Statements.

The public page for this directory is:

- `index.html`

This README documents the Certifier trust-related surface, its relationship to evidence and certification confidence, and the authority boundary with Satoshium Attestor.

## Governing Boundary

Certifier performs certification.

It does not issue a universal trust conclusion.

The current institutional relationship is:

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

## Reviewable Certification Confidence

Certifier supports confidence in certification by making its work reviewable.

That confidence derives from:

- preserved Evidence Records;
- transparent reasoning;
- applicable Suite Standards;
- applied Suite Methodology;
- findings and limitations;
- confidence posture where applicable;
- the canonical Certification Package;
- generated certification artifacts; and
- governed Suite relationships.

This is not equivalent to an Attestor Trust Statement.

## Evidence-Based Reviewability

Reviewable certification begins with preserved evidence.

Certification conclusions should remain traceable to:

- documented source material;
- Evidence Inventories;
- reviewer observations;
- supporting references;
- integrity material;
- findings; and
- the Certification Package.

Evidence supports evaluation.

Evidence does not independently create the certification decision.

## Transparent Reasoning

Certification confidence depends on transparent reasoning.

Certifier should preserve:

- scope;
- applicable Suite Standards;
- applied Suite Methodology;
- findings;
- limitations;
- confidence posture;
- certification decision; and
- supporting rationale.

Reviewability is strengthened when the basis of the decision remains visible.

## Generated Artifacts

Certifier makes certification outcomes publicly reviewable through artifacts generated from the canonical Certification Package.

These may include:

- **SCPR** — Certification Process Report;
- **SCR** — Certification Receipt;
- **SCRD HTML**; and
- **SCRD JSON**.

Generated artifacts communicate the certification result.

They do not replace the Certification Package.

## Governed Suite Integration

Certification records may participate in governed relationships across the Suite.

Current roles include:

- **Registry** → Satoshium Registry Entry / SREG
- **Chronicle** → Chronicle Entry / CHR
- **Anchor** → Integrity Reference / ANCH
- **Beacon** → Discovery Signal / Discovery Metadata
- **Attestor** → Attestation / ATT and Trust Statement / TRST
- **Navigator** → Workflow Definition / Orchestration

These institutions add cataloging, chronology, integrity, discovery, downstream evaluation, or orchestration.

They do not transfer authority over the Certifier record.

## Certification Confidence Flow

The current bounded Certifier model is:

```text
Certification Subject
        ↓
Evidence Records & Evidence Review
        ↓
Suite Standards & Suite Methodology
        ↓
Certification Package
        ↓
Evaluation & Certification Decision
        ↓
SCPR · SCR · SCRD HTML / JSON
        ↓
Governed Suite Relationships
        ↓
Reviewable Certification Confidence
```

The final state above is a Certifier confidence/reviewability concept.

It is not a canonical Attestor object.

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

Therefore:

- Certification Outcome ≠ Trust Statement
- Certification Class ≠ Trust Statement
- Certifier Confidence Posture ≠ Trust Statement
- SCR ≠ Attestation
- SCRD ≠ Attestation
- Certification Package ≠ Attestation
- Certifier Evaluation ≠ Attestor Rule-Constrained Evaluation

Attestor may consume eligible governed Certifier outputs.

That downstream use does not change the identity of Certifier artifacts.

## Public Verification

Certification Receipts and Certified Records provide concise public confirmation of what was certified.

They may communicate:

- certification identity;
- certification date;
- certification result;
- class or status;
- source package; and
- links to supporting records.

Public verification of certification is not the same as an Attestor Trust Statement.

## Long-Term Preservation

Governed Suite institutions extend the usability of certification records after issuance through distinct responsibilities:

- Registry catalogs;
- Chronicle preserves chronology;
- Anchor preserves integrity references;
- Beacon supports discovery;
- Attestor performs governed assertion, evaluation, and trust operations;
- Navigator orchestrates workflows.

These relationships remain institutionally separate.

## Relationship to the Trust Model

This `/certifier/trust/` page is the broader public-facing explanation of why Certifier outcomes are reviewable.

`/certifier/trust-model/` is the more formal Certifier documentation surface describing the structured mechanics behind certification confidence and reviewability.

Both surfaces must remain bounded from Attestor's canonical Trust Statement architecture.

## Atlas Trust Context

Atlas certification may involve trust-related dimensions, signals, metadata, evidence, currency, completeness, traceability, and reproducibility.

Certifier may evaluate those characteristics as part of certification.

They remain distinct from Attestor Trust Statements.

## Relationship to the Suite Trust Standard

This page links to the Suite Trust Standard.

That standard may govern trust-related expectations relevant to certification.

Its precise relationship to Attestor's mature Trust Statement architecture should remain subject to Suite Reconciliation.

## Authority Discipline

This directory should preserve the following distinctions:

- Certification ≠ Attestation
- Certification Evaluation ≠ Attestor Evaluation
- Certification Outcome ≠ Trust Statement
- Certification Class ≠ Trust Statement
- Confidence Posture ≠ Trust Statement
- Reviewable Certification Confidence ≠ Universal Trust
- Registry Entry ≠ Certification Decision
- Integrity Reference ≠ Certification Decision
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Suite Reconciliation Considerations

This page requires explicit Suite Reconciliation because its title and historic language overlap directly with Attestor.

The following should be resolved:

1. whether **Trust** remains the preferred name for this Certifier page;
2. whether the surface should instead be framed as **Certification Confidence**, **Reviewability**, or another bounded concept;
3. how `/certifier/trust/` and `/certifier/trust-model/` should differ structurally;
4. the precise role of the Suite Trust Standard relative to Attestor;
5. how Certifier confidence posture relates to Attestor Trust Statements; and
6. how Atlas trust dimensions should be interpreted across Atlas, Certifier, and Attestor.

These are architectural questions and should not be settled through README reconciliation alone.

## Repository Expectations

Changes to this directory should preserve:

1. Certifier as certification authority;
2. the Certification Package as Certifier's canonical operational record;
3. evidence-based reviewability;
4. separation between Certifier confidence and Attestor Trust Statements;
5. current Suite object terminology;
6. governed institutional relationships;
7. historical terminology where deliberately preserved; and
8. the rule that reference does not transfer authority.

## Governing Principle

**Certifier supports confidence by making certification reviewable; Attestor owns governed Attestation, Rule-Constrained Evaluation, and Trust Statement.**
