from scripts.models.discovery_candidate import DiscoveryCandidate


class DiscoveryEngine:
    """
    BotAtlas Layer 6 discovery boundary.

    Generates discovery candidates from raw discovery inputs.

    A discovery candidate is not verified.
    Discovery success does not establish truth, confidence,
    source authority, reputation, or claim selection.
    """

    def discover(
        self,
        candidate_name: str,
        candidate_url: str,
        discovery_method: str = "UNKNOWN",
        candidate_type: str = "UNKNOWN",
    ) -> DiscoveryCandidate:
        return DiscoveryCandidate(
            candidate_name=candidate_name,
            candidate_url=candidate_url,
            discovery_method=discovery_method,
            candidate_type=candidate_type,
        )
