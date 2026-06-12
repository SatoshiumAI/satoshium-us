# Hash Evidence

This directory contains cryptographic hash records used by Satoshium Certifier to support integrity verification, evidence preservation, traceability, and future proof-of-record capabilities.

Hashes help answer a simple question:

> Is this the same artifact that was originally reviewed?

Hash records provide a mechanism for detecting changes to files, reports, receipts, datasets, screenshots, and other certification artifacts.

---

# Purpose

The purpose of the hashes directory is to preserve integrity references associated with certification activities.

Hash records may be generated for:

* Certification reports
* Certification receipts
* Evidence packages
* Screenshots
* Datasets
* Source files
* Documentation
* Registry records
* Future preservation artifacts

Hashes do not prove correctness.

Hashes help demonstrate consistency and integrity.

---

# Hash Philosophy

Certifier is founded upon evidence-based review.

Evidence itself should be capable of verification whenever practical.

Hash records support this objective by providing a reproducible fingerprint of a digital artifact at a specific point in time.

If the artifact changes, the hash changes.

This allows future reviewers to determine whether a reviewed artifact remains identical to the version originally examined.

---

# What Belongs Here

Examples of hash-related records include:

## Certification Report Hashes

Integrity references for certification reports.

Examples:

```text
certification-report-2026-000001.sha256
```

---

## Certification Receipt Hashes

Integrity references for certification receipts.

Examples:

```text
receipt-2026-000001.sha256
```

---

## Evidence Package Hashes

Integrity references for collections of certification evidence.

Examples:

```text
atlas-initial-build-evidence.sha256
```

---

## Screenshot Hashes

Integrity references for screenshots used as certification evidence.

Examples:

```text
atlas-homepage-screenshot.sha256
```

---

## Dataset Hashes

Integrity references for structured datasets reviewed during certification.

Examples:

```text
atlas-jurisdiction-records.sha256
```

---

## Future Anchor References

Future versions of Certifier may generate hash records specifically intended for preservation by Anchor.

Examples:

```text
anchor-reference-2026-000001.sha256
```

---

# Recommended Structure

```text
hashes/
├── reports/
├── receipts/
├── evidence/
├── screenshots/
├── datasets/
├── standards/
└── archive/
```

Additional categories may be introduced as Certifier evolves.

---

# Recommended Algorithms

Version 1.0 recommends:

```text
SHA-256
```

for certification activities.

Future versions may support additional algorithms where appropriate.

Examples:

```text
SHA-256
SHA-384
SHA-512
```

Hash algorithms should be clearly documented whenever used.

---

# Hash Record Format

A hash record should clearly identify:

* Hash algorithm
* Hash value
* Artifact name
* Artifact location
* Date generated
* Generator or process

Example:

```text
Algorithm:
SHA-256

File:
certification-report-2026-000001.md

Hash:
3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Generated:
2026-07-25
```

---

# Example File Naming

Recommended format:

```text
artifact-name.sha256
```

Examples:

```text
atlas-initial-build-report.sha256
atlas-initial-build-receipt.sha256
atlas-homepage-screenshot.sha256
```

For versioned artifacts:

```text
atlas-standard-v1.sha256
atlas-standard-v2.sha256
```

---

# Verification Process

Future reviewers should be able to:

1. Obtain the original artifact.
2. Generate a new hash using the same algorithm.
3. Compare the generated value to the stored hash.

Matching values indicate that the artifact has not changed since the hash was originally generated.

Non-matching values indicate that the artifact has changed or become corrupted.

---

# Relationship to Evidence

Hashes are considered evidence references rather than primary evidence.

For example:

| Artifact   | Primary Evidence | Hash            |
| ---------- | ---------------- | --------------- |
| Screenshot | Screenshot File  | Screenshot Hash |
| Report     | Report File      | Report Hash     |
| Dataset    | Dataset File     | Dataset Hash    |

The artifact remains the primary evidence.

The hash supports integrity verification.

---

# Relationship to Certification Records

Hash references may be included within:

* Certification Records
* Certification Reports
* Certification Receipts
* Registry Entries
* Future Attestation Records

This allows integrity verification to remain associated with certification outcomes.

---

# Relationship to Anchor

Future versions of the Satoshium ecosystem may introduce Anchor as a preservation subsystem.

Hash records are expected to become a primary integration point between Certifier and Anchor.

Example workflow:

```text
Certification Report
        ↓
SHA-256 Hash
        ↓
Anchor Record
        ↓
Long-Term Preservation
```

In this model, Anchor preserves proof references while Certifier preserves review records.

---

# Relationship to Attestor

Future Attestor activities may independently validate:

* Hash generation
* Hash preservation
* Hash consistency
* Artifact integrity

Attestation records may reference hash values as supporting evidence.

---

# Retention

Hash records should generally be preserved for at least as long as the associated certification artifact exists.

Whenever practical:

* Reports should retain hashes.
* Receipts should retain hashes.
* Evidence packages should retain hashes.
* Archived certification records should retain hashes.

Hash preservation supports future verification activities.

---

# Long-Term Vision

The hashes directory represents the foundation of Certifier's integrity layer.

Today, hashes provide simple verification references.

Tomorrow, they may support:

* Anchor preservation
* Attestation workflows
* Registry validation
* Historical integrity verification
* Automated trust systems

The purpose remains unchanged:

To provide a reproducible method for determining whether a reviewed artifact remains identical to the version originally certified.

---

# Guiding Statement

> Evidence explains what was reviewed.
>
> Hashes help prove it has not changed.
>
> The hashes directory exists to preserve integrity across time.
