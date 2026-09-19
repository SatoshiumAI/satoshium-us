# Satoshium Attestor — Conformance Mechanics

**Version:** 0.1  
**Stage:** Implementation & Validation  
**Step:** 13 — Conformance Mechanics

## 1. Purpose

This specification defines how Satoshium Attestor uses governed Validation Results and other required evidence to make a bounded Conformance Determination.

It implements the established architecture:

> Target + Declared Requirements Set + Required Validation / Evidence → Conformance Determination

Conformance is not another name for Validation. Validation produces governed evidence about tested requirements. Conformance determines whether a declared target satisfies a declared requirements set under an identified conformance scope.

## 2. Governing Distinctions

- Validation ≠ Conformance.
- Evaluation ≠ Conformance.
- Eligibility ≠ Conformance.
- Publication ≠ Conformance.
- `valid` ≠ `conformant`.
- `invalid` ≠ automatically a universal nonconformance claim outside the declared requirements set.
- Partial Testing ≠ Full Conformance.
- Unknown ≠ Pass.
- `not-tested` ≠ pass.
- Conformant ≠ Published.
- Conformance does not establish universal truth.
- Conformance does not transfer authority.

## 3. Conformance Targets

Attestor recognizes three distinct conformance target classes:

1. **Object Conformance** — a specific ATT or TRST object against an identified object requirements set.
2. **Implementation Conformance** — a validator, serializer, producer, or other implementation against an identified implementation requirements set.
3. **Process Conformance** — an identified Attestor process/run against an identified process requirements set.

A determination MUST identify exactly one target class and one target identity.

## 4. Conformance Input Model

A Conformance Determination requires:

```yaml
conformance_request:
  target:
    target_class:
    target_identifier:
    target_version:
  requirements:
    requirements_set:
    requirements_version:
    conformance_profile:
  evidence:
    validation_reports: []
    review_records: []
    context_records: []
  requested_at:
```

### 4.1 Target

The target MUST be identifiable and bounded. A determination for one object, implementation, version, or process MUST NOT be silently generalized to another.

### 4.2 Declared Requirements Set

The determination MUST identify:

- requirements set;
- requirements version;
- applicable conformance profile.

A changed requirements set or materially changed profile requires a new determination.

### 4.3 Evidence

Evidence MAY include:

- executable Validation Reports;
- governed Review records;
- registry/context evidence;
- lifecycle/version evidence;
- implementation test evidence;
- process evidence.

Evidence MUST remain attributable and traceable to its source.

## 5. Conformance Requirement Disposition

Each applicable conformance requirement receives one of:

- `satisfied`
- `not-satisfied`
- `not-applicable`
- `not-demonstrated`

Meanings:

### satisfied
Required evidence demonstrates the requirement within the declared scope.

### not-satisfied
Evidence demonstrates that the requirement is not met.

### not-applicable
The requirements set explicitly determines that the requirement does not apply to the declared target/profile.

### not-demonstrated
The requirement is applicable, but required evidence is absent, incomplete, unresolved, or insufficient.

`not-demonstrated` MUST NOT be treated as `satisfied`.

## 6. Aggregate Conformance Determinations

The canonical aggregate vocabulary is:

- `conformant`
- `nonconformant`
- `undetermined`
- `error`

### conformant

A target is `conformant` only when:

1. the target and requirements set are identified;
2. every applicable mandatory conformance requirement is `satisfied`;
3. no applicable mandatory requirement is `not-satisfied`;
4. no applicable mandatory requirement is `not-demonstrated`;
5. all evidence required by the declared profile is present and traceable.

### nonconformant

A target is `nonconformant` when one or more applicable mandatory requirements are `not-satisfied`.

### undetermined

A target is `undetermined` when no applicable mandatory requirement is known to be `not-satisfied`, but one or more applicable mandatory requirements are `not-demonstrated`.

### error

`error` is used when the conformance process cannot reliably make a determination because the request, requirements set, evidence package, or execution itself is unprocessable.

## 7. Validation-to-Conformance Mapping

Validation Results are evidence, not Conformance Determinations.

For a validation-backed conformance requirement:

| Validation evidence | Conformance disposition |
|---|---|
| applicable mandatory rule `pass` | may support `satisfied` |
| applicable mandatory rule `fail` | supports `not-satisfied` |
| rule `not-applicable` | may support `not-applicable` only when applicability is consistent with the conformance profile |
| applicable mandatory rule `not-tested` | `not-demonstrated` |
| aggregate `valid` | eligible evidence for conformance; not itself `conformant` |
| aggregate `invalid` | evidence of one or more failed mandatory validation requirements |
| aggregate `incomplete` | cannot establish full validation-backed conformance |
| aggregate `error` | cannot establish conformance |

