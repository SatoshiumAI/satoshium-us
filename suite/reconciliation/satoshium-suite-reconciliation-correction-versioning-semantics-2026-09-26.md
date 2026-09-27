# Satoshium Suite Reconciliation — Correction & Versioning Semantics

**Date:** September 26, 2026  
**Phase:** II — Objects, Terminology & Semantics  
**Status:** COMPLETE — APPROVED

## Purpose

This record documents the Suite-wide reconciliation of correction, versioning, deletion, supersession, mutation, and canonical-identity semantics conducted during the September 26, 2026 phase of the Satoshium Suite Reconciliation.

The reconciliation preserves the following governing distinctions:

> **Correction ≠ Version**

> **Correction ≠ Deletion**

> **Supersession ≠ Mutation**

> **Changed Conclusion = Changed Canonical Statement**

The purpose of this record is to prevent silent rewriting of canonical history, accidental identity changes, ambiguous versioning, and the collapse of materially different conclusions into a single canonical object.

---

# 1. Correction

## Controlled Definition

**Correction** is the institution-governed act of fixing an error, omission, misstatement, metadata defect, reference defect, representation defect, or other correctable flaw in an existing canonical object or its approved representation.

Correction answers:

> **What was wrong, and how was it corrected?**

A correction may include:

- corrected metadata;
- corrected wording;
- corrected references;
- corrected provenance;
- corrected formatting;
- corrected representation;
- corrected supporting information;
- a new version of the same canonical object.

## Controlled Distinction

> **Correction ≠ Version**

Correction is the action or reason for change.

Version is the governed resulting state or edition of the same continuing canonical identity.

Conceptually:

```text
Correction
    ↓ may produce
New Version
```

---

# 2. Version

## Controlled Definition

**Version** is a governed state or edition of the same continuing canonical object identity.

It answers:

> **Which governed edition/state of this canonical object is this?**

Example:

```text
SREG-2026-0001
Version 1.0
    ↓ correction
SREG-2026-0001
Version 1.1
```

The identifier remains stable because the canonical object remains the same.

## Controlled Distinctions

> **Version ≠ New Canonical Object by default**

and:

> **Correction may produce a Version, but Correction itself is not Version.**

Institution-specific identity rules remain authoritative when determining whether a change is still a version of the same object or requires new canonical identity.

---

# 3. Correction vs Deletion

Correction preserves the governed object and repairs it.

Deletion removes an object or representation from availability or storage, where deletion is permitted by the owning institution.

These are fundamentally different actions.

```text
Correction
→ preserve identity and repair

Deletion
→ remove
```

Therefore:

> **CORRECTION ≠ DELETION**

Canonical history should not be silently removed merely because an error is discovered.

Where permitted, the preferred model is:

```text
Original Version
    ↓
Correction
    ↓
Corrected Version
```

with the correction history preserved.

---

# 4. Correction History

Canonical corrections should preserve historical traceability where appropriate.

The system should be able to preserve:

- what changed;
- why it changed;
- when it changed;
- which prior version was affected;
- which process or authority approved the change;
- which version or object superseded the prior state.

The governing principle is:

> **CORRECTION SHOULD REPAIR THE RECORD WITHOUT ERASING THE RECORD OF THE REPAIR.**

Correction must not become a mechanism for rewriting institutional history.

---

# 5. Supersession

## Controlled Definition

**Supersession** means that one canonical object or version replaces another in operative standing.

It answers:

> **Which object or version is now authoritative for current use within the applicable domain?**

Examples:

```text
Version 1.0
    ↓ superseded-by
Version 1.1
```

or:

```text
Object A
    ↓ superseded-by
Object B
```

depending on institution-specific identity rules.

## Controlled Distinction

> **Supersession ≠ Mutation**

The earlier object or version does not transform into the successor.

The prior state remains historically distinct and traceable.

---

# 6. Supersession Preserves History

A superseded object may remain:

- identifiable;
- published;
- archived;
- historically accessible;
- referenced by other records;
- part of provenance chains.

Therefore:

> **Superseded ≠ Deleted**

and:

> **Superseded ≠ Unpublished**

Supersession changes operative standing, not historical existence.

---

# 7. Mutation

