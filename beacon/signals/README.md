# Satoshium Beacon — Signals

**Path:** `/beacon/signals/`  
**Institution:** Satoshium Beacon  
**Canonical Object:** Discovery Signal  
**First Production Signal:** `BEAC-2026-0001`  
**Last Updated:** September 13, 2026

---

## Purpose

Discovery Signals are Beacon-owned canonical objects used to preserve discoveries that are relevant enough to become governed institutional records.

Beacon owns the Discovery Signal.

The referenced source or Suite institution retains authority over its own object.

> **Reference does not transfer authority.**

---

## Governed Signal Types

Beacon's initial governed Signal Type vocabulary is:

- Information
- Jurisdiction
- Certification
- Registry
- Historical
- Integrity
- Trust
- Relationship

One primary Signal Type is preferred for a Discovery Signal.

Exact frozen machine enums remain subject to later machine-serialization decisions.

---

## Critical Classification Rule

```text
Signal Type ≠ Source Object Type ≠ Source Status
```

For example, the first production signal has:

- **Signal Type:** Certification
- **Source Object Type:** Canonical Certification Package
- **Observed Source Condition:** Issued · Active · Operational

These concepts must not be collapsed into one field.

---

## Canonical Lifecycle

Pre-object identification occurs before a canonical Discovery Signal exists.

At Creation:

- the canonical Discovery Signal comes into existence;
- the permanent BEAC identifier is assigned;
- the object enters Draft;
- publication begins as Unpublished.

Canonical lifecycle:

```text
Draft
→ Active
→ Superseded / Resolved / Withdrawn
```

Review and validation are processes, not canonical lifecycle states.

---

## Publication State

Publication is governed separately from lifecycle:

```text
Unpublished / Published
```

A signal may therefore be:

```text
Active · Unpublished
```

before a publication decision transitions it to:

```text
Active · Published
```

---

## First Production Signal

**`BEAC-2026-0001`**

Title:

**Active Operational Certification — Atlas Jurisdiction Record — El Salvador**

Production state:

- **Signal Type:** Certification
- **Primary Source:** `SC-CERT-2026-0001`
- **Lifecycle:** Active
- **Publication:** Published
- **Version:** 1.0
- **Published:** September 13, 2026

This is the first production exercise of the **Certification** Signal Type.

---

## Authority Boundary

Certifier retains authority for:

- the certification decision
- Certification Class
- certification lifecycle
- certification status
- `SC-CERT-2026-0001`

Beacon owns:

- `BEAC-2026-0001`
- the Discovery Signal
- Discovery Metadata
- Beacon provenance
- Beacon lifecycle
- publication state
- Beacon-side relationships

---

## Relationship to Discovery

```text
Workflow / Query
→ Discovery
→ Discovery Signal / Metadata
→ Referenced Source or Canonical Object
```

Not every observation becomes a canonical Discovery Signal.

Creation is the institutional event that transforms a sufficiently relevant constructed discovery into a canonical Beacon object.

---

## Governing Principle

**Beacon discovers. Beacon signals. Authority remains with the source.**
