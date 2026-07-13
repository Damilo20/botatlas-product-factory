# BotAtlas Layer 7 — Evidence Expansion

## Purpose

Layer 7 expands a discovered product candidate into multiple independent
evidence-source candidates.

Layer 7 increases evidence coverage.

Layer 7 does not determine truth.

## Upstream Boundary

Layer 7 may receive:

- DiscoveryCandidate
- AcquiredMaterial
- product identity hints
- candidate URLs
- candidate names
- manufacturer hints
- model hints

## Responsibilities

Layer 7 may:

- generate evidence search targets
- discover additional source candidates
- expand manufacturer sources
- identify documentation sources
- identify authorized retailer candidates
- identify technical source candidates
- identify independent reporting candidates
- deduplicate evidence source candidates
- preserve discovery provenance

## Source Families

Layer 7 may expand evidence across:

1. OFFICIAL_MANUFACTURER
2. OFFICIAL_DOCUMENTATION
3. AUTHORIZED_RETAILER
4. TECHNICAL_SOURCE
5. INDEPENDENT_REPORTING

Source family labels are discovery classifications only.

They are not authority scores.

## Trust Boundary

Layer 7 must not:

- verify evidence
- declare evidence true
- resolve claims
- assign evidence confidence
- assign product confidence
- assign product quality
- assign authority scores
- assign reputation scores
- select winning claims
- set product verification status

## Downstream Boundary

Layer 7 supplies expanded evidence-source candidates.

Layer 5 remains responsible for source authority classification and scoring.

Layer 4 remains responsible for claim resolution and truth application.

## Acceptance Contract

More sources do not automatically mean more truth.

A discovered source is not authoritative merely because it matches a source family.

An evidence-source candidate remains untrusted until downstream authority
and truth layers process it.

Layer 7 must preserve the BotAtlas trust boundary.
