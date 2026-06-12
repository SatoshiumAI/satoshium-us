# Assets

This directory contains visual, graphical, and supporting media assets used by Satoshium Certifier.

Assets are intended to support documentation, certification reports, certification receipts, standards, presentations, public communication, and future subsystem interfaces.

---

# Purpose

The assets directory serves as a centralized location for non-document resources associated with Certifier.

Examples include:

* Logos
* Icons
* Certification marks
* Workflow diagrams
* Architecture diagrams
* Screenshots
* Badges
* Report graphics
* Presentation materials
* Future user interface assets

---

# Suggested Structure

```text
assets/
├── logos/
├── icons/
├── diagrams/
├── badges/
├── screenshots/
├── presentations/
└── archive/
```

Future additions may introduce additional asset categories as Certifier evolves.

---

# Asset Categories

## Logos

Official Certifier branding assets.

Examples:

* certifier-logo.png
* certifier-mark.svg
* certifier-wordmark.svg

---

## Icons

Small graphical elements used throughout documentation and interfaces.

Examples:

* certification icon
* evidence icon
* receipt icon
* report icon

---

## Diagrams

Visual representations of Certifier concepts.

Examples:

* certification lifecycle diagrams
* workflow diagrams
* interoperability diagrams
* architecture diagrams

---

## Badges

Visual indicators representing certification status or certification class.

Future examples may include:

* Informational
* Operational
* Verified

Badge formats may include:

```text
.svg
.png
.webp
```

---

## Screenshots

Screenshots used to support documentation, demonstrations, reports, and examples.

Screenshots should not replace evidence records maintained within certification activities.

Evidence-related screenshots should be preserved according to the Evidence Model.

---

## Presentations

Presentation materials supporting demonstrations, briefings, or educational content.

Examples:

```text
.pptx
.pdf
```

---

## Archive

Historical or retired assets retained for preservation purposes.

Archived assets should not be considered active branding or operational resources unless explicitly noted.

---

# Naming Conventions

Assets should use clear and descriptive filenames.

Recommended format:

```text
asset-name-version.ext
```

Examples:

```text
certifier-logo-v1.svg
workflow-diagram-v1.png
verified-badge-v1.svg
```

Avoid generic filenames such as:

```text
image1.png
logo-new-final-final.png
diagram.png
```

---

# Versioning

When practical, significant asset revisions should be versioned rather than overwritten.

Example:

```text
certifier-logo-v1.svg
certifier-logo-v2.svg
```

This supports historical preservation and future reference.

---

# Relationship to Certification Evidence

Assets and evidence serve different purposes.

Assets support communication and presentation.

Evidence supports certification determinations.

Certification evidence should be managed according to:

```text
docs/evidence-model.md
```

and should not rely solely upon the assets directory.

---

# Long-Term Vision

As Certifier evolves, the assets directory may become the home of official certification marks, certification class badges, workflow visualizations, and public-facing trust indicators used throughout the Satoshium ecosystem.

The purpose of this directory is to ensure that visual resources remain organized, reusable, and preserved alongside the documentation and standards that define Certifier.

---

# Guiding Statement

> Documentation explains.
>
> Standards define.
>
> Assets communicate.
>
> The assets directory exists to support the visual expression of Certifier.
