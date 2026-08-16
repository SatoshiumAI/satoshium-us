# Chronicle Rules

## Purpose

Chronicle Rules consolidates the normative operating rules governing Satoshium Chronicle.

These Rules define what Chronicle:

* Must do
* Must not do
* Should do
* Should ordinarily avoid

during creation, maintenance, correction, publication, and preservation of Chronicle-owned records.

The Rules are intended to prevent operational drift and maintain consistent institutional behavior across Chronicle.

They consolidate normative requirements that might otherwise become scattered across:

* Purpose
* Scope
* Entry Model
* Event Type Framework
* Preservation Eligibility
* Sources
* Evidence
* Verification
* Corrections
* Schemas
* Integration
* Historical Preservation
* Trust Model
* Production procedures

Chronicle should not create separate Policies and Governance pages unless later operational experience demonstrates a distinct institutional need.

---

# Rule Hierarchy

Chronicle Rules operate within the broader Satoshium Suite architecture.

Conceptually:

```text
Suite Standards
Suite Methodology
Suite Interoperability
Suite Evidence Standard
Suite Schemas Standard
        ↓
Chronicle Rules
        ↓
Chronicle Procedures
        ↓
Schemas / Controlled Values / Validation
        ↓
Production Chronicle Records
```

Chronicle Rules must not contradict controlling Suite-level architecture.

Where a conflict exists, the controlling Suite authority prevails unless the Suite architecture is formally revised.

---

# Rule 1 — Canonical Object

Chronicle has one canonical historical-preservation object:

> Chronicle Entry

Chronicle must not create a competing canonical object such as:

* Chronicle Event
* Historical Event Record
* Event Record
* Historical Record Object

The Occurrence is what happened.

The Chronicle Entry is Chronicle's canonical structured representation of that qualifying Occurrence.

---

# Rule 2 — Preservation Eligibility Before Entry Creation

A canonical Chronicle Entry must not be created unless the underlying Occurrence satisfies Preservation Eligibility.

Conceptually:

```text
Occurrence
    ↓
Preservation Eligibility
    ↓
Chronicle Entry
```

Chronicle should not create a record first and decide afterward whether the Occurrence belonged in Chronicle.

---

# Rule 3 — Entry Model Conformance

Every production Chronicle Entry must conform conceptually to the Chronicle Entry Model.

Required components include:

* Identity
* Event Representation
* Temporal Information
* Event Type
* Historical Context
* Provenance
* Verification
* Version
* Publication State
* Lifecycle / Status

Conditional components must be present when applicable.

These may include:

* Source Record References
* Relationships
* Evidence
* Correction History

---

# Rule 4 — Event Type Is Classification

Event Type must be treated as a classification system.

It is not a separate canonical object.

Every production Chronicle Entry must use an approved Event Type Controlled Value.

Event-Type Profiles may strengthen Entry requirements but must not create competing canonical objects.

---

# Rule 5 — Authority Boundaries

Chronicle must remain authoritative only for Chronicle-owned records and Chronicle historical-preservation state.

Chronicle must not assume or recreate authority belonging to another Suite system.

Examples:

```text
Certifier → Certification Package / certification determination
Registry  → SREG Registry Entry / Registry lifecycle
Anchor    → Integrity Reference
Beacon    → Discovery Signal / Discovery Metadata
Attestor  → Trust Statement / attestation
Navigator → Workflow Definition / orchestration
Atlas     → Atlas authoritative records and intelligence
Chronicle → Chronicle Entry / Chronicle preservation state
```

Conceptually:

> Reference does not transfer authority.

---

# Rule 6 — Reference Rather Than Duplicate

Chronicle should reference authoritative external objects rather than duplicate or recreate them.

A Chronicle Entry may preserve:

* Authoritative record identifier
* Relationship to the external object
* Historical context
* Relevant Provenance
* Relevant Source or Evidence relationships

Chronicle should not copy another system's full authoritative object merely to make Chronicle self-contained.

---

# Rule 7 — Source Record Referencing

Chronicle should use Source Records when origin, attribution, access history, archival context, limitations, or traceability needs distinct structured representation.

A Source Record must remain distinct from:

* Evidence Record
* Provenance
* Authoritative Record
* Chronicle Entry

Source answers:

> Where did the information come from?

---

# Rule 8 — Source Does Not Equal Authority

A Source must not be treated as authoritative merely because Chronicle references it.

A Source may be:

* Authoritative
* Non-authoritative
* Primary
* Secondary
* Contextual
* Archival
* Corroborating
* Other approved role

