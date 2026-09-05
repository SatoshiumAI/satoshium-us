# Satoshium Beacon — Discovery Signal Lifecycle

## Overview

The **Discovery Signal Lifecycle** defines how a Beacon-owned **Discovery Signal** moves through governed institutional states over time.

This is the third component of:

```text
Beacon Phase II — Production Architecture
```

The Discovery Signal Entry Model established:

```text
Status
```

as a structural component of the canonical Beacon object.

The Lifecycle architecture determines what that status means, which conditions belong to the canonical object's lifecycle, which concepts are events or processes, and which concerns should remain separate dimensions.

---

## Purpose

The lifecycle exists to answer:

```text
What happens to a Discovery Signal after a potential discovery is identified?
```

Phase II began with the provisional sequence:

```text
Identified
→ Created
→ Reviewed
→ Published
→ Updated / Superseded / Resolved
```

That sequence was treated as an inquiry starting point rather than adopted automatically.

Review showed that it mixed several different architectural concepts:

```text
candidate discovery condition
event
process
lifecycle state
publication state
```

The Lifecycle architecture separates those concepts.

---

## Lifecycle Inquiry Result

The architectural distinction is:

```text
Identified
→ pre-object discovery condition

Created
→ object-creation event

Reviewed
→ institutional action / process

Published
→ publication state

Updated
→ action

Draft
Active
Superseded
Resolved
Withdrawn
→ canonical lifecycle states
```

This separation prevents every action or condition from being treated as though it were the same kind of institutional state.

---

## Pre-Object Condition — Identified

**Identified** describes a potential discovery that Beacon has recognized as a candidate for institutional treatment.

At this point:

```text
a canonical Discovery Signal may not yet exist
a permanent Beacon identifier may not yet exist
the observation may still be rejected
the observation may still be abandoned
institutional review may not yet have begun
```

Therefore:

```text
Identified
≠
canonical Discovery Signal lifecycle state
```

It belongs to discovery intake or pre-object processing.

Conceptually:

```text
Potential Discovery
        ↓
Identified
        ↓
Decision to Create
        ↓
Canonical Discovery Signal
```

---

## Creation Event — Created

**Created** describes the event that brings the canonical Beacon Discovery Signal into existence.

Creation establishes:

```text
Beacon-owned object existence
initial identity
initial content
creation timestamp
initial institutional state
```

The resulting lifecycle state is:

```text
Draft
```

Therefore:

```text
Created
→ event

Draft
→ lifecycle state
```

This distinction allows the system to preserve both what happened and what state resulted from it.

---

## Review — Institutional Action

**Reviewed** is best understood as an institutional action or process rather than a durable lifecycle state.

Review may:

```text
evaluate the Draft
identify required revisions
confirm required information
evaluate source attribution
evaluate provenance
support validation
support progression toward publication
return the object for additional work
```

A signal does not need to remain permanently in a state called:

```text
Reviewed
```

Instead, review history can later be preserved through process records, timestamps, provenance, methodology, or other governed metadata.

---

## Publication — Separate State Dimension

**Published** describes public availability.

It does not fully describe the institutional lifecycle condition of a Discovery Signal.

For example:

```text
Active + Published
Superseded + Published
Resolved + Published
Withdrawn + Published
```

may all be meaningful combinations depending on later Publication architecture.

A superseded signal may remain public because removing it would destroy historical traceability.

Likewise, a resolved signal may remain discoverable even though it is no longer active.

Therefore:

```text
Lifecycle State
≠
Publication State
```

The initial publication dimension is:

```text
Unpublished
Published
```

Exact publication rules belong to:

```text
/beacon/publication/
```

---

# Canonical Lifecycle States

The Discovery Signal Lifecycle establishes the following architectural state model:

```text
Draft
→ Active
→ Superseded / Resolved / Withdrawn
```

The five canonical lifecycle states are:

1. Draft
2. Active
3. Superseded
4. Resolved
5. Withdrawn

---

## 1. Draft

A **Draft** Discovery Signal exists as a Beacon-owned canonical object but has not yet completed the institutional process required for active standing.

A Draft may have:

```text
canonical object identity
initial subject
Signal Type
source
provenance
canonical references
Discovery Metadata
timestamps
version information
relationships
```

but may still require:

```text
review
revision
validation
publication decision
```

A Draft should not automatically be treated as publicly authoritative Beacon output.

Conceptually:

```text
Discovery Signal Created
        ↓
Draft
```

Draft begins the lifecycle of the canonical Beacon object.

---

## 2. Active

An **Active** Discovery Signal is the current institutionally accepted Beacon signal for the discovery it represents.

Active means the signal has satisfied the production conditions required for current institutional standing.

An Active signal may:

```text
be published
remain subject to later observation
receive governed updates
be superseded
be resolved
be withdrawn
```

Active describes the current standing of the Beacon Discovery Signal.

It does not describe or transfer the authority of its source.

