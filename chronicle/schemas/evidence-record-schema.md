# Chronicle Evidence Record Schema

## Purpose

The Chronicle Evidence Record Schema defines the Chronicle-owned supporting structure used to identify, describe, link, and preserve Evidence relevant to Satoshium Chronicle.

An Evidence Record answers:

> What material bears on the Chronicle Entry or claim?

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Corroborate
* Contextualize
* Limit confidence

Evidence supports Chronicle's historical representation.

It does not become the authoritative event itself.

The governing principle is:

> Evidence supports the historical representation. It does not become the event.

---

# Canonical Role

A Chronicle Evidence Record is a **supporting Chronicle-owned record**.

It is not the canonical historical-preservation object.

The canonical Chronicle object remains:

```text
Chronicle Entry
```

Conceptually:

```text
Chronicle Entry or Claim
        ↑
Evidence Relationship
        ↑
Evidence Record
```

An Evidence Record exists to preserve:

* Evidence identity
* Evidence Type
* Source linkage
* Provenance
* relationship to Entry or claim
* limitations
* integrity information
* Version lineage
* review context

---

# Evidence Is Not Authority

An Evidence Record may refer to an authoritative Suite object.

That does not transfer authority to Chronicle.

Examples:

* Certification Package remains authoritative within Certifier.
* SREG Registry Entry remains authoritative within Registry.
* Integrity Reference remains authoritative within Anchor.
* Trust Statement remains authoritative within Attestor.

Chronicle may use such objects as Authoritative Evidence while preserving their originating authority.

---

# Evidence, Source, Provenance, and Verification

These concepts remain distinct.

## Evidence

Answers:

> What material bears on the Chronicle Entry or claim?

## Source

Answers:

> Where did the information come from?

## Provenance

Answers:

> How did the information or Evidence originate, move, and enter Chronicle?

## Verification

Answers:

> Has Chronicle reviewed its own historical representation and the supporting material relevant to that review?

Conceptually:

```text
Evidence ≠ Source ≠ Provenance ≠ Verification
```

---

# Production Status

This specification defines the Phase VII reconciled architecture for Chronicle Evidence Records.

The canonical human-readable file is:

```text
evidence-record-schema.md
```

A future machine-readable implementation may be created as:

```text
evidence-record-schema.json
```

after the specification is exercised against a real production Evidence Record.

---

# Field Architecture

The Evidence Record Schema distinguishes:

```text
Required
Conditional
Optional
```

A field should not be Required unless every production Evidence Record needs it.

---

# Universal Required Fields

Every production Chronicle Evidence Record should contain:

```text
evidence_id
schema_id
schema_version
evidence_record_version

title
evidence_type

provenance

created_at
```

These fields define the minimum Evidence Record identity and traceability structure.

---

# Identity Fields

## `evidence_id`

Stable unique identifier assigned to the Chronicle Evidence Record.

**Requirement:** Required.

The final Evidence Record identifier namespace remains to be formally established.

Until approved, implementation should not invent a permanent namespace casually.

The identifier should remain:

* unique
* stable
* non-reusable
* independent of Evidence Type
* independent of Verification State
* independent of Publication State
* independent of Version

---

## `schema_id`

Stable identifier for the Evidence Record Schema.

**Requirement:** Required.

Initial value:

```text
chronicle-evidence-record
```

---

## `schema_version`

Version of the Evidence Record Schema governing the record.

**Requirement:** Required.

Initial production convention:

```text
1.0.0
```

Schema Version is distinct from Evidence Record Version.

---

## `evidence_record_version`

Sequential preserved Version of the same Chronicle Evidence Record.

**Requirement:** Required.

Initial value:

```text
1
```

Material changes should advance Evidence Record Version where historical or review meaning changes.

Examples:

* changed Evidence identity
* changed Evidence Type
* changed Entry / claim linkage
* changed Provenance
* changed limitation
* changed integrity representation
* changed Source reference

---

# Human-Readable Identity

## `title`

Concise human-readable title describing the Evidence.

**Requirement:** Required.

Example:

```text
Screenshot of Chronicle Launch Page
```

---

## `description`

Brief factual description of the Evidence item.

