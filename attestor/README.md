# Satoshium Attestor

**Path:** `/attestor/`  
**Institution:** Satoshium Attestor  
**Institutional Role:** Governed Attestation & Rule-Constrained Evaluation  
**Canonical Objects:** Attestation + Trust Statement  
**Evaluation Function:** Rule-Constrained Evaluation  
**Status:** Operational

---

## Overview

Satoshium Attestor is the Satoshium Suite institution for governed Attestation and Rule-Constrained Evaluation.

Attestor creates canonical **Attestations** and **Trust Statements** while preserving the authority, provenance, relevant state, scope, limitations, and meaning of the governed inputs and references used in evaluation.

Its canonical institutional flow is:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

Attestor does not determine universal truth, replace certification, redefine Registry records, rewrite Chronicle history, establish Anchor integrity, perform Beacon discovery, or assume Atlas or Navigator authority.

> **Reference does not transfer authority.**

---

## Institutional Role

Attestor's institutional role is:

**Governed Attestation & Rule-Constrained Evaluation**

This role includes:

- forming governed Attestations from eligible governed inputs;
- evaluating Attestations under applicable Attestor rules;
- producing controlled Evaluation Outcomes;
- forming bounded Attestor conclusions;
- expressing those conclusions through canonical Trust Statements;
- preserving authority boundaries, provenance, scope, limitations, conflicts, uncertainty, and relevant source state;
- validating and reviewing Attestor-owned objects;
- governing lifecycle, publication, versioning, corrections, relationships, and conformance.

Rule-Constrained Evaluation is an institutional function and process.

It is **not** a separate canonical object.

---

## Canonical Objects

Attestor has two canonical governed object families.

### Attestation

An **Attestation** is a governed, attributable assertion about a subject, record, relationship, condition, or other trust-relevant matter.

Canonical identifier family:

```text
ATT-YYYY-NNNN
```

### Trust Statement

A **Trust Statement** is a governed, attributable, bounded Attestor conclusion produced through Rule-Constrained Evaluation of an Attestation against eligible governed inputs.

Canonical identifier family:

```text
TRST-YYYY-NNNN
```

The relationship is:

```text
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

A Trust Statement is ordinarily derived from one or more governed Attestations and applicable eligible governed inputs.

---

## Canonical Responsibility

Within the Satoshium Suite:

```text
Attestor
→ Attestation
→ Rule-Constrained Evaluation
→ Trust Statement
```

This notation expresses Attestor's canonical responsibility and institutional flow.

It does **not** mean that Rule-Constrained Evaluation is a canonical object.

Attestor owns:

- Attestations;
- Trust Statements;
- Attestor Evaluation Outcomes;
- Attestor-controlled lifecycle state;
- Attestor-controlled publication state;
- Attestor provenance;
- Attestor relationships;
- Attestor Validation;
- Attestor Conformance determinations;
- Attestor Corrections and Versions.

Referenced institutions and external authorities retain authority over their own source objects.

---

## Authority Boundary

Attestor may consume or reference governed inputs from other Suite institutions and external sources.

Those references do not transfer authority.

Examples:

- Atlas retains authority over Atlas-governed intelligence.
- Navigator retains authority over Workflow Definitions and orchestration.
- Certifier retains authority over certification and Certification Packages.
- Registry retains authority over Satoshium Registry Entries.
- Chronicle retains authority over Chronicle Entries and historical-preservation records.
- Anchor retains authority over Integrity References.
- Beacon retains authority over Discovery Signals and Discovery Metadata.
- External authorities retain authority over their own source objects.

Attestor is authoritative for its own Attestations, Evaluation Outcomes, bounded conclusions, and Trust Statements.

> **Authority ≠ Eligibility ≠ Evaluation Outcome**

> **Attribution ≠ Adoption**

> **Connection ≠ Identity**

> **Reference ≠ Derivation**

> **Reference ≠ Support**

> **Reference ≠ Authority Transfer**

---

## Eligibility

Eligibility determines whether a potential input may participate in a particular Attestor evaluation.

Eligibility does not determine:

- whether the input supports the Attestation;
- whether the input is sufficient;
- whether the evaluation outcome will be favorable;
- whether the resulting Trust Statement will be Active or Published.

> **Eligibility ≠ Evaluation Outcome**

---

## Rule-Constrained Evaluation

Rule-Constrained Evaluation is the governed Attestor process through which an Attestation is evaluated against eligible governed inputs and applicable rules.

Controlled Evaluation Outcomes are:

- `supported`
- `partially-supported`
- `not-supported`
- `contradicted`
- `indeterminate`

An Evaluation Outcome is not itself a Trust Statement.

It contributes to the bounded conclusion represented by the Trust Statement.

> **Outcome ≠ Conclusion ≠ Trust Statement Identity**

---

## Attestation Types

Adopted Attestation Type families are:

- `identity`
- `evidence`
- `source-provenance`
- `verification-related`
- `relationship-condition`
- `correction-supersession`

These classifications remain distinct from canonical object types owned by other Suite institutions.

---

## Lifecycle

Adopted Attestor lifecycle states are:

- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

Review and correction are activities, not lifecycle states.

---

## Publication

Adopted Attestor publication states are:

- `unpublished`
- `published`

Canonical creation, lifecycle activation, and publication are distinct.

> **Canonical Creation ≠ Lifecycle Activation ≠ Publication**

A technically accessible object is not necessarily a Published object.

---

## Validation

Validation determines whether an Attestor-governed object satisfies applicable structural and normative requirements.

Validation is distinct from substantive evaluation.

```text
Attestor Object
        ↓
