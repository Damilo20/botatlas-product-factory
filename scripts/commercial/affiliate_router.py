from scripts.commercial.models.commercial_offer import CommercialOffer
from scripts.commercial.models.commercial_route import (
    CommercialRoute,
    RouteType,
)


class CommercialDisclosureError(ValueError):
    pass


class AffiliateRouter:
    """
    Converts commercial offers into navigable commercial routes.

    Affiliate and sponsored routes require explicit disclosure.

    Routing does not rank evidence, verify claims, select truth,
    or modify intelligence records.
    """

    def route(self, offer: CommercialOffer) -> CommercialRoute:
        if offer.sponsored:
            route_type = RouteType.SPONSORED
        elif offer.affiliate_relationship:
            route_type = RouteType.AFFILIATE
        else:
            route_type = RouteType.DIRECT

        disclosure_required = route_type in {
            RouteType.AFFILIATE,
            RouteType.SPONSORED,
        }

        if disclosure_required and not (
            offer.disclosure_text and offer.disclosure_text.strip()
        ):
            raise CommercialDisclosureError(
                f"{route_type.value} route requires disclosure"
            )

        return CommercialRoute(
            product_name=offer.product_name,
            seller_name=offer.seller_name,
            destination_url=offer.destination_url,
            route_type=route_type,
            disclosure_required=disclosure_required,
            disclosure_text=offer.disclosure_text,
        )

    def route_all(
        self,
        offers: list[CommercialOffer],
    ) -> list[CommercialRoute]:
        return [
            self.route(offer)
            for offer in offers
            if offer.active
        ]
