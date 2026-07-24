from .base_claim_extractor import BaseClaimExtractor

from .runtime_extractor import RuntimeExtractor
from .weight_extractor import WeightExtractor

from .battery_extractor import BatteryExtractor
from .charging_time_extractor import ChargingTimeExtractor
from .degrees_of_freedom_extractor import (
    DegreesOfFreedomExtractor,
)
from .dimensions_extractor import DimensionsExtractor
from .manufacturer_extractor import ManufacturerExtractor
from .payload_extractor import PayloadExtractor
from .price_extractor import PriceExtractor
from .release_date_extractor import ReleaseDateExtractor
from .speed_extractor import SpeedExtractor

__all__ = [
    "BaseClaimExtractor",
    "RuntimeExtractor",
    "WeightExtractor",
    "BatteryExtractor",
    "ChargingTimeExtractor",
    "DegreesOfFreedomExtractor",
    "DimensionsExtractor",
    "ManufacturerExtractor",
    "PayloadExtractor",
    "PriceExtractor",
    "ReleaseDateExtractor",
    "SpeedExtractor",
]