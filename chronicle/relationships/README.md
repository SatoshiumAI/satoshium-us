# Chronicle Relationship Model

## Purpose

The Chronicle Relationship Model defines how a canonical Chronicle Entry connects to other Chronicle records, authoritative Suite objects, supporting records, external systems, and related historical Occurrences.

Relationships provide structure for:

* Cross-record traceability
* Historical sequence
* Cross-Suite interoperability
* Supporting-record references
* Supersession
* Correction lineage
* Source relationships
* Registry relationships
* Originating-system context
* Public historical discovery

Relationships must improve historical understanding without transferring authority to Chronicle.

The governing principle is:

> Connect records. Preserve direction. Keep authority visible.

---

# Core Principle

A Relationship describes a connection between two objects.

It does not automatically establish:

* Authority
* Ownership
* Custody
* Causation
* Equivalence
* Control
* Responsibility

Conceptually:

```text
Source Object
    ↓
Relationship Type
    ↓
Target Object
```

The meaning of the Relationship comes from the approved Relationship Type and the actual historical evidence supporting the connection.

---

# Relationship and Canonical Object

The canonical Chronicle object remains the Chronicle Entry.

Relationships do not create a competing canonical layer.

A Chronicle Entry may have many Relationships.

Each Relationship explains how the Entry connects to another object or Entry.

Conceptually:

```text
Chronicle Entry
├── Relationship → Source Record
├── Relationship → Registry Entry
├── Relationship → Chronicle Entry
├── Relationship → Certification Package
├── Relationship → Originating System
└── Relationship → Other approved object
```

---

# Relationship Components

A structured Relationship should conceptually identify:

```text
Source Object
Relationship Type
Target Object
Target Identifier
Target System
Direction when applicable
Context or rationale when needed
```

The final schema may add:

* Relationship identifier
* Creation date
* Verification state
* Provenance
* Supporting Evidence
* Schema version
* Relationship status

These should be added only if operational need requires them.

---

# Source Object

The Source Object is the object from which the Relationship is expressed.

Example:

```text
Source Object:
CHR-2026-0001
```

---

# Target Object

The Target Object is the object to which the Relationship points.

Examples may include:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0002
Source Record
Evidence Record
External authoritative record
```

---

# Relationship Type

Relationship Type is a Controlled Value.

The initial Relationship Type vocabulary includes:

```text
References
Related To
Derived From
Supersedes
Superseded By
Corrects
Corrected By
Precedes
Follows
```

Additional values should be added only when real operational needs justify them.

---

# Directionality

Some Relationship Types are directional.

Direction must be explicit.

Examples:

```text
Precedes ↔ Follows
Supersedes ↔ Superseded By
Corrects ↔ Corrected By
```

If:

```text
CHR-2026-0001 Precedes CHR-2026-0002
```

then the inverse relationship may be represented as:

```text
CHR-2026-0002 Follows CHR-2026-0001
```

Chronicle should not rely on UI placement or implicit ordering to convey direction.

---

# Non-Directional Relationships

Some relationships may be non-directional.

The principal initial example is:

```text
Related To
```

If two objects are simply historically related without a stronger approved semantic relationship, `Related To` may be appropriate.

This value should be used carefully.

Overuse may reduce historical precision.

---

# References

## Purpose

`References` indicates that one Chronicle object explicitly points to another object for identity, authority, context, support, or traceability.

Example:

```text
CHR-2026-0001
    References
SC-CERT-2026-0001
```

This does not imply that Chronicle owns or controls the Certification Package.

---

# Derived From

## Purpose

`Derived From` indicates that the Chronicle representation, supporting record, or structured information was materially constructed from the target Source or record.

Example:

```text
Chronicle Source Record
    Derived From
Archived institutional document
```

`Derived From` should not be used merely because a target is mentioned.

There should be a meaningful derivation relationship.

---

# Related To

## Purpose

`Related To` indicates a meaningful historical association when no more precise approved relationship applies.

Potential uses include:

* Related Entries
* Related authoritative objects
* Related governance records
* Related historical developments

It should not be used as a universal fallback for weak or speculative association.

---

# Precedes

## Purpose

`Precedes` establishes that the Source Occurrence occurred before the Target Occurrence in a historically meaningful sequence.

Example:

```text
CHR-2026-0001
Certification Created
    ↓ Precedes
