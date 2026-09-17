# Satoshium Attestor — Records

## Path
`/attestor/records/`

## Purpose
This directory documents foundational **reference profiles** through which Attestor may relate governed source objects to Attestations, evaluation, and Trust Statements.

It does **not** establish a second Attestor record system.

**Attestor → Trust Statement**

## Governing Principle
> **Reference does not transfer authority.**

A referenced source object remains governed by its originating institution or external authority.

## Reference Profiles
- `atlas.md` — Atlas Authoritative Intelligence
- `certifier.md` — Certifier Certification Package
- `registry.md` — Satoshium Registry Record
- `chronicle.md` — Chronicle Entry
- `anchor.md` — Anchor Integrity Reference
- `beacon.md` — Beacon Discovery Signal / Discovery Metadata
- `external.md` — eligible external governed sources

## Foundational Model
`Source Object → Governed Reference → Attestation / Evaluation → Trust Statement`

The source object does not become an Attestor-owned record merely because Attestor references it.

## Architectural Status
These documents are foundational reference profiles pending whole-foundation review and advanced architecture. They do not yet establish independent Attestor Record identifiers, record classes, machine schemas, publication states, lifecycle states, or automatic cross-institutional actions.

## Reconciliation Note
The June-era documents described Attestor as maintaining broad trust records, reputation records, trust signals, identity-linked records, and copies or derivatives of other institutions' records. Those assumptions are not carried forward.

The whole-foundation review should decide whether the directory name **Records** remains appropriate or whether the architecture should ultimately call these **Reference Profiles**.
