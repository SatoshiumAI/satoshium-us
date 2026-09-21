# Satoshium Attestor — Corrections

## Page

`/attestor/corrections/`

## Purpose

This page establishes the foundational role of **Corrections** within Satoshium Attestor.

Corrections provide governed mechanisms for addressing errors, clarifications, withdrawals, supersession, and other changes affecting Attestor's own Attestations and Trust Statements.

The correction architecture must preserve both the currently effective state and sufficient provenance to understand what previously existed and why it changed.

## Authority Boundary

> **Attestor corrects Attestor-owned objects.**

Attestor does not correct or rewrite authoritative objects owned by other Suite institutions.

The Suite-wide principle applies:

> **Reference does not transfer authority.**

If a referenced source changes, Attestor may need to reconsider or update its own Attestation or Trust Statement. The originating institution remains responsible for the source object's correction and lifecycle.

## Established Correction Capabilities

Attestor now governs:

- correction;
- clarification;
- withdrawal;
- supersession;
- provenance of change; and
- historical traceability.

Correction and clarification are governed change activities. `withdrawn` and `superseded` are established Lifecycle states. Their use remains subject to Lifecycle, Versioning, Relationships, Provenance, Validation, and Publication.

## No Separate Correction Record

Attestor does not establish a separate **Correction Record** as another canonical Attestor object class.

Attestor's canonical responsibility remains:

**Attestor → Trust Statement**

Correction is represented through the applicable governed combination of:

- Lifecycle;
- Versioning;
- Relationships;
- Provenance;
- Validation;
- Publication;
- replacement Attestations where material assertion change requires one; and
- replacement Trust Statements where material conclusion change requires one.

The first production correction was completed without creating a separate canonical Correction Record.

## Correction Attestations

A dedicated **Correction Attestation** mechanism is not adopted by this page and was not required by the first production operation.

Correction remains a governed activity. If a future correction itself requires a new Attestation, that determination must arise from the applicable Attestation Type, materiality, Lifecycle, Versioning, and Methodology rules rather than from an automatic assumption that every correction creates a Correction Attestation.

## Current State vs Historical State

A correction system should distinguish:

- the currently effective Attestor state; and
- historically relevant prior states.

A prior Attestation or Trust Statement may remain traceable without remaining current or effective.

Conceptually:

`Prior State → Governed Change → Current State`

Provenance and relationships should remain visible across the transition.

## Provenance of Change

Correction governance preserves enough information to determine, as applicable:

- what changed;
- why it changed;
- who or what authorized the change;
- when the change occurred;
- which Attestor object or version was affected;
- what object or state replaced it;
- the relationship between prior and current states.

Canonical production artifacts have now demonstrated preservation of correction reason, affected objects, historical representations, and the separate versioning determination. Applicable exact fields remain governed by the relevant Schemas and records.

## Changes in Referenced Sources

If a referenced authoritative source changes, Attestor should not rewrite that source.

Depending on Attestor rules and the significance of the change, Attestor may instead:

- leave the existing Attestation or Trust Statement unchanged if the change is immaterial;
- clarify its own object;
- correct its own object;
- withdraw its own object;
- supersede its own object with a new evaluation.

The applicable decision is governed by materiality, Lifecycle, Versioning, Eligibility/Evaluation where relevant, and Publication. A source change triggers governed review; it does not predetermine the Attestor response.

## Historical Traceability

The June-era principle that corrections should improve understanding without erasing history is preserved, but expressed more precisely.

Historical traceability should coexist with a clear current state. Preserving a superseded or withdrawn object does not mean presenting it as currently effective.

Retention, public visibility, and publication behavior are governed through the established Lifecycle, Versioning, and Publication architecture.

## First Production Correction Demonstration

The first controlled production operation identified a relationship-serialization defect in the early representations of:

- `ATT-2026-0001`; and
- `TRST-2026-0001`.

The early representations used descriptive relationship strings. The governed correction replaced those with structured relationship blocks containing explicit relationship types and target identifiers.

The correction preserved:

- canonical ATT identity;
- canonical TRST identity;
- the Attestation assertion;
- the Trust Statement conclusion;
- scope;
- provenance;
- limitations;
- production history; and
- historical representations.

The governed materiality determination concluded that the correction was serialization-only and did not materially alter canonical institutional meaning.

Accordingly:

- `ATT-2026-0001` remained `V1.0`;
- `TRST-2026-0001` remained `V1.0`;
- no new ATT was required;
- no new TRST was required; and
- no separate canonical Correction Record was created.

**Correction architecture → DEMONSTRATED IN PRODUCTION**

## Correction and Versioning

The production operation demonstrated that correction reason and versioning consequence are separate governed decisions.

`Correction Reason → Why change is required`

`Versioning Decision → How canonical identity and version behave`

For the first production operation:

`Relationship serialization defect → Corrected within V1.0`

This does not establish a universal rule that every correction remains within the same version.

Standing boundaries remain:

`Material Attestation Assertion Change → New ATT`

`Material Trust Statement Conclusion Change → New TRST`

`Correction ≠ Versioning Decision`

## Historical Integrity

The earlier relationship representations were preserved rather than silently overwritten.

The production correction therefore demonstrated:

`Correction ≠ Deletion`

`Correction ≠ Historical Erasure`

`Correction ≠ Silent Overwrite`

`Correction ≠ Automatic New Canonical Object`

Historical preservation does not make an earlier representation current. It preserves the institutional record of what existed and how it changed.

## Status

**Corrections → Established and Production-Proven**

- correction as governed activity → established and exercised
- clarification → established governed change
- separate Correction Record → not adopted
- dedicated Correction Attestation mechanism → not required by first production operation
- provenance of change → exercised
- historical traceability → exercised
- no silent overwrite → demonstrated
- Correction / Versioning distinction → demonstrated
- bounded serialization correction → exercised
- canonical identity preservation → demonstrated
- `V1.0` retention → governed and demonstrated for the bounded production correction
- withdrawal / supersession correction paths → established but not exercised in first production
- production proof → **ESTABLISHED**

## Continuing Correction Governance

Production proof does not make every future correction non-material.

Each correction must independently determine:

- Attestor authority to correct the affected object;
- correction reason;
- materiality;
- canonical identity consequences;
- version consequences;
- lifecycle effects;
- relationship effects;
- provenance requirements;
- publication consequences;
- historical preservation requirements; and
- whether a new canonical object is required.

Attestor continues to correct only Attestor-owned objects.

**Reference does not transfer authority.**

## Files

- `index.html` — public Corrections page.
- `README.md` — repository documentation for the Corrections page.
