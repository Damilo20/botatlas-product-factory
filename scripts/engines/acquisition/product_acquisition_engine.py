"""
BotAtlas Product Acquisition Engine

Responsible for acquiring products from external sources
and converting them into Product models.

Future Sources:
- Manufacturer websites
- Product pages
- RSS feeds
- APIs
- AI Research Agents
"""

from scripts.models.product import Product


class ProductAcquisitionEngine:

    def acquire_from_manual(self, product_data):

        """
        Creates a Product model from manually supplied data.
        (Temporary until web acquisition is implemented.)
        """

        return Product(

            product_name=product_data.get("product_name", ""),

            manufacturer=product_data.get("manufacturer", ""),

            brand=product_data.get("brand", ""),

            model=product_data.get("model", ""),

            category=product_data.get("category", ""),

            primary_use=product_data.get("primary_use", ""),

            industry=product_data.get("industry", ""),

            environment=product_data.get("environment", ""),

            target_user=product_data.get("target_user", ""),

            mobility=product_data.get("mobility", ""),

            autonomy_level=product_data.get("autonomy_level", ""),

            description=product_data.get("description", ""),

            msrp=product_data.get("msrp", 0),

            current_price=product_data.get("current_price", 0),

            affiliate_link=product_data.get("affiliate_link", "")
        )