# Atlas Entry-Layer Structural Review

## Executive Summary

The Atlas entry layer is structurally coherent at a high level, but it still depends too much on internal vocabulary and duplicate entry paths instead of a clearly taught navigation model.

Atlas root, corridor entry, corridor matrix, jurisdiction engine, U.S. layer, and state directory all share a stable visual shell and a recognizable top-down hierarchy. The main structural weaknesses are onboarding clarity and layer separation. The root explains that Atlas is a jurisdiction intelligence surface, but it does not fully teach what corridors and state packages are in practical navigation terms. The jurisdiction engine and U.S. layer also overlap heavily, which makes the hierarchy visible but not fully differentiated.

The strongest entry surface is the U.S. state directory, which is easy to scan and use. Its main weakness is navigation completeness, especially the dead A–Z anchors and the limited upward/lateral return structure.

Overall structural condition: strong visual consistency, workable hierarchy, incomplete framing of layer roles, and several navigation gaps that become more noticeable deeper in the entry stack.

## Atlas Root Findings

- `atlas/index.html` clearly explains that Atlas is the jurisdiction intelligence layer of Satoshium.
- The page does establish the existence of corridors, jurisdiction packages, and a U.S.-first expansion path.
- The card layout makes the primary entry options easy to see quickly.
- Navigation flow is only partly clarified. Users can enter through the jurisdiction engine, the U.S. package, or the U.S. state index directly, but the page does not clearly explain why those are separate layers instead of parallel shortcuts.
- The relationship between Atlas, corridors, and state packages is present at a conceptual level, but not fully operationalized as a simple hierarchy such as Atlas -> corridor layer / jurisdiction engine -> U.S. layer -> state packages.
- Missing framing component: the root does not explain the internal structure of a state package, so users are sent deeper without understanding the package model.
- Missing framing component: the root mentions corridor topology and deployment surfaces, but it does not clearly distinguish the corridor index from the corridor assignment matrix in user-facing structural terms.
- Structural note: the Corridors card contains a small markup irregularity around the second CTA block. Even if rendering is unaffected, it weakens DOM cleanliness on a key entry page.

## Corridor Layer Findings

- `atlas/corridors/index.html` clearly defines the corridor layer as the topology layer that connects normalized state packages.
- The page explains corridor purpose well in structural terms and makes the relationship to state packages visible.
- The relationship to Atlas is explicit because the page presents itself as a layer of Atlas rather than a detached surface.
- The page has good upward and downward links: back to Atlas, forward to U.S. state packages, and forward to the corridor assignment matrix.
- Corridor taxonomy clarity is mixed. The page first teaches the canonical trio of Corridor Group, Foundation Layer, and Topology Completion Layer, then later introduces Corridor Classification Families such as Energy-Compute, Research, and Interconnection corridors.
- Because the page does not explicitly connect those two classification frames, the corridor layer risks being read as two overlapping taxonomies instead of one corridor system with multiple explanatory views.
- Relationship to states is structurally clear, but relationship to the jurisdiction engine is only indirect. The page links straight to state packages instead of showing how corridor navigation and engine navigation fit together.

## Corridor Matrix Findings

- `atlas/corridors/corridor-assignment-matrix.html` has a strong structural introduction and clearly presents the three matrix dimensions.
- Terminology is consistent with the canonical trio presented on the corridor index.
- Visual hierarchy is generally good on desktop because the page moves from purpose -> interpretation rules -> matrix table -> usage rules.
- Readability weakens on smaller screens because the table is wide, uses a minimum width, and depends on horizontal scrolling for full inspection.
- Corridor membership clarity is strong at the row level because each state has a deterministic assignment across all three columns.
- Structural isolation remains a problem. The matrix is canonical, but row entries do not link into state packages and corridor labels do not link into any corridor-specific detail surface.
- The page explains how Atlas uses the matrix, but it does not provide a direct navigation bridge from matrix reading into deeper exploration.
- Terminology consistency with the corridor index is strong for the canonical trio, but the matrix does not help resolve the taxonomy split introduced by the corridor index's later classification-family section.

