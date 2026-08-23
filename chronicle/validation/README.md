# Chronicle Validation

## Purpose

Satoshium Chronicle Validation defines the institutional and machine-readable requirements used to determine whether a Chronicle Entry conforms to the rules governing its current representation.

Validation is a Chronicle function.

It tests whether the Entry has been implemented correctly according to the applicable:

* Chronicle Base Schema
* Event-Type Profile
* Identifier rules
* Controlled Values
* Relationship rules
* Provenance requirements
* Versioning and Correction requirements
* publication prerequisites
* Suite authority boundaries
* other governing Chronicle requirements

Validation applies to the Chronicle Entry.

It does not transfer authority from another Satoshium Suite institution.

---

# Core Principle

Chronicle Validation asks:

> Does this Chronicle Entry conform to the institutional and machine-readable requirements governing this Entry Version?

The governing distinction is:

```text
Schema
  defines structure.

Verification
  reviews Chronicle's historical representation.

Validation
  tests conformance.

Publication
  determines public production state.
```

Therefore:

```text
Schema ≠ Verification ≠ Validation ≠ Publication
```

These functions are connected.

They are not interchangeable.

---

# Institutional Position

Validation occurs after Chronicle has constructed and Verified the current Entry representation and before the Entry proceeds through the publication gate.

Conceptually:

```text
Occurrence Identified
        ↓
Preservation Eligibility Assessed
        ↓
Entry Drafted
        ↓
Sources / Authoritative References Linked
        ↓
Evidence / Provenance / Relationships Assembled
        ↓
Verification Performed
        ↓
Validation Performed
        ↓
Publication Decision
        ↓
Published / Maintained / Preserved
```

Validation is therefore neither the first decision nor the final act.

---

# Validation Scope

Chronicle Validation evaluates the current Chronicle Entry Version against the requirements applicable to that Entry.

The Validation scope includes:

```text
Entry Identity
Schema Conformance
Event-Type Profile Conformance
Controlled Values
Required and Conditional Fields
Authoritative References
Date and Time Formatting
Relationship Integrity
Provenance
Version and Correction Consistency
Publication Readiness
Authority Boundaries
```

Validation should evaluate only requirements that actually govern the Entry.

It should not create additional obligations merely for completeness or architectural symmetry.

---

# What Validation Is

Chronicle Validation is:

* a conformance review;
* a publication-readiness control feeding the separate Chronicle Publication Gate;
* a machine-readable and institutional review process;
* a check against the requirements governing one Entry Version;
* a mechanism for identifying blocking implementation defects;
* a basis for determining whether an Entry may proceed toward publication;
* a repeatable operational control;
* a process that may require revalidation after material change.

---

# What Validation Is Not

Chronicle Validation is not:

* Preservation Eligibility;
* Chronicle Verification;
* historical adjudication;
* external Source Authority review;
* Certifier Certification;
* Registry registration;
* Anchor integrity establishment;
* Beacon discovery;
* Attestor attestation;
* Navigator workflow authorization;
* Atlas source adjudication;
* publication itself;
* a numerical trust score;
* authority over another Suite institution.

Validation does not establish that every underlying historical claim is independently true.

Validation establishes whether Chronicle implemented its own current representation according to the governing requirements.

---

# Authority Boundaries

Chronicle validates Chronicle-owned records and Chronicle-owned representation.

Chronicle does not validate another institution's authoritative object as though Chronicle owned that authority.

## Certifier

Certifier remains authoritative for:

* Certification Packages
* certification determinations
* certification lifecycle actions
* certification status
* Certifier evidence and findings
* certification methodology and procedure

Chronicle may validate that:

```text
a required Certifier reference exists
```

and:

```text
the Entry represents that reference correctly
```

Chronicle does not re-certify the subject.

---

## Registry

Registry remains authoritative for:

* SREG Registry Entries
* registration
* cataloging
* Registry metadata
* Registry lifecycle state
* Registry record relationships

Chronicle may validate that a Registry reference:

* is structurally valid;
* is materially appropriate;
* is represented as Registry-owned;
* does not replace the authoritative certification reference where Certifier authority is required.

