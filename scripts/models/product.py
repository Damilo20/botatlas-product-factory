from dataclasses import dataclass, field
from typing import Optional

from scripts.models.evidence import Evidence
from scripts.models.claim import Claim

@dataclass
class Product:
    """Master product object used across BotAtlas."""

    # -------------------------
    # Identity
    # -------------------------

    product_id: str
    product_name: str

    manufacturer: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    category: Optional[str] = None

    # -------------------------
    # Technical
    # -------------------------

    weight: Optional[str] = None
    runtime: Optional[str] = None
    battery: Optional[str] = None
    connectivity: Optional[str] = None

    # -------------------------
    # Content
    # -------------------------

    description: Optional[str] = None
    ai_summary: Optional[str] = None

    # -------------------------
    # Pricing
    # -------------------------

    msrp: Optional[float] = None
    current_price: Optional[float] = None
    currency: str = "USD"

    official_store: Optional[str] = None
    amazon_url: Optional[str] = None
    affiliate_url: Optional[str] = None

    # -------------------------
    # Trust
    # -------------------------

    official_url: Optional[str] = None

    quality_score: float = 0.0

    # -------------------------
    # # Intelligence
    # -------------------------

    confidence_score: float = 0.0
    verification_status: str = "Pending"

    sources: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    notes: list = field(default_factory=list)

    evidence: list[Evidence] = field(default_factory=list)
    claims: list[Claim] = field(default_factory=list)

    def __str__(self):

        return f"""

==================================================
BOTATLAS PRODUCT REPORT
==================================================

Name:             {self.product_name}
Product ID:       {self.product_id}

Manufacturer:     {self.manufacturer}
Brand:            {self.brand}
Model:            {self.model}
Category:         {self.category}

Weight:           {self.weight}
Runtime:          {self.runtime}
Battery:          {self.battery}
Connectivity:     {self.connectivity}

MSRP:             {self.msrp}
Current Price:    {self.current_price}
Currency:         {self.currency}

Official Store:   {self.official_store}
Amazon:           {self.amazon_url}
Affiliate Link:   {self.affiliate_url}

Official Source:  {self.official_url}

Quality Score:         {self.quality_score}%
Confidence Score:      {self.confidence_score}%
Verification Status:   {self.verification_status}

Sources:                {self.sources}
Warnings:               {self.warnings}
Notes:                  {self.notes}

==================================================
"""