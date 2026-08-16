# Chronicle Evidence Record Schema

## Purpose

The Chronicle Evidence Record Schema defines the structure used to represent evidence referenced or maintained by Satoshium Chronicle.

Evidence Records support Chronicle Entries by preserving structured information about materials that may support, challenge, contradict, clarify, corroborate, or contextualize Chronicle's historical representation of a qualifying occurrence.

Evidence does not transfer authority to Chronicle and does not determine the official outcome of another Suite system.

Chronicle uses Evidence Records to preserve reviewability, provenance, limitations, integrity information, and the relationship between evidence and the Chronicle Entry or claim it bears upon.

---

## Suite Alignment

Chronicle Evidence Records should align with the Satoshium Suite Standards, Methodology, Schemas Standard, Evidence Standard, and Interoperability principles.

The schema should support:

* Recognized evidence types
* Evidence quality
* Evidence integrity
* Evidence sufficiency
* Evidence limitations
* Provenance and traceability
* Durable references
* Structured relationships
* Validation-ready records
* Version preservation
* Reference-based interoperability
* Clear institutional authority boundaries

Chronicle should not create a competing evidence standard where the Suite Evidence Standard already defines one.

---

## Canonical Role

An Evidence Record is a **supporting Chronicle-owned record**.

It is not the canonical historical-preservation object.

The canonical Chronicle object remains the **Chronicle Entry**.

Conceptually:

```text
Chronicle Entry
      ↓
Evidence Relationship
      ↓
Evidence Record
      ↓
Verification / Review Context
```

An Evidence Record exists to describe and preserve the evidentiary role, origin, integrity, limitations, and relationship of evidence relevant to Chronicle.

---

## Schema Overview

A Chronicle Evidence Record should answer:

* What is the evidence?
* What evidence type is it?
* Where did it originate?
* Who or what created it?
* When was it created, observed, collected, or preserved?
* How did it enter Chronicle?
* Which Chronicle Entry or claim does it relate to?
* Does it support, challenge, contradict, clarify, corroborate, or contextualize that Entry or claim?
* What limitations apply?
* What integrity information is available?
* What is its preservation status?
* Has Chronicle reviewed or verified aspects of it?
* Has the Evidence Record passed structural validation?

---

# Field Architecture

The exact production identifier format, controlled values, and required/conditional designations remain subject to Chronicle Identifier Architecture, Controlled Values, Validation Rules, Evidence procedures, and Publication Standard.

The structure below is an operational architectural draft.

---

## Identity Fields

### `evidence_id`

Stable unique identifier assigned to the Chronicle Evidence Record.

**Status:** Required in production.

The final identifier format is not yet settled.

Example placeholder:

```text
<EVIDENCE-IDENTIFIER>
```

Legacy examples such as `EVD-000001` should not be treated as canonical.

---

### `schema_version`

Version of the Evidence Record Schema governing the record.

**Status:** Required.

Example:

```text
1.0.0
```

Schema version and evidence-record version should remain distinct concepts.

---

### `title`

Concise human-readable title describing the evidence.

**Status:** Required.

Example:

```text
Screenshot of Chronicle Launch Page
```

---

### `description`

Brief factual description of the evidence item.

**Status:** Required.

Example:

```text
Screenshot showing the public Chronicle homepage as it appeared on the documented launch date.
```

---

## Evidence Classification Fields

### `evidence_type`

Controlled classification identifying the evidence category.

**Status:** Required.

Chronicle should use Suite-recognized evidence categories rather than inventing incompatible local categories.