Source Role and Source Type should be governed separately.

---

# Rule 9 — Evidence Must Remain Distinct

Evidence must remain distinct from Source and Provenance.

Evidence answers:

> What material bears on the Chronicle Entry or claim?

Evidence may:

* Support
* Challenge
* Contradict
* Clarify
* Corroborate
* Contextualize
* Limit confidence

Chronicle must not automatically treat all Source material as Evidence.

---

# Rule 10 — Evidence Limitations Must Remain Visible

Material Evidence limitations should remain visible.

Examples may include:

* Incompleteness
* Bias
* Conflicting material
* Missing Provenance
* Limited authenticity
* Secondary status
* Unavailable original artifact
* Archival-only representation

Chronicle should not conceal uncertainty merely to make the historical record appear more certain.

---

# Rule 11 — Preservation Eligibility Is Distinct From Evidence Sufficiency

Historical importance and Evidence quality are separate questions.

An Occurrence may be:

* Historically significant but incompletely evidenced
* Strongly evidenced but historically trivial
* Authoritatively established but outside Chronicle Scope
* Disputed but historically important

Chronicle must not use Evidence sufficiency as a substitute for Preservation Eligibility.

---

# Rule 12 — Automatic Preservation Must Be Explicitly Approved

Chronicle must not assume that every Occurrence matching an Event Type is automatically eligible for preservation.

Automatic Preservation Classes may exist only when explicitly approved.

Until approved:

* Eligibility remains discretionary or rule-based
* Historical Significance may be considered
* Exclusion criteria remain applicable

---

# Rule 13 — Routine Activity Is Not Automatically History

Routine activity should ordinarily remain outside Chronicle.

Potential examples include:

* Automated checks
* Routine validation
* Ordinary metadata updates
* Standard deployment actions
* Formatting changes
* Routine lifecycle administration
* Internal file movement
* Standard system maintenance

Routine activity may become preservable when specific historical context creates significance.

---

# Rule 14 — One Occurrence, One Canonical Entry

Chronicle should ordinarily create one canonical Chronicle Entry for one underlying Occurrence.

Conceptually:

```text
One Occurrence
    ↓
One Canonical Chronicle Entry
    ├── Multiple Sources
    ├── Multiple Evidence Records
    ├── Multiple Relationships
    └── Multiple Authoritative References
```

Multiple records describing the same Occurrence should not automatically create multiple Entries.

---

# Rule 15 — Distinct Occurrences Require Distinct Eligibility Review

Related Occurrences involving the same authoritative object may require separate Chronicle Entries.

Example:

```text
Certification Created
Certification Suspended
Certification Revoked
```

These are distinct Occurrences.

Each must satisfy applicable Preservation Eligibility unless governed by an approved Automatic Preservation Class.

---

# Rule 16 — Relationship Integrity

Relationships must represent real, supportable connections.

Chronicle should not infer:

* Causation
* Authority
* Ownership
* Dependency
* Succession
* Supersession
* Equivalence

merely because two records are associated.

Relationship semantics should be governed through Controlled Values where meaning or direction matters.

---

# Rule 17 — Relationships Must Not Replace Event Type

Event Type and Relationships serve different functions.

### Event Type

Classifies the Occurrence.

### Relationship

Describes how records or objects connect.

Chronicle must not create Event Types merely to encode relationships.

---

# Rule 18 — Provenance Is Required

Every production Chronicle Entry must contain sufficient Provenance to explain how supporting information, authoritative references, Sources, Evidence, or historical material entered Chronicle.

Provenance answers:

> How did the information get here?

Provenance may include:

* Originating system
* Originating institution
* Access path
* Acquisition method
* Capture method
* Transfer history
* Archive path
* Preservation history

---

# Rule 19 — Verification Reviews Chronicle

Verification must review Chronicle's own historical representation.

It may examine:

* Authoritative references
* Sources
* Evidence
* Provenance
* Temporal consistency
* Relationship integrity
* Known limitations
* Contradictions
* Internal consistency

Verification must not re-adjudicate another Suite system's authoritative determination.

---

# Rule 20 — Validation Is Distinct From Verification

Chronicle must distinguish Verification from Validation.

### Verification

Reviews historical representation.

### Validation

Determines structural and procedural conformance.

Conceptually:

```text
Verification ≠ Validation
```

A record may pass one and fail the other.

---

# Rule 21 — Chronicle Corrects Only Chronicle-Owned Records

Chronicle may correct:

* Chronicle Entries
* Source Records
* Evidence Records
* Correction Records
* Other Chronicle-owned supporting records

Chronicle must not use its Correction process to modify:

* Certification Packages
* SREG Registry Entries
* Integrity References
* Trust Statements
* Discovery Signals
* Workflow Definitions
* Atlas records
* Other external authoritative objects

---

# Rule 22 — No Silent Substantive Rewriting

Substantive corrections must remain historically traceable.

Conceptually:

```text
Prior Version
    ↓
Correction Record
    ↓
Resulting Version
```

Chronicle should preserve:

* Correction reason
* Prior state
* Corrected state
* Relevant Evidence
* Version linkage
* Publication history

---

# Rule 23 — Minor Corrections May Use Simplified Procedure

Non-substantive changes may be handled differently from material corrections.

Potential minor changes may include:

* Typographical corrections
* Formatting
* Non-semantic presentation fixes
* Other approved minor metadata changes

The boundary between minor and substantive Correction should be defined operationally.

Minor correction handling must not become a mechanism for hiding substantive change.

---

# Rule 24 — Version Must Remain Distinct From Schema Version

Every production Chronicle Entry must identify its record Version.

Record Version must remain distinct from Schema Version.

Conceptually:

```text
Entry Version ≠ Schema Version
```

A record may change without a schema change.

A schema may change while a record remains unchanged.

---

# Rule 25 — Event Date Must Remain Distinct From Chronicle Dates

Chronicle must distinguish the date of the underlying Occurrence from Chronicle's own recordkeeping dates.

Conceptually:

```text
Event Date
≠ Entry Creation Date
≠ Publication Date
≠ Correction Date
≠ Version Date
```

This rule is mandatory for retrospective preservation.

---

# Rule 26 — Publication Is a Controlled Institutional Action

A file existing publicly does not by itself define Chronicle Publication.

Publication should occur only after applicable requirements are satisfied.

Potential prerequisites include:

* Entry identity
* Event Type
* Preservation Eligibility
* Required authoritative references
* Provenance
* Verification
* Validation
* Required Relationships
* Required Evidence
* Approval
* Publication metadata

---

# Rule 27 — Publication State Must Remain Distinct

Publication State must remain distinct from:

* Verification State
* Validation State
* Lifecycle State
* Preservation State
* Status of the underlying external object

These concepts must not be collapsed into a single generic status.

---

# Rule 28 — Publication Does Not Transfer Authority

Publishing a Chronicle Entry does not make Chronicle authoritative for the underlying external object or determination.

Publication means Chronicle has published its historical-preservation record.

Nothing more should be inferred.

---

# Rule 29 — Historical Limitations Must Remain Visible

Chronicle should preserve material limitations that affect historical interpretation.

Potential examples include:

* Missing Source
* Conflicting Sources
* Incomplete Provenance
* Disputed Evidence
* Unknown author
* Uncertain date
* Archived-only copy
* Later Correction
* Retrospective Entry creation

Trust improves when limitations are visible.

---

# Rule 30 — Historical Context Must Not Become Unsupported Interpretation

Chronicle may preserve Historical Context.

It should not present unsupported interpretation as institutional fact.

Where interpretation is necessary, Chronicle should make the distinction clear.

---

# Rule 31 — Retrospective Preservation Is Permitted

Chronicle may preserve an Occurrence after it happened if later context establishes Preservation Eligibility.

Retrospective Entries must preserve:

* Original Event Date
* Entry Creation Date
* Publication Date
* Relevant Version and Correction dates

Chronicle must not rewrite the historical Occurrence date.

---

# Rule 32 — Timeline Is Downstream

Timeline is a discovery mechanism derived from published Chronicle Entries.

Timeline must not become:

* A separate canonical object
* An alternate record system
* A substitute for Chronicle Entry

Chronicle Entry remains canonical.

---

# Rule 33 — Rules Must Remain Implementable

A Chronicle Rule should be:

* Clear
* Operationally meaningful
* Testable where practical
* Compatible with Validation
* Consistent with Suite architecture
* Stable enough to guide production

Rules should not exist merely as aspirational language.

---

# Rule 34 — Procedures Implement Rules

Rules define normative requirements.

Procedures define the operational steps used to satisfy those requirements.

Conceptually:

```text
Rule = What must be true
Procedure = How Chronicle makes it true
```

Procedures may evolve without changing the underlying Rule if the institutional requirement remains the same.

---

# Rule 35 — Schemas Implement Structure

