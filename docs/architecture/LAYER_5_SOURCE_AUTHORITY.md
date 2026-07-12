# BotAtlas Layer 5 — Source Authority & Provenance Engine

## Status

Architecture Approved — Implementation In Progress

## Mission

Layer 5 determines how much trust BotAtlas should assign to evidence based on the source, claim context, provenance, freshness, and independent corroboration.

Layer 5 does not discover products or crawl the web.

Its responsibility is to evaluate intelligence already entering BotAtlas.

## Core Doctrine

Source authority is contextual.

A source must not receive universal trust for every type of claim.

Evidence weight is derived from:

Source
+
Claim Field
+
Provenance
+
Freshness
+
Independent Corroboration
=
Evidence Weight

Evidence Weight feeds the Layer 4 Intelligence Graph.

## Layer Boundary

Layer 5 sits before Layer 4 claim confidence resolution.

Source
↓
Source Classification
↓
Authority Evaluation
↓
Provenance Evaluation
↓
Freshness Evaluation
↓
Field Relevance
↓
Independent Corroboration
↓
Evidence Weight
↓
Layer 4 Claim Engine
↓
Claim Resolver
↓
Truth Applicator
↓
Canonical Product

## Source Classification

Supported source types may include:

- MANUFACTURER
- REGULATOR
- RESEARCH
- DISTRIBUTOR
- RETAILER
- NEWS
- REVIEW
- MARKETPLACE
- COMMUNITY
- AFFILIATE
- AGGREGATOR
- UNKNOWN

Supported ownership types may include:

- FIRST_PARTY
- SECOND_PARTY
- THIRD_PARTY
- COMMUNITY
- UNKNOWN

## Contextual Authority

Authority must be evaluated relative to the claim field.

Example:

A manufacturer may have high authority for:

- product identity
- manufacturer
- model
- technical specifications
- MSRP

The same manufacturer may have lower contextual authority for:

- independent performance conclusions
- comparative rankings
- subjective product quality claims

A retailer may have high authority for:

- current listing price
- availability
- seller information

A retailer may have lower authority for:

- canonical product identity
- engineering architecture
- manufacturer capability claims

## Provenance

Source and provenance are separate concepts.

Source answers:

Where did the intelligence come from?

Provenance answers:

How did this specific intelligence travel into BotAtlas?

Example:

Manufacturer
↓
Official specification page
↓
Research Agent
↓
Evidence extraction
↓
Claim
↓
Canonical truth

Layer 5 must preserve this chain for future auditability.

## Evidence Weight

Layer 5 calculates evidence confidence.

Layer 4 consumes that confidence.

Conceptual factors:

- source authority
- field relevance
- provenance quality
- freshness
- independent corroboration

Initial conceptual weighting:

authority = 0.35
field relevance = 0.25
provenance = 0.20
freshness = 0.10
corroboration = 0.10

All final evidence weights must be normalized to:

0.0 <= evidence_weight <= 1.0

The weighting policy may evolve without changing Layer 4 claim resolution architecture.

## Independent Corroboration

Source count is not equal to independent source count.

Multiple pages may repeat intelligence originating from one upstream source.

BotAtlas must avoid treating copied claims as independent confirmation.

Example:

Blog A
Blog B
Blog C

If all three repeat Article X, the provenance family represents one originating intelligence path rather than three independent confirmations.

## Freshness

Freshness is field-sensitive.

Stable identity fields may remain trustworthy longer than volatile commerce fields.

Examples of relatively stable fields:

- product_name
- manufacturer
- model

Examples of volatile fields:

- current_price
- availability
- affiliate_url

Freshness policy must remain outside individual agents.

## Proposed Components

Models:

- Source
- Provenance
- Evidence
- Claim

Layer 5 engines:

- SourceClassifier
- SourceAuthorityEngine
- ProvenanceEngine
- EvidenceWeightEngine

Policy:

- authority policy
- freshness policy

Layer 4 consumers:

- ClaimEngine
- ClaimResolver
- TruthApplicator

## Non-Responsibilities

Layer 5 must not:

- search Google
- crawl websites
- discover robots
- call research providers
- generate articles
- build Shopify products
- create affiliate links
- schedule research jobs

Those responsibilities belong to downstream or provider layers.

## Acceptance Test

Competing claims:

Claim A:
weight = 70 kg

Source:
official manufacturer specification

Source type:
MANUFACTURER

Ownership:
FIRST_PARTY

Original source:
TRUE

Claim B:
weight = 65 kg

Source:
unknown affiliate website

Source type:
AFFILIATE

Ownership:
THIRD_PARTY

Original source:
FALSE

Expected behavior:

The official manufacturer evidence receives greater contextual evidence weight for a technical specification claim.

Layer 4 receives the derived evidence confidence values.

The Claim Resolver selects the stronger claim.

Expected conceptual result:

70 kg -> VERIFIED -> SELECTED
65 kg -> REJECTED -> NOT SELECTED

## Architectural Rule

Agents may collect evidence.

Layer 5 evaluates evidence trust.

Layer 4 resolves competing claims.

The Product stores canonical truth.

These responsibilities must remain separate.

## Build Order

1. Architecture document
2. Upgrade Source model
3. Add Provenance model
4. Implement SourceClassifier
5. Define authority policy
6. Implement SourceAuthorityEngine
7. Define freshness policy
8. Implement EvidenceWeightEngine
9. Integrate Layer 5 with Layer 4
10. Execute conflict test
11. Execute full regression
12. Seal Layer 5

## Layer 5 Definition of Done

Layer 5 is complete when BotAtlas can:

1. classify a source
2. identify source ownership context
3. preserve evidence provenance
4. evaluate source authority contextually
5. evaluate field relevance
6. evaluate freshness
7. account for independent corroboration
8. derive normalized evidence confidence
9. pass derived confidence into Layer 4
10. resolve competing claims using weighted evidence
11. preserve Product Factory regression behavior

