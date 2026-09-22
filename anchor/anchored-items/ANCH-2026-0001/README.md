# ANCH-2026-0001

## Overview

This directory is the production package for:

```text
ANCH-2026-0001
```

the first published Satoshium Anchor Integrity Reference.

The Integrity Reference preserves durable integrity context for the complete JSON representation of:

```text
SCRD-SC-CERT-2026-0001
```

owned by:

```text
Satoshium Certifier
```

> Reference does not transfer authority.

---

## Package Location

```text
/anchor/anchored-items/ANCH-2026-0001/
```

This directory is the package home for the Anchor record itself.

The future:

```text
/anchor/integrity-references/
```

serves as the published Integrity Reference index and should not be confused with the individual record package.

---

## Package Contents

```text
index.html
integrity-reference.json
source-rfc8785-jcs.json
sha256.txt
README.md
```

### `index.html`

Human-readable package page.

It is the canonical human-readable representation of the published Integrity Reference.

Publication Gate approval and public Anchor authority are preserved through the governed production record and current published state.

### `integrity-reference.json`

Canonical machine-readable Integrity Reference governed by the Anchor Integrity Reference Base Schema.

### `source-rfc8785-jcs.json`

Preserved Canonical Representation used to generate the Integrity Value.

### `sha256.txt`

Human-readable digest generation record.

### `README.md`

Repository documentation for this production package.

---

# Anchor Identity

```text
Anchor Identifier
→ ANCH-2026-0001

Anchor Version
→ 1

Schema Version
→ 1.0-draft
```

The Anchor Identifier is permanently assigned.

It must not be recycled or reassigned if this candidate fails Validation or never reaches publication.

---

# Source

```text
Source Institution
→ Satoshium Certifier

Source Artifact
→ SCRD-SC-CERT-2026-0001

Source Artifact Type
→ Satoshium Certified Record (SCRD JSON)

Source Version
→ 1.1

Source Package
→ SC-CERT-2026-0001

Source Location
→ /certifier/certifications/SC-CERT-2026-0001/records/certified-record/scrd_json.json
```

---

# Representation

```text
Representation Type
→ canonical_json

Representation Boundary
→ complete SCRD JSON document

Canonicalization
→ RFC 8785 — JSON Canonicalization Scheme (JCS)

Encoding
→ UTF-8

Canonical Byte Length
→ 4,415 bytes
```

The Representation Boundary includes the complete SCRD JSON document.

It does not include linked or referenced artifacts such as:

```text
Certification Package
SCPR
SCR
SCRD HTML
Atlas pages
Registry records
Chronicle records
other linked Suite artifacts
```

unless those objects are separately anchored.

---

# Integrity Method

```text
Integrity Method
→ cryptographic_digest

Algorithm
→ SHA-256

Digest Encoding
→ lowercase hexadecimal
```

The generated Integrity Value is:

```text
945e272f49f433f2ddab5e94b65120f11cc5192a0916c15eca1b6ebd9c19af84
```

---

# Relationship

The initial production relationship set contains one required relationship:

```text
ANCH-2026-0001
→ references_source
→ SCRD-SC-CERT-2026-0001
```

Machine-level context:

```text
relationship_type
→ references_source

target_identifier
→ SCRD-SC-CERT-2026-0001

target_system
→ Satoshium Certifier

target_location
→ https://satoshium.us/certifier/certifications/SC-CERT-2026-0001/records/certified-record/scrd_json.json
```

The initial Version 1 source relationship remains `references_source`. Later Verification, Publication, and downstream Suite references do not change the Source Artifact relationship or transfer source authority.

---

# Record State

Current production state:

```text
Integrity State
→ current

Publication State
→ published

Lifecycle State
→ active

Published At
→ 2026-08-29T15:40:14-07:00
```

These dimensions remain distinct.

```text
Integrity State
≠
Publication State
≠
Lifecycle State
```

---

# Current Production Position

The Version 1 production sequence is complete:

```text
Source Artifact selected
Representation Boundary defined
Representation Type frozen
RFC 8785 JCS selected
SHA-256 selected
Integrity Value generated
Anchor Identifier assigned
Anchor Version assigned
Source relationship defined
Integrity Reference constructed
Base Schema conformance check passed
Stage A — Structural / Institutional Validation PASS
Initial Verification match
Canonical HTML prepared
Canonical JSON prepared
Stage B — Publication-Readiness Validation completed
Publication Gate APPROVED
Publication COMPLETE
```

---

# Validation Status

Formal Stage A Validation is complete.

```text
Outcome → PASS
Rule Set → VAL-001 through VAL-042
PASS → 28
FAIL → 0
NOT APPLICABLE → 14
```

Schema conformance remains distinct from formal Anchor Validation.

---

# Verification Status

Initial Verification is complete.

```text
Verified At → 2026-08-29T14:31:00-07:00
Verification Result → match
Method ID → digest-1
```

Detailed digest-comparison evidence is preserved in:

```text
initial-verification.json
```

---

# Publication Status

```text
Publication State → published
Lifecycle State → active
Published At → 2026-08-29T15:40:14-07:00
Publication Gate → APPROVED
```

Anchor Version 1 has entered public Anchor authority for its own Integrity Reference metadata.

---

# Production Path

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

# Later Suite Relationships

`ANCH-2026-0001` later became an eligible governed Suite-source input in Attestor's first controlled production operation.

```text
ATT-2026-0001
        ↓
references
        ↓
ANCH-2026-0001
```

```text
TRST-2026-0001
        ↓
references
        ↓
ANCH-2026-0001
```

`TRST-2026-0001` remains `derived-from` `ATT-2026-0001`.

These references do **not** extend Anchor integrity beyond the defined canonical SCRD JSON representation. They do not make Anchor authoritative for the Certification Package as a whole, the Atlas subject, Beacon discovery, Attestor evaluation, or the Trust Statement.

> Reference does not transfer authority.

---

# Authority Boundary

Satoshium Anchor owns:

```text
ANCH-2026-0001
```

Satoshium Certifier remains authoritative for:

```text
SCRD-SC-CERT-2026-0001
```

Anchor does not become authoritative for the Source Artifact's certification meaning, substantive content, status, or Source lifecycle merely because it records an Integrity Reference.

> Reference does not transfer authority.

---

# Preservation Principle

> Preserve durable integrity context without absorbing the authority of the referenced record.

---

## Status

**Published · Active · Version 1**

```text
Anchor Identifier → ANCH-2026-0001
Anchor Version → 1
Integrity State → current
Publication State → published
Lifecycle State → active
Published At → 2026-08-29T15:40:14-07:00
Stage A Validation → PASS
Initial Verification → match
Publication Gate → APPROVED
Publication → COMPLETE
```

Future changes must follow Anchor maintenance, reverification, Validation, Versioning, Correction, and Publication procedures as applicable.

**Maintained By:** Satoshium
