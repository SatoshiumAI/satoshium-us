# Satoshium Navigator — Certification Queries

**Path:** `/navigator/certification-queries/`  
**Institution:** Satoshium Navigator  
**Surface:** Certification Query Framework  
**Status:** Current repository documentation

## Purpose

This directory documents **Satoshium Navigator Certification Queries**.

Certification Queries define the structured operational questions Navigator asks across the Satoshium Suite to identify:

- certifications;
- certification opportunities;
- lifecycle conditions;
- supporting records;
- missing relationships;
- operational work requiring attention.

Navigator does not own certification data.

It orchestrates questions across authoritative systems and preserves references back to those systems.

## Institutional Role

Navigator expresses operational intent through structured questions.

A Certification Query should answer questions such as:

- What work requires attention?
- Which records meet a governed condition?
- Which expected relationships are absent?
- Which certification states require review?
- Which Suite institutions contain the authoritative records needed to continue a workflow?

Navigator uses the results to inform orchestration.

It does not become the source authority for the queried information.

## Reference-Based Query Model

Certification Queries operate through references to authoritative Suite institutions.

Current referenced institutions include:

- **Atlas**
- **Certifier**
- **Registry**
- **Chronicle**
- **Anchor**
- **Beacon**
- **Attestor**

Navigator may query across those systems without duplicating their records.

The governing principle is:

> **Query across authority; do not absorb authority.**

## Representative Certification Queries

The current public page identifies examples including:

- Find uncertified Atlas records.
- Find certifications due for initial review.
- Find certifications requiring additional evidence.
- Find expired certifications.
- Find certifications approaching expiration.
- Find certifications due for renewal.
- Find revoked certifications.
- Find suspended certifications.
- Find Registry Entries without certification.
- Find certifications without Registry Entries.
- Find certifications missing Chronicle events.
- Find certifications missing Anchor references.
- Find certifications without Beacon signals.
- Find certifications without Trust Statements.

These are operational questions.

They do not themselves:

- create a Certification Package;
- issue a certification decision;
- create a Registry Entry;
- create a Chronicle Entry;
- establish an Integrity Reference;
- publish a Beacon Discovery Signal;
- create an Attestation;
- produce a Trust Statement.

They identify conditions that may require governed follow-on work.

## Query Inputs

Certification Queries may use parameters such as:

- identifiers;
- certification classes;
- lifecycle states;
- jurisdictions;
- dates;
- evidence conditions;
- Registry status;
- trust-related conditions;
- workflow requirements.

Input parameters should reference authoritative source semantics wherever possible.

Navigator should not redefine another institution's controlled values merely for query convenience.

## Query Results

Query results identify operational work requiring attention.

A result should preserve enough context to determine:

- what condition matched;
- which institution owns the authoritative source record;
- which identifier or object was referenced;
- what workflow may be appropriate next;
- whether the result is informational or action-eligible.

A query result is an orchestration result, not a replacement for the underlying institutional record.

## Cross-System Queries

Navigator may evaluate questions spanning multiple Suite institutions.

Examples include identifying:

```text
Certification exists
        +
Registry Entry absent
```

or:

```text
Certification active
        +
Anchor relationship absent
```

or:

```text
Certification record exists
        +
no qualifying downstream Attestor Trust Statement found
```

The cross-system result does not transfer ownership of any participating record to Navigator.

## Missing-Relationship Queries

Several current Certification Queries identify missing downstream relationships.

Examples include:

- certification without Registry Entry;
- certification missing Chronicle event;
- certification missing Anchor reference;
- certification without Beacon signal;
- certification without Trust Statement.

These should be interpreted carefully.

A missing downstream object or relationship does not automatically mean:

- an error exists;
- the upstream record is invalid;
- the downstream institution is required to act;
- publication is required;
- eligibility has been established.

The query reveals an operational condition.

A later governed process determines whether action is appropriate.

## Relationship to Certifier

