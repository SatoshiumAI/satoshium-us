# Versioning

## Overview

**Versioning** defines when a change remains part of the same Satoshium Anchor Integrity Reference and when a change is material enough to require a new Integrity Reference.

The central rule is:

```text
Same integrity subject
+ governed Anchor change
→ new Anchor Version

New integrity subject
→ new Integrity Reference
→ new Anchor Identifier
```

The governing principle is:

> Preserve identity when the subject remains. Create new identity when the subject changes.

---

## Why Versioning Matters

Anchor must preserve continuity without allowing materially different integrity subjects to hide behind one identifier.

Versioning therefore answers:

> Is this still the same Integrity Reference?

rather than merely:

> Did something change?

---

# Integrity Subject

The **integrity subject** is the combination of:

```text
Source Artifact identity
+
Canonical Representation
+
Representation Boundary
```

that the Integrity Reference exists to preserve.

Conceptually:

```text
Source Artifact
        ↓
Canonical Representation
        +
Representation Boundary
        ↓
Integrity Subject
```

The Integrity Method supports preservation of that subject.

The method does not define the subject by itself.

---

# Versioning Decision Rule

The primary decision rule is:

```text
If the integrity subject remains the same
→ use a new Anchor Version where the Anchor record changes.

If the integrity subject changes
→ create a new Integrity Reference.
```

This rule should govern Corrections, Maintenance changes, schema migration, new commitment evidence, and Source changes.

---

# Version Dimensions

Anchor must formally distinguish:

```text
Source Artifact Version
Anchor Version
Schema Version
Algorithm Version
Commitment-Method Version
Canonicalization Version
```

Therefore:

```text
Source Artifact Version
≠
Anchor Version
≠
Schema Version
≠
Algorithm Version
≠
Commitment-Method Version
≠
Canonicalization Version
```

These Versions may change independently.

---

# Source Artifact Version

A **Source Artifact Version** is assigned or governed by the Source Institution.

Examples may include:

- Certification Package Version;
- Registry Entry Version;
- Chronicle Entry Version;
- Trust Statement Version;
- Workflow Definition Version;
- external document Version.

Anchor must preserve the Source Version where it materially affects the integrity subject.

Anchor does not govern Source Version numbering.

---

# Anchor Version

An **Anchor Version** is the sequential production Version of the Anchor-owned Integrity Reference while its identity remains the same.

The initial production model is:

```text
anchor_version = 1
anchor_version = 2
anchor_version = 3
...
```

This simple integer model is now adopted as the initial Anchor Version architecture.

---

# Initial Anchor Version Model

The first production Integrity Reference begins at:

```text
anchor_version = 1
```

Each governed production change to the same Integrity Reference increments the Version:

```text
1 → 2 → 3 → 4
```

Semantic Versioning is not adopted for Integrity References.

If future production proves that major/minor/patch semantics add durable value, that may be reconsidered.

---

# Why Sequential Integers

Sequential integers provide:

- clear ordering;
- simple machine validation;
- human readability;
- low ambiguity;
- no premature semantic assumptions.

The Version number answers:

> Which governed production state of this Integrity Reference is this?

It does not attempt to explain the magnitude of the change.

---

# Schema Version

A **Schema Version** identifies which machine-readable schema governs the structure of an Integrity Reference representation.

Example:

```text
Schema Version 1.0-draft
```

Schema Version changes do not automatically create a new Integrity Reference.

A schema migration may produce a new Anchor Version if the canonical Anchor record representation changes.

---

# Algorithm Version

An **Algorithm Version** identifies the applicable Version of an integrity algorithm or implementation when Version affects reproducibility.

Examples may include:

- signature algorithm Version;
- implementation profile;
- hashing library profile;
- cryptographic standard revision.

Algorithm Version is method metadata.

It is not Anchor identity.

---

# Commitment-Method Version

A **Commitment-Method Version** identifies the Version of the process used to create external or composite commitment evidence.

Potential examples include:

- timestamp profile;
- Merkle batching method;
- transparency-log protocol;
- Bitcoin commitment procedure.

A commitment-method Version change does not automatically create a new Integrity Reference if the integrity subject remains the same.

---

# Canonicalization Version

A **Canonicalization Version** identifies the Version of rules used to construct the Canonical Representation.

This may become important for:

- JSON canonicalization;
- deterministic serialization;
- text normalization;
- package manifest generation;
- file-ordering rules.

A canonicalization Version change requires analysis of whether the resulting integrity subject remains equivalent.

---

# When to Create a New Anchor Version

A new Anchor Version is appropriate when:

```text
the Anchor-owned record changes
```

but:

```text
the integrity subject remains the same
```

Likely examples include:

