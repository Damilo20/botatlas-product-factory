# BotAtlas Capability Catalog v1.0

> The official engineering catalog of every capability implemented within BotAtlas.

This document defines every capability that exists within the BotAtlas platform.

Unlike the Architecture document, which explains **how the platform is organized**, this catalog explains **what the platform is capable of doing**.

Every capability documented here represents a long-term business capability—not merely a Python file.

Implementations may evolve, technologies may change, and code may be rewritten, but capabilities remain.

---

# Purpose

The Capability Catalog exists to answer the following questions.

- Why does this capability exist?
- What business problem does it solve?
- Which architectural domain owns it?
- Where does it fit within the Intelligence Lifecycle?
- What information does it consume?
- What information does it produce?
- Which capabilities depend on it?
- How should it evolve over time?

---

# Capability Principles

Every capability within BotAtlas follows these principles.

## Single Responsibility

A capability owns one responsibility.

---

## Domain Ownership

Every capability belongs to one architectural domain.

---

## Information Flow

Every capability consumes information and produces information.

---

## Long-Term Evolution

Capabilities evolve.

Implementations change.

Responsibilities remain stable.

---

# Capability Index

## Knowledge Domain

- acquisition_engine.py
- discovery_engine.py
- retrieval_adapter.py
- evidence_material_acquisition.py
- evidence_query_planner.py
- claim_engine.py
- claim_extraction_engine.py
- claim_grouping_engine.py
- provenance_engine.py
- source_authority_engine.py
- truth_applicator.py
- identity_engine.py
- knowledge_engine.py

---

## Product Domain

- product_acquisition_engine.py
- product_normalization_engine.py
- product_validation_engine.py
- product_enrichment_engine.py
- product_repository.py

---

## Commercial Domain

Documentation Pending

---

## Platform Domain

Documentation Pending

---

## Presentation Domain

Documentation Pending

---

# Capability Specification Template

Every capability documented in this catalog follows the same specification.

---

## Capability Name

### Purpose

Why does this capability exist?

---

### Business Value

What business problem does it solve?

---

### Architectural Domain

Product

Knowledge

Commercial

Platform

Presentation

---

### Intelligence Lifecycle Stage

Which stage of the Intelligence Lifecycle owns this capability?

---

### Capability Type

Core Capability

Supporting Capability

Integration Capability

---

### Inputs

Information consumed.

---

### Outputs

Information produced.

---

### Dependencies

Capabilities required.

---

### Used By

Capabilities that consume this capability.

---

### Current Status

Implemented

Partial

Planned

Experimental

Deprecated

---

### Long-Term Vision

Describe the long-term evolution of this capability.

---

### Architectural Notes

Important design decisions, limitations, and architectural responsibilities.

---

# Knowledge Domain

The Knowledge Domain transforms raw information into verified knowledge.

Capabilities within this domain never modify products or make commercial decisions.

Their sole responsibility is to discover, acquire, evaluate, organize, and verify knowledge.

---

# acquisition_engine.py

## Purpose

Acquire raw information required to satisfy a research request.

This engine represents the primary entry point into the Knowledge Processing Layer.

Its responsibility is to coordinate information acquisition without evaluating evidence or determining truth.

---

### Business Value

Provides a standardized mechanism for collecting information from multiple sources while separating acquisition from verification.

---

### Architectural Domain

Knowledge

---

### Intelligence Lifecycle Stage

Evidence Acquisition

---

### Capability Type

Core Capability

---

### Inputs

- Research Request
- Configuration
- Source Information

---

### Outputs

- Raw Information
- Acquisition Results

---

### Dependencies

- discovery_engine.py
- retrieval_adapter.py

---

### Used By

- evidence_material_acquisition.py
- Knowledge Processing Pipeline

---

### Current Status

✅ Implemented

---

### Long-Term Vision

Future versions should support:

- Parallel acquisition
- Distributed workers
- Streaming acquisition
- Retry orchestration
- Source prioritization
- AI-directed acquisition planning
- Multi-provider acquisition strategies
- Intelligent workload balancing

---

### Architectural Notes

This capability acquires information.

It does not evaluate evidence.

It does not determine truth.

Truth belongs to later stages of the Knowledge Processing Layer.

Information quality should never influence acquisition logic.

---