from dataclasses import dataclass
from typing import Optional


@dataclass
class AttributedEvidenceClaim:
    """
    Untrusted extracted claim with explicit evidence attribution.

    Records where the claim came from and how it was extracted.

    Does not verify, score trust, select, or resolve the claim.
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

    extraction_method: str
    attribution_method: str

    material_acquired_at: Optional[str] = None
    active: bool = True
