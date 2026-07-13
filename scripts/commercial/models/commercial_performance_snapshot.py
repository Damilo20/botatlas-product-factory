from dataclasses import dataclass
from decimal import Decimal

from scripts.commercial.models.channel_performance import ChannelPerformance
from scripts.commercial.models.journey_performance import JourneyPerformance
from scripts.commercial.models.product_performance import ProductPerformance


@dataclass(frozen=True)
class CommercialPerformanceSnapshot:
    total_event_count: int
    confirmed_event_count: int
    conversion_count: int
    confirmed_gross_revenue: Decimal
    product_performance: list[ProductPerformance]
    channel_performance: list[ChannelPerformance]
    journey_performance: JourneyPerformance
