from scripts.engine.retrieval_adapter import RetrievalAdapter
from scripts.models.evidence_search_target import EvidenceSearchTarget
from scripts.models.retrieval_result import RetrievalResult


class StaticRetrievalAdapter(RetrievalAdapter):
    """
    Deterministic retrieval adapter for architecture tests.

    Raw retrieval data is externally supplied.
    """

    def __init__(
        self,
        results_by_query: dict[str, list[RetrievalResult]] | None = None,
    ):
        self.results_by_query = results_by_query or {}

    def retrieve(
        self,
        target: EvidenceSearchTarget,
    ) -> list[RetrievalResult]:
        return list(
            self.results_by_query.get(
                target.search_query,
                [],
            )
        )
