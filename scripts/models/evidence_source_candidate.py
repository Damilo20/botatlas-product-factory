from dataclasses import dataclass
from typing import Optional


@dataclass
class EvidenceSourceCandidate:
    """
    Untrusted Layer 7 evidence-source candidate.

    A source candidate is not verified, authoritative,
    or true merely because it was discovered.
    """

    source_name: str
    source_url: str
    source_family: str = "UNKNOWN"
    discovery_method: str = "UNKNOWN"
    parent_candidate_name: Optional[str] = None
    parent_candidate_url: Optional[str] = None
    discovered_at: Optional[str] = None
    active: bool = True