Chronicle does not re-register the object.

---

## Other Suite Institutions

The same rule applies to:

```text
Anchor
Beacon
Attestor
Navigator
Atlas
```

Chronicle may validate its reference to those authoritative objects.

Chronicle does not absorb their institutional authority.

The governing principle remains:

> Reference does not transfer authority.

---

# Validation Object

The primary Validation object is the current:

```text
Chronicle Entry Version
```

Validation should identify:

```text
entry_id
entry_version
schema_id
schema_version
event_type
event_type_profile where applicable
```

Validation applies to a defined Entry state.

A later material Entry Version may require a new Validation result.

---

# Validation Inputs

A Chronicle Validation should identify the requirements being applied.

Minimum Validation inputs include, where applicable:

```text
Chronicle Entry
Chronicle Base Schema
Chronicle Base Schema Version
Event-Type Profile
Event-Type Profile Version
Chronicle Identifier Specification
Chronicle Controlled Values
Chronicle Relationship rules
Chronicle Provenance requirements
Chronicle Verification State
Chronicle Correction / Versioning rules
Chronicle Publication prerequisites
Suite authority boundaries
Validation procedure or checklist version
```

The specific inputs may vary by Entry Type.

A Validation result is meaningful only when the governing requirements are identifiable.

---

# Validation Outputs

Every material Chronicle Validation should produce a clear result.

The initial outcome model is intentionally minimal:

```text
PASS
FAIL
```

## PASS

PASS means:

```text
All blocking Validation requirements
applicable to the current Entry Version
have been satisfied.
```

PASS permits the Entry to proceed toward the next publication decision.

PASS does not itself publish the Entry.

PASS does not eliminate future revalidation.

---

## FAIL

FAIL means:

```text
One or more blocking Validation requirements
applicable to the current Entry Version
have not been satisfied.
```

FAIL means the current representation should not proceed through the publication gate until the blocking issue is resolved or formally governed.

FAIL does not mean:

* the historical Occurrence did not happen;
* an authoritative external object is invalid;
* the Chronicle Entry must be deleted;
* the prior record may be silently rewritten.

---

# Minimum Validation Record

A material Validation result should preserve enough information to reconstruct what was checked.

Minimum Validation record content should include:

```text
Entry Identifier
Entry Version
Validation Date / Time
Validation Result
Governing Base Schema Version
Applicable Event-Type Profile and Version
Checks Performed
Blocking Failures
Warnings or Notes where retained
Validator / Validation Method
Revalidation Requirement where applicable
Supporting Validation Artifact Reference when one exists
```

The exact storage location of Validation results may remain operationally lightweight during early production.

A separate canonical Validation Record is not required unless production use proves the need.

---

# Validation Sequence

The standard Chronicle Validation sequence is:

```text
Entry Received for Validation
        ↓
Identifier Validation
        ↓
Base Schema Validation
        ↓
Event-Type Profile Validation
        ↓
Controlled Values Validation
        ↓
Required / Conditional Field Validation
        ↓
Authoritative Reference Validation
        ↓
Date / Time Validation
        ↓
Relationship Integrity Validation
        ↓
Provenance Validation
        ↓
Version / Correction Consistency Validation
        ↓
Verification Dependency Validation
        ↓
Authority Boundary Integrity Validation
        ↓
Human / Machine Consistency Validation
        ↓
Publication Readiness Validation
        ↓
Validation Result Recorded
        ↓
Separate Publication Gate
```

A Validation may stop early when a blocking failure makes later checks impossible.

Where practical, however, Chronicle should identify all material failures in one validation pass rather than forcing repeated one-error-at-a-time correction cycles.

---

# 1. Identifier Validation

Identifier Validation confirms that Chronicle Entry identity conforms to the approved Identifier architecture.

Minimum requirements:

```text
entry_id is present
entry_id matches CHR-YYYY-NNNN
identifier namespace is Chronicle
identifier is not reused
identifier remains stable across Entry Versions
identifier assignment year is not confused with Event Date
Event Type is not encoded into permanent identity
```

Example pattern:

```text
^CHR-[0-9]{4}-[0-9]{4}$
```