Certifier remains authoritative for:

- certification determinations;
- Certification Packages;
- certification lifecycle;
- certification status;
- Certifier evidence and validation structures.

Navigator may query Certifier records and certification states.

It does not reinterpret or replace the certification decision.

## Relationship to Registry

Navigator may compare certification records against Registry Entries.

Registry remains authoritative for SREG objects, Registry metadata, and Registry lifecycle.

A query result identifying a missing Registry relationship does not itself create a registration requirement or Registry Entry.

## Relationship to Chronicle

Navigator may query whether a certification has a related Chronicle Entry.

Chronicle remains authoritative for determining and preserving qualifying historical Occurrences.

A query such as `Find certifications missing Chronicle events` should be understood as an operational discovery question, not as a declaration that every certification requires a Chronicle Entry.

## Relationship to Anchor

Navigator may identify certifications without a relevant Anchor relationship.

Anchor retains authority over Integrity References and integrity-preservation processes.

The absence of an Anchor reference does not by itself imply invalidity or incompleteness unless a governing workflow establishes that requirement.

## Relationship to Beacon

Navigator may identify certification records without related Beacon discovery outputs.

Beacon retains authority over Discovery Signals, Discovery Metadata, provenance, lifecycle, and publication.

A query result does not require Beacon publication by itself.

## Relationship to Attestor

Navigator may identify certification records without related Attestor outputs.

Attestor retains authority over:

- Attestations;
- Eligibility;
- Rule-Constrained Evaluation;
- Evaluation Outcomes;
- Trust Statements.

A missing Trust Statement does not mean a certification lacks validity, confidence, or authority.

It means no matching governed Attestor Trust Statement was identified under the query conditions.

## Future Query Types

The current architecture contemplates future support for:

- scheduled queries;
- saved queries;
- parameterized workflows;
- automation triggers;
- APIs;
- machine-readable query definitions.

These remain implementation directions until separately established.

Future query capabilities should preserve the same institutional boundaries as current manual or interactive queries.

## Authority Discipline

Certification Queries should preserve the following distinctions:

- query result ≠ source record;
- query result ≠ certification decision;
- missing relationship ≠ institutional failure;
- missing object ≠ required object;
- search condition ≠ eligibility;
- search condition ≠ lifecycle decision;
- query match ≠ publication requirement;
- query match ≠ Trust Statement;
- reference ≠ ownership;
- reference ≠ support;
- connection ≠ identity.

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

## Suite Reconciliation Flag

The core Certification Query architecture is sound.

Suite Reconciliation should review a small set of terminology and semantic questions:

1. **`trust signals` in Query Inputs**  
   This phrase could be confused with legacy Attestor terminology or Beacon Discovery Signals. Current mature terminology should distinguish trust-related query conditions from formal Attestor Trust Statements and Beacon Discovery Signals.

2. **`Find certifications missing Chronicle events`**  
   Chronicle preserves qualifying Occurrences, not every event by default. The wording may benefit from clarification such as identifying certifications with no related qualifying Chronicle Entry.

3. **`Find certifications without Beacon signals`**  
   A missing Beacon Discovery Signal is an operational condition, not necessarily an omission requiring correction.

4. **`Find certifications without Trust Statements`**  
   The absence of an Attestor Trust Statement should not imply deficient certification status. Attestor Eligibility and Rule-Constrained Evaluation remain separate governed processes.

These are clarity and terminology issues, not architectural defects in the Navigator query model.

## Repository Expectations

Changes to this directory should preserve:

1. Navigator as the operational query/orchestration institution;
2. authoritative data ownership by source institutions;
3. reference-based cross-system querying;
4. repeatable and traceable operational results;
5. the distinction between identifying work and authorizing work;
6. the distinction between missing relationships and required relationships;
7. mature Beacon and Attestor terminology; and
8. the principle that reference does not transfer authority.

## Governing Principle

**Operational questions reveal operational work.**
