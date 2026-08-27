# Maintenance

## Overview

**Maintenance** governs post-publication operations required to preserve the continued integrity, resolvability, verifiability, and historical usefulness of Satoshium Anchor Integrity References.

Maintenance covers:

- broken Source links;
- Source Artifact changes;
- Reverification;
- algorithm deprecation;
- algorithm migration;
- key rotation;
- key compromise;
- external commitment health;
- publication health;
- relationship health;
- Version history;
- Corrections;
- Lifecycle review;
- storage migration;
- long-term preservation.

The governing principle is:

> Observe continuously. Preserve history. Escalate governed change.

---

## Maintenance Boundary

Maintenance observes and evaluates.

It does not silently change institutional authority.

```text
Maintenance finding
        ↓
governed decision
        ↓
Verification
Correction
Versioning
Lifecycle
Publication
new Integrity Reference
```

Maintenance may trigger these systems.

It does not replace them.

---

# Post-Publication Monitoring

Published Integrity References should remain reviewable for:

```text
Source reachability
canonical HTML availability
canonical JSON availability
current-Version resolution
historical-Version resolution
relationship resolution
Verification Material availability
external commitment availability
algorithm status
key status
Correction notices
Lifecycle notices
```

---

# Broken Source Links

A broken Source URL does not automatically invalidate the Integrity Reference.

```text
Source Identifier
→ identity

Source URL
→ location
```

Maintenance should distinguish:

```text
temporary outage
permanent relocation
Source withdrawal
Source deletion
archive relocation
identifier resolution failure
```

---

# Source Relocation

If a Source Artifact moves but identity remains the same:

```text
Source location changes
≠
Source identity changes
```

Anchor may update location metadata through governed Versioning, Maintenance metadata, Publication redirect, or relationship update depending on whether the canonical Anchor record changes.

Historical Source locations should remain preserved where useful.

---

# Source Artifact Changes

Maintenance may discover that a Source Artifact has changed.

Use the Versioning integrity-subject test:

```text
Source changed
        ↓
Source Artifact identity
+
Canonical Representation
+
Representation Boundary
        ↓
same integrity subject?
```

Possible outcomes:

```text
no Anchor action
Reverification
new Anchor Version
new Integrity Reference
```

A Source change is not automatically an Anchor Correction.

---

# Reverification

Maintenance is a primary trigger for Reverification.

Potential triggers include:

```text
scheduled review
Source change
Source relocation
suspected corruption
algorithm review
key rotation
external commitment concern
Correction
Version change
governance request
manual investigation
```

---

# Failed Reverification

A failed or incomplete Reverification remains a preserved Verification event.

```text
Reverification
        ↓
Verification Result
        ↓
investigate
        ↓
determine cause
```

Possible consequences:

```text
no institutional change
Maintenance note
Correction
new Anchor Version
Lifecycle review
new Integrity Reference
```

Maintenance must not silently infer cause from a Verification Result.

---

# Algorithm Deprecation

Algorithms may become unsuitable for new use while historical Integrity References remain meaningful.

```text
historical evidence
→ preserve

new use
→ may be deprecated or prohibited
```

Maintenance should determine whether stronger replacement evidence, a new Anchor Version, method-status metadata, or Reverification is needed.

---

# Algorithm Migration

For the same integrity subject:

```text
same Canonical Representation
+
new algorithm evidence
```

may lead to:

```text
additional method evidence
```

or:

```text
new Anchor Version
```

Historical evidence remains preserved.

---

# Key Rotation

Maintenance should preserve:

```text
old key reference
→ historical Verification

new key reference
→ future signing
```

Key rotation must not rewrite prior signature attribution.

---

# Key Compromise

If a key is compromised, preserve:

```text
compromise time
affected key reference
affected signatures
affected Integrity References
Verification impact
remediation action
```

Potential responses:

```text
Reverification
Integrity State review
Correction
replacement evidence
Lifecycle review
```

---

# External Commitment Health

Potential checks include:

```text
service availability
proof availability
identifier resolution
log / ledger accessibility
protocol deprecation
historical proof validity
inclusion-proof availability
```

External-system failure must remain distinguishable from Integrity mismatch.

---

# Bitcoin Commitment Health

If Bitcoin commitments are later adopted, Maintenance may review:

```text
transaction resolution
confirmation history
commitment location
inclusion proof
committed value correspondence
archival proof availability
```

No Bitcoin-specific Maintenance procedure is frozen yet.

---

# Publication Health

Maintenance should monitor:

```text
canonical HTML
canonical JSON
current-Version pointer
historical Version access
Correction notices
supersession notices
withdrawal notices
archival notices
canonical redirects
```

---

# Human / Machine Consistency

Maintenance should periodically verify:

```text
Canonical HTML
↔
Canonical JSON
```

Material institutional fields should remain consistent.

---

# Relationship Health

Maintenance should review:

```text
Source Artifact relationship
previous Version
next Version
Correction lineage
supersession lineage
external commitment
Verification Record
Publication representation
```

A broken relationship target should be investigated without automatically deleting the relationship.

---

# Version Health

Maintenance should ensure:

```text
current Version resolves
historical Versions remain preserved
Version lineage remains ordered
Correction lineage remains intact
supersession relationships remain resolvable
```