Therefore:

```text
Active Beacon Signal
≠
authoritative source object
```

---

## 3. Superseded

A **Superseded** Discovery Signal has been replaced by a later Beacon signal or governed version that now carries the current discovery context.

Supersession should preserve:

```text
the prior signal
the replacement reference
the supersession relationship
the reason or basis when appropriate
the relevant timestamps
```

Supersession should not silently overwrite institutional history.

A Superseded signal may have been valid and appropriate when originally issued.

Therefore:

```text
Superseded
≠
Invalid
```

Conceptually:

```text
Active Signal A
        ↓
Later governed replacement
        ↓
Signal A → Superseded
Signal B → Current
```

The exact relationship between versioning and creation of a separate replacement signal remains subject to:

```text
/beacon/versioning/
```

---

## 4. Resolved

A **Resolved** Discovery Signal no longer requires active discovery attention because the condition represented by the signal has reached a governed conclusion or closure.

Resolution should preserve:

```text
resolution basis
supporting source or reference
resolution timestamp
relevant relationship
historical traceability
```

A Resolved signal is not deleted.

Conceptually:

```text
Active
        ↓
Supported closure condition
        ↓
Resolved
```

Resolution describes Beacon's treatment of the Discovery Signal.

It does not claim that the source institution has independently resolved its own object unless the authoritative source actually says so.

---

## 5. Withdrawn

A **Withdrawn** Discovery Signal has been intentionally removed from active institutional standing by Beacon.

Possible reasons may include:

```text
error
invalid discovery basis
unsupported classification
material defect
institutional withdrawal
```

Withdrawal should preserve:

```text
withdrawal reason
withdrawal timestamp
prior existence
relevant history
```

Withdrawal differs from both Superseded and Resolved.

```text
Superseded
→ a later governed object or version replaces the signal

Resolved
→ the discovery condition reaches supported closure

Withdrawn
→ Beacon determines the signal itself should no longer stand
```

Withdrawal should not erase the historical fact that the signal existed.

---

## Why Archived Is Not a Lifecycle State Yet

An **Archived** state was considered but is not currently required.

The existing states already preserve meaningful institutional conditions:

```text
Superseded
Resolved
Withdrawn
```

Each can remain historically preserved.

An archival storage condition does not automatically represent a distinct institutional meaning.

Therefore:

```text
Archived
→ not frozen
```

It should be added only if production demonstrates that Beacon requires a separate institutional archival state.

---

# Publication State

Publication remains separate from lifecycle.

Initial architectural values are:

```text
Unpublished
Published
```

This produces a two-dimensional model:

```text
Lifecycle State
+
Publication State
```

Examples:

```text
Draft + Unpublished

Active + Published

Superseded + Published

Resolved + Published

Withdrawn + Published
```

Whether every combination will ultimately be permitted remains subject to the Publication Model and Validation architecture.

---

## Update Is an Action

**Updated** is not established as a permanent lifecycle state.

An update is an action performed on a Discovery Signal.

Its governed consequence may involve:

```text
new version
changed metadata
changed observation information
supersession
new Discovery Signal
```

depending on later Versioning architecture.

Therefore:

```text
Updated
→ action

Version / Supersession
→ governed consequence
```

This prevents temporary actions from being confused with durable institutional states.

---

# Conceptual Lifecycle Flow

The resulting architecture is:

```text
Candidate Discovery
        ↓
Identified
        ↓
Decision to Create
        ↓
Discovery Signal Created
        ↓
Draft
        ↓
Review / Validation / Publication Decision
        ↓
Active
        ↓
Later Observation or Institutional Action
        ↓
Superseded / Resolved / Withdrawn
```

Publication runs alongside the lifecycle:

```text
Unpublished
↔
Published
```

according to rules that will be defined later.

---

## Lifecycle State vs. Source Status

Beacon's lifecycle describes:

```text
the Discovery Signal
```

It does not describe the lifecycle of the referenced source object.

The distinction is:

```text
Beacon Lifecycle State
→ condition of the Beacon Discovery Signal

Source Status
→ condition maintained by the authoritative source institution
```

For example, a Certification Package may change status within Certifier.

Beacon may observe that change and:

```text
update a Discovery Signal
create a new Discovery Signal
supersede a prior Discovery Signal
resolve a Discovery Signal
```

But Beacon does not own the Certification Package status.

---

## Transition Discipline

Lifecycle transitions should eventually require a traceable institutional basis.

Expected principles include:

```text
Draft → Active
only after required production conditions are satisfied

Active → Superseded
only when a governed replacement exists

Active → Resolved
only when a supported resolution basis exists

Draft or Active → Withdrawn
only with a preserved institutional reason
```

Prior states and transition history should remain traceable.

The exact transition gates remain subject to later:

```text
Validation
Versioning
Publication
Methodology
Production
```

architecture.

---

## Transition History

