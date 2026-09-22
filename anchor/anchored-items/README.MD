# Satoshium Anchor — Anchored Items

**Path:** `/anchor/anchored-items/`  
**Canonical Page:** `index.html`  
**Institution:** Satoshium Anchor  
**Directory Role:** Production package index for assigned Anchor Integrity References

---

## Purpose

The Anchored Items directory is the production-package home for assigned Satoshium Anchor Integrity References.

```text
/anchor/anchored-items/
→ production package home

/anchor/integrity-references/
→ published Integrity Reference index
```

An Anchored Item package may exist before publication. Inclusion in this directory therefore does not, by itself, establish that an Integrity Reference is published or has passed the Publication Gate.

Assignment establishes stable Anchor identity.

```text
Assigned
≠
Published
≠
Publication Gate APPROVED
```

---

## Package Model

An Anchored Item package may contain:

```text
Integrity Reference JSON
canonical Source representation
integrity-value record
Validation records
Verification records
canonical publication representations
Corrections / Version lineage where applicable
README documentation
```

Each package preserves the record-specific production evidence needed to understand the Integrity Reference, its source boundary, integrity method, Validation and Verification history, lifecycle, publication state, and later maintenance.

---

## ANCH-2026-0001

`ANCH-2026-0001` is the first Satoshium Anchor Integrity Reference.

**Current production state:**

```text
Anchor Identifier → ANCH-2026-0001
Anchor Version → 1
Source Institution → Satoshium Certifier
Source Artifact → SCRD-SC-CERT-2026-0001
Representation Type → canonical_json
Canonicalization → RFC 8785 JCS
Integrity Method → cryptographic_digest
Algorithm → SHA-256
Stage A Validation → PASS
Initial Verification → match
Stage B Publication-Readiness Validation → COMPLETE
Publication Gate → APPROVED
Publication State → published
Lifecycle State → active
Published At → 2026-08-29T15:40:14-07:00
```

Canonical package:

```text
/anchor/anchored-items/ANCH-2026-0001/
```

`ANCH-2026-0001` preserves cryptographic integrity context for the complete canonical JSON representation of:

```text
SCRD-SC-CERT-2026-0001
```

The representation boundary does not extend to the Certification Package as a whole or to linked and referenced artifacts unless those objects are separately anchored.

---

## Published Integrity Reference Index

The published Integrity Reference index is:

```text
/anchor/integrity-references/
```

Only records that have completed the required governed path should appear as published Integrity References.

For `ANCH-2026-0001`, that path is complete:

```text
Integrity Reference candidate
        ↓
Stage A — Structural / Institutional Validation
        ↓
Initial Verification
        ↓
Canonical HTML + Canonical JSON
        ↓
Stage B — Publication-Readiness Validation
        ↓
Human / Machine consistency confirmation
        ↓
Publication Gate
        ↓
Publication
        ↓
Maintenance / Reverification
```

---

## Authority Boundary

Satoshium Anchor owns:

```text
Anchor Integrity References
Anchor-controlled integrity metadata
representation boundaries
integrity methods and values
Anchor Validation
Anchor Verification
Anchor lifecycle
Anchor publication state
Anchor-controlled relationships
```

Source institutions remain authoritative for the source records referenced by Anchor.

For `ANCH-2026-0001`, Satoshium Certifier remains authoritative for:

```text
SCRD-SC-CERT-2026-0001
SC-CERT-2026-0001
certification meaning
certification status
Certifier lifecycle
Certifier-controlled content
```

Anchor does not become authoritative for those matters merely because it records an Integrity Reference.

> **Reference does not transfer authority.**

---

## Relationship to Attestor

`ANCH-2026-0001` later became an eligible governed Suite-source input in Attestor's first controlled production operation.

```text
ATT-2026-0001
→ references
→ ANCH-2026-0001

TRST-2026-0001
→ references
→ ANCH-2026-0001
```

`TRST-2026-0001` remains `derived-from` `ATT-2026-0001`.

These downstream references do not extend Anchor integrity beyond the defined canonical SCRD JSON representation and do not transfer Anchor authority to Attestor.

---

## Governance Distinctions

The Anchored Items directory preserves several independent governance dimensions:

```text
Identity
≠
Validation
≠
Verification
≠
Lifecycle
≠
Publication
```

A successful integrity verification confirms agreement with the governed integrity value for the defined representation. It does not establish the substantive truth, certification meaning, or authority of the source record.

Likewise:

> **Integrity of a representation ≠ truth of its contents.**

---

## Maintenance

Publication does not end Anchor responsibility.

Future maintenance may include:

```text
reverification
source-version review
representation-boundary review
Correction
Versioning
Supersession
lifecycle change
publication-state change
relationship maintenance
```

Material changes must follow the applicable Anchor governance process and preserve prior material state where required.

---

## Current Directory Status

The Anchored Items directory contains Anchor production packages across their governed lifecycle.

The first production package, `ANCH-2026-0001`, has completed its production sequence and is:

```text
Published
Active
Version 1
Stage A Validation PASS
Initial Verification match
Publication Gate APPROVED
```

---

## Guiding Principles

> Preserve durable integrity context without absorbing the authority of the referenced record.

> Reference does not transfer authority.

> Production validates architecture. Architecture does not validate itself.

---

**Maintained By:** Satoshium
