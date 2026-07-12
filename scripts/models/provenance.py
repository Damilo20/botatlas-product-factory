from dataclasses import dataclass
from typing import Optional


@dataclass
class Provenance:
    """
    Represents the origin and observation history of intelligence.

    Provenance does not decide whether a claim is true.
    It records how intelligence entered BotAtlas.
    """

    source_id: str
    source_url: str

    discovery_method: str = "UNKNOWN"
    observed_at: Optional[str] = None

    content_type: str = "UNKNOWN"
    content_reference: Optional[str] = None

    active: bool = True
