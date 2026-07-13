from scripts.models.claim_group import ClaimGroup
from scripts.models.evidence_comparison import (
    EvidenceComparison,
    EvidenceRelationship,
)


class EvidenceComparisonEngine:
    """
    Layer 9 evidence relationship classification.

    Classifies grouped claims by exact distinct claimed values.

    Does not select a preferred value, verify evidence,
    score authority, assign trust, or resolve claims.
    """

    def compare(
        self,
        group: ClaimGroup,
    ) -> EvidenceComparison:
        distinct_values = list(
            dict.fromkeys(
                claim.claimed_value
                for claim in group.claims
            )
        )

        if len(group.claims) < 2:
            relationship = (
                EvidenceRelationship.INSUFFICIENT_EVIDENCE
            )
        elif len(distinct_values) == 1:
            relationship = EvidenceRelationship.AGREEMENT
        else:
            relationship = EvidenceRelationship.CONFLICT

        return EvidenceComparison(
            parent_candidate_name=group.parent_candidate_name,
            parent_candidate_url=group.parent_candidate_url,
            field_name=group.field_name,
            relationship=relationship,
            distinct_values=distinct_values,
            claims=list(group.claims),
        )

    def compare_all(
        self,
        groups: list[ClaimGroup],
    ) -> list[EvidenceComparison]:
        return [
            self.compare(group)
            for group in groups
        ]
