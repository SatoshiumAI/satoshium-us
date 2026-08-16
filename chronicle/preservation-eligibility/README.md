# Chronicle Preservation Eligibility Model

## Purpose

The Chronicle Preservation Eligibility Model defines how Satoshium Chronicle determines whether an Occurrence should be admitted into the historical record through a canonical Chronicle Entry.

Preservation Eligibility is Chronicle's institutional admission rule.

It answers:

> Should Chronicle preserve this Occurrence?

This model also incorporates **Historical Significance** as a principal rationale for preservation.

Historical Significance therefore does not require a separate institutional page at this stage.

It answers:

> Why is this Occurrence worth preserving?

Keeping these concepts together reflects their operational relationship:

```text
Occurrence
    ↓
Preservation Eligibility
    ├── Automatic Preservation Basis
    └── Historical-Significance / Discretionary Basis
    ↓
Chronicle Entry
```

A separate Historical Significance page should be created only if future operational experience demonstrates that significance develops into an independent system requiring its own governance, controlled vocabulary, procedures, or records.

---

# Institutional Role

Chronicle is selective by design.

It is not:

* A universal log
* A mirror of every Suite record
* A record of every lifecycle transition
* A feed of every technical action
* A repository for every Source
* A repository for every Evidence item
* A historical dump of all observable activity

Chronicle preserves qualifying historical Occurrences.

Conceptually:

> Logs preserve activity.  
> Chronicle preserves history.

Preservation Eligibility is the boundary that makes this distinction operational.

---

# Position in the Chronicle Process

Preservation Eligibility occurs before production Entry creation.

Conceptually:

```text
Occurrence Identified
        ↓
Preservation Eligibility
        ↓
If Eligible
        ↓
Chronicle Entry Model
        ↓
Chronicle Entry Creation
        ↓
Verification / Validation / Publication
        ↓
Historical Preservation
```

The Entry Model determines how an admitted Occurrence is represented.

Preservation Eligibility determines whether the Occurrence should be admitted at all.

---

# Eligibility Principles

Chronicle should preserve an Occurrence when there is a defensible institutional reason for doing so.

Eligibility should be:

* Explainable
* Consistent
* Reviewable
* Historically grounded
* Institutionally bounded
* Resistant to arbitrary inclusion
* Flexible enough for retrospective history

Chronicle should not require every eligible Occurrence to satisfy the same combination of factors.

Different Event Types may have different preservation bases.

---

# Eligibility Criteria

Potential eligibility criteria include the following.

## Institutional Relevance

The Occurrence materially relates to:

* Satoshium
* A Satoshium Suite institution
* A Suite authoritative object
* Governance
* Architecture
* Interoperability
* Public operation
* Institutional identity
* Another recognized area of Satoshium history

Mere mention of Satoshium does not automatically establish Institutional Relevance.

---

## Historical Significance

The Occurrence has enduring value for understanding how Satoshium developed, changed, operated, or established continuity.

Historical Significance is a principal discretionary preservation rationale.

It should be documented when it materially supports the eligibility decision.

---

## Lifecycle Significance

The Occurrence represents a meaningful lifecycle event.

Examples may include:

* Creation
* Issuance
* Renewal
* Suspension
* Revocation
* Expiration
* Completion
* Retirement
* Replacement
* Major transition

Not every lifecycle action is automatically historically significant.

---

## First / Last / Milestone Significance

The Occurrence may qualify because it represents:

* First occurrence
* Last occurrence
* Inaugural action
* Terminal action
* Major threshold
* Major numerical milestone
* First use of a system
* First inter-system relationship
* First production record
* Major institutional milestone

This factor may make an otherwise ordinary event historically important.

---

## Governance Significance

The Occurrence materially changes:

* Rules
* Standards
* Methodology
* Institutional authority
* Scope
* Governance procedures
* Publication rules
* Validation rules
* Preservation rules

Governance changes often possess historical value because they alter how the institution operates.

---

## Architectural Significance

The Occurrence materially changes:

* System architecture
* Canonical objects
* Data models
* Schema architecture
* Interoperability
* Suite boundaries
* Authority relationships
* Production architecture

Not every technical implementation change qualifies.

The change should have durable architectural meaning.

---

## Relationship Significance

The Occurrence establishes, changes, or terminates a historically meaningful relationship.

Potential examples may involve:

* Certifier and Registry
* Certifier and Chronicle
* Registry and Chronicle
* Anchor relationships
* Attestor relationships
* Cross-Suite references
* Institutional dependencies

Relationship significance should not be confused with the technical existence of a Relationship field.

---

## Evidentiary or Interpretive Importance

An Occurrence may qualify because preserving it materially improves understanding of another historical record or institutional development.

Examples may include:

* An event explaining why a later Correction occurred
* A governance decision explaining a later schema change
* A Source publication materially changing historical interpretation
* A significant contradictory record

