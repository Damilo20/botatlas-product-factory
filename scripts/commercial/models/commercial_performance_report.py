from dataclasses import dataclass
from decimal import Decimal

from scripts.commercial.models.product_revenue_summary import (
    ProductRevenueSummary,
)
from scripts.commercial.models.revenue_channel_summary import (
    RevenueChannelSummary,
)


@dataclass(frozen=True)
class CommercialPerformanceReport:
    total_event_count: int
    recorded_event_count: int
    pending_event_count: int
    confirmed_event_count: int
    reversed_event_count: int
    confirmed_gross_revenue: Decimal
    pending_revenue: Decimal
    reversed_revenue: Decimal
    channel_summaries: list[RevenueChannelSummary]
    product_summaries: list[ProductRevenueSummary]