- Anchor Correction;
- added Verification history;
- corrected publication metadata;
- Maintenance metadata;
- repaired current location;
- added external commitment evidence;
- added signature or timestamp for the same subject;
- schema migration preserving equivalent meaning;
- provenance clarification that does not alter the governed representation.

---

# When to Create a New Integrity Reference

A new Integrity Reference is appropriate when the integrity subject changes.

Likely examples include:

```text
different Source Artifact
different Canonical Representation
different Representation Boundary
materially changed canonical Source content
different artifact package
materially different governed serialization subject
```

A new Integrity Reference receives:

```text
new Anchor Identifier
anchor_version = 1
```

unless future production architecture establishes a different initial Version rule.

---

# Source Version Change

A Source Version change does not automatically mean:

```text
new Anchor Version
```

or:

```text
new Integrity Reference
```

The decision depends on whether the integrity subject changed.

Conceptually:

```text
Source Version changes
        ↓
compare governed representation
        ↓
same integrity subject?
```

If yes:

```text
possibly no action
or Reverification
or new Anchor Version
```

If no:

```text
new Integrity Reference
```

---

# Same Bytes, New Source Version

A Source Institution may change metadata or Version number while the Canonical Representation remains byte-for-byte identical.

In that case, Anchor may not need a new Integrity Reference.

The Source Version change should be preserved as Source metadata if materially relevant.

---

# Changed Canonical Content

If Source Version 2 materially changes the Canonical Representation:

```text
Source Version 1
→ Canonical Representation A

Source Version 2
→ Canonical Representation B
```

the normal outcome should be:

```text
Integrity Reference A
→ preserves Representation A

Integrity Reference B
→ preserves Representation B
```

with separate Anchor Identifiers.

---

# Representation Boundary Change

A material Representation Boundary change normally creates a new integrity subject.

Example:

```text
Boundary A
→ JSON record only

Boundary B
→ JSON record + attached evidence package
```

Even if both arise from the same Source Artifact, the Integrity References preserve different things.

Therefore:

```text
new Representation Boundary
→ normally new Integrity Reference
```

---

# Canonicalization Change

Canonicalization changes require a subject-equivalence test.

### Equivalent Result

If a new canonicalization Version produces the same governed Canonical Representation:

```text
same subject
→ Anchor Version / method migration may be appropriate
```

### Different Result

If the canonicalization rules materially redefine what representation is protected:

```text
new subject
→ new Integrity Reference
```

---

# Integrity Method Change

Integrity Method changes normally do not change the integrity subject.

For the same Canonical Representation, Anchor may later add:

```text
new digest algorithm
digital signature
trusted timestamp
transparency commitment
Bitcoin commitment
```

These are additional or replacement integrity mechanisms for the same subject.

The normal architecture is:

```text
same Anchor Identifier
→ new Anchor Version or additional method evidence
```

depending on whether the canonical Anchor record changes.

---

# Algorithm Deprecation

Suppose an Integrity Reference originally uses:

```text
Algorithm A
```

and later Anchor adopts:

```text
Algorithm B
```

If the integrity subject remains unchanged:

```text
preserve Algorithm A evidence
add Algorithm B evidence
```

Historical proof must not be discarded.

---

# External Commitment Migration

If Anchor later moves from one external commitment method to another:

```text
timestamp service
→ Bitcoin commitment
```

that does not automatically create a new Integrity Reference.

If both commit to the same Integrity Value / same integrity subject, the change may be Versioned evidence.

---

# Correction and Versioning

The normal Correction model should be:

```text
same Integrity Reference
+ Anchor-owned error
→ Correction
→ new Anchor Version
```

Examples include:

- wrong Source location;
- wrong timestamp metadata;
- wrong signer reference;
- wrong publication URL;
- incorrect descriptive provenance.

However, if Anchor originally anchored the wrong Source Artifact or wrong Canonical Representation:

```text
wrong integrity subject
→ new Integrity Reference
```

The flawed prior record may then be withdrawn or superseded according to Lifecycle rules.

---

# Version History

Every production Version must remain preserved.

Conceptually:

```text
Anchor Identifier A

Version 1
↓
Version 2
↓
Version 3
```

Version 3 does not erase Versions 1 or 2.

Historical Version access is part of durable Anchor integrity.

---

# Version Relationships

Version lineage should eventually support relationships equivalent to:

```text
previous_version
next_version
```

The exact machine tokens remain governed by Relationships Controlled Values.

---

# Version Immutability

Once a production Version is published or otherwise committed as canonical, it should not be edited in place.

Instead:

```text
Version N
→ preserved

change
→ Version N+1
```

This is foundational to auditability.

---

# Draft Changes

