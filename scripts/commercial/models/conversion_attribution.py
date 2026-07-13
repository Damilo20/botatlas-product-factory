from dataclasses import dataclass
from enum import Enum
from typing import Optional

from scripts.commercial.models.conversion_journey import ConversionJourney
from scripts.commercial.models.revenue_event import RevenueEvent


class AttributionState(Enum):
    ATTRIBUTED = "ATTRIBUTED"
    PARTIALLY_ATTRIBUTED = "PARTIALLY_ATTRIBUTED"
    UNATTRIBUTED = "UNATTRIBUTED"


@dataclass(frozen=True)
class ConversionAttribution:
    revenue_event: RevenueEvent
    journey: Optional[ConversionJourney]
    attribution_state: AttributionState
    matched_product_url: bool
    matched_commercial_reference: bool
    attribution_method: str
