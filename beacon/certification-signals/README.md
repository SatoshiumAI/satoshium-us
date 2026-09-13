# Satoshium Beacon — Certification Signals

**Path:** `/beacon/certification-signals/`  
**Institution:** Satoshium Beacon  
**Canonical Object:** Discovery Signal  
**Primary Signal Type:** Certification  
**Production Example:** `BEAC-2026-0001`  
**Last Updated:** September 13, 2026

---

## Purpose

Certification discovery allows Beacon to make certification-related information findable while preserving the authority of Satoshium Certifier.

Beacon does not certify.

Beacon creates and publishes Beacon-owned Discovery Signals that may reference authoritative Certifier objects and observed certification conditions.

> **Reference does not transfer authority.**

---

## Terminology Reconciliation

The governed Beacon primary Signal Type is:

**Certification**

Terms such as **Certified**, **Active**, **Expired**, **Revoked**, **Updated**, and **Pending** describe certification-related conditions or states that Beacon may observe from an authoritative source. They are not separate replacements for Beacon's governed primary Signal Type vocabulary.

This distinction preserves the Phase II rule:

```text
Signal Type ≠ Source Object Type ≠ Source Status
```

---

## First Production Certification Signal

Beacon's first real production certification Discovery Signal is:

**`BEAC-2026-0001`**

### Identity

- **Title:** Active Operational Certification — Atlas Jurisdiction Record — El Salvador
- **Primary Signal Type:** Certification
- **Lifecycle:** Active
- **Publication:** Published
- **Version:** 1.0
- **Published:** September 13, 2026

### Primary Source

- **Institution:** Satoshium Certifier
- **Object:** `SC-CERT-2026-0001`
- **Object Type:** Canonical Certification Package
- **Source Version:** 1.1
- **Observed Condition:** Issued · Active · Operational

### Discovery

Beacon identified the discoverable condition that an active Operational certification exists for the Atlas Jurisdiction Record — El Salvador, represented by `SC-CERT-2026-0001`.

Public Beacon record:

https://satoshium.us/beacon/records/BEAC-2026-0001/

---

## Production Relationship

```text
SC-CERT-2026-0001
Satoshium Certifier
        ↓
direct Beacon observation
        ↓
Certification discovery
        ↓
BEAC-2026-0001
Satoshium Beacon
```

Certifier owns the certification.

Beacon owns the Discovery Signal.

---

## Discovery Signal Structure

A certification Discovery Signal may preserve:

- Beacon Identifier
- Subject
- Primary Signal Type
- Source Reference
- Provenance
- Discovery Metadata
- Canonical References
- Timestamps
- Version
- Lifecycle State
- Publication State
- Relationships

Conditional fields depend on the discovery and its governed relationships.

---

## Authority Boundary

Satoshium Certifier remains authoritative for:

- Certification Packages;
- certification determinations;
- Certification Classes;
- certification lifecycle;
- certification status;
- Certifier evidence review and certification records.

Satoshium Beacon owns:

- its Discovery Signal;
- `BEAC` identifier;
- Discovery Metadata;
- discovery provenance;
- Beacon lifecycle;
- publication state;
- Beacon-side relationships.

A Beacon Discovery Signal may reflect an authoritative certification condition.

It does not independently create, modify, revoke, renew, or adjudicate that condition.

---

## Related Production Objects

`BEAC-2026-0001` also references related Suite objects for context:

- `SREG-2026-0001` — Registry
- `CHR-2026-0001` — Chronicle
- `ANCH-2026-0001` — Anchor

Those objects remain governed by their respective institutions.

---

## Governing Principle

**Beacon makes certification discoverable. Certifier remains authoritative for certification.**
