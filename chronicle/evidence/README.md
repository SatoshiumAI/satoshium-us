# Chronicle Evidence

## Purpose

Chronicle Evidence defines how Evidence is referenced, described, linked, evaluated, and preserved in support of Chronicle Entries.

Within Chronicle, Evidence is material that bears on Chronicle's historical representation of a qualifying Occurrence.

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Corroborate
* Contextualize
* Limit confidence

Evidence is not the authoritative event itself.

Evidence also does not transfer institutional authority to Chronicle.

Where another Suite system owns the underlying action, determination, or authoritative record, that authority remains with the originating system.

Chronicle uses Evidence to keep its own historical record transparent, reviewable, challengeable, and understandable over time.

---

# Suite Alignment

Chronicle Evidence operates within the Satoshium Suite architecture.

Evidence handling should remain aligned with Suite-wide expectations for:

* Recognized Evidence Types
* Evidence quality
* Evidence integrity
* Evidence sufficiency
* Evidence limitations
* Traceability
* Provenance
* Structured Evidence Records
* Validation-ready data
* Durable references
* Reference-based interoperability
* Clear institutional authority boundaries

Chronicle should inherit the Satoshium Suite Evidence Standard rather than create a competing Chronicle-only evidence standard.

---

# Role Within Chronicle

Evidence supports Chronicle's historical representation.

Conceptually:

```text
Occurrence
    ↓
Chronicle Entry
    ↓
Evidence bears on the Entry or claim
```

Evidence does not replace:

* The Occurrence
* The Chronicle Entry
* The authoritative Suite object
* Source
* Provenance
* Verification

---

# What Is Evidence?

Evidence is information, documentation, material, data, testimony, metadata, media, machine output, archival material, or another approved record that bears on:

* A Chronicle Entry
* A claim within an Entry
* A Relationship
* Historical Context
* Provenance
* Verification
* A Correction

Evidence is meaningful because of how it relates to Chronicle's historical representation.

The existence of an Evidence item does not automatically validate a claim.

Likewise, absence of Evidence does not automatically prove that an Occurrence did not happen.

---

# Evidence Is Not the Authoritative Event

Chronicle must preserve the distinction between:

```text
Occurrence
Authoritative Object
Chronicle Entry
Evidence
```

Example:

```text
Certification Occurrence
        ↓
Certifier Certification Package
        ↓
Chronicle Entry preserves the qualifying Occurrence
        ↓
Evidence supports review of Chronicle's representation
```

The Certification Package may itself provide Authoritative Evidence.

Certifier remains authoritative for the certification determination.

Chronicle remains authoritative for the Chronicle Entry.

Evidence does not become the event or the authority merely because Chronicle relies on it.

---

# Core Principles

## Preserve Reviewability

Evidence references and material context should remain available whenever practical so future reviewers can understand the basis for Chronicle's historical representation.

---

## Transparency

Evidence should be clearly described and documented.

Reviewers should be able to determine, where applicable:

* What the Evidence is
* What Evidence Type applies
* Where it originated
* When it was created, obtained, or observed
* How it entered Chronicle
* Which Entry or claim it relates to
* How it bears on that Entry or claim
* What limitations apply
* Whether it remains available
* What integrity information exists

---

## Provenance

Evidence Provenance should describe how the Evidence originated, was obtained, transformed where applicable, and entered Chronicle.

Provenance is related to, but distinct from, Source.

---

## Independence

Evidence should remain distinguishable from the conclusions drawn from it.

Chronicle should not present the existence of Evidence as automatic proof of a historical claim.

---

## Context Matters

Evidence gains meaning through context.

Chronicle should preserve enough context for later reviewers to understand:

* Why the Evidence was relevant
* What was known at the time
* What limitations existed
* Whether later information changed interpretation

---

## Authority Boundaries

Evidence referenced by Chronicle does not transfer authority from another Suite system.

Chronicle may preserve and evaluate Evidence relevant to its own Entry while Certifier, Registry, Anchor, Beacon, Attestor, Navigator, Atlas, and other Suite systems retain authority over their own records and determinations.

Conceptually:

> Evidence may reference authority. Evidence does not become the authority.

---

# Controlled Evidence Types

Evidence Type should use the Chronicle Controlled Values Registry.

The initial canonical Evidence Type values are:

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

These values replace older free-form category lists for Chronicle production use.