CHR-2026-0002
Certification Revoked
```

Temporal ordering should be supportable from Event Dates or other authoritative temporal information.

---

# Follows

## Purpose

`Follows` is the inverse of `Precedes`.

Example:

```text
CHR-2026-0002
Follows
CHR-2026-0001
```

Chronicle may store one direction and derive the inverse in interfaces if the schema and Validation rules support that approach.

The implementation decision remains open.

---

# Supersedes

## Purpose

`Supersedes` indicates that a later record or Entry formally or materially replaces an earlier record or representation for a defined institutional purpose.

Supersession should not be used merely because something is newer.

A superseding relationship should be supportable.

---

# Superseded By

## Purpose

`Superseded By` is the inverse of `Supersedes`.

Superseded records should remain historically preserved.

Conceptually:

```text
Superseded ≠ Deleted
```

---

# Corrects

## Purpose

`Corrects` indicates that a later Correction Record, Entry Version, or other Chronicle-owned object formally corrects a prior Chronicle-owned record.

Chronicle should use this relationship only within its own authority boundary.

---

# Corrected By

## Purpose

`Corrected By` is the inverse of `Corrects`.

Example:

```text
CHR-2026-0001 Version 1
    Corrected By
Correction Record
```

---

# Relationship to Authoritative Source Records

Chronicle Entries may relate to authoritative Source Records.

The architecture must distinguish several concepts.

### Source Relationship

Answers:

> Which Source is connected to this Entry?

### Evidence Relationship

Answers:

> How does material bear on the Entry or claim?

### Authority Relationship

Answers:

> Which system or institution owns the authoritative referenced object?

These should not be collapsed.

---

# Authoritative Source Records

A Source Record may document an authoritative source.

For example:

```text
Source Type:
Authoritative Record
```

The Chronicle Entry may:

```text
References
```

that Source Record.

The Source Record may in turn identify the authoritative external object.

Chronicle should not create a relationship that implies Chronicle itself becomes the authority.

---

# Relationship to Registry Entries

A Chronicle Entry may reference an SREG Registry Entry when:

* The registered object is relevant to the historical Occurrence
* The registration action is itself historically significant
* Registry provides authoritative catalog identity needed for traceability
* Cross-Suite relationship is useful to future reviewers

Example:

```text
CHR-2026-0001
    References
SREG-2026-0001
```

Registry retains authority for the SREG Registry Entry.

Chronicle preserves the historical relationship.

---

# Registry Authority Boundary

Conceptually:

```text
Registry:
Owns SREG-2026-0001

Chronicle:
Owns CHR-2026-0001

Relationship:
CHR-2026-0001 References SREG-2026-0001
```

The Relationship does not merge the records or transfer Registry authority.

---

# Relationship to Other Chronicle Entries

Chronicle Entries may relate to other Chronicle Entries when they preserve distinct but connected Occurrences.

Examples:

```text
CHR-2026-0001
Precedes
CHR-2026-0002
```

or:

```text
CHR-2026-0005
Related To
CHR-2026-0011
```

Each Entry retains:

* Its own identifier
* Its own Event Type
* Its own Event Date
* Its own Preservation Eligibility basis
* Its own Historical Context
* Its own Verification
* Its own Version lineage

Relationships connect Entries.

They do not merge them.

---

# Preceding and Following Events

Chronicle may preserve historical sequence using directional relationships.

Sequence should reflect actual Occurrence order.

Chronicle should not infer:

* Causation
* Dependency
* Supersession

merely because one Entry precedes another.

Conceptually:

```text
Precedes ≠ Causes
```

---

# Originating Systems

Chronicle may identify the originating system associated with an authoritative action, object, or record.

Examples may include:

```text
Certifier
Registry
Anchor
Beacon
Attestor
Navigator
Atlas
Chronicle
External Institution
```

Originating System may later become:

* A structured field
* A Controlled Value
* A formal Relationship
* Part of Provenance

The final implementation should avoid duplicating the same semantic concept across multiple structures without need.

---

# Originating System and Authority

Originating System is descriptive.

It does not automatically determine authority.

For example:

A Chronicle Entry may originate from a historical action involving multiple systems.

The authoritative object may belong to one institution while supporting Sources belong to another.

Authority should therefore remain explicit rather than inferred from origin alone.

---

# Superseding Occurrences

A later Occurrence may supersede an earlier Occurrence or institutional state.

Examples might include:

* A governance rule replaced by a new rule
* A public release replaced by a later canonical release
* A Chronicle Entry correction that materially replaces prior representation
* A new institutional artifact superseding an older artifact

Supersession should be used only when the replacement relationship is real and supportable.

---

# Related Occurrences

Two Occurrences may be historically related without a temporal or supersession relationship.

Example:

```text
Certification Created
Related To
Registry Entry Created
```

If these are distinct qualifying Occurrences, each may receive its own Chronicle Entry.

The Relationship explains connection.

It should not imply they are the same Occurrence.

---

# Relationship and Duplicate Handling

Chronicle should not create duplicate Entries merely because multiple systems reference the same Occurrence.

Conceptually:

```text
One Occurrence
    ↓
