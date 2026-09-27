# Satoshium Suite Reconciliation — Identifier-Family Audit

**Date:** September 26, 2026  
**Phase:** Phase II — Objects, Terminology & Semantics  
**Decision Class:** RECONCILE  
**Status:** COMPLETE — APPROVED

---

## Purpose

This audit reviews the canonical identifier families used across the Satoshium Suite and reconciles what those identifiers mean — and, equally important, what they do **not** mean.

The goal is to ensure that identifier syntax is not being used as an implied substitute for:

- institutional authority;
- lifecycle state;
- publication state;
- validation;
- conformance;
- evaluation outcome;
- version;
- provenance;
- or relationship.

The governing principle is:

> **An identifier establishes identity within an institutional namespace. It does not independently establish authority, status, meaning, or relationship.**

---

## Canonical Identifier Families Reviewed

The current formal Suite identifier families include:

```text
Certifier
→ SC-CERT-YYYY-NNNN

Registry
→ SREG-YYYY-NNNN

Chronicle
→ CHR-YYYY-NNNN

Anchor
→ ANCH-YYYY-NNNN

Beacon
→ BEAC-YYYY-NNNN

Attestor — Attestation
→ ATT-YYYY-NNNN

Attestor — Trust Statement
→ TRST-YYYY-NNNN
```

Navigator does not currently require an invented `NAV-*` identifier family.

Atlas does not require a new identifier family to be invented as part of this reconciliation.

The audit therefore preserves existing identifier architecture rather than creating naming schemes solely for symmetry.

---

# Core Identifier Rule

For every formal identifier family:

```text
Identifier
→ establishes canonical identity
→ establishes institutional namespace
```

An identifier does **not**, by itself, establish:

```text
authority
lifecycle state
publication state
validation result
conformance result
evaluation outcome
version
provenance
relationship
currentness
truth
trust
```

This distinction applies across the Suite.

---

# Certifier — `SC-CERT-YYYY-NNNN`

The formal Certifier identifier family is:

```text
SC-CERT-YYYY-NNNN
```

Example:

```text
SC-CERT-2026-0001
```

The identifier establishes:

- Certifier namespace;
- canonical Certification Package identity;
- identifier year;
- sequence identity within the family.

It does not independently mean:

- Certified;
- Active;
- Published;
- Valid;
- Current;
- Version 1.0;
- supported by Attestor;
- registered;
- historically preserved;
- integrity-protected;
- discovered.

Therefore:

> **SC-CERT identity ≠ Certification Outcome by syntax alone.**

The Certification Package and its governed decision fields establish the substantive certification result.

---

# Registry — `SREG-YYYY-NNNN`

The formal Registry identifier family is:

```text
SREG-YYYY-NNNN
```

Example:

```text
SREG-2026-0001
```

The identifier establishes:

- Registry namespace;
- Satoshium Registry Entry identity;
- identifier year;
- sequence identity.

It does not mean:

- the source object is certified;
- the source object is valid;
- the source object is trusted;
- the source object is current;
- the source object shares the same lifecycle state as the SREG.

Therefore:

> **SREG identity establishes registration identity, not source authority.**

---

# Chronicle — `CHR-YYYY-NNNN`

The formal Chronicle identifier family is:

```text
CHR-YYYY-NNNN
```

Example:

```text
CHR-2026-0001
```

The identifier establishes:

- Chronicle namespace;
- Chronicle Entry identity;
- identifier year;
- sequence identity.

It does not mean:

- the source object's event date equals the identifier year;
- Chronicle owns the source object's substantive authority;
- the event is certified;
- the event is validated by another institution;
- the source object is current.

Therefore:

> **CHR identity establishes Chronicle Entry identity, not source-object authority.**

---

# Anchor — `ANCH-YYYY-NNNN`

The formal Anchor identifier family is:

```text
ANCH-YYYY-NNNN
```

Example:

```text
ANCH-2026-0001
```

The identifier establishes:

- Anchor namespace;
- Integrity Reference identity;
- identifier year;
- sequence identity.

It does not mean:

- the source is true;
- the source is certified;
- the entire package is protected;
- the source representation is currently valid;
- integrity has been verified unless the relevant verification state says so.

Therefore:

> **ANCH identity ≠ proof of truth, certification, or whole-package integrity.**

The Integrity Subject and Representation Boundary determine what is actually protected.

---

# Beacon — `BEAC-YYYY-NNNN`

