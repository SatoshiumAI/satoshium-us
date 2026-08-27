# Publication

## Overview

**Publication** defines when a completed Satoshium Anchor Integrity Reference becomes a publicly authoritative Anchor record.

Publication governs:

- Publication Gate;
- public Anchor authority;
- canonical HTML;
- canonical JSON;
- publication timestamps;
- human / machine consistency;
- current-Version resolution;
- historical Version visibility;
- Correction notices;
- Lifecycle notices;
- publication withdrawal;
- publication Maintenance.

The governing principle is:

> Publish only what Anchor can preserve, explain, verify, and version.

---

## Public Authority Boundary

Publication makes Anchor authoritative for:

```text
Integrity Reference
Anchor Identifier
Anchor Version
Anchor-owned integrity metadata
Anchor provenance
Anchor relationships
Anchor lifecycle state
Anchor publication state
```

Publication does not make Anchor authoritative for:

```text
Source Artifact meaning
Source truth
Source certification
Source trustworthiness
Source lifecycle
```

Therefore:

```text
Public Anchor Record Authority
≠
Source Artifact Authority
```

> Reference does not transfer authority.

---

# Publication Gate

Anchor should use a formal **Publication Gate** before a draft Integrity Reference becomes publicly authoritative.

The conceptual sequence is:

```text
Completed Integrity Reference
        ↓
Validation / Institutional Review
        ↓
Initial Verification
        ↓
Publication Gate
        ↓
APPROVED
or
NOT APPROVED
        ↓
Canonical Public Anchor Record
```

The Publication Gate is now an architecturally required production control.

---

# Why a Publication Gate Is Necessary

Without a Gate, publication can become equivalent to:

```text
file exists
→ therefore public record
```

That is insufficient for an institutional system.

The Gate ensures that a public Anchor record has crossed a governed boundary.

---

# Publication Gate Decision

The Publication Gate should produce:

```text
APPROVED
```

or:

```text
NOT APPROVED
```

These are Gate decisions.

They are not automatically Publication State values.

---

# Gate Decision vs. State

```text
Publication Gate Decision
≠
Publication State
```

The Gate Decision answers:

> May this Version become publicly authoritative now?

Publication State answers:

> What is the durable publication condition of this record?

This distinction should remain explicit.

---

# Publication Preconditions

Before Gate approval, the Integrity Reference should normally have:

```text
Anchor Identifier
Anchor Version
Source Institution
Source-System Identifier
Source Artifact type
Canonical Representation
Representation Boundary
Integrity Method
Integrity Value / proof material
required Provenance
required Relationships
Initial Verification
appropriate Lifecycle State
no blocking Correction
canonical HTML candidate
canonical JSON candidate
```

Validation should eventually turn these expectations into formal checks.

---

# Validation and Publication

Validation should answer:

> Does this Integrity Reference satisfy Anchor's structural and institutional requirements for publication?

Conceptually:

```text
Validation
+
Initial Verification
→ Publication Gate evidence
```

The precise Validation sequence remains defined by `/anchor/validation/`.

---

# Verification and Publication

Initial Verification should normally occur before Publication Gate approval.

Conceptually:

```text
Integrity Reference constructed
        ↓
Initial Verification
        ↓
Publication Gate
```

A later Reverification event does not automatically require republishing the Integrity Reference.

Republication is required only when canonical Anchor record data changes.

---

# APPROVED

`APPROVED` means:

> Anchor has determined that the current Anchor Version is eligible to enter public institutional use.

Approval does not mean:

```text
Source content is true
Source is trusted
Certification succeeded
future Verification is guaranteed
```

---

# NOT APPROVED

`NOT APPROVED` means:

> The current Anchor Version is not eligible to enter public institutional use.

Potential causes include:

- incomplete schema;
- failed institutional Validation;
- unresolved Verification issue;
- missing Provenance;
- invalid Relationship;
- unresolved Correction;
- unclear Representation Boundary;
- missing canonical publication representation;
- governance hold.

NOT APPROVED should preserve draft work without creating a misleading public production event.

