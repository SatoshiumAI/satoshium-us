# Satoshium Attestor — Validation Rule Catalog

**Version:** 0.1  
**Stage:** Implementation & Validation  
**Applies to:** Attestation (`ATT`) and Trust Statement (`TRST`) validation  
**Parent requirements:** `attestor-validation-requirements.md`

## 1. Purpose

This catalog translates established Attestor architecture into stable, numbered validation rules suitable for later machine implementation.

A rule appears here only when the governing architecture supports a validation requirement. Institutional principles that require substantive human judgment remain identified as review-dependent rather than being falsely reduced to syntax.

`Principle → Rule → Normative Requirement → Validation Rule → Validation Result`

Validation does not perform Evaluation, Eligibility determination, Conformance determination, publication authorization, or substantive truth adjudication.

---

## 2. Rule Classes

- **MACHINE** — deterministically executable when the canonical machine representation is fixed.
- **CONDITIONAL** — executable when the relevant field/object/context exists or a declared profile makes it applicable.
- **REVIEW** — requires governed human/institutional judgment; machine validation may verify that required review context is represented but may not decide the substance.
- **DEFERRED** — architecture establishes the requirement, but exact machine representation is not yet fixed.

---

## 3. Representation / Syntax Rules

### VAL-REP-001 — Parseable Representation
**Class:** MACHINE  
The validation target must be parseable under the serialization declared by its applicable schema/profile.

**Failure condition:** Representation cannot be parsed.  
**Architecture effect:** No deeper structural validation should be asserted for an unparseable representation.

### VAL-REP-002 — Declared Object Profile
**Class:** MACHINE  
The target must resolve to a recognized Attestor validation profile: canonical Attestation, canonical Trust Statement, or an adopted specialized Attestation profile.

**Failure condition:** Object/profile cannot be identified or is noncanonical.

### VAL-REP-003 — Legacy Trust Signal Exclusion
**Class:** MACHINE  
A legacy Trust Signal representation must not validate as a canonical Attestor object.

**Failure condition:** A Trust Signal is presented under canonical ATT/TRST validation as though it were an Attestor canonical object.

---

## 4. Identifier Rules

### VAL-STR-001 — Attestation Identifier Family
**Class:** MACHINE  
A canonically created Attestation must use `ATT-YYYY-NNNN`.

### VAL-STR-002 — Trust Statement Identifier Family
**Class:** MACHINE  
A canonically created Trust Statement must use `TRST-YYYY-NNNN`.

### VAL-STR-003 — Four-Digit Creation Year
**Class:** MACHINE  
`YYYY` must be a four-digit year representing the object's canonical creation year.

### VAL-STR-004 — Four-Digit Sequence
**Class:** MACHINE  
`NNNN` must be a four-digit sequence within the applicable object family and creation year.

### VAL-STR-005 — Object-Class / Prefix Coherence
**Class:** MACHINE  
An Attestation must not carry a `TRST` identifier and a Trust Statement must not carry an `ATT` identifier.

### VAL-STR-006 — Canonical Identifier Uniqueness
**Class:** CONDITIONAL  
Within the authoritative Attestor identifier register, one canonical identifier must resolve to one and only one canonical object.

**Failure condition:** Duplicate assignment, reuse, or reassignment is detected.

### VAL-STR-007 — Pre-Creation Identifier Boundary
**Class:** CONDITIONAL  
Candidate/preparation material must not be represented as possessing a canonically assigned ATT/TRST identity before canonical Creation.

### VAL-STR-008 — Source Identifier Preservation
**Class:** CONDITIONAL  
Referenced source identifiers must remain distinguishable from Attestor canonical identifiers and must not be reissued as ATT/TRST identities.

---

## 5. Controlled Semantic Rules

### VAL-SEM-001 — Attestation Type Vocabulary
**Class:** MACHINE  
When `attestation_type` is represented, its value must be one of:

`identity`, `evidence`, `source-provenance`, `verification-related`, `relationship-condition`, `correction-supersession`.

### VAL-SEM-002 — Lifecycle Vocabulary
**Class:** MACHINE  
Lifecycle state must be one of:

`draft`, `active`, `superseded`, `withdrawn`, `retired`.

`inactive`, `review`, and `correction` must not validate as canonical lifecycle-state values.

### VAL-SEM-003 — Publication Vocabulary
**Class:** MACHINE  
Publication state must be `unpublished` or `published`.

### VAL-SEM-004 — Evaluation Outcome Vocabulary
**Class:** MACHINE  
A represented Evaluation Outcome must be one of:

`supported`, `partially-supported`, `not-supported`, `contradicted`, `indeterminate`.

### VAL-SEM-005 — Provenance Mode Vocabulary
**Class:** MACHINE  
A represented provenance mode must be:

`direct`, `referenced`, or `derived`.

### VAL-SEM-006 — Relationship Vocabulary
**Class:** MACHINE  
A canonical relationship type must be:

`supports`, `references`, `derived-from`, `evaluates`, `results-in`, `supersedes`, `corrects`, or `related-to`.

### VAL-SEM-007 — Noncanonical Trust/Confidence Vocabulary
**Class:** MACHINE  
Canonical ATT/TRST validation must not require or interpret legacy Trust Signal direction, signal strength, reputation, or confidence-score vocabularies as canonical Attestor semantics.

---

## 6. Attestation Rules

### VAL-ATT-001 — Distinct Attestation Identity
**Class:** MACHINE  
An Attestation is a distinct canonical object and must not share the canonical identity of a resulting Trust Statement.

### VAL-ATT-002 — Attesting Authority Identifiable
**Class:** CONDITIONAL  
An Attestation must preserve enough authority context to identify the party or governed source responsible for its assertion.

### VAL-ATT-003 — Authority-to-Assertion Context
**Class:** CONDITIONAL  
The relationship between the Attesting Authority and the assertion must be represented sufficiently to remain understandable.

### VAL-ATT-004 — Attestation Scope Preserved
**Class:** CONDITIONAL  
The Attestation must preserve the scope that bounds its assertion.

### VAL-ATT-005 — Attestation Provenance Preserved
**Class:** CONDITIONAL  
The Attestation must preserve enough provenance to identify assertion origin, attributable source/authority, entry into Attestor, and material governed references.

### VAL-ATT-006 — Material Limitations Preserved
**Class:** CONDITIONAL  
Material limitations applicable to the Attestation must be representable and must not be silently discarded.

### VAL-ATT-007 — Attestation Is Not Trust Statement
**Class:** MACHINE  
An Attestation representation must not use the Trust Statement's bounded conclusion as a substitute for the governed assertion/evaluation distinction.

**Implementation note:** Exact ATT field names/cardinalities remain blocked on normalization of the canonical Attestation machine schema.

---

## 7. Trust Statement Rules

### VAL-TRST-001 — Bounded Conclusion Present
**Class:** MACHINE once schema cardinality is fixed  
A canonical Trust Statement must represent a bounded Attestor conclusion.

### VAL-TRST-002 — Conclusion / Outcome Separation
**Class:** MACHINE  
`bounded_conclusion` and `evaluation.outcome` must remain structurally distinct.

### VAL-TRST-003 — Attestor Attribution
**Class:** MACHINE  
A Trust Statement must preserve Attestor attribution and its Attestor authority context.

### VAL-TRST-004 — Evaluation Outcome Present
**Class:** MACHINE once schema cardinality is fixed  
The Trust Statement must preserve the governed Evaluation Outcome that informed its conclusion.

### VAL-TRST-005 — Evaluation Basis Traceable
**Class:** CONDITIONAL  
The Trust Statement must remain traceable to its evaluation basis.

### VAL-TRST-006 — Supporting Attestation Traceability
**Class:** CONDITIONAL  
Applicable supporting Attestation reference(s) must remain traceable from the Trust Statement/evaluation basis.

### VAL-TRST-007 — Applicable Rules / Methodology Context
**Class:** CONDITIONAL  
The evaluation context must preserve applicable Attestor rules or methodology context sufficiently for review.

