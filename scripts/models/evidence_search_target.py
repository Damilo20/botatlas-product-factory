from dataclasses import dataclass


@dataclass(frozen=True)
class EvidenceSearchTarget:
    parent_candidate_name: str
    parent_candidate_url: str
    source_family: str
    search_query: str
    discovery_method: str = "SOURCE_QUERY_PLANNING"
