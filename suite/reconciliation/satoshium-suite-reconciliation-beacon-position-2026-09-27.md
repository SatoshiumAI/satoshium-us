# Satoshium Suite Reconciliation — Beacon Position

**Date:** September 27, 2026  
**Phase:** Phase III — Whole-Suite Architecture  
**Decision Class:** RECONCILE  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record reconciles Beacon's position within the mature Satoshium Suite.

The purpose is to ensure that Beacon's role as:

> **Discovery & Signals**

is not confused with:

- verification;
- certification;
- registration;
- historical preservation;
- integrity authority;
- trust determination;
- or source ownership.

The governing principle is:

> **Beacon discovers and signals relevant conditions, objects, or changes. It does not verify, certify, register, or determine trust merely by discovering them.**

---

# Formal Role

Beacon's reconciled institutional role is:

> **Discovery & Signals**

Its canonical object is:

> **Discovery Signal**

Its governed supporting layer is:

> **Discovery Metadata**

The essential model is:

```text
Relevant condition / object / change
        ↓
Observation
        ↓
Identification
        ↓
Relevance assessment
        ↓
Discovery Signal
```

Beacon's authority begins and ends with governed discovery and signaling.

---

# Discovery ≠ Verification

Beacon may observe something and establish provenance sufficient to create a Discovery Signal.

That does not mean Beacon has substantively verified the source in the sense used by other institutions.

For example:

```text
Beacon observes:
SC-CERT-2026-0001 exists and is published
```

Beacon may create a Discovery Signal based on that observation.

It does not thereby independently verify the certification evidence or re-perform Certifier review.

Therefore:

> **Discovery ≠ Verification**

And:

> **Observed ≠ Verified**

unless Beacon has a separately defined verification process for a specific discovery field.

---

# Provenance Traceability ≠ Substantive Verification

Beacon may establish:

- source location;
- source identity;
- direct or indirect provenance;
- observation time;
- source reference.

That establishes discovery traceability.

It does not prove every substantive claim made by the source.

Therefore:

> **Provenance traceability ≠ substantive verification**

Beacon may accurately state:

> **This signal was derived from this observed source.**

without asserting:

> **Beacon independently proved the source's substantive conclusion.**

---

# Discovery ≠ Certification

Certifier owns:

> **Operational Certification**

and creates:

> **Certification Package**

Beacon may discover a certification.

For example:

```text
SC-CERT-2026-0001
        ↓ observed by
Beacon
        ↓
BEAC-2026-0001
```

But:

```text
BEAC-2026-0001
≠
SC-CERT-2026-0001
```

And:

> **Beacon does not certify the subject merely because it signals the certification.**

Therefore:

> **Discovery Signal ≠ Certification Package**

And:

> **Discovery ≠ Certification**

---

# Certification Signal Does Not Create Certification Authority

Beacon may classify a Discovery Signal as:

```text
Signal Type: Certification
```

That means the discovery concerns a certification-related matter.

It does not mean Beacon created or approved the certification.

Therefore:

> **Certification Signal = Discovery Signal category**

not:

> **new certification object**

and not:

> **Beacon certification authority**

---

# Discovery ≠ Registration

Registry owns:

> **Canonical Registration / Public Catalog**

and creates:

> **Satoshium Registry Entry**

Beacon may discover:

- a source object;
- a Registry Entry;
- a new registration;
- a change in Registry state.

But the Discovery Signal does not register the object.

Therefore:

> **Discovery ≠ Registration**

And:

> **Discovery Signal ≠ SREG**

A signal may reference a SREG.

It does not become one.

---

# Beacon Does Not Allocate Registry Identity

Even if a Beacon workflow notices an unregistered object, Beacon does not automatically:

- allocate SREG identity;
- determine Registry Record Type;
- establish Registry lifecycle;
- publish Registry catalog state.

Those remain Registry functions.

Therefore:

> **Discovery of a registrable object ≠ registration of that object.**

---

# Discovery ≠ Trust Determination

This is the most important boundary.

Attestor owns:

> **Governed Attestation & Rule-Constrained Evaluation**

and creates:

- Attestations;
- Trust Statements.

Beacon may discover something relevant to trust-related evaluation.

But:

> **Beacon does not decide whether the discovered matter is trustworthy.**

Therefore:

```text
Discovery Signal
≠
Evaluation Outcome
≠
Trust Statement
```

And:

> **Discovery ≠ Trust Determination**

---

# Legacy “Trust Signal” Must Remain Non-Canonical

Legacy language such as:

> **trust signal**

must not be allowed to imply that Beacon makes a trust conclusion.

The mature distinction is:

```text
Beacon Discovery Signal
→ canonical discovery object

legacy trust signal
→ non-canonical indicator terminology

Attestor Trust Statement
→ bounded governed conclusion
```

Therefore:

> **Beacon Discovery Signal ≠ Trust Statement**

---

# Discovery May Inform Attestor Without Becoming Attestor

A Beacon Discovery Signal may become part of a governed Attestor evidence set.

For example:

```text
BEAC-2026-0001
        ↓ referenced in
ATT-2026-0001
        ↓
Rule-Constrained Evaluation
        ↓
TRST-2026-0001
```

Beacon contributes:

> **discovery context and provenance**

Attestor contributes:

> **evaluation and bounded conclusion**

Therefore:

> **Discovery evidence may inform evaluation without becoming evaluation.**

---

# Beacon ≠ Anchor Verification

Beacon may discover an Anchor Integrity Reference or a change in integrity state.

That does not make Beacon the integrity verifier.

For example:

```text
Anchor
→ verifies protected representation

Beacon
→ discovers or signals that result
```

Therefore:

> **Discovery of verification ≠ performing verification**

And:

> **Discovery Signal ≠ Integrity Reference**

---

# Beacon ≠ Chronicle Historical Preservation

Beacon may discover a historically significant event.

Chronicle determines whether that occurrence qualifies for historical preservation.

Conceptually:

```text
Beacon
→ discovers relevant event

Chronicle
→ preserves qualifying occurrence
```

These functions may intersect.

They remain distinct.

Therefore:

> **Discovery ≠ Historical Preservation**

---

# Beacon Validation Applies Only to Beacon Objects

Beacon may validate a Discovery Signal against Beacon requirements.

That validation may examine:

- identifier;
- subject;
- Signal Type;
- provenance;
- source references;
- Discovery Metadata;
- timestamps;
- relationships;
- lifecycle fields;
- schema requirements.

That means:

> **the Discovery Signal is valid under Beacon rules.**

It does not mean:

- the source object is valid;
- the source is certified;
- the source is trusted;
- the source is registered.

Therefore:

> **Valid Discovery Signal ≠ Valid source object by inheritance.**

---

# First Production Boundary

The first production object:

```text
BEAC-2026-0001
```

was based on:

```text
SC-CERT-2026-0001
```

Beacon directly observed the Certifier-owned source, established direct provenance, created a Discovery Signal, validated it, activated it, and published it.

That did not change the authority model.

Certifier remained authoritative for the certification.

Atlas remained authoritative for the underlying jurisdiction intelligence.

Beacon owned only:

- the Discovery Signal;
- Discovery Metadata;
- Beacon provenance;
- Beacon lifecycle;
- Beacon publication state;
- Beacon-side relationships.

This production operation demonstrates Beacon's bounded role.

---

# Discovery Does Not Create Endorsement

A Beacon signal should not be read as:

> **Satoshium approves this.**

or:

> **Satoshium certifies this.**

or:

> **Satoshium trusts this.**

The correct meaning is narrower:

> **Beacon identified and governed this discovery as a relevant signal under Beacon rules.**

Therefore:

```text
Discovered
≠
Approved
≠
Certified
≠
Registered
≠
Verified
≠
Trusted
```

---

# Beacon Can Discover External Sources

Beacon is not limited to Suite-owned objects.

It may discover relevant externally sourced information where its rules permit.

This reinforces:

> **Registry is not a universal prerequisite.**

And:

> **Certifier is not a universal prerequisite.**

Beacon's actual dependency is on:

- a relevant observable condition;
- sufficient source/provenance basis;
- Beacon eligibility/relevance requirements.

