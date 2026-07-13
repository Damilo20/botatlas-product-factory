# BotAtlas Layer 10 — Evidence Weighting & Source Authority

## Purpose

Layer 10 assesses evidence characteristics that may later inform
claim reasoning.

Layer 10 does not declare truth.

Layer 10 receives reconciled claims and their preserved Layer 8 evidence
lineage from Layer 9.

Its responsibility is to describe source authority and evidence strength
without selecting a winning claim.

---

## Constitutional Boundary

Layer 10 may assess:

- source family
- source authority characteristics
- evidence directness
- provenance completeness
- claim specificity
- material freshness
- independent corroboration
- source duplication
- evidence support characteristics

Layer 10 must not:

- verify a claim
- declare a claim true
- declare a claim false
- select a winning claim
- resolve a disputed claim
- overwrite reconciliation state
- silently discard contradictory evidence
- convert authority into truth
- convert evidence weight into verification

---

## Core Principle

Authority is not truth.

Weight is not verification.

A highly authoritative source may still contain:

- outdated information
- incomplete information
- ambiguous information
- product-family information applied to the wrong model
- conflicting information

A lower-authority source may contain relevant direct evidence.

Layer 10 preserves this distinction.

---

## Architecture

ClaimReconciliation[]
        |
        v
SourceAuthorityAssessmentEngine
        |
        v
SourceAuthorityAssessment[]
        |
        v
EvidenceWeightEngine
        |
        v
WeightedEvidenceAssessment[]

---

## Source Authority Assessment

A SourceAuthorityAssessment describes characteristics of a source.

Possible authority dimensions include:

- source family
- manufacturer relationship
- documentation relationship
- technical specialization
- retailer relationship
- editorial independence

The assessment is descriptive.

It is not a truth decision.

---

## Evidence Weight Assessment

A WeightedEvidenceAssessment describes evidence characteristics.

Possible dimensions include:

- authority signal
- directness signal
- provenance completeness
- claim specificity
- freshness signal
- corroboration signal
- duplication signal

Weights are reasoning inputs only.

They are not final claim decisions.

---

## Source Families

Layer 10 recognizes the preserved Layer 7 source families:

- OFFICIAL_MANUFACTURER
- OFFICIAL_DOCUMENTATION
- AUTHORIZED_RETAILER
- TECHNICAL_SOURCE
- INDEPENDENT_REPORTING

Source family may influence authority assessment.

Source family alone must never establish truth.

---

## Contradiction Preservation

If Layer 9 produces:

runtime:
- 5 hours
- 4.5 hours

with reconciliation state:

DISPUTED

Layer 10 must preserve both claims.

Layer 10 may assess their evidence characteristics independently.

Layer 10 must not automatically change:

DISPUTED

into:

CONSISTENT

or:

VERIFIED

because one source has a stronger authority signal.

---

## Corroboration

Independent corroboration may strengthen an evidence assessment.

Repeated copies of the same originating claim must not automatically count
as independent corroboration.

Example:

Manufacturer claim
    |
    +--> Retailer copy
    |
    +--> News article quoting manufacturer

These may represent one originating information lineage.

Layer 10 must preserve the distinction between:

source count

and

independent corroboration.

---

## Forbidden Decision Concepts

The following concepts are forbidden from Layer 10 runtime contracts:

- verified
- verification_status
- truth
- true
- false
- winner
- winning_claim
- selected_claim
- resolved_value
- final_value
- accepted_claim
- rejected_claim

Layer 10 describes evidence.

Layer 10 does not decide truth.

---

## Layer 10 Output Principle

Layer 10 answers:

"What characteristics does this evidence have?"

Layer 10 does not answer:

"Which claim is true?"

---

## Architectural Rule

Layer 9 classifies claim relationships.

Layer 10 assesses evidence characteristics.

A later trust or decision layer may consume these assessments.

That later layer must remain architecturally separate.

---

## BotAtlas Principle

Evidence may be strong without being truth.

Authority may be high without being infallible.

Disagreement must survive weighting.

Uncertainty must remain visible.
