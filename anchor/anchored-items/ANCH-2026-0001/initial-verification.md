# ANCH-2026-0001 — Initial Verification

## Verification Record

**Anchor Identifier:** ANCH-2026-0001  
**Anchor Version:** 1  
**Verification Type:** Initial Verification  
**Verified At:** 2026-08-29T14:31:00-07:00  
**Stage A Prerequisite:** PASS  
**Verification Result:** **match**

---

## Verification Purpose

Initial Verification tests whether the governed Canonical Representation can be reproduced and whether the resulting integrity evidence agrees with the Integrity Value preserved by Anchor.

```text
Original SCRD JSON
        ↓
RFC 8785 JCS
        ↓
UTF-8 canonical bytes
        ↓
SHA-256
        ↓
Observed Integrity Value
        ↓
compare
        ↓
Expected Integrity Value
```

---

## Verification Subject

```text
Source Institution
→ Satoshium Certifier

Source Artifact
→ SCRD-SC-CERT-2026-0001

Source Version
→ 1.1

Representation Type
→ canonical_json

Representation Boundary
→ complete SCRD JSON document

Canonicalization
→ RFC 8785 JCS

Encoding
→ UTF-8

Integrity Method
→ cryptographic_digest

Algorithm
→ SHA-256
```

---

## Expected Integrity Value

```text
945e272f49f433f2ddab5e94b65120f11cc5192a0916c15eca1b6ebd9c19af84
```

## Observed Integrity Value

```text
945e272f49f433f2ddab5e94b65120f11cc5192a0916c15eca1b6ebd9c19af84
```

---

## Reproduction Results

| Check | Result | Evidence |
|---|---|---|
| source_artifact_loaded | **PASS** | SCRD-SC-CERT-2026-0001 source JSON loaded successfully. |
| canonicalization_preconditions | **PASS** | Source contains no JSON numeric values; the governed RFC 8785 reproduction for this document requires no special ECMAScript number serialization handling. |
| canonical_representation_reproduced | **PASS** | Reproduced canonical bytes exactly match the preserved canonical representation. |
| canonical_byte_length | **PASS** | Reproduced length=4415 bytes; preserved length=4415 bytes. |
| sha256_recalculated | **PASS** | Recalculated SHA-256=945e272f49f433f2ddab5e94b65120f11cc5192a0916c15eca1b6ebd9c19af84. |
| integrity_value_comparison | **PASS** | Recalculated digest matches expected Integrity Value=945e272f49f433f2ddab5e94b65120f11cc5192a0916c15eca1b6ebd9c19af84. |

---

## Canonical Representation Comparison

```text
Reproduced canonical byte length
→ 4415 bytes

Preserved canonical byte length
→ 4415 bytes

Byte-for-byte comparison
→ MATCH
```

The source document contains no JSON numeric values. For the data types present in this SCRD, the reproduced deterministic serialization does not require special ECMAScript numeric serialization handling.

---

## Digest Comparison

```text
Expected SHA-256
→ 945e272f49f433f2ddab5e94b65120f11cc5192a0916c15eca1b6ebd9c19af84

Observed SHA-256
→ 945e272f49f433f2ddab5e94b65120f11cc5192a0916c15eca1b6ebd9c19af84

Comparison
→ MATCH
```

---

## Verification Result

```text
Verification Result
→ match
```

The governed Canonical Representation was reproduced successfully.

The independently recalculated SHA-256 Integrity Value agrees exactly with the Integrity Value preserved in `ANCH-2026-0001`.

This supports integrity consistency for the reviewed representation.

It does not establish substantive truth, certification validity, reputation, or trust.

> Integrity Verification ≠ Certification ≠ Trust

---

## Production Effect

Initial Verification is now complete.

```text
Stage A Validation
→ PASS

Initial Verification
→ match
```

The record remains:

```text
Publication State
→ unpublished

Lifecycle State
→ draft
```

Initial Verification does not itself authorize publication.

---

## Next Required Step

Prepare the canonical Anchor human-readable and machine-readable publication representations, then perform:

```text
Stage B — Publication-Readiness Validation
```

**Maintained By:** Satoshium
