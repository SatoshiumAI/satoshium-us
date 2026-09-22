# Satoshium Certifier — Certified Items

**Path:** `/certifier/certified-items/`  
**Institution:** Satoshium Certifier  
**Purpose:** Public directory of certification subjects and their canonical Certification Packages  
**Updated for Attestor integration:** September 2026

---

## Purpose

Certified Items catalogs certification subjects reviewed through Satoshium Certifier under Suite Standards and Suite Methodology.

Each completed certified item should resolve to its canonical Certification Package and may identify generated Certifier artifacts and downstream Suite references that make the certification reviewable, verifiable, discoverable, and interoperable.

This directory does not create certification authority independently of the canonical Certification Package.

---

## Inaugural Certified Item

### Atlas Jurisdiction Record — El Salvador

**Certification Package:** `SC-CERT-2026-0001`  
**Certification Class:** Operational  
**Certification Status:** Issued · Active  
**Certification Authority:** Satoshium Certifier

Canonical Certification Package:

https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/

The Atlas Jurisdiction Record — El Salvador is Certifier's inaugural operational certification subject.

---

## Generated Certifier Artifacts

The Certification Package generated the supporting certification record set, including:

- SCPR — Certification Process Report
- SCR — Certified Record
- SCRD HTML
- SCRD JSON
- certification receipt and supporting public representations

These artifacts remain subordinate to the canonical Certification Package.

---

## Downstream Suite References

The inaugural certification now participates in the following production relationships:

```text
SC-CERT-2026-0001
        │
        ├── SREG-2026-0001  → Satoshium Registry
        ├── CHR-2026-0001   → Satoshium Chronicle
        ├── ANCH-2026-0001  → Satoshium Anchor
        ├── BEAC-2026-0001  → Satoshium Beacon
        ├── ATT-2026-0001   → Satoshium Attestor
        └── TRST-2026-0001  → Satoshium Attestor
```

Each downstream institution owns its own canonical object.

### Registry

`SREG-2026-0001` catalogs the certification.

### Chronicle

`CHR-2026-0001` preserves the qualifying historical certification occurrence.

### Anchor

`ANCH-2026-0001` preserves integrity context for the defined machine-readable certified-record representation.

### Beacon

`BEAC-2026-0001` is Beacon's first published production Discovery Signal.

Beacon directly used `SC-CERT-2026-0001` as its primary authoritative source to identify the existence and current active Operational certification of the Atlas Jurisdiction Record — El Salvador.

Public Beacon record:

https://satoshium.us/beacon/records/BEAC-2026-0001/

### Attestor

`ATT-2026-0001` is Attestor's first canonical production Attestation and `TRST-2026-0001` is its first canonical production Trust Statement.

The certification context participated in Attestor's first controlled production operation as governed Suite-source evidence:

```text
SC-CERT-2026-0001
        ↓
eligible governed input
        ↓
ATT-2026-0001
        ↓
Rule-Constrained Evaluation
        ↓
supported
        ↓
TRST-2026-0001
```

`TRST-2026-0001` is `derived-from` `ATT-2026-0001`. Both Attestor objects preserve governed references to the relevant Suite-source objects.

Attestor's conclusion is bounded. It does not independently re-certify the Certifier decision, establish the substantive truth of the underlying Atlas jurisdiction intelligence, extend Anchor integrity beyond its defined representation, or establish generalized trustworthiness.

---

## Authority Boundary

Satoshium Certifier remains authoritative for:

- `SC-CERT-2026-0001`;
- the certification decision;
- Certification Class;
- certification lifecycle;
- certification status;
- generated Certifier certification artifacts.

Satoshium Registry, Chronicle, Anchor, Beacon, and Attestor remain authoritative for their own respective objects and institutional representations.

Beacon discovery does not re-certify the subject.

Anchor integrity preservation does not become certification.

Registry cataloging does not become certification.

Chronicle historical preservation does not become certification.

Attestor evaluation and a bounded Trust Statement do not become certification.

> **Reference does not transfer authority.**

---

## Certified Item Flow

```text
Certification Subject
↓
Certification Package
↓
SCPR · SCR · SCRD HTML / JSON
↓
Registry · Chronicle · Anchor · Beacon · Attestor
↓
SREG-2026-0001 · CHR-2026-0001 · ANCH-2026-0001 · BEAC-2026-0001 · ATT-2026-0001 · TRST-2026-0001
```

---

## Related Production Objects

- Certifier — `SC-CERT-2026-0001`  
  https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/

- Registry — `SREG-2026-0001`  
  https://satoshium.us/registry/registered-items/SREG-2026-0001/registry-entry.html

- Chronicle — `CHR-2026-0001`  
  https://satoshium.us/chronicle/entries/CHR-2026-0001/

- Anchor — `ANCH-2026-0001`  
  https://satoshium.us/anchor/anchored-items/ANCH-2026-0001/

- Beacon — `BEAC-2026-0001`  
  https://satoshium.us/beacon/records/BEAC-2026-0001/

- Attestor Attestation — `ATT-2026-0001`  
  https://satoshium.us/attestor/attestations/ATT-2026-0001/

- Attestor Trust Statement — `TRST-2026-0001`  
  https://satoshium.us/attestor/trust-statements/TRST-2026-0001/

---

## Governing Principle

**Certified Items makes certification outcomes navigable while the canonical Certification Package remains the Certifier authority.**
