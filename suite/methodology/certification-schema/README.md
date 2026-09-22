# Certification Schema

**Path:** `/suite/methodology/certification-schema/`  
**Surface:** Satoshium Suite · Methodology  
**Status:** Current repository documentation

## Purpose

This directory documents the Satoshium Suite **Certification Schema** methodology surface.

The Certification Schema defines structured representations used for certification records so that certification information can be represented consistently, validated against governed structures, exchanged between systems, and interpreted by both people and software.

The public page for this directory is:

- `index.html`

This README documents the repository role and architectural boundaries of the directory. It does not replace the public presentation in `index.html`.

## Methodology Role

Certification Schema belongs to the Satoshium Suite Methodology.

Its role is to translate governed certification information into structured, machine-readable representations while preserving consistency, interoperability, provenance, and long-term verification.

Methodology defines how governed processes are implemented. Schema structure supports that implementation by defining how resulting information is represented.

A schema does not create certification authority, determine a certification outcome, activate lifecycle state, or publish a record merely by validating its structure.

## Canonical Responsibility

This surface documents the schema-level structure used to represent certification information.

Where an official schema is separately published under the applicable Satoshium schema or standards surface, that governed schema is authoritative for structural conformance.

The illustrative structure shown in `index.html` is explanatory only and must not be treated as the official schema.

## Structural Concerns

The Certification Schema may define or constrain fields such as:

- canonical identifiers;
- version information;
- applicable standard references;
- status values;
- subject information;
- evidence references;
- evaluation information;
- scoring information;
- decision information;
- issuance or lifecycle-related timestamps;
- metadata; and
- other governed certification fields required by the applicable schema.

The presence of a field in a schema does not transfer authority over the referenced object or concept to the schema.

## Validation

Schema validation determines whether a structured record conforms to the applicable schema requirements.

Schema validation is not the same as:

- certification eligibility;
- substantive evaluation;
- certification outcome;
- conformance to a separate institutional framework;
- publication;
- truth;
- support; or
- a trust statement.

A structurally valid record may still fail other governed requirements.

## Interoperability

Structured schemas support consistent exchange and interpretation of certification information across Suite institutions, software, and future implementations.

Interoperability does not collapse institutional boundaries.

A certification record represented through a common schema remains governed by the institution and canonical process responsible for that record.

Reference does not transfer authority.

## Relationship to Certifier

Satoshium Certifier remains the Suite institution responsible for certification operations and the Certification Package.

This methodology surface supports Certifier by defining structured representation requirements where applicable.

The Certification Schema does not replace Certifier, issue certifications independently, or become the authoritative source for the certification object merely because it defines how that object is represented.

## Relationship to Other Suite Institutions

Certification information may be referenced by other Suite institutions, including Registry, Chronicle, Anchor, Beacon, and Attestor.

Those relationships must preserve the established Suite boundaries:

- Registry records canonical Registry objects and does not become the source authority for the certification merely by referencing it.
- Chronicle records governed chronology.
- Anchor establishes integrity references.
- Beacon provides discovery signals and discovery metadata.
- Attestor may reference certification objects as eligible governed inputs but does not inherit Certifier authority over them.

Reference does not equal derivation, support, or authority transfer.

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
6. consistency with the governing Suite standards, methodology, and Certifier architecture.

Changes that would alter the authority, lifecycle, or institutional meaning of certification records require the appropriate governed architectural review rather than a documentation-only edit.

## Governing Principle

**Schemas define structure. They do not transfer authority.**
