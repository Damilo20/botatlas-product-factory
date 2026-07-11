import json
from dataclasses import asdict
from pathlib import Path

from scripts.models.product import Product


class ProductRepository:
    """
    BotAtlas Product Repository.

    Responsible for persisting and retrieving
    product intelligence records.
    """

    def __init__(self, storage_path: str = "data/products"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)

    def save(self, product: Product) -> Path:
        """
        Save a Product object as structured JSON.
        """

        file_name = self._build_file_name(product)
        file_path = self.storage_path / file_name

        product_data = asdict(product)

        with file_path.open("w", encoding="utf-8") as file:
            json.dump(
                product_data,
                file,
                indent=4,
                ensure_ascii=False,
            )

        print(f"💾 Product saved: {file_path}")

        return file_path

    def load(self, product_id: str) -> Product | None:
        """
        Load a product by product ID.
        """

        for file_path in self.storage_path.glob("*.json"):
            with file_path.open("r", encoding="utf-8") as file:
                product_data = json.load(file)

            if product_data.get("product_id") == product_id:
                return Product(**product_data)

        return None

    def list_products(self) -> list[Path]:
        """
        Return all stored product records.
        """

        return list(self.storage_path.glob("*.json"))

    def _build_file_name(self, product: Product) -> str:
        """
        Generate a safe product JSON filename.
        """

        safe_name = product.product_name.lower()

        safe_name = safe_name.replace(" ", "-")
        safe_name = safe_name.replace("/", "-")

        return f"{safe_name}.json"