A validation `pass` does not automatically satisfy a conformance requirement if that requirement also requires governed Review or other evidence.

## 8. Governed Review Evidence

Review-dependent requirements remain outside automatic machine adjudication.

A governed Review record used for Conformance MUST identify:

- review record identity;
- target identity/version;
- requirement or rule reviewed;
- reviewer/authority;
- determination;
- basis;
- limitations or uncertainty where material;
- review timestamp;
- source evidence references.

Initial Review disposition vocabulary:

- `satisfied`
- `not-satisfied`
- `not-demonstrated`

A missing required Review record produces `not-demonstrated`, not machine pass.

## 9. Conformance Evidence Package

A complete evidence package SHOULD use:

```yaml
conformance_evidence:
  target_identifier:
  target_version:
  requirements_set:
  requirements_version:
  validation_reports: []
  review_records: []
  context_records: []
  evidence_created_at:
  notes:
```

Evidence identity and provenance MUST be preserved. Evidence MAY be referenced rather than embedded where the reference remains governed and reviewable.

## 10. Conformance Determination Record

Canonical initial structure:

```yaml
conformance_determination:
  determination_version: V1.0
  target:
    target_class:
    target_identifier:
    target_version:
  requirements:
    requirements_set:
    requirements_version:
    conformance_profile:
  evidence_references: []
  requirement_results:
    - requirement_id:
      disposition:
      evidence_references: []
      message:
  aggregate_determination:
  determined_by:
    identifier:
    authority_context:
  determined_at:
  limitations: []
  notes:
```

## 11. Authority

Conformance authority is bounded to the declared requirements set and target.

A Conformance Determination:

- does not adopt source authority;
- does not transfer Attesting Authority;
- does not replace Attestor evaluation;
- does not establish publication authorization;
- does not establish universal truth;
- does not establish conformance to requirements not declared in the determination.

## 12. Versioning and Change

A Conformance Determination is bound to:

- target identity;
- target version;
- requirements-set identity;
- requirements-set version;
- conformance profile;
- evidence package used.

A materially changed target version, requirements set, conformance profile, or required evidence state requires a new determination or governed superseding determination.

Prior determinations remain historical records and MUST NOT be silently overwritten.

## 13. Representative Validation Proof and Conformance

The Step 12 representative ATT and TRST achieved machine Validation Result `valid`.

That establishes representative executable-validation proof only.

It does **not** by itself establish Object Conformance because Review-bound requirements remain `not-tested` in the Validation Reports. If the selected conformance profile requires those Review requirements, governed Review evidence must be supplied before aggregate `conformant` is available.

This is intentional:

> Machine validity can be established while full Conformance remains undetermined pending required governed Review.

## 14. Initial Object-Conformance Profile

The initial Attestor object-conformance profile requires:

1. canonical target identity/version;
2. applicable base-profile Validation Report;
3. Validation aggregate `valid`;
4. zero failed mandatory validation rules;
5. zero mandatory machine-testable `not-tested` rules;
6. required governed Review records for applicable Review-bound requirements;
7. traceable execution/context evidence where used;
8. no unresolved mandatory conformance requirement.

This profile does not require publication.

## 15. Mechanics

The initial deterministic conformance procedure is:

1. identify target and target version;
2. identify requirements set/version/profile;
3. load required evidence;
4. verify evidence refers to the same target/version;
5. map machine validation evidence to applicable conformance requirements;
6. identify applicable Review-bound requirements;
7. resolve those requirements from governed Review records;
8. mark unavailable or insufficient mandatory evidence `not-demonstrated`;
9. aggregate:
   - any mandatory `not-satisfied` → `nonconformant`;
   - else any mandatory `not-demonstrated` → `undetermined`;
   - else all mandatory applicable requirements satisfied → `conformant`;
   - unprocessable request/evidence → `error`;
10. preserve the determination as a governed record.

## 16. Step 13 Determination

**Conformance Mechanics v0.1 → ESTABLISHED.**

The architecture now has an explicit governed bridge:

> Validation Rules → Validation Results → Conformance Evidence → Conformance Determination

Executable conformance implementation and representative conformance testing remain subsequent implementation work.
