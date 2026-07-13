from dataclasses import dataclass
from enum import Enum
from typing import Optional


class InquiryType(Enum):
    PRODUCT_INFORMATION = "PRODUCT_INFORMATION"
    REQUEST_QUOTE = "REQUEST_QUOTE"
    DEMO_REQUEST = "DEMO_REQUEST"
    PROCUREMENT = "PROCUREMENT"
    ENTERPRISE_DEPLOYMENT = "ENTERPRISE_DEPLOYMENT"


class InquiryStatus(Enum):
    RECEIVED = "RECEIVED"
    ROUTABLE = "ROUTABLE"
    UNROUTABLE = "UNROUTABLE"


@dataclass(frozen=True)
class CommercialInquiry:
    inquiry_reference: str
    product_name: str
    product_url: str
    inquiry_type: InquiryType
    requester_name: str
    requester_email: str
    organization_name: Optional[str] = None
    requested_quantity: Optional[int] = None
    inquiry_message: str = ""
    status: InquiryStatus = InquiryStatus.RECEIVED
    active: bool = True
