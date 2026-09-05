# Query Log Schema

## Purpose

The **Query Log Schema** defines an optional operational structure for preserving information about discovery requests processed by or involving Beacon.

Query history may support:

```text
traceability
reproducibility
review
audit
operational analysis
discovery improvement
```

A Query Log is not Beacon's canonical production object.

---

## Schema Role

```text
Role → Optional Operational History
Canonical Beacon Object → No
Canonical Beacon Identifier → Not established
```

Beacon's canonical production object remains:

```text
Discovery Signal
```

with identifier:

```text
BEAC-YYYY-NNNN
```

---

# Relationship to Navigator

Navigator owns:

```text
Workflow Definition / Orchestration
```

Beacon may receive or process discovery activity within a Navigator-directed workflow.

Conceptually:

```text
Navigator
→ workflow / query context
→ Beacon discovery
```

This schema must not redefine Navigator's orchestration authority.

---

# Query Structure

Potential Query Log information may include:

```text
query_reference
query_type
title
query_text
objective
scope
parameters
discovery_method
sources_consulted
related_results
related_signals
submitted_by
workflow_reference
timestamps
processing_metadata
status
notes
```

Because Query Logs are operational rather than canonical objects, exact required fields remain unfrozen.

---

## Query Reference

The previous schema assigned:

```text
QRY-YYYY-NNNNNN
```

as a permanent identifier.

That convention is not frozen in the current architecture.

Reason:

```text
persistent Query Logs have not yet been proven necessary as canonical institutional objects
```

If persistent query identity becomes operationally necessary, a separate identifier rule may later be established.

For now, implementations may preserve a local or workflow reference without implying canonical Beacon identity.

---

## Query Type

Possible descriptive query types may include:

```text
Search
Research
Investigative
Exploratory
Relationship
Automated
```

These values are operational descriptors rather than frozen canonical vocabulary.

---

## Query Text

Preserves the original request when retention policy permits.

---

## Objective

Describes the intended discovery outcome.

---

## Scope

Potential query scope may include:

```text
jurisdiction
time range
topic
object type
source type
domain
other discovery boundary
```

---

## Parameters

Optional structured parameters used to perform discovery.

---

## Discovery Method

Potential methods may include:

```text
Search
Index Lookup
Relationship Mapping
Cross-System Discovery
Manual Review
```

Future methodology may refine these terms.

---

## Sources Consulted

Preserve attributable source references where practical.

Examples may include:

```text
Atlas
Certifier
Registry
Chronicle
Anchor
Attestor
external sources
```

A source consultation does not transfer source authority to Beacon.

---

## Related Results

If Discovery Results are persisted, the query may reference them.

---

## Related Signals

A query may reference Discovery Signals that were surfaced, reviewed, or created in connection with the activity.

Example:

```yaml
related_signals:
  - BEAC-2026-0001
```

The query does not own those signals.

---

## Submitted By

When appropriate and permitted, preserve the actor, system, process, or workflow responsible for the request.

Examples:

```text
User
Navigator
Beacon process
Automated process
```

This field requires privacy-aware implementation.

---

## Workflow Reference

When a query originates in Navigator, preserve the Navigator workflow reference rather than duplicating workflow authority inside Beacon.

---

## Timestamps

Potential timestamps include:

```text
submitted_at
started_at
completed_at
last_updated_at
```

Exact requirements remain operational.

---

## Processing Metadata

Optional operational information may include:

```text
processing duration
result count
source count
error information
```

This metadata should not be confused with Discovery Signal Metadata.

---

## Query Status

The previous schema proposed:

```text
Submitted
Processing
Completed
Archived
Failed
```

These remain useful candidate operational states but are not frozen as canonical Beacon lifecycle values.

If Query Logs become persistent production artifacts, their state model should be governed separately.

---

# Privacy and Retention

Query Logs may contain:

```text
user intent
search terms
sensitive research topics
workflow context
identifiable actor information
```

Therefore retention must not be assumed.

A future operational implementation should explicitly determine:

```text
whether query text is stored
whether actors are identified
whether data is anonymized
retention period
deletion policy
access controls
aggregate analytics policy
```

Until those rules exist, Query Logs should be treated as optional and privacy-sensitive.

---

# Conceptual Example

```yaml
query_reference: navigator-workflow-step-004
query_type: Research
title: Digital Asset Friendly Jurisdictions

query_text: >
  Find jurisdictions with favorable digital asset policies.

objective: >
  Identify jurisdiction information relevant to digital asset businesses.

scope:
  geography: Global
  topic: Digital Assets

discovery_method: Cross-System Discovery

sources_consulted:
  - Atlas
  - Registry
  - Chronicle

related_signals:
  - BEAC-2026-0001

submitted_by: Navigator

workflow_reference: NAV-WORKFLOW-EXAMPLE

timestamps:
  submitted_at: 2026-09-05T00:00:00Z
  completed_at: 2026-09-05T00:00:03Z

processing_metadata:
  result_count: 27
```

This example is conceptual only.

---

# Relationship to Discovery Results

Conceptually:

```text
Query
→ Discovery Activity
→ Discovery Result
```

A Discovery Result may later contribute to creation or review of a Discovery Signal.

---

# Relationship to Discovery Signals

A query does not automatically create a canonical signal.

Conceptually:

```text
Query
        ↓
Discovery
        ↓
Result
        ↓
Institutional evaluation
        ↓
Possible Discovery Signal
```

---

# Analytics

Future implementations may use privacy-governed query history for:

```text
discovery optimization
query trends
search improvement
relationship analysis
workflow analysis
user experience improvement
```

Analytics must not silently convert private query history into public Beacon records.

---

# Authority Boundary

A query may ask Beacon to discover authoritative information.

The query itself carries no source authority.

Beacon should preserve the distinction between:

```text
request
discovery activity
result
canonical signal
source authority
```

> **Reference does not transfer authority.**

---

# Status

```text
Schema Role → Optional Operational History
Canonical Object → No
Permanent Identifier → Not established
Privacy Rules → Pending
Retention Rules → Pending
Lifecycle → Not frozen
Machine Validation → Pending if retained
```

---

## Last Updated

September 5, 2026
