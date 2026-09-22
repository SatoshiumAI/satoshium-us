# License

**Scope:** Satoshium Anchor  
**Institution:** Satoshium Anchor  
**Canonical Object:** Integrity Reference  
**License:** MIT License

Copyright Holder: Christopher D. Burris — Satoshium™ Intelligence Systems

---

# Overview

Satoshium Anchor is released under the MIT License.

The MIT License is a permissive open-source license that allows individuals and organizations to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the licensed materials, subject to the conditions contained within the license.

The legally binding license governing this repository is contained in the repository's `LICENSE` file.

This `LICENSE.md` document provides additional context regarding the licensing philosophy, institutional boundaries, and intended use of Satoshium Anchor. It does not replace or modify the terms of the MIT License.

---

# Licensing Philosophy

Satoshium Anchor is the Satoshium Suite institution responsible for preserving durable **Integrity References** for authoritative artifacts and records.

Anchor records cryptographic, temporal, representation, provenance, and verification context so that later reviewers can determine whether a referenced representation remains consistent with the representation Anchor preserved.

Anchor does not assume authority over the referenced artifact, its meaning, its certification, its historical interpretation, or any trust conclusion derived from it.

Releasing Anchor under the MIT License reflects the belief that integrity-preservation methods, schemas, verification procedures, and related infrastructure should remain broadly accessible for study, implementation, adaptation, research, and improvement.

Open licensing encourages:

* Transparency
* Independent verification
* Collaboration
* Research
* Interoperability
* Reproducibility
* Long-term preservation
* Technical improvement

---

# Permitted Uses

Subject to the terms of the MIT License, users may:

* Use Anchor materials for personal projects.
* Use Anchor materials within organizations.
* Modify licensed Anchor materials.
* Extend licensed Anchor materials.
* Incorporate licensed materials into other software or systems.
* Create derivative works.
* Distribute modified versions.
* Use licensed materials commercially.

These permissions arise from the MIT License itself. This document does not create additional license rights beyond those terms.

---

# Attribution

The MIT License requires preservation of the applicable copyright notice and license text.

Users redistributing licensed materials should retain the notices required by the MIT License.

Use of the Satoshium name, Satoshium Anchor name, or Satoshium™ branding is not, by itself, granted merely because source materials are licensed under the MIT License. Trademark and branding rights are separate from copyright licensing.

---

# Institutional Role

Satoshium Anchor is an operational Satoshium Suite institution.

Its canonical object is the:

**Integrity Reference**

An Integrity Reference preserves the context required to independently review the integrity relationship between an authoritative Source Artifact and a defined Canonical Representation.

Anchor answers a bounded integrity question:

> Does the referenced representation remain consistent with the representation that Anchor preserved?

Anchor does not determine:

* who owns the Source Artifact;
* whether the Source Artifact is true;
* whether the Source Artifact is certified;
* what the Source Artifact means historically;
* whether a trust conclusion should be drawn from it.

Those responsibilities remain with the appropriate source or Suite institution.

---

# Authority Boundary

Anchor is authoritative for Anchor-owned institutional records and processes, including:

* Anchor Identifiers;
* Integrity References;
* Anchor-owned metadata;
* Anchor Validation;
* Anchor Verification results;
* Anchor lifecycle state;
* Anchor publication state;
* Anchor Corrections; and
* Anchor Versions.

Anchor is **not** authoritative for the referenced Source Artifact.

The Source Institution retains authority over its own canonical object.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

**Connection ≠ Identity.**  
**Reference ≠ Derivation.**  
**Reference ≠ Support.**  
**Reference ≠ Authority Transfer.**

---

# Standards, Schemas, Procedures, and Documentation

Unless otherwise stated, documentation contained within this repository is released under the same repository licensing framework.

This may include:

* Institutional documentation
* Architectural materials
* Anchor standards
* Governance documentation
* Schemas
* Controlled Values
* Validation rules
* Verification procedures
* Lifecycle documentation
* Versioning documentation
* Correction procedures
* Publication procedures
* Maintenance procedures
* Production procedures
* Examples
* Sample records
* Supporting documentation

Licensing these materials does not grant the licensee official Anchor institutional authority.

A third-party implementation may reproduce Anchor methods or structures without thereby becoming Satoshium Anchor.

---

# Canonical Records and Derivative Implementations

The MIT License permits modification, redistribution, forks, and derivative works.

Those permissions do not convert a derivative implementation or independently generated record into an official Satoshium Anchor Integrity Reference.

In particular:

* Reproducing the `ANCH-` identifier format does not create an official Anchor Identifier.
* Reproducing an Integrity Reference schema does not create an official Anchor Integrity Reference.
* Running equivalent validation logic does not create an official Anchor Validation record.
* Recomputing a digest does not create an official Anchor Verification result.
* Publishing a compatible record does not make it part of Anchor's official published Integrity Reference index.

Canonical status depends upon the applicable Anchor institutional process, not upon software licensing alone.

---

# Integrity and Verification Boundary

Anchor preserves integrity context.

It does not certify universal truth.

A successful Anchor Verification result establishes only the governed integrity relationship defined by Anchor's applicable method and representation boundary.

