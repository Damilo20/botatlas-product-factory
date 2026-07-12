from dataclasses import dataclass
from typing import Optional


@dataclass
class DiscoveryCandidate:
    """
    Represents a possible product discovered by BotAtlas.

    A DiscoveryCandidate is not a verified product.
    Discovery does not establish truth, identity, or authority.
    """

    candidate_name: str
    candidate_url: str

    discovery_method: str = "UNKNOWN"
    candidate_type: str = "UNKNOWN"

    discovered_at: Optional[str] = None

    active: bool = True
