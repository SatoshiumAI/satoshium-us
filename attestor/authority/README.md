# Satoshium Attestor — Authority

**Path:** `/attestor/authority/`  
**Institution:** Satoshium Attestor  
**Architecture Stage:** Advanced Architecture  
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

Exact machine representation remains a Schema concern.

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

**Authority → Established**

- Attesting Authority → defined and bounded
- Attestor authority → defined and bounded
- referenced/source authority → preserved
- external authority → attributable and bounded
- automatic authority ranking → not adopted
- authority transfer by reference → prohibited
- production proof → pending
