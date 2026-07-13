from dataclasses import dataclass
from enum import Enum
from typing import Optional

from scripts.commercial.models.commercial_inquiry import InquiryType


class LeadQualificationSignal(Enum):
    GENERAL = "GENERAL"
    COMMERCIAL_INTENT = "COMMERCIAL_INTENT"
    PROCUREMENT_INTENT = "PROCUREMENT_INTENT"
    ENTERPRISE_INTENT = "ENTERPRISE_INTENT"


@dataclass(frozen=True)
class QualifiedLead:
    inquiry_reference: str
    product_name: str
    product_url: str
    inquiry_type: InquiryType
    requester_name: str
    requester_email: str
    qualification_signal: LeadQualificationSignal
    organization_name: Optional[str] = None
    requested_quantity: Optional[int] = None
    qualification_method: str = "COMMERCIAL_INTENT_CLASSIFICATION"
    active: bool = True