This category should be used cautiously.

Chronicle should not become an archive of every interpretive development.

---

## Continuity Value

An Occurrence may be worth preserving because it fills a necessary historical gap.

An event with modest standalone significance may still be important if future reviewers cannot reconstruct an institutional sequence without it.

Continuity Value supports Chronicle's role as institutional memory.

---

# Eligibility Is Not a Numerical Score

Chronicle should not initially assign arbitrary point values to eligibility criteria.

For example:

```text
Institutional Relevance = 5
Lifecycle Significance = 3
Historical Significance = 4
```

would create artificial precision without operational evidence that such scoring improves decisions.

Chronicle should initially use reasoned institutional determinations.

If future production scale demonstrates a genuine need for scoring, that system should be developed separately and validated against real preservation decisions.

---

# Eligibility Paths

Chronicle may recognize more than one path to Preservation Eligibility.

## Automatic Preservation

An approved class of Occurrences is institutionally presumed to require preservation.

## Discretionary Preservation

An Occurrence is assessed using eligibility factors and Historical Significance.

## Retrospective Preservation

An earlier Occurrence becomes eligible after later history reveals its significance.

These paths should produce the same canonical outcome:

```text
Preservation Eligible
        ↓
Chronicle Entry
```

---

# Automatic Preservation Classes

Chronicle may eventually approve limited Automatic Preservation Classes.

An Automatic Preservation Class means:

> Chronicle has already determined that Occurrences in this defined class ordinarily possess sufficient institutional historical value to warrant preservation.

Automatic preservation should remain narrow.

It should not become a shortcut for broad Event Type admission.

---

## Requirements for an Automatic Class

An Automatic Preservation Class should be approved only when:

* The class is clearly defined
* Repeated Occurrences demonstrate durable historical relevance
* Individual discretionary review adds little value
* Automatic preservation will not overwhelm Chronicle with routine noise
* Applicable exclusion rules remain available
* Event-Type and profile requirements are sufficiently mature

---

## Automatic Preservation Does Not Bypass Production Rules

Automatic eligibility does not mean automatic publication.

Even an automatically eligible Occurrence must still satisfy applicable:

* Entry Model requirements
* Identifier rules
* Event Type rules
* Event-Type Profile requirements
* Authoritative-reference requirements
* Source requirements
* Evidence requirements
* Provenance requirements
* Verification
* Validation
* Publication procedures
* Versioning and preservation rules

Automatic means the admission question is already answered.

It does not mean the record is automatically valid.

---

## Initial Automatic Preservation Classes

No broad Automatic Preservation Class should be frozen during the initial Preservation Eligibility Model.

Certification operational experience should determine whether certain classes deserve automatic preservation.

Potential candidates may later include historically fundamental events such as:

* First production certification
* First production Chronicle Entry
* Major governance changes
* First operation of a new Suite institution

These are examples only.

They are not yet canonical Automatic Preservation Classes.

---

# Discretionary Consideration

Most early Chronicle preservation decisions should remain discretionary.

Discretionary consideration should review:

* Scope
* Event Type
* Institutional Relevance
* Historical Significance
* Lifecycle significance
* Milestone significance
* Governance or architectural significance
* Relationship significance
* Evidentiary or interpretive importance
* Continuity Value
* Exclusion criteria

The decision should preserve enough rationale to explain why Chronicle admitted or rejected the Occurrence.

---

# Historical-Significance Rationale

Where Historical Significance forms a material part of the preservation decision, Chronicle should preserve a concise rationale.

The rationale should answer:

> Why does this Occurrence possess durable historical value?

Potential rationale concepts may include:

```text
Institutional Change
Lifecycle Significance
First / Last / Milestone
Governance Significance
Architectural Significance
Relationship Significance
Evidentiary / Interpretive Importance
Continuity Value
```

These are working significance factors.

They should not yet be treated as a frozen Controlled Value vocabulary.

---

## Significance Is Contextual

Historical Significance depends on context.

An apparently small event may be highly significant.

Example:

```text
A single first production Chronicle Entry
```

may involve only one record creation action but represent the operational beginning of an entire institution.

Conversely, a technically large event may have little historical significance if it is routine.

Chronicle should evaluate meaning, not merely scale.

---

# Exclusion Criteria

An Occurrence should ordinarily not become a Chronicle Entry when one or more exclusion conditions apply and no stronger preservation basis overrides them.

Potential exclusion categories include:

* Routine Activity
* Trivial Occurrence
* Exact Duplicate
* Administrative Noise
* Unsupported Speculation
* Out-of-Scope Activity
* Purely Technical Maintenance
* Redundant Representation
* Insufficient Distinct Occurrence

---

## Routine Activity

Routine activity should ordinarily remain in operational systems, logs, Registry records, audit records, or other appropriate storage.