One Chronicle Entry
    ├── References Certification Package
    ├── References Registry Entry
    ├── References Source Record
    └── Related To other relevant objects
```

Relationships support non-duplication.

---

# Relationship and Event Type

Relationship Type and Event Type are distinct.

### Event Type

Classifies the Occurrence.

### Relationship Type

Classifies the connection between objects.

Example:

```text
Event Type:
Certification Created

Relationship:
References SC-CERT-2026-0001
```

Chronicle should not encode relationship semantics into Event Type labels.

---

# Relationship and Evidence

Evidence relationships may eventually require a distinct Controlled Value vocabulary.

Potential Evidence Relationship concepts include:

```text
Supports
Challenges
Contradicts
Clarifies
Corroborates
Contextualizes
Limits Confidence
```

These describe how Evidence bears on an Entry or claim.

They should not automatically be mixed into the general Relationship Type set unless schema development shows that one unified relationship model is preferable.

---

# Relationship and Provenance

Provenance may use relationships to document movement or derivation.

Examples:

```text
Derived From
Captured From
Archived From
Imported From
```

Not all Provenance semantics should necessarily become general Relationship Types.

The Provenance architecture should decide which concepts belong in:

* Provenance fields
* Controlled Values
* Relationship Types
* Supporting records

This prevents vocabulary inflation.

---

# Authority Boundary

Relationships must not become authority claims.

The following statements are distinct:

```text
CHR-2026-0001 References SC-CERT-2026-0001
```

and:

```text
Chronicle is authoritative for SC-CERT-2026-0001
```

The first may be correct.

The second would violate Suite authority boundaries.

---

# Relationship Does Not Transfer Authority

This rule applies across the Suite.

Examples:

```text
Chronicle → References → Certification Package
Certifier remains authoritative

Chronicle → References → SREG Registry Entry
Registry remains authoritative

Chronicle → References → Trust Statement
Attestor remains authoritative

Chronicle → References → Integrity Reference
Anchor remains authoritative
```

---

# Relationship Does Not Establish Causation

Chronicle must not infer causation from:

* Temporal sequence
* Shared objects
* Shared Sources
* Shared institutions
* Similar Event Types
* Cross-references

If causation later becomes a legitimate supported relationship requiring structured representation, Chronicle should create a distinct Controlled Value only after operational need is demonstrated.

---

# Relationship Does Not Establish Ownership

A Relationship must not imply that Chronicle owns the target record.

Ownership and institutional responsibility remain with the originating authority.

---

# Relationship Does Not Establish Equivalence

Two records referencing the same object are not necessarily equivalent.

Example:

```text
Certification Package
SREG Registry Entry
Chronicle Entry
```

may all concern the same certification but perform different institutional functions.

Relationships should preserve those distinctions.

---

# Relationship Direction Rules

Directional relationships should identify:

* Source object
* Relationship Type
* Target object

Example:

```text
Source:
CHR-2026-0002

Type:
Follows