---

## Authoritative Evidence

Evidence drawn from or directly reflecting an authoritative record or authoritative system.

Examples may include:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Trust Statement
* Other authoritative Suite object

Authority remains with the originating system.

---

## Documentary Evidence

Documents, reports, letters, publications, filings, records, or other documentary material that bears on the Chronicle Entry or claim.

---

## Repository Evidence

Repository records, commits, releases, structured artifacts, issue records, or other preserved repository material relevant to historical review.

---

## Archival Evidence

Archived webpages, snapshots, preserved documents, historical collections, or other material accessed through an archive or preservation system.

---

## Machine-Generated Evidence

Machine-produced material such as:

* Logs
* Hashes
* Timestamps
* System outputs
* Receipts
* Generated metadata
* Automated records
* Integrity data

---

## Testimonial Evidence

Statements, interviews, declarations, witness accounts, recorded testimony, or similar human-sourced material relevant to the Entry.

---

## Contextual Evidence

Material that primarily helps explain the surrounding historical circumstances rather than directly establishing an authoritative action or determination.

---

## Other

`Other` should be used only when no approved Evidence Type accurately represents the material.

Repeated use of `Other` should trigger review for a possible new Controlled Value.

---

# Evidence Type and Evidence Relationship

Evidence Type and Evidence Relationship are different concepts.

### Evidence Type

Answers:

> What kind of Evidence is this?

### Evidence Relationship

Answers:

> How does this Evidence bear on the Chronicle Entry or claim?

Candidate Evidence Relationship terms include:

```text
Supports
Challenges
Contradicts
Clarifies
Corroborates
Contextualizes
Limits Confidence
```

These relationship terms should become a formal Controlled Value set only when schema and production use demonstrate that stable machine-readable semantics are required.

Chronicle should not confuse Evidence Type with evidentiary function.

---

# Evidence Linkage to Chronicle Entries

Evidence should be linked explicitly to the Chronicle Entry or specific claim it bears upon.

Conceptually:

```text
Evidence Item / Evidence Record
        ↓
Evidence Relationship
        ↓
Chronicle Entry or Claim
```

Linkage should make clear whether the Evidence:

* Supports
* Challenges
* Contradicts
* Clarifies
* Corroborates
* Contextualizes
* Limits confidence

A single Evidence item may relate to:

* One Entry
* Multiple Entries
* One claim
* Multiple claims

The relationship should remain explicit.

---

# Evidence Record Structure

Where a distinct Evidence Record is used, it should preserve enough structure to identify the Evidence and connect it to Chronicle's supporting architecture.

Expected components may include:

### Evidence Type

The approved Controlled Value describing the Evidence category.

### Source Reference

The Source or Source Record from which the Evidence originated.

### Provenance

How the Evidence originated, was obtained, moved, transformed, and entered Chronicle.

### Relationship to Entry or Claim

How the Evidence bears on the Chronicle Entry or specific claim.

### Date / Temporal Context

Relevant creation, publication, collection, observation, capture, or preservation date.

### Limitations

Known weaknesses, gaps, conflicts, or interpretive limitations.

### Integrity Information

Hashes, signatures, timestamps, version information, archive references, or other integrity indicators where applicable.

### Review Notes

Documented review observations, context, or unresolved issues.

### Public Reference

A durable public or archival reference where available.

The final schema should implement these concepts without duplicating Source or Provenance structures unnecessarily.

---

# Evidence and Sources

Evidence and Sources are related but distinct.

A Source answers:

> Where did the information originate?

Evidence answers:

> What material bears on the Chronicle Entry or claim?

Provenance answers:

> How did that information or Evidence originate, move, and enter Chronicle?

Example:

```text
Source:
Official certification webpage

Evidence:
Screenshot showing publication date

Provenance:
Screenshot captured from the official webpage on the recorded retrieval date
```

A Source may contain multiple Evidence items.

An Evidence item should remain traceable to its Source whenever practical.

---

# Evidence and Authoritative Records

An authoritative Suite record is not merely an ordinary supporting Evidence item.

Examples:

* Certification Package → authoritative within Certifier
* SREG Registry Entry → authoritative within Registry
* Integrity Reference → authoritative within Anchor
* Trust Statement → authoritative within Attestor

Chronicle may reference these records as:

* Authoritative objects
* Sources
* Authoritative Evidence

depending on context.