Possible working concepts may include:

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
```

These values are illustrative only until Controlled Values are formally approved.

Legacy categories such as:

```text
document
digital_record
physical_artifact
measurement
log
testimonial
```

should not automatically be carried forward as canonical unless the Suite Evidence Standard or Chronicle Controlled Values explicitly recognizes them.

---

### `evidence_relationship`

Controlled value describing how the evidence bears on the Chronicle Entry or claim.

**Status:** Required.

Potential working concepts may include:

```text
supports
challenges
contradicts
clarifies
corroborates
contextualizes
limits_confidence
```

These values remain provisional until Chronicle Controlled Values are approved.

Evidence should not be treated as uniformly supportive merely because it is linked.

---

## Origin and Provenance Fields

### `source_reference`

Reference to the source from which the evidence originated or was obtained.

**Status:** Conditional.

Source identifies where information originated.

---

### `original_creator`

Entity, institution, system, or person responsible for creating the original evidence material.

**Status:** Conditional.

---

### `original_created_at`

Date or timestamp associated with the original creation of the evidence.

**Status:** Conditional.

---

### `observed_or_collected_at`

Date or timestamp when Chronicle or another process observed, collected, acquired, or preserved the evidence.

**Status:** Conditional.

This field should not be confused with original creation time.

---

### `collection_method`

Description or controlled value identifying how the evidence was obtained or preserved.

**Status:** Recommended.

---

### `provenance`

Structured information describing how the evidence originated, moved, was obtained, and entered Chronicle.

**Status:** Expected to become required in production.

Provenance may include:

* Originating system
* Source path
* Acquisition method
* Archival path
* Collection context
* Preservation history
* Chain-of-custody information
* Related authoritative record

The final structure will be governed by the Chronicle Provenance Model.

---

## Relationship Fields

### `related_entry_references`

References to Chronicle Entries associated with the evidence.

**Status:** Required when the Evidence Record exists to support a Chronicle Entry.

Example placeholder:

```text
<CHRONICLE-ENTRY-ID>
```

---

### `related_claim_references`

References to specific claims, assertions, fields, or propositions within a Chronicle Entry where Chronicle later supports structured claim-level relationships.

**Status:** Conditional.

---

### `related_evidence_references`

References to associated Chronicle Evidence Records.

**Status:** Conditional.

---

### `related_correction_references`

References to Correction Records affecting this Evidence Record or its interpretation within Chronicle.

**Status:** Conditional.

---

### `authoritative_record_references`

References to authoritative Suite objects associated with the evidence or underlying occurrence.

**Status:** Conditional.

Examples may include:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Trust Statement
* Workflow Definition
* Atlas record

Chronicle references these objects but does not convert them into Chronicle-owned evidence authority.

---

## Evidence Quality Fields

### `quality_assessment`

Structured assessment of evidence quality factors.

**Status:** Conditional until the Suite Evidence Standard implementation is finalized.

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

The schema should avoid collapsing all quality considerations into a single unsupported numeric score unless the Suite standard explicitly requires one.

---

### `limitations`

Structured or narrative description of known evidence limitations.

**Status:** Required when material limitations exist.

Examples may include:

* Incomplete
* Conflicting
* Stale
* Missing provenance
* Unverifiable
* Broken reference
* Ambiguous authorship
* Uncertain date
* Limited context
* Derivative or altered material

Limitations are part of the historical record and should remain visible.

---

## Integrity Fields

### `checksum`

Cryptographic checksum or digest associated with the evidence object where available.

**Status:** Optional or conditional.

Example:

```text
sha256:<HASH>
```

---

### `digital_signature_reference`

Reference to a digital signature or signature-verification artifact.

**Status:** Conditional.

---

### `chain_of_custody`

Structured or narrative documentation describing evidence handling history.

**Status:** Conditional.

---

### `preservation_status`

Controlled value describing the current preservation condition of the evidence.

**Status:** Expected to become required.

Potential working concepts may include:

```text
available
archived
referenced_only
unavailable
superseded
preserved_copy
```

These values remain provisional.

---

### `integrity_notes`

Additional information relevant to authenticity, completeness, alteration risk, versioning, or preservation.

**Status:** Conditional.

---

## Verification Fields

### `verification_state`

Current Chronicle verification state relating to the Evidence Record.

**Status:** Conditional.

The final values remain to be defined.

Legacy values such as:

```text
unverified
under_review
partially_verified
verified
disputed
```

should be treated as historical draft vocabulary, not approved controlled values.

---

### `verification_references`

References to Chronicle verification records or activities.

**Status:** Conditional.

Verification may review:

* Authenticity
* Consistency
* Corroboration
* Provenance
* Traceability
* Temporal consistency
* Relationship integrity
* Integrity information
* Evidence limitations

Verification does not re-adjudicate an authoritative determination owned by another Suite system.

---

## Validation Fields

### `validation_state`

State or result of Chronicle Evidence Record validation.

**Status:** Required before production publication or operational use where validation is required.

Validation may include:

* Identifier integrity
* Schema conformance
* Required fields
* Controlled values
* Source-reference integrity
* Related-entry integrity
* Provenance requirements
* Preservation-status requirements
* Version linkage
* Publication readiness

Verification and Validation are separate functions.

---

### `validation_references`

References to validation results or records where Chronicle preserves them separately.

**Status:** Conditional.

---

## Lifecycle and Publication Fields

### `evidence_status`

Current lifecycle state of the Chronicle Evidence Record.

**Status:** Required.

The final controlled values remain to be defined.

Legacy values such as:

```text
draft
active
archived
superseded
```

should not be assumed to be canonical.

---

### `publication_state`

Current publication state of the Evidence Record.

**Status:** Conditional or required depending on Chronicle publication architecture.

Not every evidence item should necessarily be public even when the associated Chronicle Entry is public.

---

## Versioning Fields

### `evidence_record_version`

Version or preserved state of the Chronicle Evidence Record.

**Status:** Required if Chronicle adopts explicit evidence-record versioning.

---

### `prior_version_reference`

Reference to the prior Evidence Record state where applicable.

**Status:** Conditional.

Substantive changes to provenance, integrity, evidence relationship, or limitations should remain traceable.

---

## Metadata and Discovery Fields

### `tags`

Optional discovery metadata.

**Status:** Optional.

Tags should not replace controlled evidence type or evidence relationship values.

---

### `jurisdiction`

Optional geographic, organizational, legal, or operational scope associated with the evidence.

**Status:** Conditional.

Where jurisdiction matters, Chronicle should prefer controlled or authoritative references over ambiguous free text.

---

## Deprecated Legacy Fields

The following concepts from the original draft should not be carried forward unchanged:

### `collection_timestamp`

Deprecated as an ambiguous universal date.

Use more precise fields such as:

* `original_created_at`
* `observed_or_collected_at`

depending on the event being represented.

### `collector`

Deprecated as the only acquisition-actor field.

Use provenance and collection-method structures instead.

### `verification_status`

Deprecated in favor of:

```text
verification_state
```

once controlled values are settled.

### `verification_reference`

Deprecated in favor of:

```text
verification_references
```

to support one or more verification records.

### `author`

Deprecated as a universal field.

Use explicit actor roles where needed.

### Generic `version`

Deprecated as ambiguous.

Use:

* `schema_version`
* `evidence_record_version`

as separate concepts.

---

# Working Example

The following is conceptual only and does not establish final identifiers, controlled values, or production field names.

```yaml
evidence_id: <EVIDENCE-IDENTIFIER>
schema_version: 1.0.0

