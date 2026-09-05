# Satoshium Beacon — Validation

## Overview

The **Beacon Validation** architecture defines what must be true before a Beacon-owned **Discovery Signal** can be accepted as a valid production object.

Validation applies the institutional rules established through:

```text
Discovery Signal Entry Model
→ Discovery Signal Types
→ Discovery Signal Lifecycle
→ Beacon Identifier Standard
→ Beacon Schemas
→ Validation
```

Beacon's canonical production object is:

```text
Discovery Signal
```

with canonical identifier:

```text
BEAC-YYYY-NNNN
```

Validation determines whether a Discovery Signal conforms to Beacon's structural and institutional requirements.

It does not independently establish:

```text
truth
certification
registration
historical authority
integrity verification
trust
source authority
publication approval
```

---

# Purpose

Validation answers:

> **Does this candidate Discovery Signal satisfy the minimum structural and institutional requirements required to stand as a valid Beacon object?**

Validation is therefore a **production-conformance gate**.

It is not the discovery itself.

It is not the creation event.

It is not publication.

It is not certification or attestation.

---

# Architectural Position

The Discovery Signal Lifecycle established:

```text
Identified
→ pre-object condition

Created
→ canonical object creation event

Draft
→ first canonical lifecycle state
```

Validation occurs after canonical creation.

Conceptually:

```text
Candidate Discovery Identified
        ↓
Discovery Signal Created
        ↓
BEAC Identifier Assigned
        ↓
Draft
        ↓
Review / Validation
        ↓
Active
```

Validation is therefore one of the institutional gates required before a Draft can become Active.

Passing Validation does not itself perform the lifecycle transition.

It establishes eligibility for institutional progression.

---

# Validation Principle

The relevant architectural layers remain distinct:

```text
Schema
→ defines structure

Validation
→ tests conformance

Methodology
→ governs process

Publication
→ governs public release
```

A structurally valid Discovery Signal is not necessarily a published Discovery Signal.

A published Discovery Signal does not inherit the authority of its source.

---

# Core Validation Requirements

A valid Beacon Discovery Signal must satisfy the following production concerns.

---

## 1. Canonical Identity

A Discovery Signal must have a valid canonical identity.

Expected identity requirements include:

```text
Beacon identifier
Object Type
Institution
human-readable title or identifying label
```

Canonical values:

```text
Object Type → Discovery Signal
Institution → Beacon
```

Identity must be:

```text
stable
unique
reviewable
institutionally attributable
```

---

# 2. Identifier Conformance

The identifier must conform to the Beacon Identifier Standard.

Canonical pattern:

```text
BEAC-YYYY-NNNN
```

Example:

```text
BEAC-2026-0001
```

Validation should confirm:

```text
BEAC prefix
four-digit creation year
four-digit zero-padded sequence
identifier uniqueness
identifier non-reuse
identifier assigned at canonical creation
```

The identifier must not encode:

```text
Signal Type
Lifecycle State
Publication State
Version
```

Conceptual pattern:

```regex
^BEAC-[0-9]{4}-[0-9]{4}$
```

Formal machine-readable enforcement remains an implementation concern.

---

# 3. Subject

A valid Discovery Signal must identify what the discovery concerns.

Expected Subject requirements include:

```text
subject name or equivalent identifier
subject type when applicable
sufficient distinguishing context
```

Additional context may include:

```text
jurisdiction
domain
entity
record
event
artifact
system
relationship
```

A signal whose subject cannot be meaningfully identified cannot be meaningfully reviewed.

---

# 4. Permitted Signal Type

The primary Signal Type must come from the governed Phase II architectural vocabulary:

```text
Information
Jurisdiction
Certification
Registry
Historical
Integrity
Trust
Relationship
```

Ad hoc Signal Types do not satisfy production validation unless Beacon formally governs an extension to the vocabulary.

Signal Type classifies:

```text
the discovery
```

not:

```text
the authority of the source object
```

---

# 5. Source Reference

A valid Discovery Signal must preserve an attributable source.

Expected source information includes:

```text
source name
source kind or institution
source identifier when available
source object type when relevant
source location or reviewable reference when available
```

If a source already possesses a canonical identifier, Beacon should preserve it.

