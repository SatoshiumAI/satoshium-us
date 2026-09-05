# Certification Signals

## Purpose

Certification Signals are Beacon-owned **Discovery Signals** that identify certification-related information as potentially relevant for discovery.

Beacon does not certify.

Beacon publishes Discovery Signals and discovery metadata that may reference Certification Packages, certification status, evidence references, SREG records, and related information while preserving the authority of the originating institution.

Certifier retains certification and verification authority.

**Reference does not transfer authority.**

---

## Core Distinction

Certification Signals preserve a clear separation between institutional responsibilities:

* **Certifier → Certification Package**
* **Registry → SREG**
* **Beacon → Discovery Signal / Metadata**

Certification Packages and certification status belong to Certifier.

SREG records and Registry lifecycle status belong to Registry.

Certification Signals and their discovery metadata belong to Beacon.

---

## What Is a Certification Signal?

A Certification Signal is a Beacon Discovery Signal associated with certification-related information.

It may direct users, applications, or workflows toward:

* Certification Packages
* Certification status
* Evidence references
* Verification metadata
* SREG records
* Certification-related events
* Relevant source material
* Related canonical objects

A Certification Signal identifies discovered relevance.

It does not independently create the certification state it reports.

---

## Signal Types

Beacon may publish certification-related Discovery Signals corresponding to authoritative certification states or changes.

Initial signal types include:

* **Certified**
* **Expired**
* **Revoked**
* **Updated**
* **Pending**

These signal types describe what Beacon has discovered from an authoritative source.

They do not create the underlying state.

---

## Certified

A **Certified** signal indicates that Beacon has observed an authoritative Certifier source showing the referenced subject or Certification Package in a certified state.

Beacon may signal that state.

Certifier remains authoritative for it.

---

## Expired

An **Expired** signal indicates that Beacon has observed an authoritative Certifier source showing the referenced certification in an expired state.

The signal should preserve the source and relevant certification reference so the authoritative state can be reviewed.

---

## Revoked

A **Revoked** signal indicates that Beacon has observed an authoritative Certifier source showing the referenced certification in a revoked, withdrawn, or otherwise invalidated state.

Beacon reports the discovered state.

It does not perform the revocation.

---

## Updated

An **Updated** signal indicates that Beacon has observed a change in certification-related information, metadata, references, or authoritative status that may warrant renewed attention.

An Updated signal should preserve sufficient context to identify what changed and where the authoritative information can be reviewed.

---

## Pending

A **Pending** signal indicates that Beacon has observed an authoritative certification source showing a certification process or review that has not yet reached a final certification state.

Beacon does not determine the eventual outcome.

---

## Future Certification Signals

Future certification-related signals may include states such as:

* Renewed
* Suspended
* Superseded
* Challenged
* Corrected

Additional signal types should correspond to authoritative Certifier lifecycle semantics or other governed certification information.

Integrity-related states remain within Anchor authority.

Trust-related states remain within Attestor authority.

Beacon may discover those relationships without redefining them as certification authority.

---

## What a Certification Signal Contains

A Certification Signal should preserve enough discovery context to identify the relevant certification information and trace it back to its authoritative source.

Conceptual attributes may include:

* Discovery Signal ID
* Signal type
* Subject
* Source institution
* Certification Package ID
* Related SREG ID
* Related canonical-object references
* Provenance
* Public reference
* Discovery context
* Authoritative status observed
* Signal date
* Last observed
* Version
* Supersession information
* Relationships

Specific operational schemas may evolve as Beacon advances toward production.

---

## Relationship to Certifier

Certifier owns **Certification Packages** and certification/verification authority.

Certifier remains authoritative for:

* Certification outcomes
* Certification status
* Evidence review
* Scoring
* Verification
* Certification lifecycle
* Certification artifacts

Beacon may discover and publish a Certification Signal reflecting an authoritative Certifier state.

```text
Beacon may publish a Certified signal.
Certifier determines and records the authoritative certification state.
```

---

## Relationship to Registry

Registry owns **SREG** records and their lifecycle.

A Certification Signal may reference an SREG record when that record is relevant to certification discovery.