Examples may include:

* Routine automated processing
* Regular validation runs
* Ordinary maintenance
* Routine synchronization
* Standard publication processing
* Minor recurring lifecycle administration

Routine activity may become historically significant under unusual circumstances.

---

## Trivial Occurrence

A trivial Occurrence has no meaningful enduring value for:

* Institutional history
* Lifecycle understanding
* Governance
* Architecture
* Relationships
* Interpretation
* Continuity

Triviality should not be judged solely by technical size.

---

## Administrative Noise

Administrative actions should not become Chronicle Entries merely because they generate records.

Potential examples include:

* Formatting changes
* Typographical fixes without historical significance
* Internal file movement
* Metadata cleanup
* Automated housekeeping
* Routine index rebuilding
* Non-material deployment actions

---

## Unsupported Speculation

Chronicle preserves history.

It should not create historical Entries for:

* Rumors
* Predictions
* Possible future events
* Proposed actions that never occurred
* Unverified speculation presented as occurrence

A proposal itself may be historically preservable if the proposal's existence is the qualifying Occurrence.

---

## Out-of-Scope Activity

An external Occurrence should not be preserved merely because it is interesting.

It must have a legitimate historical relationship to Satoshium sufficient to fall within Chronicle Scope.

---

# Duplicate Occurrence Handling

Chronicle should distinguish between:

* One Occurrence described by multiple records
* Multiple distinct Occurrences that are related

The first situation should ordinarily produce one Chronicle Entry.

Conceptually:

```text
One Occurrence
    ↓
One Canonical Chronicle Entry
    ├── Multiple Sources
    ├── Multiple Evidence Records
    ├── Multiple Authoritative References
    └── Multiple Relationships
```

Chronicle should not create duplicate Entries merely because multiple systems or Sources reference the same historical Occurrence.

---

## Distinct Later Occurrences

A later change involving the same object may represent a new Occurrence.

Example:

```text
Certification Created
Certification Suspended
Certification Revoked
```

These are separate historical Occurrences even though they concern the same Certification Package.

Each must independently satisfy applicable Preservation Eligibility rules unless governed by an Automatic Preservation Class.

---

# Trivial Occurrence Handling

Chronicle should avoid two opposite errors.

## Over-Preservation

Preserving every small action until institutional history becomes indistinguishable from logs.

## Under-Preservation

Discarding a small event that later proves foundational.

The correct question is not:

> Was this event large?

The correct question is:

> Does preserving this Occurrence materially improve institutional historical memory?

---

# Event Type and Preservation Eligibility

Event Type and Preservation Eligibility are separate.

### Event Type

Answers:

> What kind of Occurrence is this?

### Preservation Eligibility

Answers:

> Should Chronicle preserve it?

Conceptually:

```text
Occurrence
    ↓
Event Type Classification
    +
Preservation Eligibility
    ↓
Chronicle Entry
```

The exact sequencing during workflow may vary, because preliminary Event Type identification may assist the eligibility decision.

Institutionally, however, classification does not equal admission.

---

# Event Type as an Eligibility Basis

Chronicle may later approve rules such as:

```text
Approved Event Type
        +
Required Conditions
        =
Automatically or Presumptively Eligible
```

This should occur only through explicit governance.

The existence of an Event Type alone does not mean every matching Occurrence should be preserved.

---

# Preservation Eligibility and Evidence

Preservation Eligibility is distinct from Evidence sufficiency.

An Occurrence may be:

* Clearly historically significant but incompletely evidenced
* Strongly evidenced but historically trivial
* Authoritatively established but outside Chronicle Scope
* Disputed but historically important

Chronicle should not collapse these questions.

Conceptually:

```text
Historical Importance ≠ Evidence Quality
Eligibility ≠ Verification
Eligibility ≠ Validation
```

Evidence limitations should be documented within the Entry if preservation proceeds.

---

# Preservation Eligibility and Verification

Verification occurs after or during Entry development.

It should not substitute for the admission decision.

An Occurrence may be eligible for preservation even if Chronicle Verification later identifies:

* Conflicting Sources
* Incomplete Provenance
* Unresolved Evidence
* Historical uncertainty

The Verification State should preserve that uncertainty.

---

# Preservation Eligibility and Validation

Validation determines whether Chronicle's record conforms to structure and procedure.

A structurally valid record is not automatically historically eligible.

Likewise, an eligible Occurrence cannot bypass Validation simply because it is historically important.

---

# Retrospective Preservation Eligibility

Historical meaning may emerge later.

Chronicle therefore permits retrospective eligibility.

Conceptually:

```text
Occurrence happens
        ↓
Initially not preserved
        ↓
Later history establishes significance
        ↓
Retrospective Eligibility Review
        ↓
Chronicle Entry created
```

The Chronicle Entry must preserve the original Event Date.

