from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class RevenueEventType(Enum):
    AFFILIATE_CLICK = "AFFILIATE_CLICK"
    AFFILIATE_CONVERSION = "AFFILIATE_CONVERSION"
    QUALIFIED_LEAD = "QUALIFIED_LEAD"
    SPONSORED_PLACEMENT = "SPONSORED_PLACEMENT"
    SUBSCRIPTION = "SUBSCRIPTION"
    API_USAGE = "API_USAGE"
    DATA_LICENSE = "DATA_LICENSE"
    MANUFACTURER_INTELLIGENCE = "MANUFACTURER_INTELLIGENCE"


class RevenueEventStatus(Enum):
    RECORDED = "RECORDED"
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    REVERSED = "REVERSED"


@dataclass(frozen=True)
class RevenueEvent:
    event_reference: str
    event_type: RevenueEventType
    product_name: str
    product_url: str
    revenue_channel: str
    commercial_reference: str
    currency: Optional[str] = None
    gross_amount: Optional[str] = None
    compensation_model: Optional[str] = None
    event_status: RevenueEventStatus = RevenueEventStatus.RECORDED
    occurred_at: datetime = datetime.now(timezone.utc)
    active: bool = True