---

# Canonical Public Representations

A published Integrity Reference should have two primary canonical public representations:

```text
Canonical HTML
Canonical JSON
```

These serve different audiences but must express the same institutional state.

---

# Canonical HTML

The canonical HTML is the human-readable public representation.

It should clearly expose material information such as:

```text
Anchor Identifier
Anchor Version
Source Institution
Source-System Identifier
Source Artifact type
Representation Boundary
Integrity Method
Integrity Value / proof context
Lifecycle State
Publication State
published_at
Correction notice
supersession / withdrawal notice
```

Exact presentation is not frozen.

---

# Canonical JSON

The canonical JSON is the machine-readable public representation.

It should conform to the applicable Integrity Reference Schema.

It should support:

- schema validation;
- independent Verification;
- archival preservation;
- relationship resolution;
- cross-Suite processing;
- future API use.

---

# Human / Machine Consistency

The canonical HTML and JSON must not disagree on institutional facts.

Conceptually:

```text
Canonical HTML
↔
Canonical JSON
```

Both should represent the same:

```text
Anchor Identifier
Anchor Version
Source identity
integrity subject
Integrity Method
Integrity Value
Lifecycle State
material Corrections
publication timestamp
```

Presentation may differ.

Meaning may not.

---

# Canonical vs. Derived Presentation

Anchor may publish:

- indexes;
- search results;
- discovery cards;
- summary pages;
- mirrors;
- dashboards;
- navigation pages.

These are derived presentations.

They are not automatically canonical Integrity Reference representations.

```text
Canonical Anchor Record
≠
Derived Presentation
```

Derived pages should reference the canonical record.

---

# Publication Timestamp

Every publicly authoritative Anchor Version should preserve:

```text
published_at
```

This timestamp represents:

> when the Version entered public Anchor authority.

It does not necessarily equal:

```text
Source creation time
Integrity generation time
Verification time
```

---

# Time Separation

Anchor should preserve:

```text
Source creation time
≠
Source retrieval time
≠
Integrity generation time
≠
Verification time
≠
Publication time
```

These timestamps serve different evidentiary purposes.

---

# Current Canonical Version

A stable Anchor Identifier should resolve to the current canonical production Version.

Conceptually:

```text
Anchor Identifier
        ↓
Current Canonical Anchor Version
```

This resolution should not erase historical Versions.

---

# Historical Version Access

Prior production Versions should remain accessible.

Example:

```text
Anchor Identifier A

Version 1
→ historical

Version 2
→ historical

Version 3
→ current canonical
```

Public presentation should clearly identify:

- current Version;
- prior Versions;
- Version effective times;
- Correction history where applicable.

---

# Canonical URL Architecture

Publication will eventually require stable canonical URLs.

Potential architecture:

```text
stable Integrity Reference URL
canonical JSON URL
Version-specific historical URLs
```

Exact URL syntax remains unfrozen because the final Anchor Identifier format is still unfrozen.

---

# URL vs. Identifier

A canonical URL is a location.

An Anchor Identifier is identity.

Therefore:

```text
Canonical URL
≠
Anchor Identifier
```

The URL may contain the Identifier.

The URL does not replace it.

---

# Correction Publication

Material Corrections should be publicly visible.

Conceptually:

```text
Version 1
→ published

Correction
→ recorded

Version 2
→ current canonical
```

Public Version 2 should make the Correction visible.

Version 1 should remain historically available.

---

# Lifecycle Publication Behavior

Initial publication behavior should conceptually be:

```text
draft
→ not publicly authoritative

active
→ current public record where published

superseded
→ preserved with supersession notice

withdrawn
→ preserved with withdrawal notice

archived
→ preserved with archival notice
```

Lifecycle does not automatically equal Publication State.

---

# Withdrawal Does Not Mean Erasure

Anchor should preserve historical publication evidence.

```text
withdrawn
≠
deleted
```

unless legal, security, privacy, or safety requirements require restricted access.

Even then, internal institutional history should be preserved where permitted.

---

# Publication State

Publication architecture proves the need for a durable Publication State category.

