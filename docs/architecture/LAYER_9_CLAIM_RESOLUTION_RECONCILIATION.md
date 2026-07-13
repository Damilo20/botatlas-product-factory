# BotAtlas Layer 9 — Claim Resolution and Evidence Reconciliation

## Purpose

Layer 9 reconciles attributed evidence claims produced by Layer 8.

Layer 9 reasons over competing claims while preserving the complete
evidence lineage attached to each claim.

Layer 9 must never silently discard contradictory evidence.

---

## Input

AttributedEvidenceClaim[]

Layer 8 claims preserve:

- field name
- claimed value
- exact claim text
- source name
- source URL
- source family
- parent candidate identity
- search query
- extraction method
- attribution method
- material acquisition timestamp

---

## Architecture

AttributedEvidenceClaim[]
        |
        v
ClaimGroupingEngine
        |
        v
ClaimGroup
        |
        v
EvidenceComparisonEngine
        |
        v
ClaimResolutionCandidate
        |
        v
ClaimResolutionEngine
        |
        v
ResolvedClaim

---

## Claim Grouping

Claims are grouped by:

- parent candidate identity
- field name

Example:

Figure 02
runtime

Claims:

- 5 hours
- 4.5 hours

These claims remain independent evidence records.

Grouping does not merge or delete evidence.

---

## Evidence Comparison

EvidenceComparisonEngine identifies:

- agreement
- contradiction
- partial agreement
- insufficient evidence

Comparison must preserve every attributed claim.

The comparison layer may describe evidence relationships.

It must not mutate Layer 8 claims.

---

## Resolution States

Layer 9 may produce the following resolution states:

- AGREEMENT
- CONFLICT
- PARTIAL_AGREEMENT
- INSUFFICIENT_EVIDENCE
- UNRESOLVED

A resolution state describes the evidence condition.

It is not a declaration of absolute truth.

---

## Resolution

ClaimResolutionEngine may:

- identify a preferred claim candidate
- preserve alternative claims
- explain why evidence differs
- abstain from selecting a preferred value
- emit an unresolved result

Every resolution must preserve its supporting evidence.

---

## Resolved Claim

A ResolvedClaim may contain:

- parent candidate name
- parent candidate URL
- field name
- preferred value
- resolution state
- resolution method
- resolution explanation
- supporting claims
- alternative claims

A ResolvedClaim must never erase contradictory evidence.

---

## Abstention

Layer 9 must support abstention.

If evidence cannot justify a preferred value:

preferred_value = None

resolution_state = UNRESOLVED

This is valid system behavior.

BotAtlas must prefer uncertainty over fabricated certainty.

---

## Trust Boundary

Layer 9 performs evidence reconciliation.

Layer 9 does not declare absolute truth.

The following concepts remain forbidden as direct Layer 9 decisions:

- true
- truth
- absolute_truth
- guaranteed
- certainty

Layer 9 may describe:

- evidence agreement
- evidence conflict
- preferred evidence-supported value
- unresolved evidence

---

## Core Rule

Layer 8 records what sources claim.

Layer 9 reasons over competing claims.

No evidence may disappear during reconciliation.
