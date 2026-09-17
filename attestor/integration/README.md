# Satoshium Attestor — Integration

## Page

`/attestor/integration/`

## Purpose

This page defines the foundational operational integration model for **Satoshium Attestor**.

Integration concerns how Attestor receives, resolves, references, and uses governed information from the Satoshium Suite and potentially other eligible sources.

It does not transfer the authority of those sources to Attestor.

## Canonical Responsibility

**Attestor → Trust Statement**

Attestor Integration exists to make eligible governed inputs available for Attestor's own evaluation and Trust Statement production.

## Governing Principle

> **Reference does not transfer authority.**

The source institution remains authoritative for its canonical object.

Attestor remains authoritative for its own Attestations, evaluation, lifecycle operations, and Trust Statements as defined by Attestor architecture.

## Integration vs Interoperability

The two concepts are related but distinct.

### Interoperability

Interoperability defines what must remain intact when information crosses institutional boundaries.

This includes, as applicable:

- meaning;
- identifier;
- source;
- provenance;
- type;
- status;
- scope;
- relationships;
- authority;
- limitations.

### Integration

Integration defines the operational connection through which Attestor obtains and uses governed information.

Conceptually:

`Interoperability → Preserve Meaning and Authority`

`Integration → Connect and Exchange`

`Attestor Evaluation → Produce the Trust Statement`

## Conceptual Integration Flow

The foundational relationship is:

`Source Object → Resolve Reference → Preserve Context → Establish Eligibility → Attestor Evaluation → Trust Statement`

This is intentionally conceptual.

It does **not** yet establish:

- required machine steps;
- validation sequence;
- API calls;
- transport protocols;
- schemas;
- workflow identifiers;
- lifecycle transitions;
- PASS/FAIL outcomes.

## Availability Is Not Eligibility

A source object being technically available to Attestor does not make it eligible for use.

Likewise, an eligible source object does not automatically become an Attestation or determine a Trust Statement.

The foundational distinction is:

`Availability ≠ Eligibility ≠ Attestation ≠ Trust Statement`

Advanced architecture must define the rules separating these states and concepts.

## Suite Integration Relationships

### Atlas

**Atlas → Authoritative Intelligence**

Attestor may receive or resolve references to authoritative Atlas intelligence when relevant.

Atlas retains authority over that intelligence.

### Navigator

**Navigator → Workflow Definition / Orchestration**

Navigator may define or orchestrate workflows in which Attestor participates.

Navigator governs workflow definition and orchestration. Attestor governs its own evaluation and Trust Statement.

### Certifier

**Certifier → Certification Package**

Attestor may resolve and reference Certification Packages and governed certification artifacts when eligible.

Certification authority remains with Certifier.

The June page specifically named SCPRs, SCRs, and SCRDs. Those remain possible certification artifacts where current Certifier architecture recognizes them, but this page does not independently redefine their role or make them mandatory Attestor inputs.

### Registry

**Registry → Satoshium Registry Record**

Attestor may resolve and reference Registry records and their governed relationships.

Registry retains authority over its identifiers, status, and lifecycle.

### Chronicle

**Chronicle → Chronicle Entry**

Attestor may resolve and reference Chronicle Entries when historical, event, or provenance context is relevant.

Chronicle retains authority over the preserved historical entry.

### Anchor

**Anchor → Integrity Reference**

Attestor may resolve and reference Anchor Integrity References.

Anchor retains authority over its integrity model and canonical object.

### Beacon

**Beacon → Discovery Signal / Discovery Metadata**

Attestor may resolve and reference Beacon Discovery Signals or Discovery Metadata.

Beacon retains authority over its discovery objects and lifecycle.

### Attestor

**Attestor → Trust Statement**

Attestor evaluates eligible inputs under its own rules and remains responsible for the resulting Trust Statement.

## No Automatic Certification-to-Attestation Conversion

The June page framed the central integration question as:

> “how does certification become an attestation?”

That question is not carried forward literally.

A certification does not necessarily **become** an Attestation.

A Certification Package may instead be an authoritative input referenced by an Attestation or evaluated by Attestor under rules that remain to be established.

The distinction prevents transformation of a Certifier-owned canonical object into an Attestor-owned object merely through integration.

## Reference-Based Operation

Where an authoritative object already exists, Attestor should normally reference that object rather than silently duplicate it.

Attestor may preserve enough information to:

- resolve the source;
- validate eligibility;
- preserve the state considered;
- establish provenance;
- understand scope;
- evaluate relevance;
- trace relationships;
- support later review.

The authoritative source remains authoritative.

## Source Change and Integration

Integrated source objects may change after an Attestor evaluation.

Advanced integration architecture should determine how Attestor detects or receives relevant changes and what happens when a material source change affects an Attestation or Trust Statement.

Potential concerns include:

- source status change;
- source correction;
- source supersession;
- source withdrawal;
- version change;
- publication-state change;
- failed resolution;
- unavailable source;
- changed provenance.

The resulting Attestor response remains governed by Attestor's own lifecycle and correction rules.

## External Integration

External integration remains possible but unresolved.

Attestor should not accept an external input merely because it can technically connect to the source.

Advanced rules must establish:

- source eligibility;
- authority;
- provenance;
- scope;
- status;
- validation;
- persistence;
- permitted use;
- failure handling.

## Technology Neutrality

The June page anticipated:

- machine-readable attestations;
- APIs;
- digital signatures;
- policy frameworks;
- verification ecosystems.

Those technologies and frameworks are not adopted by this foundational reconciliation.

They may later be selected where demonstrated requirements justify them.

The architecture should establish institutional and semantic requirements before selecting transport or implementation mechanisms.

## Reconciliation Notes

Major changes include:

- redefining Integration as operational connection and exchange rather than generic ecosystem participation;
- distinguishing Integration from Interoperability;
- replacing “how does certification become an attestation?” with a broader governed-input model;
- establishing that Certification Packages do not automatically become Attestations;
- adding Atlas and Navigator integration relationships;
- updating all institutional relationships to current canonical responsibilities;
- replacing broad record duplication with reference-based operation;
- adding reference resolution and eligibility as separate concepts;
- establishing `Availability ≠ Eligibility ≠ Attestation ≠ Trust Statement`;
- adding a conceptual integration flow;
- preserving source authority throughout integration;
- adding source-change concerns;
- retaining external integration as possible but unresolved;
- removing premature adoption of APIs, digital signatures, policy frameworks, and external verification ecosystems.

## Deferred to Advanced Architecture

The following remain intentionally unresolved:

- reference-resolution mechanism;
- input eligibility rules;
- workflow entry points;
- integration event model;
- validation sequence;
- source-state preservation;
- change-detection mechanism;
- retry and failure behavior;
- unavailable-source handling;
- publication dependencies;
- API requirements;
- transport protocols;
- authentication;
- authorization;
- digital signatures, if required;
- external-source integration;
- machine schemas;
- integration validation rules;
- conformance tests;
- reference vectors.

## Files

- `index.html` — public Integration page.
- `README.md` — repository documentation for the Integration page.
