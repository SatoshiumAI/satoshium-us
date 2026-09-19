# Satoshium Attestor — Machine Contract Specification

**Version:** 0.1  
**Stage:** Implementation & Validation  
**Applies to:** Canonical Attestation (`ATT`) and Trust Statement (`TRST`) representations  
**Dependencies:** Attestation Schema, Trust Statement Schema, Controlled Values, Identifiers, Authority, Provenance, Relationships, Lifecycle, Versioning, Validation Requirements, Validation Rule Catalog, Methodology, Conformance, Production

## 1. Purpose

This specification establishes the first exact machine-readable contract for canonical Attestor objects.

It converts the established conceptual ATT/TRST schemas into an executable representation without changing Attestor architecture.

`Architecture → Schema → Machine Contract → Executable Validation → Validation Result`

This contract is intentionally limited to object representation and deterministic validation prerequisites. It does not perform Eligibility determination, Rule-Constrained Evaluation, institutional Review, Conformance determination, Publication authorization, or Production Readiness approval.

## 2. Serialization Decision

**Canonical validation serialization: YAML 1.2-compatible mapping syntax.**

Rationale:
- the adopted Attestation and Trust Statement schemas are already expressed structurally in YAML;
- YAML preserves human reviewability during the first production implementation;
- the same data model can later be represented in JSON without changing institutional meaning;
- executable validation should validate the governed data model, not depend on decorative HTML.

UTF-8 is required.

The root document must contain exactly one Attestor object.

## 3. Common Scalar Conventions

### 3.1 Identifiers

Attestation identifier:

`^ATT-[0-9]{4}-[0-9]{4}$`

Trust Statement identifier:

`^TRST-[0-9]{4}-[0-9]{4}$`

This expression validates representation only. Allocation, uniqueness, reuse prevention, and creation-year truth require authoritative registry/process context.

### 3.2 Timestamps

Machine timestamps use RFC 3339 date-time strings with an explicit UTC offset or `Z`.

Examples:

`2026-09-18T21:15:00-07:00`

`2026-09-19T04:15:00Z`

A date without a time is not a canonical object timestamp under this contract.

### 3.3 Version Identity

`version_identity` is a non-empty string.

For the initial implementation profile, the recommended canonical form is:

`V<major>.<minor>`

Example: `V1.0`

The validator may enforce the representation pattern when this implementation profile is declared. Version semantics remain governed by Versioning architecture.

### 3.4 Empty Values

A required field must not be satisfied by:
- YAML null;
- an empty string;
- an empty mapping where substantive content is required.

An optional list may be omitted. If present, it must be a YAML sequence. An empty sequence is permitted unless an applicable rule/profile requires one or more members.

## 4. Reusable Machine Structures

### 4.1 Subject Reference

```yaml
identifier: <non-empty string>
type: <non-empty string>
```

Both fields are required in the base machine contract.

### 4.2 Authority Reference

```yaml
identifier: <non-empty string>
authority_context: <controlled value>
```

Allowed `authority_context` values:
- `Attestor`
- `Suite-source`
- `external-source`

### 4.3 Governed Object Reference

```yaml
identifier: <non-empty string>
source: <non-empty string>
```

Profiles may add type, state, version, URI, or provenance metadata.

### 4.4 Relationship

```yaml
type: <controlled relationship value>
target_identifier: <non-empty string>
```

Allowed types:
- `supports`
- `references`
- `derived-from`
- `evaluates`
- `results-in`
- `supersedes`
- `corrects`
- `related-to`

The containing object is the relationship source unless a later exchange profile explicitly serializes source identity.

### 4.5 Provenance

```yaml
mode: <direct|referenced|derived>
source_or_origin: <non-empty value>
relevant_time_or_state: <value or null>
derivation_basis: <value or null>
material_limitations:
  - <string>
```

`mode` and `source_or_origin` are required.

`derivation_basis` is required when `mode: derived`.

## 5. Canonical Attestation Machine Contract

### 5.1 Required Fields

A base canonical Attestation must contain:

- `attestation_identifier`
- `attestation_type`
- `lifecycle_state`
- `publication_state`
- `attesting_authority`
- `subject`
- `assertion`
- `scope`
- `provenance`
- `created_at`
- `updated_at`
- `version_identity`

### 5.2 Optional / Conditional Fields

- `evidence_references`
- `source_references`
- `governed_references`
- `relationships`
- `limitations`
- `uncertainty`
- `notes`

Specialized profiles may make an optional base field mandatory.

### 5.3 Controlled Values

`attestation_type`:
- `identity`
- `evidence`
- `source-provenance`
- `verification-related`
- `relationship-condition`
- `correction-supersession`

`lifecycle_state`:
- `draft`
- `active`
- `superseded`
- `withdrawn`
- `retired`

