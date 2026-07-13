from dataclasses import dataclass
from enum import Enum
from typing import Optional


class RevenueChannel(Enum):
    AFFILIATE = "AFFILIATE"
    SPONSORSHIP = "SPONSORSHIP"
    LEAD_GENERATION = "LEAD_GENERATION"
    SUBSCRIPTION = "SUBSCRIPTION"
    API = "API"
    DATA_LICENSING = "DATA_LICENSING"
    MANUFACTURER_INTELLIGENCE = "MANUFACTURER_INTELLIGENCE"


class DisclosureRequirement(Enum):
    REQUIRED = "REQUIRED"
    NOT_REQUIRED = "NOT_REQUIRED"
    UNDETERMINED = "UNDETERMINED"


@dataclass(frozen=True)
class CommercialOpportunity:
    product_name: str
    product_url: str
    revenue_channel: RevenueChannel
    commercial_partner_name: Optional[str] = None
    commercial_destination_url: Optional[str] = None
    compensation_model: Optional[str] = None
    disclosure_requirement: DisclosureRequirement = (
        DisclosureRequirement.UNDETERMINED
    )
    active: bool = True
