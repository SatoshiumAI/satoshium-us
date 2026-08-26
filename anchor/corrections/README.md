# Corrections

## Overview

**Corrections** define how Satoshium Anchor repairs Anchor-owned errors while preserving the historical record.

The governing principle is:

> Correct forward. Preserve backward.

A Correction must never silently rewrite history.

The central authority distinction is:

```text
Source Artifact Change
≠
Anchor Correction
```

Source Institutions correct their own artifacts.

Anchor corrects only Anchor-owned information.

---

## Purpose

Corrections answer:

> What happens when Anchor itself recorded something incorrectly?

Examples include:

- incorrect Source reference;
- incorrect Representation Boundary;
- incorrect integrity material;
- incorrect provenance;
- incorrect relationship;
- incorrect signer metadata;
- incorrect publication metadata.

Corrections do not govern legitimate Source-system changes.

---

# Source Artifact Change vs. Anchor Correction

A **Source Artifact Change** occurs under Source authority.

Examples:

```text
Source publishes new Version
Source corrects content
Source withdraws artifact
Source revokes statement
Source supersedes artifact
Source changes lifecycle
```

These are not Anchor Corrections.

An **Anchor Correction** occurs when Anchor's own record was wrong.

Examples:

```text
wrong Source-System Identifier
wrong Source Institution
wrong Representation Boundary
wrong canonicalization metadata
wrong Integrity Value
wrong algorithm metadata
wrong timestamp
wrong signer reference
wrong relationship
wrong publication metadata
```

---

# Core Correction Rule

The first question is:

```text
Was Anchor wrong?
```

If no:

```text
not an Anchor Correction
```

If yes, ask:

```text
Does the integrity subject remain the same?
```

If yes:

```text
Correction
→ new Anchor Version
```

If no:

```text
new Integrity Reference
→ new Anchor Identifier
```

The flawed earlier Integrity Reference may then require withdrawal or supersession.

---

# Integrity Subject Test

Versioning defined the integrity subject as:

```text
Source Artifact identity
+
Canonical Representation
+
Representation Boundary
```

Corrections use the same test.

### Same Subject

Examples:

- wrong timestamp metadata;
- wrong Source URL;
- wrong signer reference;
- wrong publication path;
- wrong digest stored for the correct representation;
- wrong relationship metadata.

Normal outcome:

```text
same Anchor Identifier
→ Correction
→ new Anchor Version
```

### Wrong Subject

Examples:

- wrong Source Artifact;
- wrong Canonical Representation;
- materially wrong Representation Boundary;
- wrong artifact package;
- wrong Source identity.

Normal outcome:

```text
flawed Integrity Reference
→ withdraw / supersede

correct integrity subject
→ new Integrity Reference
→ new Anchor Identifier
```

---

# Correction Lineage

Every production Correction should preserve enough information to reconstruct:

```text
affected Anchor Identifier
affected Anchor Version
error discovered
error description
affected field / condition
prior value
corrected value
correction reason
corrected Anchor Version
effective time
related Verification event
related Maintenance event
lifecycle consequence
```

Exact field names remain unfrozen.

---

# Correction History

Corrections are cumulative institutional history.

Conceptually:

```text
Anchor Version 1
→ contains error

Correction 1
→ identifies error

Anchor Version 2
→ contains corrected state
```

Version 1 remains preserved.

Version 2 does not overwrite Version 1.

---

# Correction Record

Anchor may eventually create separately identified Correction records.

Potential architecture:

```text
Integrity Reference
        ↓
corrected_by
        ↓
Correction Record
        ↓
applied_in
        ↓
Anchor Version N+1
```

Whether Correction Records receive their own identifiers remains unfrozen.

Production procedure should prove whether separate Correction records add enough value beyond Version history.

---

# Correction Type

**Correction Type** is now proven to be a useful Controlled Value category.

Initial candidate values include:

```text
source_reference_error
representation_error
integrity_material_error
provenance_error
relationship_error
attribution_error
publication_metadata_error
lifecycle_metadata_error
other_anchor_metadata_error
```

These are not production-frozen.

The first real Correction cases should determine which distinctions are operationally meaningful.

---

# Source Reference Error

A Source reference error may include:

- wrong Source-System Identifier;
- wrong Source Institution;
- wrong Source URL;
- wrong Source Version metadata.

