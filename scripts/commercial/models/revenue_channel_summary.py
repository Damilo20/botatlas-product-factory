from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class RevenueChannelSummary:
    revenue_channel: str
    event_count: int
    recorded_event_count: int
    pending_event_count: int
    confirmed_event_count: int
    reversed_event_count: int
    confirmed_revenue: Decimal
    pending_revenue: Decimal
    reversed_revenue: Decimal
