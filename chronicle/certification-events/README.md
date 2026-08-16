# Chronicle Certification Events

## Purpose

Chronicle Certification Events define the certification-related historical occurrences that Satoshium Chronicle may preserve as part of the historical record.

Chronicle does not create, replace, or reinterpret certifications. Certifier remains authoritative for Certification Packages and certification lifecycle actions. Chronicle preserves the historical occurrence and context of certification activity by referencing those authoritative records.

The purpose of this specification is to establish a clear historical model for preserving qualifying certification-related occurrences while maintaining the authority boundaries established by the Satoshium Suite.

---

## Suite Alignment

Certification Events operate within the Satoshium Suite architecture.

They should follow Suite-wide expectations for:

* Stable terminology
* Clear institutional authority boundaries
* Reference-based interoperability
* Structured records
* Durable references
* Repeatable procedures
* Schema discipline
* Version-aware preservation
* Validation-ready workflows

Chronicle references authoritative Suite objects rather than duplicating, replacing, or reinterpreting them.

---

## Core Institutional Distinction

The participating Suite systems retain independent authority over their own objects and actions.

### Certifier

Certifier is authoritative for:

* Certification Packages
* Certification determinations
* Certification lifecycle actions
* Certification status

### Registry

Registry is authoritative for:

* SREG Registry Entries
* Registration and cataloging
* Registry lifecycle state
* Registry record relationships

### Chronicle

Chronicle is responsible for:

* Preserving qualifying certification-related historical occurrences
* Recording historical context
* Maintaining relationships to authoritative records
* Supporting long-term historical continuity and discovery

Chronicle does not assume the authority of Certifier or Registry.

---

## Historical Model

A certification event is the historical occurrence associated with an authoritative certification action or state.

Chronicle may preserve that occurrence through a Chronicle Entry when the occurrence satisfies Chronicle preservation rules.

A preserved certification occurrence should make clear:

* What happened
* When it happened
* Which system originated the authoritative action
* Which authoritative record establishes the occurrence
* Which related Suite records provide context
* Why the occurrence matters within the broader certification history

The event itself is not the authoritative certification object.

Chronicle preserves the history of the occurrence by referencing the authoritative object that established it.

---

## Certification Event Types

Chronicle may preserve certification-related event types when the underlying occurrence satisfies Chronicle preservation rules and can be tied to an authoritative certification record.

Initial certification-related event types include:

* Certification Created
* Certification Renewed
* Certification Suspended
* Certification Revoked
* Certification Expired

Additional certification event types may be defined only when they correspond to authoritative certification lifecycle actions or states recognized by Certifier.

Anchor, Attestor, Beacon, Registry, or other Suite-system activity should not be reclassified as certification authority. Those occurrences should be handled through their own Chronicle event-type profiles where appropriate.

---

## Certification Created

A Certification Created event records the historical occurrence in which Certifier produced a new authoritative Certification Package.

Chronicle references the Certification Package and preserves the historical context surrounding its creation.

Chronicle does not recreate or independently determine the certification.

---

## Certification Renewed

A Certification Renewed event records the historical occurrence in which Certifier authoritatively renewed a certification according to the applicable certification rules and lifecycle model.

Chronicle preserves the occurrence and references the authoritative certification record.

---

## Certification Suspended

A Certification Suspended event records the historical occurrence in which Certifier authoritatively placed a certification into a suspended state according to the applicable certification status model.

Chronicle does not independently determine or impose suspension.

---

## Certification Revoked

A Certification Revoked event records the historical occurrence in which Certifier authoritatively revoked a certification according to the applicable certification rules and lifecycle model.

Chronicle preserves the occurrence but does not create or reinterpret the revocation authority.

---

## Certification Expired

A Certification Expired event records the historical occurrence in which a certification reached an expired state under the applicable Certifier rules and certification lifecycle model.

Chronicle records the historical transition without independently determining expiration.

---

## Record References

Certification Events should reference the authoritative Certification Package produced by Certifier.

They may also reference related Suite or public records, including:

* Registry Entries
* Receipts
* Public certification pages
* Attestations
* Integrity references
* Public archival references
* Other supporting Suite records

Referenced records remain authoritative within the systems that created them.

Chronicle uses these references to preserve context, relationships, provenance, and historical continuity.

---