Examples:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
```

Beacon must not manufacture a new Beacon identity for a source merely because Beacon references it.

---

# 6. Provenance

A valid Discovery Signal must have a reviewable provenance basis.

Provenance should explain how the discovery became known to Beacon.

Expected concerns include:

```text
observed source
observation method
observation context
supporting reference
discovery actor when appropriate
discovery process when appropriate
```

Source and Provenance remain distinct.

```text
Source
→ Where did the information originate?

Provenance
→ How did Beacon encounter and preserve the discovery?
```

The dedicated:

```text
/beacon/provenance/
```

architecture will refine these requirements further.

---

# 7. Canonical References

Canonical References are conditional.

Not every Discovery Signal must reference another Suite canonical object.

When such a reference exists, Validation must confirm that it preserves:

```text
correct source institution
correct canonical identifier
correct object type when known
appropriate relationship
```

Examples may include:

```text
Atlas Authoritative Intelligence
Certifier Certification Package
Registry SREG
Chronicle Entry
Anchor Integrity Reference
Attestor Trust Statement
Navigator workflow reference
```

A Beacon reference does not replace the referenced object's identity.

---

# 8. Discovery Metadata

A valid Discovery Signal must contain enough Discovery Metadata to make the discovery understandable and reviewable.

Relevant metadata may include:

```text
discovery context
topic
domain
jurisdiction
classification
observed source status
workflow context
search context
keywords
tags
relationship context
```

Not every metadata field is required for every signal.

Validation should determine whether the metadata required by the represented discovery is sufficiently complete.

---

# 9. Timestamps

A valid production object must preserve canonical creation time.

At minimum:

```text
created_at
```

is required.

The creation year must correspond to the year encoded in:

```text
BEAC-YYYY-NNNN
```

Other timestamps may include:

```text
observed_at
updated_at
published_at
last_observed_at
```

`observed_at` should be present when the observation time is meaningfully distinct from canonical creation.

Exact timestamp serialization remains a machine-readable implementation decision.

---

# 10. Status

Status contains two separate dimensions.

## Lifecycle State

The governed architectural values are:

```text
Draft
Active
Superseded
Resolved
Withdrawn
```

## Publication State

The governed architectural values are:

```text
Unpublished
Published
```

These dimensions must remain separately interpretable.

Correct:

```text
lifecycle_state: Active
publication_state: Published
```

Validation should reject or flag representations that collapse lifecycle and publication into an ambiguous single status.

---

# 11. Version

A production Discovery Signal must preserve explicit version information.

At minimum, the initial object should identify its version.

Version must remain separate from the canonical identifier.

Correct:

```text
identifier: BEAC-2026-0001
version: 1
```

Not:

```text
BEAC-2026-0001-v1
```

Later Versioning architecture will determine:

```text
version progression
previous-version references
supersession semantics
version history
```

Validation should preserve the principle that institutional history must not be silently overwritten.

---

# 12. Relationships

Relationships are conditional.

When a Discovery Signal represents relationships, Validation should confirm:

```text
identifiable endpoints
understandable relationship meaning
reviewable supporting basis
source or provenance support
```

Unsupported inference should not be represented as an established relationship.

The dedicated:

```text
/beacon/relationships/
```

architecture will govern the final relationship model.

---

# Schema Conformity

A valid production Discovery Signal must conform to the canonical Beacon schema architecture.

Canonical schema:

```text
/beacon/schemas/discovery-signal-schema.md
```

Schema conformity includes:

```text
required structural components
permitted values
expected data shapes
valid relationships between fields
```

The current human-readable schema defines architectural meaning.

Future machine-readable implementation will enforce exact technical constraints.

---

# Required vs. Conditional Requirements

Validation distinguishes between:

```text
Required
→ every production Discovery Signal must satisfy

Conditional
→ required when the represented condition exists
```

Examples:

```text
Canonical Identity → Required
Subject → Required
Signal Type → Required
Source → Required
Provenance → Required
Discovery Metadata → Required
Timestamps → Required
Status → Required
Version → Required
Schema Conformity → Required

