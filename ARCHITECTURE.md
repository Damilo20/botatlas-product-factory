# BotAtlas System Architecture v1.0

> **The official architectural blueprint for the BotAtlas platform.**

This document defines the long-term architecture, design principles, domain boundaries, and capability ownership for BotAtlas.

Every feature, engine, workflow, AI agent, database table, API, and future service must align with this architecture.

---

# 1. Vision

BotAtlas exists to build the world's most trusted Product Intelligence Platform.

The platform is designed to discover, understand, verify, organize, enrich, and commercialize trusted product knowledge.

BotAtlas is not simply a product catalog.

It is an intelligence platform capable of transforming raw information into trusted knowledge and trusted knowledge into commercial intelligence.

---

# 2. Mission

BotAtlas empowers businesses and consumers by providing verified product intelligence that is transparent, explainable, evidence-based, and commercially actionable.

---

# 3. Core Design Principles

Every component within BotAtlas follows these principles.

## Single Responsibility

Every engine owns one responsibility.

No engine should perform multiple unrelated tasks.

---

## Domain Ownership

Every capability belongs to exactly one architectural domain.

Domains collaborate.

Domains do not duplicate responsibilities.

---

## Evidence Before Truth

Truth is never assumed.

Every conclusion must be supported by evidence.

---

## Knowledge Before Commercialization

Commercial decisions should only be made after knowledge has been verified.

---

## Platform Independence

Infrastructure supports business logic.

Infrastructure never owns business logic.

---

## Modular Evolution

Every component should be replaceable without affecting unrelated capabilities.

---

# 4. Architectural Domains

BotAtlas is organized into five domains.

Each domain owns a specific area of responsibility.

---

## Product Domain

### Purpose

Create, organize, validate, enrich, and manage products.

### Responsibilities

- Product Acquisition
- Product Normalization
- Product Validation
- Product Enrichment
- Product Repository
- Manufacturer Management
- Product Specifications
- Product Images
- Product Pricing
- Product SEO
- Product Publishing

### Primary Output

Structured Products

---

## Knowledge Domain

### Purpose

Transform information into verified knowledge.

### Responsibilities

- Discovery
- Retrieval
- Evidence Collection
- Evidence Processing
- Claim Extraction
- Claim Resolution
- Provenance
- Identity Resolution
- Source Authority
- Truth Resolution
- Knowledge Modeling

### Primary Output

Verified Knowledge

---

## Commercial Domain

### Purpose

Transform verified knowledge into business intelligence.

### Responsibilities

- Affiliate Intelligence
- Pricing Intelligence
- Revenue Intelligence
- Opportunity Detection
- Sponsorship Intelligence
- SEO Intelligence
- Conversion Intelligence
- ROI Analysis
- Commercial Reporting

### Primary Output

Commercial Intelligence

---

## Platform Domain

### Purpose

Provide shared infrastructure for every domain.

### Responsibilities

- Airtable
- APIs
- Shopify
- Configuration
- Authentication
- Logging
- Storage
- Integrations
- Scheduling
- Notifications

### Primary Output

Shared Platform Services

---

## Presentation Domain

### Purpose

Deliver BotAtlas capabilities to users.

### Responsibilities

- Dashboard
- Public Website
- Admin Portal
- Reports
- Public API
- Internal Tools

### Primary Output

User Experience

---

# 5. System Layer Architecture

The platform is implemented through four architectural layers.

Each layer builds upon the layer beneath it.

---

## Layer 1 — Product Intelligence

### Purpose

Convert raw product information into structured products.

### Owns

- Products
- Manufacturers
- Categories
- Specifications
- Images
- Pricing
- Product Repository

### Consumes

Verified Knowledge

### Produces

Structured Products

---

## Layer 2 — Knowledge Processing

### Purpose

Convert raw information into verified knowledge.

### Owns

- Discovery
- Retrieval
- Evidence
- Claims
- Provenance
- Identity
- Authority
- Truth Resolution
- Knowledge Models

### Consumes

Research Requests

### Produces

Verified Knowledge

---

## Layer 3 — Commercial Intelligence

### Purpose

Transform trusted knowledge into commercial value.

### Owns

