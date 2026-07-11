from dataclasses import dataclass
from typing import Optional


@dataclass
class Evidence:
    """
    Represents a single piece of evidence supporting
    a BotAtlas product intelligence claim.
    """

    field_name: str
    claimed_value: str

    source_name: str
    source_url: Optional[str] = None

    source_type: str = "UNKNOWN"

    confidence_score: float = 0.0

    verified: bool = False