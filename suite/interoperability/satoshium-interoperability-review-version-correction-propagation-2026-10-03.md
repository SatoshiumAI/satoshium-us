# Satoshium Suite Interoperability Review — Version & Correction Propagation Review

**Date:** October 3, 2026  
**Review:** Satoshium Suite Interoperability Review  
**Step:** 8 — Review Version and Correction Propagation  
**Status:** COMPLETE — APPROVED

---

## Purpose

This review defines how downstream Satoshium Suite references respond when an upstream governed object is corrected, versioned, superseded, materially changed, or replaced by a new canonical assertion or conclusion.

The governing rule is:

> **CORRECTIONS REPAIR. VERSIONS PRESERVE CONTINUITY. SUPERSESSION PRESERVES HISTORY. MATERIAL CHANGE MAY REQUIRE NEW IDENTITY.**

This review does not redefine any institution's correction, versioning, or supersession architecture.

It defines interoperability behavior across institutional boundaries.

---

# 1. Governing Distinctions

The following settled Suite distinctions remain controlling:

```text
CORRECTION ≠ VERSION

CORRECTION ≠ DELETION

SUPERSESSION ≠ MUTATION

VERSION ≠ LIFECYCLE STATE

CHANGED CONCLUSION = CHANGED CANONICAL STATEMENT

MATERIAL CHANGE MAY REQUIRE NEW IDENTITY
```

And:

> **HISTORICAL REFERENCES MUST NOT BE SILENTLY MUTATED.**

A downstream institution may update its current-facing understanding of a source object.

It may not rewrite the source identity, version, state, or conclusion that actually existed when the downstream reference was created or evaluated.

---

# 2. Propagation Model

The adopted propagation model is:

```text
Upstream Change
        ↓
Classify Change Type
        ↓
Preserve Historical Reference
        ↓
Record New Source State / Version / Identity
        ↓
Assess Downstream Materiality
        ↓
Receiving Institution Determines Action
```

Possible downstream actions include:

```text
no action
metadata refresh
reference refresh
review flag
revalidation
reevaluation
new downstream version
correction
supersession
new canonical identity
republication
```

No upstream change automatically determines a downstream canonical-state change.

---

# 3. Non-Material Corrections

## Definition

A non-material correction repairs an error or defect without materially changing the source object's substantive meaning, assertion, conclusion, subject identity, or governed scope.

Examples may include:

```text
typographical correction
format repair
clarifying metadata
non-substantive label repair
broken public link correction
non-material provenance clarification
```

The source institution determines whether a correction is non-material.

## Downstream Response

### Preserve Historical Reference

**REQUIRED**

The downstream record must retain:

```text
source identifier used
source version used
source state at use
timestamp / evaluation basis where material
```

### Record Correction

**YES**

Where relevant, preserve:

```text
correction notice
new source version
correction timestamp
correction rationale
```

### Refresh

**PERMITTED / OFTEN APPROPRIATE**

Current-facing displays may refresh to the corrected representation.

### Flag

**NOT REQUIRED BY DEFAULT**

Flag only if the corrected field was material to downstream processing or interpretation.

### New Downstream Identity

**NO by default**

A non-material source correction does not itself require a new downstream canonical identity.

### Governing Rule

> **CORRECTION REPAIRS; IT DOES NOT ERASE THE PRIOR STATE.**

---

# 4. New Versions

## Definition

A new version preserves continuity of the same canonical object while representing a new preserved edition or state.

A new version may result from:

```text
correction
metadata update
schema-compatible revision
expanded evidence
clarification
maintenance
other institution-governed change
```

A new version does not automatically mean:

```text
new canonical identity
new lifecycle state
new publication state
supersession
material semantic change
```

## Downstream Response

### Preserve Version at Use

**REQUIRED**

The downstream institution must retain the exact source version used historically.

### Record New Version

**YES**

Where the source is monitored or current-facing, record:

```text
previous version
current version
version change time
materiality classification
```

### Refresh

**CONDITIONAL**

Refresh current references if the receiving institution intends to display or use the latest version.

### Flag

**ONLY IF MATERIAL**

If the new version changes a field material to the downstream object's basis, flag for review.

### Republish

**NOT AUTOMATIC**

A receiving institution republishes only under its own publication rules.

### Governing Rule

> **VERSIONS PRESERVE CONTINUITY.**

---

# 5. Supersession

## Definition

Supersession changes operative standing while preserving prior identity and history.

The adopted direction remains:

```text
successor
→ supersedes
→ prior object
```

## Downstream Response

### Preserve Prior Reference

**REQUIRED**

Existing downstream historical references to the superseded object remain valid as historical references.

### Record Successor

**YES**

Where current source standing matters, store:

```text
prior identifier
successor identifier
supersession relationship
effective time
```

### Refresh Current-Facing Resolution

**YES where current operative standing is displayed**

A current catalog, discovery page, workflow, or status view may point users to the successor while preserving the prior object.

