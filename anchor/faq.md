# Satoshium Anchor — Frequently Asked Questions

## What is Satoshium Anchor?

Satoshium Anchor is the Satoshium Suite institution responsible for preserving durable **Integrity References** for authoritative artifacts and records.

Anchor records cryptographic, temporal, representation, and verification context so the integrity of a referenced representation can be reviewed later.

Anchor does not assume authority over the source artifact itself.

## What is Anchor's canonical object?

Anchor's canonical object is the:

**Integrity Reference**

An Integrity Reference preserves the information required to evaluate whether a later observed representation remains consistent with the representation Anchor preserved.

## Is Anchor an identity layer?

No.

Earlier Anchor development explored identity, claims, attestations, reputation, and trust as central concepts.

The operational Anchor institution is now specifically responsible for **integrity preservation**.

Identity-, claim-, attestation-, reputation-, and trust-related artifacts may be anchored, but Anchor does not become the authority for those concepts.

## Does Anchor create identities?

No.

Anchor may preserve the integrity of identity-related artifacts, but it does not create legal identities, government identities, official credentials, or identity authority.

## Does Anchor determine truth?

No.

Anchor determines neither truth nor meaning.

It preserves integrity context for a defined representation.

A successful integrity Verification means the observed representation matches the expected integrity evidence under the governed Anchor process.

It does not prove that the underlying source claim is true.

## Does Anchor certify artifacts?

No.

Certification belongs to Certifier.

Anchor may preserve the integrity of a certified artifact, but it does not inherit certification authority.

For example:

```text
Certifier
→ authoritative for the Certification Package / certified record

Anchor
→ authoritative for the Integrity Reference
```

Reference does not transfer authority.

## What problem does Anchor solve?

Digital records can change, disappear, be replaced, or become difficult to compare over time.

Anchor creates a durable integrity relationship between:

1. an authoritative source artifact;
2. a defined canonical representation;
3. integrity material derived from that representation;
4. a governed Integrity Reference.

That relationship supports later independent integrity review.

## What is a Canonical Representation?

A Canonical Representation is the specifically defined representation of a source artifact used for integrity generation.

Anchor does not hash an undefined idea of a document.

It preserves integrity against a defined representation boundary.

## What is an Integrity Value?

An Integrity Value is cryptographic or other governed integrity material generated from the defined Canonical Representation.

For `ANCH-2026-0001`, the current implementation uses SHA-256 over RFC 8785 JCS canonical JSON.

## What is Verification?

Verification compares expected integrity evidence with observed or reconstructed evidence.

Verification answers whether the integrity relationship still matches.

Verification does not transfer source authority to Anchor.

## What is Validation?

Validation evaluates whether an Integrity Reference satisfies Anchor's governed institutional requirements.

Anchor's production process currently uses formal PASS/FAIL Validation.

Validation and Verification are related but distinct.

## What is the difference between Validation and Verification?

In simplified form:

```text
Validation
→ Does the Anchor record satisfy institutional requirements?

Verification
→ Does the integrity evidence match?
```

Both are required parts of the governed production path.

## What is ANCH-2026-0001?

`ANCH-2026-0001` is the first published Satoshium Anchor Integrity Reference.

Its source artifact is:

`SCRD-SC-CERT-2026-0001`

The record completed:

- Stage A Validation — PASS
- Initial Verification — match
- Stage B Validation — PASS
- Publication Gate — APPROVED
- Publication — COMPLETE

Its lifecycle state is active and its publication state is published.

## What is the difference between Anchored Items and Integrity References?

Anchor maintains two distinct operational indexes:

```text
/anchor/anchored-items/
→ production packages, including unpublished candidates

/anchor/integrity-references/
→ published Integrity References only
```

The published Integrity References index is not a workspace or candidate queue.

## Does publication transfer authority over the Source Artifact?

No.

Publication makes Anchor authoritative for the published Integrity Reference and Anchor-owned metadata.

The Source Institution remains authoritative for the referenced Source Artifact.

## How does Anchor relate to Certifier?

Certifier performs certification.

Anchor preserves integrity references.

A Certifier artifact may become the source artifact for an Anchor Integrity Reference, but the institutions retain separate authority.

## How does Anchor relate to Registry?

Registry owns Satoshium Registry Records.

Anchor may preserve integrity context for Registry-owned records.

Anchor does not become the Registry authority.

## How does Anchor relate to Chronicle?

Chronicle owns Chronicle Entries and historical preservation.

Anchor may preserve the integrity of Chronicle artifacts.

Anchor does not determine historical interpretation.

## How does Anchor relate to Attestor?

Attestor owns Attestations, Rule-Constrained Evaluation, and Trust Statements.

Anchor may preserve integrity context for attestation or trust artifacts.

Anchor does not make the attestation or trust determination.

## How does Anchor relate to Beacon?

Beacon owns Discovery Signals and Discovery Metadata.

Anchor may preserve integrity context for Beacon artifacts.

Anchor does not become the discovery authority.

## How does Anchor relate to Atlas?

Atlas owns authoritative intelligence within its institutional domain.

Anchor may preserve integrity references for Atlas artifacts.

Anchor does not inherit Atlas authority.

## How does Anchor relate to Navigator?

Navigator defines and orchestrates workflows.

Anchor may participate in a Navigator-defined workflow or preserve workflow-related artifacts.

Navigator orchestration does not transfer Anchor authority, and Anchor integrity operations do not transfer Navigator authority.

## Does Anchor use blockchain technology?

Anchor is institutionally implementation-neutral.

No blockchain is required by the current Anchor architecture.

The present production implementation uses canonical JSON, RFC 8785 JCS, and SHA-256.

Future commitment mechanisms may be added through governed architecture without changing Anchor's core authority boundary.

## Does Anchor manage reputation?

No.

Anchor may preserve the integrity of reputation-related artifacts.

It does not calculate reputation, assign reputation authority, or determine reputation truth.

## Does Anchor determine trust?

No.

Trust judgments and Trust Statements remain outside Anchor's authority.

Anchor may preserve the integrity of trust-related artifacts without becoming a trust authority.

## Is Anchor operational?

Yes.

Anchor is operational.

Its first full end-to-end production cycle is complete and its first Integrity Reference, `ANCH-2026-0001`, is published and active.

## What happens after publication?

Published Integrity References enter maintenance.

Post-publication operations may include:

- Source-link health review;
- Reverification;
- algorithm or key-health review;
- external commitment review;
- Corrections;
- new Versions;
- long-term preservation.

## Can an Anchor record be corrected?

Yes.

Anchor distinguishes:

- Source changes;
- Anchor-owned errors;
- Corrections;
- Versions;
- superseding records.

The governing principle is:

> **Correct forward. Preserve backward.**

## Where can I learn more?

See:

- `/anchor/purpose/`
- `/anchor/definitions/`
- `/anchor/integrity-preservation/`
- `/anchor/anchoring-process/`
- `/anchor/integration/`
- `/anchor/standards/`
- `/anchor/governance/`
- `/anchor/identifiers/`
- `/anchor/controlled-values/`
- `/anchor/relationships/`
- `/anchor/provenance/`
- `/anchor/schemas/`
- `/anchor/verification/`
- `/anchor/validation/`
- `/anchor/lifecycle/`
- `/anchor/versioning/`
- `/anchor/corrections/`
- `/anchor/publication/`
- `/anchor/maintenance/`
- `/anchor/procedures/`
- `/anchor/anchored-items/`
- `/anchor/integrity-references/`
- `/anchor/status/`

## Guiding Principle

> **Preserve the reference. Preserve the boundary. Preserve the authority.**
