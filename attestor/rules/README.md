# Satoshium Attestor — Rules

**Path:** `/attestor/rules/`  
**Institution:** Satoshium Attestor  
**Status:** Established and Production-Proven  
**Canonical Objects:** Attestation (`ATT`) and Trust Statement (`TRST`)

## Purpose

This directory documents the foundational institutional rules that constrain how Attestor forms and governs Attestations, assesses eligible inputs, performs Rule-Constrained Evaluation, and issues bounded Trust Statements.

The canonical public explanation is `index.html`. This README documents **the Rules surface**, not the separate legacy `/attestor/trust-signals/` terminology.

> **Reference does not transfer authority.**

## Twelve Foundational Rules

The public Rules page establishes:

1. **Preserve Attribution** — identify the accountable origin of assertions, sources, Attestor objects, and actions.
2. **Preserve Provenance** — retain origin, relationships, status, and relevant input and object history.
3. **Preserve Scope** — keep assertions, evidence relationships, evaluations, and conclusions bounded.
4. **Preserve Authority Boundaries** — referencing other institutions' objects never transfers their authority.
5. **Preserve Evidence Context** — retain material source status, limitations, and conflicting information.
6. **Preserve Traceability** — make inputs, evaluations, records, corrections, and conclusions reviewable.
7. **Preserve Governed Change** — corrections, withdrawals, and supersession must not silently erase history.
8. **Distinguish Current and Historical State** — preserve lineage without confusing past states with current state.
9. **Do Not Claim Universal Truth** — Trust Statements make bounded conclusions, not universal truth determinations.
10. **Do Not Convert Inputs into Conclusions** — no single input automatically determines a Trust Statement; Attestor performs its own governed evaluation.
11. **Preserve Uncertainty** — incomplete, conflicting, or insufficient evidence must not produce exaggerated conclusions.
12. **Support Interoperability Without Authority Transfer** — cross-Suite references preserve each institution's independent canonical ownership and meaning.

These rules operate together; they are not a mandatory cross-institutional pipeline.

## Rule Application and Institutional Boundaries

```text
Eligible Governed Inputs
        ↓
Attestation (ATT)
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement (TRST)
```

**Attestation formation ≠ Eligibility ≠ Evaluation ≠ Validation ≠ Conformance ≠ Lifecycle Activation ≠ Publication.**

The institutional rules inform normative requirements, schemas/profiles, Validation, governed Review, and Conformance, but not every rule is reducible to the same machine check.

```text
Principle → Rule → Normative Requirement
                        ↓
             Validation / Governed Review
                        ↓
                   Conformance
```

An executable validation outcome does not substitute for a substantive Evaluation Outcome or a governing publication action.

**NOT-TESTED ≠ PASS. Valid ≠ Published. Conformant ≠ Published. Reference ≠ Support.**

## First Production Demonstration

The first controlled Attestor production operation exercised this framework with:

- `ATT-2026-0001` — canonical Attestation;
- a bounded Rule-Constrained Evaluation with outcome `supported`;
- `TRST-2026-0001` — canonical Trust Statement;
- governed Validation, Review, Conformance, lifecycle, and publication steps, separately evidenced.

The public Rules page reports **25/25 governed Review requirements satisfied**, **ATT and TRST conformant**, and a **post-operation institutional review of 11 PASS / 0 FAIL / 0 UNRESOLVED**.

This is proof of the assessed first operation, not advance approval of future objects, evaluation outcomes, processes, or publication.

## Relationship to Other Attestor Surfaces

- `../eligibility/` — evaluation-specific admission of governed inputs;
- `../attestation-generation/` — formation and canonical creation of an Attestation;
- `../evaluation/` — Rule-Constrained Evaluation and bounded outcome;
- `../validation/` — normative object validation;
- `../conformance/` — declared scope of conformance determinations;
- `../production/` — first production record and operational proof;
- `../trust-signals/` — **legacy/descriptive terminology only**, not a canonical Trust Signal object or a Beacon Discovery Signal.

## Governing Position

Attestor's two canonical objects remain **Attestation** and **Trust Statement**. The rules constrain their formation, evaluation, validation, change, and publication without creating a reputation model, generic trust score, additional canonical Trust Signal, or authority over other Suite institutions.