Initial candidate values are:

```text
unpublished
published
withdrawn_from_publication
```

These are not yet frozen.

The key open question is whether an `approved` state is necessary.

Current architecture suggests:

```text
APPROVED
```

should remain a Gate decision rather than a durable Publication State.

Validation and Procedures should confirm this.

---

# Publication State vs. Lifecycle State

```text
Publication State
≠
Lifecycle State
```

Examples may include:

```text
active + unpublished
active + published
superseded + published
withdrawn + published
archived + published
```

This separation preserves institutional clarity.

---

# Publication State vs. Verification Result

```text
Publication State
≠
Verification Result
```

A Verification event may later fail while the historical record remains published with an appropriate notice.

Maintenance and Governance should determine response.

---

# Publication and Versioning

Every new production Anchor Version should receive its own publication decision before replacing the current canonical Version.

Conceptually:

```text
Version N
        ↓
governed change
        ↓
Version N+1
        ↓
Validation / Verification
        ↓
Publication Gate
        ↓
Version N+1 becomes canonical
```

Version N remains historical.

---

# Publication and Corrections

A corrected Anchor Version should not silently replace the historical Version.

Public publication should preserve:

```text
prior Version
Correction notice
current Version
```

This is the publication expression of:

> Correct forward. Preserve backward.

---

# Publication and Maintenance

Maintenance should monitor:

- canonical HTML availability;
- canonical JSON availability;
- current-Version resolution;
- historical Version resolution;
- human / machine consistency;
- Correction notices;
- Lifecycle notices;
- Source links;
- external commitment references.

Broken publication infrastructure should not silently alter institutional meaning.

---

# Publication Record

Anchor may later preserve a separately structured Publication record.

Potential fields include:

```text
Anchor Identifier
Anchor Version
Gate decision
decision time
published_at
canonical HTML URL
canonical JSON URL
Validation result
Verification result
publication notes
```

Whether the Publication record receives its own identifier remains unfrozen.

---

# Publication Procedure

The conceptual publication procedure is:

```text
1. Complete Integrity Reference construction.
2. Confirm Anchor Identifier and Anchor Version.
3. Complete required Validation.
4. Complete Initial Verification.
5. Confirm no blocking Correction or governance hold.
6. Generate canonical HTML.
7. Generate canonical JSON.
8. Confirm human / machine consistency.
9. Apply Publication Gate.
10. Record APPROVED or NOT APPROVED.
11. If APPROVED, assign published_at.
12. Publish canonical representations.
13. Update current-Version resolution.
14. Update Integrity Reference index.
15. Preserve prior Versions and notices.
```

This should later become a formal procedure under `/anchor/procedures/`.

---

# Current Freeze Decisions

### Publication Gate

```text
Required
```

### Gate Decisions

```text
APPROVED
NOT APPROVED
```

These are workflow decisions, not yet Controlled Values for Publication State.

### Canonical Public Representations

```text
Canonical HTML
Canonical JSON
```

### Publication Timestamp

```text
published_at
```

required for publicly authoritative Anchor Versions.

### Publication State Category

```text
Architecturally required
```

### Candidate Publication State Values

```text
unpublished
published
withdrawn_from_publication
```

### Production Publication State Enumeration Frozen

```text
No
```

### Still Unfrozen

```text
final Publication State values
whether APPROVED is ever stored as durable state
Publication Gate record schema
Publication identifier
canonical URL format
Version-specific URL format
publication withdrawal procedure
restricted-access behavior
human / machine consistency Validation rules
Publication Gate approval authority
first production publication event
```

---

# Publication Principle

> Publish only what Anchor can preserve, explain, verify, and version.

Anchor Publication should create durable public authority over the Integrity Reference itself while preserving Source authority, historical Version access, Correction transparency, and human/machine consistency.

---

## Status

**Post-Foundational Architecture**

Publication architecture is now defined.

A formal Publication Gate is required.

Canonical HTML and canonical JSON are established as the primary public representations.

**Version:** 1.0-draft

**Maintained By:** Satoshium