`publication_state`:
- `unpublished`
- `published`

### 5.4 ATT Contract

```yaml
attestation_identifier: ATT-YYYY-NNNN
attestation_type: identity

lifecycle_state: draft
publication_state: unpublished

attesting_authority:
  identifier: <non-empty string>
  authority_context: <Attestor|Suite-source|external-source>

subject:
  identifier: <non-empty string>
  type: <non-empty string>

assertion: <non-empty string>
scope: <non-empty value>

evidence_references: []
source_references: []
governed_references: []

provenance:
  mode: <direct|referenced|derived>
  source_or_origin: <non-empty value>
  relevant_time_or_state:
  derivation_basis:
  material_limitations: []

relationships: []

created_at: <RFC3339 timestamp>
updated_at: <RFC3339 timestamp>
version_identity: V1.0

limitations: []
uncertainty: []
notes:
```

### 5.5 Deterministic ATT Invariants

1. Identifier matches ATT pattern.
2. Attestation Type is controlled.
3. Lifecycle state is controlled.
4. Publication state is controlled.
5. Attesting Authority identifier is non-empty.
6. Attesting Authority context is controlled.
7. Subject identifier and type are non-empty.
8. Assertion is non-empty.
9. Scope is non-empty.
10. Provenance mode is controlled.
11. Provenance source/origin is non-empty.
12. Derived provenance includes derivation basis.
13. Relationship types are controlled.
14. Relationship targets are non-empty.
15. `created_at` and `updated_at` are valid RFC 3339 date-times.
16. `updated_at` must not precede `created_at`.
17. Version identity is non-empty and, under this profile, matches `V<major>.<minor>`.
18. An ATT object must not contain `trust_statement_identifier`.
19. `review`, `correction`, and `inactive` must not appear as lifecycle-state values.

Materiality, truth, eligibility, sufficiency, and authority legitimacy remain outside deterministic object validation unless an applicable governed profile supplies additional machine-testable evidence.

## 6. Canonical Trust Statement Machine Contract

### 6.1 Required Fields

A base canonical Trust Statement must contain:

- `trust_statement_identifier`
- `lifecycle_state`
- `publication_state`
- `subject`
- `bounded_conclusion`
- `scope`
- `attestor_attribution`
- `supporting_attestations`
- `evaluation`
- `provenance`
- `created_at`
- `updated_at`
- `version_identity`

### 6.2 Optional / Conditional Fields

- `relationships`
- `limitations`
- `uncertainty`
- `notes`

Within `evaluation`, material conflicts/exclusions may be empty but the fields are retained in the canonical contract so the production record explicitly distinguishes none recorded from silently omitted.

### 6.3 TRST Contract

```yaml
trust_statement_identifier: TRST-YYYY-NNNN

lifecycle_state: draft
publication_state: unpublished

subject:
  identifier: <non-empty string>
  type: <non-empty string>

bounded_conclusion: <non-empty string>
scope: <non-empty value>

attestor_attribution:
  identifier: <non-empty string>
  authority_context: Attestor

supporting_attestations:
  - ATT-YYYY-NNNN

evaluation:
  outcome: <supported|partially-supported|not-supported|contradicted|indeterminate>
  basis_references:
    - <reference>
  applicable_rules:
    - <rule identifier>
  relevant_time_or_state: <value>
  material_conflicts: []
  material_exclusions: []

provenance:
  mode: derived
  source_or_origin: <non-empty value>
  derivation_basis: <non-empty value>
  material_limitations: []

relationships: []

created_at: <RFC3339 timestamp>
updated_at: <RFC3339 timestamp>
version_identity: V1.0

limitations: []
uncertainty: []
notes:
```

### 6.4 Deterministic TRST Invariants

1. Identifier matches TRST pattern.
2. Lifecycle state is controlled.
3. Publication state is controlled.
4. Subject identifier and type are non-empty.
5. Bounded conclusion is non-empty.
6. Scope is non-empty.
7. Attestor attribution identifier is non-empty.
8. Attestor attribution authority context equals `Attestor`.
9. `supporting_attestations` is a sequence with at least one ATT identifier for the initial production profile.
10. Every supporting Attestation identifier matches the ATT pattern.
11. Evaluation Outcome is controlled.
12. `basis_references` is a sequence with at least one member for the initial production profile.
13. `applicable_rules` is a sequence with at least one member for the initial production profile.
14. `material_conflicts` and `material_exclusions` are sequences.
15. Provenance mode equals `derived`.
16. Provenance source/origin is non-empty.
17. Derivation basis is non-empty.
18. Relationship types are controlled.
19. Relationship targets are non-empty.
20. `created_at` and `updated_at` are valid RFC 3339 date-times.
21. `updated_at` must not precede `created_at`.
22. Version identity is non-empty and, under this profile, matches `V<major>.<minor>`.
23. A TRST object must not contain `attestation_identifier`.
24. Bounded conclusion and Evaluation Outcome remain separate fields.

