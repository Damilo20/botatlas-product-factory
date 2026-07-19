from dataclasses import asdict, dataclass

from scripts.config.schema_constants import (
    PRODUCT_NAME,
    MANUFACTURER,
    BRAND,
    MODEL,
    CATEGORY,
    PRIMARY_USE,
    INDUSTRY,
    ENVIRONMENT,
    TARGET_USER,
    MOBILITY,
    AUTONOMY_LEVEL,
    DESCRIPTION,
    AI_SUMMARY,
    MSRP,
    CURRENT_PRICE,
    AFFILIATE_LINK,
    AI_VERSION,
    LAST_AI_ANALYSIS,
)


@dataclass
class Product:
    """
    Canonical BotAtlas Product Model.

    Represents a verified product after passing through the
    Product Intelligence Pipeline.
    """

    product_id: str = ""

    product_name: str = ""

    manufacturer: str = ""

    brand: str = ""

    model: str = ""

    category: str = ""

    primary_use: str = ""

    industry: str = ""

    environment: str = ""

    target_user: str = ""

    mobility: str = ""

    autonomy_level: str = ""

    status: str = ""

    description: str = ""

    ai_summary: str = ""

    msrp: float = 0.0

    current_price: float = 0.0

    affiliate_link: str = ""

    last_ai_analysis: str = ""

    ai_version: str = ""

    def to_airtable(self) -> dict:
        """
        Convert the Product into an Airtable-compatible dictionary.
        """

        return {
            PRODUCT_NAME: self.product_name,
            MANUFACTURER: self.manufacturer,
            BRAND: self.brand,
            MODEL: self.model,
            CATEGORY: self.category,
            PRIMARY_USE: self.primary_use,
            INDUSTRY: self.industry,
            ENVIRONMENT: self.environment,
            TARGET_USER: self.target_user,
            MOBILITY: self.mobility,
            AUTONOMY_LEVEL: self.autonomy_level,
            DESCRIPTION: self.description,
            AI_SUMMARY: self.ai_summary,
            MSRP: self.msrp,
            CURRENT_PRICE: self.current_price,
            AFFILIATE_LINK: self.affiliate_link,
            AI_VERSION: self.ai_version,
            LAST_AI_ANALYSIS: self.last_ai_analysis,
        }

    def to_dict(self) -> dict:
        """
        Convert the Product into a standard Python dictionary.
        """

        return asdict(self)