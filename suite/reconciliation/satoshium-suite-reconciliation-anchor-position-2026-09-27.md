# Satoshium Suite Reconciliation — Anchor Position

**Date:** September 27, 2026  
**Phase:** Phase III — Whole-Suite Architecture  
**Decision Class:** RECONCILE  
**Status:** COMPLETE — APPROVED

---

## Purpose

This record reconciles Anchor's position within the mature Satoshium Suite.

The purpose is to ensure that Anchor's role as:

> **Integrity Preservation**

remains bounded to the exact protected representation rather than implying:

- truth;
- certification;
- whole-package integrity;
- source-object correctness;
- package completeness;
- or semantic authority beyond the defined representation boundary.

The governing principle is:

> **Anchor protects a defined representation within a declared boundary. It does not prove the truth, certification, completeness, or whole-package integrity of everything associated with that source.**

---

# Formal Role

Anchor's reconciled institutional role is:

> **Integrity Preservation**

Its canonical object is:

> **Integrity Reference**

The essential model is:

```text
Source Artifact
        ↓
Canonical Representation
        ↓
Representation Boundary
        ↓
Integrity Processing
        ↓
Integrity Reference
```

Anchor therefore protects a specific representation, not an abstract concept.

---

# Integrity Is Representation-Bounded

The protected subject is not simply:

```text
"the certification"
```

or:

```text
"the package"
```

or:

```text
"the truth of the record"
```

The actual Integrity Subject is defined through:

```text
Source Artifact Identity
+
Canonical Representation
+
Representation Boundary
```

That combination determines what the Integrity Reference actually covers.

Therefore:

> **Integrity must always be interpreted within its declared representation boundary.**

---

# Integrity Reference ≠ Truth

An integrity check can establish that a tested representation matches the protected representation.

It cannot establish that the representation's substantive claims are true.

For example:

```text
Protected JSON
        ↓
Hash match
        ↓
Integrity Verification: MATCH
```

This means:

> **the tested representation matches the protected canonical representation.**

It does not mean:

> every claim inside the JSON is true.

Therefore:

> **Integrity ≠ Truth**

And:

> **Hash match ≠ truth determination**

---

# Integrity Reference ≠ Certification

Anchor may protect an artifact associated with a Certification Package.

That does not mean Anchor independently certifies:

- the subject;
- the certification outcome;
- the certification evidence;
- the Certification Decision.

Therefore:

```text
Integrity Reference
≠
Certification Package
```

And:

> **Integrity Verification ≠ Certification**

Anchor may prove that a protected representation has not changed from the representation originally protected.

Certifier remains authoritative for what the certification means.

---

# Integrity Reference ≠ Whole-Package Integrity

This is a central architectural boundary.

If Anchor protects:

```text
SCRD JSON
```

that does **not** automatically mean it protects:

```text
the entire Certification Package
```

unless the Integrity Subject and Representation Boundary explicitly define the whole package as the protected representation.

Therefore:

> **Protected component ≠ whole-package integrity**

And:

> **Component integrity must not be generalized to the entire package.**

---

# Whole-Package Integrity Must Be Explicitly Defined

If Satoshium later wants to assert integrity over an entire package, the architecture must explicitly define:

- included files;
- excluded files;
- ordering rules;
- canonicalization rules;
- metadata treatment;
- representation boundaries;
- how multiple artifacts are combined;
- whether the package itself has one canonical serialized form.

Without that explicit definition, a protected file remains only a protected file.

Therefore:

> **Whole-package integrity requires a whole-package representation boundary.**

---

# Anchor Does Not Protect Abstract Meaning

Anchor protects representations.

It does not directly protect:

- semantic interpretation;
- institutional intent;
- conceptual meaning;
- future reinterpretation;
- external references;
- unstated context.

For example:

```text
Text remains byte-for-byte identical
```

does not guarantee:

> everyone interprets it the same way.

Therefore:

> **Representation integrity ≠ semantic immutability**

---

# Source Artifact ≠ Canonical Object Identity Automatically

A source artifact may be:

- JSON;
- HTML;
- Markdown;
- a manifest;
- another serialization.

That artifact may represent a canonical object.

But the artifact itself is not necessarily the canonical institutional object.

For example:

```text
Certification Package
        ↓ represented by
SCRD JSON
```

Anchor may protect the SCRD JSON representation.

That does not make:

```text
SCRD JSON = Certification Package
```

