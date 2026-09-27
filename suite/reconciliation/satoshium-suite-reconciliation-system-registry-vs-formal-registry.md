# Satoshium Suite Reconciliation — System Registry vs Formal Satoshium Registry

**Date:** September 25, 2026  
**Phase:** Phase I — Baseline & Institutional Architecture  
**Decision Class:** RECONCILE  
**Status:** COMPLETE — APPROVED  
**Deferred Issue:** DI-001 — CLOSED

---

## Purpose

This record resolves the previously deferred architectural question concerning the relationship between the legacy `SYS-*` System Registry and the formal Satoshium Registry established within the completed Satoshium Suite.

The purpose of this reconciliation is to determine whether the two structures represent:

- competing registries;
- layers of one current registry;
- legacy and current terminology for the same object;
- or distinct architectural systems with different roles.

The reconciliation preserves historical accuracy while ensuring that the current Suite architecture uses one unambiguous formal Registry model.

---

## Reconciled Determination

The `SYS-*` System Registry and the formal Satoshium Registry are **distinct structures**.

Their reconciled positions are:

```text
SYS-*
→ Legacy / Pre-Suite Platform System Index

SREG-*
→ Formal Satoshium Registry canonical object family
→ Satoshium Registry Entry
```

Therefore:

> **SYS ≠ SREG**

The legacy `SYS-*` structure is preserved as historical platform identity and indexing.

The formal Satoshium Registry is the current Suite institution responsible for:

> **Canonical Registration / Public Catalog**

Its canonical object is the:

> **Satoshium Registry Entry (SREG)**

---

## Legacy System Registry

The legacy System Registry predates the mature institutional Suite architecture.

Its `SYS-*` identifiers represent the earlier platform-level indexing model used to identify or organize Satoshium systems and components.

This historical role remains valid.

The reconciliation does **not** require:

- deletion of legacy `SYS-*` records;
- renumbering of legacy systems;
- conversion of `SYS-*` identities into `SREG-*`;
- rewriting historical documentation that accurately used the System Registry;
- or retroactive migration solely for naming consistency.

The governing treatment is:

> **Preserve legacy identity; do not preserve legacy authority where the mature Suite has established a formal institutional authority model.**

---

## Formal Satoshium Registry

The formal Registry is one of the eight operational institutions of the Satoshium Suite.

Its institutional role is:

> **Canonical Registration / Public Catalog**

Its canonical operational object is:

> **Satoshium Registry Entry**

with identifier family:

```text
SREG-YYYY-NNNN
```

The Registry may register qualifying source objects while preserving the source institution's ownership and authority.

The formal layered model is:

```text
Registry
    ↓
Satoshium Registry Entry (SREG)
    ↓
Registry Record Type
    ↓
Authoritative Source Record
```

The final layer describes the source object being registered.

It does not transfer ownership of that source object to Registry.

---

## Authority Boundary

The reconciliation preserves the distinction between registration authority and source authority.

For example:

```text
Certifier
→ owns Certification Package

Registry
→ owns SREG that registers/references the Certification Package
```

Likewise, other source institutions retain authority over their own canonical objects even where Registry catalogs them.

Therefore:

> **REGISTRATION DOES NOT TRANSFER SOURCE AUTHORITY.**

And:

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

A Registry Entry may identify, classify, and publicly catalog a source object without becoming authoritative for that source object's substantive meaning.

---

## Relationship Between SYS and SREG

The relationship is historical and architectural, not migratory.

The correct interpretation is:

```text
SYS-*
→ legacy platform/system index

SREG-*
→ mature institutional registration architecture
```

The two may coexist.

They do not form:

```text
SYS-* → SREG-*
```

as a mandatory migration chain.

Nor should they be treated as:

```text
SYS-* = SREG-*
```

with different naming.

They are distinct artifacts from different architectural periods.

---

## No Forced Migration

No forced migration from `SYS-*` to `SREG-*` is required.

Reasons:

1. `SYS-*` records preserve legitimate historical identity.
2. SREGs represent a different institutional function.
3. Reassigning identifiers would blur historical provenance.
4. The mature Registry can reference legacy systems where useful without absorbing or replacing their original identity.
5. Reconciliation should document existing architecture rather than fabricate continuity where none is required.

Therefore:

> **Legacy records remain legacy records. Formal Registry objects remain formal Registry objects.**

---

## Current-State Documentation Rule

Current Suite documentation should not describe `SYS-*` as though it were the current formal Satoshium Registry.

Current-state descriptions should use:

```text
Satoshium Registry
→ Canonical Registration / Public Catalog

Satoshium Registry Entry
→ canonical Registry object

SREG-YYYY-NNNN
→ canonical Registry identifier family
```

Historical documentation may retain `SYS-*` terminology where historically accurate.

The rule is:

> **Historical identity may be preserved; current institutional authority must be described using the mature architecture.**

---

## Legacy Documentation Treatment

When reviewing older pages:

### Preserve

Preserve references to:

- System Registry;
- `SYS-*`;
- legacy system identifiers;
- platform component indexing;

where the page is historical or clearly describing the earlier platform architecture.

### Correct or Clarify

Correct or clarify current-state wording where it implies:

- `SYS-*` is the formal Registry identifier family;
- the legacy System Registry owns current canonical registration;
- `SYS-*` and `SREG-*` are interchangeable;
- formal Registry authority originates from the old System Registry.

---

## Reconciled Registry Model

The current Registry model is:

```text
Formal Satoshium Suite
        ↓
Registry
        ↓
Canonical Registration / Public Catalog
        ↓
Satoshium Registry Entry
        ↓
SREG-YYYY-NNNN
```

Source relationships are preserved separately:

```text
Source Institution
        ↓ owns
Source Canonical Object
        ↓ referenced by
SREG
```

This ensures:

```text
Registration ≠ Source Ownership
Registration ≠ Certification
Registration ≠ Historical Preservation
Registration ≠ Discovery
Registration ≠ Evaluation
```

---

## Governing Principles

The following principles govern the reconciled treatment:

> **SYS ≠ SREG**

> **Legacy identity ≠ current institutional authority**

> **Registration does not transfer source authority**

> **Reference does not transfer authority**

> **Connection ≠ Identity**

> **Historical architecture may be preserved; current architecture must be current**

---

## Decision

The architectural question is resolved as follows:

```text
SYS-*
= Legacy / Pre-Suite Platform System Index

SREG-*
= Formal Satoshium Registry canonical identifier family
```

They are:

- distinct;
- non-competing;
- historically compatible;
- allowed to coexist;
- not subject to mandatory migration or merger.

The formal Registry remains the current canonical registration institution.

---

## Deferred Issue Disposition

```text
DI-001
System Registry (SYS-*) vs Formal Satoshium Registry
→ CLOSED
```

No further architectural decision is required unless future work intentionally redesigns the relationship between the legacy system index and formal Registry.

---

## Final Disposition

# SYSTEM REGISTRY VS FORMAL SATOSHIUM REGISTRY — COMPLETE — APPROVED

The mature Suite preserves the legacy `SYS-*` System Registry as a historical platform index while recognizing the formal Satoshium Registry and its `SREG-*` objects as the current canonical registration architecture.

No merger, forced migration, identifier replacement, or authority transfer is required.
