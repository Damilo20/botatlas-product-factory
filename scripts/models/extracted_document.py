from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ExtractedDocument:
    """
    Provider-neutral extracted document.

    Represents clean content extracted from raw evidence material.

    This object contains no truth assessment, trust assignment,
    claim extraction, or AI interpretation.
    """

    source_name: str
    source_url: str
    source_family: str

    parent_candidate_name: str
    parent_candidate_url: str

    search_query: str

    title: Optional[str]

    text: str

    language: Optional[str] = None

    extraction_method: str = "HTML"

    active: bool = True