**Requirement:** Conditional.

Required when the title alone does not adequately identify or explain the Evidence.

---

# Evidence Type

## `evidence_type`

Controlled classification identifying the Evidence category.

**Requirement:** Required.

Approved Chronicle Evidence Type values are:

```text
authoritative_evidence
documentary_evidence
repository_evidence
archival_evidence
machine_generated_evidence
testimonial_evidence
contextual_evidence
other
```

Human-readable labels:

```text
Authoritative Evidence
Documentary Evidence
Repository Evidence
Archival Evidence
Machine-Generated Evidence
Testimonial Evidence
Contextual Evidence
Other
```

Rules:

* Evidence Type describes what kind of Evidence this is.
* Evidence Type does not establish evidentiary strength by itself.
* Evidence Type does not define the Evidence Relationship.
* `other` should be used only when no approved value accurately fits.
* Repeated use of `other` should trigger Controlled Values review.

---

# Evidence Relationship

## `evidence_relationship`

Describes how the Evidence bears on the Chronicle Entry or claim.

**Requirement:** Conditional.

Required when an Evidence Record is linked to an Entry or claim and the evidentiary function needs explicit structured representation.

Candidate relationship semantics include:

```text
supports
challenges
contradicts
clarifies
corroborates
contextualizes
limits_confidence
```

These values are **not yet a frozen Controlled Value set**.

Chronicle should not formalize them merely for architectural completeness.

They should become governed Controlled Values only when production schema and review use demonstrate the need.

---

# Evidence Linkage

## `related_entry_references`

References to Chronicle Entries associated with the Evidence.

**Requirement:** Conditional.

Required when the Evidence Record exists in support of or relation to one or more Chronicle Entries.

---

## `related_claim_references`

References to specific claims, fields, assertions, or propositions within a Chronicle Entry.

**Requirement:** Conditional.

Used when Chronicle supports structured claim-level Evidence linkage.

This should not be required where Entry-level linkage is sufficient.

---

## `related_evidence_references`

References to associated Evidence Records.

**Requirement:** Conditional.

Used when another Evidence Record is materially relevant to interpretation, corroboration, conflict, or lineage.

---

## `related_correction_references`

References to Correction Records affecting this Evidence Record or its use in Chronicle.

**Requirement:** Conditional.

Required when a formal Correction applies.

---

# Source Linkage

## `source_reference`

Reference to the Source from which the Evidence originated or was obtained.

**Requirement:** Conditional.

Required when a Source is separately identifiable and materially relevant.

A Source Record may or may not be necessary.

The Source architecture determines whether a direct Source reference is sufficient.

---

# Authoritative Record Linkage

## `authoritative_record_references`

References to authoritative Suite or external institutional objects associated with the Evidence.

**Requirement:** Conditional.

Examples may include:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Trust Statement
* Workflow Definition
* Atlas record

Rules:

* Chronicle references the authoritative object.
* Chronicle does not flatten that object into generic Evidence authority.
* Authority remains with the originating institution.

---

# Creator and Origin Fields

## `original_creator`

Entity, institution, system, or person responsible for creating the original Evidence material.

**Requirement:** Conditional.

Required when known and material to interpretation.

---

## `original_created_at`

Date or timestamp associated with creation of the original Evidence.

**Requirement:** Conditional.

---

## `observed_or_collected_at`

Date or timestamp when Chronicle or another documented process observed, collected, acquired, or preserved the Evidence.

**Requirement:** Conditional.

This should remain distinct from the original creation time.

---

# Provenance

## `provenance`

Structured information describing how the Evidence originated, was obtained, moved, transformed, and entered Chronicle.

**Requirement:** Required.

Every production Evidence Record should preserve, at minimum:

```text
origin
acquisition_method
retrieved_at
```

and, when applicable:

```text
source_reference
authoritative_record_reference
limitations
```

Expanded Provenance may include:

* transfer history
* transformation history
* archival path
* preservation history
* collection context
* chain-of-custody information
* integrity metadata

The Chronicle Provenance Model governs meaning.

---

# Evidence Quality

## `quality_assessment`

Structured or narrative assessment of Evidence quality factors.