Their authority remains with the originating system.

Chronicle should preserve the distinction between:

```text
Authoritative Record
Supporting Evidence
Chronicle Entry
```

---

# Evidence and Provenance

Evidence Provenance should identify how the Evidence entered Chronicle.

Potential Provenance may include:

* Originating system
* Source path
* Access method
* Capture date
* Archive reference
* Transfer history
* Transformation
* Preservation history
* Integrity metadata
* Known limitations

Evidence quality and Provenance quality remain separate dimensions.

---

# Evidence and Verification

Evidence contributes to Chronicle Verification.

Verification may assess:

* Authenticity
* Reliability
* Consistency
* Corroboration
* Provenance
* Traceability
* Reference integrity
* Temporal consistency
* Evidence limitations
* Relationship consistency
* Contradictions

Verification concerns Chronicle's own historical representation.

It does not re-adjudicate an outcome owned by another Suite system.

---

# Verification Does Not Convert Evidence Into Authority

A Verified Chronicle Entry does not make every Evidence item authoritative.

Similarly, Authoritative Evidence does not make Chronicle authoritative for the originating determination.

The authority boundary remains explicit.

---

# Evidence and Validation

Validation and Evidence review are separate functions.

Evidence review concerns:

* Content
* Relevance
* Integrity
* Provenance
* Limitations
* Relationship to the Entry

Validation concerns whether Chronicle's structured record conforms to:

* Required schemas
* Controlled Values
* Required fields
* Identifier rules
* Relationship rules
* Provenance requirements
* Event-Type Profile requirements
* Publication rules

An Entry may contain strong Evidence and still fail Validation.

A structurally valid Entry may contain Evidence with known limitations.

---

# Evidence Validation Expectations

Future Validation should confirm, where applicable:

1. Evidence Type is an approved Controlled Value.
2. Evidence is linked to the correct Entry or claim.
3. Source reference is present where required.
4. Required Provenance is present.
5. Relevant dates are valid.
6. Known limitations are represented.
7. Relationship semantics are valid.
8. Integrity information is structurally valid where required.
9. Event-Type Profile Evidence requirements are satisfied.
10. Evidence Record structure conforms to the governing schema Version.

---

# Evidence Quality

Chronicle should not reduce Evidence quality to a simple present/absent determination.

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

The significance of each factor may vary according to:

* Event Type
* Historical claim
* Source context
* Verification need
* Event-Type Profile

These factors should not automatically become a universal numerical score.

---

# Evidence Limitations

Evidence limitations are part of the historical record and should remain visible.

Examples may include:

* Incomplete Evidence
* Conflicting Evidence
* Stale Evidence
* Missing Provenance
* Unverifiable material
* Unsupported assertions
* Broken or unavailable references
* Ambiguous authorship
* Uncertain dates
* Limited context
* Altered or derivative material
* Archive-only representation

Chronicle should disclose material limitations rather than imply certainty the Evidence does not support.

---

# Evidence Integrity

Evidence integrity concerns whether an Evidence item remains identifiable, reviewable, and resistant to undetected alteration.

Integrity information may include:

* Cryptographic hashes
* Checksums
* Digital signatures
* Timestamps
* Chain-of-custody information
* Version information
* Archival references
* Preservation status
* Source-system identifiers
* File or object metadata
* Anchor references

Integrity supports reviewability.

It does not replace Provenance or authority.

---

# Evidence, Preservation Eligibility, and Sufficiency

Preservation Eligibility and Evidence sufficiency remain separate questions.

### Preservation Eligibility

Asks:

> Should Chronicle preserve this Occurrence?

### Evidence Sufficiency

Asks:

> Is the available Evidence adequate for the particular historical purpose for which it is being used?

A historically significant Occurrence may warrant preservation even when Evidence is:

* Incomplete
* Disputed
* Limited
* Conflicting

provided Chronicle records those limitations transparently and follows applicable rules.

Chronicle should not automatically import Certifier Evidence-sufficiency thresholds into historical preservation.

---

# Evidence Sufficiency Is Contextual

Different Event-Type Profiles may establish different Evidence expectations.

For example:

A Certification Event-Type Profile may rely heavily on authoritative Certifier records.

A future governance Event-Type Profile may require a different supporting Evidence pattern.

The Evidence Standard provides the general framework.

Chronicle Event-Type Profiles may specialize requirements where needed.

