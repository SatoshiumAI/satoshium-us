# Satoshium Certifier — Interoperability

**Path:** `/certifier/interoperability/`  
**Institution:** Satoshium Certifier  
**Canonical Page:** `index.html`  
**Status:** Operationally Reconciled  
**Updated:** September 2026

---

## Purpose

Certifier Interoperability defines how Satoshium Certifier connects certification activity to the broader Satoshium Suite while preserving clear institutional responsibility between systems.

Certifier applies Suite Standards and Suite Methodology to produce the canonical Certification Package and generated certification artifacts. Other Suite institutions may independently catalog, preserve, integrity-reference, discover, evaluate, attest, or use those records in governed workflows.

Interoperability connects institution-owned objects.

It does not merge their authority.

> **Reference does not transfer authority.**

---

## Operational Certification Flow

The inaugural production certification demonstrates the following cross-Suite path:

```text
Certification Subject
        ↓
Certification Package
        ↓
SCPR · SCR · SCRD HTML / JSON
        ↓
SREG · CHR · ANCH · BEAC · ATT · TRST
        ↓
Registry · Chronicle · Anchor · Beacon · Attestor
```

Navigator provides workflow definition and orchestration around Suite records without changing institutional ownership.

---

## First Production Interoperability Set

The current production-proven object set includes:

```text
Certifier  → SC-CERT-2026-0001
Registry   → SREG-2026-0001
Chronicle  → CHR-2026-0001
Anchor     → ANCH-2026-0001
Beacon     → BEAC-2026-0001
Attestor   → ATT-2026-0001
Attestor   → TRST-2026-0001
```

These are related institution-owned canonical objects.

They are not Versions of one another and do not share authority.

`TRST-2026-0001` is `derived-from` `ATT-2026-0001`.

Both Attestor objects preserve governed references to the relevant Suite-source objects.

---

## Certifier

Satoshium Certifier remains authoritative for:

```text
SC-CERT-2026-0001
certification action
certification determination
Certification Package
Certification Class
certification lifecycle
certification status
Certifier-controlled artifacts
```

The Certification Package remains Certifier's canonical operational record.

Downstream Suite use does not transfer Certifier authority.

---

## Registry

Satoshium Registry creates and governs its own Registry Entry.

Production relationship:

```text
SC-CERT-2026-0001
        ↓
SREG-2026-0001
```

`SREG-2026-0001` catalogs the certification while Registry retains authority over registration, cataloging, Registry metadata, lifecycle, and Registry-controlled relationships.

Registry cataloging does not become certification.

---

## Chronicle

Satoshium Chronicle creates and governs its own Chronicle Entry for qualifying historical Occurrences.

Production relationship:

```text
SC-CERT-2026-0001
certification-created Occurrence
        ↓
CHR-2026-0001
```

`CHR-2026-0001` preserves the July 5, 2026 certification Occurrence.

Chronicle historical preservation does not become certification.

---

## Anchor

Satoshium Anchor creates and governs an Integrity Reference for a specifically defined representation of an authoritative artifact.

Production relationship:

```text
SCRD-SC-CERT-2026-0001
        ↓
references_source
        ↓
ANCH-2026-0001
```

`ANCH-2026-0001` applies only to the defined complete canonical SCRD JSON representation.

It does not establish integrity for the Certification Package as a whole or for linked and referenced artifacts.

Anchor integrity preservation does not become certification.

---

## Beacon

Satoshium Beacon is Operational.

Beacon directly observed the canonical Certifier source and published its first Discovery Signal:

```text
SC-CERT-2026-0001
        ↓
direct Beacon observation
        ↓
BEAC-2026-0001
```

Beacon owns `BEAC-2026-0001`, its Discovery Signal, discovery metadata, provenance, lifecycle, publication state, and Beacon-controlled relationships.

Certifier remains authoritative for the certification decision, class, lifecycle, and status.

Beacon discovery does not become certification.

The September 13 Beacon observation does not, by itself, establish unchanged Certifier state on later dates.

---

## Attestor

Satoshium Attestor is Operational.

The inaugural Attestor production operation used eligible governed Suite-source evidence concerning `SC-CERT-2026-0001` and produced:

```text
Eligible Governed Inputs
        ↓
ATT-2026-0001
        ↓
Rule-Constrained Evaluation
        ↓
supported
        ↓
TRST-2026-0001
```

`ATT-2026-0001` and `TRST-2026-0001` are:

```text
Active
Published
V1.0
```

`TRST-2026-0001` is `derived-from` `ATT-2026-0001`.

Attestor preserves governed references to `SC-CERT-2026-0001`, `SREG-2026-0001`, `CHR-2026-0001`, `ANCH-2026-0001`, and `BEAC-2026-0001`.

Attestor does not:

```text
re-certify the Certifier decision
replace Certifier authority
redefine Atlas authority
rewrite Registry or Chronicle
extend Anchor integrity beyond its defined representation
convert Beacon discovery authority into Attestor authority
establish generalized trustworthiness
```

Its Trust Statement is governed, attributable, and bounded to the evaluated proposition, evidence, scope, and limitations.

---

## Atlas

Satoshium Atlas remains authoritative for the underlying subject intelligence and Atlas-controlled records that may become Certification Subjects.

For the inaugural production certification, the subject is:

```text
Satoshium Atlas Jurisdiction Record — El Salvador
```

Certifier evaluates the certification subject under its governed certification process without absorbing Atlas authority over the underlying jurisdiction intelligence.

---

## Navigator

Satoshium Navigator is Operational and provides:

```text
Workflow Definition
Orchestration
```

Navigator may coordinate workflows around Suite records while each participating institution retains authority over its own canonical objects and decisions.

---

## Authority Model

The production-proven institutional boundary is:

```text
Atlas      → authoritative subject intelligence
Certifier  → certification
Registry   → registration and cataloging
Chronicle  → historical preservation
Anchor     → integrity references
Beacon     → discovery signals
Attestor   → governed Attestations and bounded Trust Statements
Navigator  → workflow definition and orchestration
```

No downstream relationship changes the originating institution's authority.

---

## Relationship Semantics

Interoperability must preserve relationship meaning.

```text
Connection ≠ Identity
Reference ≠ Derivation
Reference ≠ Support
Reference does not transfer authority
```

A reference identifies or connects an object.

A derivation relationship asserts that one governed object is derived from another.

A support determination belongs to the institution and process authorized to make that determination.

These concepts must not be silently collapsed.

---

## Canonical Production References

```text
SC-CERT-2026-0001
/certifier/certifications/SC-CERT-2026-0001/

SREG-2026-0001
/registry/registered-items/SREG-2026-0001/

CHR-2026-0001
/chronicle/entries/CHR-2026-0001/

ANCH-2026-0001
/anchor/anchored-items/ANCH-2026-0001/

BEAC-2026-0001
/beacon/records/BEAC-2026-0001/

ATT-2026-0001
/attestor/attestations/ATT-2026-0001/

TRST-2026-0001
/attestor/trust-statements/TRST-2026-0001/
```

---

## Governing Principle

> Certifier certifies. Registry catalogs. Chronicle preserves historical Occurrences. Anchor preserves Integrity References. Beacon publishes Discovery Signals. Attestor creates governed Attestations and produces bounded Trust Statements through Rule-Constrained Evaluation. Navigator defines and orchestrates workflows.

> **Reference does not transfer authority.**

---

**Maintained By:** Satoshium