Pattern validation does not by itself establish issuance or uniqueness.

Operational checks must also confirm that the identifier has not been duplicated or reused.

---

# 2. Base Schema Validation

Every production Chronicle Entry must conform to the applicable Chronicle Base Schema.

Minimum requirements:

```text
schema_id is present
schema_id is recognized
schema_version is present
schema_version is supported
all universal Required fields are present
field names are valid
field types are valid
formats are valid
conditional Base fields are used correctly
unapproved additional fields are absent
machine-readable Entry parses successfully
```

The current Base Schema is:

```text
/chronicle/schemas/chronicle-base-schema.json
```

The Base Schema defines universal Chronicle Entry structure.

---

# 3. Event-Type Profile Validation

When an approved Event-Type Profile applies, the Entry must conform to that Profile in addition to the Base Schema.

Conceptually:

```text
Chronicle Base Schema
        +
Event-Type Profile
        =
Specialized Chronicle Entry Validation
```

Minimum requirements:

```text
correct Profile is selected
Profile identifier is valid
Profile Version is known
Profile-specific Required fields are present
Profile-specific Controlled Values are valid
Profile-specific authoritative references are satisfied
Profile-specific date restrictions are satisfied
Profile-specific Provenance requirements are satisfied
Profile-specific Relationship rules are satisfied
```

For certification-related Entries, the current production Profile is:

```text
/chronicle/schemas/certification-event-profile/
```

---

# 4. Controlled Values Validation

Fields governed by Controlled Values must use approved Chronicle values.

Validation should confirm current approved values for applicable fields including:

```text
Event Type
Verification State
Lifecycle State
Publication State
Relationship Type
Source Type
Evidence Type
Correction Type
```

A free-form alternative must not be substituted where a governed Controlled Value is required.

Deprecated values should be handled according to future migration or compatibility rules rather than silently rewritten.

---

# 5. Required and Conditional Field Validation

Validation must distinguish:

```text
Required
Conditional
Optional
```

## Required

Required fields must always be present for the governing schema or Profile.

## Conditional

Conditional fields must be present when the condition requiring them applies.

Examples include:

```text
event_type_profile
originating_system
authoritative_record_references
published_at
limitations
prior_version_reference
correction_references
```

depending on the Entry.

## Optional

Optional fields may be omitted without causing Validation failure unless another applicable rule makes them necessary.

---

# 6. Authoritative Reference Validation

Chronicle Validation must confirm required authoritative references.

Minimum requirements:

```text
required authoritative reference exists
referenced object is identifiable
owning institution is represented correctly where required
reference form conforms to schema
reference does not transfer authority
Profile-specific authority requirements are satisfied
material Registry or other Suite relationships are represented when required
```

For Certification Event-Type Profile Entries, at least one authoritative reference must explicitly identify:

```text
system: certifier
```

This does not make Chronicle the certification authority.

It proves that Chronicle has identified whose authority it is referencing.

---

# 7. Date and Time Validation

Chronicle uses several distinct temporal concepts.

Validation should confirm they are formatted correctly and not collapsed.

Potential fields include:

```text
event_date
entry_created_at
retrieved_at
published_at
updated_at
Correction date
Version date
```

Minimum rules include:

```text
Event Date represents the Occurrence
Entry creation date represents Chronicle creation
retrieval date represents access / capture
publication date represents public release
Correction date represents correction action
Version date represents resulting preserved state when recorded
```

An Entry should not substitute one timestamp for another merely because the correct value is unknown.

Profile-specific rules may strengthen the Base Schema.

For example:

```text
Base Schema
  may permit event_date = null

Certification Event-Type Profile
  does not permit event_date = null
```

---

# 8. Relationship Integrity Validation

Relationship Validation confirms that Chronicle relationships are structurally and semantically coherent.

Minimum requirements:

```text
Relationship Type is approved
target is identifiable
target system is represented where necessary
direction is correct
inverse relationships are coherent where represented
duplicates are avoided
contradictions are resolved or documented
Relationship does not imply unsupported causation
Relationship does not transfer authority
```

Important distinctions include:

```text
Precedes ≠ Causes
Supersedes ≠ Deletes
References ≠ Owns
Related To ≠ Authoritative For
```

---

# 9. Provenance Validation

Provenance Validation confirms that Chronicle preserves how information entered the record.

Minimum requirements:

```text
Origin
Acquisition / Access Method
Capture / Retrieval Date
Source or Authoritative Record Reference when required
Material Provenance Limitations when applicable
```

Where applicable, Validation may also review:

```text
transfer_history
transformation_history
preservation_path
integrity_metadata
```

The governing principle is:

> Preserve origin. Preserve path. Preserve limitations.

Unknown Provenance must not be converted into known Provenance merely to satisfy Validation.

Instead, the limitation should remain visible.

---

# 10. Version and Correction Consistency Validation

Where an Entry has been materially changed, Validation should confirm:

```text
Entry identity remains stable
Entry Version increments appropriately
prior Version remains identifiable
formal Correction exists where required
Correction reason is preserved
affected fields are identifiable
resulting Version is identified
Reverification occurred where required
Revalidation occurs where required
publication lineage remains traceable
```

The governing rules remain:

```text
Correction explains why Chronicle changed its record.
Version preserves the resulting state.
```

and:

> Correct forward. Preserve backward.

---

# 11. Publication Readiness Validation

Publication Readiness is the final Validation-domain readiness test.

It is not the separate Chronicle Publication Gate.

`CHR-VAL-011` tests whether the Entry satisfies publication prerequisites from a Validation standpoint. The Publication Gate makes the separate institutional decision to approve or withhold Publication.

Before an Entry can proceed toward publication, Validation should confirm:

```text
Base Schema PASS
Event-Type Profile PASS where applicable
Identifier requirements PASS
Controlled Values PASS
Required and Conditional fields PASS
Authoritative references PASS
Date / Time requirements PASS
Relationship integrity PASS
Provenance PASS
Version / Correction consistency PASS where applicable
Verification State satisfies publication requirements
No unresolved blocking Validation failure remains
Authority boundaries are represented correctly
```

A Validation PASS means:

```text
Eligible to proceed to the Publication Gate
```

It does not mean:

```text
Automatically published
```

---

# Validation and Verification

Verification and Validation remain distinct.

## Verification

Verification asks:

> Is Chronicle's historical representation adequately supported and internally reviewable?

Verification may review:

* Entry identity
* authoritative references
* Sources
* Evidence
* Event Dates
* Relationships
* Provenance
* Historical Context
* limitations

## Validation

Validation asks:

> Does the current Entry Version conform to the requirements governing it?

Verification evaluates representation.

Validation evaluates conformance.

Neither replaces the other.

---

# Validation and Publication

Validation precedes publication.

Conceptually:

```text
Verification Complete
        ↓
Validation PASS
        ↓
CHR-VAL-011 Publication Readiness PASS
        ↓
Publication Gate
        ↓
Approved for Publication / Publication Withheld
        ↓
Publication when approved
```

Publication may still be withheld after Validation PASS for reasons governed by Chronicle Publication procedure.

Validation therefore does not itself change:

```text
publication_state
```

unless the production procedure explicitly performs that later action.

---

# Failure Handling

Validation failure should be explicit and actionable.

A FAIL result should identify:

```text
failed requirement
affected field / rule
blocking condition
required correction or review
whether Reverification is required
whether full or targeted Revalidation is required
```

A failed Entry should ordinarily return to the appropriate production step.

Examples:

```text
Identifier failure
  → identifier correction / assignment review

Schema failure
  → Entry construction correction

Profile failure
  → classification or Profile-specific correction

Authoritative reference failure
  → reference acquisition / correction

Provenance failure
  → provenance completion or limitation recording

Relationship failure
  → relationship correction

Publication-readiness failure
  → publication prerequisite completion
```

---

# Validation Failure Does Not Erase History

Validation failure must not trigger silent historical deletion.

A FAIL result does not authorize:

```text
deleting the Occurrence
rewriting prior published history silently
removing prior material Entry Versions
altering external authoritative records
```

If a published Entry later fails Validation:

```text
Failure Identified
        ↓
Entry Returned for Review
        ↓
Correction / New Version where material
        ↓
Reverification
        ↓
Revalidation
        ↓
Republish / Maintain / Withdraw as governed
```

Prior material states remain preserved.

---

# Revalidation

Revalidation may be required after:

* material Entry correction;
* new Entry Version;
* Event Type correction;
* authoritative-reference change;
* Source or Evidence change affecting the representation;
* Relationship change;
* Provenance correction;
* schema migration;
* Event-Type Profile migration;
* material Controlled Value change;
* publication-state change where prerequisites must be reevaluated;
* discovery of a prior Validation defect.

Revalidation may be:

```text
Targeted
```

or:

```text
Full
```

depending on the scope of change.

Targeted Revalidation should be used only when Chronicle can demonstrate that unaffected domains remain valid.

---

# Machine Validation

Machine Validation should enforce requirements wherever a stable machine-readable contract exists.

Current examples include:

```text
JSON Schema Draft 2020-12
CHR identifier pattern
required fields
field types
date / time formats
Controlled Value enumerations
Event-Type Profile constraints
conditional field requirements
structured authoritative references
Relationship structures
Provenance structures
```

Machine Validation is necessary but not sufficient.

A schema cannot independently determine every institutional condition.

---

# Institutional Validation

Institutional Validation evaluates requirements that cannot be established reliably by schema alone.

Examples include:

```text
identifier uniqueness
authority ownership
material relevance of a Registry relationship
semantic correctness of Relationship direction
whether an authoritative reference is genuinely authoritative
whether Historical Context misstates an external determination
whether Provenance limitations are materially complete
whether Verification State is sufficient for publication
whether a Correction requires a new Entry Version
```

Institutional Validation should remain explicit rather than being hidden behind machine checks.

---

# Human and Machine Alignment

Where Chronicle publishes both human-readable and machine-readable representations, Validation should confirm that material fields agree.

Potential comparison domains include:

```text
Entry Identifier
Entry Version
title
summary
Event Type
Event Date
Historical Context
authoritative references
Relationships
Provenance
Verification State
Lifecycle State
Publication State
Correction references
Version references
publication date
```

A Chronicle Entry should not be considered publication-ready when its official forms materially disagree.

---

# Validation Warnings

The initial Chronicle Validation outcome remains:

```text
PASS
FAIL
```

Chronicle may preserve warnings or informational notes without creating additional official Validation States.

Examples:

```text
non-blocking limitation
future maintenance note
reference availability concern
known but acceptable archival constraint
```

Warnings should not be allowed to obscure a blocking failure.

If a requirement is blocking:

```text
FAIL
```

---

# Exceptions

A formal Validation exception should be rare.

An exception should require:

```text
identified requirement
reason for exception
authority approving exception
scope
effective period if limited
risk / limitation
publication effect
revalidation requirement
```

An exception should not be used to bypass fundamental authority boundaries or canonical identity rules.

---

# Validation Version Context

Validation results should remain associated with the requirement versions that governed them.

At minimum, Chronicle should be able to determine:

```text
which Base Schema Version
which Event-Type Profile Version
which Entry Version
which Controlled Values
which Validation Procedure
```

were applied.

A later schema or procedure change does not automatically make an older Validation invalid.

Historical interpretation should preserve the standards that applied at the time.

---

# Validation and Schema Evolution

When a schema changes, Chronicle should determine whether existing Entries require:

```text
No action
Targeted review
Revalidation
Migration
New Entry Version
```

A backward-compatible schema clarification should not automatically trigger unnecessary historical rewriting.

A breaking change may require migration guidance.

Older Entries should remain interpretable under their original Schema Version.

---

# Validation and Event-Type Profile Evolution

An Event-Type Profile may evolve independently of the Base Schema.

Validation should preserve:

```text
Profile identity
Profile Version
Entry Version
Base Schema Version
```

A new Profile Version does not automatically require a new Entry Version unless Chronicle materially changes the Entry representation.

If migration changes material Entry content, normal Versioning and Correction rules apply.

---

# Validation and Preservation Eligibility

Preservation Eligibility and Validation remain separate.