## Jurisdiction Engine Findings

- `atlas/jurisdiction-intelligence-engine/index.html` is structurally clear as the main engine entry page.
- Its purpose is visible: national entry first, then routing into state indexes and future jurisdiction layers.
- The two-card primary navigation section gives users a clean choice between entering the U.S. layer and jumping straight to the state index.
- The page explains state packages only indirectly through routing language. Users learn where to go, but not what package structure they are entering.
- Explanation of the evidence layer is incomplete. The page uses phrases like evidence-aligned jurisdiction packages, but it does not explain evidence as a distinct layer in the package model.
- Explanation of the signals layer is missing at the entry level. Signals are central to package interpretation, but the page does not surface them as a visible part of the state-package stack.
- The page scales well structurally for future country expansion, but current navigation clarity depends more on abstract framing than on a clearly taught package anatomy.

## U.S. Layer Findings

- `atlas/jurisdiction-intelligence-engine/us/index.html` clearly functions as a national entry layer above the state directory.
- National-layer framing is present and visually easy to recognize.
- Entry into state packages is clear because the state index CTA is prominent.
- Navigation hierarchy is visible, but lightly. The page communicates that it sits between the engine root and the state directory, yet it does not provide a direct return path back to the jurisdiction engine root.
- Structurally, the page overlaps heavily with the engine root. Both pages explain routing into state packages and future expansion, so the U.S. layer feels more like a hierarchy placeholder than a strongly differentiated navigation surface.
- The page is still useful as a national boundary layer, but the distinction between engine root and U.S. layer is thinner than the distinction between U.S. layer and state directory.

## State Directory Findings

- `atlas/jurisdiction-intelligence-engine/us/states/index.html` is the strongest usability surface in the reviewed entry stack.
- Discoverability is strong because the page offers both a clickable state map and an alphabetical index.
- Scanning usability is strong for users who already know the state they want.
- Naming consistency is good inside the index. Display labels are human-readable and multi-word state slugs are handled consistently in links.
- Navigation completeness is weaker than discoverability. The page offers a return path to the U.S. layer, but no visible path back to the jurisdiction engine root, Atlas root, or corridor surfaces.
- The A-Z letter navigation is structurally incomplete because it includes letters with no matching section anchors. This introduces dead navigation targets for letters such as B, E, J, Q, X, Y, and Z.
- The page is effective as a state finder, but it does not frame what users should expect when they open a state package.
- Internal link style is not fully consistent with the rest of the entry layer because the return link uses an absolute production URL while other pages rely mostly on relative or root-relative internal paths.

## Priority Structural Issues

### High

- Atlas root does not clearly teach the layer model well enough before offering multiple parallel entry points, especially the difference between Atlas root, corridors, jurisdiction engine, U.S. layer, and state packages.
- Corridor taxonomy is structurally split between the canonical trio and the later classification-family scheme without an explicit bridge between them.
- The U.S. state directory contains dead A-Z navigation targets, which weakens one of the page's main scanning tools.

### Medium

- The corridor assignment matrix is structurally isolated because it does not link rows to state pages or corridor names to any deeper corridor surface.
- The jurisdiction engine does not clearly explain the state-package layer model, especially the role of evidence and signals.
- The U.S. layer is only lightly differentiated from the jurisdiction engine root and lacks a visible return path upward.
- Entry surfaces do not consistently explain what users will find inside a state package before sending them into the deeper layer.

### Low

- Internal link styles vary across the entry stack, including relative, root-relative, and absolute production links.
- `atlas/index.html` contains a small markup irregularity in the Corridors card area.
- Several entry pages rely on shared-shell navigation and repeated framing instead of stronger local hierarchy cues within the page body.
