# Signal Record Schema — Deprecated Compatibility Notice

## Status

```text
Status → Deprecated as canonical Beacon schema
Replacement → discovery-signal-schema.md
Effective → September 5, 2026
```

---

## Purpose

This file preserves the transition from the earlier conceptual **Signal Record Schema** to the Phase II canonical **Discovery Signal Schema**.

The former Signal Record model used identifiers such as:

```text
SIG-2026-000001
```

and included earlier signal classifications and status concepts.

That model predates Beacon Phase II architecture.

Beacon has now established:

```text
Canonical Object → Discovery Signal
Canonical Identifier → BEAC-YYYY-NNNN
Canonical Schema → discovery-signal-schema.md
```

Therefore the earlier Signal Record schema must not be used for new production Beacon objects.

---

## Canonical Replacement

Use:

```text
/beacon/schemas/discovery-signal-schema.md
```

The canonical structure is:

```text
Identity
→ Subject
→ Signal Type
→ Source
→ Provenance
→ Canonical References
→ Discovery Metadata
→ Timestamps
→ Version
→ Status
→ Relationships
```

---

## Identifier Migration

Legacy:

```text
SIG-YYYY-NNNNNN
```

Current canonical standard:

```text
BEAC-YYYY-NNNN
```

Example:

```text
BEAC-2026-0001
```

Do not issue new `SIG-` identifiers for canonical Beacon Discovery Signals.

---

## Signal Type Migration

Earlier examples included categories such as:

```text
Regulatory Signal
Media Signal
Identity Signal
Research Signal
```

The Phase II architectural vocabulary is now:

```text
Information
Jurisdiction
Certification
Registry
Historical
Integrity
Trust
Relationship
```

Specialized context should normally be represented through:

```text
Discovery Metadata
canonical references
relationships
specialized profiles
```

rather than ad hoc type proliferation.

---

## Status Migration

Earlier Signal Record status examples included:

```text
Active
Archived
Superseded
Monitoring
Closed
```

The current lifecycle architecture is:

```text
Draft
Active
Superseded
Resolved
Withdrawn
```

Publication is separate:

```text
Unpublished
Published
```

`Monitoring`, `Closed`, and `Archived` are not canonical Discovery Signal lifecycle states.

---

## Confidence and Relevance

Earlier drafts included generalized:

```text
Signal Confidence
Signal Relevance
```

These are not currently required canonical Discovery Signal fields.

They may only return if later architecture establishes explicit meaning, methodology, and validation rules.

A Beacon confidence field must not become a substitute for:

```text
Certifier verification
Anchor integrity
Attestor Trust Statement
```

---

## Authority Boundary

The earlier principle that signals should remain connected to sources is preserved and strengthened.

Beacon owns the Discovery Signal.

The source institution owns the referenced canonical object.

> **Reference does not transfer authority.**

---

## Historical Preservation

This file exists so older architectural references can be understood.

It should not be interpreted as a second active schema.

For production architecture, use:

```text
discovery-signal-schema.md
```

---

## Last Updated

September 5, 2026
