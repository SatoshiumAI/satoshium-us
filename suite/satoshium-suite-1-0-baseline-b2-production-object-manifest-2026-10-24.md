# Satoshium Suite 1.0 — B2 Historical Production Object Baseline Manifest

**Review date:** October 24, 2026  
**Repository/branch:** `SatoshiumAI/satoshium-us` / `phase004`  
**Evidence snapshot (pre-B2):** `225f3076dab7f85baf16a2ef270f7ab7700cc7f6`  
**Status:** **B2 COMPLETE — APPROVED (fixed-commit historical production-object manifest)**  
**Phase 3 Suite 1.0 Baseline Review:** ACTIVE  
**Suite 1.0 release:** **NOT APPROVED / NOT TAGGED BY THIS RECORD**

## Scope and meaning

This manifest identifies the **seven distinct institution-owned inaugural production objects** previously traced in Phase 2 (PI-07), with stable repository paths, file-blob identities, recorded versions, state, and provenance boundaries. It is a **historical evidence manifest**, not a new production issuance, current-state polling exercise, prospective automated pipeline, or confirmation that `satoshium.us` successfully served each route in an independent browser.

The source files listed below were retrieved from the exact frozen snapshot. Git **blob SHAs identify repository file bytes**; they are not the Anchor JCS/SHA-256 integrity digest, and no claim of independent cryptographic verification of issued records is made here.

**Governing rule: Authority follows the governed subject. Reference does not transfer authority.**

## Seven canonical object-family entries

| Object | Institution / governed meaning | Record version and recorded production standing | Canonical record location in repository |
|---|---|---|---|
| `SC-CERT-2026-0001` | **Certifier:** Certification Package, issued for the Atlas El Salvador jurisdiction subject; Certifier owns its determination | Package **1.1**, **Issued · Active**, Operational; dated July 5, 2026 | `certifier/certifications/SC-CERT-2026-0001/index.html` and `README.md` |
| `SREG-2026-0001` | **Registry:** canonical Satoshium Registry Entry registering the Certifier source | Entry **1.0**, `registry_status=active`, Registry publication recorded August 2, 2026 | `registry/registered-items/SREG-2026-0001/record.json`, `registry-entry.html` |
| `CHR-2026-0001` | **Chronicle:** Chronicle Entry preserving the certification-created occurrence | Entry **1**, schema **1.0.0**, `verification_state=verified`, `lifecycle_state=active`, `publication_state=published`; August 22, 2026 | `chronicle/entries/CHR-2026-0001/record.json`, `index.html` |
| `ANCH-2026-0001` | **Anchor:** Integrity Reference for **defined SCRD JSON representation**, not entire Certifier Package | Anchor Version **1**; serialized `schema_version=1.0-draft`; verification record says `match`, separate publication record says `published` and `active`; August 29, 2026 | `anchor/anchored-items/ANCH-2026-0001/integrity-reference.json` and `publication.json` |
| `BEAC-2026-0001` | **Beacon:** Discovery Signal following direct observation of Certifier's canonical Package | Signal **1.0**, **Active · Published**, September 13, 2026 | `beacon/records/BEAC-2026-0001/index.html` and `README.md` |
| `ATT-2026-0001` | **Attestor:** verification-related Attestation with governed references, not a Trust Statement | **V1.0**, `active` / `published`; final recorded Validator **0.5** aggregate `valid`, conformance `conformant` | `attestor/attestations/ATT-2026-0001/attestation.yaml`, `index.html` |
| `TRST-2026-0001` | **Attestor:** Trust Statement derived from ATT via Rule-Constrained Evaluation, bounded `supported` outcome | **V1.0**, `active` / `published`; final recorded Validator **0.5** aggregate `valid`, conformance `conformant` | `attestor/trust-statements/TRST-2026-0001/trust-statement.yaml`, `index.html` |

**Canonical-file cautions:** The Certifier `scrd_json.json` is a **subordinate Certified Record representation** and must not be promoted to the canonical Certification Package. Registry `record.json` and Chronicle `record.json` are machine representations of their respective independently issued objects. The two Attestor YAML objects are separate canonical types and are not the same object in two formats. Beacon's first object directory contains its `README.md` and `index.html`, **not** a Beacon `record.json`; do not invent a canonical machine contract. Anchor's `1.0-draft` serialized schema label must not be silently presented as production-final `1.0` schema adoption.

## Fixed blob identities — principal sampled files

These blob IDs were read back directly through the GitHub connection at the frozen HEAD; they pin contents for later release comparison, not external runtime behavior.

