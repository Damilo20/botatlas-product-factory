from collections import defaultdict

from scripts.models.claim import Claim


class ClaimResolver:
    """
    Resolves competing claims and selects the strongest
    claim for each product field.
    """

    def resolve(self, claims: list[Claim]) -> list[Claim]:
        grouped_claims = defaultdict(list)

        for claim in claims:
            grouped_claims[claim.field_name].append(claim)

        selected_claims = []

        for field_claims in grouped_claims.values():
            winner = max(
                field_claims,
                key=lambda claim: claim.confidence_score,
            )

            for claim in field_claims:
                claim.selected = claim is winner

                if claim.selected:
                    claim.verification_status = "Verified"
                else:
                    claim.verification_status = "Rejected"

            selected_claims.append(winner)

        return selected_claims