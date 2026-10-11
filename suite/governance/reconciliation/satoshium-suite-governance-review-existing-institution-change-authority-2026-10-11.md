# Satoshium Suite Governance Review — Existing Institution Change Authority

**Date:** October 11, 2026  
**Review:** Satoshium Suite Governance Review  
**Day:** 2 of 4 — Institutional Change, Creation & Constitutional Boundaries  
**Step:** 3 — Determine When an Existing Institution May Change  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record determines when an existing Satoshium Suite institution may:

- expand capabilities;
- narrow capabilities;
- change Procedures;
- add supporting objects;
- change its canonical object;
- change its institutional role.

The governing objective is to allow legitimate institutional evolution without permitting lower-level operational change to silently rewrite Suite architecture.

---

# Governing Principle

> **An institution may evolve freely within its settled role and authority boundary. It may not unilaterally change the constitutional architecture that defines that role, its canonical ownership, or its relationship to the rest of the Suite.**

The core distinction is:

```text
CHANGE WITHIN AUTHORITY
→ institution may govern

CHANGE TO AUTHORITY
→ Suite Governance must govern
```

---

# 1. Expand Capabilities

## Permitted When

An institution may expand capabilities when the expansion:

- remains inside its settled institutional role;
- does not create a new canonical object family;
- does not absorb another institution's responsibility;
- does not create de facto authority over another institution;
- does not make another institution constitutionally dependent on it;
- remains compatible with Suite Standards, Methodology, and Interoperability;
- preserves existing authority boundaries.

Examples:

```text
Beacon adds another discovery mechanism
→ PERMITTED INSTITUTIONAL EVOLUTION

Anchor adds another supported integrity method
→ PERMITTED INSTITUTIONAL EVOLUTION

Certifier adds automation to evidence review
→ PERMITTED INSTITUTIONAL EVOLUTION

Navigator adds a new orchestration capability
→ PERMITTED INSTITUTIONAL EVOLUTION
```

## Requires Suite Review When

Capability expansion would:

- enter another institution's settled domain;
- create a new cross-Suite approval power;
- create a new canonical object family;
- impose a mandatory cross-institution dependency;
- alter constitutional authority.

Examples:

```text
Beacon begins issuing certification decisions
→ NOT unilateral
→ institutional-role / constitutional review required

Navigator becomes mandatory approval gate
for all institutional publication
→ constitutional review required
```

## Determination

```text
Expansion within settled role
→ INSTITUTIONAL AUTHORITY

Expansion that changes role or authority
→ SUITE GOVERNANCE
```

---

# 2. Narrow Capabilities

## Permitted When

An institution may narrow, retire, or suspend a capability when:

- the capability is not itself part of the institution's settled constitutional responsibility;
- canonical responsibilities remain performable;
- no other institution is forced to assume authority;
- no Suite-wide dependency is broken;
- the change does not effectively abandon the institutional role.

Examples:

```text
Registry retires a nonessential presentation feature
→ PERMITTED

Anchor stops supporting one nonrequired verification interface
→ PERMITTED

Beacon retires an obsolete discovery channel
→ PERMITTED
```

## Requires Suite Review When

Narrowing capability would:

- make the institution unable to perform its settled role;
- eliminate a required canonical function;
- transfer responsibility elsewhere;
- create a material cross-Suite dependency problem;
- amount to partial retirement of the institution.

Examples:

```text
Chronicle stops preserving qualifying historical occurrences
→ institutional-role impact
→ Suite review required

Certifier stops making certification determinations
→ constitutional role impact
→ Suite review required
```

## Determination

```text
Capability reduction that preserves institutional purpose
→ INSTITUTIONAL AUTHORITY

Capability reduction that impairs institutional purpose
→ SUITE GOVERNANCE
```

---

# 3. Change Procedures

## Permitted When

An institution may change its Procedures when the change:

- remains inside settled Rules and Policies;
- remains consistent with applicable Suite Standards and Methodology;
- does not alter canonical ownership;
- does not alter another institution's authority;
- does not create constitutional dependency;
- does not convert procedure into new authority.

Examples:

```text
Anchor changes production sequence
→ PERMITTED

Registry changes internal review steps
→ PERMITTED

Attestor changes operational execution order
→ PERMITTED
```

## Escalation Required When

A Procedure change would:

- contradict a binding institutional Rule;
- contradict a Suite Standard;
- create new decision authority;
- transfer authority;
- alter a canonical object boundary;
- create mandatory authority over another institution.

Example:

```text
Navigator Procedure now requires
Navigator approval before Certifier may certify
→ NOT a mere Procedure change
→ constitutional governance issue
```

## Determination

```text
Procedure change within existing authority
→ INSTITUTIONAL AUTHORITY

Procedure change that creates new authority
→ RECLASSIFY TO HIGHER GOVERNANCE LEVEL
```

---

# 4. Add Supporting Objects

## Definition

A **supporting object** is an institution-owned object, record, artifact, metadata structure, or implementation object that assists institutional operation but does not become a distinct Suite-level canonical object.

## Permitted When

An institution may add supporting objects when they:

- remain subordinate to an existing canonical object or institutional function;
- do not claim independent Suite-wide canonical status;
- do not create new constitutional authority;
- do not duplicate another institution's canonical object;
- do not blur source authority;
- do not alter the formal object model of the Suite.

Examples:

```text
Beacon creates supporting Discovery Metadata
→ PERMITTED

Anchor creates verification evidence records
→ PERMITTED

Registry creates internal validation artifacts
→ PERMITTED
```

## Requires Suite Review When

The proposed supporting object:

- is intended to become independently canonical;
- requires a new formal identifier family with independent Suite status;
- acquires its own lifecycle and authority boundary equivalent to a canonical object;
- duplicates another institution's canonical responsibility;
- changes the Suite object model.

Example:

```text
Discovery Metadata is elevated from supporting structure
to a second Beacon canonical object
→ CANONICAL-OBJECT CHANGE
→ Suite review required
```

## Determination

```text
Supporting object
→ INSTITUTIONAL AUTHORITY

New canonical object
→ SUITE GOVERNANCE
```

---

# 5. Change Its Canonical Object

## General Rule

An institution may **not unilaterally change its canonical object architecture**.

Canonical objects are part of the settled Suite architecture and define institutional identity, ownership, interoperability, and authority.

A canonical-object change includes:

- replacing the canonical object;
- adding another canonical object family;
- deleting a canonical object family;
- splitting one canonical object into multiple canonical families;
- merging canonical object families;
- transferring canonical ownership;
- materially redefining the identity boundary of the canonical object.

## Required Governance

```text
Canonical-object change
→ Suite-level architectural review required
```

If ownership moves between institutions:

```text
Canonical-object ownership transfer
→ CONSTITUTIONAL CHANGE
```

## What Does Not Count

The institution may still change:

- schema fields;
- presentation;
- serialization;
- controlled values;
- supporting metadata;
- version structure;
- internal implementation;

provided the same canonical object and authority boundary remain intact.

## Example

```text
Registry changes SREG schema
→ NOT automatically canonical-object change

Registry replaces SREG with a new canonical object family
→ canonical-object change

Registry transfers SREG ownership to Chronicle
→ constitutional change
```

## Determination

```text
Internal canonical-object refinement
→ may remain institutional

Canonical-object architecture change
→ Suite Governance

Canonical ownership transfer
→ Constitutional Governance
```

---

# 6. Change Its Institutional Role

## General Rule

An institution may **not unilaterally change its settled institutional role**.

The role is part of the constitutional allocation of responsibility across the Suite.

Examples of role change:

```text
Anchor
Integrity Preservation
→ Integrity Preservation + Certification

Registry
Canonical Registration / Public Catalog
→ Registration + Source Authority

Beacon
Discovery & Signals
→ Discovery + Verification Authority
```

These are not ordinary institutional evolution.

## Permitted Clarification

An institution may clarify or refine the expression of its role when the change:

- does not expand or narrow the settled responsibility;
- does not alter authority;
- does not alter canonical ownership;
- does not alter Suite membership;
- merely improves precision of existing language.

Example:

```text
Navigator
"Workflow Definition / Orchestration"
clarified in documentation
without authority change
→ NOT institutional-role change
```

## Required Governance

```text
Actual role change
→ Suite-level constitutional review
```

A role reassignment, merger, split, or transfer of responsibility is presumptively constitutional.

## Determination

```text
Role clarification
→ documentation / governance clarification

Role expansion or narrowing
→ Suite Governance

Role transfer or reallocation
→ Constitutional Change
```

---

# Decision Matrix

| Proposed Change | Institution May Act Alone? | Suite Review Required? | Constitutional? |
|---|---:|---:|---:|
| Expand capability within settled role | Yes | No | No |
| Expand into another institution's domain | No | Yes | Usually |
| Narrow nonessential capability | Yes | No | No |
| Narrow capability so role cannot be performed | No | Yes | Likely |
| Change Procedure within existing authority | Yes | No | No |
| Procedure creates new authority | No | Yes | Possibly |
| Add supporting object | Yes | No | No |
| Elevate supporting object to canonical | No | Yes | Possibly |
| Refine canonical-object schema | Yes | Sometimes | No, if identity unchanged |
| Replace/add/remove canonical object family | No | Yes | Material |
| Transfer canonical ownership | No | Yes | Yes |
| Clarify role wording | Yes | Sometimes | No |
| Expand/narrow settled institutional role | No | Yes | Yes or presumptively yes |
| Transfer role to another institution | No | Yes | Yes |

---

# Capability Expansion Test

Before an institution expands a capability, ask:

```text
1. Is the capability clearly inside the settled role?
2. Does it preserve canonical ownership?
3. Does it avoid absorbing another institution's authority?
4. Does it avoid becoming a mandatory approval gate?
5. Does it avoid creating a new canonical object?
6. Does it remain compatible with Suite Standards and Methodology?
```

If all are YES:

```text
INSTITUTION MAY PROCEED
```

If any are NO:

```text
ESCALATE
```

---

# Capability Narrowing Test

Before narrowing a capability, ask:

```text
1. Can the institution still perform its settled role?
2. Can it still maintain its canonical objects?
3. Does another institution avoid being forced to absorb the function?
4. Are Suite dependencies preserved?
5. Is this capability nonconstitutional?
```

If all are YES:

```text
INSTITUTION MAY PROCEED
```

If any are NO:

```text
ESCALATE
```

---

# Canonical Change Test

Before changing an object, ask:

```text
Does the object remain the same canonical object?

Does ownership remain unchanged?

Does identity remain continuous?

Does the change preserve the same constitutional responsibility?
```

If YES:

```text
possible institutional refinement
```

If NO:

```text
canonical-object change
→ Suite review required
```

---

# Role Change Test

Ask:

```text
Does this change what the institution exists to do?
```

If NO:

```text
institutional evolution
```

If YES:

```text
institutional-role change
→ constitutional review
```

---

# Governing Doctrine

> **Existing institutions may evolve extensively inside their settled constitutional boundaries. They may not unilaterally redefine those boundaries.**

Expanded:

> **Capability, Procedure, implementation, and supporting-object changes remain institution-governed when they preserve settled role, canonical ownership, authority, and institutional independence. Changes to canonical architecture or institutional role belong to Suite Governance, and transfers of canonical ownership or foundational responsibility are constitutional changes.**

---

## Final Disposition

```text
Expand capabilities
→ PERMITTED WITHIN SETTLED ROLE

Narrow capabilities
→ PERMITTED IF SETTLED ROLE REMAINS PERFORMABLE

Change Procedures
→ PERMITTED WITHIN EXISTING RULES / AUTHORITY

Add supporting objects
→ PERMITTED IF NONCANONICAL

Change canonical object
→ SUITE REVIEW REQUIRED

Transfer canonical ownership
→ CONSTITUTIONAL CHANGE

Change institutional role
→ SUITE / CONSTITUTIONAL REVIEW REQUIRED

Existing Institution Change Authority
→ COMPLETE — APPROVED
```

# EXISTING INSTITUTION CHANGE AUTHORITY — COMPLETE — APPROVED
