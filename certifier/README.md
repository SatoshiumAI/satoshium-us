# Satoshium Certifier

**Path:** `/certifier/`  
**Institution:** Satoshium Certifier  
**Institutional Role:** Operational Certification  
**Canonical Operational Object:** Certification Package  
**Status:** Operational  
**Updated for Attestor integration:** September 2026

---

## Overview

Satoshium Certifier is the operational certification implementation of the Satoshium Suite.

Certifier applies Suite Standards and Suite Methodology to evidence-supported review, reaches certification determinations, and preserves those determinations through canonical Certification Packages and generated certification artifacts.

The inaugural operational Certification Package is:

**`SC-CERT-2026-0001` — Atlas Jurisdiction Record — El Salvador**

---

## Canonical Authority

Certifier owns:

- the certification action;
- the Certification Package;
- the certification determination;
- the Certification Class;
- certification lifecycle and status;
- generated Certifier certification artifacts.

Referenced subject systems and downstream Suite institutions retain authority over their own objects.

> **Reference does not transfer authority.**

---

## Production Suite Lineage

`SC-CERT-2026-0001` now participates in a multi-institution production lineage while remaining the authoritative Certifier object for the certification.

### Registry

`SREG-2026-0001` catalogs the certification.

Registry owns the Registry Entry. Certifier retains certification authority.

### Chronicle

`CHR-2026-0001` preserves the qualifying historical certification occurrence.

Chronicle owns the historical-preservation representation. Certifier retains certification authority.

### Anchor

`ANCH-2026-0001` preserves integrity context for the defined SCRD JSON representation associated with `SC-CERT-2026-0001`.

Anchor owns the Integrity Reference. Certifier owns the source certification record.

### Beacon

`BEAC-2026-0001` is Satoshium Beacon's first published production Discovery Signal.

Beacon directly used the canonical Certification Package `SC-CERT-2026-0001` as its primary authoritative source to identify the existence and active Operational certification status of the Atlas Jurisdiction Record — El Salvador.

Public Beacon record:

https://satoshium.us/beacon/records/BEAC-2026-0001/

Beacon owns:

- `BEAC-2026-0001`;
- its Discovery Metadata;
- discovery provenance;
- Beacon lifecycle and publication state;
- Beacon-side relationships.

Certifier continues to own:

- `SC-CERT-2026-0001`;
- the certification determination;
- Certification Class;
- certification lifecycle;
- certification status.

Beacon's discovery representation does not re-certify or replace the Certifier object.

---

## Production Relationship

```text
Atlas Jurisdiction Record — El Salvador
        ↓ certification subject

SC-CERT-2026-0001
Satoshium Certifier
        ↓
        ├── SREG-2026-0001  → Registry
        ├── CHR-2026-0001   → Chronicle
        ├── ANCH-2026-0001  → Anchor integrity context
        ├── BEAC-2026-0001  → Beacon discovery
        ├── ATT-2026-0001   → Attestor Attestation
        └── TRST-2026-0001  → Attestor Trust Statement
```

These relationships connect institution-owned objects without merging their identities or authority.

---

## Certifier Workflow

```text
Certification Subject
↓
Evidence
↓
Certification Package
↓
Evaluation & Decision
↓
SCPR · SCR · SCRD HTML / JSON
↓
Registry · Chronicle · Anchor · Beacon · Attestor · Navigator
```

Standards define expectations. Methodology defines process. Certifier executes certification. Other Suite institutions may catalog, preserve, protect integrity, discover, attest, or orchestrate without assuming Certifier authority.

---

## Beacon Integration

The publication of `BEAC-2026-0001` provides the first real production evidence for Certifier-to-Beacon interoperability.

The relationship is:

```text
SC-CERT-2026-0001
        ↓
primary authoritative source for discovery
        ↓
BEAC-2026-0001
```

This demonstrates a core Satoshium Suite principle:

**Discovery can make a certification easier to find without becoming certification authority.**

---

## Attestor Integration

The certification context represented by `SC-CERT-2026-0001` later participated in Satoshium Attestor's first controlled production operation.

The governed production path was:

```text
SC-CERT-2026-0001
+ eligible governed Suite-source inputs
        ↓
ATT-2026-0001
        ↓
Rule-Constrained Evaluation
        ↓
supported
        ↓
TRST-2026-0001
```

`ATT-2026-0001` is Attestor's first canonical production Attestation.

`TRST-2026-0001` is Attestor's first canonical production Trust Statement and is `derived-from` `ATT-2026-0001`.

Both are:

```text
Active · Published · V1.0
```

Attestor owns its Attestation, Rule-Constrained Evaluation, Evaluation Outcome, Trust Statement, lifecycle, publication state, and Attestor-controlled relationships.

Certifier continues to own `SC-CERT-2026-0001` and the certification decision, Certification Class, certification lifecycle, and certification status.

The Attestor conclusion is bounded. It does not independently re-certify the Certifier decision, establish the substantive truth of the underlying Atlas jurisdiction intelligence, extend Anchor integrity beyond its defined representation, or establish generalized trustworthiness.

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

**Certifier certifies. Registry catalogs. Chronicle preserves. Anchor preserves integrity references. Beacon discovers. Attestor evaluates governed attestations and produces bounded Trust Statements. Navigator defines and orchestrates workflows. Each institution retains authority over its own canonical object.**

**Reference does not transfer authority.**
