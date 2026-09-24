# Satoshium Navigator — Integration

**Path:** `/navigator/integration/`  
**Institution:** Satoshium Navigator  
**Surface:** Cross-Institution Workflow Integration  
**Status:** Current repository documentation

## Purpose

This directory documents **Satoshium Navigator Integration**.

Navigator Integration defines how Navigator coordinates operational workflows across the Satoshium Suite while preserving the independent authority and canonical responsibilities of participating institutions.

Navigator exists to connect institutional work without absorbing institutional authority.

## Institutional Role

Navigator serves as the Suite's workflow-definition and orchestration institution.

Navigator may:

- identify operational work;
- initiate governed workflows;
- coordinate multi-step processes;
- sequence institution-specific actions;
- monitor workflow progress;
- carry references between participating systems;
- expose workflow state;
- support future automation and external integrations.

Navigator does not become the authority for the records or decisions involved.

## Core Boundary

The public Integration page establishes the central rule clearly:

```text
Navigator does not certify.
Navigator does not catalog.
Navigator does not preserve history.
Navigator does not anchor integrity.
Navigator does not publish discovery.
Navigator does not produce Trust Statements.

Navigator orchestrates workflows that connect those capabilities.
```

The durable architectural principle is:

**Orchestration over duplication.  
Coordination over centralization.  
References over ownership.  
Workflow over authority.**

## Relationship Within the Suite

The current Suite relationship model is:

```text
Atlas        → provides authoritative intelligence
Certifier    → performs certification
Registry     → catalogs governed records
Chronicle    → preserves qualifying historical Occurrences
Anchor       → preserves integrity
Beacon       → governs discovery outputs
Attestor     → governs Attestations, Rule-Constrained Evaluation, and Trust Statements
Navigator    → orchestrates workflows
```

Each institution retains authority over its own canonical objects and institutional acts.

Navigator coordinates interactions among them.

## Atlas Integration

Navigator may identify Atlas records that require:

- certification;
- recertification;
- review;
- additional evidence;
- workflow attention.

Atlas remains authoritative for its jurisdiction intelligence and Atlas-owned records.

Navigator does not reinterpret Atlas intelligence simply by using it as workflow input.

## Certifier Integration

Navigator may initiate or coordinate certification workflows.

Certifier remains authoritative for:

- Certification Packages;
- certification determinations;
- certification lifecycle;
- certification status;
- Certifier validation and review structures.

Workflow initiation does not equal certification approval.

## Registry Integration

Navigator may identify Registry Entries requiring:

- registration activity;
- lifecycle review;
- synchronization;
- workflow attention.

Registry owns its canonical Registry Entries and Registry-controlled metadata.

Navigator does not alter Registry authority by orchestrating Registry-related work.

## Chronicle Integration

Navigator may retrieve Chronicle Entries and historical context relevant to an operational workflow.

Chronicle owns the historical-preservation representation of qualifying Occurrences.

Navigator does not decide that an Occurrence qualifies for Chronicle preservation merely because a workflow references it.

## Anchor Integration

Navigator may include integrity-verification or preservation steps inside a workflow.

Anchor retains authority over:

- Integrity References;
- canonicalization and hashing context;
- verification outcomes;
- integrity-preservation procedures;
- Anchor lifecycle and publication state.

Navigator coordinates the step.

Anchor performs the institutional act.

## Beacon Integration

Navigator may request or consume discovery-related information during workflows.

Beacon retains authority over:

- Discovery Signals;
- Discovery Metadata;
- Beacon provenance;
- Beacon lifecycle;
- Beacon publication decisions.

Navigator may coordinate workflows that result in Beacon action without owning the resulting Beacon object.

## Attestor Integration

Navigator may initiate or coordinate trust-related workflows that enter Attestor's governed process.

Attestor retains authority over:

- Attestations;
- Eligibility;
- Rule-Constrained Evaluation;
- Evaluation Outcomes;
- Trust Statements.

A Navigator workflow may lead to an Attestor result.

The result remains Attestor-owned.

## Reference-Based Architecture

Navigator Integration is reference-based.

Navigator may carry identifiers, references, workflow state, or coordination context across institutions.

It should not duplicate another institution's canonical record merely to coordinate workflow execution.

The governing rule is:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

A companion Navigator rule is:

**COORDINATION DOES NOT TRANSFER AUTHORITY.**

## Workflow Orchestration

A generalized Suite workflow may look like:

```text
Atlas intelligence
        ↓
Navigator identifies work
        ↓
Certifier performs certification
        ↓
Registry performs registration/cataloging
        ↓
Chronicle preserves qualifying historical Occurrence
        ↓
Anchor preserves integrity where applicable
        ↓
Beacon publishes or updates discovery outputs where appropriate
        ↓
Attestor performs governed Attestation / Evaluation / Trust Statement work where eligible
```

This is an orchestration model.

It should not be interpreted as:

- a mandatory linear pipeline for every object;
- proof that every downstream institution must act;
- transfer of authority to Navigator;
- automatic creation of downstream canonical objects.

Each institution performs its own governed responsibility when applicable.

## Future Integration

Navigator may eventually coordinate:

- additional Suite institutions;
- external references;
- APIs;
- datasets;
- operational services;
- event-driven systems;
- machine-triggered workflows;
- third-party intelligence sources.

Future integration must preserve the same authority rules as current Suite integration.

External participation does not imply that Navigator owns external records or that external authority transfers into the Suite.

## Workflow Philosophy

Navigator exists because operational processes naturally span multiple institutions.

Rather than embedding cross-system workflow logic inside Certifier, Registry, Chronicle, Anchor, Beacon, or Attestor, Navigator provides a dedicated orchestration layer.

This preserves institutional independence while making coordinated operations repeatable.

## Authority Discipline

Navigator Integration should preserve the following distinctions:

- orchestration ≠ certification;
- orchestration ≠ registration;
- orchestration ≠ historical preservation;
- orchestration ≠ integrity preservation;
- orchestration ≠ discovery authority;
- orchestration ≠ Attestor evaluation;
- workflow state ≠ canonical object state;
- workflow request ≠ institutional approval;
- workflow completion ≠ authority transfer;
- reference ≠ derivation;
- reference ≠ support;
- connection ≠ identity.

## Suite Reconciliation Flag

The architecture is fundamentally strong.

Suite Reconciliation should review only a limited set of terminology details:

1. **“Beacon publishes discovery”**  
   This is directionally correct but may be better expressed using Beacon's mature object language: Discovery Signals, Discovery Metadata, lifecycle, and publication.

2. **“Attestor produces trust statements”**  
   Current terminology should consistently preserve the complete Attestor flow:
   `Eligible Governed Inputs → Attestation → Rule-Constrained Evaluation → Trust Statement`.

3. **Workflow linearity**  
   The representative flow should remain clearly illustrative rather than interpreted as a mandatory universal sequence for every Suite matter.

4. **Registry wording**  
   “Registry catalogs records” is useful shorthand, but Suite Reconciliation may confirm whether “Registry Entry” / SREG terminology should be preferred in all integration documentation.

These are terminology and explanatory refinements, not architectural defects.

## Repository Expectations

Changes to this directory should preserve:

1. Navigator as the Suite orchestration institution;
2. institutional independence of every participating system;
3. reference-based integration;
4. separation between workflow state and canonical institutional state;
5. the non-mandatory nature of representative workflow sequences;
6. mature Beacon and Attestor terminology;
7. support for future internal and external integrations without authority transfer; and
8. the principle that coordination does not transfer authority.

## Governing Principle

**Independent systems. Coordinated workflows.**
