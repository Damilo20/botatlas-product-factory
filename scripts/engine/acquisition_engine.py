from datetime import datetime, timezone

from scripts.models.discovery_candidate import DiscoveryCandidate
from scripts.models.acquired_material import AcquiredMaterial


class AcquisitionEngine:
    """
    BotAtlas Layer 6 acquisition boundary.

    Converts retrieved content associated with a discovery candidate
    into acquired material.

    Retrieval success does not establish truth, confidence,
    verification, source authority, reputation, or claim selection.
    """

    def acquire(
        self,
        candidate: DiscoveryCandidate,
        content: str,
        acquisition_method: str = "UNKNOWN",
        content_type: str = "UNKNOWN",
    ) -> AcquiredMaterial:
        return AcquiredMaterial(
            candidate_name=candidate.candidate_name,
            source_url=candidate.candidate_url,
            content=content,
            acquisition_method=acquisition_method,
            content_type=content_type,
            acquired_at=datetime.now(timezone.utc).isoformat(),
        )