If the actual integrity subject remains identifiable and unchanged:

```text
Correction + new Anchor Version
```

may be sufficient.

If the wrong Source reference means the wrong artifact was actually anchored:

```text
new Integrity Reference
```

is required.

---

# Representation Error

Representation errors require careful subject analysis.

### Metadata Error Only

If the record described the Representation Boundary incorrectly but the actual Canonical Representation used for integrity generation was correct:

```text
Correction
→ new Anchor Version
```

may be appropriate.

### Wrong Representation Actually Anchored

If Anchor generated integrity material from the wrong representation:

```text
wrong integrity subject
→ new Integrity Reference
```

is the normal outcome.

---

# Integrity Material Error

Examples include:

- wrong digest;
- wrong signature metadata;
- wrong external commitment identifier;
- wrong timestamp proof;
- wrong algorithm identifier.

If the intended Canonical Representation was correct:

```text
same subject
+ wrong integrity material
→ Correction
→ new Anchor Version
```

Reverification should follow.

---

# Provenance Error

Examples include incorrect:

- producing system;
- generation timestamp;
- canonicalization method;
- signer reference;
- key reference;
- transformation details;
- external commitment provenance.

Anchor should distinguish:

```text
provenance was recorded incorrectly
```

from:

```text
the actual historical process later changed
```

Only the former is a Correction.

---

# Relationship Error

Examples include an incorrect:

- Source relationship;
- previous-Version relationship;
- Correction relationship;
- supersession relationship;
- external commitment relationship.

A relationship Correction should preserve the incorrect prior relationship in historical Version state.

---

# Attribution Error

Anchor may incorrectly record:

- signer;
- institutional role;
- reviewer;
- producing system;
- key reference.

These are Anchor-owned attribution errors when Anchor recorded them incorrectly.

They do not give Anchor identity authority over the person or institution.

---

# Publication Metadata Error

Examples include:

- wrong canonical URL;
- wrong publication timestamp;
- wrong public JSON location;
- wrong publication state metadata.

These may be corrected through Versioning without changing the integrity subject.

---

# Lifecycle Metadata Error

Anchor may record the wrong Lifecycle State or transition metadata.

Example:

```text
record marked archived
when governed decision was superseded
```

The error is Anchor-owned.

The corrected lifecycle history must preserve the prior incorrect production state.

---

# Severity

Correction severity may eventually be useful.

Candidate conceptual levels include:

```text
clerical
material
integrity_affecting
subject_invalidating
```

These values are not frozen.

The architecture should avoid adding a Severity category unless it changes:

- review requirements;
- publication behavior;
- lifecycle response;
- Verification requirements;
- governance approval.

---

# Clerical Corrections

A clerical Correction may include:

- spelling error;
- non-material notes;
- formatting metadata;
- harmless descriptive typo.

Even clerical production changes should preserve Version history where they alter the canonical Anchor record.

---

# Material Corrections

A material Correction affects information needed to interpret the Integrity Reference.

Examples:

- Source Version metadata;
- Representation Boundary description;
- signer identity reference;
- relationship target.

Material Corrections should be visibly published.

---

# Integrity-Affecting Corrections

An integrity-affecting Correction changes information directly used for Verification.

Examples:

- Integrity Value;
- algorithm;
- canonicalization method;
- proof material;
- external commitment identifier.

These should normally require:

```text
Correction
→ new Anchor Version
→ Reverification
```

---

# Subject-Invalidating Errors

A subject-invalidating error means the original Integrity Reference was about the wrong integrity subject.

Examples:

```text
wrong Source Artifact
wrong canonical representation
wrong package
materially wrong Representation Boundary
```

The normal response is not merely:

```text
Version 2
```

Instead:

```text
new Integrity Reference
→ new Anchor Identifier
```

The flawed prior Integrity Reference should remain preserved under an appropriate Lifecycle State.

---

# Verification-Discovered Corrections

Verification may reveal a mismatch.

The required sequence is:

```text
Verification mismatch
        ↓
investigate cause
        ↓
Source changed?
Anchor error?
Reviewed wrong representation?
External method unavailable?
        ↓
Correction only if Anchor error is confirmed
```

Mismatch does not itself prove that Anchor needs a Correction.

---

# Maintenance-Discovered Corrections

Maintenance may identify errors such as:

- broken Source location;
- stale publication metadata;
- wrong current commitment reference;
- relationship inconsistency;
- incorrect method-status metadata.

Maintenance should route confirmed Anchor errors through Correction architecture.

It should not silently modify production records.

---

# Correction and Versioning

Versioning provides the normal Correction mechanism.

```text
Anchor Version N
→ preserved

Correction
→ recorded

Anchor Version N+1
→ corrected state
```

The Anchor Identifier remains stable when the integrity subject remains the same.

---

# Correction and Lifecycle

Correction does not automatically set Lifecycle State.

Possible outcomes include:

```text
active remains active
active → withdrawn
active → superseded
active → archived
```

The lifecycle response depends on severity and subject validity.

---

# Correction and Publication

Publication should expose material Corrections.

A public record should make it possible to determine:

```text
current Anchor Version
prior Anchor Versions
Correction existence
Correction effective time
Correction reason
current corrected state
```

Public presentation may emphasize the current Version.

It must not create the false impression that prior production state never existed.

---

# Correction and Relationships

Correction lineage may require relationships equivalent to:

```text
corrects
corrected_by
applied_in
supersedes
superseded_by
```

The final Relationship Type enumeration remains governed elsewhere.

---

# Correction and Provenance

A Correction itself has provenance.

Potential Correction provenance includes:

- detection method;
- Verification event;
- Maintenance event;
- reviewer or process;
- effective time;
- Version created;
- publication update.

The minimum required Correction provenance remains unfrozen.

---

# Correction and Schema

The current Base Schema supports:

```text
corrections[]
```

with conceptual fields:

```text
correction_identifier
correction_type
applied_in_anchor_version
```

Corrections architecture now confirms the need for Correction references.

A separate Correction schema should be created only if separately identified Correction Records are adopted.

---

# No Destructive Correction

Anchor must not correct a production record by rewriting the historical Version in place.

Prohibited model:

```text
Version 1
→ silently edited
```

Required model:

```text
Version 1
→ preserved

Correction
→ documented

Version 2
→ corrected
```

This is the practical meaning of:

> Correct forward. Preserve backward.

---

# Correction Validation

A future Validation or Production Procedure should verify:

```text
affected Anchor Identifier exists
affected Anchor Version exists
error is Anchor-owned
prior state preserved
Correction reason provided
corrected state supplied
Version increment valid
subject continuity decision documented
lifecycle consequence valid
relationship lineage coherent
Reverification completed where required
```

No formal Validation rule numbers are defined here.

---

# Correction Procedure

The conceptual procedure is:

```text
1. Detect potential error.
2. Preserve the current production state.
3. Determine Source change vs. Anchor error.
4. Determine whether the integrity subject remains the same.
5. Classify the Correction where useful.
6. Record prior and corrected values.
7. Create new Anchor Version or new Integrity Reference.
8. Preserve Correction lineage.
9. Apply lifecycle consequence where required.
10. Publish Correction notice / current state.
11. Reverify where applicable.
```

This should later become a formal procedure under `/anchor/procedures/`.

---

# Current Freeze Decisions

### Core Correction Principle

```text
Correct forward. Preserve backward.
```

### Authority Boundary

```text
Source Artifact Change
≠
Anchor Correction
```

### Normal Same-Subject Correction

```text
same integrity subject
+ Anchor error
→ Correction
→ new Anchor Version
```

### Subject-Invalidating Error

```text
wrong integrity subject
→ new Integrity Reference
→ new Anchor Identifier
```

### Correction Type Category

```text
Architecturally required
```

### Production Correction Type Enumeration Frozen

```text
No
```

### Separately Identified Correction Record Frozen

```text
No
```

### Still Unfrozen

```text
Correction Identifier format
Correction Record schema
Correction Type values
Correction Severity values
Correction approval authority
Correction publication format
Correction notice requirements
mandatory Reverification thresholds
lifecycle consequence rules
Correction provenance minimum
first production Correction
```

---

# Correction Principle

> Correct forward. Preserve backward.

Anchor Corrections should repair present accuracy while preserving evidence of past institutional state.

---

## Status

**Post-Foundational Architecture**

Correction semantics, authority boundaries, subject-validity test, Versioning behavior, and lineage requirements are now defined.

**Version:** 1.0-draft

**Maintained By:** Satoshium
