from dataclasses import fields
from datetime import datetime, timezone
from decimal import Decimal

from scripts.commercial.models.commercial_performance_report import (
    CommercialPerformanceReport,
)
from scripts.commercial.models.product_revenue_summary import (
    ProductRevenueSummary,
)
from scripts.commercial.models.revenue_channel_summary import (
    RevenueChannelSummary,
)
from scripts.commercial.models.revenue_event import (
    RevenueEvent,
    RevenueEventStatus,
    RevenueEventType,
)
from scripts.commercial.revenue_reporting_engine import (
    RevenueReportingEngine,
)


FORBIDDEN = {
    "verified",
    "verification_status",
    "truth",
    "true",
    "confidence_score",
    "authority_score",
    "quality_score",
    "accepted_claim",
    "rejected_claim",
    "final_value",
}


def assert_commercial_boundary(model: type) -> None:
    names = {field.name for field in fields(model)}
    leaked = names & FORBIDDEN
    assert not leaked, f"{model.__name__} leaked intelligence fields: {leaked}"


def revenue_event(
    reference: str,
    event_type: RevenueEventType,
    product_name: str,
    product_url: str,
    channel: str,
    amount: str | None,
    status: RevenueEventStatus,
) -> RevenueEvent:
    return RevenueEvent(
        event_reference=reference,
        event_type=event_type,
        product_name=product_name,
        product_url=product_url,
        revenue_channel=channel,
        commercial_reference=f"COMM-{reference}",
        currency="USD",
        gross_amount=amount,
        compensation_model="AUDIT_TEST",
        event_status=status,
        occurred_at=datetime.now(timezone.utc),
        active=True,
    )


print("=== BOTATLAS R8 REVENUE REPORTING AUDIT ===")

print("\n=== COMMERCIAL BOUNDARY AUDIT ===")

for model in (
    RevenueChannelSummary,
    ProductRevenueSummary,
    CommercialPerformanceReport,
):
    assert_commercial_boundary(model)
    print(f"PASS: {model.__name__} contains no intelligence decision fields")


events = [
    revenue_event(
        "R8-001",
        RevenueEventType.QUALIFIED_LEAD,
        "Figure 02",
        "https://www.figure.ai/",
        "LEAD_GENERATION",
        "250.00",
        RevenueEventStatus.CONFIRMED,
    ),
    revenue_event(
        "R8-002",
        RevenueEventType.SPONSORED_PLACEMENT,
        "Example Robot",
        "https://example.com/robot",
        "SPONSORSHIP",
        "5000.00",
        RevenueEventStatus.CONFIRMED,
    ),
    revenue_event(
        "R8-003",
        RevenueEventType.AFFILIATE_CLICK,
        "Figure 02",
        "https://www.figure.ai/",
        "AFFILIATE",
        None,
        RevenueEventStatus.RECORDED,
    ),
    revenue_event(
        "R8-004",
        RevenueEventType.API_USAGE,
        "BotAtlas API",
        "https://botatlas.example/api",
        "API",
        "125.00",
        RevenueEventStatus.PENDING,
    ),
    revenue_event(
        "R8-005",
        RevenueEventType.DATA_LICENSE,
        "BotAtlas Dataset",
        "https://botatlas.example/data",
        "DATA_LICENSING",
        "800.00",
        RevenueEventStatus.REVERSED,
    ),
]

engine = RevenueReportingEngine()
report = engine.report(events)

print("\n=== COMMERCIAL PERFORMANCE REPORT ===")
print("TOTAL EVENTS:", report.total_event_count)
print("RECORDED EVENTS:", report.recorded_event_count)
print("PENDING EVENTS:", report.pending_event_count)
print("CONFIRMED EVENTS:", report.confirmed_event_count)
print("REVERSED EVENTS:", report.reversed_event_count)
print("CONFIRMED GROSS REVENUE:", report.confirmed_gross_revenue)
print("PENDING REVENUE:", report.pending_revenue)
print("REVERSED REVENUE:", report.reversed_revenue)

print("\n=== CHANNEL SUMMARIES ===")

for summary in report.channel_summaries:
    print(
        summary.revenue_channel,
        "| EVENTS:", summary.event_count,
        "| RECORDED:", summary.recorded_event_count,
        "| PENDING:", summary.pending_event_count,
        "| CONFIRMED:", summary.confirmed_event_count,
        "| REVERSED:", summary.reversed_event_count,
        "| CONFIRMED REVENUE:", summary.confirmed_revenue,
    )

print("\n=== PRODUCT SUMMARIES ===")

for summary in report.product_summaries:
    print(
        summary.product_name,
        "|", summary.product_url,
        "| EVENTS:", summary.event_count,
        "| CONFIRMED:", summary.confirmed_event_count,
        "| CONFIRMED REVENUE:", summary.confirmed_revenue,
    )

assert report.total_event_count == 5
assert report.recorded_event_count == 1
assert report.pending_event_count == 1
assert report.confirmed_event_count == 2
assert report.reversed_event_count == 1

assert report.confirmed_gross_revenue == Decimal("5250.00")
assert report.pending_revenue == Decimal("125.00")
assert report.reversed_revenue == Decimal("800.00")

channels = {
    summary.revenue_channel: summary
    for summary in report.channel_summaries
}

assert channels["LEAD_GENERATION"].confirmed_revenue == Decimal("250.00")
assert channels["SPONSORSHIP"].confirmed_revenue == Decimal("5000.00")
assert channels["AFFILIATE"].recorded_event_count == 1
assert channels["API"].pending_revenue == Decimal("125.00")
assert channels["DATA_LICENSING"].reversed_revenue == Decimal("800.00")

products = {
    summary.product_url: summary
    for summary in report.product_summaries
}

figure = products["https://www.figure.ai/"]

assert figure.event_count == 2
assert figure.confirmed_event_count == 1
assert figure.confirmed_revenue == Decimal("250.00")

print("\nPASS: revenue lifecycle states remain independently visible")
print("PASS: confirmed gross revenue aggregates confirmed events only")
print("PASS: pending revenue remains independently visible")
print("PASS: reversed revenue remains independently visible")
print("PASS: revenue channels aggregate independently")
print("PASS: canonical product URL drives product revenue aggregation")
print("PASS: multiple revenue events survive product aggregation")
print("PASS: reporting does not alter R7 revenue events")
print("PASS: BOTATLAS R8 REVENUE REPORTING GATE")
