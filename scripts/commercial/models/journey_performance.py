from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class JourneyPerformance:
    journey_count: int
    converting_journey_count: int
    attributed_event_count: int
    partially_attributed_event_count: int
    unattributed_event_count: int
    attribution_coverage: Decimal
    journey_conversion_rate: Decimal
