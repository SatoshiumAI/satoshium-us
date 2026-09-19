# Satoshium Attestor — Executable Validation Requirements

**Version:** 0.1  
**Stage:** Implementation & Validation  
**Purpose:** Normative bridge from established Attestor architecture to executable validation rules.

## 1. Governing Principle

`Object + Applicable Normative Requirements → Validation → Governed Validation Result`

Validation tests whether an Attestor-owned object or governed representation satisfies applicable structural and normative requirements.

- `Validation ≠ Evaluation`
- `Validation ≠ Eligibility`
- `Validation ≠ Conformance`
- `Valid ≠ Published`
- `Valid ≠ True`
- `Valid ≠ Supported`
- `Machine-readable ≠ Valid`

A validator implements adopted architecture. It does not create architecture.

## 2. Canonical Validation Targets

Executable validation requires separate profiles for:

1. **Attestation (`ATT`)**
2. **Trust Statement (`TRST`)**

Specialized Attestation profiles may add requirements for adopted Attestation Types such as `evidence` and `source-provenance`.

**Trust Signal is excluded.** It is a legacy design artifact, not a canonical Attestor object.

A Correction / Change profile may govern change behavior, but correction does not become a separate canonical object class merely because a profile exists.

## 3. Validation Layers

Validation must support these layers:

1. **Representation / Syntax** — parseability and supported serialization.
2. **Structure** — required elements, forms, and object-specific structure.
3. **Controlled Semantics** — canonical controlled values used in their governed contexts.
4. **Relationships** — permitted meanings, directionality, source/target roles, and applicable cardinality.
5. **Provenance / Authority** — preserved provenance and authority context without authority transfer.
6. **Lifecycle / Versioning** — coherent state, identity, version, and governed history.
7. **Normative Rules** — satisfaction of applicable Attestor requirements traceable to architecture.

## 4. Controlled Vocabulary

### Attestation Type
`identity` · `evidence` · `source-provenance` · `verification-related` · `relationship-condition` · `correction-supersession`

### Lifecycle State
`draft` · `active` · `superseded` · `withdrawn` · `retired`

### Publication State
`unpublished` · `published`

### Evaluation Outcome
`supported` · `partially-supported` · `not-supported` · `contradicted` · `indeterminate`

### Relationship Type
`supports` · `references` · `derived-from` · `evaluates` · `results-in` · `supersedes` · `corrects` · `related-to`

### Provenance Mode
`direct` · `referenced` · `derived`

### Authority Context
`Attestor` · `Suite-source` · `external-source`

Implementations must not silently introduce unofficial canonical values. Confidence scales, reputation scores, Trust Signal direction/strength values, and similar June-era concepts are not adopted.

## 5. Identifier Baseline

- Attestation → `ATT-YYYY-NNNN`
- Trust Statement → `TRST-YYYY-NNNN`

Canonical identifier answers **which governed object**. Version identity answers **which governed state of that object**.

Identifiers must not be reused or reassigned.

Exact executable regex, year constraints, allocation/collision behavior, and URI/addressing rules require the Identifiers specification before machine rules are frozen.

## 6. Attestation Validation Baseline

An Attestation is a governed, attributable assertion presented for an Attestor purpose.

The executable ATT profile must ultimately test the presence and coherence of:

- canonical Attestation identity;
- Attestation Type;
- Attesting Authority;
- subject;
- bounded assertion;
- scope;
- evidence references where applicable;
- source / governed references where applicable;
- provenance;
- relevant time/state where material;
- lifecycle context;
- publication context where represented;
- limitations / uncertainty where material;
- governed relationships;
- creation/update context;
- version identity.

`Attestation = governed assertion`

An Attestation must not be validated as though it were Attestor's final bounded conclusion.

### Current implementation boundary

The supplied `attestation-schema.md` is still labeled **Foundational Candidate Profile** and explicitly says it is not a normative machine schema. It therefore cannot responsibly freeze exact field names, cardinalities, required/optional status, timestamp rules, or serialization.

The canonical Attestation schema must be reconciled to completed Advanced Architecture before the final ATT machine profile is frozen.

## 7. Trust Statement Validation Baseline

A Trust Statement is Attestor's canonical institutional output: a governed, attributable, bounded conclusion produced through Rule-Constrained Evaluation.

The supplied Advanced Architecture Trust Statement schema establishes this structural baseline:

