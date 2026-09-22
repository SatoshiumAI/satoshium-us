# Satoshium Certifier — Attestations

**Path:** `/certifier/attestations/`  
**Institution:** Satoshium Certifier  
**Surface:** Certifier · Attestations  
**Status:** Current repository documentation

## Purpose

This directory documents the relationship between **Satoshium Certifier** certification outputs and the broader **Satoshium Attestor** architecture.

The public page for this directory is:

- `index.html`

This surface does not define Attestor's canonical objects or rules. It explains how completed Certifier outputs may become eligible governed inputs to Attestor while preserving institutional authority.

## Certifier Boundary

Certifier performs certification.

Its canonical operational output is the **Certification Package**.

The established Suite rule is:

> **Standards define expectations. Methodology defines implementation. Certifier performs certification.**

Certifier does not own Attestations or Trust Statements.

## Attestor Boundary

Attestor operates through the canonical flow:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

An **Attestation** is a governed, attributable assertion.

A **Trust Statement** is a governed, attributable, bounded Attestor conclusion.

Attestor does not reopen or replace a Certifier certification decision.

## Relationship Between Certification and Attestation

A Certification Package or related governed certification artifact may be used as an eligible governed Attestor input where Attestor rules permit.

That relationship does not make the Attestation part of the Certification Package.

Likewise, an Attestor Trust Statement does not become a certification outcome.

The correct boundary is:

```text
Certification Package
        ↓ referenced / eligible governed input where permitted
Attestor
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

## First Production Attestor Operation

The first production Attestor operation produced:

- `ATT-2026-0001`
- `TRST-2026-0001`

Both are Active · Published · V1.0.

`ATT-2026-0001` references:

- `SC-CERT-2026-0001`
- `SREG-2026-0001`
- `CHR-2026-0001`
- `ANCH-2026-0001`
- `BEAC-2026-0001`

`TRST-2026-0001` is derived from `ATT-2026-0001` and references the same governed Suite records.

These relationships preserve provenance while leaving each institution authoritative for its own canonical object.

## Cross-Institution Relationships

### Certifier

Certifier owns the certification operation and Certification Package.

### Registry

Registry owns the Satoshium Registry Record / SREG.

A Registry reference does not make Registry authoritative for the Certification Package.

### Chronicle

Chronicle owns Chronicle Entries and preserves governed chronology.

### Anchor

Anchor owns Integrity References and preserves integrity context.

### Beacon

Beacon owns Discovery Signals / Discovery Metadata.

### Attestor

Attestor owns:

- Attestations;
- rule-constrained evaluation; and
- Trust Statements.

### Navigator

Navigator defines and orchestrates workflows.

## Authority Discipline

This surface must preserve the following distinctions:

- Certification Package ≠ Attestation
- Certification Decision ≠ Trust Statement
- Attestation ≠ Trust Statement
- Validation ≠ Evaluation
- Eligibility ≠ Evaluation Outcome
- Evaluation Outcome ≠ Trust Statement
- Reference ≠ Derivation
- Reference ≠ Support
- Connection ≠ Identity
- Valid ≠ True
- Valid ≠ Supported
- Conformant ≠ Published

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Historical / Legacy Terminology

Earlier Certifier documentation used an older **SATR / Attestation Record** model and described Attestor primarily as verifying selected certification claims and record relationships.

That language has been superseded by the mature Attestor architecture.

Current documentation should use:

- Attestation;
- rule-constrained evaluation; and
- Trust Statement

as the Attestor model.

Historical artifacts should remain historically accurate if preserved, but current-state surfaces should not present the legacy model as governing architecture.

## Repository Expectations

Changes to this directory should preserve:

1. Certifier authority over certification;
2. Attestor authority over Attestations and Trust Statements;
3. the canonical Attestor flow;
4. separation between certification outcomes and Attestor conclusions;
5. source provenance;
6. institutional ownership;
7. current production status; and
8. the rule that reference does not transfer authority.

Changes that would redefine Attestor object identity, Certifier authority, or cross-institution ownership require governed Suite Reconciliation rather than a documentation-only edit.

## Governing Principle

**Certification establishes the certification result. Attestor may later make governed assertions and bounded trust conclusions about eligible governed inputs without replacing the original certification authority.**
