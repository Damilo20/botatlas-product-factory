from scripts.commercial.models.commercial_inquiry import (
    CommercialInquiry,
    InquiryType,
)
from scripts.commercial.models.qualified_lead import (
    LeadQualificationSignal,
    QualifiedLead,
)


class LeadQualificationEngine:
    """
    Classifies commercial intent.

    Qualification describes the commercial inquiry.

    It does not assess evidence, resolve claims, verify products,
    assign authority, or decide truth.
    """

    SIGNAL_BY_INQUIRY_TYPE = {
        InquiryType.PRODUCT_INFORMATION:
            LeadQualificationSignal.GENERAL,
        InquiryType.REQUEST_QUOTE:
            LeadQualificationSignal.COMMERCIAL_INTENT,
        InquiryType.DEMO_REQUEST:
            LeadQualificationSignal.COMMERCIAL_INTENT,
        InquiryType.PROCUREMENT:
            LeadQualificationSignal.PROCUREMENT_INTENT,
        InquiryType.ENTERPRISE_DEPLOYMENT:
            LeadQualificationSignal.ENTERPRISE_INTENT,
    }

    def qualify(
        self,
        inquiry: CommercialInquiry,
    ) -> QualifiedLead:
        signal = self.SIGNAL_BY_INQUIRY_TYPE[
            inquiry.inquiry_type
        ]

        return QualifiedLead(
            inquiry_reference=inquiry.inquiry_reference,
            product_name=inquiry.product_name,
            product_url=inquiry.product_url,
            inquiry_type=inquiry.inquiry_type,
            requester_name=inquiry.requester_name,
            requester_email=inquiry.requester_email,
            organization_name=inquiry.organization_name,
            requested_quantity=inquiry.requested_quantity,
            qualification_signal=signal,
            qualification_method="COMMERCIAL_INTENT_CLASSIFICATION",
            active=inquiry.active,
        )

    def qualify_all(
        self,
        inquiries: list[CommercialInquiry],
    ) -> list[QualifiedLead]:
        return [
            self.qualify(inquiry)
            for inquiry in inquiries
        ]