### Flag

**YES where operative standing materially affects downstream meaning**

### Replace Historical Identifier

**PROHIBITED**

The downstream institution must not silently rewrite:

```text
old identifier
→ new identifier
```

inside historical records.

### Governing Rule

> **SUPERSESSION PRESERVES HISTORY.**

---

# 6. Materially Changed Assertions

## Definition

A materially changed assertion changes the semantic substance of a governed assertion sufficiently that continuity under the same assertion identity would misrepresent history.

This is especially important for Attestor.

The settled rule is:

> **MATERIALLY CHANGED ASSERTION → NEW ATTESTATION.**

## Downstream Response

### Preserve Original Assertion Reference

**REQUIRED**

A downstream object that relied on the earlier Attestation must retain the original `ATT-*` reference.

### Record New Attestation

**YES**

The new Attestation receives a new canonical identity where required by Attestor governance.

### Flag

**YES**

Any downstream use that depends on the assertion must be reviewed for material impact.

### Reevaluation

**CONDITIONAL / OFTEN REQUIRED**

Where the assertion participates in a later Trust Statement or other governed evaluation, the new assertion may trigger reevaluation.

### Silent Replacement

**PROHIBITED**

A prior `ATT-*` reference must not be silently replaced with the new Attestation identifier.

### Governing Rule

> **MATERIAL CHANGE MAY REQUIRE NEW IDENTITY.**

---

# 7. Changed Trust Statement Conclusions

## Definition

A Trust Statement expresses Attestor's canonical bounded conclusion.

The settled rule is:

> **CHANGED TRUST STATEMENT CONCLUSION → NEW TRUST STATEMENT IDENTITY.**

This is stronger than ordinary version continuity.

A changed conclusion is a changed canonical statement.

## Downstream Response

### Preserve Original Trust Statement

**REQUIRED**

Historical references to the original `TRST-*` must remain intact.

### Create / Reference New Trust Statement

**REQUIRED when Attestor issues a changed conclusion**

The changed conclusion must be represented by a new Trust Statement identity.

### Record Relationship

Where applicable:

```text
new Trust Statement
→ supersedes / corrects / otherwise governed relationship
→ prior Trust Statement
```

The exact relationship depends on Attestor's governing change classification.

### Flag Downstream Consumers

**YES**

Consumers of the prior conclusion must be able to distinguish:

```text
conclusion at historical time
≠ current conclusion
```

### Silent Version Mutation

**PROHIBITED**

A materially changed Trust Statement conclusion must not be represented as though the old canonical conclusion simply changed in place.

### Governing Rule

> **CHANGED CONCLUSION = CHANGED CANONICAL STATEMENT.**

---

# 8. Downstream Mutation Prohibition

The Suite adopts the following interoperability prohibition:

> **A DOWNSTREAM INSTITUTION MUST NOT SILENTLY MUTATE A HISTORICAL REFERENCE TO MATCH A LATER SOURCE STATE.**

Examples of prohibited behavior:

```text
replacing SC-CERT-2026-0001 V1.0 with V1.1
inside a historical evaluation record
without preserving that V1.0 was originally used

replacing a superseded source identifier
with its successor identifier
inside an earlier Chronicle Entry

rewriting a historical BEAC reference
to point only to the source's current version

replacing ATT-2026-0001
with a later Attestation
inside TRST-2026-0001

changing a prior Trust Statement conclusion
without issuing the required new canonical Trust Statement
```

Historical basis must remain reconstructable.

---

# 9. Current-State Reference Refresh

Current-facing systems may update their present-day reference pointers.

Examples:

```text
Registry catalog current-source panel
Beacon discovery status
Navigator current workflow context
Attestor source-health display
public current-status pages
```

But:

```text
Current-State Refresh
≠ Historical Reference Rewrite
```

A current display may say:

```text
Current source version → 1.2
Historical source version used → 1.0
```

Both may be true simultaneously.

---

# 10. Institution-Specific Propagation

## Atlas

A new Atlas package version may be consumed downstream while prior downstream references preserve the version originally used.

A materially changed intelligence object may require institution-specific review but does not automatically mutate downstream objects.

---

## Navigator

Navigator may refresh workflow inputs to newer source versions.

Workflow-local history must preserve what was actually passed to participating institutions.

A retry using a newer version must be distinguishable from the earlier invocation.

---

## Certifier

Certifier determines whether an upstream source change requires:

```text
no action
correction
new package version
recertification
new certification identity
```

Downstream consumers must preserve the exact Certification Package version referenced historically.

---

## Registry

Registry may update source metadata or create a new SREG version where the registered subject remains the same.

If the registered subject changes materially, a new SREG may be required.

Registry must preserve source and SREG history separately.

---

## Chronicle

Chronicle must preserve the historical source object/version relevant to the preserved Occurrence.

Later source correction or supersession may itself become a new qualifying Occurrence.

The original Chronicle Entry must not be rewritten to erase the earlier state.