- Affiliate Intelligence
- Pricing Intelligence
- Revenue Intelligence
- SEO Intelligence
- Conversion Intelligence
- Opportunity Detection
- ROI Analysis
- Sponsorship Intelligence

### Consumes

Structured Products

Verified Knowledge

### Produces

Commercial Intelligence

---

## Layer 4 — Platform Services

### Purpose

Provide infrastructure for every layer.

### Owns

- Airtable
- APIs
- Authentication
- Configuration
- Logging
- Storage
- Shopify
- Integrations

### Produces

Shared Infrastructure

---

# 6. Domain Communication

BotAtlas follows a one-directional intelligence flow.

```

```
                    Product Requests
                           │
                           ▼
                 Knowledge Processing
                           │
                           ▼
                Verified Knowledge
                           │
                           ▼
               Product Intelligence
                           │
                           ▼
              Commercial Intelligence
                           │
                           ▼
                 Presentation Layer
```

## Communication Rules

- Product Domain may request knowledge.
- Knowledge Domain never modifies products.
- Commercial Domain consumes verified knowledge.
- Platform Domain supports every domain.
- Presentation Domain never contains business logic.

---

# 7. Capability Inventory

This section documents every major capability implemented within BotAtlas.

Every engine must belong to exactly one domain.

Every capability should have a clearly defined responsibility.

The inventory below will expand as development continues.

---

# Knowledge Processing Layer

## Mission

Transform raw information into verified knowledge.

Current capabilities will be documented individually.

| Engine | Purpose | Status | Future Evolution |
|---------|----------|--------|------------------|
| acquisition_engine.py | Acquire raw information | ✅ Implemented | Multi-source acquisition |
| discovery_engine.py | Discover information sources | ✅ Implemented | AI-assisted discovery planning |
| retrieval_adapter.py | Retrieve information from sources | ✅ Implemented | Multi-provider retrieval |
| evidence_material_acquisition.py | Collect evidence | ✅ Implemented | Distributed evidence collection |
| evidence_query_planner.py | Plan evidence collection | ✅ Implemented | AI query planning |

---

# 8. Development Philosophy

BotAtlas is designed as a long-term intelligence platform.

New functionality should extend existing capabilities rather than duplicate them.

When introducing new code, always ask:

- Which domain owns this capability?
- Which layer should implement it?
- Which existing engine should perform this work?
- Does an engine already exist that should be extended instead?

The objective is architectural consistency rather than rapid expansion.

---

# 9. Long-Term Roadmap

## Phase 1

Core Product Intelligence

**Status:** In Progress

---

## Phase 2

Knowledge Processing Platform

**Status:** In Progress

---

## Phase 3

Commercial Intelligence Platform

**Status:** Planned

---

## Phase 4

Autonomous AI Research Agents

**Status:** Future

---

## Phase 5

Global Product Knowledge Graph

**Status:** Vision

---

# Architecture Principle

The architecture of BotAtlas is capability-driven, not folder-driven.

Folders may change.

Technologies may change.

Databases may change.

Programming languages may change.

Capabilities endure.

Every architectural decision should strengthen a capability rather than simply reorganize code.

# 10. Intelligence Lifecycle

Every piece of information entering BotAtlas follows the same lifecycle.

No component may bypass this lifecycle.

```

```
External World
      │
      ▼
Research Request
      │
      ▼
Knowledge Discovery
      │
      ▼
Evidence Acquisition
      │
      ▼
Evidence Processing
      │
      ▼
Claim Extraction
      │
      ▼
Identity Resolution
      │
      ▼
Authority Analysis
      │
      ▼
Truth Resolution
      │
      ▼
Verified Knowledge
      │
      ▼
Product Intelligence
      │
      ▼
Commercial Intelligence
      │
      ▼
Presentation
```

## Lifecycle Description

### Stage 1 — Research Request

A request is generated to research a product, manufacturer, technology, or topic.

Examples

- Research Unitree G1
- Research HP LaserJet MFP X677
- Research Figure AI

Output

Research Request

---

### Stage 2 — Knowledge Discovery

Potential information sources are identified.

Examples

- Manufacturer websites
- Technical documentation
- Government databases
- Academic papers
- Retail websites
- News
- Community discussions

