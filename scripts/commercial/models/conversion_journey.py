from dataclasses import dataclass

from scripts.commercial.models.conversion_touchpoint import (
    ConversionTouchpoint,
)


@dataclass(frozen=True)
class ConversionJourney:
    journey_reference: str
    product_name: str
    product_url: str
    touchpoints: list[ConversionTouchpoint]