---

# Preservation

Chronicle favors durable Evidence references and preservation information whenever practical.

Evidence should remain accessible in its original or authoritative form where possible.

When direct preservation is not appropriate or permitted, Chronicle should preserve enough:

* Reference information
* Source identity
* Provenance
* Metadata
* Archive information
* Integrity information
* Limitations

to maintain historical reviewability.

Chronicle should not silently replace earlier Evidence with later material.

---

# Evidence and Relationships

Evidence may connect to:

* Chronicle Entries
* Claims
* Source Records
* Authoritative records
* Corrections
* Verification
* Other Evidence Records

General object Relationships should follow the Chronicle Relationship Model.

Evidence-specific semantics such as `Supports` or `Contradicts` should remain distinct from general Relationship Types unless later schema design intentionally unifies them.

---

# Evidence and Corrections

New Evidence may justify:

* Supplemental context
* A Correction
* A new Entry Version
* Reverification
* A Relationship update
* A new Chronicle Entry describing a later Occurrence

Chronicle corrects only its own records.

If another Suite system changes an authoritative record, Chronicle may preserve that later Occurrence and update its references according to Chronicle rules.

---

# Evidence and Versioning

Substantive changes to Chronicle's evidentiary representation should remain traceable.

Examples include:

* Evidence added
* Evidence removed
* Evidence reclassified
* Source corrected
* Provenance corrected
* Limitations discovered
* Relationship to claim changed

Material changes may require:

* New Entry Version
* Evidence Record Version
* Correction Record
* Verification update

depending on impact.

---

# Evidence and Controlled Values

The Controlled Values Registry currently governs Evidence Type.

Canonical initial values are:

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

Evidence Relationship remains a candidate future Controlled Value set.

Evidence pages and schemas should not independently introduce conflicting Evidence Type vocabularies.

---

# Evidence and Event-Type Profiles

An Event-Type Profile may strengthen Evidence requirements.

A Profile may require:

* Specific Evidence Types
* Minimum authoritative Evidence
* Specific Source references
* Provenance minimums
* Evidence Relationship semantics
* Integrity information
* Verification rules

The universal Chronicle Evidence model should remain flexible enough to support these specializations without redefining the canonical Entry.

---

# Production Example — Certification Event

A future production certification Entry might include:

```text
Chronicle Entry:
CHR-2026-0001

Event Type:
Certification Created

Authoritative Evidence:
SC-CERT-2026-0001

Supporting Evidence:
Repository record or public certification page

Evidence Relationship:
Supports

Provenance:
Direct repository access with retrieval date

Limitations:
None known
```

The exact production structure remains subject to the Certification Event-Type Profile and final schema.

---

# Future Development

Future Chronicle Evidence work may include:

* Final Evidence Record schema refinement
* Evidence Relationship Controlled Values
* Preservation State vocabulary
* Event-Type-specific Evidence requirements
* Integrity metadata
* Automated Validation
* Cryptographic integrity verification
* Digital signatures
* Chain-of-custody tracking
* Long-term archival preservation
* Public Evidence discovery where appropriate

Future development should remain aligned with the Satoshium Suite Evidence Standard and Suite authority boundaries.

---

# Guiding Principle

> Evidence supports the historical representation.  
> It does not become the event.

And operationally:

> Preserve the Evidence. Preserve its relationship. Preserve its limitations.

---

## Relationship to Other Chronicle Documentation

Chronicle Evidence should remain aligned with:

* Entry Model
* Preservation Eligibility
* Chronicle Rules
* Identifier Specification
* Controlled Values Registry
* Relationship Model
* Provenance Model
* Sources
* Verification
* Corrections
* Schemas
* Trust Model
* Validation

Evidence is part of Chronicle's supporting-record architecture.

It does not replace the Chronicle Entry as the canonical object.

---

## Status

**Active pre-operational Chronicle Evidence specification.**

This README is aligned with the current Chronicle Entry Model, Controlled Values Registry, Relationship Model, Provenance Model, Source architecture, Preservation Eligibility Model, Chronicle Rules, and Suite Evidence Standard.

Evidence Type is governed through the Controlled Values Registry.

Evidence Relationship values, final Evidence Record schema details, Preservation State values, Validation requirements, and Event-Type-specific Evidence requirements remain subject to later operational-development steps where production use demonstrates a need.
