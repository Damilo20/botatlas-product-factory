# BotAtlas Layer 8 — Evidence Extraction & Attribution

## Purpose

Layer 8 converts retrieved source material into explicit,
source-attributed claim candidates.

Layer 8 answers:

> What does this source claim?

Layer 8 does not answer:

> Is the claim true?

---

## Architectural Position

Layer 7
Evidence expansion and source discovery

↓

Layer 8
Evidence material acquisition
Claim extraction
Claim attribution

↓

Future trust and claim resolution layers

---

## Inputs

Layer 8 may consume:

- discovered evidence sources
- source URLs
- source family provenance
- search-query provenance
- retrieved source content
- retrieved text snippets
- document metadata

---

## Outputs

Layer 8 produces untrusted attributed claim records.

Example:

Source:
Figure AI Documentation

Claim:

- field_name: runtime
- claimed_value: 5 hours
- claim_text: Figure 02 can operate for 5 hours
- source_name: Figure AI Documentation
- source_url: source URL
- source_family: OFFICIAL_DOCUMENTATION

The record means:

> This source made this claim.

The record does not mean:

> BotAtlas accepts this claim as true.

---

## Core Contracts

### RetrievedEvidenceMaterial

Represents raw material acquired from a discovered evidence source.

Possible fields:

- source_name
- source_url
- source_family
- parent_candidate_name
- parent_candidate_url
- search_query
- content
- content_type
- acquisition_method
- acquired_at
- active

This contract carries provenance and material only.

---

### ExtractedClaimCandidate

Represents a claim statement extracted from evidence material.

Possible fields:

- field_name
- claimed_value
- claim_text
- extraction_method
- source_material_url
- active

This contract represents extraction only.

---

### AttributedEvidenceClaim

Represents an extracted claim explicitly attributed to its source.

Possible fields:

- field_name
- claimed_value
- claim_text
- source_name
- source_url
- source_family
- parent_candidate_name
- parent_candidate_url
- search_query
- extraction_method
- active

This contract means:

> Source X claims Y about field Z.

It does not assign truth.

---

## Responsibilities

Layer 8 may:

- acquire source material
- preserve source provenance
- extract explicit claim statements
- normalize claim field names
- preserve original claim text
- attribute claims to sources
- deduplicate identical attributed claims
- preserve extraction provenance

Layer 8 may not:

- verify claims
- assign truth
- select winning claims
- resolve conflicting claims
- assign authority scores
- assign reputation scores
- assign quality scores
- promote claims into product truth

---

## Proposed Engines

### EvidenceMaterialAcquisition

Converts discovered evidence sources into raw retrieved material.

DiscoveredEvidenceSource

↓

RetrievedEvidenceMaterial

---

### ClaimExtractionEngine

Extracts explicit claim candidates from retrieved material.

RetrievedEvidenceMaterial

↓

ExtractedClaimCandidate

---

### ClaimAttributionEngine

Combines extracted claims with source provenance.

ExtractedClaimCandidate
+
RetrievedEvidenceMaterial

↓

AttributedEvidenceClaim

---

### EvidenceExtractionPipeline

Orchestrates:

DiscoveredEvidenceSource

↓

EvidenceMaterialAcquisition

↓

RetrievedEvidenceMaterial

↓

ClaimExtractionEngine

↓

ExtractedClaimCandidate

↓

ClaimAttributionEngine

↓

AttributedEvidenceClaim

---

## Trust Boundary

The following concepts are forbidden from Layer 8 contracts:

- verified
- verification_status
- selected
- truth
- true
- confidence_score
- quality_score
- authority_score
- reputation_score

Layer 8 discovers claims.

Layer 8 does not decide claims.

---

## Evidence Lineage Requirement

Every AttributedEvidenceClaim must preserve enough provenance to answer:

1. Which product candidate caused the evidence search?
2. Which source family requested the evidence?
3. Which search query led to the source?
4. Which source supplied the material?
5. What material contained the claim?
6. What exact claim text was extracted?
7. Which field and value were extracted?

BotAtlas must be able to reconstruct the path:

Product Candidate

↓

Evidence Source Family

↓

Search Query

↓

Discovered Source

↓

Retrieved Material

↓

Extracted Claim

↓

Attributed Evidence Claim

---

## Architectural Invariant

Evidence extraction is not verification.

Claim attribution is not trust.

Claim presence is not claim acceptance.

Layer 8 must preserve this invariant at both contract
and runtime boundaries.
