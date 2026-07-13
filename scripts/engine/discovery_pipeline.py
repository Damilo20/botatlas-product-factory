from scripts.engine.acquisition_engine import AcquisitionEngine
from scripts.engine.candidate_deduplicator import CandidateDeduplicator
from scripts.engine.discovery_engine import DiscoveryEngine
from scripts.models.acquired_material import AcquiredMaterial
from scripts.models.discovery_candidate import DiscoveryCandidate


class DiscoveryPipeline:
    """
    BotAtlas Layer 6 discovery and acquisition orchestration boundary.

    Flow:
        DiscoveryEngine
            -> DiscoveryCandidate
            -> CandidateDeduplicator
            -> AcquisitionEngine
            -> AcquiredMaterial

    Layer 6 discovers, deduplicates, and acquires material.

    Layer 6 does not verify evidence, assign confidence, resolve claims,
    classify source authority, or apply truth.
    """

    def __init__(self):
        self.discovery = DiscoveryEngine()
        self.deduplicator = CandidateDeduplicator()
        self.acquisition = AcquisitionEngine()

    def process(
        self,
        candidates: list[DiscoveryCandidate],
        content_by_url: dict[str, str] | None = None,
    ) -> list[AcquiredMaterial]:
        content_by_url = content_by_url or {}

        unique_candidates = self.deduplicator.deduplicate(candidates)

        acquired_material = []

        for candidate in unique_candidates:
            content = content_by_url.get(candidate.candidate_url, "")

            material = self.acquisition.acquire(
                candidate=candidate,
                content=content,
                acquisition_method="PIPELINE",
                content_type="TEXT",
            )

            acquired_material.append(material)

        return acquired_material

    def discover_and_process(
        self,
        candidate_name: str,
        candidate_url: str,
        discovery_method: str = "PIPELINE",
        candidate_type: str = "UNKNOWN",
        content: str = "",
    ) -> list[AcquiredMaterial]:
        candidate = self.discovery.discover(
            candidate_name=candidate_name,
            candidate_url=candidate_url,
            discovery_method=discovery_method,
            candidate_type=candidate_type,
        )

        return self.process(
            candidates=[candidate],
            content_by_url={candidate.candidate_url: content},
        )