Canonical References → Conditional
Relationships → Conditional
```

This prevents optional contextual structures from becoming artificial requirements for every signal.

---

# Minimum Production Gate

A Draft should not become Active unless required production conditions are satisfied.

Conceptually:

```text
Identifier valid
+
Subject identifiable
+
Signal Type permitted
+
Source attributable
+
Provenance reviewable
+
Discovery Metadata sufficient
+
Timestamps valid
+
Lifecycle State valid
+
Publication State valid
+
Version present
+
Schema conformant
+
Conditional references valid when present
+
Conditional relationships valid when present
=
Eligible for Active consideration
```

Eligibility does not itself change lifecycle state.

---

# Validation Severity

Validation findings should eventually distinguish the seriousness of identified issues.

Initial architectural categories are:

```text
Error
→ prevents production conformance

Warning
→ requires review but may not invalidate the object

Informational
→ observation without direct conformance effect
```

These concepts are architecturally useful.

Exact machine-readable severity values remain unfrozen.

---

# Validation Outcomes

Initial architectural outcomes are:

```text
Valid
Invalid
Review Required
```

## Valid

Required Beacon production requirements are satisfied.

## Invalid

One or more required production requirements failed.

## Review Required

The object may be structurally acceptable, but an unresolved warning or institutional issue requires human or governed review.

Whether:

```text
Review Required
```

becomes a formal machine-readable production outcome remains to be proven through implementation.

---

# What Validation Does Not Prove

Passing Beacon Validation does not establish:

```text
truth of underlying information
correctness of an external source
certification
registration
historical significance
integrity verification
trustworthiness
publication approval
```

Validation means:

```text
This Beacon Discovery Signal conforms to Beacon's production requirements.
```

It does not mean:

```text
Everything referenced by this signal is true.
```

---

# Authority Separation

Beacon Validation evaluates Beacon's object.

Other Suite institutions retain their own authority.

```text
Atlas
→ Authoritative Intelligence

Certifier
→ Certification Package

Registry
→ SREG

Chronicle
→ Chronicle Entry

Anchor
→ Integrity Reference

Beacon
→ Discovery Signal / Metadata

Attestor
→ Trust Statement

Navigator
→ Workflow Definition / Orchestration
```

Beacon Validation does not assume the responsibilities of those institutions.

---

# Source-State Validation

A Discovery Signal may preserve a status observed from a source.

When it does, Validation must ensure that the status remains attributed to the source.

Correct concept:

```text
Observed Source Status
→ Active
Source Institution
→ Registry
```

Incorrect concept:

```text
Beacon independently declares the Registry object Active
```

unless Beacon is merely reproducing an attributable Registry-owned status.

Beacon does not own another institution's lifecycle.

---

# Validation Record

A validation process should eventually preserve enough information to reconstruct what was evaluated.

Potential validation information includes:

```text
Discovery Signal identifier
schema or schema version evaluated
validation timestamp
rules evaluated
errors
warnings
informational findings
validation outcome
```

However, Phase II does **not** establish a separate canonical Validation Record object.

That decision should be driven by demonstrated production need.

---

# No New Canonical Object by Default

Validation output should not automatically create another Beacon object class.

The governing posture is:

```text
Production need first
→ institutional necessity demonstrated
→ separate object considered
→ identifier considered only if justified
```

This prevents schema and process artifacts from multiplying into unnecessary canonical records.

---

# Conceptual Validation Sequence

A future validation implementation should generally perform the following sequence:

```text
1. Parse Discovery Signal

2. Confirm canonical identity

3. Confirm schema structure

4. Confirm required fields

5. Confirm permitted Signal Type

6. Confirm source attribution

7. Confirm provenance basis

8. Confirm timestamp requirements

9. Confirm Lifecycle State

10. Confirm Publication State

11. Confirm Version structure

12. Confirm canonical references when present

13. Confirm relationships when present

14. Produce validation findings

15. Produce validation outcome
```

The exact implementation may evolve without changing the institutional meaning of Validation.

---

# Relationship to Lifecycle

Validation operates within the Discovery Signal lifecycle.

Conceptually:

```text
Created
↓
Draft
↓
Review / Validation
↓
Eligible for Active
```

Validation failure does not erase the Draft object.

The Draft may potentially be:

```text
corrected
re-reviewed
revalidated
withdrawn
```

according to later Methodology and production rules.

---

# Relationship to Publication

Validation and Publication are separate gates.

A Discovery Signal may be:

```text
valid
```

while still:

```text
Unpublished
```

Publication architecture will determine what additional conditions must be satisfied before public release.

Therefore:

```text
Valid
≠
Automatically Published
```

---

# Relationship to Provenance

Provenance is a core Validation concern.

The next Phase II architecture:

```text
/beacon/provenance/
```

will define Discovery Provenance more precisely.

Validation will then consume those provenance rules as conformance requirements.

---

# Relationship to Methodology

Validation defines what must conform.

Methodology will define how institutional review and validation are actually performed.

```text
Validation
→ what must be true

