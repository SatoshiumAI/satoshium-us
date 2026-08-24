# Integration

## Overview

**Satoshium Anchor Integration** defines how Anchor participates in the broader **Satoshium Suite**.

Anchor preserves durable **Integrity References** for authoritative artifacts owned by other institutions.

Integration is reference-first.

Anchor does not duplicate or absorb the external artifact merely because Anchor preserves integrity context for it.

The governing rule is:

> Reference does not transfer authority.

---

## Integration Purpose

Anchor Integration establishes the institutional relationship between:

```text
Source Institution
        ↓
Authoritative Artifact
        ↓
Canonical Representation
        ↓
Anchor Integrity Reference
```

The Source Institution remains authoritative for the external artifact.

Anchor becomes authoritative only for:

```text
the Integrity Reference
Anchor-controlled integrity metadata
Anchor-controlled lifecycle
Anchor-controlled publication
Anchor-controlled verification history
Anchor Corrections
Anchor Versions
```

---

# Suite Object Model

The current Suite object model is:

```text
Atlas
→ authoritative intelligence

Certifier
→ Certification Package

Registry
→ Satoshium Registry Entry

Chronicle
→ Chronicle Entry

Anchor
→ Integrity Reference

Beacon
→ Discovery Signal / Metadata

Attestor
→ Trust Statement

Navigator
→ Workflow Definition
```

Each institution retains authority over its own canonical object.

Anchor may preserve integrity context for any of these objects without taking ownership of them.

---

# Reference-First Interoperability

Anchor should integrate through references rather than duplication.

The preferred model is:

```text
Authoritative Artifact
        ↓
stable Source-System reference
        ↓
defined Canonical Representation
        ↓
Anchor Integrity Reference
```

Anchor should avoid copying external institutional meaning into its own record where a reference is sufficient.

This reduces duplication and preserves responsibility boundaries.

---

# Relationship to Atlas

Satoshium Atlas remains authoritative for Atlas-owned jurisdiction intelligence and related canonical records.

Anchor may preserve Integrity References for defined Atlas representations.

Anchor does not become authoritative for:

- jurisdiction facts;
- Atlas evidence;
- Atlas signals;
- Atlas metadata;
- jurisdiction interpretation.

Anchor contributes only integrity context.

---

# Relationship to Certifier

Satoshium Certifier remains authoritative for:

- certification actions;
- Certification Packages;
- certification determinations;
- certification classes;
- certification lifecycle;
- certification status;
- generated certification artifacts.

Anchor may preserve Integrity References for:

```text
Certification Package
SCPR
SCR
SCRD HTML
SCRD JSON
```

An Anchor Integrity Reference does not become a certification record.

Certifier remains the certification authority.

---

# Relationship to Registry

Satoshium Registry remains authoritative for:

- Satoshium Registry Entries;
- Registry identifiers;
- Registry Record Types;
- Registry metadata;
- Registry relationships;
- Registry lifecycle;
- Registry publication;
- Registry Corrections;
- Registry Versions.

Anchor may preserve an Integrity Reference for a defined SREG representation.

For example:

```text
SREG-2026-0001
```

remains Registry-owned even if Anchor later preserves a digest or commitment for its canonical representation.

---

# Relationship to Chronicle

Satoshium Chronicle remains authoritative for:

- Chronicle Entries;
- Chronicle identifiers;
- historical-preservation representation;
- Chronicle Relationships;
- Chronicle Provenance;
- Chronicle Verification;
- Chronicle Validation;
- Chronicle Publication;
- Chronicle Corrections;
- Chronicle Versions;
- Chronicle Maintenance.

Anchor may preserve an Integrity Reference for a defined Chronicle Entry representation.

For example:

```text
CHR-2026-0001
```

remains Chronicle-owned.

Anchor does not become the historical authority merely because it preserves integrity context for that Entry.

---

# Relationship to Beacon

Satoshium Beacon remains authoritative for:

```text
Discovery Signals
Discovery Metadata
```

and related Beacon-owned discovery artifacts.

Anchor may preserve integrity context for those artifacts.

Anchor does not become responsible for determining discovery significance or Beacon publication logic.

---

# Relationship to Attestor

Satoshium Attestor remains authoritative for:

```text
Trust Statements
```

and other Attestor-owned trust artifacts.

Anchor may preserve Integrity References for those representations.

A valid Anchor verification does not determine whether the Trust Statement should be accepted or believed.

---

# Relationship to Navigator

Satoshium Navigator remains authoritative for:

```text
Workflow Definitions
```

and Navigator-owned orchestration logic.

Anchor may preserve integrity context for those artifacts.

Anchor does not become the workflow authority.

---

# Relationship to Anchor-Owned Artifacts

Anchor may later preserve integrity lineage for Anchor-owned records where doing so adds durable value.

However, Anchor should avoid recursive integrity structures that merely duplicate existing information.

The principle remains:

> Use structure when structure adds durable institutional value.

---

# Integration Candidate Types

Potential Anchor integration candidates include:

```text
Atlas records
Certification Packages
SCPRs
SCRs
SCRDs
Satoshium Registry Entries
Chronicle Entries
Discovery artifacts
Trust Statements
Workflow Definitions
other governed Suite artifacts
```