title: Screenshot of Chronicle Launch Page

description: >
  Screenshot showing the public Chronicle homepage as it appeared
  on the documented launch date.

evidence_type: screenshot
evidence_relationship: contextualizes

original_created_at: 2026-09-01T09:15:00Z
observed_or_collected_at: 2026-09-01T09:15:00Z

source_reference: <SOURCE-REFERENCE>

related_entry_references:
  - <CHRONICLE-ENTRY-ID>

authoritative_record_references: []

provenance:
  collection_method: direct_capture
  source: public_webpage

limitations: []

checksum: sha256:<HASH>

preservation_status: <CONTROLLED-VALUE>
verification_state: <CONTROLLED-VALUE>
validation_state: <CONTROLLED-VALUE>
evidence_status: <CONTROLLED-VALUE>
publication_state: <CONTROLLED-VALUE>

evidence_record_version: <VERSION>
```

This example intentionally avoids inventing final values that have not yet been architecturally approved.

---

## Evidence and Authoritative Records

An authoritative Suite object may itself provide strong evidentiary support for a Chronicle Entry, but its institutional role should remain distinct.

For example:

* A Certification Package is authoritative within Certifier for its certification determination.
* An SREG Registry Entry is authoritative within Registry for its catalog record.
* An Integrity Reference is authoritative within Anchor for anchoring.
* A Trust Statement is authoritative within Attestor for attestation.

Chronicle may reference these objects as authoritative records and may also preserve their evidentiary relevance.

The schema should not flatten all authoritative records into generic evidence objects.

---

## Evidence and Preservation Eligibility

Evidence sufficiency and Preservation Eligibility are separate questions.

An occurrence may qualify for Chronicle preservation even when evidence is incomplete, disputed, or limited, provided Chronicle records those limitations transparently and follows applicable rules.

Chronicle should not automatically import a Certifier evidence-sufficiency threshold into historical preservation.

Event-Type Profiles may define evidence requirements appropriate to specific occurrence classes.

---

## Evidence Record Lifecycle

A generalized Evidence Record lifecycle may include:

1. Evidence identified
2. Evidence type classified
3. Source and provenance documented
4. Relationship to Entry or claim established
5. Integrity information recorded
6. Limitations documented
7. Verification performed where applicable
8. Validation performed
9. Evidence Record published, retained privately, or otherwise applied according to Chronicle rules
10. Evidence Record maintained
11. Corrections or versioning applied when necessary
12. Preservation status maintained

Not every Evidence Record will require every step.

---

## Preservation Principles

Chronicle favors durable evidence references and preservation information whenever practical.

Where direct preservation is permitted and appropriate:

* Original materials should remain available
* Provenance should remain documented
* Integrity information should remain available
* Limitations should remain visible
* Historical relationships should remain intact
* Prior substantive record states should remain traceable

Where direct preservation is not appropriate or permitted, Chronicle should preserve enough durable reference, metadata, provenance, archival information, and integrity context to support future review.

Chronicle should not silently replace earlier evidence with later material.

---

## Design Goals

The Chronicle Evidence Record Schema should:

* Preserve evidentiary context
* Maintain Suite evidence vocabulary
* Preserve provenance
* Maintain integrity information
* Preserve limitations
* Support evidence-aware relationships
* Support verification
* Support validation
* Maintain authority boundaries
* Support version lineage
* Enable independent review
* Support long-term archival preservation
* Remain machine-readable and durable

---

## Future Development

Future Chronicle Evidence Schema work may include:

* Final Evidence Record identifier architecture
* Controlled evidence types
* Controlled evidence-relationship values
* Formal quality-assessment structures
* Preservation-status values
* Provenance schema
* Integrity metadata
* Evidence validation rules
* Chain-of-custody structures
* Automated reference validation
* Cryptographic integrity verification
* Event-Type-specific evidence requirements
* Public evidence discovery where appropriate

---

## Status

**Architectural draft — not yet a frozen production schema.**

This document has been reconciled with the current Chronicle Evidence page, Chronicle Evidence README, Chronicle Records architecture, Chronicle Base Schema direction, and Satoshium Suite Standards, Methodology, Schemas Standard, Evidence Standard, and Interoperability principles.

The final identifier format, controlled values, evidence-quality structures, provenance requirements, validation rules, preservation-status values, versioning conventions, and publication requirements must be settled through the remaining Chronicle operational-development steps before this schema becomes production authoritative.
