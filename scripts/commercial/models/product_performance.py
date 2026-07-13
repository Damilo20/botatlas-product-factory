from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class ProductPerformance:
    product_name: str
    product_url: str
    event_count: int
    confirmed_event_count: int
    conversion_count: int
    confirmed_gross_revenue: Decimal
    attributed_event_count: int
    partially_attributed_event_count: int
    unattributed_event_count: int