### VAL-TRST-008 — Derived Provenance
**Class:** MACHINE / CONDITIONAL  
A Trust Statement produced through Attestor evaluation must preserve derived provenance and its derivation basis.

### VAL-TRST-009 — Relevant Time / State
**Class:** CONDITIONAL  
Where source state or time is material, the Trust Statement/evaluation provenance must distinguish the state evaluated from later state.

### VAL-TRST-010 — Material Conflict Preservation
**Class:** CONDITIONAL  
Material conflicts affecting interpretation must remain represented or traceably recorded.

### VAL-TRST-011 — Material Exclusion Preservation
**Class:** CONDITIONAL  
Material exclusions affecting interpretation must remain represented or traceably recorded.

### VAL-TRST-012 — Limitation Preservation
**Class:** CONDITIONAL  
Material limitations must remain visible and traceable.

### VAL-TRST-013 — Uncertainty Preservation
**Class:** CONDITIONAL / REVIEW  
Material uncertainty must be represented where applicable. Machine validation verifies representation; it does not decide whether the substantive degree of uncertainty is correct.

### VAL-TRST-014 — No Universal-Truth Representation
**Class:** REVIEW  
A Trust Statement must remain bounded by scope, basis, limitations, authority, and relevant state and must not represent itself as universal truth.

### VAL-TRST-015 — Trust Statement Is Not Automatic Input Conversion
**Class:** REVIEW  
The representation/process record must not indicate that a single evidence item, certification, verification result, Discovery Signal, historical event, or other input was automatically converted into the Trust Statement without governed Attestor evaluation.

---

## 8. Provenance / Authority Rules

### VAL-PA-001 — Material Input Traceability
**Class:** CONDITIONAL  
Every material input used in evaluation must remain traceable to its source or derivation path.

### VAL-PA-002 — Minimum Provenance Context
**Class:** CONDITIONAL  
Material provenance must preserve enough applicable context to avoid materially ambiguous lineage, including source/origin identity, stable reference when available, provenance mode, authority context, relevant state/time, relationship to evaluation, derivation basis where applicable, and material limitations.

### VAL-PA-003 — Evaluation Provenance
**Class:** CONDITIONAL  
The governed evaluation basis must identify the Attestation evaluated, material eligible inputs considered, applicable rules/methodology, and sufficient process context for review.

### VAL-PA-004 — Provenance Continuity
**Class:** CONDITIONAL  
Publication, lifecycle change, correction, supersession, withdrawal, retirement, or version change must not sever required provenance history.

### VAL-PA-005 — Source-State Preservation
**Class:** CONDITIONAL  
Where source state can change, the historical state used in evaluation must not be silently replaced by a later source representation.

### VAL-PA-006 — Authority Context Preservation
**Class:** CONDITIONAL  
Referenced authority must remain attributable and bounded to its source role, jurisdiction, subject, period, or other material scope.

### VAL-PA-007 — No Authority Transfer
**Class:** REVIEW / CONDITIONAL  
References and relationships must not represent source authority as having migrated to Attestor.

### VAL-PA-008 — Attestor Authority Boundary
**Class:** REVIEW  
Attestor may claim authority for its governed evaluation, Attestor-owned objects, and Trust Statements, but not for canonical objects or institutional acts owned by another source authority.

### VAL-PA-009 — Authority Conflict Preservation
**Class:** CONDITIONAL / REVIEW  
Material conflict among authorities or governed sources must remain available as evaluation context rather than being silently erased.

---

## 9. Relationship Rules

### VAL-REL-001 — Explicit Source and Target
**Class:** MACHINE once serialization is fixed  
A material canonical relationship must identify its source object and target object sufficiently for resolution.

### VAL-REL-002 — Direction Preserved
**Class:** MACHINE / CONDITIONAL  
Canonical relationships are interpreted source → target. Implementations must not silently reverse a directional relationship.

### VAL-REL-003 — `supports` Direction
**Class:** CONDITIONAL  
`supports` means the source object provides material support to the target assertion, evaluation, or conclusion.