Not on a fixed upstream institution.

---

# Beacon Can Discover State Without Owning State

Beacon may signal that another institutional object is:

- Active;
- Published;
- Superseded;
- Updated;
- Newly Created.

But Beacon does not thereby own that source object's lifecycle state.

For example:

```text
Beacon Signal:
"SC-CERT-2026-0001 is Active"
```

means Beacon observed that state.

Certifier remains authoritative for whether the Certification Package is Active.

Therefore:

> **Observed source state ≠ Beacon-owned source state**

---

# Beacon Publication ≠ Source Publication

A Discovery Signal may be Published.

The source object may have its own independent publication state.

Therefore:

```text
BEAC Publication State
≠
Source Publication State
```

unless both states are independently true.

---

# Beacon Does Not Create a Source-of-Truth Layer

Because Beacon can observe multiple systems, it could be misread as a central aggregation authority.

That interpretation is rejected.

Beacon may aggregate discoverable signals.

It does not become authoritative for the underlying domains.

Therefore:

> **Aggregation ≠ Authority**

And:

> **Discovery visibility ≠ source ownership**

---

# Correct Architectural Position

Beacon is best represented as a cross-cutting observational institution:

```text
Authoritative / Observable Sources
      ├── Atlas
      ├── Certifier
      ├── Registry
      ├── Chronicle
      ├── Anchor
      ├── Attestor
      └── External Sources
               │
               ▼
             Beacon
        Discovery & Signals
               │
               ▼
       Discovery Signal
```

Beacon can observe many sources.

It is not superior to those sources.

---

# Reconciled Beacon Boundaries

Beacon may:

- observe relevant conditions;
- identify discovery subjects;
- establish discovery provenance;
- assess relevance;
- create Discovery Signals;
- classify Signal Types;
- maintain Discovery Metadata;
- validate Discovery Signals;
- govern Beacon lifecycle;
- publish signals;
- maintain Beacon relationships.

Beacon does **not**, merely by doing so:

- verify source truth;
- perform certification;
- register source objects;
- create SREGs;
- establish historical authority;
- perform integrity verification;
- perform Attestor evaluation;
- issue Trust Statements;
- create source lifecycle states;
- endorse source content.

---

# Governing Rules

1. **Beacon = Discovery & Signals.**
2. Beacon's canonical object is the **Discovery Signal**.
3. Discovery Metadata remains supporting structure, not a second canonical object.
4. **Discovery ≠ Verification.**
5. Observation ≠ substantive verification.
6. Provenance traceability ≠ substantive verification.
7. **Discovery ≠ Certification.**
8. Certification Signal is a Discovery Signal category, not a certification.
9. **Discovery ≠ Registration.**
10. Discovery Signal ≠ SREG.
11. **Discovery ≠ Trust Determination.**
12. Discovery Signal ≠ Evaluation Outcome.
13. Discovery Signal ≠ Trust Statement.
14. Legacy “trust signal” terminology must not imply Beacon trust authority.
15. Beacon Validation applies to Beacon objects, not source objects.
16. Valid Discovery Signal does not make the source valid by inheritance.
17. Discovered ≠ Approved.
18. Discovered ≠ Certified.
19. Discovered ≠ Registered.
20. Discovered ≠ Trusted.
21. Beacon may observe source state without owning that state.
22. Beacon publication does not replace source publication.
23. Aggregation does not create source authority.
24. **Discovery does not transfer authority.**

---

# Governing Formulation

> **BEACON DISCOVERS AND SIGNALS. IT DOES NOT VERIFY, CERTIFY, REGISTER, OR DETERMINE TRUST FOR THE SOURCE OBJECT.**

Short form:

> **DISCOVERY ≠ DETERMINATION.**

---

## Final Disposition

# BEACON POSITION RECONCILIATION — COMPLETE — APPROVED

Beacon is formally positioned as the Suite's cross-cutting **Discovery & Signals** institution.

It has authority over the Discovery Signals it creates while preserving strict boundaries against verification, certification, registration, historical authority, integrity authority, Attestor evaluation, trust determination, and source ownership.