**Requirement:** Optional / Conditional.

Relevant factors may include:

* Authority
* Independence
* Completeness
* Authenticity
* Timeliness
* Reproducibility
* Traceability
* Resistance to alteration
* Resistance to misinterpretation
* Corroboration
* Contextual adequacy

Rules:

* Quality assessment should not collapse into an unsupported universal numerical score.
* Quality factors are review inputs, not authority claims.
* Different Event-Type Profiles may weigh quality factors differently.

---

# Limitations

## `limitations`

Structured or narrative description of known Evidence limitations.

**Requirement:** Conditional.

Required when material limitations exist.

Examples may include:

* incomplete
* conflicting
* stale
* missing Provenance
* unverifiable
* broken reference
* ambiguous authorship
* uncertain date
* limited context
* derivative or altered material
* archive-only representation

Limitations are part of the historical record.

They should remain visible over time.

---

# Integrity Metadata

## `checksum`

Cryptographic checksum or digest associated with the Evidence object.

**Requirement:** Optional / Conditional.

Example:

```text
sha256:<HASH>
```

---

## `digital_signature_reference`

Reference to a digital signature or signature-verification artifact.

**Requirement:** Conditional.

---

## `chain_of_custody`

Structured or narrative information describing Evidence handling history.

**Requirement:** Conditional.

Use only where the nature of the Evidence makes chain-of-custody meaningful.

---

## `integrity_metadata`

Other integrity information relevant to authenticity, completeness, alteration risk, or preservation.

**Requirement:** Optional / Conditional.

Potential examples:

* repository commit
* timestamp
* immutable object identifier
* Anchor Integrity Reference
* file metadata
* archival capture identifier

Integrity metadata supports reviewability.

It does not replace Provenance.

---

# Preservation Information

## `preservation_notes`

Information describing archival state, preservation method, availability, or long-term accessibility.

**Requirement:** Conditional.

A formal Evidence Preservation State vocabulary is **not yet frozen**.

Therefore the schema should not invent a production `preservation_status` enumeration at this stage.

If production use demonstrates a stable need, Preservation State can later be introduced through schema evolution.

---

# Verification

## `verification_state`

Chronicle Verification State associated with the Evidence Record where Chronicle separately reviews Evidence-level questions.

**Requirement:** Conditional.

Approved values:

```text
not_reviewed
in_review
verified
verified_with_limitations
unresolved
```

Human-readable labels:

```text
Not Reviewed
In Review
Verified
Verified with Limitations
Unresolved
```

Evidence-level Verification may review:

* authenticity
* consistency
* corroboration
* Provenance
* traceability
* temporal consistency
* linkage
* integrity information
* limitations

Verification does not re-adjudicate another institution's determination.

---

## `verification_references`

References to separately preserved Verification activity or records.

**Requirement:** Conditional.

Whether Chronicle needs distinct Verification Records remains a later production decision.

---

# Validation

The Evidence Record Schema is designed for Validation.

It does not presently require a universal embedded:

```text
validation_state
```

The Validation Procedure should determine where Validation results are stored.

Validation may test:

* Evidence Record identifier integrity
* schema conformance
* required fields
* Evidence Type Controlled Values
* Entry linkage
* claim linkage
* Source linkage
* Provenance requirements
* Version linkage
* publication prerequisites

Conceptually:

```text
Schema ≠ Verification ≠ Validation
```

---

# Lifecycle

A separate production `evidence_status` field is not yet required.

The Lifecycle State vocabulary established for Chronicle Entries should not automatically be applied to Evidence Records without evidence that the same lifecycle model fits.

The Evidence Record lifecycle may conceptually include:

```text
identified
structured
linked
reviewed
validated
used
maintained
corrected / versioned
preserved
```

These are process concepts, not approved Evidence Record Controlled Values.

---

# Publication

## `publication_state`

Publication State of the Evidence Record when Chronicle independently publishes the Evidence Record.

**Requirement:** Conditional.

Approved Chronicle Publication State values are:

```text
not_published
pending_publication
published
withdrawn_from_publication
```

Not every Evidence Record should necessarily be public even when its Chronicle Entry is public.

---

## `published_record_at`

