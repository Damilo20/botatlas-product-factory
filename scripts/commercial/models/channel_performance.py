from dataclasses import dataclass
from decimal import Decimal

from scripts.commercial.models.commercial_opportunity import RevenueChannel


@dataclass(frozen=True)
class ChannelPerformance:
    revenue_channel: RevenueChannel
    event_count: int
    confirmed_event_count: int
    conversion_count: int
    confirmed_gross_revenue: Decimal
