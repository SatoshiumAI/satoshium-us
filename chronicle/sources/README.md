# Chronicle Sources

## Purpose

Sources identify where information originated.

Within Satoshium Chronicle, Source Records support canonical Chronicle Entries by preserving attribution, location, temporal context, provenance, limitations, archival state, integrity information, and traceable relationships to the information being used.

A source helps answer:

> Where did this information come from?

Chronicle preserves source context so future reviewers can understand not only the origin of information, but also how it was accessed, captured, preserved, related to evidence, and connected to the Chronicle historical record.

A source does not automatically establish truth or transfer institutional authority to Chronicle.

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
Source Relationship
      ↓
Source Record
```

Source Records exist to preserve origin, attribution, provenance, archival context, limitations, and traceable relationships needed to support Chronicle Entries.

---

## What Is a Source?

A source is the origin of information referenced by Chronicle.

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

A source does not automatically establish truth.

Instead, it establishes origin.

Understanding origin is essential for evaluating context, reliability, evidence, provenance, and historical meaning.

---

## Source, Evidence, and Provenance

Source, Evidence, and Provenance are related but distinct.

### Source

Answers:

> Where did the information come from?

### Evidence

Answers:

> What material bears on the Chronicle Entry, claim, or occurrence?

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Corroborate
* Contextualize
* Limit confidence

### Provenance

Answers:

> How did the information or evidence originate, move, and enter Chronicle?

A single source may contain multiple evidence items.

A single evidence item may depend on one or more sources.

A Source Record should not replace an Evidence Record or a Provenance structure where those functions require separate representation.

---

## Core Principles

### Attribution

Information should be traceable to its origin whenever possible.

Chronicle should preserve who created, published, distributed, recorded, or otherwise originated the information being referenced.

### Provenance

Source identity alone is not enough.

Chronicle should preserve how the source:

* Was discovered
* Was accessed
* Was captured
* Was transferred
* Was archived
* Entered Chronicle
* Was preserved over time

### Transparency

Source relationships should remain understandable and reviewable.

Reviewers should be able to determine:

* What the source is
* Who created it
* Who published it
* When it was created
* When it was published
* When it was accessed
* When it was captured
* Where it can be found
* What limitations exist
* How it relates to Chronicle Entries and Evidence Records

### Preservation

Durable source references and source context should remain available whenever practical.

When direct preservation is appropriate and permitted, Chronicle should preserve archival or captured representations.

### Independence

Recording a source does not imply endorsement.

A disputed, incomplete, biased, or superseded source may still remain historically relevant.

### Authority Boundaries

A source may be authoritative within another Suite system.

That authority remains with the originating system.

Chronicle Source Records do not recreate or transfer external institutional authority.

---

## Source Type and Source Role

Source Type and Source Role are separate concepts.

### Source Type

Describes what the source is.

Potential types may include:

* Webpage
* Document
* Publication
* Archive
* Database
* Public Record
* Institutional Record
* Repository
* Dataset
* Statement
* Interview
* Broadcast
* Other Approved Source

### Source Role

Describes how the source functions in relation to a Chronicle Entry or Evidence Record.

Potential roles may include:

* Primary Source
* Secondary Source
* Contextual Source
* Archival Source
* Authoritative Source
* Corroborating Source
* Reference Source

The final values should be governed through Chronicle Controlled Values.

Source Type should not be used as a substitute for Source Role.

---

## Authoritative Sources

Some sources are authoritative objects maintained by another Suite system.

Examples may include:

* Certification Package
* SREG Registry Entry
* Integrity Reference
* Discovery Signal
* Discovery Metadata
* Trust Statement
* Workflow Definition
* Atlas record

Chronicle may reference those objects as sources.

Their authority comes from the originating system.

A Chronicle Source Record does not:

* Recreate that authority
* Supersede the authoritative object
* Control the object's lifecycle
* Reinterpret the originating system's institutional determination

Reference does not transfer authority.

---

## Source Categories

Chronicle may reference or preserve many forms of source information.

### Web Sources

Examples:

* Websites
* Public webpages
* Blogs
* Online publications
* Repositories
* Public databases

### Documents and Publications

Examples:

* Reports
* Letters
* Contracts
* Research publications
* Institutional documents
* Official records

### Archival Sources

Examples:

* Preserved webpages
* Historical collections
* Archived documents
* Repository snapshots
* Institutional archives

### Public and Institutional Records

Examples:

* Government filings
* Registrations
* Regulatory records
* Court records
* Legislative records
* Suite authoritative objects

### Media Sources

Examples:

* Interviews
* Broadcasts
* Audio recordings
* Video recordings
* Presentations

### Data Sources

Examples:

* Databases
* Datasets
* Structured repositories
* Metadata records

### Statements and Testimonial Sources

Examples:

* Recorded statements
* Interviews
* Witness accounts
* Public declarations

These categories describe source form.

They do not automatically determine source role or evidentiary weight.

---

## Source and Evidence

Sources and Evidence remain distinct.

A Source identifies where information originated.

Evidence describes material that bears on a Chronicle Entry or claim.

Examples:

* A webpage may be a Source.
* A screenshot from that webpage may be Evidence.
* A report may be a Source.
* A table within the report may be Evidence.
* A Certification Package may be an authoritative Source and also provide strong evidentiary support.
* A news article may be a Source containing multiple claims, images, quotations, or records that may function as Evidence.

Chronicle should preserve the distinction rather than treating every Source as Evidence or every Evidence item as a Source.

---

## Source and Verification

Verification may review aspects of a Source Record.

Chronicle verification may examine:

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

Verification does not replace the Source Record.

Verification also does not convert the Source into Chronicle authority.

---

## Validation

Validation is distinct from Verification.

Validation determines whether the Source Record conforms to Chronicle structural and procedural requirements.

Validation may include:

* Identifier integrity
* Schema conformance
* Required fields
* Controlled values
* Source-location integrity
* Archive-reference integrity
* Related-entry integrity
* Provenance requirements
* Preservation-status requirements
* Version linkage
* Publication readiness

Conceptually:

> Verification ≠ Validation

---

## Preservation State

Preservation State describes the continuing availability or archival condition of the source.

Potential concepts may include:

* Available
* Archived
* Captured Copy
* Referenced Only
* Unavailable
* Superseded
* Preserved Copy

The final values should be governed through Chronicle Controlled Values.

Preservation State is distinct from:

* Verification State
* Validation State
* Publication State
* Source lifecycle state

Conceptually:

> Verification ≠ Validation ≠ Preservation State

---

## Source Relationships

Source Records may relate to:

* Chronicle Entries
* Evidence Records
* Verification Records
* Correction Records
* Other Source Records
* Authoritative Suite objects
* Archived representations
* Provenance structures

These relationships help establish a broader historical context.

Relationships should use controlled values where direction or meaning matters.

---

## Source Limitations

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
* Missing provenance
* Archived copy only
* Secondary or derivative status
* Altered or reformatted representation
* Limited context

Chronicle should document material limitations transparently.

A limitation does not necessarily disqualify a source.

It becomes part of the historical review context.

---

## Source Reliability

Chronicle may preserve reliability notes where useful.

Reliability assessment should consider context such as:

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

Reliability notes should not be treated as a universal truth score unless a formal Suite standard explicitly requires one.

---

## Source Integrity

Where available and appropriate, Chronicle may preserve:

* Checksums
* Digital signature references
* Archive references
* Capture metadata
* Preservation notes
* Chain-of-custody information
* Integrity notes

Integrity mechanisms improve reviewability.

They do not replace provenance or institutional authority.

---

## Source Record Lifecycle

A generalized Source Record lifecycle may include:

1. Source identified
2. Source type classified
3. Source role classified
4. Creator and publisher documented
5. Temporal information recorded
6. Source location established
7. Provenance documented
8. Entry and Evidence relationships established
9. Limitations documented
10. Integrity or archival information recorded
11. Verification performed where applicable
12. Validation performed
13. Source Record published, retained privately, or otherwise applied according to Chronicle rules
14. Source Record maintained
15. Corrections or versioning applied when necessary
16. Preservation State maintained

Not every Source Record will require every step.

---

## Source Versioning

Source Records may evolve when:

* Source location changes
* An archive becomes available
* Provenance improves
* Creator or publisher information is corrected
* New limitations are discovered
* Preservation State changes
* Relationships change
* Verification results change

Material changes should remain traceable.

Chronicle should preserve prior substantive Source Record states where required.

Schema versioning and Source Record versioning are separate concepts.

---

## Preservation Philosophy

Chronicle should preserve durable source references and source context whenever practical.

Where direct preservation is appropriate and permitted:

* Original material should remain available
* Archive references should remain maintained
* Provenance should remain documented
* Integrity information should remain available
* Source limitations should remain visible
* Relationships to Entries and Evidence should remain intact
* Prior substantive Source Record states should remain traceable

Where direct preservation is not appropriate or possible, Chronicle should preserve enough durable reference, metadata, provenance, archival information, and preservation context to support future review.

A source becoming unavailable should not silently erase its historical role.

---

## Relationship to Chronicle

Chronicle preserves qualifying historical occurrences through Chronicle Entries.

Source Records help explain where the information used to create, verify, contextualize, or maintain those Entries originated.

Conceptually:

```text
Chronicle Entry
    ├── Source Records
    ├── Evidence Records
    ├── Provenance
    ├── Verification
    ├── Corrections
    └── Authoritative References
```

Source Records are part of the supporting Chronicle architecture.

They do not replace Chronicle Entry as the canonical object.

---

## Future Development

Future Chronicle Sources work may include:

* Final Source Record identifier architecture
* Controlled Source Types
* Controlled Source Roles
* Formal provenance structures
* Source validation rules
* Archival-reference structures
* Automated source capture
* Archive integration
* Integrity metadata
* Cryptographic timestamping
* Source availability monitoring
* Cross-system reference validation
* Public source discovery where appropriate

---

## Status

**Architectural draft — not yet a frozen production specification.**

This README has been reconciled with the revised Chronicle Sources public page, the current Source Record Schema, Chronicle Evidence architecture, Chronicle Records model, Chronicle Base Schema direction, and Satoshium Suite Standards, Methodology, Schemas Standard, Evidence Standard, and Interoperability principles.

The final identifier format, controlled values, Source Type and Source Role vocabularies, provenance requirements, validation rules, Preservation State values, versioning conventions, and publication requirements must be settled through the remaining Chronicle operational-development steps before Sources become production authoritative.