```text
Preservation Eligibility
  Should Chronicle preserve this Occurrence?

Validation
  Does the resulting Entry conform?
```

An Occurrence may be eligible for preservation while its first drafted Entry fails Validation.

That means:

```text
The Occurrence remains eligible.
The representation requires correction.
```

Validation should not reopen Preservation Eligibility unless the failure reveals that the Entry was created under an invalid or mistaken eligibility premise.

---

# Validation and Historical Significance

Historical Significance is not a Validation score.

Validation should not attempt to calculate whether history is important enough through a numerical threshold.

Historical Significance belongs primarily to Preservation Eligibility and Historical Context.

Validation may confirm that required Historical Context exists.

It should not replace Chronicle's substantive preservation judgment with a machine score.

---

# Validation and Evidence

Evidence may support Chronicle Verification.

Validation may confirm that:

```text
required Evidence references exist
Evidence structures conform
Evidence types are approved
Evidence references resolve where required
```

Validation does not convert Evidence into the historical Occurrence.

The principle remains:

> Evidence supports the historical representation. It does not become the event.

---

# Validation and Sources

Validation may confirm:

```text
required Source references exist
Source Type is valid where structured
Source identity is traceable
Source references are represented correctly
Source authority is not overstated
```

A Source is not necessarily an authoritative record.

Chronicle must preserve the distinction among:

```text
Source
Evidence
Authoritative Record
Provenance
```

---

# Validation and Trust

Chronicle does not use Validation as a universal numerical trust score.

Trust remains reviewable through:

```text
Preservation Eligibility
Authoritative References
Sources
Evidence
Provenance
Verification
Validation
Corrections
Version lineage
Publication history
Preservation
```

Validation contributes to trust by proving conformance.

It does not replace the other trust components.

---

# Certification Event-Type Profile Validation

The first production Event-Type Profile is:

```text
Certification Event-Type Profile
```

A certification-related Chronicle Entry must satisfy:

```text
Chronicle Base Schema
        +
Certification Event-Type Profile
```

Current Profile requirements include:

```text
event_type_profile = certification-event-profile
originating_system = certifier
approved Certification Event Type
non-null event_date
authoritative_record_references present
at least one structured reference with system: certifier
Certification-specific Provenance
```

A related Registry reference becomes required only when the corresponding SREG exists and is materially relevant under Chronicle rules.

The Profile does not duplicate Certification Package contents.

---

# Initial Validation Workflow

The initial operational Validation workflow is:

```text
1. Receive current Entry Version.
2. Confirm governing Base Schema.
3. Confirm applicable Event-Type Profile.
4. Validate Entry Identifier.
5. Run machine-readable schema validation.
6. Validate Controlled Values.
7. Validate Required and Conditional fields.
8. Validate authoritative references.
9. Validate date and time fields.
10. Validate Relationships.
11. Validate Provenance.
12. Validate Version / Correction consistency where applicable.
13. Confirm Verification Dependency.
14. Validate Authority Boundary Integrity.
15. Validate Human / Machine Consistency where applicable.
16. Validate CHR-VAL-011 Publication Readiness.
17. Record PASS or FAIL.
18. Return FAIL Entries for correction.
19. Permit PASS Entries to proceed to the separate Publication Gate.
```

This sequence should remain repeatable.

---

# Minimum Validation Requirements

Every production Chronicle Entry must pass, at minimum:

```text
Identifier Validation
Base Schema Validation
Controlled Values Validation
Required Field Validation
Date / Time Validation
Provenance Validation
Publication Readiness Validation
```

Where applicable, it must also pass:

```text
Event-Type Profile Validation
Authoritative Reference Validation
Relationship Integrity Validation
Source Validation
Evidence Validation
Correction Validation
Version Validation
Revalidation Requirements
```

The applicable requirement set is determined by the Entry's actual structure and governing rules.

---

# Production Rule

No production Chronicle Entry should be presented as publication-ready when a known blocking Validation failure remains unresolved.

Conceptually:

```text
Validation FAIL
        ↓
Return for Correction / Completion / Review

Validation PASS
        ↓
Eligible for Publication Decision
```

---

# Validation Artifact Strategy