The formal Beacon identifier family is:

```text
BEAC-YYYY-NNNN
```

Example:

```text
BEAC-2026-0001
```

The identifier establishes:

- Beacon namespace;
- Discovery Signal identity;
- identifier year;
- sequence identity.

It does not mean:

- Verified;
- Certified;
- Registered;
- Trusted;
- Supported;
- historically preserved.

Therefore:

> **BEAC identity establishes Discovery Signal identity, not a trust or verification outcome.**

---

# Attestor — `ATT-YYYY-NNNN`

The formal Attestation identifier family is:

```text
ATT-YYYY-NNNN
```

Example:

```text
ATT-2026-0001
```

The identifier establishes:

- Attestor namespace;
- Attestation identity;
- identifier year;
- sequence identity.

It does not mean:

- the assertion is supported;
- the assertion is true;
- the Attestation is valid;
- the Attestation is published;
- a Trust Statement exists.

Therefore:

> **ATT identity establishes the canonical assertion object, not its evaluation result.**

---

# Attestor — `TRST-YYYY-NNNN`

The formal Trust Statement identifier family is:

```text
TRST-YYYY-NNNN
```

Example:

```text
TRST-2026-0001
```

The identifier establishes:

- Attestor Trust Statement namespace;
- Trust Statement identity;
- identifier year;
- sequence identity.

It does not, by itself, mean:

- Supported;
- Partially Supported;
- Not Supported;
- Contradicted;
- Indeterminate;
- Active;
- Published;
- current;
- universally true;
- universally trusted.

The conclusion belongs to the Trust Statement's governed content.

Therefore:

> **TRST identity ≠ trust outcome by syntax alone.**

---

# Identifier Year Semantics

The `YYYY` component identifies the year used in the identifier family.

It should not be silently interpreted as every other time-related field.

The identifier year is not necessarily identical to:

```text
effective year
publication year
evidence year
occurrence year
expiration year
supersession year
correction year
```

Those dates require their own governed fields.

Therefore:

> **Identifier year ≠ universal temporal meaning.**

---

# Sequence Number Semantics

The `NNNN` sequence identifies an object's position within the identifier family.

For example:

```text
0001
```

means the first identifier allocated within that family's relevant sequence.

It does not imply:

- higher authority;
- earlier source chronology across institutions;
- dependency;
- relationship;
- matching production stage;
- common subject.

Therefore:

> **Sequence number ≠ semantic relationship.**

---

# Matching Numbers Across Institutions

The first production objects include:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
BEAC-2026-0001
ATT-2026-0001
TRST-2026-0001
```

The repeated:

```text
0001
```

suffix does not itself establish a relationship.

These objects are related because explicit governed relationships connect them.

They are **not** related merely because they share a sequence number.

Therefore:

> **MATCHING IDENTIFIER SUFFIXES ≠ RELATIONSHIP.**

And:

> **Relationship must be explicitly represented.**

---

# Identifier Similarity Does Not Establish Lineage

The first production lineage is real.

But its lineage is established through:

- source references;
- typed relationships;
- production records;
- provenance;
- derivation;
- institutional actions.

It is not established by matching identifier numbers.

Thus:

```text
SC-CERT-2026-0001
→ SREG-2026-0001
```

is meaningful because Registry explicitly registers/references the Certification Package.

It is not meaningful because both identifiers end in `0001`.

Therefore:

> **IDENTIFIER SIMILARITY ≠ LINEAGE.**

---

# Identifier ≠ Authority

Authority belongs to institutions and governed domains.

For example:

```text
SC-CERT-*
→ identifies Certifier canonical objects

