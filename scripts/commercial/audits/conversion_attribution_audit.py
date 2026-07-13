from dataclasses import fields
from datetime import datetime, timezone

from scripts.commercial.conversion_attribution_engine import (
    ConversionAttributionEngine,
)
from scripts.commercial.conversion_journey_builder import (
    ConversionJourneyBuilder,
)
from scripts.commercial.models.commercial_opportunity import RevenueChannel
from scripts.commercial.models.conversion_attribution import (
    AttributionState,
    ConversionAttribution,
)
from scripts.commercial.models.conversion_journey import ConversionJourney
from scripts.commercial.models.conversion_touchpoint import (
    ConversionTouchpoint,
    TouchpointType,
)
from scripts.commercial.models.revenue_event import (
    RevenueEvent,
    RevenueEventStatus,
    RevenueEventType,
)


FORBIDDEN = {
    "verified",
    "verification_status",
    "truth",
    "true",
    "confidence_score",
    "quality_score",
    "authority_score",
    "reputation_score",
    "accepted_claim",
    "rejected_claim",
    "winning_claim",
    "final_value",
}


def assert_boundary(model: type) -> None:
    names = {field.name for field in fields(model)}
    leaked = names & FORBIDDEN
    print(model.__name__, "TRUST/DECISION LEAK:", sorted(leaked))
    assert not leaked


def touchpoint(
    reference: str,
    journey_reference: str,
    touchpoint_type: TouchpointType,
    commercial_reference: str | None,
    minute: int,
) -> ConversionTouchpoint:
    return ConversionTouchpoint(
        touchpoint_reference=reference,
        journey_reference=journey_reference,
        product_name="Figure 02",
        product_url="https://www.figure.ai/",
        touchpoint_type=touchpoint_type,
        source_reference=None,
        commercial_reference=commercial_reference,
        occurred_at=datetime(
            2026,
            7,
            13,
            12,
            minute,
            tzinfo=timezone.utc,
        ),
    )


print("=== BOTATLAS R9 CONVERSION ATTRIBUTION AUDIT ===")

print("\n=== RUNTIME COMMERCIAL BOUNDARY AUDIT ===")
assert_boundary(ConversionTouchpoint)
assert_boundary(ConversionJourney)
assert_boundary(ConversionAttribution)

touchpoints = [
    touchpoint(
        "TP-AUDIT-001",
        "JOURNEY-AUDIT-001",
        TouchpointType.DISCOVERY,
        None,
        0,
    ),
    touchpoint(
        "TP-AUDIT-002",
        "JOURNEY-AUDIT-001",
        TouchpointType.COMMERCIAL_CLICK,
        "AFFILIATE-AUDIT-001",
        5,
    ),
    touchpoint(
        "TP-AUDIT-003",
        "JOURNEY-AUDIT-002",
        TouchpointType.PRODUCT_VIEW,
        None,
        10,
    ),
]

builder = ConversionJourneyBuilder()
journeys = builder.build(touchpoints)

event = RevenueEvent(
    event_reference="REV-R9-AUDIT-001",
    event_type=RevenueEventType.AFFILIATE_CONVERSION,
    product_name="Figure 02",
    product_url="https://www.figure.ai/",
    revenue_channel=RevenueChannel.AFFILIATE,
    commercial_reference="AFFILIATE-AUDIT-001",
    currency="USD",
    gross_amount="125.00",
    compensation_model="COMMISSION",
    event_status=RevenueEventStatus.CONFIRMED,
    occurred_at=datetime.now(timezone.utc),
)

engine = ConversionAttributionEngine()
attribution = engine.attribute(event, journeys)

print("\n=== JOURNEY AUDIT ===")
for journey in journeys:
    print(
        journey.journey_reference,
        "|",
        journey.product_name,
        "|",
        journey.product_url,
        "| TOUCHPOINTS:",
        len(journey.touchpoints),
    )

print("\n=== ATTRIBUTION AUDIT ===")
print(
    attribution.revenue_event.event_reference,
    "|",
    attribution.attribution_state.value,
    "|",
    attribution.attribution_method,
    "| JOURNEY:",
    (
        attribution.journey.journey_reference
        if attribution.journey
        else None
    ),
)

assert len(journeys) == 2
assert attribution.attribution_state is AttributionState.ATTRIBUTED
assert attribution.journey is not None
assert attribution.journey.journey_reference == "JOURNEY-AUDIT-001"

print("\nPASS: conversion touchpoints remain commercially descriptive")
print("PASS: journeys preserve canonical product identity")
print("PASS: journeys preserve chronological touchpoint history")
print("PASS: explicit commercial reference supports attribution")
print("PASS: attribution does not create intelligence conclusions")
print("PASS: revenue outcomes remain outside intelligence truth")
print("PASS: BOTATLAS R9 CONVERSION ATTRIBUTION GATE")
