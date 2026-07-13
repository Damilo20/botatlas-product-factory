from collections import defaultdict

from scripts.commercial.models.commercial_offer import CommercialOffer


class CommercialOfferRegistry:
    """
    Commercial offer registry.

    Stores and retrieves commercial destinations by product identity.

    Does not rank evidence, verify products, resolve claims, or decide truth.
    """

    def __init__(self) -> None:
        self._offers_by_product: dict[str, list[CommercialOffer]] = defaultdict(list)

    def register(self, offer: CommercialOffer) -> None:
        self._offers_by_product[offer.product_url].append(offer)

    def register_all(self, offers: list[CommercialOffer]) -> None:
        for offer in offers:
            self.register(offer)

    def get_offers(self, product_url: str) -> list[CommercialOffer]:
        return list(self._offers_by_product.get(product_url, []))

    def get_active_offers(self, product_url: str) -> list[CommercialOffer]:
        return [
            offer
            for offer in self.get_offers(product_url)
            if offer.active
        ]
