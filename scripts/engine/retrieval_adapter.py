from abc import ABC, abstractmethod

from scripts.models.evidence_search_target import EvidenceSearchTarget
from scripts.models.retrieval_result import RetrievalResult


class RetrievalAdapter(ABC):
    """
    Provider-neutral Layer 7 retrieval boundary.

    Implementations retrieve raw results only.
    They must not verify evidence or assign trust.
    """

    @abstractmethod
    def retrieve(
        self,
        search_target: EvidenceSearchTarget
    ) -> list[RetrievalResult]:
        raise NotImplementedError
