from scripts.models.product import Product

from scripts.config.schema_constants import *


class ProductMapper:

    @staticmethod
    def from_airtable(record):

        fields = record.get("fields", {})

        return Product(

            product_id=record.get("id", ""),

            product_name=fields.get(PRODUCT_NAME, ""),

            manufacturer=fields.get(MANUFACTURER, ""),

            brand=fields.get(BRAND, ""),

            model=fields.get(MODEL, ""),

            category=fields.get(CATEGORY, ""),

            primary_use=fields.get("Primary Use", ""),

            industry=fields.get("Industry", ""),

            environment=fields.get("Environment", ""),

            target_user=fields.get("Target User", ""),

            mobility=fields.get("Mobility", ""),

            autonomy_level=fields.get("Autonomy Level", ""),

            description=fields.get(DESCRIPTION, ""),

            msrp=fields.get(MSRP, 0),

            current_price=fields.get(CURRENT_PRICE, 0),

            affiliate_link=fields.get(AFFILIATE_LINKS, "")
        )

    @staticmethod
    def to_airtable(product: Product):

        return {

            PRODUCT_NAME: product.product_name,

            MANUFACTURER: product.manufacturer,

            BRAND: product.brand,

            MODEL: product.model,

            CATEGORY: product.category,

            "Primary Use": product.primary_use,

            "Industry": product.industry,

            "Environment": product.environment,

            "Target User": product.target_user,

            "Mobility": product.mobility,

            "Autonomy Level": product.autonomy_level,

            DESCRIPTION: product.description,

            MSRP: product.msrp,

            CURRENT_PRICE: product.current_price,

            AFFILIATE_LINKS: product.affiliate_link

        }