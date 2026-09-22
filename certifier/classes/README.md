# Satoshium Certifier — Certification Classes

**Path:** `/certifier/classes/`  
**Institution:** Satoshium Certifier  
**Surface:** Certification Classes  
**Status:** Current repository documentation

## Purpose

This directory documents the **Certification Classes** used by Satoshium Certifier.

Certification Classes communicate the level, scope, and confidence posture associated with a completed certification under the governing Suite Standards and Suite Methodology.

The public page for this directory is:

- `index.html`

This README documents the current class model, assignment boundary, authority relationship, artifact propagation rules, and areas requiring later Suite Reconciliation.

## Role of Certification Classes

Certification Classes describe the result of a completed Certifier process.

They do not create certification authority.

They summarize the certification posture established through:

- preserved Evidence Records;
- applicable Suite Standards;
- applied Suite Methodology;
- Certifier evaluation;
- the certification decision; and
- the canonical Certification Package.

The assigned class is therefore downstream from the completed certification process.

## Current Certification Classes

The current public model defines three Certification Classes.

### Informational

Used for certification subjects whose primary purpose is documentation, observation, inventory, or factual preservation rather than operational certification.

The class communicates that the subject was reviewed within an informational or preservation-oriented certification scope.

### Operational

Used for certification subjects that satisfy the applicable Suite Standards and Suite Methodology for their intended operational purpose.

The class communicates that the subject successfully completed the defined certification workflow within its documented operational scope.

`SC-CERT-2026-0001` is the first production example of the Operational class.

### Verified

The current public documentation describes **Verified** as the highest current Certification Class.

It is associated with the strongest available certification confidence under the present class model and may include stronger evidence preservation, integrity references, Registry integration, and governed interoperability with Attestor where applicable.

The meaning and boundaries of this class should remain subject to the governing Suite Standards, Suite Methodology, and future Suite Reconciliation.

## Class Assignment Flow

The current assignment model is:

```text
Certification Subject
        ↓
Evidence Records & Evidence Review
        ↓
Suite Standards + Suite Methodology
        ↓
Certification Package
        ↓
Evaluation & Certification Decision
        ↓
Certification Class
        ↓
SCPR · SCR · SCRD HTML / JSON
```

The Certification Class is assigned only after the certification process has been completed.

The class communicates the decision.

It does not independently create the decision.

## Canonical Relationship

The canonical Certification Package remains the authoritative operational record for the certification.

Certification Class should remain consistent across downstream Certifier artifacts, including:

- Certification Package;
- Certification Process Report (SCPR);
- Certification Receipt (SCR);
- Certified Record (SCRD HTML);
- Certified Record (SCRD JSON); and
- governed Suite references or integrations.

If a downstream representation conflicts with the canonical Certification Package, the Certification Package governs.

## Standards and Methodology Boundary

The enduring Suite relationship remains:

> **Standards define expectations. Methodology defines implementation. Certifier performs certification.**

Certification Classes do not independently define Suite Standards or Suite Methodology.

Their meaning derives from the certification process governed by those layers.

## Confidence Posture

The current Certification Classes page uses **confidence posture** as part of the class model.

That language belongs to Certifier only insofar as it communicates the certification result produced under the governing Standards and Methodology.

It must not automatically be treated as equivalent to:

- Attestor rule-constrained evaluation;
- an Attestor Trust Statement;
- universal truth;
- generalized trust ranking; or
- external reputation scoring.

This distinction requires continued architectural discipline.

## Relationship to Attestor

Attestor is operational and institutionally distinct from Certifier.

Attestor's canonical flow is:

```text
Eligible Governed Inputs
        ↓
Attestation
        ↓
Rule-Constrained Evaluation
        ↓
Trust Statement
```

A Certification Class is not an Attestation.

A Certification Class is not a Trust Statement.

A `Verified` Certification Class therefore must not be interpreted as an Attestor validation or trust outcome merely because Attestor may later reference or consume eligible Certifier outputs.

## Relationship to Registry

Registry may reference or register governed Certifier records through the Registry architecture.

Registry references do not determine the Certification Class and do not transfer Certifier authority.

## Relationship to Anchor

Anchor may preserve Integrity References associated with certification artifacts.

Integrity preservation may strengthen the evidentiary or preservation context of a certification, but Anchor does not assign the Certification Class.

## Relationship to Other Suite Institutions

Other Suite institutions may reference Certifier outputs under their own governed roles.

Such relationships should preserve institutional ownership and object identity.

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Not a Value Judgment

Certification Classes do not measure:

- commercial value;
- popularity;
- ownership;
- social importance;
- market quality;
- general superiority; or
- universal trustworthiness.

They communicate the level and purpose of review within the Certifier certification framework.

## Version and Historical Discipline

Additional Certification Classes may be introduced in the future.

Historical certifications should remain traceable to the class definitions that existed when those certifications were issued.

Changes to class definitions should not silently rewrite the meaning of previously issued certifications.

## Suite Reconciliation Considerations

The following matters should be reviewed during Suite Reconciliation rather than redesigned within this README pass:

1. whether **Verified** remains the preferred name and meaning for the highest Certifier class;
2. how Certifier **confidence posture** should remain bounded from Attestor evaluation and Trust Statements;
3. whether evidence preservation, Registry integration, Anchor integrity references, or Attestor interoperability are class characteristics, prerequisites, or merely common implementation patterns; and
4. whether future class additions require explicit versioned definitions in Standards or Methodology.

These are architectural questions rather than documentation-only corrections.

## Repository Expectations

Changes to this directory should preserve:

1. Certifier as certification authority;
2. the Certification Package as canonical operational record;
3. Certification Class as a downstream communication of the completed certification;
4. synchronization across generated Certifier artifacts;
5. distinction between Certifier confidence posture and Attestor trust conclusions;
6. historical class-version traceability;
7. separation between certification class and value judgment; and
8. the rule that reference does not transfer authority.

## Governing Principle

**Certification Classes communicate the scope and confidence posture of a completed certification; they do not independently create certification authority or Attestor trust conclusions.**
