from dataclasses import dataclass


@dataclass
class Product:

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

    msrp: float = 0.0

    current_price: float = 0.0

    affiliate_link: str = ""

    last_ai_analysis: str = ""

    ai_version: str = ""