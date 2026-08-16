# Chronicle Verification Procedure

## Purpose

Chronicle Verification is the structured review process used to evaluate Chronicle's own historical representation.

Verification asks whether a Chronicle Entry is:

* Properly identified
* Traceable to its Sources
* Correctly linked to authoritative records
* Temporally consistent
* Relationship-aware
* Supported by available Evidence
* Consistent with documented Provenance
* Transparent about material limitations

Verification does **not** determine absolute truth.

It also does **not** re-adjudicate certifications, registrations, attestations, anchors, discovery signals, workflows, Atlas records, or other determinations owned by another Satoshium institution.

The governing principle is:

> Verify the record. Respect the authority boundary.

---

# Verification Question

Chronicle Verification should answer:

> Does Chronicle's historical representation accurately and traceably reflect the information, records, relationships, dates, Evidence, Provenance, and limitations available?

It should not answer:

> Should Chronicle independently re-decide the authoritative determination made by another institution?

That distinction is fundamental.

---

# Scope of Verification

Chronicle Verification applies to Chronicle-owned historical representation.

It may review:

* Chronicle Entry identity
* Chronicle Entry Version
* Event Type
* Event Date
* Source Records
* External Source references
* Authoritative Suite references
* Evidence
* Provenance
* Relationships
* Historical Context
* Corrections
* Limitations
* Publication-relevant review state

Verification does not assume authority over referenced external objects.

---

# What Chronicle Actually Verifies

## 1. Entry Identity

Verification should confirm:

* Chronicle Entry identifier is present
* Identifier conforms to the Chronicle Identifier Specification
* Identifier is associated with the correct canonical Entry
* Identifier has not been reused
* Entry Version under review is clear

Example:

```text
Chronicle Entry:
CHR-2026-0001
```

Verification should not treat Event Type, Publication State, or other metadata as part of Entry identity.

---

## 2. Source Record Existence

Verification should confirm that required Source Records or external Source references:

* Exist
* Are identifiable
* Match the Source cited by the Entry
* Are accessible or properly preserved where required
* Carry enough citation information for later review

If a Source is unavailable, that limitation should be recorded rather than hidden.

---

## 3. Authoritative Reference Correctness

When Chronicle references an authoritative Suite object, Verification should confirm that:

* The identifier is correct
* The referenced object exists where reasonably reviewable
* The originating system is correctly identified
* Chronicle accurately represents the object's institutional role
* Chronicle does not claim authority over the object

Examples:

```text
SC-CERT-2026-0001
SREG-2026-0001
```

Chronicle may verify that it references these records correctly.

Chronicle does not re-certify, re-register, or otherwise re-adjudicate their authoritative determinations.

---

# Authority Boundary

The authority boundary is mandatory.

Examples:

```text
Chronicle may verify:
“This Entry correctly references SC-CERT-2026-0001.”

Chronicle must not independently decide:
“SC-CERT-2026-0001 should or should not have been certified.”
```

Similarly:

```text
Chronicle may verify:
“This Entry correctly references SREG-2026-0001.”

Chronicle must not independently replace Registry's registration determination.
```

Conceptually:

> Reference review is permitted. Re-adjudication is not.

---

## 4. Event-Date Consistency

Verification should confirm that Event Date is supported and internally consistent.

Chronicle must distinguish:

```text
Event Date
Entry Creation Date
Source Publication Date
Source Retrieval Date
Publication Date
Correction Date
Version Date
```

These dates may legitimately differ.

Verification should identify accidental date substitution or temporal inconsistency.

---

## 5. Relationship Consistency

Verification should review material Relationships for:

* Approved Relationship Type
* Correct source and target
* Correct direction
* Target identifier accuracy
* Historical plausibility
* Semantic accuracy
* Unsupported authority implications
* Unsupported causation
* Unsupported equivalence

Example:

```text
CHR-2026-0001
Precedes
CHR-2026-0002
```

Verification should confirm that the underlying Event Dates or records support that sequence.

---

## 6. Evidence Availability

Verification should confirm that required Evidence:

* Exists or is properly referenced
* Uses an appropriate Evidence Type
* Is linked to the correct Entry or claim
* Remains available or has an adequate archival reference
* Carries known limitations
* Is not misrepresented as authoritative where it is merely supporting

Evidence availability does not guarantee Evidence sufficiency.

---

## 7. Provenance Consistency

Verification should confirm that the minimum Provenance requirements are coherent.

The Provenance Model requires:

