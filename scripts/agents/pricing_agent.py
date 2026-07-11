from scripts.models.product import Product


class PricingAgent:
    """
    Responsible for pricing and marketplace information.
    """

    def enrich(self, product: Product) -> Product:

        print("💲 Gathering pricing information...")

        # Temporary demo values
        product.msrp = 30000
        product.current_price = 28999

        product.official_store = "Figure AI"

        product.amazon_url = None

        product.affiliate_url = None

        return product