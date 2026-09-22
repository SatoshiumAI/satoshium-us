# Satoshium Certifier — Frequently Asked Questions

**Path:** `/certifier/faq/`  
**Institution:** Satoshium Certifier  
**Canonical Page:** `index.html`  
**Status:** Operationally Reconciled  
**Updated:** September 2026

---

## Purpose

This FAQ provides public guidance on Satoshium Certifier, its certification architecture, evidence model, Certification Packages, generated artifacts, authority boundaries, and production-proven Suite interoperability.

Certifier is **Operational**. Its inaugural production Certification Package is `SC-CERT-2026-0001`.

---

## What is Satoshium Certifier?

Satoshium Certifier is the operational certification implementation of the Satoshium Suite. It reviews defined Certification Subjects against applicable Suite Standards and Suite Methodology, evaluates supporting Evidence, reaches certification determinations, and preserves the result through a canonical Certification Package.

Certifier is authoritative for its own certification actions, Certification Packages, Certification Classes, lifecycle, and generated certification artifacts.

---

## What does Certifier certify?

Certifier supports defined digital Certification Subjects such as pages, reports, services, workflows, datasets, and tools. Additional subject categories may be introduced through documented Certifier and Suite governance.

---

## What is a Certification Subject?

A Certification Subject is the defined item, system, record, workflow, service, dataset, tool, or other governed subject being reviewed.

The Certification Subject establishes what is inside the certification boundary.

---

## What is certification?

Certification is the process of reviewing a defined Certification Subject against applicable standards and methodology, evaluating supporting evidence, and recording a governed determination.

Certification creates a transparent and reviewable record of that process.

---

## What is a Certification Package?

The Certification Package is Certifier's canonical operational record for a certification.

It preserves the Certification Subject, certification boundary, governing Standards, applied Methodology, Evidence Inventory, evaluation, determination, Certification Class, lifecycle information, and generated artifact relationships.

Reports, receipts, certified records, and downstream Suite references derive from the Certification Package.

> **Reference does not transfer authority.**

---

## Does certification guarantee correctness?

No.

Certification documents a review performed according to defined standards, methodology, scope, and available evidence at a specific point in time.

It does not guarantee absolute accuracy, completeness, future performance, regulatory compliance, legal validity, or universal truth.

---

## What standards are used?

Certifier applies documented Suite Standards and certification requirements. Standards define scope, requirements, evaluation criteria, evidence requirements, and determination guidance.

Certification activity should remain traceable to its governing standards.

---

## What evidence can be used?

Evidence may include canonical records, reports, structured data, durable references, captures, hashes and integrity metadata, notes and review observations, and supporting institutional artifacts.

Evidence requirements depend on the applicable Standards, Methodology, Certification Subject, and certification boundary.

---

## What are Certification Classes?

Version 1.0 defines three Certification Classes:

- **Informational** — the subject exists and has been documented.
- **Operational** — the subject exists, is documented, and demonstrates operation.
- **Verified** — the subject has been reviewed against an established standard and is supported by documented evidence.

The inaugural production certification is **Operational**.

---

## What are Certification Outcome, Certification Status, and Lifecycle State?

These are distinct concepts.

**Certification Outcome** records the determination reached by Certifier for the defined review.

**Certification Status** communicates the current certification-domain condition of an issued certification, such as `Issued · Active`.

**Lifecycle State** describes where the certification record exists in its broader institutional lifecycle.

They should not be collapsed into one generic status field.

---

## What are SCPR, SCR, and SCRD?

Certifier generates several artifact forms from the canonical Certification Package:

```text
SCPR — Certification Process Report
SCR  — Certification Receipt
SCRD — Satoshium Certified Record
```

The SCPR preserves the detailed review process and reasoning. The SCR provides a concise public-facing certification receipt. The SCRD provides a certified-record representation in human-readable and, where published, machine-readable form.

These artifacts remain traceable to and materially consistent with the canonical Certification Package.

---

## Why are hashes used?

Hashes support integrity verification by helping determine whether a defined representation matches the representation whose digest was recorded.

