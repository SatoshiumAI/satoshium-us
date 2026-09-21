# Satoshium Attestor — Authority

**Path:** `/attestor/authority/`  
**Institution:** Satoshium Attestor  
**Current Stage:** Operational Authority  
**Canonical Responsibility:** `Attestor → Trust Statement`

## Purpose

The Authority architecture defines:

- Attesting Authority;
- Attestor authority;
- referenced authority;
- source authority;
- external authority; and
- the boundaries between them.

## Governing Principle

**Reference does not transfer authority.**

Attestor may evaluate governed assertions and authoritative references without acquiring the authority of the institution, source, or party that produced them.

## Attesting Authority

The **Attesting Authority** is the attributable party or governed source responsible for the assertion carried by an Attestation.

Its authority is bounded by the subject matter, role, jurisdiction, source context, scope, time, and limitations under which it legitimately stands behind the assertion.

Conceptually, an Attestation must preserve enough information for the Attesting Authority to be:

- identifiable;
- attributable;
- connected to the assertion;
- understood within its material scope or role;
- traceable through provenance; and
- bounded by relevant limitations.

Canonical structured representations now preserve authority context in production, while Schemas and Validation govern the applicable machine requirements.

## Attestor Authority

Attestor is authoritative for:

- its governed institutional evaluation process;
- Attestor-owned Attestations;
- application of Attestor rules;
- Attestor evaluation records/context;
- Trust Statements;
- lifecycle of Attestor-owned objects; and
- correction or supersession of Attestor-owned objects.

Attestor is **not** authoritative merely by reference for the underlying canonical objects or responsibilities of other institutions.

A Trust Statement is authoritative as an **Attestor conclusion within its defined scope, basis, limitations, status, and relevant time/state**. It is not a universal truth claim.

## Suite Authority Map

- Atlas → Authoritative Intelligence
- Navigator → Workflow Definition / Orchestration
- Certifier → Certification Package
- Registry → Satoshium Registry Record
- Chronicle → Chronicle Entry
- Anchor → Integrity Reference
- Beacon → Discovery Signal / Discovery Metadata
- Attestor → Trust Statement

Attestor may reference these objects without reissuing or replacing their institutional authority.

## Referenced and Source Authority

A referenced authority retains its source-defined authority.

Attestor preserves, where material:

- source identity;
- source identifier;
- provenance;
- scope;
- status;
- relevant time/state;
- role or jurisdiction;
- limitations; and
- relationship to the Attestation or evaluation.

Attribution does not enlarge the source authority.

## External Authority

External authorities may be used where eligible. Their authority must remain attributable and bounded to the role or source under which the relevant assertion or evidence was produced.

External authority does not automatically establish Attestor eligibility or determine an evaluation outcome.

## Authority vs. Eligibility

These concepts are distinct:

- **Authority** → who legitimately stands behind the source assertion, object, or institutional conclusion.
- **Eligibility** → whether that input may enter a particular Attestor evaluation.
- **Evaluation** → what Attestor concludes from eligible governed inputs.

`Authority ≠ Eligibility ≠ Evaluation Outcome`

## Authority vs. Agreement

Preserving an authority does not require Attestor to adopt the authority's assertion as Attestor's conclusion.

`Attribution ≠ Adoption`

Attestor may preserve source authority while reaching any evaluation outcome permitted by its governed Evaluation architecture.

## Conflicting Authorities

When multiple authorities materially disagree:

- each remains separately attributable;
- material conflict is preserved as evaluation context;
- Attestor does not silently erase the disagreement;
- no generic authority ranking is assumed; and
- any bounded resolution belongs to governed Evaluation.

This page does not create a universal hierarchy of authorities.

## First Production Authority Demonstration

The first controlled production operation exercised the Authority architecture across a real multi-institution evaluation.

`ATT-2026-0001` and `TRST-2026-0001` referenced governed Suite objects while preserving the authority of each source institution:

- `SC-CERT-2026-0001` → Certifier authority preserved
- Atlas El Salvador jurisdiction intelligence → Atlas authority preserved
- `SREG-2026-0001` → Registry authority preserved
- `CHR-2026-0001` → Chronicle authority preserved
- `ANCH-2026-0001` → Anchor authority preserved within its defined SCRD integrity scope
- `BEAC-2026-0001` → Beacon authority preserved
- `ATT-2026-0001` → Attestor authority over the canonical Attestation
- `TRST-2026-0001` → Attestor authority over the bounded Trust Statement

**Authority transfer by reference → NONE**

The production evaluation did not:

- re-certify the Certifier decision;
- redefine the underlying Atlas jurisdiction intelligence;
- extend Anchor integrity beyond its defined representation;
- rewrite Registry or Chronicle records;
- convert Beacon discovery into Attestor-owned source authority; or
- create universal Attestor authority over the underlying subject.

The operation therefore demonstrated the governing principle in practice:

**Reference does not transfer authority.**

## What Authority Does Not Establish

Authority does not independently establish:

- truth;
- evidence sufficiency;
- eligibility;
- validation;
- conformance;
- publication;
- currency; or
- a favorable Trust Statement.

## Dependency Position

`Entry Model → Identifiers → Controlled Values → Authority → Provenance → Eligibility → Evaluation → Relationships → Lifecycle → Versioning → Schemas → Validation → Conformance → Publication → Templates → Methodology → Production`

## Status

**Authority → Established and Production-Proven**

- Attesting Authority → defined, bounded, and exercised
- Attestor authority → defined, bounded, and exercised
- referenced/source authority → preserved in production
- external authority → attributable and bounded where applicable
- automatic authority ranking → not adopted
- Authority / Eligibility distinction → preserved
- Authority / Evaluation Outcome distinction → preserved
- Attribution / Adoption distinction → preserved
- authority transfer by reference → prohibited and avoided
- canonical structured authority context → exercised
- production proof → **ESTABLISHED**

## Continuing Authority Governance

Production proof does not enlarge Attestor's authority.

Future Attestor operations remain governed by the same institutional boundary:

**Attestor is authoritative for its own governed Attestations, Evaluation, and Trust Statements. It does not acquire the canonical authority of referenced institutions or external sources.**

Each referenced source retains only the authority legitimately belonging to its own object, assertion, role, jurisdiction, scope, and relevant state.

`Connection ≠ Identity`

`Reference ≠ Authority Transfer`

`Attribution ≠ Adoption`