Changes made before production assignment may occur without creating permanent Version history.

Conceptually:

```text
draft editing
→ draft editing
→ Validation
→ production Version 1
```

Whether internal draft Versions are retained is a Production Procedure decision.

---

# Changes That May Not Require Versioning

Changes outside the canonical Anchor record may not require a new Anchor Version.

Examples may include:

- CSS changes;
- navigation changes;
- footer changes;
- regenerated presentation wrappers;
- mirrored non-canonical URLs;
- transient UI state;
- analytics changes;
- unrelated site metadata.

Publication architecture must define the canonical Anchor representation.

---

# Versioning Decision Test

For any proposed change, ask:

```text
1. Did the Source Artifact identity change?
2. Did the Canonical Representation materially change?
3. Did the Representation Boundary materially change?
4. Is Anchor still preserving the same integrity subject?
5. Is the change only Anchor-owned metadata, evidence, or structure?
```

Decision:

```text
same integrity subject
→ Version where needed

different integrity subject
→ new Integrity Reference
```

---

# Version vs. Supersession

These must remain separate:

```text
new Anchor Version
→ same Anchor Identifier
```

versus:

```text
new Integrity Reference
→ new Anchor Identifier
→ may supersede earlier Integrity Reference
```

Supersession belongs to Relationships and Lifecycle.

Versioning preserves continuity inside one Integrity Reference.

---

# Version vs. Lifecycle

```text
Anchor Version
≠
Lifecycle State
```

Examples:

```text
Version 3
+ active
```

or:

```text
Version 3
+ superseded
```

may both be meaningful.

A lifecycle transition may or may not create a new Version depending on whether the canonical record changes.

---

# Version vs. Publication State

```text
Anchor Version
≠
Publication State
```

A Version may exist before publication.

A published Integrity Reference may later receive another Version.

Publication architecture should define which Version is currently canonical.

---

# Version vs. Verification Result

```text
Anchor Version
≠
Verification Result
```

Verification may occur many times against the same Version.

A new Verification event does not necessarily require a new Anchor Version unless Verification history is part of the canonical Anchor record representation.

That design choice remains to be finalized.

---

# Version vs. Integrity State

```text
Anchor Version
≠
Integrity State
```

State changes and Version changes may interact but should not be conflated.

Maintenance architecture should determine when state changes require Versioned record updates.

---

# Versioning and Schema

The Integrity Reference Base Schema already defines:

```text
anchor_version
```

as:

```text
integer
minimum 1
```

This Versioning architecture confirms that design.

A future schema revision should preserve the same model unless production demonstrates a need for something more complex.

---

# Versioning and Publication

Publication should preserve:

```text
current canonical Anchor Version
```

and allow access to:

```text
prior production Versions
```

A stable Anchor Identifier should resolve to the current canonical Version while exposing Version history.

Exact URL behavior remains unfrozen.

---

# Versioning and Corrections

Corrections architecture should use Versioning to ensure:

```text
wrong prior state remains preserved
corrected state becomes later Version
```

unless the Correction reveals that the record was about the wrong integrity subject entirely.

---

# Versioning and Maintenance

Maintenance may cause Version changes when Anchor-owned record content changes.

Potential examples include:

- new external commitment;
- updated algorithm status metadata;
- new canonical location;
- new maintenance result;
- repaired provenance metadata.

Maintenance should not create Versions unnecessarily for transient operational activity.

---

# Versioning Governance

Anchor Governance should eventually control:

- Version increment authority;
- Version publication;
- Version immutability;
- Version restoration;
- Version relationship rules;
- invalid Version handling;
- schema migration;
- supersession boundary decisions.

---

# Initial Freeze Decisions

### Anchor Version Model

```text
Sequential integer
```

### First Production Version

```text
1
```

### Increment Pattern

```text
1 → 2 → 3 → ...
```

### Core Decision Rule

```text
same integrity subject
→ new Anchor Version where needed

new integrity subject
→ new Integrity Reference
```

### Still Unfrozen

```text
whether every lifecycle change creates a Version
whether every Verification-history change creates a Version
whether Maintenance events are embedded or external
draft Version retention
Version-specific canonical URLs
Version relationship tokens
schema migration procedure
equivalence test for canonicalization changes
formal version-diff record
first production Version history
```

---

# Versioning Principle

> Preserve identity when the subject remains. Create new identity when the subject changes.

Anchor Versioning should preserve continuity, auditability, and historical meaning without using Version changes to disguise a materially different integrity subject.

---

## Status

**Post-Foundational Architecture**

Versioning architecture is now defined.

The initial Anchor Version model is frozen as sequential integers beginning at `1`.

**Version:** 1.0-draft

**Maintained By:** Satoshium
