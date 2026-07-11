from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ResearchResult:
    """
    Structured identity research result.

    Represents product identity information discovered
    before it is merged into the BotAtlas Product model.
    """

    product_name: str

    manufacturer: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    category: Optional[str] = None

    official_url: Optional[str] = None

    confidence_score: float = 0.0

    sources: list = field(default_factory=list)
    warnings: list = field(default_factory=list)