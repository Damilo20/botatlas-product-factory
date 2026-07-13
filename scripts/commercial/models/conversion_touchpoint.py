from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class TouchpointType(Enum):
    DISCOVERY = "DISCOVERY"
    PRODUCT_VIEW = "PRODUCT_VIEW"
    COMMERCIAL_CLICK = "COMMERCIAL_CLICK"
    INQUIRY = "INQUIRY"
    QUALIFIED_LEAD = "QUALIFIED_LEAD"
    CONVERSION = "CONVERSION"


@dataclass(frozen=True)
class ConversionTouchpoint:
    touchpoint_reference: str
    journey_reference: str
    product_name: str
    product_url: str
    touchpoint_type: TouchpointType
    source_reference: Optional[str]
    commercial_reference: Optional[str]
    occurred_at: datetime
    active: bool = True
