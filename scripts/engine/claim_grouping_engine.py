from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)
from scripts.models.claim_group import ClaimGroup


class ClaimGroupingEngine:
    """
    Layer 9 claim grouping engine.

    Groups Layer 8 attributed claims by parent candidate identity
    and field name.

    Grouping preserves every original claim object.
    It does not merge values, resolve contradictions,
    select preferred claims, or assign truth.
    """

    def group(
        self,
        claims: list[AttributedEvidenceClaim],
    ) -> list[ClaimGroup]:
        grouped: dict[
            tuple[str, str, str],
            list[AttributedEvidenceClaim],
        ] = {}

        for claim in claims:
            key = (
                claim.parent_candidate_name,
                claim.parent_candidate_url,
                claim.field_name,
            )

            grouped.setdefault(key, []).append(claim)

        return [
            ClaimGroup(
                parent_candidate_name=parent_candidate_name,
                parent_candidate_url=parent_candidate_url,
                field_name=field_name,
                claims=group_claims,
            )
            for (
                parent_candidate_name,
                parent_candidate_url,
                field_name,
            ), group_claims in grouped.items()
        ]
