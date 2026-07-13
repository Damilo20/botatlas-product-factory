from dataclasses import dataclass

from scripts.commercial.models.revenue_event import RevenueEvent


@dataclass(frozen=True)
class RevenueAttribution:
    event: RevenueEvent
    product_name: str
    product_url: str
    attribution_key: str
    attribution_method: str