| Repository path | Git blob SHA |
|---|---|
| `certifier/certifications/SC-CERT-2026-0001/README.md` | `867d555d384d647bf490e22d0df8de6fca5f1ac7` |
| `certifier/certifications/SC-CERT-2026-0001/index.html` | `0e54deb0c42de3396a4c13c9058da5739a2b0ce4` |
| `certifier/certifications/SC-CERT-2026-0001/records/certified-record/scrd_json.json` | `f1aedbc2899aaa94a59dcbef7d9438869adb62bc` |
| `registry/registered-items/SREG-2026-0001/record.json` | `9faf4401ec432ae1367aec5207a6eb08da308f99` |
| `chronicle/entries/CHR-2026-0001/record.json` | `b3be44b9fd143c0336f20eb22343506ab6bfb317` |
| `chronicle/entries/CHR-2026-0001/CHR-2026-0001-v1-validation.md` | `db451cb7d6677ad7e2b49cbc38d11684e17fec2d` |
| `anchor/anchored-items/ANCH-2026-0001/integrity-reference.json` | `fc2063daf1b8ba402e93c9e13b9070385e28b2ac` |
| `anchor/anchored-items/ANCH-2026-0001/publication.json` | `26b95e0a3b9c4875382e57e284fe9587966ceaf6` |
| `beacon/records/BEAC-2026-0001/README.md` | `86a76bca577c02fa8055513d87a2c7c1e0832062` |
| `beacon/records/BEAC-2026-0001/index.html` | `20f48f2e2659c8760eec1734360f51018bdddf0b` |
| `attestor/attestations/ATT-2026-0001/attestation.yaml` | `421ba0154bf07c52bfcb4622e8643dbeff2fef85` |
| `attestor/trust-statements/TRST-2026-0001/trust-statement.yaml` | `48232d2cc406e6e55dbda5671faceacd46fa129b` |
| `attestor/production/first-operation/validation/validation-report-ATT-2026-0001-final-active-published-v05.json` | `f16c27606bc6beda22d4e8d89b06d0b0a30820d5` |
| `attestor/production/first-operation/validation/validation-report-TRST-2026-0001-final-active-published-v05.json` | `d9506cc63c133550b498a460a2085d8db4520228` |

## Lineage and authority checks

- **Atlas** retains jurisdiction intelligence authority; no separate Atlas object is invented as an eighth inaugural lineage object.
- **Certifier** issued `SC-CERT` independently. Its associated `SCRD` JSON representation is the **Anchor integrity subject**.
- **Registry** registers and catalogs the source; **Chronicle** preserves the occurrence; **Anchor** records representation-bound integrity; **Beacon** directly observed Certifier for discovery. These four institutions do not inherit the source certification decision or form a mandatory serial workflow.
- **Attestor** created the distinct `ATT`, evaluated within a governed and bounded evidence context, and produced `TRST` with a `supported` outcome; `TRST` is `derived-from ATT`, not `derived-from` every merely referenced upstream record.
- Source versions, lifecycle states and publication states remain **institution-specific dimensions**; values such as `active`, `published`, `valid`, `conformant` and `supported` are not interchangeable.

## B2 acceptance determination

| B2 criterion | Evidence-bound result |
|---|---|
| Enumerate the fixed first-production object identifiers and source owner | **PASS — 7/7** |
| Record principal source paths, content blob fingerprints and versions | **PASS — 7/7 source families; 14 inspected principal blobs** |
| Preserve object-vs-representation / authority / provenance distinctions | **PASS within sampled sources** |
| Distinguish historical preserved operational decisions from fresh validation | **PASS** |
| Existing current live HTTP availability of each canonical URL | **NOT TESTED** |
| New machine validation and end-to-end runtime replay | **NOT TESTED** |
| A released Suite 1.0 tag or deployment configuration | **NOT ESTABLISHED** |

**Disposition:** **B2 — COMPLETE — APPROVED (fixed-commit historical production-object evidence manifest).** This is not a comprehensive re-audit of all objects' every artifact, nor is it new institutional production validation. It creates a bounded, reproducible source basis for B3–B8 and any later release candidate.

## Next gate — B3

Compare this manifest's actual version and state values against Suite Standards, Methodology, Governance, Versions and Interoperability release expectations. Determine which are controlling current contracts, historical versions, draft schemas or deferred implementation profiles. **Version ≠ Decision.** No release tag or public Suite 1.0 claim is authorized in B2.

**Overall Phase 3 remains ACTIVE.**