## Controlled Meaning

**Mutation**, in the problematic sense, is the silent alteration of an existing canonical object so that its historical meaning changes without preserving the prior state.

This pattern should be avoided.

### Prohibited Pattern

```text
Object X
Meaning A
    ↓ silently rewritten
Object X
Meaning B
```

### Preferred Pattern — Non-Material Change

```text
Object X
Version 1.0
Meaning A
    ↓ governed correction
Object X
Version 1.1
Meaning A, corrected or clarified
```

### Preferred Pattern — Material Change

```text
Object X
    ↓ superseded-by
Object Y
```

This preserves prior meaning and prevents hidden historical rewriting.

---

# 8. Material vs Non-Material Change

## Non-Material Correction

A non-material correction preserves the canonical meaning of the object.

Examples may include:

- typographical correction;
- metadata repair;
- broken-reference repair;
- formatting correction;
- non-substantive clarification;
- provenance-field repair.

Likely result:

> Same canonical identity, with a new version where warranted.

## Material Change

A material change alters the substantive meaning, assertion, subject, decision, or conclusion of the canonical object.

Material changes may require:

> New canonical object identity.

The owning institution determines the threshold under its object-governance rules.

---

# 9. Attestor — Attestation Identity

Attestor preserves the rule:

> **Materially changed assertion = new Attestation**

Example:

```text
ATT-2026-0001
Assertion A
```

must not be silently converted through ordinary versioning into:

```text
ATT-2026-0001
Assertion B
```

when Assertion B is materially different.

The proper pattern is:

```text
ATT-2026-0001
    ↓ related / superseded as applicable
ATT-2026-0002
```

The earlier Attestation remains historically identifiable.

---

# 10. Attestor — Trust Statement Identity

The strongest identity rule in this reconciliation is:

> **Changed Conclusion = Changed Canonical Statement**

A Trust Statement carries a bounded canonical conclusion.

Example:

```text
TRST-2026-0001
Conclusion: Supported
```

must not become:

```text
TRST-2026-0001
Conclusion: Not Supported
```

through ordinary versioning.

That would mutate the canonical meaning.

The proper pattern is:

```text
TRST-2026-0001
Conclusion: Supported
        ↓ superseded-by
TRST-2026-0002
Conclusion: Not Supported
```

The prior statement remains preserved and traceable.

---

# 11. Certifier

For Certifier, ordinary correction or documentation refinement may remain within the same Certification Package identity when canonical certification meaning is unchanged.

However, a materially changed Certification Decision must not be silently rewritten.

The prior decision history must be preserved through the applicable Certifier mechanism, such as:

- a superseding certification object;
- recertification;
- another explicitly governed replacement mechanism.

The governing principle is:

> **Changed certification meaning must preserve the prior certification decision history.**

---

# 12. Registry

For Satoshium Registry Entries:

```text
Same registered subject
+ corrected Registry metadata
→ same SREG identity
→ new version where appropriate
```

But:

```text
Different registered subject
→ new SREG
```

Therefore:

> **Correction does not create a new SREG by default.**

and:

> **Changed registration identity requires a new SREG.**

---

# 13. Chronicle

Chronicle should preserve historical continuity.

Where the same historical Occurrence remains the subject:

> The same CHR identity may continue through governed correction and versioning.

Where the represented Occurrence is materially different:

> A new Chronicle Entry is required.

The governing rule is:

> **Correction ≠ historical rewriting**

The historical correction trail should remain visible where appropriate.

---

# 14. Anchor

Anchor preserves a clear identity rule:

```text
Same Integrity Subject
→ new Integrity Reference Version

New Integrity Subject
→ new Integrity Reference
```

The Integrity Subject is defined by:

- Source Artifact identity;
- Canonical Representation;
- Representation Boundary.

A materially changed source identity or representation boundary may therefore require new Anchor identity rather than ordinary versioning.

---

# 15. Beacon

For Discovery Signals:

```text
Same discovery subject
+ corrected metadata or context
→ same BEAC identity
→ new version as needed
```

But:

```text
Materially different discovery
→ new Discovery Signal
```

Beacon should not mutate one discovery into another.

---

# 16. Atlas

