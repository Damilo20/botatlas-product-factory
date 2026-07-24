"""
BotAtlas Evidence Comparison

Canonical evidence relationship model.

Describes the relationship among multiple pieces of weighted
evidence for the same candidate field.

Comparison identifies relationships but does not determine truth,
select a canonical value, or verify evidence.
"""

from dataclasses import dataclass, field
from enum import Enum

from scripts.models.weighted_evidence_assessment import (
    WeightedEvidenceAssessment,
)


class EvidenceRelationship(str, Enum):
    """Relationship among evidence describing the same field."""

    AGREEMENT = "AGREEMENT"

    PARTIAL_AGREEMENT = "PARTIAL_AGREEMENT"

    CONFLICT = "CONFLICT"

    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


@dataclass(frozen=True)
class EvidenceComparison:
    """
    Layer 11 evidence comparison contract.

    Represents the relationship among weighted evidence for a
    single product field.

    This model intentionally preserves every evidence assessment
    for downstream truth resolution.
    """

    parent_candidate_name: str

    parent_candidate_url: str

    field_name: str

    relationship: EvidenceRelationship

    distinct_values: list[str] = field(default_factory=list)

    evidence: list[
        WeightedEvidenceAssessment
    ] = field(default_factory=list)