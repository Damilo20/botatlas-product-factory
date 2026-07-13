from dataclasses import dataclass
from enum import Enum


class RouteType(Enum):
    DIRECT = "DIRECT"
    AFFILIATE = "AFFILIATE"
    SPONSORED = "SPONSORED"


@dataclass(frozen=True)
class CommercialRoute:
    product_name: str
    seller_name: str
    destination_url: str
    route_type: RouteType
    disclosure_required: bool
    disclosure_text: str | None = None
