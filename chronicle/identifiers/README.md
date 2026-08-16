# Chronicle Identifier Specification

## Purpose

The Chronicle Identifier Specification defines the identity architecture for canonical Chronicle Entries.

The identifier must provide:

* Stable Entry identity
* Human readability
* Namespace separation
* Operational sequencing
* Permanent historical reference
* Compatibility with corrections and Versioning
* Independence from changing classification semantics

The identifier should not attempt to encode the entire meaning of the Chronicle Entry.

The guiding principle is:

> Identity should be permanent. Meaning should remain in the record.

---

# Recommended Identifier Format

The Chronicle Entry identifier format is:

```text
CHR-YYYY-NNNN
```

Example:

```text
CHR-2026-0001
```

The components are:

```text
CHR  = Chronicle Entry namespace
YYYY = Identifier assignment year
NNNN = Annual sequential number
```

This format intentionally encodes only minimal durable semantics.

---

# Why This Structure

Chronicle requires identifiers that can remain valid across:

* Event Type changes
* Historical-context changes
* Corrections
* Entry Version changes
* Schema Version changes
* Relationship changes
* Verification changes
* Validation changes
* Publication-state changes
* Preservation-state changes

A highly semantic identifier would make permanent identity dependent on classifications or states that may later change.

The selected structure avoids that problem.

---

# Identifier Namespace

## `CHR`

The namespace for canonical Chronicle Entries is:

```text
CHR
```

`CHR` identifies the record as a Chronicle Entry.

It distinguishes Chronicle Entries from identifiers issued by other Satoshium Suite systems.

The namespace should remain stable.

---

## Namespace Scope

The `CHR` namespace applies to the canonical Chronicle Entry.

Supporting Chronicle-owned records should not automatically reuse the same namespace.

If Source Records, Evidence Records, Correction Records, Verification Records, or other supporting objects later require dedicated public identifiers, those identifier namespaces should be designed separately.

This prevents the Chronicle Entry namespace from becoming a generic prefix for every internal record.

---

# Year Component

The year component uses a four-digit calendar year:

```text
YYYY
```

Example:

```text
2026
```

The year represents:

> The year in which the Chronicle Entry identifier is assigned.

It does not necessarily represent:

* Event Date
* Source publication date
* Evidence date
* Certification date
* Registry date
* Publication date

---

## Why Assignment Year

Chronicle supports retrospective preservation.

An Occurrence may happen in one year and be admitted into Chronicle later.

Example:

```text
Occurrence Date: 2025-06-03
Chronicle Entry Created: 2026-09-04
Identifier: CHR-2026-0001
```

Using Event Date in the identifier would create ambiguity when:

* Event Date is uncertain
* Event Date changes after correction
* An Occurrence spans multiple dates
* A retrospective Entry is created years later
* Multiple related Occurrences share dates

Assignment year is operationally stable.

---

# Sequence Structure

The sequence component is:

```text
NNNN
```

The initial production form uses four digits.

Examples:

```text
0001
0002
0003
0127
9999
```

Sequence numbers should begin at:

```text
0001
```

for each identifier-assignment year.

---

## Annual Sequence

The sequence is scoped to the assignment year.

Conceptually:

```text
CHR-2026-0001
CHR-2026-0002
...
CHR-2027-0001
```

The sequence resets when a new assignment year begins.

The year and sequence together preserve uniqueness within the `CHR` namespace.

---

## Sequence Capacity

A four-digit sequence supports:

```text
0001 through 9999
```

Chronicle should not prematurely increase identifier length without operational need.

If production volume eventually exceeds this capacity, Chronicle may revise the sequence specification through formal identifier governance while preserving already assigned identifiers permanently.

---

# Sequential Assignment

Identifiers should ordinarily be assigned monotonically.

Example:

```text
CHR-2026-0001
CHR-2026-0002
CHR-2026-0003
```

Chronicle should not deliberately assign identifiers out of sequence without an operational reason.

---

## Gaps

Sequence gaps are permitted.

Potential reasons include:

* Reserved identifier
* Entry creation aborted after identifier assignment
* Void record
* Operational failure
* Duplicate discovered before publication
* Other documented reason

