# Chronicle Evidence

## Purpose

Chronicle Evidence defines how evidence is referenced, described, evaluated, and preserved in support of Chronicle Entries.

Within Chronicle, evidence may support, challenge, contradict, clarify, or contextualize Chronicle's historical representation of a qualifying occurrence.

Chronicle does not create a competing evidence system. Evidence used by Chronicle should align with the Satoshium Suite Evidence Standard and with Suite-wide requirements for traceability, provenance, integrity, structured records, validation, and reference-based interoperability.

Evidence does not determine another Suite system's authoritative outcome.

Instead, Chronicle uses evidence to keep its own historical record transparent, reviewable, and understandable over time.

---

## Suite Alignment

Chronicle Evidence operates within the Satoshium Suite architecture.

Evidence handling should follow Suite-wide expectations for:

* Recognized evidence types
* Evidence quality
* Evidence integrity
* Evidence sufficiency
* Evidence limitations
* Traceability
* Provenance
* Preservation status
* Structured evidence records
* Validation-ready data
* Durable references

Chronicle should inherit the Suite Evidence Standard rather than invent a separate Chronicle-only evidence standard.

---

## What Is Evidence?

Evidence is information, documentation, material, data, testimony, metadata, media, or another approved record that bears on a Chronicle Entry, occurrence, claim, relationship, or historical representation.

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Contextualize
* Corroborate
* Qualify
* Limit confidence

Chronicle should preserve the relationship between the evidence item and the Entry or claim it affects.

Evidence should not be treated as uniformly supportive merely because it is attached to a Chronicle record.

---

## Core Principles

### Preserve Reviewability

Evidence references and material context should remain available whenever practical so future reviewers can understand the basis for Chronicle's historical representation.

### Transparency

Evidence should be clearly described and documented.

Reviewers should be able to determine, where applicable:

* What the evidence is
* Where it originated
* When it was created, obtained, or observed
* How it entered the Chronicle record
* Which Entry or claim it relates to
* Whether it supports, challenges, contradicts, or contextualizes that Entry or claim
* What limitations apply
* Whether the evidence remains available

### Provenance

Evidence provenance should describe how the evidence originated, was obtained, and entered Chronicle.

Provenance is related to, but distinct from, Source.

### Independence

Evidence should remain distinguishable from the conclusions drawn from it.

The existence of an evidence item does not automatically validate a claim.

Likewise, absence of evidence does not automatically prove that an occurrence did not happen.

### Context Matters

Evidence gains meaning through context.

Chronicle should preserve enough context for later reviewers to understand how the evidence related to the historical occurrence at the time.

### Authority Boundaries

Evidence referenced by Chronicle does not transfer authority from another Suite system.

Chronicle may preserve and evaluate evidence relevant to its own Entry while Certifier, Registry, Anchor, Beacon, Attestor, Navigator, Atlas, and other Suite systems retain authority over their own records and determinations.

---

## Recognized Evidence Categories

Chronicle should use evidence categories recognized by the Satoshium Suite Evidence Standard.

Depending on the applicable Suite standard and controlled values, these may include:

### Primary Sources

Materials created directly by participants, systems, institutions, or processes associated with the occurrence.

### Secondary Sources

Materials that analyze, describe, summarize, or report information derived from primary or other sources.

### Institutional Records

Official records produced by an organization, system, government, institution, or Suite component.

### Self-Attestations

Statements or declarations made by the subject, participant, organization, or system associated with the information.

### Cryptographic Records

Evidence supported by hashes, signatures, blockchain records, timestamps, integrity proofs, or other cryptographic mechanisms.

### Metadata

Structured contextual information describing creation, modification, identity, location, version, relationships, or other properties.

### Screenshots and Images

Visual captures used to preserve or document observable information.

### Archives

Archived webpages, records, snapshots, repositories, or other preserved historical materials.

### Audio and Video

Recorded media preserving statements, actions, conditions, broadcasts, demonstrations, or other occurrences.

### Receipts and Transaction Records

Records showing transactions, submissions, processing, issuance, publication, or other documented actions.

### Witness Statements

Statements made by individuals with direct or relevant knowledge.

### Other Approved Evidence Types

Additional evidence types may be recognized through Suite controlled values or Chronicle Event-Type Profiles as the architecture develops.

---

## Evidence Quality

Chronicle should not reduce evidence quality to a simple present/absent determination.

Relevant evidence-quality factors may include:

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

The significance of any factor may vary depending on the type of occurrence and the purpose for which the evidence is being used.

---

## Evidence Limitations

Evidence limitations are part of the historical record and should remain visible.

Examples may include:

* Incomplete evidence
* Conflicting evidence
* Stale evidence
* Missing provenance
* Unverifiable evidence
* Unsupported assertions
* Broken or unavailable references
* Ambiguous authorship
* Uncertain dates
* Limited context
* Altered or derivative materials

Chronicle should disclose material limitations rather than implying certainty that the evidence does not support.

---

## Evidence Integrity

Evidence integrity concerns whether an evidence item remains reviewable and whether its identity, authenticity, completeness, and history can be evaluated.

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

