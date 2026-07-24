from typing import Protocol

from scripts.models.discovered_evidence_source import (
    DiscoveredEvidenceSource,
)
from scripts.models.retrieved_evidence_material import (
    RetrievedEvidenceMaterial,
)


class EvidenceMaterialRetriever(Protocol):
    """
    Provider-neutral material retrieval boundary.
    """

    def retrieve(
        self,
        source: DiscoveredEvidenceSource,
    ) -> str:
        ...


class EvidenceMaterialAcquisition:
    """
    Layer 8 evidence material acquisition.

    Converts discovered Layer 7 evidence sources into retrieved
    evidence material while preserving source lineage.

    Does not extract claims, verify evidence, assign trust,
    score authority, or resolve truth.
    """

    def __init__(
        self,
        retriever: EvidenceMaterialRetriever,
    ):
        self.retriever = retriever

    def acquire(
        self,
        source: DiscoveredEvidenceSource,
    ) -> RetrievedEvidenceMaterial:
        content = self.retriever.retrieve(source)

        return RetrievedEvidenceMaterial(
            source_name=source.source_name,
            source_url=source.source_url,
            source_family=source.source_family,
            parent_candidate_name=source.parent_candidate_name,
            parent_candidate_url=source.parent_candidate_url,
            search_query=source.search_query,
            content=content,
            content_type="TEXT",
            acquisition_method="RETRIEVER",
        )

    def acquire_all(
        self,
        sources: list[DiscoveredEvidenceSource],
    ) -> list[RetrievedEvidenceMaterial]:
        return [
            self.acquire(source)
            for source in sources
        ]
