# Reputation

## Overview

Within the current Satoshium Anchor architecture, **Reputation** is not an Anchor-owned institutional function.

Anchor does not:

```text
calculate reputation
accumulate reputation
score reputation
rank participants
maintain reputation profiles
```

A reputation assessment belongs to the institution, community, system, methodology, or process that produces it.

Anchor's role is narrower:

> Preserve the integrity of a defined reputation-related artifact when that preservation has durable institutional value.

The governing distinction is:

```text
Reputation Meaning
≠
Reputation Artifact Integrity
```

---

## Purpose

The `/anchor/reputation/` route is retained for continuity, but its role is now to explain how Anchor handles reputation-related artifacts.

Potential examples include:

- reputation scores;
- trust scores;
- reputation summaries;
- reliability assessments;
- community ratings;
- institutional assessments;
- reputation signals;
- ranking records;
- methodology documents;
- Trust Statements containing reputation-related judgments;
- historical reputation reports.

Anchor may preserve the integrity of these artifacts.

Anchor does not adopt the reputation judgment.

---

# Reputation Artifact

A **Reputation Artifact** is a score, summary, signal, assessment, ranking, statement, record, or methodology expressing reputation-related information.

Examples may include:

```text
reputation score
reliability rating
trust signal
community assessment
risk label
ranking
reputation report
scoring methodology
historical reputation summary
```

A Reputation Artifact may become an Anchor candidate when later integrity verification provides durable value.

---

# Source Authority

The Source Institution or producing system remains authoritative for:

- the reputation assessment;
- scoring methodology;
- weighting;
- interpretation;
- publication;
- correction;
- lifecycle;
- withdrawal;
- replacement.

Anchor owns only the Integrity Reference created for a defined representation.

> Reference does not transfer authority.

---

# Canonical Representation

Before anchoring a reputation-related artifact, Anchor must define:

```text
Canonical Representation
Representation Boundary
```

This is especially important where a score or assessment appears inside a dynamic interface.

Anchor may need to distinguish:

```text
canonical reputation record
```

from:

```text
live dashboard
sorting
presentation layer
current rank
derived visualization
later comments
```

The anchored representation should be reproducible or clearly identifiable.

---

# Reputation Artifact Integrity

Reputation Artifact Integrity asks:

> Does the reviewed reputation-related representation remain consistent with the representation governed by the Integrity Reference?

It does not ask:

> Is the reputation assessment correct?

Therefore:

```text
Reputation Artifact Integrity
≠
Reputation Validity
```

and:

```text
Reputation Artifact Integrity
≠
Trustworthiness
```

---

# Integrity of a Score vs. Validity of a Score

A reputation score can retain perfect cryptographic integrity while being:

- poorly designed;
- biased;
- outdated;
- based on incomplete data;
- methodologically weak;
- disputed;
- wrong.

Anchor can verify that the score has not changed from the anchored representation.

Anchor cannot infer that the score is valid merely from integrity.

The governing distinction is:

```text
Integrity of a Score
≠
Validity of the Scoring Methodology
```

---

# Reputation Methodology Artifacts

A methodology may itself be anchored.

Potential examples include:

- scoring formula;
- weighting model;
- methodology document;
- governance rule;
- calculation specification;
- data-source specification;
- versioned reputation framework.

In that case, Anchor preserves the integrity of the methodology artifact.

Anchor does not endorse the methodology.

---

# Reputation vs. History

Chronicle may preserve qualifying historical Occurrences through Chronicle Entries.

Historical records may later inform reputation.

Anchor does not derive reputation from Chronicle history.

Conceptually:

```text
Chronicle Entry
→ historical preservation

Reputation System
→ may interpret history

Anchor
→ may preserve Integrity References
```

These functions remain separate.

---

# Reputation vs. Certification

Certifier may issue a certification outcome.

A reputation system may use that outcome as one input.

Anchor may preserve integrity for:

- Certification Package;
- reputation artifact;
- both.

Anchor does not convert certification into reputation.

---

# Reputation vs. Attestation

An attestation or Trust Statement may influence reputation.

Attestor remains authoritative for Trust Statements.

Another institution may remain authoritative for the reputation calculation.

Anchor may preserve integrity for either artifact without assigning weight between them.

---

# Reputation vs. Trust

Reputation and trust remain conceptually distinct.

A reputation artifact may inform trust.

A Trust Statement may refer to reputation.

Anchor does not own either judgment.

Therefore:

```text
Reputation
≠
Trust
```

and:

```text
Integrity
≠
Reputation
≠
Trust
```

---

# Reputation Artifact Lifecycle

A Reputation Artifact may change because:

- new information becomes available;
- methodology changes;
- weighting changes;
- a Source correction occurs;
- a participant's behavior changes;
- a community changes its assessment;
- a Trust Statement is superseded;
- a scoring system is replaced.

A later change does not erase the earlier Integrity Reference.

Conceptually:

```text
Earlier Reputation Representation
        ↓
Earlier Integrity Reference

Later Reputation Representation
        ↓
Later Anchor Version or New Integrity Reference
where required
```

The final Versioning rule remains unfrozen.

---

# Source Reputation Change vs. Anchor Correction

A **Source Reputation Change** occurs when the Source Institution changes:

- the reputation score;
- methodology;
- assessment;
- label;
- ranking;
- trust signal;
- underlying reputation artifact.

An **Anchor Correction** occurs when Anchor incorrectly recorded its own integrity information.

Examples may include:

- wrong Source Artifact;
- wrong Source-System Identifier;
- wrong Canonical Representation;
- wrong Representation Boundary;
- wrong digest;
- wrong algorithm;
- wrong timestamp;
- wrong signer reference;
- wrong verification metadata.

Therefore:

```text
Source Reputation Change
≠
Anchor Correction
```

---

# Reputation Withdrawal or Replacement

A reputation assessment may later be withdrawn or replaced.

Anchor should preserve the historical integrity relationship of the earlier representation.

Where relevant, Anchor may later reference:

```text
withdrawn Source Artifact
replacement Source Artifact
later reputation representation
new Integrity Reference
```

without silently rewriting the prior record.

---

# Privacy and Fairness Boundary

Reputation systems may involve sensitive or evaluative information.

Anchor should not amplify such information merely because it is technically possible to anchor it.

Anchor should apply the minimum-necessary-data principle.

Potentially preferable approaches may include preserving:

- institutional identifiers rather than personal identifiers;
- canonical record references rather than copied personal data;
- cryptographic integrity material rather than full evaluative content;
- externally governed references rather than duplicated profiles.

The governing principle is:

> Preserve necessary integrity context. Do not amplify unnecessary reputation data.

---

# What Anchor Preserves

For a reputation-related Integrity Reference, Anchor may preserve:

- Anchor Identifier;
- Source Institution;
- Source-System Identifier;
- Reputation Artifact Type;
- Canonical Representation;
- Representation Boundary;
- Integrity Method;
- Integrity Value;
- algorithm metadata;
- timestamps;
- signer information;
- Verification Material;
- Anchor Version;
- Integrity State;
- Publication State;
- Lifecycle State;
- Correction lineage;
- verification history.

The final schema remains unfrozen.

---

# What Anchor Does Not Do

Anchor does not:

- calculate reputation;
- assign reputation scores;
- rank people;
- rank organizations;
- aggregate reputation history;
- maintain reputation profiles;
- determine credibility;
- determine trustworthiness;
- create reputation portability;
- define universal reputation semantics;
- endorse reputation methodologies;
- determine whether a reputation assessment is fair;
- become the Source authority for externally created reputation records.

---

# Relationship to Attestor

Attestor owns:

```text
Trust Statement
```

A Trust Statement may contain reputation-related reasoning or conclusions.

Anchor may preserve an Integrity Reference for the Trust Statement representation.

Anchor does not convert the Trust Statement into an Anchor reputation score.

---

# Relationship to Chronicle

Chronicle preserves qualifying historical memory through Chronicle Entries.

Those entries may be evidence used by another system when forming reputation.

Anchor may preserve the Integrity Reference for the Chronicle Entry or resulting reputation artifact.

It does not perform the reputation inference.

---

# Relationship to Certifier

Certifier owns Certification Packages and certification determinations.

A certification may influence reputation.

Anchor may preserve the integrity of the certification artifact or reputation artifact.

It does not translate certification status into reputation status.

---

# Relationship to Anchor Attestations

The `/anchor/attestations/` section now concerns attestation artifact integrity.

A reputation artifact may reference attestations.

An attestation artifact may reference reputation.

Anchor may preserve both without creating a combined reputation engine.

---

# Relationship to Anchor Integration

The preferred interoperability model is:

```text
Source Institution
        ↓
Authoritative Reputation Artifact
        ↓
Canonical Representation
        ↓
Anchor Integrity Reference
```

The Source Institution retains responsibility for reputation meaning.

---

# Reputation Principle

The governing principle is:

> Preserve reputation artifacts. Do not become a reputation system.

Anchor should preserve reputation-related integrity where it adds durable value and stop before calculation, scoring, ranking, interpretation, or trust judgment.

---

## Status

**Foundation Reconciliation**

This document replaces the pre-Suite model in which reputation was treated as an evolving Anchor trust-layer function.

The current model treats reputation as **externally governed information that may be represented in artifacts subject to Anchor integrity preservation**.

The following remain intentionally unfrozen:

```text
Reputation Artifact Type Controlled Values
reputation-related privacy requirements
methodology-artifact anchoring rules
score / signal representation rules
withdrawal / replacement handling
new Anchor Version vs. new Integrity Reference rule
reputation-specific schema conditions
first production reputation-related Integrity Reference
```

**Version:** 1.0-draft

**Maintained By:** Satoshium