Output

Candidate Sources

---

### Stage 3 — Evidence Acquisition

Raw evidence is collected from discovered sources.

Examples

- Specifications
- Images
- Product manuals
- Videos
- Press releases
- Documentation

Output

Evidence

---

### Stage 4 — Evidence Processing

Evidence is cleaned, normalized, indexed, and prepared for analysis.

Output

Processed Evidence

---

### Stage 5 — Claim Extraction

Individual factual claims are extracted from evidence.

Examples

- Weight = 35 kg
- Battery life = 2 hours
- Manufacturer = Unitree

Output

Claims

---

### Stage 6 — Identity Resolution

Determine whether different references describe the same real-world entity.

Examples

- Unitree G1
- Unitree G1 EDU
- Unitree Robotics G1

Output

Resolved Entities

---

### Stage 7 — Authority Analysis

Evaluate the credibility of each source.

Factors

- Manufacturer
- Government
- Academic
- Retail
- Community

Output

Authority Scores

---

### Stage 8 — Truth Resolution

Resolve conflicting claims using evidence and authority.

Output

Verified Knowledge

---

### Stage 9 — Product Intelligence

Verified knowledge enriches structured product records.

Examples

- Product specifications
- Categories
- Features
- Images
- SEO metadata

Output

Structured Product

---

### Stage 10 — Commercial Intelligence

Structured products are analyzed for business opportunities.

Examples

- Affiliate programs
- Price intelligence
- Revenue opportunities
- SEO opportunities
- Competitive positioning

Output

Commercial Intelligence

---

### Stage 11 — Presentation

Information becomes available through dashboards, APIs, reports, websites, AI assistants, and future interfaces.

Output

Actionable Intelligence

# 11. Core Intelligence Objects

Every layer within BotAtlas transforms one intelligence object into another.

Understanding these objects is essential to understanding the architecture.

---

## Research Request

The starting point of all intelligence.

Represents a question the platform has been asked to answer.

Examples

- Research Unitree G1
- Research HP Color LaserJet Enterprise Flow MFP X677
- Research Figure 02
- Research Boston Dynamics Spot

Created By

- User
- Scheduler
- AI Agent
- Workflow
- API

Produced Output

Candidate Sources

---

## Source

A location where information may exist.

Examples

- Manufacturer Website
- Technical Manual
- Government Database
- Research Paper
- Retail Website
- Community Forum
- News Article
- YouTube Video

Produced Output

Evidence

---

## Evidence

Raw information collected from a source.

Evidence is never assumed to be true.

Examples

- PDF Manual
- Specification Sheet
- Product Images
- Product Videos
- API Response
- Web Page
- Datasheet

Produced Output

Claims

---

## Claim

A single factual statement extracted from evidence.

Examples

Manufacturer = HP

Weight = 35 kg

Battery Life = 2 Hours

Operating System = Linux

Claims may agree or conflict.

Produced Output

Resolved Claims

---

## Entity

A real-world object recognized by BotAtlas.

Examples

Product

Manufacturer

Technology

Organization

Category

Country

Person

Entities allow multiple claims to reference the same object.

Produced Output

Resolved Identity

---

## Authority Score

Represents the trustworthiness of a source.

Factors

- Source Type
- Reputation
- Provenance
- Freshness
- Verification
- Consistency

Produced Output

Confidence

---

## Verified Knowledge

A claim that has survived evidence evaluation.

Verified knowledge becomes trusted platform knowledge.

Examples

Verified Specifications

Verified Manufacturer

Verified Features

Verified Compatibility

Produced Output

Structured Product Data

---

## Structured Product

The canonical product representation inside BotAtlas.

Contains verified information only.

Examples

Specifications

Images

SEO

Pricing

Categories

Manufacturer

Produced Output

Commercial Intelligence

---

## Commercial Intelligence

Business opportunities derived from trusted product knowledge.

Examples

Affiliate Programs

SEO Opportunities

Price Monitoring

Revenue Opportunities

Market Position

Produced Output

Presentation

---

## Presentation

The final delivery of intelligence.

Examples

Dashboard

Website

API

Reports

AI Assistant

Export

Presentation never modifies intelligence.

It only communicates it.