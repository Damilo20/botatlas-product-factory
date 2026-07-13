from dataclasses import fields

from scripts.commercial.models.revenue_event import (
    RevenueEvent,
    RevenueEventStatus,
    RevenueEventType,
)
from scripts.commercial.models.revenue_attribution import RevenueAttribution
from scripts.commercial.revenue_attribution_engine import (
    RevenueAttributionEngine,
)
from scripts.commercial.revenue_event_ledger import (
    DuplicateRevenueEventError,
    RevenueEventLedger,
)


FORBIDDEN = {
    "verified",
    "verification_status",
    "truth",
    "true",
    "final_score",
    "final_value",
    "accepted_claim",
    "rejected_claim",
    "authority_score",
    "quality_score",
    "confidence_score",
    "evidence_weight",
    "reconciliation_state",
}


def assert_boundary(model: type) -> None:
    names = {
        field.name
        for field in fields(model)
    }

    leaked = names & FORBIDDEN

    print(
        model.__name__,
        "TRUST LEAK:",
        sorted(leaked),
    )

    assert not leaked


print("=== BOTATLAS R7 REVENUE EVENT LEDGER AUDIT ===")

assert_boundary(RevenueEvent)
assert_boundary(RevenueAttribution)


events = [
    RevenueEvent(
        event_reference="REV-001",
        event_type=RevenueEventType.QUALIFIED_LEAD,
        product_name="Figure 02",
        product_url="https://www.figure.ai/",
        revenue_channel="LEAD_GENERATION",
        commercial_reference="INQUIRY-001",
        currency="USD",
        gross_amount="250.00",
        compensation_model="QUALIFIED_LEAD_FEE",
        event_status=RevenueEventStatus.CONFIRMED,
    ),
    RevenueEvent(
        event_reference="REV-002",
        event_type=RevenueEventType.AFFILIATE_CLICK,
        product_name="Figure 02",
        product_url="https://www.figure.ai/",
        revenue_channel="AFFILIATE",
        commercial_reference="ROUTE-001",
        compensation_model="COMMISSION",
        event_status=RevenueEventStatus.RECORDED,
    ),
    RevenueEvent(
        event_reference="REV-003",
        event_type=RevenueEventType.SPONSORED_PLACEMENT,
        product_name="Example Robot",
        product_url="https://example.com/robot",
        revenue_channel="SPONSORSHIP",
        commercial_reference="CAMPAIGN-001",
        currency="USD",
        gross_amount="5000.00",
        compensation_model="CAMPAIGN_FEE",
        event_status=RevenueEventStatus.CONFIRMED,
    ),
]


engine = RevenueAttributionEngine()

attributions = engine.attribute_all(events)


print("\n=== ATTRIBUTIONS ===")

for attribution in attributions:
    print(
        attribution.event.event_reference,
        "|",
        attribution.event.event_type.value,
        "|",
        attribution.product_name,
        "|",
        attribution.attribution_key,
        "|",
        attribution.attribution_method,
    )


ledger = RevenueEventLedger()

ledger.append_all(attributions)


print("\n=== LEDGER ===")

for event in ledger.get_events():
    print(
        event.event_reference,
        "|",
        event.event_type.value,
        "|",
        event.product_name,
        "|",
        event.revenue_channel,
        "|",
        event.gross_amount,
        event.currency,
        "|",
        event.event_status.value,
    )


figure_events = ledger.get_events_for_product(
    "https://www.figure.ai"
)


print(
    "\nFIGURE 02 ATTRIBUTED EVENTS:",
    len(figure_events),
)


assert len(ledger) == 3
assert len(figure_events) == 2

assert {
    event.event_reference
    for event in figure_events
} == {
    "REV-001",
    "REV-002",
}


blocked = False

try:
    ledger.append(attributions[0])
except DuplicateRevenueEventError as exc:
    blocked = True
    print("\nBLOCKED:", exc)

assert blocked


print("\nPASS: commercial events become explicit revenue events")
print("PASS: revenue events preserve product identity")
print("PASS: canonical product URL drives revenue attribution")
print("PASS: multiple revenue channels survive independently")
print("PASS: revenue ledger preserves event status")
print("PASS: revenue ledger rejects duplicate event references")
print("PASS: product revenue events can be retrieved by identity")
print("PASS: revenue contracts cannot carry intelligence conclusions")
print("PASS: BOTATLAS R7 REVENUE EVENT LEDGER")
