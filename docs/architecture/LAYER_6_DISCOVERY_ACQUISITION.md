# BotAtlas Layer 6 — Discovery & Acquisition

## Responsibility

Layer 6 discovers product candidates, discovers source candidates, acquires source content, and records acquisition metadata.

Layer 6 answers:

> What products and source candidates should BotAtlas investigate?

## Core Principles

- DISCOVERED != VERIFIED
- RETRIEVED != TRUE
- SOURCE CANDIDATE != AUTHORITATIVE SOURCE

## Inputs

- discovery seed
- discovery target
- candidate URL
- source URL

## Outputs

- DiscoveryCandidate
- SourceCandidate
- AcquisitionRecord

## Models

- DiscoveryCandidate
- SourceCandidate
- AcquisitionRecord

## Engines

- DiscoveryEngine
- AcquisitionEngine
- CandidateDeduplicator
- DiscoveryPipeline

## Downstream Boundary

Layer 6 supplies discovered and acquired material to product intelligence.

Layer 5 remains responsible for source classification and authority scoring.

Layer 4 remains responsible for claim resolution.

## Non-Responsibilities

Layer 6 must not:

- verify evidence
- assign evidence confidence
- resolve claims
- select claims
- apply truth
- classify source authority
- assign authority scores
- assign reputation scores
- set product verification status
- set product confidence score
- set product quality score
- generate affiliate links
- publish products
- generate articles
- schedule marketing jobs

## Acceptance Contract

A discovered candidate is not verified.

Acquired content is not true merely because retrieval succeeded.

A source candidate is not authoritative until processed by Layer 5.

Layer 6 must preserve the BotAtlas trust boundary.
