# Chronicle Sources

## Purpose

Sources identify where information originated.

Within Satoshium Chronicle, Source Records and external source references support canonical Chronicle Entries by preserving attribution, source identity, temporal context, citation information, limitations, archival state, integrity information, and traceable relationships to the historical record.

A Source helps answer:

> Where did this information come from?

Chronicle preserves source context so future reviewers can understand the origin of information and identify what Chronicle relied upon.

Source identity is distinct from Provenance, Evidence, Verification, and authority.

A Source does not automatically establish truth or transfer institutional authority to Chronicle.

---

## Suite Alignment

Chronicle Sources operate within the Satoshium Suite architecture.

They should align with Suite-wide expectations for:

* Stable identifiers
* Clear source attribution
* Provenance and traceability
* Durable references
* Archival preservation
* Source limitations
* Evidence-aware review
* Validation-ready records
* Version preservation
* Reference-based interoperability
* Clear institutional authority boundaries

Chronicle should not create a competing source-authority model where another Suite system already owns the authoritative object.

---

## Role Within Chronicle

A Source Record is a **supporting Chronicle-owned record**.

It is not the canonical historical-preservation object.

The canonical Chronicle object remains the **Chronicle Entry**.

Conceptually:

```text
Chronicle Entry
      ↓
Source Reference / Relationship
      ↓
Source Record or External Source
```

Source architecture exists to preserve origin and citation context without turning every source into Evidence or every referenced record into Chronicle authority.

---

# Source Contexts

Chronicle distinguishes three principal source contexts.

## Authoritative Source Record

An **Authoritative Source Record** is a Chronicle Source Record that documents an authoritative object or authoritative institutional source used by a Chronicle Entry.

Examples may include Source Records documenting:

* Certification Packages
* SREG Registry Entries
* Integrity References
* Discovery Signals
* Discovery Metadata
* Trust Statements
* Workflow Definitions
* Atlas authoritative records
* Other institutional records owned by an originating authority

The Chronicle Source Record documents the source relationship.

Authority remains with the originating institution or Suite system.

Conceptually:

```text
Chronicle Source Record
      ↓ references
Authoritative External Object
      ↓
Authority remains with originating system
```

A Chronicle Source Record does not recreate, supersede, or transfer that authority.

---

## Supporting Source

A **Supporting Source** provides information useful to a Chronicle Entry without being the authoritative object for the underlying action or determination.

A Supporting Source may provide:

* Context
* Corroboration
* Background
* Attribution
* Temporal detail
* Interpretation
* Archival support
* Additional factual detail

Examples may include:

* Institutional documents
* Public webpages
* Research publications
* Archived copies
* Repository records
* Reports
* Statements
* Secondary sources

Supporting status does not imply weak quality.

It means the Source does not own the authoritative institutional determination being preserved.

---

## Referenced External Source

A **Referenced External Source** is a Source outside Chronicle—and possibly outside the Satoshium Suite—that is cited or referenced directly without necessarily creating a separate Chronicle Source Record.

A direct external reference may be appropriate when:

* The Source is stable
* The Source is narrowly used
* The Source is easily identifiable
* A separate Source Record would add little durable value
* No independent Chronicle lifecycle is needed for the Source
* The applicable Event-Type Profile does not require a Source Record

Examples may include:

* Public institutional webpages
* External reports
* Government publications
* Repository objects
* Public datasets
* External archives

Chronicle should create a Source Record when structured source identity, attribution, archival context, limitations, Provenance, reuse, Validation, or preservation needs justify one.

Conceptually:

> Use structure when structure adds durable historical value.

---

# What Is a Source?

A Source is the origin of information referenced by Chronicle.

Sources may contain or provide:

* Facts
* Claims
* Statements
* Observations
* Records
* Publications
* Metadata
* Context
* Evidence
* Archival material
* Authoritative Suite objects

A Source does not automatically establish truth.

Instead, it establishes origin.

Understanding origin is essential for evaluating context, reliability, Evidence, Provenance, and historical meaning.

---

# Source, Evidence, Provenance, and Verification

These concepts are related but distinct.

## Source

Answers:

> Where did the information come from?

## Evidence

Answers:

> What material bears on the Chronicle Entry, claim, or Occurrence?

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Corroborate
* Contextualize
* Limit confidence

## Provenance

Answers:

> How did the information or Evidence originate, move, and enter Chronicle?

## Verification

Answers:

> Has Chronicle adequately reviewed its own historical representation?

Conceptually:

```text
Source = Origin
Evidence = Material bearing on the Entry or claim
Provenance = Information path
Verification = Review of Chronicle's representation
```

A single Source may contain multiple Evidence items.

A single Evidence item may depend on one or more Sources.

A Source Record should not replace an Evidence Record or Provenance structure where those functions require separate representation.

---

# Core Principles

## Attribution

Information should be traceable to its origin whenever possible.

Chronicle should preserve who created, published, distributed, recorded, or otherwise originated the information being referenced.

---

## Source Identity

A Source should be identifiable independently of Chronicle where possible.

Source identity may include:

* Stable institutional identifier
* Repository identifier
* Archive identifier
* Dataset identifier
* Suite identifier
* Document title
* Creator
* Publisher
* Publication date
* Stable URI or other locator

A URL may assist retrieval but should not be treated as the sole identity of a Source when a more durable identifier exists.

---

## Provenance

Source identity alone is not enough.

Chronicle should preserve how information:

* Was discovered
* Was accessed
* Was captured
* Was transferred
* Was transformed where applicable
* Was archived
* Entered Chronicle
* Was preserved over time

The formal Provenance Model governs these requirements.

---

## Transparency

Source relationships should remain understandable and reviewable.

Reviewers should be able to determine, where applicable:

* What the Source is
* Who created it
* Who published it
* When it was created
* When it was published
* When Chronicle accessed or retrieved it
* Where it can be found
* What stable identifier exists
* What archival reference exists
* What limitations exist
* How it relates to Chronicle Entries and Evidence Records

---

## Preservation

Durable source references and source context should remain available whenever practical.

When direct preservation is appropriate and permitted, Chronicle may preserve archival or captured representations.

Where direct preservation is not appropriate, Chronicle should preserve enough identifying and provenance information to support future review.

---

## Independence

Recording a Source does not imply endorsement.

A disputed, incomplete, biased, superseded, or contradictory Source may still remain historically relevant.

---

## Authority Boundaries

A Source may be authoritative within another Suite system or external institution.

That authority remains with the originating system.

Chronicle Source Records do not recreate or transfer external institutional authority.

Conceptually:

> Reference does not transfer authority.

---

# Source Type and Source Role

Source Type and Source Role are separate concepts.

## Source Type

Source Type describes what the Source is.

The Chronicle Controlled Values Registry currently establishes initial Source Type values:

```text
Authoritative Record
Institutional Document
Web Page
Repository Record
Dataset
Archive
Statement
Other
```

These should be used where applicable in production schemas and Validation.

---

## Source Role

Source Role describes how the Source functions in relation to a Chronicle Entry or Evidence Record.

Potential roles may include:

```text
Authoritative
Supporting
Primary
Secondary
Contextual
Archival
Corroborating
Reference
```

These are not yet frozen as a canonical Controlled Value set.

Source Role should be formalized only when production use demonstrates that stable machine-readable role semantics are necessary.

Source Type should not be used as a substitute for Source Role.

---

# Authoritative Sources

Some Sources are authoritative objects maintained by another Suite system.

Examples may include:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Discovery Metadata
* Trust Statement
* Workflow Definition
* Atlas record

Chronicle may preserve either:

* A Chronicle Source Record documenting the authoritative Source
* A direct authoritative reference when a separate Source Record is unnecessary

Their authority comes from the originating system.

A Chronicle Source Record does not:

* Recreate that authority
* Supersede the authoritative object
* Control the object's lifecycle
* Reinterpret the originating system's institutional determination

---

# Citation and Reference Expectations

Chronicle should cite or reference Sources with enough specificity to support:

* Identification
* Retrieval
* Independent review
* Provenance
* Long-term traceability

The citation or reference should preserve, where applicable:

```text
Source identity
Creator / publisher
Stable identifier
Source location
Relevant source date
Chronicle retrieval / access date
Archive reference
Known limitations
```

A citation does not need to reproduce the Source.

It should preserve enough information for a future reviewer to determine what Chronicle relied upon.

---

## Stable Identifier Preferred

When a Source has a stable identifier, Chronicle should preserve it.

Examples may include:

* Suite identifier
* Repository identifier
* Archive identifier
* Government record identifier
* Dataset identifier
* DOI-like identifier
* Commit identifier

A stable identifier is preferable to relying solely on:

* Display title
* Filename
* URL
* Human description

---

## URLs Are Locations, Not Identity

A URL may change while the Source remains the same.

Chronicle should therefore treat URLs primarily as retrieval locations.

