from dataclasses import dataclass
from typing import Optional


@dataclass
class AcquiredMaterial:
    candidate_name: str
    source_url: str
    content: str

    acquisition_method: str = "UNKNOWN"
    content_type: str = "UNKNOWN"
    acquired_at: Optional[str] = None
    active: bool = True
