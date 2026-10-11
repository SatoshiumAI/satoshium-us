# Certification Schema

**Path:** `/suite/methodology/certification-schema/`  
**Surface:** Satoshium Suite · Methodology  
**Status:** Current repository documentation

## Purpose

This directory documents the Satoshium Suite **Certification Schema** methodology surface.

The Certification Schema defines structured representations used for **Certifier / certification-domain records** so that certification information can be represented consistently, validated against governed structures, exchanged between systems, and interpreted by both people and software.

It is not a universal Suite schema and does not define the canonical objects of other Suite institutions.

The public page for this directory is:

- `index.html`

This README documents the repository role and architectural boundaries of the directory. It does not replace the public presentation in `index.html`.

## Methodology Role

Certification Schema belongs to the Satoshium Suite Methodology as a **certification-specific methodology surface**.

Its role is to translate governed certification information into structured, machine-readable representations while preserving consistency, interoperability, provenance, and long-term verification.

Methodology defines how governed processes are implemented. Schema structure supports that implementation by defining how resulting information is represented.

A schema does not create certification authority, determine a certification outcome, activate lifecycle state, publish a record, or create canonical ownership merely by defining or validating structure.

## Scope Boundary

This methodology surface governs **certification-record representation only**.

```text
Certification Schema
→ Certifier / certification-domain representation requirements

Suite Schemas Standard
→ shared structural expectations

Other Institutional Schemas
→ governed by the applicable institution
```

Therefore:

```text
CERTIFICATION SCHEMA
≠ UNIVERSAL SUITE SCHEMA

SCHEMA
≠ CANONICAL OBJECT

SCHEMA VALIDATION
≠ CERTIFICATION DETERMINATION

SCHEMA FIELD
≠ AUTHORITY OVER THE REFERENCED CONCEPT
```

Other Suite institutions may consume or reference certification representations where permitted, but they do not inherit Certifier's schema authority or canonical ownership.

## Canonical Responsibility

This surface documents the schema-level structure used to represent certification information.

The **Certification Package** remains the Certifier-owned canonical object. The Certification Schema is a representation contract for structured certification information; it is not the canonical object itself.

Where an official schema is separately published under the applicable Satoshium Schemas Standard or governed certification schema surface, that schema is authoritative for structural conformance only.

The illustrative structure shown in `index.html` is explanatory only and must not be treated as the official schema.

```text
Certification Package
→ canonical Certifier object

Certification Schema
→ structured representation rules

Illustrative JSON
→ explanatory example only
```

## Structural Concerns

The Certification Schema may define or constrain fields such as:

- canonical identifiers;
- version information;
- applicable standard references;
- status values;
- subject information;
- evidence references;
- evaluation information;
- scoring information, where scoring is explicitly adopted;
- certification determination information;
- issuance or lifecycle-related timestamps;
- metadata; and
- other governed certification fields required by the applicable schema.

The presence of a field in a schema does not transfer authority over the referenced object or concept to the schema.

## Validation

Schema validation determines whether a structured certification representation conforms to the applicable schema requirements.

Schema validation is not the same as:

- certification eligibility;
- substantive evaluation;
- certification outcome;
- conformance to a separate institutional framework;
- publication;
- truth;
- support; or
- an Attestor Trust Statement;
- canonical ownership; or
- institutional authority.

A structurally valid record may still fail other governed requirements.

```text
STRUCTURALLY VALID
≠ CERTIFIED

STRUCTURALLY VALID
≠ PUBLISHED

STRUCTURALLY VALID
≠ SUPPORTED

STRUCTURALLY VALID
≠ TRUSTED
```

## Interoperability

Structured certification schemas support consistent exchange and interpretation of certification information across Suite institutions, software, and future implementations.

Interoperability does not collapse institutional boundaries.

A certification record represented through a common schema remains governed by the institution and canonical process responsible for that record.

Reference does not transfer authority.

## Relationship to Certifier

Satoshium Certifier remains the Suite institution responsible for certification operations and the Certification Package.

This methodology surface supports Certifier by defining structured representation requirements where applicable.

The Certification Schema does not replace Certifier, issue certifications independently, or become the authoritative source for the certification object merely because it defines how that object is represented.

## Relationship to Attestor

Attestor governs its own canonical flow:

```text
Eligible Governed Inputs
→ Attestation
→ Rule-Constrained Evaluation
→ Trust Statement
```

A certification schema may contain references to information later consumed by Attestor, but it does not define an Attestor Trust Statement or Attestor evaluation structure unless Attestor's own governed schema explicitly does so.

```text
CERTIFICATION SCHEMA
≠ ATTESTOR SCHEMA

CERTIFICATION FIELD
≠ TRUST STATEMENT

CERTIFICATION REPRESENTATION
≠ ATTESTOR CANONICAL OBJECT
```

## Relationship to Other Suite Institutions

Certification information may be referenced by other Suite institutions, including Registry, Chronicle, Anchor, Beacon, and Attestor.

Those relationships must preserve the established Suite boundaries:

- Registry records canonical Registry objects and does not become the source authority for the certification merely by referencing it.
- Chronicle records governed chronology.
- Anchor establishes integrity references.
- Beacon provides governed Discovery Signals; Discovery Metadata remains supporting Beacon structure.
- Attestor may reference certification objects as eligible governed inputs but does not inherit Certifier authority over them.

Reference does not equal derivation, support, or authority transfer.

## Governance and Canonicalization Boundary

Certification schema work operates within settled Suite architecture.

A schema change may alter representation requirements, but it may not silently alter:

- Certifier's institutional role;
- canonical ownership of the Certification Package;
- another institution's canonical object;
- Suite membership;
- authority allocation; or
- constitutional dependencies.

If a proposed schema change would alter one of those matters, the issue must move to the applicable **Suite Governance / Architecture Reconciliation** process.

```text
SCHEMA CHANGE
≠ ARCHITECTURAL AUTHORITY

SCHEMA SOPHISTICATION
≠ CANONICALIZATION

CANONICALIZATION SIGNALS
≠ CANONICALIZATION
```

## Illustrative Structure

The JSON structure displayed in `index.html` is explicitly illustrative.

It exists to communicate the kinds of fields and structural relationships a certification schema may contain.

Official schemas, where published, govern actual structural requirements.

Do not treat the illustrative JSON example as a normative schema artifact.

## Repository Expectations

Changes to this directory should preserve:

1. the distinction between methodology and institutional authority;
2. the distinction between schema validation and substantive certification evaluation;
3. the distinction between structured representation and lifecycle state;
4. provenance and authority boundaries for referenced objects;
5. the non-normative status of illustrative examples; and
6. consistency with the governing Suite standards, methodology, and Certifier architecture;
7. explicit certification-domain scope;
8. separation of schema from canonical object identity;
9. separation of certification schema from Attestor schema and Trust Statement semantics;
10. explicit scoring adoption where scoring fields are used; and
11. escalation of canonical-ownership or constitutional changes to Suite Governance / Architecture Reconciliation.

Changes that would alter the authority, lifecycle, or institutional meaning of certification records require the appropriate governed architectural review rather than a documentation-only edit.

## Governing Principle

**The Certification Schema defines certification representation structure; it does not become the Certification Package, create canonical ownership, transfer authority, or define Attestor trust semantics.**
