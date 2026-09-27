# Satoshium Suite Reconciliation — Authority Terminology Reconciliation

**Date:** September 26, 2026  
**Phase:** II — Objects, Terminology & Semantics  
**Status:** COMPLETE — APPROVED

## Purpose

This record documents the Suite-wide reconciliation of authority terminology conducted during the September 26, 2026 phase of the Satoshium Suite Reconciliation.

The review preserves two governing principles:

> **CONNECTION ≠ IDENTITY**

> **REFERENCE DOES NOT TRANSFER AUTHORITY**

The purpose of this record is to ensure that cross-institution relationships, references, derivations, preservation, discovery, evaluation, publication, coordination, and provenance do not collapse distinct canonical objects or transfer institutional authority beyond the domain in which that authority is assigned.

The governing architectural rule is:

> **Institutional authority belongs to the institution that governs the canonical object, process, or decision domain.**

---

# 1. Authority

## Controlled Definition

**Authority** means institutionally assigned responsibility to govern a defined object, process, decision, or domain.

Authority may include responsibility for:

- canonical object ownership;
- lifecycle governance;
- validation or evaluation within institutional scope;
- institutional decision-making;
- correction and versioning rules;
- publication governance;
- authoritative interpretation of an institution’s own canonical objects.

Authority is domain-specific.

## Suite Institutional Authority Domains

| Institution | Authority Domain |
|---|---|
| Atlas | Jurisdiction Intelligence Packages |
| Navigator | Navigator Workflow Definitions and Workflow Orchestration |
| Certifier | Certification Packages and Certification Decisions |
| Registry | Satoshium Registry Entries |
| Chronicle | Chronicle Entries and Historical Preservation |
| Anchor | Integrity References and Integrity Preservation |
| Beacon | Discovery Signals and Discovery Metadata |
| Attestor | Attestations, Rule-Constrained Evaluation, and Trust Statements |

Institutional authority over one object does not create authority over another institution’s source object.

---

# 2. Connection ≠ Identity

A relationship between two canonical objects does not collapse them into one object.

Example:

```text
SREG
    references
Certification Package
```

This establishes a relationship.

It does not establish identity.

Therefore:

> **SREG ≠ Certification Package**

Likewise:

```text
Trust Statement
    derived-from
Attestation
```

does not mean:

> **Trust Statement = Attestation**

And:

```text
Chronicle Entry
    references
Integrity Reference
```

does not mean:

> **Chronicle Entry = Integrity Reference**

The governing rule is:

> **CONNECTION ≠ IDENTITY**

This remains true regardless of the importance, strength, or permanence of the relationship.

---

# 3. Reference Does Not Transfer Authority

A reference establishes traceability or connection.

It does not transfer institutional authority from the referenced object to the referencing object.

Example:

```text
SREG
    references
SC-CERT-2026-0001
```

The Registry Entry may identify and expose the Certification Package.

Registry does not thereby gain:

- certification authority;
- control over the Certification Decision;
- authority to alter the Certification Package;
- authority to reinterpret the certification outcome.

Therefore:

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

This is a governing Suite-wide authority rule.

---

# 4. Registration Does Not Transfer Authority

Registry governs the Satoshium Registry Entry.

The authoritative source record remains governed by the originating institution.

Example:

```text
Certifier
    owns
Certification Package

Registry
    owns
SREG
```

The SREG may reference the Certification Package, but:

```text
Registry authority
≠
Certification authority
```

Therefore:

> **REGISTRATION PRESERVES CANONICAL REGISTRATION AND DISCOVERABILITY; IT DOES NOT TRANSFER SOURCE AUTHORITY.**

---

# 5. Historical Preservation Does Not Transfer Source Authority

Chronicle may preserve a historical representation of an event or institutional action.

Chronicle is authoritative for:

- the Chronicle Entry;
- its historical structure;
- its preservation lifecycle;
- its historical representation.

Chronicle is not authoritative for the underlying canonical source object owned by another institution.

Example:

```text
Chronicle Entry
    records
Certification Event
```

Chronicle remains authoritative for the historical record it created.

Certifier remains authoritative for the certification itself.

Therefore:

> **HISTORICAL AUTHORITY ≠ SOURCE AUTHORITY**

---

# 6. Integrity Preservation Does Not Transfer Source Authority