Methodology
→ how Beacon determines and documents that it is true
```

---

# Machine Validation

Automated machine validation remains pending.

Future implementation may validate:

```text
identifier syntax
required properties
data types
controlled values
timestamp format
reference structures
relationship structures
status values
schema version
```

Institutional review may still be required for concerns that cannot be resolved structurally.

Examples include:

```text
whether provenance is sufficient
whether the Signal Type accurately represents the discovery
whether a relationship is adequately supported
whether metadata is materially complete
```

Therefore future Beacon Validation may combine:

```text
machine validation
+
institutional review
```

The exact boundary remains unfrozen.

---

# What Is Now Established

The following architectural decisions are established:

```text
Validation is a production-conformance gate.

Validation occurs after canonical object creation.

A Draft must satisfy required validation conditions before Active standing.

Canonical identity must conform to BEAC-YYYY-NNNN.

Subject is required.

Signal Type must come from the governed vocabulary.

An attributable Source Reference is required.

Reviewable Provenance is required.

Sufficient Discovery Metadata is required.

Canonical creation time is required.

Lifecycle State and Publication State are separate.

Version information is required and separate from identity.

Schema conformity is required.

Canonical References are validated when present.

Relationships are validated when present.

Passing Validation does not establish truth, trust, certification, or publication approval.

Validation does not transfer source authority.
```

---

# What Remains Unfrozen

The following implementation details remain pending:

```text
exact machine-readable required-field list
exact JSON property names
JSON Schema dialect
timestamp serialization rules
formal validation error codes
formal warning codes
severity enum representation
validation report format
schema version representation
who or what authorizes final validation acceptance
whether validation results are persisted
whether Review Required becomes a formal outcome
automated vs. manual validation boundaries
```

These should be refined through production implementation and Beacon Discovery Methodology.

---

# Current Status

As of September 5, 2026:

```text
Institution → Beacon
Suite Role → Discovery & Signals
Canonical Responsibility → Discovery Signal / Metadata
Status → Continuing Development
Phase → Phase II — Production Architecture

Discovery Signal Entry Model → Defined
Discovery Signal Types → Defined
Discovery Signal Lifecycle → Defined
Beacon Identifier Standard → Defined
Beacon Schemas → Defined
Beacon Validation → Defined

Machine Validation → Pending
Production Validation Run → Pending
First Production Discovery Signal → Not yet created
Operational → No
```

---

# Phase II Progress

```text
1. Discovery Signal Entry Model
   → COMPLETE

2. Discovery Signal Types
   → COMPLETE

3. Discovery Signal Lifecycle
   → COMPLETE

4. Beacon Identifier Standard
   → COMPLETE

5. Beacon Schemas
   → COMPLETE

6. Validation
   → COMPLETE

7. Discovery Provenance
   → NEXT

8. Authority & Reference Model

9. Relationship Model

10. Versioning & Supersession

11. Publication Model

12. Discovery Signals Register

13. Individual Discovery Signal

14. Beacon Discovery Methodology

15. Production Model / First Operation
```

---

# Governing Principles

Beacon Validation follows these principles:

```text
Validate the Beacon object.

Preserve source identity.

Require attribution.

Require reviewable provenance.

Separate lifecycle from publication.

Separate version from identity.

Reject unsupported classifications.

Reject unsupported relationships.

Do not confuse conformance with truth.

Do not create new canonical objects without institutional need.
```

The Validation principle is:

> **A valid object is not one that merely exists, but one that can withstand review.**

The Suite-wide authority principle remains:

> **Reference does not transfer authority.**

---

# Next Phase II Step

The next production-architecture page is:

```text
/beacon/provenance/
```

Its purpose is to define the Discovery Provenance model used to preserve how Beacon encountered, observed, attributed, and documented the basis of a Discovery Signal.

---

## Last Updated

September 5, 2026
