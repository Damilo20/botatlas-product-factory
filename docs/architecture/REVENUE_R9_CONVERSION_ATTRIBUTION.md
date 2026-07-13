# BotAtlas R9 — Conversion Attribution

## Purpose

Layer R9 traces the commercial journey associated with revenue events.

R9 answers:

"What commercial journey produced this commercial outcome?"

R9 does not answer:

"Which product is better?"
"Which claim is true?"
"Which evidence should win?"

---

## Architecture

ConversionTouchpoint[]
        |
        v
ConversionJourney
        |
        v
ConversionAttributionEngine
        |
        v
ConversionAttribution
        |
        v
RevenueEvent

---

## Attribution Principle

Commercial outcomes may be attributed to commercial journeys.

Commercial outcomes may not alter intelligence conclusions.

---

## Trust Boundary

Forbidden from R9 contracts:

- verified
- verification_status
- truth
- true
- confidence_score
- authority_score
- quality_score
- accepted_claim
- rejected_claim
- final_value
- winning_claim
- product_score

---

## BotAtlas Principle

Revenue may explain commercial performance.

Revenue may not define product truth.