```text
Origin
Acquisition / Access Method
Capture / Retrieval Date
Source or Authoritative Record Reference when available
Provenance Limitations when applicable
```

Verification should also review material:

* Transfer history
* Transformation history
* Archive path
* Integrity metadata

where these are relevant.

---

## 8. Historical Context

Verification should confirm that Chronicle's Historical Context:

* Is consistent with cited Sources
* Does not overstate Evidence
* Does not convert correlation into causation
* Does not imply authority Chronicle does not possess
* Does not omit material known limitations
* Remains distinguishable from unsupported interpretation

Historical Context may contain narrative explanation.

It should remain reviewable.

---

## 9. Limitations

Verification must identify and preserve material limitations.

Potential examples include:

* Missing Source
* Unavailable Source
* Incomplete Provenance
* Conflicting Evidence
* Archive-only Evidence
* Uncertain Event Date
* Unresolved Relationship
* Ambiguous attribution
* Broken external reference
* Limited contextual support

Limitations should remain visible in the record.

---

# Verification Sequence

The initial Verification Procedure is:

```text
Entry Identified
    ↓
Identifier Checked
    ↓
Sources Checked
    ↓
Authoritative References Checked
    ↓
Dates Checked
    ↓
Relationships Checked
    ↓
Evidence Checked
    ↓
Provenance Checked
    ↓
Limitations Reviewed
    ↓
Verification State Assigned
```

The exact implementation may later be automated or partially automated.

The institutional sequence should remain recognizable.

---

# Verification Procedure

## Step 1 — Identify the Entry

Confirm:

* Chronicle Entry identifier
* Entry Version
* Event Type
* Applicable Base Schema Version
* Applicable Event-Type Profile where used

The reviewer must know exactly which record state is under review.

---

## Step 2 — Check Identifier Integrity

Review:

* `CHR-YYYY-NNNN` syntax
* Assignment consistency
* Uniqueness
* Non-reuse
* Stable identity across Version changes

Verification should flag malformed or improperly reused identifiers.

---

## Step 3 — Check Sources

Review:

* Required Source Records
* Direct external references
* Stable identifiers
* URLs where applicable
* Archive references
* Attribution
* Relevant Source dates

Verification should determine whether future reviewers can identify what Chronicle relied upon.

---

## Step 4 — Check Authoritative Objects

For each authoritative Suite reference:

1. Confirm the identifier.
2. Confirm the originating system.
3. Confirm the object is being referenced for the correct function.
4. Confirm Chronicle has not absorbed or reinterpreted the authoritative role.

---

## Step 5 — Check Temporal Information

Compare:

* Event Date
* Source dates
* Provenance retrieval dates
* Entry creation dates
* Related Entry Event Dates

Look for:

* Impossible ordering
* Date substitution
* Unsupported precision
* Inconsistent chronology

---

## Step 6 — Check Relationships

Review all material structured Relationships.

Confirm:

* Type
* Direction
* Source
* Target
* Target identifier
* Semantic appropriateness
* Historical support

Examples requiring direction review:

```text
Precedes ↔ Follows
Supersedes ↔ Superseded By
Corrects ↔ Corrected By
```

---

## Step 7 — Check Evidence

Review:

* Evidence Type
* Evidence availability
* Source linkage
* Provenance
* Entry or claim linkage
* Limitations
* Material contradictions

Chronicle should not remove contradictory Evidence merely because it complicates Verification.

---

## Step 8 — Check Provenance

Confirm Chronicle can explain:

> How did this information get here?

Review:

* Origin
* Access method
* Retrieval date
* Source reference
* Transformations
* Known limitations

Verification does not manufacture missing Provenance.

---

## Step 9 — Review Limitations

Before assigning a final state, determine whether any material issue remains unresolved.

Limitations should be recorded in a form future reviewers can understand.

---

## Step 10 — Assign Verification State

Verification State must use the Chronicle Controlled Values Registry.

The initial canonical states are:

```text
Not Reviewed
In Review
Verified
Verified with Limitations
Unresolved
```

---

# Controlled Verification States

## Not Reviewed

No applicable Chronicle Verification has been completed.

Potential machine token:

```text
not_reviewed
```

---

## In Review

Verification activity is underway.

No final review outcome has yet been assigned.

Potential machine token:

```text
in_review
```

---

## Verified

Chronicle completed the applicable Verification Procedure and found the historical representation sufficiently supported and internally consistent under current Chronicle rules.

`Verified` does not mean:

* Absolute truth
* Universal certainty
* Certifier certification
* Attestor attestation
* External institutional approval

Potential machine token:

```text
verified
```

---

## Verified with Limitations

Chronicle completed the applicable review, but material limitations remain.

Examples may include:

* Missing archive
* Partial Provenance
* Conflicting supporting material
* Uncertain temporal detail
* Limited Source availability

The limitations must remain visible.

Potential machine token:

```text
verified_with_limitations
```

---

## Unresolved

A material issue remains open and prevents Chronicle from treating the representation as resolved.

Potential causes include:

* Conflicting Evidence
* Uncertain dates
* Missing authoritative record
* Incomplete Provenance
* Unresolved Relationship
* Material Source conflict

Potential machine token:

```text
unresolved
```

An Unresolved Entry may still be historically important and Preservation Eligible.

---

# Retired Verification Terms

The older Chronicle Verification model used:

```text
Unverified
Under Review
Partially Verified
Verified
Disputed
Superseded
```

These terms should no longer govern production Verification State.

They are replaced by the current Controlled Values:

```text
Not Reviewed
In Review
Verified
Verified with Limitations
Unresolved
```

`Superseded` belongs more naturally to Entry or Lifecycle state and Relationship semantics rather than Verification State.

---

# Verification Is Not Confidence Scoring

Chronicle Verification should not be reduced to a generic numerical confidence model.

The operative question is not:

> What percentage confident are we?

The operative question is:

> Has Chronicle adequately reviewed its own historical representation under the applicable rules, and what material limitations remain?

Narrative confidence observations may still be recorded where helpful.

They should not replace Verification State.

---

# Verification and Sources

Verification may examine:

* Source existence
* Source identity
* Attribution
* Stable reference
* Archive reference
* Temporal consistency
* Source limitations

Verification does not make Chronicle authoritative for the Source.

---

# Verification and Evidence

Evidence supports Verification.

Verification may assess:

* Availability
* Relevance
* Authenticity
* Consistency
* Corroboration
* Contradiction
* Provenance
* Limitations

Evidence does not automatically become authoritative because Verification relied upon it.

---

# Verification and Provenance

Provenance provides traceability.

Verification reviews whether that traceability is sufficient for Chronicle's historical representation.

Conceptually:

```text
Provenance provides the path.
Verification reviews the path.
```

If the path is incomplete, Verification should preserve the limitation.

---

# Verification and Relationships

Verification should confirm that structured Relationships do not overstate meaning.

Relationship review should protect against:

* False causation
* False equivalence
* Incorrect sequence
* Incorrect direction
* Authority transfer
* Wrong target object
* Duplicate semantics

---

# Verification and Event Type

Verification may confirm that Event Type is consistent with the represented Occurrence.

This is classification review.

It is not re-adjudication of the underlying authoritative action.

If Event Type is incorrect, a Classification Correction may be appropriate.

---

# Verification and Preservation Eligibility

Verification and Preservation Eligibility are separate.

### Preservation Eligibility

Asks:

> Should Chronicle preserve this Occurrence?

### Verification

Asks:

> Does Chronicle's historical representation adequately hold together under current review?

An Entry may be Preservation Eligible and still be:

```text
In Review
Verified with Limitations
Unresolved
```

---

# Verification and Validation

Verification and Validation remain distinct.

### Verification

Asks:

> Does Chronicle's representation hold together historically?

### Validation

Asks:

> Does the structured record conform to Chronicle's technical and procedural requirements?

Conceptually:

```text
Verification ≠ Validation
```

A record may:

* Pass Verification and fail Validation
* Pass Validation and remain Unresolved
* Be Verified with Limitations and structurally valid

---

# Verification and Corrections

Verification may identify a need for:

* Typographical Correction
* Metadata Correction
* Contextual Correction
* Relationship Correction
* Provenance Correction
* Evidence Correction
* Classification Correction
* Substantive Correction

Correction Type should use the Chronicle Controlled Values Registry.

Chronicle corrects only its own records.

---

# Verification and Versioning

A material change to an Entry may require Reverification.

Potential triggers include:

* New Evidence
* New Source
* Event-Date Correction
* Relationship change
* Provenance Correction
* Material Historical Context change
* Authoritative reference change
* Substantive Entry Version

The Entry identifier remains stable.

Verification should be tied to the Entry Version actually reviewed.

---

# Reverification

Reverification should occur when the basis of the previous Verification materially changes.

Conceptually:

```text
Entry Version 1
    ↓
Verified
    ↓
Material Correction / New Evidence
    ↓
Entry Version 2
    ↓
Reverification
```

A prior Verification result should remain historically traceable.

---

# Verification Record

Chronicle should preserve enough Verification metadata to establish:

* Entry identifier
* Entry Version reviewed
* Review date
* Verification State
* Sources considered
* Evidence considered
* Material Relationships reviewed
* Provenance issues reviewed
* Limitations
* Reviewer or review mechanism where applicable

The final schema will determine whether this requires:

* A distinct Verification Record
* Embedded Entry Verification structure
* Both, depending on complexity

That decision should be made during schema and Production Procedure development.

---

# Verification Record Authority

Any Chronicle Verification Record would be authoritative only for Chronicle's own review result.

It would not be authoritative for:

* Certification
* Registration
* Attestation
* Anchoring
* Discovery
* Workflow definition
* Atlas records

---

# Verification and Certifier

The earlier Verification specification described Certifier as producing attestations.

That framing is no longer appropriate.

Under the current Suite architecture:

* **Certifier** is authoritative for Certification Packages and certification determinations.
* **Attestor** is authoritative for Trust Statements and attestations.
* **Chronicle** is authoritative for Chronicle Entries and Chronicle Verification of those Entries.

Chronicle may use Certifier records as authoritative references.

Chronicle may use Attestor Trust Statements as external authoritative references where relevant.

Neither relationship transfers authority to Chronicle.

---

# Verification and Publication

Publication rules may require a particular Verification State.

For example, future procedure may determine whether:

```text
Verified
```

is required for ordinary publication, while:

```text
Verified with Limitations
```

or:

```text
Unresolved
```

may be published only when limitations are prominently disclosed.

These publication rules should be settled during Production Procedure development rather than assumed here.

---

# Verification and Historical Preservation

Verification outcomes should remain traceable over time.

A future reviewer should be able to understand:

* What Chronicle reviewed
* What information was available
* What limitations existed
* What Verification State was assigned
* What later information changed the review

Historical review history itself may become institutionally meaningful.

---

# Verification Validation Expectations

Future Validation should confirm, where applicable:

1. Verification State is an approved Controlled Value.
2. Entry identifier is valid.
3. Entry Version under review is identified.
4. Required Sources are referenced.
5. Required Evidence is referenced.
6. Minimum Provenance is present.
7. Required Relationship checks are represented.
8. Material limitations are recorded.
9. Review date is valid.
10. Event-Type Profile requirements are satisfied.
11. Verification structure conforms to the governing schema Version.

---

# Verification Procedure Summary

The operational model is:

```text
Chronicle Entry
      ↓
Identify Entry + Version
      ↓
Check Identifier
      ↓
Check Sources
      ↓
Check Authoritative References
      ↓
Check Event Date
      ↓
Check Relationships
      ↓
Check Evidence
      ↓
Check Provenance
      ↓
Review Limitations
      ↓
Assign Verification State
```

---

# Guiding Principle

> Chronicle verifies the integrity of its historical representation—not the institutional authority of the systems it documents.

And operationally:

> Verify the record. Respect the authority boundary.

---

## Relationship to Other Chronicle Documentation

The Verification Procedure should remain aligned with:

* Entry Model
* Event Type Framework
* Preservation Eligibility
* Chronicle Rules
* Identifier Specification
* Controlled Values Registry
* Relationship Model
* Provenance Model
* Sources
* Evidence
* Corrections
* Historical Preservation
* Trust Model
* Schemas
* Validation
* Production Procedure

Verification is a review function within Chronicle's supporting architecture.

It does not replace the canonical Chronicle Entry.

---

## Next Operational Dependencies

The Verification Procedure directly informs:

* Lifecycle
* Versioning
* Corrections
* Chronicle Base Schema
* Certification Event-Type Profile
* Validation
* Production Procedure
* First production Chronicle Entry
* Publication requirements

The first production Chronicle Entry should be used to test whether this Verification sequence is complete, proportionate, and operationally practical.

---

## Status

**Active pre-operational Chronicle Verification Procedure specification.**

The Verification State vocabulary is governed through the Chronicle Controlled Values Registry.

The procedure now defines what Chronicle Verification actually verifies and establishes the authority boundary against re-adjudicating another institution's determinations.

Final Verification Record structure, reviewer-role requirements, automation rules, Event-Type-specific checks, and publication gating remain subject to later operational-development steps.