---

# Correction Routing

When Maintenance discovers an Anchor-owned error:

```text
Maintenance finding
        ↓
Correction review
        ↓
same integrity subject?
```

If yes:

```text
Correction
→ new Anchor Version
```

If no:

```text
new Integrity Reference
→ new Anchor Identifier
```

Maintenance must not silently patch production state.

---

# Lifecycle Review

Maintenance may identify conditions requiring Lifecycle review:

- superseding Integrity Reference;
- unresolved integrity defect;
- Source permanently withdrawn;
- method no longer verifiable;
- governance change;
- long-term archival transition.

Maintenance triggers review.

Lifecycle architecture determines state.

---

# Long-Term Preservation

Maintenance should preserve:

```text
Anchor Identifier
all production Versions
Source references
Canonical Representation context
Integrity Material
Verification Material
Provenance
Relationships
Corrections
Lifecycle history
Publication history
```

---

# Storage Migration

Infrastructure may change.

```text
storage migration
≠
Anchor Identifier change
```

Migration should preserve:

- canonical record integrity;
- Integrity Values;
- Version history;
- publication URLs or redirects;
- relationships;
- provenance;
- historical access.

---

# Preservation Format Migration

If preservation migration changes the Canonical Representation, the Versioning subject test applies.

If it changes only storage infrastructure while the governed representation remains unchanged, a new Integrity Reference may not be necessary.

---

# Maintenance Event

Anchor may later preserve structured Maintenance events.

Potential fields:

```text
reviewed_at
trigger
scope
observations
Reverification result
action required
related Correction
related Anchor Version
Lifecycle review
next review due
```

Whether Maintenance events receive permanent identifiers remains unfrozen.

---

# Maintenance Cadence

No universal review cadence is frozen.

Cadence may eventually depend on:

```text
Integrity Method
algorithm risk
key status
Source volatility
external commitment dependency
Lifecycle State
institutional importance
```

---

# Scheduled vs. Triggered Maintenance

Maintenance may be:

```text
scheduled
```

or:

```text
event-triggered
```

Potential event triggers include:

- Source change;
- key compromise;
- algorithm deprecation;
- failed Reverification;
- publication outage;
- relationship break;
- Correction.

---

# Maintenance vs. Verification

```text
Maintenance
→ decides when / why review is needed

Verification
→ performs integrity comparison
```

---

# Maintenance vs. Correction

```text
Maintenance
→ detects

Correction
→ repairs Anchor-owned error
```

Not every Maintenance finding is a Correction.

---

# Maintenance vs. Versioning

```text
Maintenance event
≠
automatically new Anchor Version
```

A new Version is required only when the canonical Anchor record changes under Versioning rules.

---

# Maintenance vs. Lifecycle

```text
Maintenance
→ may trigger Lifecycle review

Lifecycle
→ determines institutional state
```

---

# Maintenance vs. Publication

Maintenance ensures that published Anchor records remain resolvable and internally consistent.

Publication governs whether and how a Version is publicly authoritative.

---

# Maintenance and Schema

The Base Schema currently contains a provisional:

```text
maintenance
```

object with fields such as:

```text
last_reviewed_at
next_review_due
maintenance_notes
```

This architecture demonstrates that richer structured events may later be needed.

---

# Maintenance Procedure

The conceptual procedure is:

```text
1. Identify Maintenance trigger.
2. Load current Integrity Reference and Version history.
3. Check publication and relationship resolution.
4. Check Source availability and Source changes.
5. Review method, algorithm, key, and commitment health.
6. Perform Reverification where required.
7. Record observations.
8. Determine whether governed action is required.
9. Route to Correction, Versioning, Lifecycle, Publication, or new Integrity Reference.
10. Preserve Maintenance history.
11. Set next review where applicable.
```

This should later become a formal procedure under `/anchor/procedures/`.

---

# Current Freeze Decisions

### Maintenance Is Required

```text
Yes
```

for published Integrity References where continued integrity preservation depends on ongoing review.

### Core Maintenance Domains

```text
Resolution Health
Reverification
Method / Algorithm Health
Key Health
External Commitment Health
Source Change Review
Correction Routing
Version / Relationship Health
Publication Health
Long-Term Preservation
```

### Maintenance Cadence Frozen

```text
No
```

### Maintenance Event Identifier Frozen

```text
No
```

### Maintenance Event Schema Frozen

```text
No
```

### Still Unfrozen

```text
universal vs. risk-based cadence
Maintenance event identifier
Maintenance event schema
review severity levels
mandatory Reverification triggers
algorithm deprecation thresholds
key compromise procedure
external commitment health thresholds
Bitcoin-specific Maintenance
automatic vs. manual escalation rules
next-review calculation
first production Maintenance record
```

---

# Maintenance Principle

> Observe continuously. Preserve history. Escalate governed change.

Anchor Maintenance should preserve long-term integrity and institutional continuity without allowing operational upkeep to rewrite canonical history.

---

## Status

**Post-Foundational Architecture**

Maintenance domains, boundaries, triggers, escalation paths, and preservation responsibilities are now defined.

**Version:** 1.0-draft

**Maintained By:** Satoshium
