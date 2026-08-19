# Chronicle Phase VII — Two-Layer Profile Validation Report

## Validation Target

This validation reviewed the final production schema artifacts used for Phase VII closeout:

```text
/chronicle/schemas/chronicle-base-schema.json

/chronicle/schemas/certification-event-profile/
└── certification-event-profile.json
```

Validation model:

```text
Chronicle Base Schema
        +
Certification Event-Type Profile
        ↓
Certification-related Chronicle Entry
```

---

# Result

**Status: PASS**

The Chronicle Base Schema and Certification Event-Type Profile successfully passed final two-layer validation.

Both files are valid JSON Schema Draft 2020-12 schemas.

The Certification Event-Type Profile correctly specializes the Chronicle Base Schema without creating a competing canonical object or duplicating Certifier-owned Certification Package contents.

---

# Schema Meta-Validation

## Chronicle Base Schema

```text
Draft 2020-12 schema validation: PASS
```

## Certification Event-Type Profile

```text
Draft 2020-12 schema validation: PASS
```

---

# Final Production Corrections Confirmed

Two issues identified during the first validation pass were corrected before final re-validation.

## Correction 1 — Base Schema `event_date`

The earlier Base Schema used:

```text
oneOf
```

for:

```text
date
date-time
null
```

The final production Base Schema now uses:

```text
anyOf
```

Conceptually:

```json
"event_date": {
  "anyOf": [
    {"type":"string","format":"date"},
    {"type":"string","format":"date-time"},
    {"type":"null"}
  ]
}
```

This avoids ambiguous validation behavior when JSON Schema `format` is treated as annotation rather than assertion.

Final result:

```text
PASS
```

---

## Correction 2 — Explicit Certifier Reference Enforcement

The earlier Certification Event-Type Profile allowed a plain string or an incompletely structured reference to satisfy the authoritative-reference requirement.

The final Profile now requires:

```text
authoritative_record_references
        ↓
contains at least one structured reference
        ↓
reference
system: certifier
```

Other valid reference forms may coexist, but at least one authoritative reference must explicitly establish Certifier as the authoritative system.

Final result:

```text
PASS
```

---

# Positive Validation Tests

## Valid Certification Created Entry

A representative Chronicle Entry containing:

```text
entry_id: CHR-2026-0001
schema_id: chronicle-entry
schema_version: 1.0.0
entry_version: 1

event_type: certification_created
event_date: 2026-07-05

event_type_profile: certification-event-profile
originating_system: certifier

authoritative_record_references:
  - reference: SC-CERT-2026-0001
    system: certifier
    record_type: certification_package

provenance:
  origin: satoshium_certifier
  acquisition_method: direct_authoritative_record_reference
  retrieved_at: valid date-time
  authoritative_record_reference:
    reference: SC-CERT-2026-0001
    system: certifier
    record_type: certification_package

verification_state: not_reviewed
lifecycle_state: draft
publication_state: not_published
entry_created_at: valid date-time
```

Result:

```text
PASS
```

---

## Valid Date-Time Event Date

A Certification Entry using a valid `date-time` value for:

```text
event_date
```

Result:

```text
PASS
```

---

## Base Schema Without Format Assertions

The corrected Base Schema was also evaluated without relying on JSON Schema format assertions.

Result:

```text
PASS
```

This confirms that the `anyOf` correction removes the earlier `oneOf` ambiguity.

---

## Mixed Authoritative References

A Certification Entry containing multiple authoritative references, including at least one structured reference with:

```text
reference: SC-CERT-2026-0001
system: certifier
```

Result:

```text
PASS
```

This confirms that the Profile permits additional valid references while still requiring explicit Certifier authority.

---

# Negative Validation Tests

Negative tests are expected to fail. A failure therefore represents correct schema behavior.

## Missing `originating_system`

Test:

```text
originating_system omitted
```

Result:

```text
FAIL as intended
```

Reason:

```text
'originating_system' is a required property
```

---

## Wrong `originating_system`

Test:

```text
originating_system: registry
```

Result:

```text
FAIL as intended
```

Reason:

```text
'certifier' was expected
```

---

## Missing `authoritative_record_references`

Test:

```text
authoritative_record_references omitted
```

Result:

```text
FAIL as intended
```

Reason:

```text
'authoritative_record_references' is a required property
```

---

## Null Certification `event_date`

Test:

```text
event_date: null
```

The Chronicle Base Schema permits `null` when an Event Date cannot be determined.

The Certification Event-Type Profile intentionally strengthens this requirement and does not permit `null`.

Result:

```text
FAIL as intended
```

---

## Invalid Certification Event Type

Test:

```text
event_type: something_else
```

Result:

```text
FAIL as intended
```

The Profile limits Event Type to:

```text
certification_created
certification_renewed
certification_suspended
certification_revoked
certification_expired
```

---

## Plain-String-Only Authoritative Reference

Test:

```json
"authoritative_record_references": [
  "SC-CERT-2026-0001"
]
```

Result:

```text
FAIL as intended
```

A plain string may be an allowed Base Schema reference form, but it cannot by itself satisfy the Certification Event-Type Profile's explicit Certifier-authority requirement.

---

## Structured Reference Missing `system`

Test:

```json
"authoritative_record_references": [
  {
    "reference": "SC-CERT-2026-0001"
  }
]
```

Result:

```text
FAIL as intended
```

The Profile requires at least one structured authoritative reference that explicitly identifies:

```text
system: certifier
```

---

## Structured Reference with Wrong System

Test:

```json
"authoritative_record_references": [
  {
    "reference": "SC-CERT-2026-0001",
    "system": "registry"
  }
]
```

Result:

```text
FAIL as intended
```

This prevents a non-Certifier reference from satisfying the Profile's authoritative certification reference requirement.

---

# Final Validation Summary

```text
Schema syntax / Draft 2020-12 validity             PASS
Base + Profile composition                          PASS
Valid Certification Created Entry                   PASS
Valid date-time Event Date                          PASS
Base Schema without format assertions               PASS
Mixed references with valid Certifier reference     PASS

Missing originating_system                          FAIL as intended
Wrong originating_system                            FAIL as intended
Missing authoritative references                    FAIL as intended
Null Certification event_date                       FAIL as intended
Invalid Certification Event Type                    FAIL as intended
Plain-string-only authoritative reference           FAIL as intended
Structured reference missing system                 FAIL as intended
Structured reference with wrong system              FAIL as intended
```

---

# Institutional Validation Result

The two-layer schema model now behaves as intended:

```text
Chronicle Base Schema
        +
Certification Event-Type Profile
        ↓
Validated Certification-related Chronicle Entry
```

The Base Schema preserves universal Chronicle Entry structure.

The Certification Event-Type Profile strengthens only certification-specific requirements.

Certifier remains authoritative for the certification action and Certification Package.

Chronicle remains authoritative for the historical-preservation record representing the qualifying Occurrence.

Reference does not transfer authority.

---

# Phase VII Closeout Decision

```text
Phase VII — Production Schemas
Status: COMPLETE
```

Phase VII successfully established:

```text
Chronicle Base Schema
✓ Human-readable production specification
✓ Machine-readable production schema

Supporting Schema Specifications
✓ Source Record Schema
✓ Evidence Record Schema
✓ Correction Record Schema

Schema Architecture
✓ Public /chronicle/schemas/ architecture
✓ Schema README
✓ Deprecated Chronicle Entry Schema compatibility pointer
✓ Controlled extension points
✓ Schema Versioning and compatibility principles

Certification Event-Type Profile
✓ Public Profile landing page
✓ Human-readable Profile specification
✓ Machine-readable JSON Profile
✓ Canonical Profile directory
✓ Explicit Certifier authority requirement
✓ Event-Type constraints
✓ Non-null certification Event Date
✓ Certification-specific Provenance requirements

Validation
✓ Draft 2020-12 meta-validation
✓ Positive validation tests
✓ Negative validation tests
✓ Base + Profile composition
✓ Final two-layer validation PASS
```

Phase VII is therefore formally closed.

---

# Next Operational Sequence

With Production Schemas complete, Chronicle moves from schema definition into production procedure.

```text
Phase VII — Production Schemas
        ↓
COMPLETE
        ↓
Chronicle Validation Procedure
        ↓
Production Procedure
        ↓
First Production Chronicle Entry
```

---

## Guiding Principle

> Validate what the architecture claims.

And for the completed Profile architecture:

> Base Schema defines the Chronicle Entry. The Certification Event-Type Profile supplies only the certification-specific requirements.

Final authority principle:

> Reference does not transfer authority, but the schema must identify whose authority is being referenced.
