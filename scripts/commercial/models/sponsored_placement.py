from dataclasses import dataclass
from enum import Enum


class PlacementSurface(Enum):
    HOMEPAGE = "HOMEPAGE"
    CATEGORY = "CATEGORY"
    PRODUCT_PAGE = "PRODUCT_PAGE"
    SEARCH = "SEARCH"


@dataclass(frozen=True)
class SponsoredPlacement:
    product_name: str
    product_url: str
    sponsor_name: str
    placement_surface: PlacementSurface
    campaign_reference: str
    disclosure_text: str
    active: bool = True