Atlas Jurisdiction Intelligence Packages may receive routine:

- evidence additions;
- evidence corrections;
- metadata repairs;
- normalization updates;
- interpretive clarifications;
- representation updates.

These may remain within the same package identity when the jurisdiction subject and canonical package meaning remain continuous.

Package maintenance should preserve provenance and change history.

A materially different subject or package scope may require a new canonical package identity or separately governed package.

The governing principle is:

> **Package evolution must not erase prior provenance or silently replace canonical meaning.**

---

# 17. Navigator

Navigator Workflow Definitions may be corrected or refined while retaining the same canonical identity when the workflow purpose and authority boundaries remain materially unchanged.

A materially different:

- workflow purpose;
- orchestration model;
- authority boundary;
- participating-system logic;
- canonical workflow meaning

may require a new Navigator Workflow Definition rather than mutation of the existing one.

---

# 18. Suite-Wide Change Decision Model

The preferred decision model is:

```text
Change Identified
      ↓
Is canonical meaning unchanged?
      ↓
YES
→ Correction
→ Same canonical identity
→ New version where appropriate
      ↓
NO
→ New canonical object
→ Explicit relationship to prior object
→ Prior object preserved
```

This model preserves identity discipline while allowing legitimate maintenance.

---

# 19. Relationship Semantics

Where a new canonical object replaces another, use explicit relationships such as:

- supersedes;
- superseded-by;
- replaces, only where formally defined;
- derived-from, where accurate;
- related-to, only where no stronger relationship applies.

Do not rely on silent replacement.

> **Supersession preserves separate identities.**

---

# 20. Prohibited Semantic Collapses

The following Suite-wide equivalences are prohibited:

- Correction = Version
- Correction = Deletion
- Correction = New Object automatically
- Version = New Canonical Identity automatically
- Supersession = Mutation
- Superseded = Deleted
- Superseded = Unpublished
- New Version = Changed Canonical Meaning automatically
- Changed Assertion = Same Attestation
- Changed Conclusion = Same Trust Statement
- Corrected Record = Erased Prior Record
- Updated Object = Silent Historical Rewrite

---

# 21. Suite-Wide Rules

The Correction & Versioning Semantics Reconciliation establishes the following rules:

1. **Correction ≠ Version.**
2. **Correction ≠ Deletion.**
3. Correction may produce a new version.
4. Version preserves canonical identity unless institution-specific identity rules require otherwise.
5. Correction should preserve historical traceability.
6. Supersession replaces operative standing without erasing prior identity.
7. **Supersession ≠ Mutation.**
8. Superseded objects may remain published and historically accessible.
9. Non-material corrections generally preserve canonical identity.
10. Material changes may require new canonical identity.
11. Materially changed assertion requires a new Attestation.
12. **Changed conclusion requires a new Trust Statement.**
13. Changed certification meaning must preserve prior certification history.
14. Same Registry subject may retain SREG identity across permitted corrections.
15. Different Registry subject requires a new SREG.
16. Same Chronicle Occurrence may retain CHR identity across governed correction/versioning.
17. Different Chronicle Occurrence requires a new Chronicle Entry.
18. Same Anchor Integrity Subject may version.
19. New Anchor Integrity Subject requires a new Integrity Reference.
20. Same Beacon discovery subject may version.
21. Materially different Beacon discovery requires a new Discovery Signal.
22. Atlas package maintenance must preserve provenance and change history.
23. Materially changed Navigator workflow meaning may require new Workflow Definition identity.
24. Canonical history must not be silently rewritten.
25. Prior canonical states should remain traceable when superseded or corrected.

---

# Governing Rule

> **CORRECTIONS REPAIR. VERSIONS PRESERVE CONTINUITY. SUPERSESSION PRESERVES HISTORY. MATERIAL CHANGE MAY REQUIRE NEW IDENTITY.**

For Attestor:

> **CHANGED CONCLUSION = CHANGED CANONICAL STATEMENT.**

---

# Final Disposition

**Correction / Versioning Semantics Reconciliation — COMPLETE — APPROVED**

This record should govern future correction handling, versioning, supersession, recertification, historical preservation, Trust Statement replacement, object identity decisions, and documentation conformance across the Satoshium Suite.