### VAL-REL-004 — `references` Does Not Imply Support
**Class:** CONDITIONAL  
A `references` relationship must not be interpreted as `supports` or `derived-from`.

### VAL-REL-005 — `derived-from` Direction
**Class:** CONDITIONAL  
A derived object is the source and its governed basis is the target.

### VAL-REL-006 — `evaluates` Direction
**Class:** CONDITIONAL  
The evaluation is the source and the evaluated Attestation/assertion is the target.

### VAL-REL-007 — `results-in` Direction
**Class:** CONDITIONAL  
The evaluation is the source and the resulting Trust Statement is the target.

### VAL-REL-008 — `supersedes` Direction
**Class:** CONDITIONAL  
The newer governed object is the source and the prior object is the target.

### VAL-REL-009 — `corrects` Direction
**Class:** CONDITIONAL  
The corrective object/change is the source and the prior affected object is the target.

### VAL-REL-010 — Connection Does Not Merge Identity
**Class:** MACHINE / REVIEW  
Related objects must preserve distinct canonical identity.

### VAL-REL-011 — Relationship Does Not Establish Eligibility
**Class:** REVIEW  
A relationship alone must not be treated as an Eligibility determination.

### VAL-REL-012 — Relationship Does Not Transfer Authority
**Class:** REVIEW  
A relationship alone must not transfer source authority or institutional ownership.

---

## 10. Lifecycle Rules

### VAL-LV-001 — Created Object Begins Draft
**Class:** MACHINE / CONDITIONAL  
A canonically created Attestor object begins in `draft` unless a later formally adopted production procedure explicitly establishes another valid creation-state rule.

### VAL-LV-002 — Creation / Activation Separation
**Class:** MACHINE / CONDITIONAL  
Canonical Creation and lifecycle activation must remain distinguishable.

### VAL-LV-003 — Lifecycle / Publication Separation
**Class:** MACHINE  
Lifecycle state and publication state must remain separate governed dimensions.

### VAL-LV-004 — Draft Is Not Active
**Class:** MACHINE  
A `draft` object must not simultaneously be represented as `active` within the same lifecycle-state dimension.

### VAL-LV-005 — Active Meaning
**Class:** REVIEW  
`active` means current governed representation within scope; validation must not interpret it as published, favorable, permanently correct, or immune from review.

### VAL-LV-006 — Non-Active State Distinction
**Class:** MACHINE  
`superseded`, `withdrawn`, and `retired` must remain distinguishable. `inactive` must not replace them as a canonical state.

### VAL-LV-007 — Review Is Activity, Not State
**Class:** MACHINE  
`review` must not validate as a canonical lifecycle state.

### VAL-LV-008 — Correction Is Activity, Not State
**Class:** MACHINE  
`correction` must not validate as a canonical lifecycle state.

### VAL-LV-009 — Review Does Not Silently Change State
**Class:** CONDITIONAL  
A review event alone must not be treated as an implicit lifecycle transition.

### VAL-LV-010 — Historical Identity Preservation
**Class:** CONDITIONAL  
Lifecycle change must preserve canonical identity and traceable governed history.

---

## 11. Versioning / Governed Change Rules

### VAL-LV-011 — Canonical Identity / Version Identity Separation
**Class:** MACHINE  
Canonical identifier and version identity must be represented as distinct concepts.

### VAL-LV-012 — Same-Object Revision Preserves Canonical Identifier
**Class:** CONDITIONAL  
A permitted bounded revision of an existing object must preserve its ATT/TRST canonical identifier.

### VAL-LV-013 — Version Identity Distinguishes Preserved Revision
**Class:** CONDITIONAL  
A preserved governed revision must be distinguishable from other governed states of the same canonical object.

### VAL-LV-014 — No Silent Historical Overwrite
**Class:** CONDITIONAL  
A governed revision must not silently destroy material prior-state history.

### VAL-LV-015 — Material Attestation Change Requires New ATT
**Class:** REVIEW / CONDITIONAL  
A materially different governed assertion requires a new Attestation canonical identity.

