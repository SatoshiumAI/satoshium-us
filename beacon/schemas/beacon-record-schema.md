# Beacon Record Schema — Deprecated Legacy Architecture

## Status

```text
Status → Deprecated as canonical production schema
Effective → September 5, 2026
Canonical Replacement → discovery-signal-schema.md
```

---

## Purpose

This document preserves the architectural transition from the earlier generic **Beacon Record Schema** to the Phase II canonical Discovery Signal model.

The previous schema defined a broad discovery-related object using:

```text
BEC-2026-000001
```

and attempted to represent:

```text
discovery activities
signals
sources
queries
relationships
results
metadata
```

inside one generic Beacon Record.

Phase II has now established a more precise institutional model.

Beacon's canonical production object is:

```text
Discovery Signal
```

with canonical identifier:

```text
BEAC-YYYY-NNNN
```

Therefore the generic Beacon Record is no longer a canonical Beacon object.

---

# Why the Model Changed

The former Beacon Record architecture risked conflating:

```text
canonical institutional object
query activity
discovery process
discovery result
source reference
relationship
metadata
```

Phase II separates these concerns.

The new architecture is:

```text
Canonical Object
→ Discovery Signal

Supporting Source Structure
→ Source Reference

Optional Discovery Output
→ Discovery Result

Optional Operational History
→ Query Log
```

This creates clearer institutional boundaries.

---

# Identifier Migration

Legacy:

```text
BEC-YYYY-NNNNNN
```

Current canonical Beacon identifier:

```text
BEAC-YYYY-NNNN
```

Example:

```text
BEAC-2026-0001
```

No new canonical Beacon objects should use `BEC-`.

---

# Canonical Replacement

Use:

```text
discovery-signal-schema.md
```

The canonical Discovery Signal structure is:

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

# Discovery Activity

The earlier Beacon Record Schema attempted to preserve discovery activity directly as a generic canonical record.

Current architecture does not assume that every discovery action deserves a permanent canonical object.

Discovery activity may instead be represented through:

```text
provenance
methodology
optional Query Log
optional Discovery Result
workflow reference
production audit information
```

depending on later operational need.

---

# Confidence

The earlier generic record included:

```text
Discovery Confidence
```

This is not retained as a canonical Beacon field.

Undefined confidence could be mistaken for:

```text
verification
certification
trust
integrity
```

Any future confidence model would require explicit methodology and governance.

---

# Status

The earlier schema proposed:

```text
Open
Active
Archived
Superseded
```

These values no longer define Beacon canonical object status.

Discovery Signal lifecycle is:

```text
Draft
Active
Superseded
Resolved
Withdrawn
```

Publication is separately:

```text
Unpublished
Published
```

---

# Source and Authority

The earlier schema correctly emphasized source attribution and traceability.

Those principles remain.

They are now represented more explicitly through:

```text
Source
Provenance
Canonical References
Relationships
```

inside the Discovery Signal architecture.

A referenced source object remains owned by its originating institution.

> **Reference does not transfer authority.**

---

# Future Use of Generic Activity Records

This file does not prohibit Beacon from ever creating an operational audit or activity record.

It establishes only that:

```text
Generic Beacon Record
≠
current canonical Beacon production object
```

If production later proves a need for a separate activity or audit record, that object should be designed explicitly, named precisely, assigned its own governed semantics, and reviewed for institutional necessity.

The former generic `BEC-` model should not be revived by default.

---

# Historical Preservation

This document is retained to:

```text
preserve architectural history
prevent accidental reuse of BEC identifiers
explain why the generic model was replaced
support repository traceability
```

For production work, use:

```text
discovery-signal-schema.md
```

---

## Last Updated

September 5, 2026
