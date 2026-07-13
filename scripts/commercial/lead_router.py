from dataclasses import dataclass

from scripts.commercial.models.qualified_lead import QualifiedLead
from scripts.commercial.offer_registry import CommercialOfferRegistry


class LeadRoutingError(ValueError):
    pass


@dataclass(frozen=True)
class LeadRoute:
    inquiry_reference: str
    product_name: str
    seller_name: str
    seller_destination_url: str
    qualification_signal: str
    routing_method: str = "PRODUCT_IDENTITY_COMMERCIAL_ROUTE"


class LeadRouter:
    """
    Routes qualified commercial inquiries through registered offers.

    Commercial routing consumes product identity.

    Commercial routing does not write intelligence conclusions.
    """

    def __init__(
        self,
        offer_registry: CommercialOfferRegistry,
    ) -> None:
        self.offer_registry = offer_registry

    def route(
        self,
        lead: QualifiedLead,
    ) -> LeadRoute:
        offers = self.offer_registry.get_offers_for_product(
            lead.product_name,
            lead.product_url,
        )

        active_offers = [
            offer
            for offer in offers
            if offer.active
        ]

        if not active_offers:
            raise LeadRoutingError(
                "No active commercial route for product identity"
            )

        offer = active_offers[0]

        return LeadRoute(
            inquiry_reference=lead.inquiry_reference,
            product_name=lead.product_name,
            seller_name=offer.seller_name,
            seller_destination_url=offer.commercial_destination_url,
            qualification_signal=lead.qualification_signal.value,
        )