Not every artifact needs a separate Integrity Reference.

Selection should follow:

- institutional value;
- reproducibility;
- canonical representation clarity;
- source authority;
- long-term integrity need;
- minimum necessary structure.

---

# Certifier Artifact Integration

Certifier may produce multiple related artifacts from one canonical Certification Package.

Anchor should not automatically anchor every artifact merely because it exists.

The decision should consider:

```text
Which artifact is canonical?
Which derivative has independent durable value?
Which representation needs independent integrity verification?
```

For example, the Certification Package may be the primary anchoring candidate while a public SCRD may warrant its own Integrity Reference only if independently useful.

This question should be resolved through later production rules.

---

# Current Production Suite Examples

The current production Suite provides concrete authoritative records:

```text
SC-CERT-2026-0001
→ Certifier-owned Certification Package

SREG-2026-0001
→ Registry-owned Satoshium Registry Entry

CHR-2026-0001
→ Chronicle-owned Chronicle Entry
```

These are useful future Anchor integration candidates.

Anchor has not yet assigned production Integrity References to them.

They should not be treated as anchored until the Anchor production architecture is complete and an actual anchoring procedure is executed.

---

# What Anchor Preserves

Anchor may preserve:

- Source Institution;
- Source-System Identifier;
- artifact type;
- Canonical Representation;
- Representation Boundary;
- Integrity Value;
- Hash Algorithm;
- timestamps;
- signatures;
- Verification Material;
- external commitment reference;
- Anchor identifier;
- Anchor Version;
- Integrity State;
- Publication State;
- Lifecycle State;
- Correction lineage;
- verification history.

Anchor should preserve enough context to make integrity independently reviewable.

It should not duplicate the complete external record unless required by a specific preservation design.

---

# Reciprocal References

Where useful, the external Source Artifact may reference its corresponding Anchor Integrity Reference.

Conceptually:

```text
Authoritative Artifact
        ↕
Integrity Reference
```

Reciprocal references improve discovery.

They do not merge institutional ownership.

A Certifier record referencing an Anchor Integrity Reference remains Certifier-owned.

An Anchor Integrity Reference referencing that Certifier record remains Anchor-owned.

---

# Source Status and Anchor State

Anchor must preserve the distinction between external Source status and Anchor state.

For example, a Source Artifact may later become:

```text
superseded
revoked
withdrawn
archived
deprecated
preserved
```

while its earlier Anchor Integrity Reference may remain historically valid.

Anchor may eventually maintain separate state systems for:

```text
Integrity State
Verification Result
Publication State
Lifecycle State
```

These should not be mapped automatically from the Source Institution.

---

# Source Artifact Changes

An external artifact may legitimately change after anchoring.

Examples include:

- new Source Artifact Version;
- Correction;
- lifecycle transition;
- new publication;
- migration;
- changed Canonical Representation;
- superseding record.

A later Source change does not erase the integrity relationship preserved for the earlier representation.

Anchor should preserve enough lineage to distinguish:

```text
Earlier Source Representation
        ↓
Earlier Integrity Reference

Later Source Representation
        ↓
Later Anchor Version or New Integrity Reference where required
```

---

# Authority Boundaries

Anchor does not determine:

- certification validity;
- Registry status;
- Chronicle historical meaning;
- Atlas jurisdiction truth;
- Beacon discovery significance;
- Attestor trustworthiness;
- Navigator workflow authority.

Anchor preserves integrity context.

The governing rule remains:

> Reference does not transfer authority.

---

# Integration with Suite Standards

Anchor Integration operates beneath the shared:

```text
Suite Standards
```

layer.

Anchor should inherit Suite-wide expectations for:

- terminology;
- governance;
- schemas;
- versioning;
- interoperability;
- trust boundaries;
- evidence;
- other shared institutional requirements.

Anchor should not create a competing Suite-wide standards system.

---

# Integration with Suite Methodology

Anchor Integration operates beneath the shared:

```text
Suite Methodology
```

layer.

Anchor-specific procedures may define how an Integrity Reference is:

```text
constructed
verified
validated
published
maintained
corrected
versioned
preserved
```

without redefining the broader Suite Methodology.

---

# Relationship to Suite Interoperability

Anchor implements the reference-first institutional model established by Suite Interoperability.

Its role is:

```text
preserve integrity context
```

rather than:

```text
absorb record authority
```

The institutional goal is interoperability with separation.

---

# Integration Philosophy

The governing philosophy is:

> Preserve the reference. Preserve the boundary. Preserve the authority.

Anchor should strengthen the Suite by making important artifacts more independently reviewable without creating duplicate ownership or institutional ambiguity.

---

## Status

**Foundation Reconciliation**

This Integration document reflects the current post-Suite Anchor model.

The following remain intentionally unfrozen pending later architecture and production testing:

```text
Anchor identifier format
Integrity Method Controlled Values
Integrity State values
Verification Result values
Schema requirements
Validation architecture
Publication architecture
Lifecycle values
Versioning rules
Correction rules
reciprocal reference requirements
first production Integrity Reference
```

**Version:** 1.0-draft

**Maintained By:** Satoshium
