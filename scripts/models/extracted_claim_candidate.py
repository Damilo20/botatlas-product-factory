from dataclasses import dataclass
from typing import Optional


@dataclass
class ExtractedClaimCandidate:
    """
    Untrusted claim candidate extracted from retrieved evidence material.

    Preserves exact extracted claim text and material provenance.

    Does not verify, select, score trust, or resolve truth.
    """

    field_name: str
    claimed_value: str
    claim_text: str

    source_name: str
    source_url: str
    source_family: str

    parent_candidate_name: str
    parent_candidate_url: str

    search_query: str

    extraction_method: str = "UNKNOWN"
    material_acquired_at: Optional[str] = None
    active: bool = True