Therefore:

> **Representation ≠ Canonical Object by default**

And:

> **Anchored representation ≠ source-object identity**

---

# Anchor Verification ≠ Source Validation

Anchor verification answers:

> **Does this tested representation match the protected representation?**

Source-institution Validation answers a different question.

For example:

```text
Certifier Validation
→ Does the Certification Package meet Certifier requirements?

Anchor Verification
→ Does this representation match the protected representation?
```

Therefore:

> **Integrity Verification ≠ Source Validation**

A representation can verify successfully while the source object is later:

- invalidated;
- superseded;
- withdrawn;
- otherwise changed by its owning institution.

---

# Anchor Validation ≠ Source Validation

Anchor may validate the Integrity Reference itself.

That may include:

- identifier;
- source identity;
- representation definition;
- hash structure;
- algorithm;
- timestamps;
- provenance;
- controlled values;
- required fields;
- lifecycle state.

That means:

> **the Integrity Reference is valid under Anchor rules.**

It does not mean:

> the underlying source object is valid under its own institution's rules.

Therefore:

> **Valid Integrity Reference ≠ Valid source object by inheritance.**

---

# Integrity Persists When Source Status Changes

A protected representation may remain integrity-verifiable after the source object's lifecycle changes.

For example:

```text
Source Object: Superseded
Integrity Reference: still verifies protected V1 representation
```

This is not contradictory.

The Integrity Reference is saying:

> the preserved representation still matches the representation that was protected.

It is not saying:

> the protected representation is still current.

Therefore:

> **Integrity State ≠ Source Lifecycle State**

---

# Integrity Can Preserve Historical Representations

An older version may remain protected even after a newer version exists.

For example:

```text
Version 1
→ protected by Integrity Reference A

Version 2
→ protected by Integrity Reference B
```

Both may remain valid integrity records.

This preserves historical continuity.

It does not collapse versions into one representation.

---

# Same Integrity Subject vs New Integrity Subject

The reconciled rule remains:

```text
Same Integrity Subject
→ new Integrity Reference version

New Integrity Subject
→ new Integrity Reference
```

A new Integrity Subject may arise when the protected representation changes materially, including changes to:

- source artifact identity;
- canonical representation;
- representation boundary.

Therefore:

> **Changed protected representation may require new Anchor identity.**

---

# Anchor Does Not Certify Completeness

Suppose the protected representation includes only one artifact from a larger package.

A valid integrity match does not prove:

- all expected artifacts exist;
- no package artifact is missing;
- the package is complete;
- all supporting evidence exists.

Those are separate questions.

Therefore:

> **Integrity ≠ Completeness**

unless completeness itself is explicitly included in the protected representation model.

---

# Anchor Does Not Certify Provenance Correctness Beyond Scope

Anchor may preserve provenance metadata within an Integrity Reference.

But if source provenance is asserted by another institution, Anchor's preservation of that provenance does not independently prove the upstream claim.

Therefore:

> **Preserved provenance ≠ independently verified provenance**

unless Anchor explicitly performs that verification under defined rules.

---

# Anchor Does Not Become Source Authority

If Anchor protects a Certifier artifact:

```text
Certifier
→ owns source object

Anchor
→ owns Integrity Reference
```

Anchor does not become authoritative for:

- certification meaning;
- certification outcome;
- source content;
- source lifecycle.

Therefore:

> **Integrity authority ≠ content authority**

And:

> **Anchoring does not transfer source authority.**

---

# Anchor and Chronicle Remain Distinct

Chronicle preserves:

> **qualifying historical occurrence**

Anchor preserves:

> **exact representation integrity**

These functions may relate to the same broader matter while remaining separate.

For example:

```text
Chronicle
→ preserves that a certification was issued

Anchor
→ preserves integrity of a certification-related machine-readable representation
```

One preserves **when**.

The other preserves **representation continuity**.

Therefore:

> **Historical preservation ≠ Integrity preservation**

---

# Anchor and Attestor Remain Distinct

Attestor may use an Integrity Reference as governed evidence.

That does not mean Anchor makes the trust conclusion.

For example:

```text
Integrity Reference
        ↓ supports evidence context
Attestor Evaluation
```

Anchor contributes:

> **representation integrity evidence**

Attestor determines:

> **the bounded evaluation conclusion**

Therefore:

> **Integrity evidence ≠ Evaluation Outcome**

And:

> **Integrity Reference ≠ Trust Statement**

---

# Anchor and Beacon Remain Distinct

Beacon may discover:

- a new Integrity Reference;
- a changed integrity state;
- a newly published protected representation.

But:

```text
Integrity Reference ≠ Discovery Signal
```

Beacon's discovery does not alter Anchor authority.

Anchor's integrity does not create Beacon discovery authority.

---

# Precise Public Wording

Anchor-related documentation should avoid overbroad wording such as:

```text
"This package is immutable."
"This certification is proven authentic."
"This record is true."
"The entire package is protected."
```

unless the architecture explicitly supports those claims.

Preferred wording is bounded.

For example:

> **This Integrity Reference protects the declared canonical representation within the defined representation boundary.**

Or:

> **Verification confirms that the tested representation matches the protected canonical representation.**

---

# Whole-Package Claims Require Explicit Basis

If future documentation says:

> **Package Integrity: Verified**

that phrase should only be used where the protected representation actually encompasses the full package under a defined whole-package integrity model.

Otherwise, documentation should identify the exact protected representation.

For example:

```text
Protected Representation:
SCRD-SC-CERT-2026-0001 JSON
```

is preferable to:

```text
Certification Package Integrity: Verified
```

unless whole-package protection actually exists.

---

# Correct Architectural Position

Anchor's position is best represented as:

```text
Source Artifact
        ↓
Canonical Representation
        ↓
Representation Boundary
        ↓
Anchor
Integrity Preservation
        ↓
Integrity Reference
```

Anchor acts on the declared representation.

It does not become a source institution or truth authority.

---

# Reconciled Anchor Boundaries

Anchor may:

- define Integrity Subjects;
- define Canonical Representations;
- define Representation Boundaries;
- canonicalize protected representations;
- hash or otherwise integrity-protect representations;
- create Integrity References;
- verify representation matches;
- validate Integrity References;
- preserve integrity provenance;
- version Integrity References;
- publish integrity records.

Anchor does **not**, merely by doing so:

- determine truth;
- certify the source;
- validate the source institution's substantive decision;
- prove whole-package integrity unless explicitly scoped;
- prove package completeness;
- replace source authority;
- create historical authority;
- create Discovery Signals;
- perform Attestor evaluation.

---

# Governing Rules

1. **Anchor = Integrity Preservation.**
2. Anchor's canonical object is the **Integrity Reference**.
3. Integrity must remain bounded to the declared Integrity Subject.
4. Integrity Subject includes **Source Artifact Identity + Canonical Representation + Representation Boundary**.
5. **Integrity ≠ Truth.**
6. **Integrity ≠ Certification.**
7. **Integrity ≠ Whole-Package Integrity by default.**
8. Protected component integrity must not be generalized to the whole package.
9. Whole-package integrity requires an explicitly defined whole-package representation boundary.
10. Representation integrity does not establish semantic truth.
11. Representation ≠ canonical object by default.
12. Integrity Verification ≠ source Validation.
13. Anchor Validation applies to the Integrity Reference, not the source object.
14. Valid Integrity Reference does not make the source object valid by inheritance.
15. Integrity state does not equal source lifecycle state.
16. Integrity can preserve superseded or historical representations.
17. Same Integrity Subject may version.
18. New Integrity Subject requires a new Integrity Reference.
19. Integrity does not establish completeness unless completeness is explicitly in scope.
20. Preserved provenance does not automatically prove upstream provenance claims.
21. **Integrity authority ≠ content authority.**
22. Anchoring does not transfer source authority.

---

# Governing Formulation

> **ANCHOR PROTECTS A DEFINED REPRESENTATION WITHIN A DECLARED BOUNDARY. IT DOES NOT PROVE THE TRUTH, CERTIFICATION, COMPLETENESS, OR WHOLE-PACKAGE INTEGRITY OF EVERYTHING ASSOCIATED WITH THAT SOURCE.**

Short form:

> **INTEGRITY IS BOUNDED TO THE REPRESENTATION ACTUALLY PROTECTED.**

---

## Final Disposition

# ANCHOR POSITION RECONCILIATION — COMPLETE — APPROVED

Anchor is formally positioned as the Suite's **Integrity Preservation** institution.

It has strong authority over the Integrity References it creates while preserving a strict boundary against truth claims, certification authority, source validation, package completeness, and whole-package integrity unless those properties are explicitly within the defined representation boundary.
