# BotAtlas Revenue Architecture v1.0

## Purpose

BotAtlas may generate revenue from commercial activity without allowing
commercial incentives to modify the intelligence core.

The intelligence core and commercial system are architecturally separate.

---

## Core Architecture

BotAtlas
|
|-- Intelligence Core
|   |-- Discovery
|   |-- Acquisition
|   |-- Evidence Expansion
|   |-- Claim Extraction
|   |-- Claim Reconciliation
|   `-- Evidence Characteristics
|
`-- Commercial System
    |-- Commercial Opportunities
    |-- Seller Offers
    |-- Affiliate Relationships
    |-- Sponsorship Disclosures
    |-- Lead Routing
    |-- Subscription Products
    |-- API Products
    `-- Data Licensing

---

## Commercial Independence Law

Money may influence commercial placement.

Money may not influence:

- product identity
- evidence discovery
- evidence acquisition
- claim extraction
- claim attribution
- claim grouping
- evidence comparison
- claim reconciliation
- source authority assessment
- evidence characteristic assessment
- truth determination

---

## Revenue Sources

### Affiliate Commerce

BotAtlas may route users to commercial offers and receive compensation.

Affiliate compensation must remain commercial metadata.

Affiliate compensation cannot alter intelligence assessments.

### Sponsorship

Manufacturers or commercial organizations may purchase visibility.

Sponsored placement must be explicitly disclosed.

Sponsorship cannot modify product evidence or claims.

### Lead Generation

BotAtlas may route qualified commercial inquiries to manufacturers,
integrators, distributors, or service providers.

Lead compensation cannot alter intelligence output.

### Subscriptions

BotAtlas may offer paid access to advanced product intelligence features.

Potential products include:

- product monitoring
- contradiction alerts
- specification change alerts
- saved watchlists
- advanced comparison tools
- evidence lineage views

### Intelligence API

BotAtlas may expose structured product intelligence through paid APIs.

Commercial API access cannot modify the underlying intelligence records.

### Data Licensing

BotAtlas may license structured robotics product datasets.

Licensed data must preserve provenance and uncertainty where applicable.

### Manufacturer Intelligence

BotAtlas may provide commercial analytics to manufacturers.

Examples:

- conflicting product claims
- outdated specification detection
- product information inconsistencies
- market comparison activity
- product research demand

Manufacturer payment cannot suppress contradictory evidence.

---

## Architectural Boundary

Intelligence Core
      |
      v
Commercial Read Boundary
      |
      v
Commercial Opportunity System
      |
      |-- Affiliate
      |-- Sponsorship
      |-- Leads
      |-- Subscription
      |-- API
      `-- Licensing

Commercial systems consume intelligence outputs.

Commercial systems do not write intelligence conclusions.

---

## Forbidden Commercial Influence

Commercial contracts must never contain or modify:

- verified
- verification_status
- truth
- true
- final_score
- final_value
- accepted_claim
- rejected_claim
- authority_score
- quality_score
- confidence_score

Commercial compensation is not evidence.

Commercial popularity is not truth.

Sponsorship is not verification.

Affiliate availability is not product quality.

---

## BotAtlas Principle

Revenue funds intelligence.

Revenue does not control intelligence.
