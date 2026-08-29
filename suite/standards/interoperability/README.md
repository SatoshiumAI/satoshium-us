# Interoperability Standard

## Overview

The **Satoshium Interoperability Standard** defines how Suite tools, records, schemas, references, verification material, and external systems communicate without losing meaning.

The governing principle is:

> Interoperability is not merely data exchange. It is preservation of meaning across systems.

---

## Standard Role

Interoperability allows Satoshium institutions to remain independent while still exchanging and referencing governed records.

```text
Atlas
Certifier
Registry
Chronicle
Anchor
Beacon
Attestor
Navigator
```

may all use shared technical conventions without transferring institutional authority.

> Reference does not transfer authority.

---

# Shared Interfaces

Shared interfaces may exchange:

- record identifiers;
- canonical URLs;
- schema Versions;
- Controlled Values;
- canonical representations;
- integrity evidence;
- verification material;
- publication metadata;
- relationship metadata.

A shared interface should preserve enough context to interpret the transferred value correctly.

---

# Record Compatibility

Records exchanged across the Suite should remain understandable outside the system that created them.

Compatibility requires preserving distinctions such as:

```text
Source-System Identifier
≠
receiving-system identifier

Source Version
≠
receiving-system Version

Source status
≠
receiving-system state
```

---

# Meaning Preservation

An exchanged value should retain its governed meaning.

For example:

```text
canonical_json
```

must mean the same thing when used by Certifier, Registry, Chronicle, Anchor, Attestor, or another Suite institution.

The Suite Schemas Standard therefore governs its canonicalization semantics.

---

# Canonical JSON Interoperability

For Suite records using:

```text
Representation Type
→ canonical_json
```

the shared canonicalization rule is:

```text
RFC 8785 — JSON Canonicalization Scheme (JCS)
UTF-8
```

A receiving Suite institution should not reinterpret `canonical_json` under a conflicting local normalization scheme.

---

# Cryptographic Digest Interoperability

When a Suite record exchanges or preserves a cryptographic digest, the record should identify:

```text
Integrity Method
Algorithm
Digest Value
Digest Encoding
```

The initial Suite-approved digest profile is:

```text
Integrity Method
→ cryptographic_digest

Algorithm
→ SHA-256

Digest Encoding
→ lowercase hexadecimal

Expected encoded length
→ 64 hexadecimal characters
```

This profile supplies an interoperable starting point for production.

---

## SHA-256 Is an Initial Profile, Not a Permanent Definition

Satoshium should remain algorithm-agile.

```text
SHA-256
→ approved initial algorithm

future stronger / successor algorithm
→ may be introduced through governed revision
```

Historical records using SHA-256 should remain interpretable after a successor algorithm is introduced.

Algorithm replacement should occur through explicit governance rather than silent reinterpretation.

---

# Digest Comparison

Where SHA-256 digest values are compared, interoperable comparison uses the decoded cryptographic value represented by the governed lowercase hexadecimal serialization.

For the canonical serialized form:

```text
64 lowercase hexadecimal characters
```

should represent the 32-byte SHA-256 digest.

---

# External Alignment

Satoshium may align with external technical standards where doing so improves reproducibility and interoperability.

The current first production alignment includes:

```text
RFC 8785
→ canonical JSON serialization

SHA-256
→ initial cryptographic digest algorithm
```

Adopting an external technical standard does not transfer Satoshium institutional authority to that external standards body or implementation.

---

# Verification Data

When verification information crosses system boundaries, it should preserve at least the context necessary to understand:

```text
what representation was tested
which canonicalization rule applied
which Integrity Method applied
which algorithm applied
which expected value was used
what Verification Result was reached
```

A digest without algorithm and representation context is insufficient as a durable interoperable record.

---

# Relationship to Schemas

The Schemas Standard governs structured representation.

The Interoperability Standard governs shared interpretation and exchange.

For the first production path:

```text
Suite Schemas Standard
→ canonical_json = RFC 8785 JCS

Suite Interoperability Standard
→ SHA-256 + lowercase hexadecimal digest profile

Anchor
→ applies both to its first Integrity Reference
```

---

# Institutional Specialization

Institutions may define narrower operational requirements when needed.

They should inherit Suite-wide rules rather than redefine them.

```text
Suite Standard
        ↓
Institution-specific requirement
        ↓
Procedure / Schema Profile
        ↓
Production Record
```

---

# Current Freeze Decisions

### Canonical JSON Interoperability

```text
canonical_json → RFC 8785 JCS
encoding → UTF-8
```

### Initial Cryptographic Digest Profile

```text
method → cryptographic_digest
algorithm → SHA-256
digest encoding → lowercase hexadecimal
encoded length → 64 characters
```

### Still Unfrozen

```text
signature interoperability profile
timestamp interoperability profile
Merkle commitment profile
Bitcoin commitment profile
algorithm deprecation procedure
successor digest algorithms
external proof interchange profiles
```

---

## Status

**Suite Standard · Production-Reconciled**

The Interoperability Standard now defines the first Suite-wide digest and canonical-representation interoperability requirements required by live production architecture.

**Version:** 1.0-draft

**Maintained By:** Satoshium
