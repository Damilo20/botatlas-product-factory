from scripts.models.source import Source


class SourceAuthorityEngine:
    """
    Assigns deterministic authority and reputation scores
    to classified BotAtlas sources.

    Layer 5 does not inspect claims or resolve evidence.
    It scores the authority of the source itself.
    """

    AUTHORITY_POLICY = {
        ("MANUFACTURER", "FIRST_PARTY"): 0.95,
        ("MARKETPLACE", "THIRD_PARTY"): 0.70,
        ("UNKNOWN", "THIRD_PARTY"): 0.30,
    }

    REPUTATION_POLICY = {
        "MANUFACTURER": 0.90,
        "MARKETPLACE": 0.65,
        "UNKNOWN": 0.25,
    }

    def score(self, source: Source) -> Source:
        authority_key = (
            source.source_type,
            source.ownership_type,
        )

        source.authority_score = self.AUTHORITY_POLICY.get(
            authority_key,
            0.20,
        )

        source.reputation_score = self.REPUTATION_POLICY.get(
            source.source_type,
            0.20,
        )

        return source