### VAL-LV-016 — Material Trust Statement Conclusion Requires New TRST
**Class:** REVIEW / CONDITIONAL  
A materially different bounded conclusion requires a new Trust Statement canonical identity.

### VAL-LV-017 — Material Successor Relationship
**Class:** CONDITIONAL  
When a new canonical object replaces a prior object because essential institutional meaning changed, the successor must preserve the applicable `supersedes` relationship.

### VAL-LV-018 — Correction Reason / Versioning Decision Separation
**Class:** REVIEW  
Correction explains why governed change occurs; versioning determines whether the change remains within the same canonical identity or requires a successor object.

---

## 12. Cross-Cutting Normative Rules

### VAL-NRM-001 — Preserve Attribution
**Class:** CONDITIONAL  
Applicable objects and process records must preserve sufficient attribution for the relevant assertion, source, or Attestor action.

### VAL-NRM-002 — Preserve Provenance
**Class:** CONDITIONAL  
Applicable objects must preserve sufficient provenance for origin, relationship, status, and relevant history.

### VAL-NRM-003 — Preserve Scope
**Class:** CONDITIONAL / REVIEW  
Represented assertion/evaluation/conclusion scope must not be silently broadened beyond its governed basis.

### VAL-NRM-004 — Preserve Authority Boundaries
**Class:** REVIEW  
Attestor must not inherit, replace, or redefine the authority of referenced institutions or external sources.

### VAL-NRM-005 — Preserve Evidence Context
**Class:** CONDITIONAL / REVIEW  
Material evidence context, including limitations, conflict, and source status where applicable, must remain traceable.

### VAL-NRM-006 — Preserve Traceability
**Class:** CONDITIONAL  
Material relationships among Attestations, governed inputs, evaluations, corrections, and Trust Statements must remain sufficiently traceable for review and validation.

### VAL-NRM-007 — Preserve Governed Change
**Class:** CONDITIONAL  
Correction, clarification, withdrawal, supersession, and other governed changes must not silently erase prior state or change provenance.

### VAL-NRM-008 — Distinguish Current / Historical State
**Class:** CONDITIONAL  
Historically relevant prior state must remain distinguishable from the currently effective governed state.

### VAL-NRM-009 — Do Not Claim Universal Truth
**Class:** REVIEW  
Trust Statement language must preserve its bounded institutional character.

### VAL-NRM-010 — Do Not Convert Inputs into Conclusions
**Class:** REVIEW  
No individual input may be represented as automatically determining a Trust Statement.

### VAL-NRM-011 — Preserve Uncertainty
**Class:** CONDITIONAL / REVIEW  
Material uncertainty must remain visible rather than being silently strengthened into a more certain conclusion.

### VAL-NRM-012 — Interoperate Without Authority Transfer
**Class:** REVIEW / CONDITIONAL  
Cross-Suite references must preserve canonical ownership, meaning, identifiers, lifecycle, and authority of referenced objects.

---

## 13. Current Machine-Implementation Boundary

This catalog is now sufficiently specific to establish stable validation rule identities and to separate deterministic checks from institutional review.

It is **not yet sufficient to implement the complete validator**, because exact ATT machine structure remains unresolved in the supplied Attestation schema and exact serialization/cardinality remain intentionally delegated to Schemas/Validation.

Before executable code is frozen:

1. Normalize the canonical Attestation schema to completed Advanced Architecture.
2. Define the machine serialization selected for ATT/TRST validation.
3. Establish exact required/optional field cardinalities.
4. Establish the governed Validation Result vocabulary and report schema.
5. Resolve specialized `evidence` and `source-provenance` profile deltas after the base ATT contract is normalized.

---

## 14. Step 2 Determination

**Attestor Validation Rule Catalog v0.1 → Established.**

The architecture now has a traceable bridge:

`Attestor Rule → Normative Requirement → VAL-* Rule → Future Executable Test → Validation Result`

### Recommended next implementation step

**Normalize `attestation-schema.md` from Foundational Candidate Profile into the canonical Advanced Architecture Attestation Schema.**

This should occur before validator code because the validator must implement the schema; it must not invent the schema.