Applicable Validation Rules
        ↓
Validation Result
```

> **Validation ≠ Evaluation**

> **Valid ≠ Published**

Validation does not establish universal truth, support, certification, or source authority.

---

## Conformance

Conformance determines whether an Object, Implementation, or Process satisfies declared Attestor requirements using applicable validation and evidence.

Adopted conformance dispositions are:

- `satisfied`
- `not-satisfied`
- `not-applicable`
- `not-demonstrated`

Adopted conformance outcomes are:

- `conformant`
- `nonconformant`
- `undetermined`
- `error`

> **Validation ≠ Conformance**

> **NOT-TESTED NEVER EQUALS PASS**

---

## Provenance

Attestor preserves how governed information entered and moved through the Attestor process.

Adopted provenance modes are:

- `direct`
- `referenced`
- `derived`

Attestor provenance should preserve, as applicable:

- source identity;
- authority context;
- relevant source state;
- derivation basis;
- supporting Attestations;
- eligible governed inputs;
- applicable rules;
- evaluation basis;
- limitations;
- conflicts;
- exclusions;
- uncertainty.

---

## Relationships

Adopted Attestor relationship vocabulary is:

- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

Relationships connect governed objects without merging their identity or authority.

---

## Versioning and Material Change

Attestor distinguishes correction, versioning, supersession, and new canonical identity.

A bounded correction may preserve canonical identity when the essential institutional meaning of the object remains intact.

A materially changed Trust Statement conclusion requires a new canonical Trust Statement and new `TRST-YYYY-NNNN` identifier.

> **A changed conclusion is a changed canonical statement.**

Prior governed states remain preserved rather than silently overwritten.

---

## Trust Statement Boundaries

A Trust Statement is not:

- a declaration of universal truth;
- a generic reputation record;
- a trust score;
- a confidence percentage;
- a certification;
- a verification result;
- a Registry record;
- a Chronicle Entry;
- an Anchor Integrity Reference;
- a Beacon Discovery Signal;
- an automatic restatement of source authority;
- a guarantee of permanent correctness.

A Trust Statement is authoritative only as an Attestor conclusion within its defined scope.

---

## Relationship to the Satoshium Suite

The reconciled Suite responsibility model is:

```text
Atlas     → Authoritative Intelligence
Navigator → Workflow Definition / Orchestration
Certifier → Operational Certification
Registry  → Canonical Registration / Public Catalog
Chronicle → Historical Preservation
Anchor    → Integrity Preservation
Beacon    → Discovery & Signals
Attestor  → Governed Attestation & Rule-Constrained Evaluation
```

Canonical institutional objects remain distinct:

```text
Atlas     → Atlas-governed authoritative intelligence records
Navigator → Workflow Definitions
Certifier → Certification Package
Registry  → Satoshium Registry Entry (SREG)
Chronicle → Chronicle Entry
Anchor    → Integrity Reference
Beacon    → Discovery Signal
Attestor  → Attestation + Trust Statement
```

Interoperability connects these responsibilities without transferring institutional authority.

---

## Production Operation

Attestor completed its first controlled production operation in September 2026.

The operation produced:

### ATT-2026-0001

**Canonical Production Attestation**  
**State:** Active · Published · V1.0

### TRST-2026-0001

**Canonical Production Trust Statement**  
**State:** Active · Published · V1.0  
**Evaluation Outcome:** `supported`

Canonical production relationship:

```text
Eligible Governed Suite-Source Inputs
        ↓