Anchor may create an Integrity Reference for an artifact owned by another institution.

Anchor is authoritative for:

- the Integrity Reference;
- integrity evidence;
- representation boundary;
- integrity verification within Anchor’s scope.

Anchor does not become authoritative for the content or substantive meaning of the source artifact.

Therefore:

> **INTEGRITY AUTHORITY ≠ CONTENT AUTHORITY**

and:

> **ANCHORING DOES NOT TRANSFER SOURCE AUTHORITY.**

---

# 7. Discovery Does Not Transfer Authority

Beacon may discover, index, surface, or signal another institution’s object.

Beacon is authoritative for the Discovery Signal it creates.

Beacon is not authoritative for the source object itself.

Example:

```text
Beacon Discovery Signal
    references
Certification Package
```

Beacon owns the Discovery Signal.

Certifier still owns the Certification Package.

Therefore:

> **DISCOVERY AUTHORITY ≠ SOURCE AUTHORITY**

---

# 8. Derivation Does Not Transfer Authority

A downstream object may derive from another object.

This lineage does not cause the downstream institution to inherit the upstream institution’s authority.

Example:

```text
Trust Statement
    derived-from
Attestation
```

Within Attestor, both objects remain governed by Attestor.

But if Attestor relies on canonical objects from Atlas, Certifier, Registry, Chronicle, Anchor, or Beacon, those source objects remain governed by their originating institutions.

Therefore:

> **DERIVATION DOES NOT TRANSFER SOURCE AUTHORITY.**

---

# 9. Support Does Not Transfer Authority

Evidence may support a conclusion without transferring authority over the conclusion.

Likewise, a conclusion may rely on evidence without becoming authoritative for the evidence source.

Example:

```text
Source Evidence
    supports
Attestation
```

The source remains governed by its source authority.

Attestor remains authoritative only for its own Attestation, Evaluation, and Trust Statement.

Therefore:

> **SUPPORT DOES NOT TRANSFER AUTHORITY.**

---

# 10. Evaluation Does Not Transfer Authority

Attestor may evaluate an assertion concerning objects from other institutions.

That does not make Attestor authoritative for those source objects.

Attestor is authoritative for:

- Evaluation Eligibility;
- Rule-Constrained Evaluation;
- Evaluation Outcome;
- Trust Statement.

Attestor is not authoritative for:

- Certifier’s Certification Decision;
- Registry’s SREG;
- Chronicle’s historical record;
- Anchor’s Integrity Reference;
- Beacon’s Discovery Signal;
- Atlas’s Jurisdiction Intelligence Package.

Therefore:

> **EVALUATION AUTHORITY ≠ SOURCE AUTHORITY**

---

# 11. Coordination Does Not Transfer Authority

Navigator may coordinate workflow across multiple institutions.

That coordination does not subordinate those institutions or absorb their authority.

Example:

```text
Navigator Workflow
    coordinates
Certifier
Registry
Chronicle
Anchor
Beacon
Attestor
```

Navigator governs:

- the Workflow Definition;
- the orchestration logic;
- workflow state within Navigator’s scope.

Each participating institution remains authoritative for its own actions, determinations, and canonical objects.

Therefore:

> **COORDINATION DOES NOT TRANSFER AUTHORITY.**

---

# 12. Publication Does Not Transfer Authority

Publication changes accessibility.

It does not change ownership.

A published canonical object remains governed by the institution that created and owns it.

Therefore:

> **PUBLICATION DOES NOT TRANSFER AUTHORITY.**

Rendering or displaying an object on another institutional surface does not transfer source authority.

---

# 13. Provenance Does Not Transfer Authority

Provenance identifies origin and lineage.

It may help locate the authoritative source.

It does not itself confer authority.

Therefore:

> **PROVENANCE MAY IDENTIFY AUTHORITY, BUT IT DOES NOT CREATE OR TRANSFER AUTHORITY.**

---

# 14. Representation Does Not Transfer Authority

An institution may render, display, serialize, or otherwise represent another institution’s object.

That representation does not become the authoritative source object merely because it is visible or operationally useful.

Example:

```text
Public Representation
    represents
Source Object
```

The representation may be governed locally.

The source object remains governed by its originating institution.

Therefore:

> **REPRESENTATION ≠ SOURCE IDENTITY**

and:

> **REPRESENTATION DOES NOT TRANSFER AUTHORITY.**

---

# 15. Cross-Institution Authority Model

The preferred Suite model is:

```text
Institution A
    owns
Canonical Object A

Institution B
    references / derives-from / supports / evaluates / preserves / discovers
Canonical Object A

Institution B
    owns
Canonical Object B
```

The connection between Institution A and Institution B does not alter the ownership or identity of either canonical object.

Thus:

```text
Connection
    ≠ Identity
    ≠ Ownership
    ≠ Authority Transfer
```

---

# 16. Authority vs Relationship

Relationship terminology describes how objects are connected.

Authority terminology describes who governs them.

These are separate semantic dimensions.

Example:

```text
relationship: references
source_authority: Certifier
referencing_authority: Registry
```

Both facts may coexist.

The relationship does not override authority metadata.

---

# 17. Authority vs Status

Authority remains separate from lifecycle, publication, validation, conformance, and operational status.

An object may become:

- Active;
- Superseded;
- Withdrawn;
- Archived;
- Published;
- Unpublished;

without changing which institution governs it.

Therefore:

> **STATUS CHANGE ≠ AUTHORITY CHANGE**

unless an explicit governance mechanism formally reassigns responsibility.

---

# 18. Authority vs Version

Versioning does not transfer authority.

Example:

```text
TRST-2026-0001
V1.0 → V1.1
```

Attestor remains authoritative for the Trust Statement.

Likewise, a superseding object remains governed by the institution that owns that canonical object class.

Therefore:

> **VERSIONING DOES NOT TRANSFER AUTHORITY.**

---

# 19. Authority vs Identifier

Identifiers establish canonical identity within an institutional namespace.

They do not independently create authority.

Example:

```text
SC-CERT-2026-0001
```

The identifier reflects Certifier’s namespace.

Authority comes from the institutional architecture and governance model, not merely from the identifier string.

Therefore:

> **IDENTIFIER ≠ AUTHORITY**

and:

> **MATCHING IDENTIFIERS ACROSS INSTITUTIONS DO NOT ESTABLISH SHARED AUTHORITY.**

---

# 20. Prohibited Authority Implications

The Suite must reject the following implied equivalences:

- reference = authority transfer
- connection = identity
- registration = source ownership
- preservation = source ownership
- anchoring = source ownership
- discovery = source ownership
- derivation = source authority
- support = source ownership
- evaluation = source ownership
- coordination = superior authority
- publication = authority
- provenance = authority
- representation = source identity
- status = authority
- version = authority
- identifier = authority

---

# 21. Suite-Wide Authority Rules

The Authority Terminology Reconciliation establishes the following rules:

1. Authority is assigned by institutional domain.
2. Canonical object ownership remains with the institution that governs the object class.
3. **Connection ≠ Identity.**
4. **Reference does not transfer authority.**
5. Registration does not transfer source authority.
6. Historical preservation does not transfer source authority.
7. Integrity preservation does not transfer source authority.
8. Discovery does not transfer source authority.
9. Derivation does not transfer source authority.
10. Support does not transfer source authority.
11. Evaluation does not transfer source authority.
12. Coordination does not transfer institutional authority.
13. Publication does not transfer authority.
14. Provenance may identify authority but does not create or transfer it.
15. Representation does not replace source identity.
16. Status changes do not inherently change authority.
17. Versioning does not transfer authority.
18. Identifiers do not independently establish authority.
19. Cross-institution relationships preserve separate canonical identities.
20. Authority remains bounded to the institutionally assigned domain.

---

# Governing Formulation

> **CONNECTION ≠ IDENTITY.**

> **REFERENCE DOES NOT TRANSFER AUTHORITY.**

And more broadly:

> **RELATIONSHIPS MAY CONNECT INSTITUTIONS, BUT THEY DO NOT COLLAPSE INSTITUTIONAL OWNERSHIP OR AUTHORITY.**

---

# Final Disposition

**Authority Terminology Reconciliation — COMPLETE — APPROVED**

This record should govern future cross-institution references, relationship metadata, derivation chains, registration, preservation, integrity handling, discovery, evaluation, orchestration, publication, provenance, and documentation conformance across the Satoshium Suite.