Integrity information supports reviewability but does not automatically establish the truth of every claim associated with an evidence item.

---

## Evidence Record Structure

Evidence referenced by Chronicle should ultimately use structured record concepts compatible with the Suite Evidence Standard.

Expected evidence-record elements may include:

### Source

The origin of the evidence.

### Evidence Type

The controlled evidence category.

### Authority

The authority or institutional weight associated with the evidence source where applicable.

### Date

The relevant creation, publication, collection, observation, or preservation date.

### Relationship to Entry or Claim

How the evidence bears on the Chronicle Entry or specific claim.

### Provenance

How the evidence originated, was obtained, and entered Chronicle.

### Preservation Status

Whether the evidence remains available, archived, referenced, unavailable, superseded, or otherwise preserved.

### Integrity Information

Hashes, signatures, timestamps, version information, or other integrity indicators where applicable.

### Review Notes

Documented limitations, conflicts, context, or review observations.

### Public Reference

A durable public or archival reference where available.

The final schema and controlled values will be defined through Chronicle's operational architecture and applicable Suite standards.

---

## Evidence and Sources

Evidence and Sources are related but distinct.

A Source answers:

> Where did the information originate?

Evidence answers:

> What material bears on the claim or occurrence?

Provenance answers:

> How did that information or evidence originate, move, and enter the Chronicle record?

A single Source may contain multiple evidence items.

Multiple Sources may contribute evidence relevant to one Chronicle Entry.

One evidence item may also relate to multiple claims or Entries.

---

## Evidence and Authoritative Records

An authoritative Suite record is not merely evidence in the same sense as an ordinary supporting item.

For example:

* A Certification Package is authoritative within Certifier for its certification determination.
* An SREG Registry Entry is authoritative within Registry for the registry record.
* An Integrity Reference is authoritative within Anchor for the anchoring function.
* A Trust Statement is authoritative within Attestor for the attestation function.

Chronicle may reference those records both as authoritative sources for the historical occurrence and as part of the evidentiary context.

Chronicle should preserve the distinction between authoritative record and supporting evidence.

---

## Evidence and Verification

Evidence contributes to Chronicle verification.

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

Verification concerns Chronicle's own historical representation.

It does not re-adjudicate an outcome owned by another Suite system.

---

## Evidence and Validation

Validation and evidence review are separate functions.

Evidence review concerns the content, quality, integrity, provenance, limitations, and relationship of evidence.

Validation concerns whether Chronicle's structured record conforms to required schemas, controlled values, required fields, references, and publication rules.

An Entry may contain evidence yet still fail validation.

Likewise, a structurally valid Entry may contain evidence with known limitations.

---

## Evidence, Preservation Eligibility, and Sufficiency

Preservation Eligibility and evidence sufficiency are separate questions.

Preservation Eligibility asks:

> Should Chronicle preserve this occurrence?

Evidence sufficiency asks:

> Is the available evidence adequate for the particular purpose for which it is being used?

A historically significant occurrence may warrant preservation even when evidence is incomplete, disputed, or limited, provided Chronicle records those limitations transparently and follows applicable rules.

Chronicle should not automatically import a Certifier evidence-sufficiency threshold into historical preservation.

Different Chronicle Event-Type Profiles may require different evidence expectations.

---

## Preservation

Chronicle favors durable evidence references and preservation information whenever practical.

Evidence should remain accessible in its original or authoritative form where possible.

When direct preservation of the evidence itself is not appropriate or permitted, Chronicle should preserve enough reference, provenance, metadata, archival information, and integrity information to maintain historical reviewability.

Chronicle should not silently replace earlier evidence with later material.

Changes in evidence availability, provenance, or interpretation may themselves become part of an Entry's historical context.

---

## Corrections and Versioning

New evidence may justify:

* Supplemental context
* A correction
* A new version
* Reverification
* A relationship update
* A new Chronicle Entry describing a later occurrence

Chronicle should correct only its own preservation record.

If another Suite system changes an authoritative record, Chronicle may preserve that later occurrence and update its references according to Chronicle rules.

Substantive changes to Chronicle's evidentiary representation should remain traceable through versioning and correction history.

---

## Future Development

Future Chronicle Evidence work may include:

* Formal evidence schemas
* Controlled evidence types
* Evidence relationship values
* Provenance requirements
* Preservation-status values
* Integrity metadata
* Automated validation
* Cryptographic integrity verification
* Digital signatures
* Chain-of-custody tracking
* Long-term archival preservation
* Event-Type-specific evidence requirements
* Public evidence discovery where appropriate

Future development should remain aligned with the Satoshium Suite Evidence Standard and Suite authority boundaries.

---

## Status

Draft operational specification.

This README has been reconciled with the Satoshium Suite Standards, Methodology, Interoperability, and Evidence Standard architecture, and with the current Chronicle model establishing Chronicle Entry as the canonical Chronicle object.

Evidence schemas, controlled values, preservation rules, validation requirements, and Event-Type-specific evidence requirements may evolve as Chronicle operational development continues.
