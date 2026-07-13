from dataclasses import dataclass


@dataclass(frozen=True)
class DiscoveredEvidenceSource:
    source_name: str
    source_url: str
    source_family: str
    parent_candidate_name: str
    parent_candidate_url: str
    search_query: str
    discovery_method: str = "EVIDENCE_SOURCE_DISCOVERY"