Beacon does not duplicate or modify the Registry record.

```text
Beacon may reference an SREG record.
Registry retains authority for SREG.
```

---

## Relationship to Chronicle

A certification-related discovery may have historical significance.

Beacon may reference a **Chronicle Entry** or related historical context when relevant.

Chronicle remains authoritative for its historical record.

A Certification Signal does not become a Chronicle Entry merely because it identifies an event or change.

---

## Relationship to Anchor

Certification-related discovery may reference an **Integrity Reference** maintained by Anchor.

Beacon may signal the relevance of that relationship.

Anchor remains authoritative for its Integrity References and integrity-preservation function.

Certification status and integrity remain distinct institutional responsibilities.

---

## Relationship to Attestor

Certification-related discovery may also relate to an Attestor **Trust Statement**.

Beacon may surface that relationship as discovery metadata or through an appropriate Discovery Signal.

Attestor remains authoritative for the Trust Statement.

Certification does not automatically establish trust, and discovery does not determine either.

---

## Relationship to Navigator

Navigator owns **Workflow Definition / Orchestration**.

A Navigator-defined workflow may require Beacon to discover certification information or monitor relevant certification states.

Beacon may return:

* Certification Signals
* Discovery metadata
* Certification Package references
* SREG references
* Supporting source references
* Related results

Navigator orchestrates.

Beacon discovers and signals.

Certifier retains certification authority.

---

## Certification Signal Authority Boundary

Beacon owns the Certification Signal as a Discovery Signal and owns its discovery metadata.

Certifier remains authoritative for the Certification Package and certification state being referenced.

Registry remains authoritative for any referenced SREG record.

Other referenced canonical objects remain under the authority of their originating institutions.

```text
The signal may reflect an authoritative state.
It does not independently create that state.
```

**Reference does not transfer authority.**

---

## Signal Interpretation

Certification Signals are indicators, not independent certification conclusions.

Users, systems, and workflows should interpret a Certification Signal by following its references to the authoritative:

* Certification Package
* Certifier status
* SREG record
* Supporting evidence
* Related canonical object
* Source information

A signal helps something be found.

It does not replace the canonical object it references.

---

## Canonical Suite Context

Certification Signals operate within the broader Suite institutional model:

* **Atlas → Authoritative Intelligence**
* **Navigator → Workflow Definition / Orchestration**
* **Beacon → Discovery Signal / Metadata**
* **Certifier → Certification Package**
* **Registry → SREG**
* **Chronicle → Chronicle Entry**
* **Anchor → Integrity Reference**
* **Attestor → Trust Statement**

Interoperability connects these responsibilities without transferring authority between institutions.

---

## Signal Principles

### Attribution

The authoritative source should remain identifiable.

### Provenance

The origin and discovery context of certification-related information should be preserved.

### Traceability

Users and systems should be able to follow the signal back to the authoritative source or canonical object.

### Stable References

Certification Package IDs, SREG IDs, and other canonical identifiers should be preserved when available.

### State Fidelity

A Certification Signal should reflect the authoritative state observed rather than inventing or redefining that state.

### Neutrality

A signal should not imply endorsement or conclusions beyond the information supported by its authoritative reference.

### Authority Preservation

Beacon does not acquire certification authority by publishing a Certification Signal.

---

## Signal Philosophy

Beacon makes certification-related information discoverable without becoming the certification authority.

Its role is to:

```text
Discover the certification information.
Publish the signal.
Preserve the reference.
Retain the provenance.
Keep Certifier authoritative.
```

A signal does not decide.

It points.

---

## Status

Beacon Certification Signal architecture is undergoing Suite alignment and production preparation ahead of its originally planned November 2026 development window.

This document establishes the governing conceptual model for Certification Signals. Operational signal schemas, lifecycle mappings, observation rules, update behavior, workflow interfaces, and interoperability mechanisms may continue to evolve while remaining aligned with Satoshium Suite Standards, Methodology, Interoperability, and Status conventions.

Beacon should not be considered operational solely because Certification Signal documentation or architecture is complete. Operational status requires the architecture to be proven through actual institutional use.