Date and time Chronicle published the Evidence Record.

**Requirement:** Conditional.

Required when:

```text
publication_state: published
```

This is distinct from `original_created_at`.

---

# Versioning

## `evidence_record_version`

Sequential Version of the Evidence Record.

**Requirement:** Required.

Material Evidence Record changes should create a new Version where a future reviewer would reasonably need to know that the prior record said something materially different.

Potential triggers:

* Evidence Type correction
* Source linkage change
* Entry / claim linkage change
* Provenance change
* integrity correction
* limitation discovery
* relationship change

---

## `prior_version_reference`

Reference to the immediately prior preserved Evidence Record Version.

**Requirement:** Conditional.

Required for Version 2 and later when prior Version linkage is represented directly.

Prior substantive Evidence Record states should remain preserved.

---

# Corrections

An Evidence Record may be corrected through Chronicle's Correction architecture.

Material Corrections should preserve:

```text
Original information
Corrected information
Correction date
Reason
Affected fields
Resulting Version
```

Chronicle must not silently rewrite:

* Evidence identity
* Evidence Type
* Entry linkage
* claim linkage
* Source linkage
* Provenance
* limitations
* integrity information

---

# Discovery Fields

## `tags`

Optional discovery metadata.

**Requirement:** Optional.

Tags should not replace Evidence Type or Evidence Relationship.

---

## `jurisdiction`

Geographic, legal, organizational, or operational scope associated with the Evidence.

**Requirement:** Optional / Conditional.

Where important, Chronicle should prefer stable identifiers or authoritative references over ambiguous free text.

---

# Fields Intentionally Not Frozen

The following concepts remain intentionally unresolved:

```text
evidence_relationship controlled vocabulary
preservation_state
validation_state location
evidence_record identifier namespace
```

These should not be frozen until production evidence demonstrates a stable institutional need.

---

# Deprecated Legacy Evidence Types

The following older draft categories should not govern production Evidence Records:

```text
primary_source
secondary_source
institutional_record
self_attestation
cryptographic_record
metadata
screenshot
image
archive
audio
video
receipt
witness_statement
other_approved

document
digital_record
physical_artifact
measurement
log
testimonial
```

Use the approved Evidence Type vocabulary instead.

---

# Deprecated Legacy Fields

## `collection_timestamp`

Deprecated as ambiguous.

Use:

```text
original_created_at
observed_or_collected_at
```

according to meaning.

---

## `collector`

Deprecated as a universal acquisition-actor field.

Use Provenance and explicit actor fields only where needed.

---

## `verification_status`

Deprecated.

Use:

```text
verification_state
```

---

## Generic `version`

Deprecated.

Use:

```text
schema_version
evidence_record_version
```

---

## Universal `author`

Deprecated.

Use explicit role fields where operationally necessary.

---

# Production Example

The following example demonstrates current Phase VII Evidence Record architecture.

The Evidence Record identifier remains illustrative until its namespace is formally established.

```yaml
evidence_id: <EVIDENCE-IDENTIFIER>
schema_id: chronicle-evidence-record
schema_version: 1.0.0
evidence_record_version: 1

title: Screenshot of Chronicle Launch Page

description: >
  Screenshot showing the public Chronicle homepage as it appeared
  at the documented capture time.

evidence_type: archival_evidence

evidence_relationship: contextualizes

source_reference: <SOURCE-REFERENCE>

related_entry_references:
  - CHR-2026-0001

original_created_at: 2026-09-01T09:15:00Z
observed_or_collected_at: 2026-09-01T09:15:00Z

provenance:
  origin: public_chronicle_webpage
  acquisition_method: direct_capture
  retrieved_at: 2026-09-01T09:15:00Z

verification_state: not_reviewed
publication_state: not_published

created_at: 2026-09-01T09:20:00Z
```

This example does not freeze `contextualizes` as an approved Evidence Relationship Controlled Value.

---

# Evidence Record Creation Test

A separate Evidence Record should ordinarily be created when one or more of the following are true:

* Evidence needs structured identity
* Entry / claim linkage must be explicit
* Source linkage is material
* Provenance is material
* limitations are material
* integrity metadata matters
* Evidence is reused across Entries
* independent Versioning is needed
* an Event-Type Profile requires it
* Validation requires it
* public Evidence discovery is needed

Otherwise a direct Evidence reference may be sufficient.

---

# Evidence and Preservation Eligibility

Evidence sufficiency and Preservation Eligibility remain separate.

Preservation Eligibility asks:

> Should Chronicle preserve this Occurrence?

Evidence sufficiency asks:

> Is the available Evidence adequate for the historical purpose for which it is being used?

A Preservation-Eligible Occurrence may still have:

* incomplete Evidence
* conflicting Evidence
* limited Evidence
* unresolved Evidence

Chronicle should preserve those limitations transparently.

---

# Evidence and Event-Type Profiles

An Event-Type Profile may strengthen Evidence requirements.

A Profile may require:

* specific Evidence Types
* minimum authoritative Evidence
* specific Source references
* Provenance minimums
* Evidence Relationship semantics
* integrity information
* Verification expectations

The Base Evidence Record Schema should remain general enough to support those requirements without becoming Event-Type-specific.

---

# Evidence Record Lifecycle

A generalized operational path may be:

```text
Evidence Identified
      ↓
Need for Evidence Record Assessed
      ↓
Evidence Record Created
      ↓
Evidence Type Assigned
      ↓
Source / Provenance Recorded
      ↓
Entry / Claim Linkage Established
      ↓
Limitations / Integrity Recorded
      ↓
Verification where Applicable
      ↓
Validation
      ↓
Use / Publication / Maintenance
      ↓
Correction / Versioning when Necessary
      ↓
Historical Preservation
```

Not every Evidence Record requires public publication or separate Verification.

---

# Authority Boundary

Chronicle Evidence Records preserve evidentiary relevance.

They do not absorb institutional authority.

The rule remains:

> Evidence may reference authority. Evidence does not become the authority.

---

# Validation Expectations

A production Evidence Record should ultimately be validated against:

* Evidence Record Schema
* Evidence Record identifier rules
* required fields
* Evidence Type Controlled Values
* Entry linkage
* claim linkage where used
* Source references
* Provenance requirements
* Versioning rules
* publication prerequisites

Evidence Relationship should not be validated against a frozen vocabulary until formally governed.

---

# Schema Versioning and Compatibility

Every production Evidence Record should remain associated with the Evidence Record Schema Version that governed it.

Schema evolution should preserve:

* Schema identity
* Schema Version
* compatibility classification
* deprecation history
* migration guidance
* Validation behavior
* historical interpretability

Older Evidence Records should remain understandable under the Schema Version that originally governed them.

---

# Design Principles

## Evidence Supports Representation

Evidence supports Chronicle's historical representation.

It does not become the event.

## Evidence ≠ Source

Evidence and Source remain distinct.

## Provenance Is Required

Evidence without information-path traceability is institutionally incomplete.

## Controlled Evidence Types

Production Evidence Types come from the Controlled Values Registry.

## Relationship Semantics Remain Provisional

Do not freeze Evidence Relationship values prematurely.

## Authority Remains External

Authoritative objects retain their originating institutional authority.

## Preserve Limitations

Conflicting, incomplete, stale, or uncertain Evidence remains visible.

## Preserve Prior States

Material Evidence Record changes remain Versioned and traceable.

---

# Guiding Principle

> Evidence supports the historical representation. It does not become the event.

And operationally:

> Preserve the Evidence. Preserve its relationship. Preserve its limitations.

---

## Status

**Phase VII reconciled Chronicle Evidence Record Schema specification.**

The Evidence Record Schema is now aligned with:

* Chronicle Base Schema
* Evidence architecture
* Controlled Values Registry
* Source architecture
* Provenance Model
* Relationship Model
* Verification Procedure
* Versioning Policy
* Corrections
* authority boundaries

The approved Evidence Type vocabulary is incorporated.

Evidence Relationship Controlled Values, Evidence Record identifier namespace, Preservation State, and the location of Validation results remain intentionally unresolved pending production evidence.

A machine-readable `evidence-record-schema.json` should be created only after this specification is tested against the first production Evidence Record.
