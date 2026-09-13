# Satoshium Beacon — Discovery Metadata

**Path:** `/beacon/discovery-metadata/`  
**Institution:** Satoshium Beacon  
**Supporting Institutional Layer:** Discovery Metadata  
**Canonical Object:** Discovery Signal  
**First Production Example:** `BEAC-2026-0001`  
**Last Updated:** September 13, 2026

---

## Purpose

Discovery Metadata is Beacon-owned structured information used to make discoverable information easier to locate, organize, interpret, filter, trace, and relate across institutional boundaries.

Discovery Metadata supports the canonical Beacon Discovery Signal.

It does not replace the canonical objects that Beacon references.

> **Reference does not transfer authority.**

---

## Production Metadata Model

The production architecture supports metadata and related canonical fields including:

- Beacon Identifier
- Subject
- Primary Signal Type
- Source Reference
- Provenance
- Discovery Character
- Discovery Domain
- Discovery Scope
- Discovery Relevance
- Discovery Basis
- Canonical References
- Relationships
- Observed / Created / Published timestamps
- Lifecycle State
- Publication State
- Version
- Supersession when applicable

Exact machine labels, serialization, enums, and schema dialect remain intentionally unfrozen where not yet institutionally required.

---

## First Production Example

`BEAC-2026-0001` provides Beacon's first real production application of Discovery Metadata.

### Identity

- **Beacon Identifier:** `BEAC-2026-0001`
- **Subject:** Atlas Jurisdiction Record — El Salvador
- **Primary Signal Type:** Certification
- **Lifecycle:** Active
- **Publication:** Published
- **Version:** 1.0

### Source

- **Source Institution:** Satoshium Certifier
- **Source Object:** `SC-CERT-2026-0001`
- **Source Object Type:** Canonical Certification Package
- **Source Version:** 1.1

### Provenance

- **Provenance Type:** Direct
- **Observation Method:** Direct review of published canonical source
- **Observed:** September 13, 2026
- **Observer:** Satoshium Beacon
- **Observed Condition:** Issued · Active · Operational

### Discovery Context

- **Discovery Character:** Institutional
- **Discovery Domain:** Certification
- **Discovery Scope:** Existence and current certification condition
- **Discovery Relevance:** Significant operational Suite object
- **Discovery Basis:** Direct authoritative source observation

These labels describe the governed production concept. They should not be interpreted as frozen machine enums unless later adopted as such.

---

## Canonical References and Relationships

The primary authoritative reference is:

`SC-CERT-2026-0001`

The underlying subject is:

`Atlas Jurisdiction Record — El Salvador`

Related Suite objects include:

- Registry → `SREG-2026-0001`
- Chronicle → `CHR-2026-0001`
- Anchor → `ANCH-2026-0001`

The related objects provide context and relationships.

They do not replace Beacon's direct provenance:

```text
SC-CERT-2026-0001
→ direct Beacon observation
→ BEAC-2026-0001
```

---

## Authority Boundary

Satoshium Beacon owns:

- `BEAC-2026-0001`
- Discovery Metadata
- discovery provenance
- Beacon lifecycle
- publication state
- Beacon-side relationships

Satoshium Certifier remains authoritative for:

- `SC-CERT-2026-0001`
- certification decision
- Certification Class
- certification lifecycle
- certification status

Registry, Chronicle, and Anchor retain authority over their own referenced canonical objects.

---

## Production Significance

The first production operation demonstrates that Discovery Metadata can preserve:

- source identity;
- direct provenance;
- discovery context;
- canonical references;
- related Suite relationships;
- lifecycle and publication state;
- version information;
- authority boundaries.

This moves Discovery Metadata beyond a purely conceptual model while preserving optionality for later machine implementation.

---

## Continuing Development

The following remain available for later development:

- exact machine serialization;
- frozen machine enums;
- machine-readable schema implementation;
- broader source indexing;
- discovery feeds;
- APIs;
- automation;
- federation;
- Navigator workflow interfaces;
- discovery analytics.

No machine representation should be treated as frozen merely because the conceptual production fields have now been exercised.

---

## Governing Principle

**Good metadata makes discovery traceable without obscuring authority.**