The validator does not determine whether the outcome or bounded conclusion is substantively correct.

## 7. Validation Result Machine Contract

The implementation requires a result vocabulary capable of distinguishing requirement failure from validator inability.

### 7.1 Per-Rule Result Vocabulary

- `pass` — applicable rule tested and satisfied.
- `fail` — applicable rule tested and not satisfied.
- `not-applicable` — rule legitimately outside the target/profile scope.
- `not-tested` — applicable rule was not executed or could not be completed.

`not-tested` is never equivalent to `pass`.

### 7.2 Aggregate Validation Determination

- `valid` — all applicable mandatory machine-testable rules executed and passed; no applicable mandatory rule is `fail` or `not-tested`.
- `invalid` — one or more applicable mandatory rules failed.
- `incomplete` — no tested mandatory rule establishes invalidity, but one or more applicable mandatory rules remain `not-tested`.
- `error` — the validation run itself could not reliably produce a governed determination because of validator/runtime failure or an unprocessable validation context.

This vocabulary concerns validation only.

`valid ≠ conformant ≠ supported ≠ published`

### 7.3 Validation Report

```yaml
validation_report:
  report_version: V1.0
  target_identifier:
  target_profile:
  target_version:
  requirements_set:
  requirements_version:
  validator_identifier:
  validator_version:
  run_at:
  aggregate_result: <valid|invalid|incomplete|error>

  results:
    - rule_id:
      layer:
      result: <pass|fail|not-applicable|not-tested>
      location:
      message:

  summary:
    passed:
    failed:
    not_applicable:
    not_tested:

  notes:
```

Every `fail` and `not-tested` result must identify a rule and provide a reviewable message. Location should be supplied when determinable.

## 8. Profile Declaration

Validation must identify the profile being applied.

Initial profile identifiers:

- `attestor.attestation.base`
- `attestor.trust-statement.base`

Specialized profiles will later include bounded extensions such as:
- `attestor.attestation.evidence`
- `attestor.attestation.source-provenance`

A specialized profile may add requirements but must not silently weaken base requirements.

## 9. Methodology Alignment

The machine contract supports, but does not replace, the governed Methodology.

The production sequence remains institutionally ordered:

`Purpose → Attestation → Eligibility → Evaluation Basis → Rule-Constrained Evaluation → Trust Statement → Validation / Review → Lifecycle / Versioning → Conformance where applicable → Publication where authorized → Continuing Governance`

Object validation occurs after canonical object formation at the applicable Methodology stage. It must not be used to reverse-engineer a conclusion or replace institutional Review.

## 10. Conformance Boundary

A valid object is not automatically conformant.

Conformance requires:
- identified target;
- declared requirements set/profile;
- version;
- complete applicable mandatory requirements;
- validation/test evidence;
- tested scope;
- limitations;
- governed conformance determination.

`Normative Requirements → Validation Rules → Validation Results → Conformance Evidence → Conformance Determination`

This machine contract supplies object-validation evidence. It does not itself make the broader conformance claim.

## 11. Production Boundary

Production requires validation of the actual canonical ATT and TRST objects created during the real operation.

A fixture, example, schema sample, or rehearsal object cannot substitute for production-object validation.

For the first production operation:

`Production ATT → Applicable Validation Rules → Validation Result`

`Production TRST → Applicable Validation Rules → Validation Result`

The Production Readiness Gate should not pass until the selected production profile can be represented and validated under this contract and the remaining required controls are operationally usable.

## 12. Deferred Specialized Contracts

The following remain next-order implementation work:

1. reconcile `evidence-attestation-schema.md` as a specialized profile;
2. reconcile `source-attestation-schema.md` as a specialized profile;
3. reconcile the correction/change template to current Corrections/Lifecycle/Versioning architecture;
4. produce executable schema files from this contract;
5. implement the validator;
6. create positive/negative validation fixtures and expected results;
7. execute validation against representative ATT/TRST objects.

## 13. Step 4 Determination

**ATT/TRST Machine Contract v0.1 → Established for implementation.**

This specification now fixes the initial:
- serialization;
- base required/optional field model;
- controlled machine structures;
- timestamp representation;
- identifier expressions;
- base ATT/TRST deterministic invariants;
- validation result vocabulary;
- validation report contract; and
- base profile identifiers.

These decisions are implementation specifications subordinate to established Attestor architecture. They do not alter canonical institutional meaning.

### Next implementation step

**Create executable ATT/TRST schema artifacts and the first validator implementation from this machine contract.**
