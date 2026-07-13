from scripts.engine.evidence_expansion_engine import EvidenceExpansionEngine
from scripts.engine.evidence_query_planner import EvidenceQueryPlanner
from scripts.engine.evidence_source_discovery import EvidenceSourceDiscovery
from scripts.engine.retrieval_adapter import RetrievalAdapter
from scripts.models.discovered_evidence_source import DiscoveredEvidenceSource
from scripts.models.retrieval_result import RetrievalResult


class EvidenceExpansionPipeline:
    """
    Layer 7 evidence expansion orchestration.

    Expansion -> query planning -> retrieval -> source discovery.

    Layer 7 discovers evidence source candidates only.
    It does not verify evidence, assign trust, or resolve claims.
    """

    def __init__(
        self,
        retrieval_adapter: RetrievalAdapter | None = None,
    ):
        self.expansion = EvidenceExpansionEngine()
        self.planner = EvidenceQueryPlanner()
        self.discovery = EvidenceSourceDiscovery()
        self.retrieval_adapter = retrieval_adapter

    def run(
        self,
        candidate_name: str,
        candidate_url: str,
        manufacturer_hint: str | None = None,
        model_hint: str | None = None,
    ) -> list[DiscoveredEvidenceSource]:
        source_candidates = self.expansion.expand(
            candidate_name=candidate_name,
            candidate_url=candidate_url,
            manufacturer_hint=manufacturer_hint,
            model_hint=model_hint,
        )

        search_targets = self.planner.plan(
            source_candidates=source_candidates,
        )

        if self.retrieval_adapter is None:
            return []

        discovered_sources: list[DiscoveredEvidenceSource] = []

        for target in search_targets:
            retrieval_results = self.retrieval_adapter.retrieve(target)

            raw_results = [
                self._to_raw_result(result)
                for result in retrieval_results
            ]

            discovered_sources.extend(
                self.discovery.discover(
                    target=target,
                    retrieval_results=raw_results,
                )
            )

        return self._deduplicate(discovered_sources)

    @staticmethod
    def _to_raw_result(
        result: RetrievalResult,
    ) -> dict:
        return {
            "name": result.title,
            "url": result.url,
            "snippet": result.snippet,
            "provider": result.provider,
        }

    @staticmethod
    def _deduplicate(
        sources: list[DiscoveredEvidenceSource],
    ) -> list[DiscoveredEvidenceSource]:
        unique: dict[str, DiscoveredEvidenceSource] = {}

        for source in sources:
            key = source.source_url.rstrip("/").lower()

            if key not in unique:
                unique[key] = source

        return list(unique.values())
