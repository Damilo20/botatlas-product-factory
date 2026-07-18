from scripts.repositories.product_repository import ProductRepository


class ProductIntelligencePipeline:

    def __init__(self):
        self.products = ProductRepository()

    def run(self):
        print("=" * 60)
        print("BOTATLAS PRODUCT INTELLIGENCE PIPELINE")
        print("=" * 60)

        records = self.products.list_products()

        print(f"Products Found: {len(records)}")

        for product in records:
            fields = product["fields"]

            print("-" * 60)
            print(fields.get("Product Name", "Unnamed"))
            print(fields.get("Category", ""))
            print(fields.get("Primary Use", ""))
            print(fields.get("Status", ""))