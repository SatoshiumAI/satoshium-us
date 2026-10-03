# Satoshium Beacon Records

**Path:** `/beacon/records/`  
**Institution:** Satoshium Beacon  
**Purpose:** Human-facing register of published canonical Discovery Signals  
**Status:** Active Production Use · Beacon Operational  
**Last Updated:** October 2, 2026

---

## Purpose

Beacon Records is the public index for Beacon Discovery Signals whose publication state permits public representation.

The Records page exists to make published Beacon objects discoverable while preserving the distinction between:

- the canonical Beacon Discovery Signal;
- the human-facing index listing;
- the individual public Beacon record; and
- every referenced source or related institutional object.

A Record listing is an index representation. It is **not** a second canonical object.

> **Reference does not transfer authority.**

---

## Inclusion Rule

A Beacon Discovery Signal is eligible for public Records inclusion when:

```text
Canonical Discovery Signal exists
+ Publication State = Published
+ Public representation remains permitted
= Eligible for Beacon Records
```

Unpublished signals remain outside the public Records index by default.

---

## Production Records

### BEAC-2026-0001

**Title:** Active Operational Certification — Atlas Jurisdiction Record — El Salvador  
**Signal Type:** Certification  
**Lifecycle State:** Active  
**Publication State:** Published  
**Current Version:** 1.0  
**Source Institution:** Satoshium Certifier  
**Source Object:** `SC-CERT-2026-0001`  
**Published:** September 13, 2026  
**Record:** https://satoshium.us/beacon/records/BEAC-2026-0001/

Discovery statement:

> Satoshium Beacon identified an active Operational certification for the Atlas Jurisdiction Record — El Salvador, represented by Satoshium Certifier object `SC-CERT-2026-0001`.

`BEAC-2026-0001` is Beacon's first published production Discovery Signal and the first object listed in Beacon Records.

---

## Records-Level Fields

The first production listing establishes the initial human-facing Records field set:

- BEAC Identifier
- Subject / Title
- Signal Type
- Lifecycle State
- Publication State
- Current Version
- Source / Source Institution
- Published At
- Record Link

These fields support discovery and navigation without reproducing the entire canonical Discovery Signal.

Future presentation refinements may occur without changing the canonical Beacon object or transferring authority.

---

## Authority Boundary

Beacon Records indexes Beacon-owned Discovery Signals.

It does not assume authority over source or related objects.

For `BEAC-2026-0001`:

- **Beacon** owns the Discovery Signal and Beacon-side metadata, provenance, lifecycle, publication state, and relationships.
- **Certifier** owns `SC-CERT-2026-0001` and the certification determination, class, lifecycle, and status.
- **Atlas** owns the underlying Atlas Jurisdiction Record — El Salvador and its jurisdiction intelligence.
- **Registry** owns `SREG-2026-0001`.
- **Chronicle** owns `CHR-2026-0001`.
- **Anchor** owns `ANCH-2026-0001`.

Beacon Records inclusion establishes public discoverability within Beacon. It does not independently establish truth, certification, registration standing, historical significance, integrity verification, or trust.

---

## Current Production State

```text
Beacon Status → Operational
Phase I → Complete
Phase II → Complete
First Controlled Production Operation → Complete
First Production Discovery Signal → BEAC-2026-0001
Lifecycle → Active
Publication → Published
Production Records → 1 published Discovery Signal
Production Evidence Preservation → Complete
Post-Operation Review → Complete
Production Proof → Established
Operational → Yes · September 2026
```

Beacon was not treated as Operational solely because its first production signal was published. Operational status was established only after production evidence was preserved and the post-operation review confirmed that Beacon's architecture functioned coherently under governed use.

---

## Directory Structure

```text
/beacon/records/
├── index.html
├── README.md
└── BEAC-2026-0001/
    ├── index.html
    └── README.md
```

Additional published Discovery Signals should be added as sibling BEAC record directories and listed on `/beacon/records/` according to Beacon publication governance.

---

## Governing Principle

**Beacon Records makes published Discovery Signals findable without becoming another canonical authority.**