The lifecycle should preserve enough information to reconstruct meaningful institutional change.

Conceptually, transition history may eventually include:

```text
prior state
new state
transition timestamp
transition reason
supporting reference
responsible process or actor
related replacement object
```

The exact representation is not frozen here.

It may become part of:

```text
Discovery Metadata
Versioning
Provenance
Validation output
production history
```

depending on later architecture.

---

## What Remains Unfrozen

This page establishes the lifecycle architecture without prematurely deciding every implementation rule.

The following remain open:

```text
machine-readable lifecycle enum values
transition validation rules
transition authorization
whether Draft receives permanent identifier immediately
update mechanics
version mechanics
supersession mechanics
resolution evidence requirements
withdrawal authorization
Publication Gate design
publication/lifecycle combination rules
transition-history schema
```

These decisions should be resolved only when their dedicated Phase II architecture is reached.

---

## Authority Boundary

A Beacon lifecycle transition changes only the institutional condition of the Beacon Discovery Signal.

It does not alter the authoritative state of the referenced source.

Therefore:

```text
Beacon lifecycle change
≠
source lifecycle change

Beacon resolution
≠
source resolution

Beacon withdrawal
≠
source withdrawal

Beacon supersession
≠
source supersession
```

Unless the source institution independently performs the corresponding action.

The governing rule remains:

> **Reference does not transfer authority.**

---

## Relationship to the Entry Model

The Entry Model established:

```text
Status
```

as a structural component.

Lifecycle architecture now gives that component two distinct dimensions:

```text
Lifecycle State
→ Draft
→ Active
→ Superseded
→ Resolved
→ Withdrawn

Publication State
→ Unpublished
→ Published
```

The later production schema will determine how these values are represented machine-readably.

---

## Relationship to Signal Types

Signal Type and Lifecycle State answer different questions.

```text
Signal Type
→ What kind of discovery is this?

Lifecycle State
→ What is the current institutional condition of this Discovery Signal?
```

For example:

```text
Signal Type → Certification
Lifecycle State → Active
Publication State → Published
```

or:

```text
Signal Type → Integrity
Lifecycle State → Superseded
Publication State → Published
```

These dimensions should remain independently interpretable.

---

## Relationship to Versioning

Lifecycle and Versioning are closely related but not identical.

A change may:

```text
update the current object
produce a new version
produce a replacement signal
supersede a prior signal
```

The exact rules governing those outcomes belong to:

```text
/beacon/versioning/
```

The Lifecycle architecture establishes only that:

```text
Superseded
```

is a meaningful institutional state when a governed replacement becomes current.

---

## Relationship to Publication

Publication architecture will determine:

```text
when Draft may become Active
when publication occurs
whether Active requires Published
whether Withdrawn remains public
how superseded signals are represented publicly
how resolved signals are represented publicly
whether publication can be reversed
```

This Lifecycle architecture deliberately avoids deciding those questions prematurely.

---

## Current Status

As of September 5, 2026:

```text
Institution → Beacon
Suite Role → Discovery & Signals
Canonical Responsibility → Discovery Signal / Metadata
Status → Continuing Development
Phase → Phase II — Production Architecture

Discovery Signal Entry Model → Defined
Discovery Signal Types → Defined
Discovery Signal Lifecycle → Defined

Canonical Lifecycle States:
Draft
Active
Superseded
Resolved
Withdrawn

Publication Dimension:
Unpublished
Published

Transition Enforcement → Pending
Machine-Readable Values → Pending
Production Proof → Pending
First Production Discovery Signal → Not yet created
Operational → No
```

---

## Phase II Progress

```text
1. Discovery Signal Entry Model
   → COMPLETE

2. Discovery Signal Types
   → COMPLETE

3. Discovery Signal Lifecycle
   → COMPLETE

4. Beacon Identifier Standard
   → NEXT

5. Beacon Schemas

6. Validation

7. Discovery Provenance

8. Authority & Reference Model

9. Relationship Model

10. Versioning & Supersession

11. Publication Model

12. Discovery Signals Register

13. Individual Discovery Signal

14. Beacon Discovery Methodology

15. Production Model / First Operation
```

---

## Governing Principles

The Discovery Signal Lifecycle follows these principles:

```text
Distinguish conditions from events.

Distinguish actions from states.

Separate lifecycle from publication.

Preserve prior institutional history.

Never silently rewrite a superseded signal.

Preserve reasons for resolution and withdrawal.

Do not confuse Beacon status with source status.

Freeze transition rules only when their dedicated architecture is reviewed.
```

The lifecycle principle is:

> **Preserve the state. Preserve the transition. Preserve the reason.**

And the Suite-wide authority rule remains:

> **Reference does not transfer authority.**

---

## Next Phase II Step

The next production-architecture page is:

```text
/beacon/identifiers/
```

Its purpose is to establish the canonical identifier convention for Beacon Discovery Signals.

---

## Last Updated

September 5, 2026