- `trust_statement_identifier`
- `lifecycle_state`
- `publication_state`
- `subject.identifier`
- `subject.type`
- `bounded_conclusion`
- `scope`
- `attestor_attribution.identifier`
- `attestor_attribution.authority_context`
- `supporting_attestations`
- `evaluation.outcome`
- `evaluation.basis_references`
- `evaluation.applicable_rules`
- `evaluation.relevant_time_or_state`
- `evaluation.material_conflicts`
- `evaluation.material_exclusions`
- `provenance.mode`
- `provenance.source_or_origin`
- `provenance.derivation_basis`
- `provenance.material_limitations`
- `relationships`
- `created_at`
- `updated_at`
- `version_identity`
- `limitations`
- `uncertainty`
- `notes`

### Minimum TRST semantic rules

1. Identifier belongs to `TRST-YYYY-NNNN`.
2. Lifecycle state is canonical.
3. Publication state is canonical.
4. `bounded_conclusion` remains separate from `evaluation.outcome`.
5. Attestor attribution uses authority context `Attestor`.
6. Evaluation Outcome is canonical.
7. Trust Statement provenance represents derivation from governed evaluation.
8. Relationship values are canonical when present.
9. Supporting Attestation reference(s) are represented as applicable.
10. Evaluation basis is traceable.
11. Applicable rules/methodology context are represented as applicable.
12. Relevant time/state, material conflicts, exclusions, limitations, and uncertainty are preserved where material.
13. Lifecycle and publication states remain distinct.
14. Canonical identifier and version identity remain distinct.
15. A materially different bounded conclusion requires a new canonical Trust Statement.

Validation tests representation and rule compliance of evaluation context; it does not rerun substantive Evaluation.

## 8. Specialized / Legacy Treatment

### Evidence Attestation
The supplied Evidence Attestation document remains a foundational candidate. Its historical candidate relationship values must not override adopted Attestor vocabulary. The adopted `evidence` type can receive an executable profile after current profile requirements are reconciled.

### Source / Provenance Attestation
The supplied Source document remains a foundational candidate. Its historical source-relationship vocabulary is not canonical machine vocabulary. The adopted `source-provenance` type can receive an executable profile after reconciliation.

### Correction / Change
The supplied Correction template predates completed Lifecycle, Versioning, and Corrections architecture. It must not be implemented as a separate canonical object class.

### Trust Signal
Legacy only; excluded from canonical validation targets.

## 9. Validation Result Contract

Every executable validation run must be capable of preserving:

- validation target identity, when parseable;
- target object class/profile;
- validator/specification version;
- applicable requirements set;
- rules/tests applied;
- validation layer for each test;
- requirement identifier for every failure;
- machine-readable per-test result;
- human-readable failure reason;
- defect location/path where determinable;
- run timestamp;
- aggregate validation determination.

A validation failure means an applicable normative requirement was not satisfied. It does **not** mean an assertion was proven false, a conclusion should be reversed, an input is ineligible, or every broader conformance question failed.

### Result vocabulary boundary

The architecture reserves final Validation Result vocabulary for implementation. Version 0.1 therefore does not yet freeze terms such as `valid`, `invalid`, `error`, or `not-applicable`.

## 10. Requirement Identifier Convention — Proposed

For the executable rule catalog:

- `VAL-REP-*` — representation / syntax
- `VAL-STR-*` — structural
- `VAL-SEM-*` — controlled semantics
- `VAL-REL-*` — relationships
- `VAL-PA-*` — provenance / authority
- `VAL-LV-*` — lifecycle / versioning
- `VAL-NRM-*` — cross-cutting normative rules
- `VAL-ATT-*` — Attestation-specific
- `VAL-TRST-*` — Trust Statement-specific

These are implementation identifiers only. They do not alter canonical ATT/TRST identifiers.

## 11. Dependencies Before Freezing Machine Rules

Bring these governing sources into the next pass:

1. **Identifiers**
2. **Authority**
3. **Provenance**
4. **Relationships**
5. **Lifecycle**
6. **Versioning**
7. **Rules**
8. **Current canonical Attestation Schema**

The current source set is sufficient for this requirements baseline, but not for responsibly freezing the complete executable validator.

## 12. Step 1 Determination

**Executable Validation Requirements Set v0.1 → Established as implementation bridge.**

Do **not** write validator code yet.

Next:

> **Normalize the canonical Attestation machine contract and import the governing dependencies needed to convert this baseline into numbered executable rules.**

Governing chain:

`Principle → Rule → Normative Requirement → Validation Rule → Validation Result`

**Validator → Implements architecture.**  
**Validator → Does not create architecture.**
