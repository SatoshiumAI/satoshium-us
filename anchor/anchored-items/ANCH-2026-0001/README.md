# ANCH-2026-0001

## Overview

This directory is the production package for:

```text
ANCH-2026-0001
```

the first assigned Satoshium Anchor Integrity Reference candidate.

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

During pre-publication it documents the assigned candidate and its production state.

It does not itself establish Publication Gate approval or public Anchor authority.

### `integrity-reference.json`

Machine-readable Integrity Reference candidate governed by the Anchor Integrity Reference Base Schema.

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

No Version, Correction, Supersession, Verification, Publication, Maintenance, or external-commitment relationship is required for the initial Version 1 candidate.

---

# Record State

Current pre-publication state:

```text
Integrity State
→ current

Publication State
→ unpublished

Lifecycle State
→ draft
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

The following have been completed:

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
Integrity Reference candidate constructed
Base Schema conformance check passed
```

The following have not yet been completed:

```text
Stage A — Structural / Institutional Validation
Initial Verification
Canonical publication representations
Stage B — Publication-Readiness Validation
Publication Gate
Publication
Integrity References Index entry
```

---

# Validation Status

The candidate has successfully passed a machine schema-conformance check against the reconciled Integrity Reference Base Schema.

This does not equal formal Anchor Validation.

```text
Schema conformance PASS
≠
Stage A Validation PASS
```

Formal Anchor Validation remains the next production step.

---

# Verification Status

Initial Verification has not yet been formally recorded.

The expected successful Verification Result is:

```text
match
```

A `match` may be recorded only after the governed Verification process reproduces the Canonical Representation and confirms exact agreement with the expected SHA-256 Integrity Value.

---

# Publication Status

```text
Publication State
→ unpublished
```

The assigned candidate has not yet:

```text
passed Stage A Validation
completed Initial Verification
passed Stage B Publication-Readiness Validation
received Publication Gate approval
entered public Anchor authority
```

It must not yet be listed in the published Integrity Reference index.

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

**Production Candidate · Assigned · Unpublished**

```text
Anchor Identifier → ANCH-2026-0001
Anchor Version → 1
Integrity State → current
Publication State → unpublished
Lifecycle State → draft
```

**Next Required Step:** Stage A — Structural / Institutional Validation

**Maintained By:** Satoshium
