# Chronicle Phase VII — Two-Layer Profile Validation Report

## Validation Target

This validation reviewed the two production schema artifacts supplied for Phase VII closeout:

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

**Status: CONDITIONAL PASS — two closeout corrections remain.**

Both JSON files are valid JSON Schema Draft 2020-12 schemas.

The intended Certification Profile constraints generally operate correctly.

However, two issues should be corrected before Phase VII is formally closed.

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

# Positive Validation Test

A representative Certification Created Chronicle Entry containing:

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
```

validated successfully when JSON Schema `format` assertions were enabled.

Result:

```text
PASS
```

---

# Negative Validation Tests

## Missing `originating_system`

Expected:

```text
FAIL
```

Actual:

```text
FAIL — correct behavior
```

Reason:

```text
'originating_system' is a required property
```

---

## Wrong `originating_system`

Test value:

```text
originating_system: registry
```

Expected:

```text
FAIL
```

Actual:

```text
FAIL — correct behavior
```

Reason:

```text
'certifier' was expected
```

---

## Missing `authoritative_record_references`

Expected:

```text
FAIL
```

Actual:

```text
FAIL — correct behavior
```

Reason:

```text
'authoritative_record_references' is a required property
```

---

## Null `event_date`

Test value:

```text
event_date: null
```

Expected under Certification Profile:

```text
FAIL
```

Actual:

```text
FAIL — correct behavior
```

The Base Schema permits an unknown Event Date, but the Certification Event-Type Profile correctly strengthens the requirement and disallows `null`.

---

## Invalid Certification Event Type

Test value:

```text
event_type: something_else
```

Expected:

```text
FAIL
```

Actual:

```text
FAIL — correct behavior
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

# Closeout Finding 1 — Base Schema `event_date`

The supplied Base Schema still uses:

```json
"oneOf": [
  {"type":"string","format":"date"},
  {"type":"string","format":"date-time"},
  {"type":"null"}
]
```

This is the earlier version.

The intended corrected production structure is:

```json
"anyOf": [
  {"type":"string","format":"date"},
  {"type":"string","format":"date-time"},
  {"type":"null"}
]
```

Why this matters:

JSON Schema `format` evaluation may be annotation-only unless a validator enables format assertions.

Without format assertions, both string branches can match the same string.

With `oneOf`, that causes an otherwise valid Event Date to fail because more than one branch matches.

Observed test without a FormatChecker:

```text
2026-07-05
→ matched both string branches
→ FAIL under oneOf
```

Therefore:

```text
Base Schema event_date:
oneOf → anyOf
```

should remain the production correction.

---

# Closeout Finding 2 — Authoritative Certifier Reference

The Certification Event-Type Profile requires:

```text
authoritative_record_references
```

and correctly requires at least one item.

However, the current machine-readable rule also accepts:

```json
"authoritative_record_references": [
  "SC-CERT-2026-0001"
]
```

and:

```json
"authoritative_record_references": [
  {
    "reference": "SC-CERT-2026-0001"
  }
]
```

Both currently validate.

Therefore the JSON Profile does not yet machine-enforce the stronger institutional requirement:

```text
At least one authoritative reference must explicitly establish Certifier
as the authoritative system.
```

Recommended correction:

Require the `contains` condition to match at least one structured reference containing:

```text
reference
system: certifier
```

The Profile may continue permitting other reference forms, but at least one structured Certifier reference should be mandatory.

Recommended conceptual rule:

```text
authoritative_record_references
        ↓
contains at least one
        ↓
reference + system: certifier
```

For stronger production clarity, `record_type: certification_package` may also be required if that value is formally governed for all applicable Certification Entries.

---

# Validation Summary

```text
Schema syntax / Draft 2020-12 validity       PASS
Base + Profile composition                    PASS
Valid certification Entry                     PASS
Missing originating_system                    FAIL as intended
Wrong originating_system                      FAIL as intended
Missing authoritative references              FAIL as intended
Null Certification event_date                 FAIL as intended
Invalid Certification Event Type              FAIL as intended

Base event_date oneOf                         CORRECTION REQUIRED
Explicit Certifier-reference enforcement      CORRECTION REQUIRED
```

---

# Phase VII Closeout Decision

Phase VII should not yet be marked formally complete.

The architecture is complete and the validation stack is functioning.

Two narrow machine-readable corrections remain:

```text
1. Base Schema:
   event_date oneOf → anyOf

2. Certification Event-Type Profile:
   require at least one structured authoritative reference
   explicitly identifying system: certifier
```

After those two corrections are applied and the same validation suite is rerun successfully:

```text
Phase VII — Production Schemas
        =
COMPLETE
```

---

## Guiding Principle

> Validate what the architecture claims.

And for Profile enforcement:

> Reference does not transfer authority, but the schema must still identify whose authority is being referenced.
