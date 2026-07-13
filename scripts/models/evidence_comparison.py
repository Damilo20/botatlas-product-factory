from dataclasses import dataclass, field
from enum import Enum

from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)


class EvidenceRelationship(str, Enum):
    AGREEMENT = "AGREEMENT"
    CONFLICT = "CONFLICT"
    PARTIAL_AGREEMENT = "PARTIAL_AGREEMENT"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


@dataclass
class EvidenceComparison:
    """
    Layer 9 evidence comparison contract.

    Describes the relationship among grouped evidence claims.

    Comparison does not select a preferred value,
    resolve a claim, verify evidence, or assign truth.
    """

    parent_candidate_name: str
    parent_candidate_url: str
    field_name: str
    relationship: EvidenceRelationship
    distinct_values: list[str] = field(default_factory=list)
    claims: list[AttributedEvidenceClaim] = field(
        default_factory=list
    )
