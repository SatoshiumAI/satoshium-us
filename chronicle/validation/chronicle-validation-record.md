# Chronicle Validation Record

## Status

**Phase VIII — Validation and Operational Procedure**

This document defines what Chronicle preserves about a completed Validation and where that information should initially reside.

It does not establish a new canonical Chronicle object.

---

# Purpose

Chronicle must be able to reconstruct:

```text
what was validated
which Entry Version was evaluated
which requirements applied
which rules passed or failed
what result was reached
what corrective action was required
whether Revalidation occurred
```

This information is the Chronicle Validation Record.

The phrase:

```text
Validation Record
```

describes the preserved Validation information.

It does not currently designate a separately identified canonical object.

---

# Initial Architecture Decision

Chronicle should keep the first production Validation implementation:

```text
lightweight
procedural
traceable
non-duplicative
```

Therefore, Chronicle will **not initially create a separate canonical Validation Record object**.

No new identifier namespace is required.

No independent Validation lifecycle is required.

No separate Validation schema is required at this stage.

---

# Governing Principle

> Preserve enough to reconstruct the Validation decision without creating a new object before operations justify one.

---

# Where Validation Results Belong

Four possible locations were considered:

```text
1. Chronicle Entry metadata
2. Publication metadata
3. Internal Validation artifact
4. Dedicated canonical Validation Record
```

The initial production model should use a combination of:

```text
Internal Validation Artifact
        +
Minimal Publication / Entry linkage where needed
```

and defer a dedicated canonical Validation Record.

---

# 1. Directly in Chronicle Entry Metadata

Chronicle should **not initially embed the entire Validation Record inside every Chronicle Entry**.

Reasons:

* Validation is a process result, not part of the historical Occurrence itself.
* Embedding full Validation detail would increase universal Entry complexity.
* Validation procedures may evolve independently of Entry schema.
* Phase VII intentionally avoided making Validation State a universal Base Schema field.
* A full embedded record risks mixing production-process metadata with historical content.

However, a minimal reference to Validation may eventually be appropriate where publication or auditability requires one.

Example future concept:

```text
validation_reference
```

This should not be added to the Base Schema until production use demonstrates a stable requirement.

---

# 2. Publication Metadata

Publication metadata may preserve limited Validation information when needed to establish that the published Entry passed the required gate.

Potential publication-facing information includes:

```text
Validation result
Validation date
validated Entry Version
Validation artifact reference
```

This is useful because:

```text
Validation PASS
        ↓
Publication eligibility
```

But Publication metadata should not become the sole authoritative storage location for full Validation findings.

Validation may occur before Publication, after Correction, or during maintenance.

---

# 3. Internal Validation Artifact

The initial preferred location for the complete material Validation result is:

```text
an internal Validation artifact
```

This may be:

```text
Markdown report
structured checklist
machine-generated validation output
build artifact
review record
```

The artifact should be associated with the exact Entry Version evaluated.

This approach provides:

* traceability;
* auditability;
* procedural flexibility;
* low schema overhead;
* room to refine Validation before freezing another object model.

This is the preferred initial implementation.

---

# 4. Dedicated Canonical Validation Record

Chronicle should **not create a dedicated canonical Validation Record yet**.

A separate object may become justified later if production demonstrates a need for:

```text
independent Validation identity
public citation of Validation decisions
multiple Validation events per Entry Version
independent Validation lifecycle
external referencing of Validation results
formal reviewer identity
machine-readable Validation histories
cross-institution validation interoperability
```

Until those needs actually appear, creating another canonical object would be premature.

---

# Initial Recording Model

The recommended first production model is:

```text
Chronicle Entry
        ↓
Validated Entry Version
        ↓
Internal Validation Artifact
        ↓
PASS / FAIL
        ↓
Publication or Return for Correction
```

The Validation artifact records the process.

The Chronicle Entry remains the canonical historical object.

---

# Minimum Validation Record Content

Every material Validation should preserve:

```text
Entry Identifier
Entry Version
Validation Date / Time
Overall Validation Result
Rules Applied
Rule-by-Rule Results
Not Applicable Rules where material
Not Evaluated Rules where applicable
Blocking Failures
Warnings / Notes where retained
Base Schema Version
Event-Type Profile and Version where applicable
Validation Method
Validator / Workflow identity
Corrective Action where required
Reverification Requirement
Revalidation Requirement
Supporting Artifact References
```

---

# Entry Identity

The Validation Record must identify:

```text
entry_id
entry_version
```

Validation is never recorded against an ambiguous Entry state.

Example:

```text
CHR-2026-0001
Entry Version 1
```

A later material Version requires a distinguishable Validation result.

---

# Governing Requirement Context

The Validation Record should identify the requirements applied.

At minimum:

```text
Chronicle Base Schema Version
Event-Type Profile Version where applicable
Chronicle Validation Rules Version or artifact state
Chronicle Validation Sequence Version or artifact state
Controlled Values applicable at Validation time
```

This allows future reviewers to interpret historical Validation under the rules that actually governed it.

---

# Rule-by-Rule Results

The Validation Record should preserve results for each applicable:

```text
CHR-VAL-*
```

rule.

Permitted procedural rule results are:

```text
PASS
FAIL
Not Applicable
Not Evaluated
```

Only the overall Validation outcome is:

```text
PASS
FAIL
```

`Not Evaluated` requires an identified prerequisite failure.

`Not Applicable` requires that the rule genuinely does not govern the Entry.

---

# Overall Result

The Validation Record must preserve one authoritative overall result:

```text
PASS
```

or:

```text
FAIL
```

No numerical score substitutes for the result.

---

# Failure Details

When the result is FAIL, the Validation Record should preserve:

```text
failed CHR-VAL rule
affected field / domain
failure description
blocking condition
required corrective action
Reverification requirement
Revalidation scope
```

The purpose is operational correction and future auditability.

---

# PASS Details

When the result is PASS, the Validation Record should preserve enough information to demonstrate:

```text
all applicable blocking rules passed
no unresolved prerequisite failure remained
Publication Readiness passed
```

PASS does not require recording meaningless boilerplate beyond what is necessary to reconstruct the decision.

---

# Validation Date and Time

The record should preserve a Validation timestamp.

This timestamp is distinct from:

```text
Event Date
Entry creation time
Source retrieval time
Publication time
Correction date
```

Validation time identifies when the conformance decision was made.

---

# Validation Method

The Validation Record should identify how Validation was performed.

Examples:

```text
machine schema validation
institutional checklist review
combined machine + institutional validation
targeted Revalidation
full Revalidation
```

Where machine tooling is used, the artifact may preserve the relevant output or tool context.

---

# Validator or Workflow Identity

Early Chronicle implementation does not require a complex reviewer-role system.

The Validation Record should preserve enough information to identify:

```text
validator
workflow
automation
institutional process
```

responsible for the result.

A formal Controlled Value set for reviewer roles should remain deferred until operational use demonstrates a need.

---

# Revalidation Record

A later Revalidation should not silently overwrite the earlier Validation result.

Chronicle should preserve:

```text
prior Validation result
reason for Revalidation
changed domains
rules rerun
new Validation date
new overall result
```

If maintained in separate artifacts, the relationship should be traceable.

---

# Validation Artifact Naming

During early production, a Validation artifact may use a descriptive filename tied to the Entry and Version.

Example pattern:

```text
CHR-2026-0001-v1-validation.md
```

or another consistent operational naming convention adopted by the Production Procedure.

This filename is not a canonical identifier.

It is an artifact locator.

The final naming convention should be confirmed when the first production Entry is created.

---

# Public vs Internal Validation Information

Not every internal Validation detail must automatically become public.

Chronicle may publish enough information to establish:

```text
validated Entry Version
Validation result
Validation date
public Validation artifact reference where appropriate
```

while retaining internal procedural detail where publication adds no historical value.

Public disclosure decisions belong to Chronicle Publication procedure.

---

# Relationship to Chronicle Entry

The Validation Record describes a production decision about the Entry.

It does not become the Entry.

Therefore:

```text
Chronicle Entry
        ≠
Validation Record
```

and:

```text
Occurrence
        ≠
Validation Record
```

Validation remains supporting institutional evidence about Chronicle's handling of its own object.

---

# Relationship to Verification

Verification findings and Validation results must remain distinct.

Verification may establish:

```text
verified
verified_with_limitations
unresolved
```

according to Chronicle Verification rules.

Validation records:

```text
PASS
FAIL
```

for conformance.

The Validation artifact may reference Verification State.

It should not duplicate the full Verification process unless needed to explain a failure.

---

# Relationship to Publication

A Validation artifact may support the Publication decision.

Conceptually:

```text
Validation Artifact
        ↓
Overall PASS
        ↓
Entry Eligible for Publication Decision
```

Publication may preserve a reference to the Validation artifact.

Publication does not replace the Validation artifact.

---

# Relationship to Correction and Versioning

If Validation failure causes a material Correction:

```text
Validation FAIL
        ↓
Correction
        ↓
New Entry Version where required
        ↓
Reverification
        ↓
Revalidation
```

The new Validation result should attach to the resulting Entry Version.

The earlier Validation result should remain reconstructable.

---

# No New Canonical Identifier

The initial Validation implementation does not require an identifier such as:

```text
CVAL-2026-0001
```

or:

```text
CHR-VALREC-2026-0001
```

Introducing such an identifier would imply an independently governed canonical object.

That level of architecture is not currently justified.

---

# Conditions That Could Justify a Future Canonical Validation Record

Chronicle should revisit this decision only if operations demonstrate recurring needs such as:

* multiple independent Validation decisions for one Entry Version;
* external systems needing durable Validation references;
* formal public citation of Validation events;
* dedicated Validation lifecycle;
* Validation Corrections independent of Entry Corrections;
* machine-to-machine Validation exchange;
* independent validator identity or signature requirements;
* significant Validation evidence packages;
* legal or governance requirements for separate Validation records.

If those conditions emerge, Chronicle may conduct a dedicated architectural review.

---

# Initial Production Decision

For the first production Chronicle Entry:

```text
Validation result
        ↓
preserved in an internal Validation artifact
        ↓
associated directly with the exact Entry Version
        ↓
referenced by Publication metadata when useful
```

No new canonical Validation object is created.

No Base Schema change is required at this stage.

---

# Recording Principle

> Record the Validation. Do not inflate the object model.

And:

> Preserve enough to reconstruct why an Entry passed or failed.

---

# Status

**Initial Chronicle Validation Record architecture established for Phase VIII.**

The current decision is:

```text
Full Validation detail
  → internal Validation artifact

Minimal publication-facing Validation information
  → publication metadata where useful

Full Validation embedded in Chronicle Entry
  → not required

Dedicated canonical Validation Record
  → deferred pending operational evidence
```

This structure should be tested during the first Chronicle Entry dry run and first production Entry before any additional Validation object architecture is frozen.
