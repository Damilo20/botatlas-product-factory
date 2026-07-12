from collections import defaultdict

from scripts.models.claim import Claim
from scripts.models.evidence import Evidence


class ClaimEngine:
    """
    Converts raw BotAtlas evidence into scored intelligence claims.

    Evidence is grouped by:
        field_name
        claimed_value

    Each unique field/value pair becomes a Claim.
    """

    def build_claims(self, evidence: list[Evidence]) -> list[Claim]:
        grouped_evidence = defaultdict(list)

        for item in evidence:
            key = (item.field_name, item.claimed_value)
            grouped_evidence[key].append(item)

        claims = []

        for (field_name, claimed_value), items in grouped_evidence.items():
            confidence_score = self._calculate_confidence(items)

            claim = Claim(
                field_name=field_name,
                claimed_value=claimed_value,
                confidence_score=confidence_score,
                evidence=items,
            )

            claims.append(claim)

        return claims

    def _calculate_confidence(self, evidence: list[Evidence]) -> float:
        if not evidence:
            return 0.0

        total_confidence = sum(
            item.confidence_score for item in evidence
        )

        return total_confidence / len(evidence)