A matching digest or other integrity result does not, by itself, establish:

* truth;
* correctness;
* certification;
* endorsement;
* authorship;
* ownership;
* legal validity;
* trustworthiness; or
* authority over the Source Artifact.

Integrity and authority are distinct.

---

# Validation and Verification

Anchor distinguishes **Validation** from **Verification**.

Validation determines whether an Anchor-owned record satisfies applicable Anchor requirements.

Verification determines whether observed integrity material matches the expected integrity relationship under the applicable Anchor method.

A PASS Validation result does not mean the Source Artifact is true.

A matching Verification result does not transfer authority over the Source Artifact to Anchor.

---

# Source Artifacts and Third-Party Content

Anchor may preserve integrity context for artifacts originating from:

* Atlas;
* Navigator;
* Certifier;
* Registry;
* Chronicle;
* Beacon;
* Attestor;
* external institutions;
* external organizations;
* publications;
* datasets;
* technologies;
* standards; or
* other third-party sources.

Ownership and authority over referenced content remain with their respective owners or source institutions unless expressly transferred through an applicable legal or institutional process.

Inclusion within Anchor does not imply:

* Ownership
* Endorsement
* Sponsorship
* Affiliation
* Derivation
* Support
* Certification
* Trust
* Transfer of authority

Reference does not transfer authority.

---

# Retained Legacy Context

Anchor contains or may preserve historical identity-, claim-, attestation-, reputation-, and trust-related documentation.

Those surfaces are retained only where they remain useful as bounded **integrity-preservation contexts**.

They do not make Anchor the authority for:

* identity;
* claims;
* attestations;
* reputation; or
* trust.

In particular, Attestor remains responsible for its own governed Attestations and Trust Statements.

Anchor may preserve the integrity of an attestation-related or trust-related artifact without inheriting Attestor authority over that artifact or conclusion.

---

# Technology Position

Anchor is implementation-neutral at the institutional level.

The first production Integrity Reference uses:

* canonical JSON;
* RFC 8785 JSON Canonicalization Scheme (JCS); and
* SHA-256 cryptographic digest.

Those implementation choices describe the current production record and do not require future Anchor implementations to depend permanently upon a single technology, algorithm, serialization format, or commitment mechanism.

Open licensing permits alternative implementations while preserving the distinction between an implementation and the official Anchor institutional record.

---

# No Warranty

Consistent with the MIT License, Satoshium Anchor is provided:

> "AS IS", WITHOUT WARRANTY OF ANY KIND.

No representation is made regarding:

* Accuracy
* Completeness
* Reliability
* Fitness for a particular purpose
* Future suitability
* Regulatory compliance
* Operational outcomes
* Legal validity of referenced artifacts
* Truth of referenced artifacts
* Continued availability of external sources
* Long-term suitability of any specific cryptographic algorithm

Users are responsible for evaluating the suitability of Anchor for their specific needs.

---

# Institutional Disclaimer

The existence of an Anchor framework, record, method, validation result, verification result, Integrity Reference, publication state, lifecycle state, or preserved reference should not be interpreted as:

* Legal advice
* Financial advice
* Tax advice
* Regulatory approval
* Government authorization
* Certification of truth
* Authentication of identity
* Proof of ownership
* Determination of trustworthiness
* Endorsement
* Transfer of source authority

Anchor preserves integrity context.

It does not replace the authority of the Source Institution.

---

# Versions, Corrections, and Historical Preservation

Anchor preserves governed Versioning, Correction, Publication, Lifecycle, and Maintenance history for Anchor-owned records.

Licensing does not alter those institutional disciplines:

* Correction is not deletion.
* Correction is not automatically a new Version.
* Supersession is not mutation.
* Source change is distinct from Anchor Correction.
* Historical records should remain historically accurate.
* Candidate production packages remain distinct from published Integrity References.

Later licensed changes to Anchor software or documentation do not retroactively alter the meaning or status of earlier canonical Anchor records.

---

# Production Status

Anchor is operational.

Its first published Integrity Reference is:

`ANCH-2026-0001`

The first production cycle established a governed production path including:

* canonical representation;
* integrity generation;
* Integrity Reference construction;
* Validation;
* Verification;
* Publication Gate review;
* Publication;
* lifecycle evidence; and
* ongoing Maintenance / Reverification.

Future official Integrity References follow the applicable governed Anchor production process.

---

# Long-Term Purpose

Satoshium Anchor is intended to provide an open and durable institutional architecture for integrity preservation across interoperable digital systems.

Open licensing supports that purpose by allowing developers, researchers, organizations, institutions, and communities to study and build upon Anchor's licensed methods and implementations while preserving transparency, interoperability, reproducibility, and independent verification.

The institutional boundary remains constant:

> **Preserve the reference. Preserve the boundary. Preserve the authority.**

---

# Reference

For the legally binding license terms governing this repository, see:

```text
LICENSE
```

located at the root of the repository.

---

# Guiding Statement

> Open licensing permits implementation.
>
> Integrity preserves the relationship.
>
> Authority remains with the source.
>
> Reference does not transfer authority.
>
> Satoshium Anchor is released in that spirit.