When a more durable identifier exists, that identifier should also be preserved.

---

## Archive References

When a Source is unstable, no longer live, or historically important, Chronicle should preserve an archive reference when practical.

Archive information may include:

* Archive service
* Snapshot identifier
* Capture date
* Archived URL
* Repository snapshot
* Institutional preservation location

---

## Retrieval Dates

Sources whose content may change over time should record Chronicle's retrieval or access date.

The retrieval date belongs primarily to Provenance but may also appear in citation context.

It must remain distinct from:

* Source creation date
* Source publication date
* Event Date
* Entry creation date
* Publication date

---

# When a Source Record Is Required

A separate Chronicle Source Record should be created when one or more of the following applies:

* Source identity requires structured preservation
* Attribution requires structured fields
* Source limitations are material
* Provenance is complex
* The Source is reused across Entries
* Archival context is important
* Integrity metadata is important
* Independent Source Record Versioning is needed
* Event-Type Profile requires it
* Validation rules require it
* Public Source discovery may later depend on it

A simple direct external reference may be sufficient where those conditions do not apply.

---

# Source and Evidence

Sources and Evidence remain distinct.

Examples:

* A webpage may be a Source.
* A screenshot from that webpage may be Evidence.
* A report may be a Source.
* A table within the report may be Evidence.
* A Certification Package may be an authoritative Source and also provide evidentiary support.
* A news article may be a Source containing claims, images, quotations, or records that may function as Evidence.

Chronicle should preserve the distinction rather than treating every Source as Evidence or every Evidence item as a Source.

---

# Source and Provenance

Source identity and Provenance remain distinct even when stored near one another.

Example:

```text
Source:
SC-CERT-2026-0001

Provenance:
Accessed directly from the Certifier repository on the recorded retrieval date
```

Source identifies origin.

Provenance records the path.

---

# Source and Verification

Verification may review aspects of Source identity and Source support.

Chronicle Verification may examine:

* Source existence
* Attribution
* Creator identity
* Publisher identity
* Publication date
* Access consistency
* Capture consistency
* Archival consistency
* Provenance
* Corroboration
* Source limitations
* Internal consistency
* Authoritative status

Verification does not replace the Source Record.

Verification also does not convert a Supporting Source into an authoritative record.

---

# Validation

Validation is distinct from Verification.

Validation determines whether the Source Record or source reference conforms to Chronicle structural and procedural requirements.

Validation may include:

* Identifier integrity
* Schema conformance
* Required fields
* Controlled Values
* Source-location integrity
* Stable-reference integrity
* Archive-reference integrity
* Related-entry integrity
* Provenance requirements
* Preservation-status requirements
* Version linkage
* Event-Type Profile requirements
* Publication readiness

Conceptually:

> Verification ≠ Validation

---

# Preservation State

Preservation State describes the continuing availability or archival condition of the Source.

Potential concepts may include:

* Available
* Archived
* Captured Copy
* Referenced Only
* Unavailable
* Superseded
* Preserved Copy

These values are not yet frozen.

If production use requires a stable vocabulary, they should be added to the Controlled Values Registry.

Preservation State is distinct from:

* Verification State
* Validation State
* Publication State
* Source lifecycle state

---

# Source Relationships

Source Records may relate to:

* Chronicle Entries
* Evidence Records
* Verification Records
* Correction Records
* Other Source Records
* Authoritative Suite objects
* Archived representations
* Provenance structures

The Chronicle Relationship Model governs structured relationship semantics.

Relationships should use approved Controlled Values where direction or meaning matters.

---

# Source Limitations

Sources are not always complete, current, independent, or available.

Potential limitations may include:

* Missing information
* Incomplete records
* Bias
* Errors
* Conflicting accounts
* Limited availability
* Broken references
* Ambiguous authorship
* Uncertain publication date
* Missing Provenance
* Archived copy only
* Secondary or derivative status
* Altered or reformatted representation
* Limited context

Chronicle should document material limitations transparently.

A limitation does not necessarily disqualify a Source.

It becomes part of the historical review context.

---

# Source Reliability

Chronicle may preserve reliability notes where useful.

Reliability assessment may consider:

* Authority
* Independence
* Completeness
* Consistency
* Corroboration
* Provenance
* Availability
* Temporal proximity
* Authenticity
* Known conflicts

Reliability notes should not become a universal numerical trust score unless a formal Suite standard explicitly requires one.

---

# Source Integrity

Where available and appropriate, Chronicle may preserve:

* Checksums
* Digital signature references
* Archive references
* Capture metadata
* Preservation notes
* Chain-of-custody information
* Integrity notes
* Repository commits
* Anchor references

Integrity mechanisms improve reviewability.

They do not replace Provenance or institutional authority.

---

# Source Record Lifecycle

A generalized Source Record lifecycle may include:

1. Source identified
2. Source context determined
3. Source Type classified
4. Source Role classified where applicable
5. Creator and publisher documented
6. Temporal information recorded
7. Stable identity or location established
8. Citation/reference information recorded
9. Provenance documented
10. Entry and Evidence relationships established
11. Limitations documented
12. Integrity or archival information recorded where applicable
13. Verification performed where applicable
14. Validation performed
15. Source Record published, retained privately, or otherwise applied according to Chronicle rules
16. Source Record maintained
17. Corrections or Versioning applied when necessary
18. Preservation State maintained

Not every Source Record will require every step.

---

# Source Versioning

Source Records may evolve when:

* Source location changes
* An archive becomes available
* Provenance improves
* Creator or publisher information is corrected
* New limitations are discovered
* Preservation State changes
* Relationships change
* Verification results change
* Stable identifiers are added

Material changes should remain traceable.

Chronicle should preserve prior substantive Source Record states where required.

Schema Version and Source Record Version remain separate concepts.

---

# Preservation Philosophy

Chronicle should preserve durable source references and source context whenever practical.

Where direct preservation is appropriate and permitted:

* Original material should remain available
* Archive references should remain maintained
* Provenance should remain documented
* Integrity information should remain available
* Source limitations should remain visible
* Relationships to Entries and Evidence should remain intact
* Prior substantive Source Record states should remain traceable

Where direct preservation is not appropriate or possible, Chronicle should preserve enough durable identity, reference, metadata, Provenance, archival information, and preservation context to support future review.

A Source becoming unavailable should not silently erase its historical role.

---

# Relationship to the Chronicle Entry Model

The Chronicle Entry Model defines:

```text
Source Record References [Conditional]
```

A production Chronicle Entry should reference Source Records when Source Records are used to establish origin, attribution, archival context, or supporting historical information.

An Event-Type Profile may convert Source Record References from Conditional to Required.

The Certification Event-Type Profile may require authoritative Certifier references even where separate Source Records remain unnecessary.

---

# Relationship to the Provenance Model

The Provenance Model establishes a universal minimum for every production Chronicle Entry:

```text
Origin
Acquisition / Access Method
Capture / Retrieval Date
Source or Authoritative Record Reference when available
Provenance Limitations when applicable
```

Source architecture should supply the Source identity required by that model.

It should not duplicate the entire provenance path inside Source fields.

---

# Relationship to Controlled Values

The Chronicle Controlled Values Registry currently establishes the following Source Type values:

```text
Authoritative Record
Institutional Document
Web Page
Repository Record
Dataset
Archive
Statement
Other
```

Source Role remains a candidate future Controlled Value set.

Source pages and schemas should not invent competing Source Type vocabularies independently.

---

# Relationship to the Relationship Model

The Relationship Model governs how Chronicle Entries connect to:

* Source Records
* Registry Entries
* Other Chronicle Entries
* Authoritative Suite objects
* Supporting records

Source references should use approved Relationship Types where structured relationship semantics are needed.

Potential relevant types include:

```text
References
Derived From
Related To
```

Relationship semantics should not replace Source identity or Provenance.

---

# Future Development

Future Chronicle Sources work may include:

* Final Source Record identifier architecture
* Controlled Source Roles
* Formal Source Record schema refinement
* Source validation rules
* Archival-reference structures
* Automated source capture
* Archive integration
* Integrity metadata
* Cryptographic timestamping
* Source availability monitoring
* Cross-system reference validation
* Public source discovery where appropriate

These should be added only where production experience demonstrates a need.

---

## Guiding Principle

> Identify the Source.  
> Preserve the reference.  
> Trace the path.  
> Keep authority visible.

---

## Status

**Active pre-operational Chronicle Sources specification.**

This README is aligned with the current Chronicle Entry Model, Provenance Model, Relationship Model, Controlled Values Registry, Identifier Specification, Chronicle Rules, Evidence architecture, and Suite authority boundaries.

Source Type values are governed through the Controlled Values Registry.

Source Role, Preservation State, Source Record identifier architecture, final Source Record schema details, and Event-Type-specific Source requirements remain subject to later operational-development steps where production use demonstrates a need.