## What a Certification Event Preserves

A Certification Event should preserve enough context to make the historical occurrence understandable without duplicating, replacing, or reinterpreting the authoritative certification record.

Expected components may include:

* Event Type
* Event Date
* Originating System
* Authoritative Certification Package
* Related Registry Entry
* Public References
* Historical Context
* Supporting Records
* Relationships
* Provenance
* Verification information
* Chronicle status or lifecycle information

The final canonical fields will be governed by the Chronicle Entry Model, Base Schema, Event-Type Profile, and controlled values.

---

## What a Certification Event Does Not Do

A Certification Event does not:

* Certify
* Renew
* Suspend
* Revoke
* Expire
* Reissue
* Reaffirm
* Independently determine certification status
* Replace a Certification Package
* Replace a Registry Entry
* Reinterpret another Suite system's authority

Those actions and determinations remain within the authority of the originating Suite system.

Chronicle preserves that the occurrence happened and references the authority that established it.

---

## Relationship to Registry

Registry creates and maintains independent SREG Registry Entries that catalog records over time.

Chronicle may reference a Registry Entry when preserving a certification-related occurrence, but Registry remains authoritative for:

* The SREG
* Registry metadata
* Registry lifecycle state
* Registry catalog relationships

Chronicle does not treat the Registry Entry as a substitute for the authoritative Certification Package.

Registry owns the catalog record.

Chronicle preserves the historical occurrence and its context.

---

## Preservation Eligibility

Not every certification-related action automatically requires Chronicle preservation.

A certification-related occurrence should be preserved only when it satisfies Chronicle Preservation Eligibility rules.

Eligibility may ultimately be established through:

* An approved Chronicle event type or preservation class
* Historical significance
* Other Chronicle preservation rules adopted through the institutional architecture

Preservation Eligibility is distinct from certification authority, evidence quality, and verification confidence.

---

## Historical Significance

Historical Significance describes why a certification-related occurrence matters within the continuing institutional history of Satoshium.

Potential factors may include:

* Lifecycle significance
* First or last occurrence
* Institutional milestone
* Material change
* Relationship significance
* Continuity value
* Future historical understanding

Historical Significance may support Preservation Eligibility but does not replace the formal eligibility mechanism.

---

## Event-Type Profile

Certification Events are expected to become the first Chronicle Event-Type Profile.

The Certification Event-Type Profile should operate as an extension of the Chronicle Base Schema.

It should define certification-specific requirements without duplicating the authoritative Certification Package.

The profile may establish:

* Allowed certification event types
* Required authoritative references
* Required originating system
* Required temporal information
* Relationship rules
* Certification-specific controlled values
* Validation requirements

The final profile will be created after the Chronicle canonical object, identifier architecture, Base Schema, and controlled values are settled.

---

## Verification

Chronicle verification should verify Chronicle's historical representation and references.

Verification may include:

* Confirmation that the referenced Certification Package exists
* Identifier consistency
* Event-date consistency
* Originating-system consistency
* Registry-reference consistency
* Relationship integrity
* Provenance completeness
* Supporting-record availability

Chronicle verification does not re-adjudicate the certification determination made by Certifier.

---

## Corrections and Versioning

If Chronicle later discovers an error in its own representation of a Certification Event, Chronicle may correct its Entry according to Chronicle correction and versioning rules.

Chronicle may correct:

* Event metadata
* References
* Historical context
* Relationships
* Provenance
* Supporting information

Chronicle does not correct the underlying Certification Package.

If Certifier later changes or supersedes its authoritative record, Chronicle may preserve that later occurrence and update its own references according to Chronicle rules.

---

## Future Development

Future Chronicle Certification Events work may include:

* Formal Certification Event-Type Profile
* Controlled event-type values
* Certification-specific validation rules
* Relationship rules
* Provenance requirements
* Structured machine-readable event records
* Public Chronicle Entry discovery
* Timeline integration
* Additional certification lifecycle event types where recognized by Certifier

Future development should preserve the Suite authority boundaries established here.

---

## Status

Draft operational specification.

This README reflects the reconciled Chronicle Certification Events architecture and is aligned with the current Satoshium Suite Standards, Methodology, and Interoperability framework.

The event-type schema, controlled values, identifiers, validation rules, and production procedures may evolve as Chronicle operational development continues.