---

## Anchor

Anchor distinguishes:

```text
Source correction
≠ Anchor correction

Source version change
≠ Integrity Reference version automatically
```

If the protected Integrity Subject changes materially, a new Integrity Reference may be required.

Prior integrity evidence remains preserved.

---

## Beacon

Beacon may refresh current discovery metadata when a source changes.

If the discovery itself becomes materially different, a new Discovery Signal may be required.

Prior Discovery Signals remain historical records.

---

## Attestor

Attestor has the strongest identity consequence rules:

```text
materially changed assertion
→ new Attestation

changed Trust Statement conclusion
→ new Trust Statement identity
```

Historical evaluation basis and prior conclusions must remain preserved.

---

# 11. Propagation Decision Matrix

| Upstream Change | Preserve Historical Reference | Record New State / Version | Flag Review | New Downstream Version Possible | New Downstream Identity Possible | Silent Historical Rewrite Allowed |
|---|---:|---:|---:|---:|---:|---:|
| Non-material correction | Yes | Yes | If material to downstream use | Yes | Rarely | **No** |
| New version | Yes | Yes | If material | Yes | Sometimes | **No** |
| Supersession | Yes | Yes | Usually if operative standing matters | Yes | Sometimes | **No** |
| Materially changed assertion | Yes | Yes | Yes | Possibly | **Yes / required under Attestor rule** | **No** |
| Changed Trust Statement conclusion | Yes | Yes | Yes | Not sufficient by itself | **Yes — required** | **No** |

---

# 12. Relationship Requirements for Propagation

Where applicable, changes should be represented explicitly using the settled relationship vocabulary:

```text
corrects
supersedes
derived-from
references
related-to
```

Examples:

```text
Correcting Version
→ corrects
→ Prior Version

Successor Object
→ supersedes
→ Prior Object

New Trust Statement
→ may supersede / correct
→ Prior Trust Statement
```

The exact relationship must reflect the governing institution's determination.

`related-to` must not be used where `corrects` or `supersedes` is actually established.

---

# 13. Provenance Requirements

Every downstream change response should preserve:

```text
source identifier
source institution
source version
source state at use
later source state
change type
change timestamp
relationship
receiving institution action
receiving institution decision timestamp
```

where material.

This allows later reconstruction of why a downstream object remained unchanged, was refreshed, was corrected, was superseded, or was replaced.

---

# 14. Unknown Change Classification

If the downstream institution detects that a source changed but cannot determine whether the change is material:

```text
change_classification → unknown
```

The system must not assume:

```text
non-material
safe
no review required
```

Preferred action:

```text
preserve
flag
review
```

> **UNKNOWN ≠ SUCCESS.**

---

# 15. Findings

## VCP-01 — Non-material corrections

**APPROVED**

Repair may propagate as metadata / reference refresh without requiring new downstream identity.

Historical source state remains preserved.

---

## VCP-02 — New versions

**APPROVED**

Downstream references preserve version-at-use and may separately track latest source version.

---

## VCP-03 — Supersession

**APPROVED**

Successor information may update current-facing references, but prior references remain historically intact.

---

## VCP-04 — Materially changed assertions

**APPROVED**

Material assertion change may require new canonical identity.

For Attestor:

```text
materially changed assertion
→ new Attestation
```

---

## VCP-05 — Changed Trust Statement conclusions

**APPROVED**

A changed Trust Statement conclusion requires a new Trust Statement identity.

---

## VCP-06 — Historical mutation

**REJECTED**

Silent downstream mutation of historical references is prohibited.

---

## VCP-07 — Current-state refresh

**APPROVED**

Current-facing representations may refresh while preserving the historical basis independently.

---

## VCP-08 — Relationship typing

**APPROVED**

Correction and supersession propagation must use their actual governed relationship semantics rather than generic `related-to`.

---

# Review Determination

The Suite's version and correction architecture is interoperable without redesign.

The correct propagation model is:

```text
Preserve Historical Reference
        +
Record New Source State
        +
Classify Change
        +
Assess Materiality
        +
Receiving Institution Governs Its Own Response
```

The review confirms:

> **CORRECTIONS REPAIR.**

> **VERSIONS PRESERVE CONTINUITY.**

> **SUPERSESSION PRESERVES HISTORY.**

> **MATERIAL CHANGE MAY REQUIRE NEW IDENTITY.**

And:

> **CHANGED CONCLUSION = CHANGED CANONICAL STATEMENT.**

No institutional role, canonical object, authority boundary, or relationship semantic requires reopening.

---

# FINAL DISPOSITION

# VERSION & CORRECTION PROPAGATION REVIEW — COMPLETE — APPROVED

The Suite must preserve historical references exactly enough to reconstruct what source identity, version, state, assertion, and conclusion were actually used.

Later source changes may update current-facing context and may trigger review, correction, supersession, reevaluation, republication, or new identity.

They must never silently rewrite history.
