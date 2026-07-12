from scripts.models.evidence import Evidence
from scripts.models.source import Source


class EvidenceWeightEngine:
    """
    Converts Layer 5 source authority into an evidence confidence signal.

    This engine does not resolve claims.
    It only weights evidence using source trust.
    """

    AUTHORITY_WEIGHT = 0.70
    REPUTATION_WEIGHT = 0.30

    def weight(
        self,
        evidence: Evidence,
        source: Source,
    ) -> Evidence:
        trust_score = (
            source.authority_score * self.AUTHORITY_WEIGHT
            + source.reputation_score * self.REPUTATION_WEIGHT
        )

        evidence.confidence_score = round(
            max(0.0, min(1.0, trust_score)),
            3,
        )

        return evidence
