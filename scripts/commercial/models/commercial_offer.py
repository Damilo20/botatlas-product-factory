from dataclasses import dataclass
from enum import Enum
from typing import Optional


class SellerRelationship(Enum):
    MANUFACTURER_DIRECT = "MANUFACTURER_DIRECT"
    AUTHORIZED_RETAILER = "AUTHORIZED_RETAILER"
    DISTRIBUTOR = "DISTRIBUTOR"
    MARKETPLACE = "MARKETPLACE"
    INTEGRATOR = "INTEGRATOR"
    UNKNOWN = "UNKNOWN"


class OfferAvailability(Enum):
    AVAILABLE = "AVAILABLE"
    PREORDER = "PREORDER"
    REQUEST_QUOTE = "REQUEST_QUOTE"
    WAITLIST = "WAITLIST"
    UNAVAILABLE = "UNAVAILABLE"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class CommercialOffer:
    product_name: str
    product_url: str
    seller_name: str
    destination_url: str
    seller_relationship: SellerRelationship
    availability: OfferAvailability
    currency: Optional[str] = None
    displayed_price: Optional[str] = None
    affiliate_relationship: bool = False
    sponsored: bool = False
    compensation_model: Optional[str] = None
    disclosure_text: Optional[str] = None
    active: bool = True