Chronicle should initially avoid creating unnecessary Validation object architecture.

Production has now established a durable Markdown Validation artifact tied directly to the Entry Version.

The first production naming convention is:

```text
CHR-YYYY-NNNN-vN-validation.md
```

For `CHR-2026-0001` Entry Version 1:

```text
CHR-2026-0001-v1-validation.md
```

The artifact may be published alongside the Entry when its durable review value justifies public preservation. It remains supporting procedural documentation rather than a separate canonical Chronicle object.

A dedicated canonical Validation Record should be created only if production experience demonstrates that Validation needs durable independent identity and lifecycle.

The architecture should remain:

> Minimum necessary structure first.

---

# Relationship to Phase VII

Phase VII established the production schema foundation.

It included:

```text
Chronicle Base Schema
Certification Event-Type Profile
Two-layer machine-readable validation
```

The Phase VII schema validation demonstrated that Chronicle can enforce structural constraints through machine-readable rules.

Phase VIII extends that capability into a complete operational Validation procedure.

The distinction is:

```text
Phase VII
  Proved the schema stack can validate.

Phase VIII
  Defines how Chronicle performs Validation as an institutional process.
```

---

# Relationship to Entry Production Procedure

Chronicle Validation is one stage of the larger Entry Production Procedure.

The production sequence is expected to be:

```text
Identify Occurrence
        ↓
Assess Preservation Eligibility
        ↓
Collect Authoritative References
        ↓
Classify Event Type
        ↓
Select Event-Type Profile
        ↓
Assign Identifier
        ↓
Create Entry
        ↓
Establish Relationships
        ↓
Record Sources / Evidence / Provenance
        ↓
Verify
        ↓
Validate
        ↓
CHR-VAL-011 Publication Readiness
        ↓
Publication Gate
        ↓
Approve / Withhold Publication
        ↓
Publish when approved
        ↓
Preserve
```

The Entry Production Procedure will define how Chronicle executes this sequence consistently.

---

# Failure Escalation

A blocking Validation failure should be routed to the institutional function capable of correcting it.

Examples:

```text
Identifier issue
  → Identifier review

Schema issue
  → Entry construction

Classification issue
  → Event Type / Profile review

Reference issue
  → authoritative-reference review

Provenance issue
  → Provenance review

Verification insufficiency
  → Verification

Correction / Version issue
  → Correction / Versioning process

Publication prerequisite issue
  → publication preparation
```

Validation identifies the defect.

It does not necessarily perform the corrective action itself.

---

# Auditability

Chronicle Validation should be reviewable after the fact.

A future reviewer should be able to determine:

```text
What Entry Version was validated?
What requirements applied?
What checks were performed?
What passed?
What failed?
What was corrected?
Was Reverification required?
Was Revalidation performed?
What result permitted publication?
```

Validation should therefore leave enough evidence to reconstruct the decision.

---

# Validation Principle

Chronicle Validation exists to protect the integrity of Chronicle's own production record.

The governing formulation is:

> Validation tests whether Chronicle implemented its own requirements correctly.

And institutionally:

> Validate the Chronicle Entry. Respect the authority of the system that established the underlying action.

---

## Status

**Phase VIII — Chronicle Validation institutional specification.**

This document establishes:

* Validation scope;
* authority boundaries;
* Validation inputs;
* Validation outputs;
* PASS / FAIL outcomes;
* failure handling;
* Revalidation;
* machine and institutional Validation;
* the standard Validation sequence;
* minimum Validation requirements;
* the relationship among Schema, Verification, Validation, and Publication.

The Phase VIII operational dry run using `SC-CERT-2026-0001` and simulated candidate `CHR-2026-0001` completed with an overall result of:

```text
PASS
```

No Validation architecture redesign was required.

This specification has now been exercised in production through `CHR-2026-0001` Entry Version 1.

Production result:

```text
Verification: verified
Validation: PASS
CHR-VAL-011 Publication Readiness: PASS
Publication Gate: APPROVED
Publication State: published
Published At: 2026-08-22T08:38:00-07:00
```

Chronicle Validation is therefore operational rather than awaiting first production use.
