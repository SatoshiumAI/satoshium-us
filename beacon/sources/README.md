# Satoshium Beacon — Sources

**Path:** `/beacon/sources/`  
**Institution:** Satoshium Beacon  
**Role:** Discovery & Signals  
**First Production Source:** `SC-CERT-2026-0001`  
**First Production Discovery Signal:** `BEAC-2026-0001`  
**Last Updated:** September 13, 2026

---

## Purpose

Sources preserve the origin, authority, context, attribution, and provenance behind information surfaced through Beacon.

Beacon does not replace its sources.

It preserves the path back to them.

---

## Source Classes

Beacon may discover information from:

- Satoshium Atlas
- Satoshium Certifier
- Satoshium Registry
- Satoshium Chronicle
- Satoshium Anchor
- Satoshium Attestor
- external sources

External discovery does not make an external source a Suite institution or a Suite-authoritative object.

---

## First Production Source

Beacon's first production-proven primary source is:

**`SC-CERT-2026-0001`**

Source details:

- **Source Institution:** Satoshium Certifier
- **Source Object:** `SC-CERT-2026-0001`
- **Source Object Type:** Canonical Certification Package
- **Source Version:** 1.1
- **Certification Subject:** Atlas Jurisdiction Record — El Salvador
- **Observed Condition:** Issued · Active · Operational
- **Observation Method:** Direct review of the published canonical source
- **Provenance Type:** Direct

The resulting Beacon object is:

**`BEAC-2026-0001`**

```text
SC-CERT-2026-0001
→ direct Beacon observation
→ BEAC-2026-0001
```

---

## Related Context

The first production Discovery Signal also preserves relationships to:

- `SREG-2026-0001`
- `CHR-2026-0001`
- `ANCH-2026-0001`

These objects provide related Suite context.

They are not intermediate sources in Beacon's direct provenance for `BEAC-2026-0001`.

---

## Source vs. Provenance

A source identifies **what Beacon observed or referenced**.

Provenance preserves **how Beacon encountered, observed, and preserved that source in the discovery process**.

These concepts are related but not interchangeable.

---

## Source Authority Boundary

Beacon owns:

- its Discovery Signals
- Discovery Metadata
- Beacon-side provenance
- Beacon-side relationships
- Beacon lifecycle and publication state

The source institution retains authority for its source object.

For `BEAC-2026-0001`:

- **Certifier** retains certification authority.
- **Atlas** retains authority over the underlying jurisdiction intelligence.
- **Beacon** owns only its Discovery Signal and Beacon-side institutional representation.

> **Reference does not transfer authority.**

---

## Source Principles

Beacon source handling should preserve:

- Attribution
- Provenance
- Transparency
- Traceability
- Stable References
- Institutional Authority
- Accessibility
- Neutrality

---

## Governing Principle

**Discovery should illuminate origins, not obscure them.**
