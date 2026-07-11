from scripts.models.product import Product


class TechnicalAgent:
    """
    Responsible for collecting and enriching
    technical specifications.
    """

    def enrich(self, product: Product) -> Product:

        print("⚙️ Gathering technical specifications...")

        product.weight = "70 kg"
        product.runtime = "5 hours"
        product.battery = "Lithium-Ion"
        product.connectivity = "Wi-Fi / Ethernet"

        return product