It should separately record Entry creation and publication dates.

---

# Eligibility Decision States

The model requires a clear institutional outcome.

Conceptually, decisions may include:

```text
Eligible
Not Eligible
Deferred
```

### Eligible

The Occurrence may proceed into Chronicle Entry creation.

### Not Eligible

Chronicle should not create a canonical Entry for the Occurrence.

### Deferred

The eligibility decision remains unresolved because additional context, authority, or historical development may be necessary.

These are conceptual states only.

Final decision-state values should be governed through Controlled Values.

---

# Reconsideration

A prior Not Eligible or Deferred decision may be reconsidered if new historical context emerges.

This is particularly important for retrospective preservation.

Reconsideration should not imply that the earlier decision was necessarily incorrect.

Historical significance can genuinely change as later events reveal context.

---

# Preservation Eligibility and Corrections

Preservation Eligibility concerns admission of an Occurrence.

Corrections concern changes to Chronicle-owned records after creation.

Chronicle should not use a Correction Record merely to document an eligibility decision.

If eligibility review eventually becomes complex enough to justify its own supporting record type, that decision should be made separately during operational development.

---

# Preservation Eligibility and Historical Preservation

The existing Historical Preservation architecture defines Chronicle's broader preservation mission.

The Preservation Eligibility Model defines the admission gate within that mission.

Conceptually:

```text
Historical Preservation
        ↓
Preservation Eligibility
        ↓
Chronicle Entry
        ↓
Long-Term Historical Continuity
```

The two pages therefore complement rather than duplicate one another.

---

# Why Historical Significance Stays Here

Historical Significance is currently inseparable from the admission decision.

A separate page would risk duplicating:

* Eligibility factors
* Milestone logic
* Governance importance
* Architectural importance
* Relationship significance
* Continuity Value
* Retrospective preservation

At this stage:

```text
Preservation Eligibility = Institutional Decision
Historical Significance = Principal Rationale
```

They should remain together.

A separate Historical Significance page should be created only if operational experience later establishes:

* Independent significance records
* Separate controlled vocabularies
* Formal significance review procedures
* Distinct governance
* Independent publication
* Scoring or assessment systems
* Other substantial standalone architecture

---

# Initial Operational Application

The first operational application of Preservation Eligibility will occur within the Certification Event framework.

Chronicle should evaluate which certification Occurrences deserve preservation.

Potential cases may include:

* First certification
* Creation of a historically significant certification
* Material renewal
* Historically significant suspension
* Historically significant revocation
* Historically significant expiration

The fact that an action belongs to the Certification Event family does not automatically require preservation.

Operational experience should determine whether certain certification events later become Automatic Preservation Classes.

---

# Preservation Eligibility Decision Model

A practical conceptual review may follow:

```text
1. Identify Occurrence
2. Confirm Chronicle Scope
3. Identify preliminary Event Type
4. Check Automatic Preservation Classes
5. Review Exclusion Criteria
6. Assess Historical Significance / other Eligibility Factors
7. Identify duplicate or prior Entry
8. Decide Eligible / Not Eligible / Deferred
9. Preserve rationale where required
10. If Eligible → Proceed to Chronicle Entry creation
```

This is a conceptual model.

The formal Production Procedure may later refine sequence and actor responsibilities.

---

# Model Principle

Chronicle should preserve enough history to maintain durable institutional memory without preserving so much routine activity that historical meaning disappears into noise.

Conceptually:

> Preserve what matters.  
> Preserve why it matters.  
> Do not confuse activity with history.

And operationally:

> Logs preserve activity. Chronicle preserves history.

---

## Relationship to Other Chronicle Documentation

The Preservation Eligibility Model should remain aligned with:

* Purpose
* Scope
* Definitions
* Historical Preservation
* Entry Model
* Event Type Framework
* Records
* Evidence
* Verification
* Trust Model
* Schemas
* Status

It directly informs:

* Event Types
* Controlled Values
* Production Procedure
* Certification Event-Type Profile
* First production Chronicle Entry
* Retrospective preservation
* Future Timeline inclusion

---

## Future Development

Later operational work may determine whether Chronicle requires:

* Formal Eligibility Decision records
* Automatic Preservation Class vocabulary
* Historical Significance Controlled Values
* Eligibility reviewer roles
* Eligibility reconsideration procedures
* Eligibility decision publication
* Machine-readable eligibility rationale
* Event-Type-specific eligibility rules

These should not be created until production use demonstrates a need.

---

## Status

**Active pre-operational Chronicle Preservation Eligibility Model specification.**

Historical Significance is incorporated as a principal preservation rationale rather than maintained as a separate institutional page.

Automatic Preservation Classes, final Eligibility Decision states, Historical Significance vocabulary, and Event-Type-specific preservation rules remain intentionally provisional until Chronicle gains production experience.
