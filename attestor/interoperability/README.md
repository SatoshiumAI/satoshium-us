Satoshium Attestor — Interoperability
Page
`/attestor/interoperability/`
Purpose
This page defines the established interoperability architecture for Satoshium Attestor.
Interoperability is semantic and authority-preserving compatibility across institutional boundaries.
It allows governed information to participate in Attestor without losing the meaning, identity, provenance, scope, relevant state, relationships, limitations, or authority necessary to interpret that information correctly.
Governing Principle
> **Reference does not transfer authority.**
Canonical Responsibility
Attestor → Trust Statement
Interoperability supports Attestor's ability to produce governed Trust Statements without absorbing the canonical responsibilities of source institutions.
Interoperability vs Integration
> **Interoperability → Preserve Meaning and Authority**
> **Integration → Connect and Exchange**
Interoperability governs what must remain intact across a boundary.
Integration governs the operational connection through which governed information is obtained or exchanged.
Reference Context
The established Attestor Reference Profile context is:
`Identifier + Source + Provenance + Type + Status + Scope + Relationship + Authority`
Additional relevant state, version identity, limitations, and source-specific context are preserved where applicable.
Structured governed references are now exercised in canonical production ATT/TRST representations. The institutional reference context is established; transport-specific or external exchange serializations may continue to evolve where future profiles require them.
Reference Rather Than Duplicate
Where an authoritative source object already exists, Attestor should normally reference it rather than silently duplicate it as an Attestor-owned canonical object.
The governed relationship is:
`Source Object → Governed Reference → Eligibility Determination → Attestation / Evaluation Basis → Rule-Constrained Evaluation → Trust Statement`
The source object remains authoritative in its originating institution.
Eligibility
Interoperability does not itself establish Eligibility.
> **Availability ≠ Eligibility**
> **Authority ≠ Eligibility**
> **Reference ≠ Eligibility**
> **Eligible Here ≠ Eligible Everywhere**
Authority
Attestor preserves the distinction among:
Attesting Authority;
Referenced Authority;
Attestor Authority.
> **Attribution ≠ Adoption**
A source's authority is not transferred merely because its object is interoperable with Attestor.
Provenance
Adopted provenance modes:
`direct`
`referenced`
`derived`
Interoperability must preserve enough provenance to prevent Evaluation from becoming a provenance break.
Relationships
Adopted relationship values:
`supports`
`references`
`derived-from`
`evaluates`
`results-in`
`supersedes`
`corrects`
`related-to`
> **Connection does not imply identity.**
> **Reference ≠ Support**
> **Reference ≠ Derivation**
Source State and Change
Attestor preserves the relevant source state used during Evaluation.
> **Source State at Evaluation ≠ Later Source State**
A material source-state change may trigger Review:
`Material Source-State Change → Review`
Review does not automatically determine:
correction;
withdrawal;
supersession;
lifecycle transition;
new Attestation;
new Trust Statement.
Attestor responds under its own Lifecycle, Versioning, Correction, and Evaluation architecture.
External Interoperability
External governed information may participate when the applicable requirements can be established, including:
source identity;
authority;
provenance;
scope;
relevant state;
permitted use;
Eligibility;
applicable Validation.
External interoperability does not transfer external authority to Attestor.
No particular external standard, protocol, API, or transport is required by the institutional architecture.
Suite Relationships
Atlas → Authoritative Intelligence
Navigator → Workflow Definition / Orchestration
Certifier → Certification Package
Registry → Satoshium Registry Record
Chronicle → Chronicle Entry
Anchor → Integrity Reference
Beacon → Discovery Signal / Discovery Metadata
Attestor → Trust Statement
Each institution retains authority for its canonical objects.
First Production Interoperability Demonstration
The first controlled production operation demonstrated concrete interoperability across the Suite.
The production object set included:
`SC-CERT-2026-0001` → Certifier Certification Package
`SREG-2026-0001` → Registry Record
`CHR-2026-0001` → Chronicle Entry
`ANCH-2026-0001` → Anchor Integrity Reference
`BEAC-2026-0001` → Beacon Discovery Signal
`ATT-2026-0001` → Attestor Attestation
`TRST-2026-0001` → Attestor Trust Statement
The operation demonstrated preservation of:
canonical identity;
source attribution and provenance;
relevant source state;
relationship meaning;
object-class distinction;
institutional authority boundaries; and
Attestor's separate authority over its own bounded conclusion.
Certifier remained authoritative for `SC-CERT-2026-0001`.
Registry, Chronicle, Anchor, and Beacon retained authority over their respective canonical objects.
Attestor governed only its own Eligibility determination, Attestation, Rule-Constrained Evaluation, and Trust Statement.
> **Connection does not imply identity.**
> **Reference does not transfer authority.**
This establishes a first-production Suite interoperability baseline. It does not establish automatic interoperability for every future external protocol, profile, transport, representation, or source.
Trust Signals and Reputation
Attestor does not establish Trust Signal as a canonical Attestor object.
Attestor does not establish a generic reputation object, reputation score, confidence percentage, or trust score.
Trust-relevant considerations are handled through the established Attestation, Evidence, Eligibility, Provenance, Relationships, Evaluation, limitations, uncertainty, and Trust Statement architecture.
Validation and Conformance
Interoperable references and resulting Attestor objects remain subject to applicable Validation and Conformance requirements.
> **Validation ≠ Eligibility**
> **Validation ≠ Evaluation**
> **Validation ≠ Conformance**
Executable Validation and object-level Conformance are established and were exercised during the first production operation. Interoperable references and resulting Attestor objects remain independently subject to their applicable Validation and Conformance requirements.
Technology-Specific Implementation Matters
The institutional interoperability architecture is established and has been demonstrated in production. The following remain technology-specific, external-profile, or future implementation concerns rather than unresolved institutional architecture:
exact machine serialization of references;
concrete object-resolution mechanisms;
source-change notification/detection mechanisms;
API and transport formats;
authentication and authorization where required;
external protocol adapters;
reference vectors.
Status
Interoperability Architecture → Established
Suite Interoperability → Operationally Demonstrated
Reference Profile context → established
governed reference fields / semantics → established
canonical identity preservation → established and demonstrated
provenance preservation → established and demonstrated
relevant source-state preservation → established and demonstrated
relationship semantics → established and demonstrated
authority boundaries → established and demonstrated
source-object duplication avoidance → established
Eligibility boundary → established
Validation dependency → established and exercised
Conformance dependency → established and exercised
`SC-CERT-2026-0001` → interoperable Certifier source demonstrated
`SREG-2026-0001` → governed Registry relationship demonstrated
`CHR-2026-0001` → governed Chronicle relationship demonstrated
`ANCH-2026-0001` → governed Anchor relationship demonstrated
`BEAC-2026-0001` → governed Beacon relationship demonstrated
`ATT-2026-0001` → canonical Attestor Attestation demonstrated
`TRST-2026-0001` → canonical Attestor Trust Statement demonstrated
authority transfer → none
first-production Suite interoperability baseline → established
Future external protocols, transports, adapters, profiles, and representations remain subject to independent interoperability, Validation, Conformance, Authority, Provenance, Eligibility, and Production requirements.
Files
`index.html` — public Interoperability page.
`README.md` — repository documentation.
