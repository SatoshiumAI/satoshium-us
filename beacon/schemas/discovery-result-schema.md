# Discovery Result Schema

## Purpose

The **Discovery Result Schema** defines an optional, noncanonical structure for information returned through a Beacon discovery activity.

A Discovery Result may represent information surfaced in response to:

```text
query
search
investigation
exploration
relationship lookup
Navigator-directed workflow
other discovery activity
```

A Discovery Result is not automatically a Beacon Discovery Signal.

---

## Schema Role

```text
Role → Optional Discovery Output
Canonical Beacon Object → No
Canonical Beacon Identifier → Not required
```

Beacon's canonical production object remains:

```text
Discovery Signal
```

identified as:

```text
BEAC-YYYY-NNNN
```

---

# Core Distinction

```text
Discovery Result
→ information returned by a discovery activity

Discovery Signal
→ governed Beacon-owned canonical object
```

A result may lead to a Discovery Signal.

It does not become one merely because it was returned.

Conceptually:

```text
Query / Discovery Activity
        ↓
Discovery Result
        ↓
Institutional evaluation
        ↓
Possible Discovery Signal
```

---

# Result Structure

Potential result information may include:

```text
result_type
title
summary
associated_query
primary_source
supporting_sources
canonical_references
related_signals
relationships
relevance_context
discovery_context
timestamps
```

Exact production requirements are not frozen because this is a supporting operational structure.

---

## Result Type

Result Type describes the form of returned information.

Possible examples:

```text
Signal Reference
Source Reference
Canonical Record Reference
Relationship Result
Jurisdiction Result
Historical Result
Information Result
```

These are not Discovery Signal Types.

---

## Title

Human-readable result title.

---

## Summary

Brief explanation of why the result is relevant to the discovery activity.

---

## Associated Query

When applicable, preserve a reference to the originating query or discovery request.

The result should not duplicate an entire query record unless required.

---

## Primary Source

A result should preserve an attributable primary source using the Source Reference architecture.

---

## Supporting Sources

Additional sources may be preserved when they materially support the result.

---

## Canonical References

A result may point directly to institution-owned canonical objects.

Examples:

```text
SC-CERT-2026-0001
SREG-2026-0001
CHR-2026-0001
ANCH-2026-0001
BEAC-2026-0001
```

Each remains owned by its institution.

---

## Related Signals

A result may reference one or more Beacon Discovery Signals.

Example:

```yaml
related_signals:
  - BEAC-2026-0001
```

The result does not absorb the signal's identity or lifecycle.

---

## Relationships

A result may expose relationships discovered during a query or workflow.

Relationship semantics should remain attributable and reviewable.

---

## Relevance Context

The previous Discovery Result Schema included a generalized:

```text
Relevance Assessment
```

using High, Moderate, Low, and Unknown.

That field is not retained as a canonical controlled assessment.

If relevance is useful operationally, it may be preserved as:

```text
relevance_context
```

or another explicitly non-authoritative discovery aid.

A relevance label must not be interpreted as:

```text
verification
trust
certification
authority
```

---

## Confidence Assessment

The previous schema included:

```text
Confidence Assessment
```

This is removed from the core structure.

Beacon should not create an undefined confidence scale that could be mistaken for:

```text
Attestor trust
Certifier verification
Anchor integrity
```

A future confidence or ranking system would require its own explicit methodology and governance.

---

## Result Status

The previous schema included generic result states such as:

```text
Active
Archived
Superseded
Pending Review
```

These are not adopted as canonical Discovery Result lifecycle values.

If persistent Result records become operationally necessary, their lifecycle should be designed explicitly rather than borrowed from Discovery Signals.

For now, Discovery Results are treated as outputs, not institutional canonical objects.

---

# Conceptual Example

```yaml
result_type: Canonical Record Reference
title: Anchor Integrity Reference Found

summary: >
  Discovery surfaced a relevant Anchor Integrity Reference.

primary_source:
  source_kind: Suite Institution
  source_name: Satoshium Anchor
  source_institution: Anchor
  source_identifier: ANCH-2026-0001
  source_object_type: Integrity Reference

canonical_references:
  - institution: Anchor
    identifier: ANCH-2026-0001
    object_type: Integrity Reference

related_signals:
  - BEAC-2026-0001

discovery_context:
  method: Query

timestamps:
  returned_at: 2026-09-05T00:00:00Z
```

This example is conceptual only.

---

# Relationship to Navigator

Navigator owns workflow definition and orchestration.

Beacon may participate in a Navigator-directed workflow and return discovery results.

Conceptually:

```text
Navigator
→ workflow / orchestration
→ Beacon discovery activity
→ Discovery Result
```

Beacon does not redefine Navigator's workflow authority through this schema.

---

# Relationship to Discovery Signals

A result may:

```text
reference an existing Discovery Signal
support creation of a new Discovery Signal
support review of a Draft Discovery Signal
surface a source without creating a Discovery Signal
```

Creation of a canonical signal remains a separate institutional action.

---

# Authority Boundary

A Discovery Result may surface an authoritative object.

The result itself does not become authoritative merely because the referenced object is authoritative.

> **Reference does not transfer authority.**

---

# Retention

Retention rules for Discovery Results are not yet established.

Future operational work may determine whether results are:

```text
ephemeral
session-bound
persisted
auditable
aggregated
discarded after use
```

No retention assumption should be treated as canonical yet.

---

# Status

```text
Schema Role → Optional Noncanonical Discovery Output
Canonical Object → No
Architecture → Revised for Phase II
Lifecycle → Not established
Retention → Not established
Machine Validation → Pending if retained
```

---

## Last Updated

September 5, 2026