ATT-2026-0001
        ↓
Rule-Constrained Evaluation
        ↓
supported
        ↓
TRST-2026-0001
```

`TRST-2026-0001` is `derived-from` `ATT-2026-0001`.

This production lineage demonstrates one exercised governed path.

It is not a mandatory universal Suite pipeline.

---

## Operational Status

**Institutional Status:** Operational

Operational evidence includes:

- Production Readiness Gate → PASS
- First Production Operation → COMPLETE
- executable Validation → exercised
- governed Review → exercised
- Conformance → exercised
- lifecycle activation → exercised
- Publication → exercised
- final-state revalidation → exercised
- Post-Operation Institutional Review → PASS
- Operational Proof → ESTABLISHED
- `ATT-2026-0001` → Active · Published · V1.0
- `TRST-2026-0001` → Active · Published · V1.0

Operational status does not make future Attestations or Trust Statements automatically valid, conformant, active, published, supported, or correct.

Each future object remains independently subject to applicable Attestor governance.

---

## Core Documentation

Primary Attestor documentation includes:

- `/attestor/purpose/`
- `/attestor/principles/`
- `/attestor/scope/`
- `/attestor/definitions/`
- `/attestor/rules/`
- `/attestor/attestations/`
- `/attestor/attestation-types/`
- `/attestor/attestation-generation/`
- `/attestor/trust-statements/`
- `/attestor/entry-model/`
- `/attestor/eligibility/`
- `/attestor/evaluation/`
- `/attestor/authority/`
- `/attestor/provenance/`
- `/attestor/relationships/`
- `/attestor/lifecycle/`
- `/attestor/versioning/`
- `/attestor/validation/`
- `/attestor/conformance/`
- `/attestor/publication/`
- `/attestor/methodology/`
- `/attestor/production/`
- `/attestor/integration/`
- `/attestor/interoperability/`
- `/attestor/status/`

Subdirectory README files document their own bounded surfaces and should not be treated as substitutes for this root institutional README.

---

## Repository Maintenance

Attestor documentation should:

- preserve the distinction between institutional role, process, and canonical objects;
- preserve Attestation and Trust Statement as separate canonical object families;
- preserve Rule-Constrained Evaluation as a governed function rather than an object;
- maintain explicit source-authority boundaries;
- distinguish Authority, Eligibility, Evaluation Outcome, Validation, Conformance, Lifecycle, and Publication;
- preserve provenance and relationship semantics;
- avoid collapsing Trust Statements into generalized truth, reputation, scoring, or certification;
- preserve historical production evidence without converting the first exercised lineage into a mandatory universal pipeline;
- keep subdirectory documentation scoped to its own institutional surface;
- correct stale current-state language without rewriting accurate historical records.

README reconciliation documents the architecture that exists. It does not redesign the architecture.

---

## Governing Principle

> **Reference does not transfer authority.**

Attestor governs its own Attestations, Rule-Constrained Evaluations, bounded conclusions, and Trust Statements while preserving the authority of every governed source it references.
