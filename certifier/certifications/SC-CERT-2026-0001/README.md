# SC-CERT-2026-0001 — Certification Package

**Path:** `/certifier/certifications/SC-CERT-2026-0001/`  
**Institution:** Satoshium Certifier  
**Object Type:** Canonical Certification Package  
**Certification Subject:** Atlas Jurisdiction Record — El Salvador  
**Certification Class:** Operational  
**Certification Status:** Issued · Active  
**Package Version:** 1.1  
**Original Certification Date:** July 5, 2026  
**Updated for Attestor downstream reference:** September 2026

---

## Canonical Role

`SC-CERT-2026-0001` is the canonical Certification Package for the inaugural operational certification of the Satoshium Atlas Jurisdiction Record — El Salvador.

The Package preserves the Certification Subject, certification boundary, governing Suite Standards, applied Suite Methodology, Evidence Inventory, evaluation, certification decision, Certification Class, generated artifacts, lifecycle state, and downstream Suite references.

Satoshium Certifier remains authoritative for the certification action, determination, class, lifecycle, and status.

---

## Certification Subject

- **Subject:** Atlas Jurisdiction Record — El Salvador
- **Subject System:** Satoshium Atlas
- **Subject Type:** Jurisdiction Intelligence Engine Record
- **Certification Date:** July 5, 2026
- **Subject Authority:** Satoshium Atlas

Atlas retains authority over the underlying jurisdiction intelligence.

---

## Generated Artifacts

The canonical Certification Package generated:

- SCPR — Certification Process Report
- SCR — Certification Receipt
- SCRD HTML — Human-readable Certified Record
- SCRD JSON — Machine-readable Certified Record

The SCRD JSON representation is the source artifact referenced by `ANCH-2026-0001`.

---

## Published Downstream Suite References

`SC-CERT-2026-0001` now has six published downstream Attestor/Suite references:

| Institution | Object | Role |
|---|---|---|
| Satoshium Registry | `SREG-2026-0001` | Registry-owned catalog and registration record corresponding to the Certification Package |
| Satoshium Chronicle | `CHR-2026-0001` | Chronicle-owned historical preservation of the July 5, 2026 certification-created occurrence |
| Satoshium Anchor | `ANCH-2026-0001` | Anchor-owned Integrity Reference for the defined SCRD JSON representation |
| Satoshium Beacon | `BEAC-2026-0001` | Beacon-owned Discovery Signal identifying the existence and current active Operational certification |
| Satoshium Attestor | `ATT-2026-0001` | Attestor-owned canonical Attestation referencing this Certification Package within the first controlled production evaluation |
| Satoshium Attestor | `TRST-2026-0001` | Attestor-owned canonical Trust Statement derived from `ATT-2026-0001` after Rule-Constrained Evaluation |

---

## Beacon Production Relationship

On September 13, 2026, Satoshium Beacon directly observed this canonical Certification Package and used it as the primary authoritative source for its first production Discovery Signal:

**`BEAC-2026-0001` — Active Operational Certification — Atlas Jurisdiction Record — El Salvador**

Public Beacon record:

https://satoshium.us/beacon/records/BEAC-2026-0001/

The relationship is:

```text
SC-CERT-2026-0001
Satoshium Certifier
        ↓
primary authoritative source for discovery
        ↓
BEAC-2026-0001
Satoshium Beacon
```

Beacon owns `BEAC-2026-0001`, its discovery metadata, provenance, lifecycle, publication state, and Beacon-side relationships.

Certifier retains authority for `SC-CERT-2026-0001`, including its certification decision, Certification Class, lifecycle, and status.

> **Reference does not transfer authority.**

---

## Attestor Production Relationship

Satoshium Attestor used this canonical Certification Package as a governed Suite-source input in its first controlled production operation.

The bounded matter concerned the canonical identity, attributable Certifier origin, relevant certification state, and traceable Suite relationships of `SC-CERT-2026-0001`.

```text
SC-CERT-2026-0001
        ↓ governed reference / eligible input
ATT-2026-0001
        ↓ Rule-Constrained Evaluation
     supported
        ↓
TRST-2026-0001
```

Production state:

- `ATT-2026-0001` → **Active · Published · V1.0**
- `TRST-2026-0001` → **Active · Published · V1.0**
- Evaluation Outcome → `supported`

`TRST-2026-0001` is `derived-from` `ATT-2026-0001`.

Attestor's conclusion is bounded. It does not independently recertify the Certifier decision, establish the substantive truth of the underlying Atlas jurisdiction intelligence, extend Anchor integrity beyond its defined SCRD representation, prove unchanged state beyond the evidence reviewed, or make a generalized determination of trustworthiness.

Certifier remains authoritative for this Certification Package, its certification decision, Certification Class, lifecycle, and status.

> **Reference does not transfer authority.**

## Production Lineage

```text
Atlas Jurisdiction Record — El Salvador
        ↓
SC-CERT-2026-0001
        │
        ├── SREG-2026-0001
        ├── CHR-2026-0001
        ├── ANCH-2026-0001
        ├── BEAC-2026-0001
        └── Attestor governed use
              ├── ATT-2026-0001
              └── TRST-2026-0001
```

Each object remains owned and governed by its respective Satoshium Suite institution.

---

## Canonical Record Principle

This Certification Package remains Certifier's canonical operational record for `SC-CERT-2026-0001`.

Every generated Certifier artifact and downstream Suite reference must remain traceable to this Package where the relationship depends upon the certification.

A discrepancy between a generated Certifier representation and the finalized Package should be resolved by correcting the affected representation to match the Package.

---

## Related Objects

- `SREG-2026-0001` — Satoshium Registry  
  https://satoshium.us/registry/registered-items/SREG-2026-0001/registry-entry.html

- `CHR-2026-0001` — Satoshium Chronicle  
  https://satoshium.us/chronicle/entries/CHR-2026-0001/

- `ANCH-2026-0001` — Satoshium Anchor  
  https://satoshium.us/anchor/anchored-items/ANCH-2026-0001/

- `BEAC-2026-0001` — Satoshium Beacon  
  https://satoshium.us/beacon/records/BEAC-2026-0001/

- `ATT-2026-0001` — Satoshium Attestor  
  https://satoshium.us/attestor/attestations/ATT-2026-0001/

- `TRST-2026-0001` — Satoshium Attestor  
  https://satoshium.us/attestor/trust-statements/TRST-2026-0001/

---

## Governing Principle

**The Certification Package remains the certification authority record. Downstream references may make it cataloged, historically preserved, integrity-referenced, discoverable, and available to bounded Attestor evaluation without transferring Certifier authority.**
