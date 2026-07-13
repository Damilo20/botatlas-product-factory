from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional


@dataclass
class RetrievedEvidenceMaterial:
    """
    Raw evidence material acquired from a discovered evidence source.

    This record preserves material and source provenance only.

    It does not verify evidence, assign trust, resolve claims,
    or promote content into product truth.
    """

    source_name: str
    source_url: str
    source_family: str
    parent_candidate_name: str
    parent_candidate_url: str
    search_query: str
    content: str
    content_type: str = "TEXT"
    acquisition_method: str = "UNKNOWN"
    acquired_at: Optional[str] = None
    active: bool = True

    def __post_init__(self):
        if self.acquired_at is None:
            self.acquired_at = datetime.now(timezone.utc).isoformat()
