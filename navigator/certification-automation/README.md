# Satoshium Navigator — Certification Automation

**Path:** `/navigator/certification-automation/`  
**Institution:** Satoshium Navigator  
**Surface:** Certification Workflow Automation  
**Status:** Current repository documentation

## Purpose

This directory documents **Satoshium Navigator Certification Automation**.

Certification Automation defines how Navigator coordinates repeatable certification workflows across the Satoshium Suite while preserving the independent authority of participating institutions.

Navigator reduces repetitive operational work by initiating, coordinating, monitoring, and tracking governed workflow steps.

Navigator does not become the authority for certification decisions.

## Institutional Role

Navigator's role is orchestration.

Within certification-related workflows, Navigator may:

- initiate a defined workflow;
- coordinate participating institutions;
- sequence repeatable operational steps;
- monitor progress;
- identify incomplete work;
- track workflow state;
- expose operational status;
- support scheduled or event-driven execution where implemented.

The governing distinction is:

> **Automation coordinates. Authority decides.**

## Certification Authority Boundary

Satoshium Certifier remains authoritative for:

- certification determinations;
- certification decisions;
- Certification Packages;
- certification lifecycle actions;
- certification status;
- Certifier-owned validation and review processes.

Navigator may coordinate a process that reaches Certifier.

Navigator does not perform Certifier's institutional decision merely because the workflow is automated.

## Repeatable Certification Processes

Current certification-automation examples include workflows that may coordinate:

- launch of certification;
- launch of recertification;
- identification of uncertified records;
- scheduling of certification reviews;
- detection of expired certifications;
- detection of certifications approaching expiration;
- requests for additional evidence;
- Registry registration workflows;
- Chronicle event-preservation workflows;
- Anchor integrity-preservation workflows;
- Beacon discovery-update workflows;
- Attestor Attestation-generation workflows.

These examples describe orchestration targets.

They should not be read as transferring downstream institutional authority to Navigator.

## Workflow Triggers

A Navigator certification workflow may begin from:

- a user request;
- a scheduled operation;
- a lifecycle event;
- a certification query;
- a policy rule;
- an external integration;
- a future machine-triggered event.

The initiating trigger does not determine the authority of later institutional actions.

## Workflow Execution

Navigator coordinates the execution path while each participating institution performs its own governed responsibility.

A generalized pattern is:

```text
Operational Question
        ↓
Workflow Selected
        ↓
Participating Systems Coordinated
        ↓
Institution-Specific Actions Performed
        ↓
Workflow State Updated
        ↓
Resulting Institutional Records Preserved
```

The current public page expresses this more concretely through certification, Registry, Chronicle, Anchor, Beacon, and Attestor stages.

That sequence should be understood as orchestration context rather than institutional ownership.

## Workflow Monitoring

Navigator may track:

- workflow progress;
- pending operations;
- completed operations;
- incomplete or blocked steps;
- scheduling state;
- execution status;
- downstream acknowledgments or results.

Monitoring does not modify authoritative institutional records unless the owning institution exposes an authorized operation that Navigator invokes through the governed workflow.

## Cross-Institution Relationships

Certification Automation may coordinate activity involving multiple Suite institutions.

### Certifier

Navigator may initiate or coordinate certification-related workflows.

Certifier retains certification authority.

### Registry

Navigator may coordinate a Registry registration workflow after an eligible certification-related matter reaches the appropriate stage.

Registry owns the resulting Registry Entry and Registry-controlled representation.

### Chronicle

Navigator may coordinate a Chronicle preservation workflow when a qualifying Occurrence should be considered for preservation.

Chronicle owns the resulting Chronicle Entry and its historical-preservation determination.

### Anchor

Navigator may coordinate an Anchor preservation workflow.

Anchor owns the Integrity Reference and its integrity-preservation process.

### Beacon

Navigator may coordinate a Beacon discovery-update workflow.

Beacon owns Discovery Signals, Discovery Metadata, provenance, lifecycle, and publication decisions.

### Attestor

Navigator may coordinate an Attestor workflow involving Attestation generation or downstream evaluation.

Attestor owns Attestations, Rule-Constrained Evaluation, Evaluation Outcomes, and Trust Statements.

## Authority Discipline

Certification Automation must preserve the following distinctions:

- orchestration ≠ certification;
- workflow initiation ≠ institutional approval;
- workflow monitoring ≠ record authority;
- scheduling ≠ lifecycle decision;
- coordination ≠ publication;
- coordination ≠ historical preservation;
- coordination ≠ integrity determination;
- coordination ≠ discovery authority;
- coordination ≠ Attestor evaluation;
- downstream result ≠ Navigator-owned result.

Most importantly:

**REFERENCE DOES NOT TRANSFER AUTHORITY.**

And:

**COORDINATION DOES NOT TRANSFER AUTHORITY.**

## Automation Sequence

The public page currently presents a representative automation sequence:

```text
Operational Question
↓
Workflow Selected
↓
Systems Coordinated
↓
Certification Executed
↓
Records Updated
↓
History Preserved
↓
Integrity Preserved
↓
Discovery Updated
↓
Trust Statements Produced
```

This should be interpreted as a cross-institution workflow path.

Each substantive institutional act remains governed by the institution that owns it.

For example:

- Certifier performs certification;
- Registry governs Registry updates;
- Chronicle preserves qualifying historical Occurrences;
- Anchor establishes integrity references;
- Beacon governs discovery outputs;
- Attestor produces governed Trust Statements.

Navigator coordinates the workflow connecting those acts.

## Future Automation

The current public architecture contemplates future support for:

- scheduled automation;
- event-driven automation;
- APIs;
- policy engines;
- machine-triggered workflows;
- cross-system orchestration.

These remain implementation directions unless and until separately established in production.

Future automation should preserve the same authority boundaries as manually coordinated workflows.

## Relationship to the Satoshium Suite

Certification Automation demonstrates Navigator's role as the Suite's workflow-definition and orchestration institution.

Navigator can coordinate the movement of governed work among institutions without becoming the owner of the participating institutions' canonical objects.

This architecture enables repeatable Suite operations while maintaining institutional separation.

## Suite Reconciliation Flag

The current architecture is fundamentally sound, but several phrases on the public page should receive Suite-wide review because they can imply stronger execution authority than Navigator actually owns.

Examples include language such as:

- `Trigger Chronicle event creation`
- `Request Anchor preservation`
- `Publish Beacon discovery updates`
- `Initiate Attestation generation`
- `Records Updated`
- `History Preserved`
- `Discovery Updated`
- `Trust Statements Produced`

The issue is not whether Navigator can coordinate workflows that lead to those results.

The issue is whether the wording clearly preserves the fact that the owning institution must perform or authorize the institutional act.

Suite Reconciliation should determine the preferred cross-institution orchestration vocabulary.

Possible distinctions to preserve include:

```text
Navigator coordinates
Institution evaluates / decides
Institution creates
Institution changes lifecycle
Institution publishes
Navigator records workflow progress
```

This is a terminology and authority-clarity issue, not a reason to redesign Navigator Certification Automation.

## Repository Expectations

Changes to this directory should preserve:

1. Navigator as the orchestration institution;
2. Certifier authority over certification;
3. independent authority of Registry, Chronicle, Anchor, Beacon, and Attestor;
4. the distinction between initiating a workflow and performing an institutional act;
5. the distinction between workflow state and canonical institutional state;
6. the ability to support repeatable automation without collapsing institutional boundaries;
7. future automation as governed implementation rather than assumed authority; and
8. the principle that coordination does not transfer authority.

## Governing Principle

**Automation coordinates. Authority decides.**