SREG-*
→ identifies Registry canonical objects
```

The identifier reflects institutional namespace.

It does not independently create authority.

Therefore:

> **Identifier namespace reflects authority domain; identifier syntax does not create authority.**

---

# Identifier ≠ Lifecycle State

An identifier persists across lifecycle changes where the same canonical identity is preserved.

For example:

```text
SREG-2026-0001
```

may move through lifecycle states without changing identifier.

Therefore:

```text
Identifier
≠
Lifecycle State
```

And:

```text
same identifier
≠
same lifecycle state forever
```

---

# Identifier ≠ Publication State

A canonical object may exist before publication.

Therefore:

```text
Identifier assigned
≠
Published
```

A published object may later be unpublished, superseded, archived, or otherwise change publication state while preserving identity.

Publication requires a separate governed state.

---

# Identifier ≠ Version

Version is distinct from canonical identity.

A canonical object may have:

```text
same identifier
+
new version
```

when the institutional semantics permit continuity of identity.

Therefore:

> **Identifier ≠ Version**

And:

> **Version suffixes or fields must not be inferred solely from sequence number.**

---

# Identifier ≠ Validation

An object's identifier says nothing about whether the object has passed Validation.

Thus:

```text
ATT-2026-0001 exists
```

does not mean:

```text
ATT-2026-0001 is VALID
```

Validation requires a separate governed result.

Therefore:

> **IDENTIFIED ≠ VALID**

---

# Identifier ≠ Conformance

Likewise:

```text
Identifier
≠
Conformance result
```

A conformant or non-conformant state must be explicitly recorded against an applicable requirement set.

And:

> **NOT-TESTED ≠ PASS**

regardless of whether the object has a canonical identifier.

---

# Identifier ≠ Evaluation Outcome

For Attestor:

```text
ATT-2026-0001
```

does not encode:

```text
Supported
Partially Supported
Not Supported
Contradicted
Indeterminate
```

Likewise:

```text
TRST-2026-0001
```

does not reveal the conclusion by identifier syntax.

Therefore:

> **Evaluation Outcome must remain explicit.**

---

# Identifier ≠ Relationship

Relationships must remain separately typed.

Examples:

```text
references
derived-from
supports
evaluates
results-in
supersedes
corrects
related-to
```

No identifier family should be interpreted as automatically creating one of these relationships.

Therefore:

> **Canonical identity and semantic relationship are separate dimensions.**

---

# Navigator Identifier Treatment

Navigator's canonical object is:

> **Navigator Workflow Definition**

No `NAV-*` identifier family is invented during reconciliation.

The reason is architectural discipline:

> **Symmetry alone is not sufficient reason to create a new identifier family.**

If Navigator later requires a formal identifier family, that should be established by explicit Navigator governance rather than inferred from other institutions.

---

# Atlas Identifier Treatment

Atlas's canonical object is:

> **Jurisdiction Intelligence Package**

The reconciliation does not invent a new Atlas identifier family solely to parallel the other institutions.

Existing Atlas/package identity mechanisms remain authoritative.

Therefore:

> **Reconciliation preserves established identity architecture rather than manufacturing identifier uniformity.**

---

# Legacy `SYS-*` Treatment

The audit also preserves the previously reconciled distinction:

```text
SYS-*
→ Legacy / Pre-Suite Platform System Index

SREG-*
→ Formal Satoshium Registry identifier family
```

Therefore:

> **SYS ≠ SREG**

The legacy identifier family does not become a current formal Registry family merely because both concern indexed or registered items.

---

# Identifier Audit Rules

The Suite adopts the following identifier rules:

1. Identifiers establish canonical identity.
2. Identifiers establish institutional namespace.
3. Identifiers do not independently establish authority.
4. Identifiers do not encode lifecycle state unless explicitly governed otherwise.
5. Identifiers do not encode publication state.
6. Identifiers do not encode validation.
7. Identifiers do not encode conformance.
8. Identifiers do not encode Evaluation Outcome.
9. Identifiers do not encode version.
10. Identifiers do not independently establish relationship.
11. Matching sequence numbers across institutions do not establish lineage.
12. Identifier year does not replace explicit temporal fields.
13. Sequence numbers do not create hierarchy.
14. Relationships must be explicit and typed.
15. Existing identifier families should be preserved unless architecture requires change.
16. New identifier families should not be invented merely for symmetry.

---

# Audit Result

The canonical identifier families are compatible with the mature Suite architecture.

No identifier family requires redesign.

The primary reconciliation requirement is interpretive discipline:

> **Identifiers must remain identifiers.**

They must not silently carry semantics that belong to:

- authority;
- lifecycle;
- publication;
- validation;
- conformance;
- evaluation;
- versioning;
- provenance;
- or relationships.

---

## Final Disposition

# IDENTIFIER-FAMILY AUDIT — COMPLETE — APPROVED

The Suite identifier families are reconciled as institutional identity mechanisms rather than hidden carriers of authority, status, version, outcome, or relationship semantics.

The governing rule is:

> **IDENTITY IS EXPLICIT. STATUS, AUTHORITY, VERSION, AND RELATIONSHIP MUST REMAIN EXPLICIT TOO.**
