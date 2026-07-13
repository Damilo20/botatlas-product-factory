from dataclasses import dataclass, field

from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)


@dataclass
class ClaimGroup:
    """
    Layer 9 grouped claim contract.

    Groups attributed evidence claims by parent candidate identity
    and field name.

    This contract preserves competing claims independently.
    It does not select a preferred value, resolve contradictions,
    verify claims, or assign truth.
    """

    parent_candidate_name: str
    parent_candidate_url: str
    field_name: str
    claims: list[AttributedEvidenceClaim] = field(
        default_factory=list
    )

    def __post_init__(self) -> None:
        for claim in self.claims:
            if claim.parent_candidate_name != self.parent_candidate_name:
                raise ValueError(
                    "ClaimGroup cannot contain claims from "
                    "different parent candidates"
                )

            if claim.parent_candidate_url != self.parent_candidate_url:
                raise ValueError(
                    "ClaimGroup cannot contain claims from "
                    "different parent candidate URLs"
                )

            if claim.field_name != self.field_name:
                raise ValueError(
                    "ClaimGroup cannot contain claims for "
                    "different fields"
                )