Hashes do not prove correctness or truth.

---

## Does Certifier require human review?

Not necessarily. The architecture can support human, AI-assisted, human-AI-assisted, or automated review where permitted by the applicable governing requirements.

Automation does not eliminate the need for attributable, transparent, and reviewable institutional decisions.

---

## What is Registry?

Satoshium Registry is the Suite institution responsible for canonical registration and durable Registry records.

The inaugural production relationship is:

```text
SC-CERT-2026-0001
        ↓
SREG-2026-0001
```

Registry owns `SREG-2026-0001`. Certifier retains certification authority.

---

## What is Chronicle?

Satoshium Chronicle preserves qualifying historical Occurrences through canonical Chronicle Entries.

The inaugural production relationship includes `CHR-2026-0001`, which preserves the qualifying certification Occurrence while Certifier remains authoritative for the certification decision.

---

## What is Anchor?

Satoshium Anchor is the Operational Suite institution responsible for governed Integrity References and verification of defined representations.

`ANCH-2026-0001` preserves integrity context for the complete canonical SCRD JSON representation `SCRD-SC-CERT-2026-0001`.

That integrity boundary does not extend to the entire Certification Package or linked artifacts unless separately anchored.

---

## What is Beacon?

Satoshium Beacon is the Operational Suite institution responsible for governed Discovery Signals and discovery metadata.

`BEAC-2026-0001` is Beacon's first published production Discovery Signal and directly observed `SC-CERT-2026-0001` as its primary authoritative source.

Beacon discovery does not become certification authority. Its September 13, 2026 observation does not by itself establish unchanged source state on later dates.

---

## What is Attestor?

Satoshium Attestor is the Operational Suite institution that creates governed Attestations and produces governed, attributable, bounded Trust Statements through Rule-Constrained Evaluation of eligible governed inputs.

Its first production operation created:

```text
ATT-2026-0001
        ↓
Rule-Constrained Evaluation
        ↓
supported
        ↓
TRST-2026-0001
```

Both objects are `Active · Published · V1.0`.

`TRST-2026-0001` is `derived-from` `ATT-2026-0001`.

Attestor does not independently re-certify Certifier's decision, establish the substantive truth of the underlying Atlas intelligence, extend Anchor integrity beyond its defined representation, or establish generalized trustworthiness.

---

## What is Navigator?

Satoshium Navigator is the Operational Suite institution for **Workflow Definition / Orchestration**.

Navigator can coordinate Suite workflows without changing institutional ownership or authority.

---

## How does Certifier fit into Satoshium?

At a high level, the Suite preserves distinct institutional roles:

```text
Atlas      → authoritative intelligence
Certifier  → certification
Registry   → registration and cataloging
Chronicle  → historical preservation
Anchor     → integrity references
Beacon     → discovery signals
Attestor   → governed Attestations and bounded Trust Statements
Navigator  → workflow definition and orchestration
```

The inaugural production lineage includes:

```text
SC-CERT-2026-0001
        ├── SREG-2026-0001
        ├── CHR-2026-0001
        ├── ANCH-2026-0001
        ├── BEAC-2026-0001
        ├── ATT-2026-0001
        └── TRST-2026-0001
```

These are institution-owned objects connected by governed relationships.

`TRST-2026-0001` is specifically `derived-from` `ATT-2026-0001`.

> **Connection ≠ Identity. Reference ≠ Derivation. Reference ≠ Support. Reference does not transfer authority.**

---

## Is Certifier open source?

Certifier is released under the MIT License unless otherwise specified by the governing repository or artifact.

---

## What is the long-term vision of Certifier?

The long-term objective is to preserve certification records that remain understandable, attributable, reviewable, and useful over time.

The goal is not merely to issue certifications, but to preserve the evidence, reasoning, decision, boundaries, provenance, and institutional relationships needed to understand them later.

---

## Guiding Statement

> Trust should not depend upon memory.  
> Trust should not depend upon reputation.  
> Trust should be supported by standards, evidence, and reviewable records.  
> Satoshium Certifier exists to help preserve those records.

---

**Maintained By:** Satoshium
