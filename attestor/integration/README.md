# Satoshium Attestor — Integration

## Page
`/attestor/integration/`

## Purpose
This page defines the established institutional integration model for **Satoshium Attestor**.

Integration concerns how Attestor receives, resolves, references, and uses governed information from the Satoshium Suite and eligible external sources without transferring source authority.

## Canonical Responsibility
**Attestor → Trust Statement**

## Governing Principle
> **Reference does not transfer authority.**

The source institution remains authoritative for its canonical object.

Attestor remains authoritative for its own Attestations, Rule-Constrained Evaluation, lifecycle/versioning decisions, and Trust Statements.

## Integration vs Interoperability
### Interoperability
Interoperability preserves semantic and authority context across institutional boundaries.

Applicable context includes:
- identifier;
- source;
- provenance;
- type;
- relevant state;
- scope;
- relationships;
- authority;
- limitations.

### Integration
Integration provides the operational connection and exchange through which Attestor obtains or resolves governed information.

> **Interoperability → Preserve Meaning and Authority**

> **Integration → Connect and Exchange**

## Established Integration Flow
`Source Object → Resolve Reference → Preserve Context → Establish Eligibility → Attestation → Rule-Constrained Evaluation → Trust Statement`

This is the established governed institutional sequence. The first controlled production operation exercised this path against real Suite-owned objects.

Exact APIs, transports, authentication, authorization, retry behavior, notification mechanisms, and serialization remain implementation choices unless separately adopted by a production specification.

## Core Distinctions
> **Availability ≠ Eligibility**

> **Authority ≠ Eligibility**

> **Reference ≠ Eligibility**

> **Eligibility ≠ Attestation**

> **Attestation ≠ Trust Statement**

> **Integration ≠ Authority Transfer**

## Reference Resolution
Where a canonical source object already exists, Attestor should normally resolve and reference it rather than silently duplicate it.

A governed reference preserves sufficient context to identify and interpret the source while maintaining authority boundaries.

The established Reference Profile context is:

`Identifier + Source + Provenance + Type + Status + Scope + Relationship + Authority`

Exact network-resolution mechanisms remain implementation work.

## Eligibility
Integration makes a potential input available for governed Eligibility determination.

Technical availability does not establish Eligibility.

Eligibility is evaluation-specific:

> **Eligible Here ≠ Eligible Everywhere**

## Suite Integration Relationships
- **Atlas → Authoritative Intelligence**
- **Navigator → Workflow Definition / Orchestration**
- **Certifier → Certification Package**
- **Registry → Satoshium Registry Record**
- **Chronicle → Chronicle Entry**
- **Anchor → Integrity Reference**
- **Beacon → Discovery Signal / Discovery Metadata**
- **Attestor → Trust Statement**

Attestor may reference eligible governed objects from these institutions while preserving the originating institution's authority.

## First Production Integration Baseline

The first controlled production operation demonstrated a real **Certifier → Attestor** integration case centered on `SC-CERT-2026-0001`.

The governed path was:

`SC-CERT-2026-0001`

`→ Eligibility under Attestor rules`

`→ ATT-2026-0001`

`→ Rule-Constrained Evaluation`

`→ Evaluation Outcome: supported`

`→ TRST-2026-0001`

The operation also preserved traceable governed relationships to:

- `SREG-2026-0001`
- `CHR-2026-0001`
- `ANCH-2026-0001`
- `BEAC-2026-0001`

Authority remained institution-specific:

- Certifier retained authority over `SC-CERT-2026-0001`;
- Registry retained authority over `SREG-2026-0001`;
- Chronicle retained authority over `CHR-2026-0001`;
- Anchor retained authority over `ANCH-2026-0001`;
- Beacon retained authority over `BEAC-2026-0001`; and
- Attestor governed only its own Attestation, Rule-Constrained Evaluation, and Trust Statement.

> **Reference does not transfer authority.**

The production operation therefore demonstrated integration by reference without canonical-object duplication or institutional authority transfer.

## No Automatic Conversion
A source object does not become an Attestation merely because Attestor integrates with or references it.

A Certification Package does not automatically become an Attestation.

A Registry Record, Chronicle Entry, Integrity Reference, Discovery Signal, or other governed source object does not automatically become a Trust Statement.

## Provenance and Authority
Integrated information remains subject to the established Authority and Provenance architecture.

Adopted provenance modes:
- `direct`
- `referenced`
- `derived`

Authority contexts:
- `Attestor`
- `Suite-source`
- `external-source`

> **Attribution ≠ Adoption**

## Source State and Change
Attestor preserves relevant source state at Evaluation.

> **Source State at Evaluation ≠ Later Source State**

A material source-state change may trigger review:

`Material Source-State Change → Review`

The trigger does not automatically determine:
- correction;
- withdrawal;
- supersession;
- lifecycle transition;
- a new Attestation;
- a new Trust Statement.

Those outcomes remain governed by the applicable Attestor architecture.

## External Integration
External governed sources may participate when Attestor can establish applicable:
- source identity;
- authority;
- provenance;
- scope;
- relevant state;
- permitted use;
- Eligibility.

External availability alone is insufficient.

External reference does not transfer external authority to Attestor.

## Validation
Integrated references and resulting Attestor objects remain subject to applicable Validation requirements.

> **Validation ≠ Eligibility**

> **Validation ≠ Evaluation**

> **Validation ≠ Conformance**

Executable Validation is established and was exercised in the first production operation through Validator v0.5. Integrated references and resulting Attestor objects remain independently subject to applicable Validation requirements.

## Publication
Integration does not itself authorize publication.

> **Canonical Creation ≠ Lifecycle Activation ≠ Publication**

A source being publicly accessible also does not make an Attestor object Published.

## Technology Neutrality
The institutional integration architecture does not require a specific:
- API;
- transport protocol;
- authentication mechanism;
- authorization mechanism;
- digital-signature system;
- external verification ecosystem.

Such mechanisms may be adopted where production requirements justify them.

## Technology-Specific Implementation Matters
The institutional Integration architecture is established and has been exercised in production. The following remain legitimate technology-specific or future-profile implementation concerns rather than unresolved institutional architecture:
- concrete reference-resolution mechanism;
- workflow entry points;
- integration event transport;
- change-notification mechanism;
- retry and failure behavior;
- unavailable-source handling;
- API/interface requirements;
- authentication and authorization;
- digital signatures if required;
- machine serialization;
- executable integration validation;
- conformance test implementation;
- reference vectors.

## Status

**Integration Architecture → Established**

**Production Integration → Operationally Demonstrated**

- governed integration flow → established
- Reference Profile context → established
- Eligibility boundary → established
- Authority / Provenance preservation → established
- source-state handling → established
- no automatic source-object conversion → established
- Validation dependency → established and exercised
- Publication separation → established and exercised
- Certifier → Attestor production integration → **demonstrated**
- `SC-CERT-2026-0001` source authority → **preserved**
- `ATT-2026-0001` → **Active · Published · V1.0**
- `TRST-2026-0001` → **Active · Published · V1.0**
- cross-Suite governed relationships → **demonstrated**
- authority transfer → **none**
- institutional Integration capability → **operationally demonstrated**

The first-production integration baseline does not imply that every future source, transport, profile, or external integration is automatically supported or conformant. Each future integration remains governed by applicable Authority, Provenance, Eligibility, Evaluation, Validation, Conformance, Lifecycle, Publication, and Production requirements.

## Files
- `index.html` — public Integration page.
- `README.md` — repository documentation.