Target:
CHR-2026-0001
```

Direction should be machine-interpretable.

---

# Inverse Relationships

Some Relationship Types have natural inverses.

Initial inverse pairs:

```text
Precedes ↔ Follows
Supersedes ↔ Superseded By
Corrects ↔ Corrected By
```

The schema may later determine whether:

* Both directions are stored
* One direction is stored and the inverse is derived

Whichever method is selected should be consistent and Validation-aware.

---

# Symmetric Relationships

`Related To` may be treated as symmetric.

If:

```text
A Related To B
```

then:

```text
B Related To A
```

may be inferred.

The schema should explicitly define whether symmetry is derived or stored.

---

# Relationship Provenance

A Relationship may itself require Provenance where the connection is not obvious from authoritative records.

Potential Relationship Provenance may include:

* Source establishing the connection
* Evidence supporting the relationship
* Date relationship was recorded
* Reviewer
* Rationale

This should be required only when operational need warrants the additional complexity.

---

# Relationship Verification

Verification should review whether a material Relationship is:

* Supported
* Semantically correct
* Directionally correct
* Consistent with authoritative records
* Not overstated
* Still valid after Corrections or Version changes

---

# Relationship Validation

Future Validation should confirm:

1. Relationship Type is approved.
2. Source object is valid.
3. Target identifier is syntactically valid where applicable.
4. Target system is recognized.
5. Direction is valid.
6. Relationship Type is permitted for the source and target classes.
7. Required inverse behavior is satisfied.
8. Duplicate relationship handling is correct.
9. Authority is not structurally misrepresented.
10. Event-Type Profile requirements are satisfied.

---

# Relationship and Corrections

A Correction may:

* Add a Relationship
* Remove an incorrect Relationship
* Change Relationship Type
* Change target
* Correct direction

Material Relationship changes may require:

* Correction Record
* New Entry Version
* Verification update
* Publication update

The applicable procedure should depend on materiality.

---

# Relationship and Versioning

Relationships may change over time while Entry identity remains stable.

Example:

```text
CHR-2026-0001
Version 1:
References SC-CERT-2026-0001

Version 2:
References SC-CERT-2026-0001
References SREG-2026-0001
```

The identifier remains unchanged.

Version lineage preserves the relationship history.

---

# Relationship and Publication

Published Entries should expose Relationships needed for historical traceability without requiring publication of every internal operational relationship.

Publication rules may later distinguish:

* Public Relationships
* Internal Relationships
* Administrative Relationships

This should be added only if a real need appears.

---

# Initial Relationship Type Registry

The initial general-purpose Relationship Types are:

```text
References
Related To
Derived From
Supersedes
Superseded By
Corrects
Corrected By
Precedes
Follows
```

These values should remain narrow.

Chronicle should not immediately add:

* Causes
* Depends On
* Owns
* Governs
* Controls
* Confirms
* Validates
* Verifies
* Replaces
* Mirrors
* Equivalent To

unless operational evidence demonstrates a precise need and the semantics can be safely governed.

---

# Relationship Model Summary

The conceptual structure is:

```text
Chronicle Entry
│
├── References → Authoritative Source Record
├── References → SREG Registry Entry
├── References → Other authoritative Suite object
├── Related To → Chronicle Entry
├── Precedes → Chronicle Entry
├── Follows → Chronicle Entry
├── Supersedes → Chronicle Entry / record
├── Superseded By → Chronicle Entry / record
├── Corrects → Chronicle-owned record
└── Corrected By → Chronicle-owned record
```

All Relationships remain subject to:

* Controlled Values
* Authority boundaries
* Verification
* Validation
* Versioning
* Correction rules
* Provenance where required

---

# Guiding Principle

> A relationship explains connection without claiming control.

And institutionally:

> Connect records. Preserve direction. Keep authority visible.

---

## Relationship to Other Chronicle Documentation

The Chronicle Relationship Model should remain aligned with:

* Entry Model
* Event Type Framework
* Preservation Eligibility
* Chronicle Rules
* Identifier Specification
* Controlled Values Registry
* Sources
* Evidence
* Provenance
* Corrections
* Integration
* Schemas
* Validation

Relationships provide the structural bridge connecting Chronicle Entries to the rest of the historical and Suite architecture.

---

## Next Operational Dependencies

The Relationship Model directly informs:

* Provenance
* Lifecycle
* Versioning
* Corrections
* Chronicle Base Schema
* Certification Event-Type Profile
* Validation
* Production Procedure
* First production Chronicle Entry

The first production Chronicle Entry should test cross-system references, Chronicle-to-Chronicle relationships where applicable, directionality, and authority-boundary enforcement.

---

## Status

**Active pre-operational Chronicle Relationship Model specification.**

The initial Relationship Type vocabulary is intentionally narrow and governed through the Chronicle Controlled Values Registry.

Future Relationship Types should be added only when real production cases demonstrate a need that cannot be represented accurately by the existing model.
