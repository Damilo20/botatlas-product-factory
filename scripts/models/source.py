from dataclasses import dataclass
from typing import Optional


@dataclass
class Source:
    """
    Represents a research source known to BotAtlas.

    A Source describes where intelligence originated and
    how much authority BotAtlas assigns to that origin.
    """

    source_name: str
    source_url: str

    source_id: Optional[str] = None
    domain: Optional[str] = None

    source_type: str = "UNKNOWN"
    ownership_type: str = "UNKNOWN"

    authority_score: float = 0.0
    reputation_score: float = 0.0

    discovered_at: Optional[str] = None
    last_checked: Optional[str] = None

    active: bool = True