Chronicle must not reuse a skipped or previously assigned number merely to make the sequence appear continuous.

Conceptually:

> Sequence continuity is desirable. Identifier permanence is mandatory.

---

# Permanence

Once assigned, a Chronicle Entry identifier is permanent.

The identifier belongs to the Chronicle Entry's historical identity.

It must not change merely because record content changes.

---

## Changes That Do Not Change the Identifier

The Chronicle Entry identifier should remain stable when:

* Historical Context is corrected
* Event Type is corrected
* Source Records are added or removed
* Evidence is added
* Provenance is improved
* Relationships are added or corrected
* Verification State changes
* Validation State changes
* Publication State changes
* Lifecycle State changes
* Preservation State changes
* Entry Version changes
* Schema Version changes

These are changes to the record.

They are not changes to the record's identity.

---

# Reuse Prohibition

A Chronicle Entry identifier must never be assigned to a second canonical Entry.

This rule applies even when the original Entry becomes:

* Withdrawn
* Superseded
* Corrected
* Unpublished
* Invalidated
* Deprecated
* Voided
* Merged
* Determined to be duplicate
* Created in error

The identifier remains historically reserved.

Conceptually:

```text
Assigned once
    ↓
Reserved forever
```

---

# Deleted Records

Chronicle should strongly prefer preservation, correction, or withdrawal over destructive deletion.

If exceptional circumstances require record removal from publication or active use, its identifier should remain reserved.

A removed identifier must not be recycled.

---

# Identifier and Entry Version

Entry Version and Chronicle Entry identifier serve different functions.

### Identifier

Answers:

> Which Chronicle Entry is this?

### Entry Version

Answers:

> Which preserved state of that Entry is this?

Conceptually:

```text
Identifier:
CHR-2026-0001

Entry Versions:
1
2
3
```

The same identifier persists across Versions.

---

# Correction Behavior

A Correction does not ordinarily create a new Chronicle Entry identifier.

Conceptually:

```text
CHR-2026-0001
Version 1
    ↓
Correction Record
    ↓
CHR-2026-0001
Version 2
```

The canonical Entry identity remains stable.

---

## When a New Identifier Is Required

A new identifier is required when Chronicle determines that the record represents a genuinely distinct qualifying Occurrence.

Example:

```text
CHR-2026-0001
Event Type: Certification Created

CHR-2026-0002
Event Type: Certification Revoked
```

Both may reference the same Certification Package.

They represent different Occurrences and therefore different Chronicle Entries.

---

# Duplicate Entry Behavior

If Chronicle later discovers that two Entry identifiers were assigned to the same underlying Occurrence, identifiers must not be collapsed through reuse.

Example:

```text
CHR-2026-0010
CHR-2026-0011
```

If both are found to represent one Occurrence, Chronicle should preserve the historical identity of both records and resolve the duplicate through approved procedures.

Potential mechanisms may include:

* Duplicate status
* Supersession
* Relationship
* Correction
* Publication withdrawal
* Canonical-reference designation

The final duplicate-resolution procedure should be defined later.

The identifier of the duplicate record remains reserved.

---

# Identifier and Event Type

Event Type must not be encoded into the Chronicle Entry identifier.

The identifier should therefore not use forms such as:

```text
CHR-CERT-2026-0001
CHR-REG-2026-0001
CHR-GOV-2026-0001
```

even though such formats may appear descriptive.

---

## Why Event Type Must Remain Separate

Event Type is classification.

Classification may change.

Example:

```text
Initial Event Type:
Certification Created

Later corrected classification:
Certification Issued
```

If Event Type were embedded in the identifier, Chronicle would face two undesirable choices:

1. Change the supposedly permanent identifier.
2. Retain an identifier containing incorrect semantic information.

Keeping Event Type in a structured field eliminates this conflict.

Conceptually:

```text
Identifier = Stable identity
Event Type = Governed classification
```

---

# Identifier and Originating System

The originating Suite system should not be encoded into the Chronicle identifier.

Avoid formats such as:

```text
CHR-CERTIFIER-2026-0001
CHR-REGISTRY-2026-0001
```

Originating System belongs in structured Entry metadata.

Reasons include:

* Cross-system Occurrences may involve more than one institution.
* Originating-system understanding may change.
* Chronicle may later classify the event differently.
* Long identifiers become harder to maintain.
* The identifier should not become a compressed record.

---

# Identifier and Status

Do not encode lifecycle, publication, verification, preservation, or validation states into identifiers.

Avoid patterns such as:

```text
CHR-PUBLISHED-2026-0001
CHR-VERIFIED-2026-0001
```

States change.

Identity should not.

---

# Identifier and Historical Significance

Historical Significance should not be encoded into identifiers.

Avoid:

```text
CHR-MILESTONE-2026-0001
CHR-MAJOR-2026-0001
```

Significance belongs in Preservation Eligibility rationale and Historical Context.

---

# Identifier and Jurisdiction

Jurisdiction should not be encoded into Chronicle Entry identifiers.

Avoid formats such as:

```text
CHR-US-2026-0001
CHR-SV-2026-0001
```

Jurisdiction is contextual metadata, not stable record identity.

---

# Identifier and Authoritative References

Chronicle Entry identifiers remain independent from authoritative external identifiers.

Example:

```text
Chronicle Entry:
CHR-2026-0001

Authoritative Certifier object:
SC-CERT-2026-0001

Registry reference:
SREG-2026-0001
```

The relationships among these objects belong in structured fields.

The identifiers should not be nested into one another.

---

# Cross-System Reference Principle

Conceptually:

```text
CHR-2026-0001
    ↓ references
SC-CERT-2026-0001
    ↓ may relate to
SREG-2026-0001
```

Each identifier retains independent institutional meaning.

---

# Identifier Assignment Timing

The formal Production Procedure should later determine the exact point at which an identifier is assigned.

Potential timing options include:

* After Preservation Eligibility approval
* At Entry draft creation
* After initial Validation
* Immediately before publication

The preferred architectural constraint is:

> Do not assign canonical Chronicle identifiers before Preservation Eligibility has been established.

This prevents unnecessary identifier issuance for Occurrences that do not belong in Chronicle.

The precise procedural moment remains to be settled.

---

# Identifier Reservation

If Chronicle requires pre-publication reservation, the reserved identifier should be treated as consumed once assigned.

A reservation that is later abandoned must not be reused.

This preserves auditability.

---

# Identifier Uniqueness

Every Chronicle Entry identifier must be unique within the Chronicle namespace.

Future Validation should verify uniqueness before publication.

---

# Case and Formatting

The canonical human-readable format should use uppercase namespace characters:

```text
CHR-2026-0001
```

Production records should not treat case variants as distinct identifiers.

For example:

```text
chr-2026-0001
CHR-2026-0001
```

must not identify separate Entries.

Canonical serialization should use uppercase `CHR`.

---

# Leading Zeros

The sequence component should preserve leading zeros.

Canonical:

```text
CHR-2026-0001
```

Not canonical:

```text
CHR-2026-1
```

Leading zeros preserve consistent lexical ordering and human readability.

---

# Delimiter

The canonical delimiter is the hyphen:

```text
-
```

Canonical:

```text
CHR-2026-0001
```

Avoid mixed delimiter forms such as:

```text
CHR/2026/0001
CHR_2026_0001
CHR.2026.0001
```

unless used solely as a noncanonical display or transport transformation.

---

# Canonical Pattern

The initial logical pattern is:

```text
^CHR-[0-9]{4}-[0-9]{4}$
```

This expresses format only.

It does not validate:

* Whether the year is permitted
* Whether the identifier was actually assigned
* Whether the sequence is unique
* Whether the identifier has been reused
* Whether the associated record exists

Those checks belong to Validation and identifier management.

---

# Identifier Validation

Future Chronicle Validation should confirm:

1. Namespace is `CHR`.
2. Year contains exactly four digits.
3. Sequence contains exactly four digits.
4. Sequence is not `0000`.
5. Identifier is unique.
6. Identifier has not previously been assigned to another Entry.
7. Canonical formatting is used.
8. Identifier matches the Entry's stored identity.
9. Version changes have not altered the canonical identifier.
10. Event Type or other mutable semantics are not embedded.

---