Schemas translate Entry Model and supporting-record requirements into formal structured representations.

Schemas must not silently redefine Chronicle institutional Rules.

If schema design reveals a conflict, the architecture should be reconciled explicitly.

---

# Rule 36 — Controlled Values Govern Enumerated Meaning

Where consistent terminology is required for:

* Event Type
* Relationship Type
* Verification State
* Validation State
* Publication State
* Preservation State
* Lifecycle State
* Source Type
* Source Role
* Evidence Type
* Evidence Relationship

Chronicle should use approved Controlled Values.

Free-form values should not substitute for governed vocabularies when machine-readable consistency matters.

---

# Rule 37 — Policies and Governance Should Not Be Multiplied Prematurely

Chronicle should not create separate Policies or Governance institutional pages merely to make the documentation hierarchy appear complete.

Additional normative layers should be introduced only if operational experience demonstrates a distinct need that cannot be adequately handled through:

* Suite-level governance
* Chronicle Rules
* Chronicle Procedures
* Controlled Values
* Validation
* Existing institutional documentation

Conceptually:

> Do not multiply governance layers without operational need.

---

# Rule 38 — Changes to Chronicle Rules Must Be Traceable

Material changes to Chronicle Rules should remain historically traceable.

Future rule governance may require:

* Rule version
* Effective date
* Change rationale
* Superseded rule reference
* Migration implications
* Affected procedures or schemas

The formal Rule change-control procedure remains to be defined.

---

# Rule 39 — Rules Must Preserve Institutional Boundaries

No Chronicle Rule should cause Chronicle to absorb responsibilities belonging to another Suite institution.

This includes:

* Certification
* Registration
* Anchoring
* Attestation
* Discovery signaling
* Workflow orchestration
* Atlas intelligence functions

Chronicle preserves history.

It does not become the system it documents.

---

# Rule 40 — Non-Duplication Applies to Architecture Too

Chronicle should avoid creating duplicate institutional concepts.

Examples include avoiding unnecessary parallel pages or systems for:

* Historical Significance when Preservation Eligibility already governs it
* Policies when Rules already govern normative behavior
* Governance when Suite-level governance and Chronicle Rules are sufficient
* Chronology when Timeline already provides downstream discovery
* Chronicle Event when Chronicle Entry is canonical

Architecture should remain as small as possible while still supporting correct operation.

---

# Core Rules Summary

The Chronicle operating model can be summarized as:

```text
Preserve only qualifying Occurrences.
Create one canonical Chronicle Entry per Occurrence.
Keep authority with the originating system.
Reference rather than duplicate.
Separate Source, Evidence, and Provenance.
Use explicit Relationships.
Verify Chronicle's representation.
Validate structural and procedural conformance.
Correct only Chronicle-owned records.
Never silently rewrite substantive history.
Publish only through controlled procedure.
Preserve Version lineage and limitations.
Keep Timeline downstream.
Add governance layers only when real need appears.
```

---

# Rules and the First Production Entry

The first production Chronicle Entry should test whether these Rules are sufficient for real operation.

That Entry should reveal whether Chronicle needs:

* Additional Rules
* Clarified Rules
* More precise Procedures
* New Controlled Values
* Additional Validation
* Distinct Policies
* Separate Governance architecture

Architecture should evolve from operational evidence rather than speculation.

---

# Relationship to Other Chronicle Documentation

Chronicle Rules should remain aligned with:

* Purpose
* Scope
* Definitions
* Entry Model
* Event Type Framework
* Preservation Eligibility
* Entries
* Records
* Sources
* Evidence
* Verification
* Corrections
* Schemas
* Integration
* Historical Preservation
* Trust Model
* Status

Chronicle Rules provide the normative layer connecting the conceptual Foundation to operational Procedures, Validation, and production records.

---

# Future Development

Later work may formalize:

* Rule identifiers
* Rule versioning
* Rule effective dates
* Rule change procedure
* Rule-to-validation mappings
* Rule-to-schema mappings
* Rule-to-procedure mappings
* Rule applicability by Event-Type Profile

These mechanisms should be introduced only where they improve operational clarity or auditability.

---

## Guiding Principle

> Clear rules.  
> Clear authority.  
> Traceable history.

Chronicle Rules exist to protect the record by protecting the boundaries around it.

---

## Status

**Active pre-operational Chronicle Rules specification.**

This document consolidates Chronicle's current normative operating requirements.

Separate Chronicle Policies and Governance pages are intentionally deferred unless production experience demonstrates a distinct need for them.