# Identifier Registry or Allocation Record

Chronicle may later require an internal allocation record or identifier ledger to prevent duplication and reuse.

That implementation should not be confused with Satoshium Registry.

The need for a dedicated internal allocation mechanism should be determined during Production Procedure development.

---

# Permanence Across Schema Evolution

Chronicle Entry identifiers must survive schema changes.

Example:

```text
CHR-2026-0001
Schema Version 1.0
```

may later be represented under a migrated schema while retaining:

```text
CHR-2026-0001
```

Schema evolution must not force identity migration.

---

# Permanence Across Event-Type Profile Evolution

If the Certification Event-Type Profile evolves, existing Chronicle Entry identifiers remain unchanged.

Profile Version should be recorded separately where required.

---

# Retrospective Preservation

Retrospective Entries use the year of identifier assignment.

Example:

```text
Historical Occurrence:
2024-11-10

Chronicle preservation decision:
2026-09-15

Identifier assigned:
CHR-2026-0042
```

This preserves the difference between:

* When history happened
* When Chronicle preserved it

---

# Semantic Restraint

Chronicle identifiers should not encode:

* Event Type
* Event subtype
* Originating system
* Source Type
* Jurisdiction
* Historical Significance
* Verification State
* Validation State
* Publication State
* Lifecycle State
* Preservation State
* Relationship Type
* Version
* Correction count
* Authority level

All of those concepts belong in structured record fields.

---

# Why Semantic Restraint Matters

Excessive semantics create fragile identifiers.

Consider:

```text
CHR-CERT-US-VERIFIED-PUBLISHED-2026-0001
```

Nearly every semantic component may later change.

A durable identifier should avoid carrying mutable meaning.

The proposed format:

```text
CHR-2026-0001
```

survives those changes.

---

# Identifier Governance

Changes to the Chronicle Identifier Specification should be rare.

Material changes should consider:

* Backward compatibility
* Existing identifiers
* Validation
* Publication systems
* Cross-Suite references
* Discovery
* Public links
* Archival records
* Machine-readable records

Existing identifiers should remain valid permanently.

---

# Future Expansion

Operational experience may eventually require:

* More than four sequence digits
* Machine-only UUID mapping
* Internal allocation ledger
* Reservation procedure
* Distributed identifier assignment
* Additional supporting-record namespaces

These should not be added prematurely.

The current identifier should remain as simple as possible while satisfying production needs.

---

# Specification Summary

The Chronicle Entry identifier architecture is:

```text
Format:
CHR-YYYY-NNNN

Namespace:
CHR

Year:
Identifier assignment year

Sequence:
Zero-padded annual sequence beginning at 0001

Permanence:
Permanent once assigned

Reuse:
Prohibited

Correction behavior:
Same identifier, new Entry Version when appropriate

Version behavior:
Version stored separately

Event Type:
Stored separately; never encoded

Other semantics:
Stored in structured fields, not identifier
```

---

# Guiding Principle

> A durable identifier names the record without trying to tell its entire story.

And institutionally:

> Identity should be permanent. Meaning should remain in the record.

---

## Relationship to Other Chronicle Documentation

The Identifier Specification should remain aligned with:

* Entry Model
* Event Type Framework
* Preservation Eligibility
* Chronicle Rules
* Definitions
* Records
* Corrections
* Schemas
* Validation
* Production Procedure
* Integration

The Identifier Specification establishes stable Entry identity before Controlled Values, Relationships, Provenance, and final schema implementation are completed.

---

## Next Operational Dependencies

Identifier architecture directly informs:

* Controlled Values
* Relationship references
* Provenance
* Chronicle Base Schema
* Event-Type Profiles
* Validation
* Publication
* Entry index
* First production Chronicle Entry

The first production Chronicle Entry should test identifier assignment, uniqueness, permanence, and cross-system referencing in practice.

---

## Status

**Active pre-operational Chronicle Identifier Specification.**

The canonical initial Chronicle Entry identifier format is:

```text
CHR-YYYY-NNNN
```

with `YYYY` representing identifier assignment year and `NNNN` representing a zero-padded annual sequence.

Event Type and other mutable semantics are intentionally excluded from the identifier.
