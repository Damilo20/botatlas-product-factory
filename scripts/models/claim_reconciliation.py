"""
BotAtlas Claim Reconciliation

Canonical reconciliation contract.

Represents the deterministic outcome of evaluating compared
evidence for a single product field.

This model does not represent stored knowledge. It represents
the decision produced by the Truth Engine.
"""

from dataclasses import dataclass, field
from enum import Enum

from scripts.models.evidence_comparison import (
    EvidenceRelationship,
)
from scripts.models.weighted_evidence_assessment import (
    WeightedEvidenceAssessment,
)


class ReconciliationState(str, Enum):
    """Deterministic reconciliation outcome."""

    CONSISTENT = "CONSISTENT"

    DISPUTED = "DISPUTED"

    UNDERDETERMINED = "UNDERDETERMINED"


@dataclass(frozen=True)
class ClaimReconciliation:
    """
    Layer 12 reconciliation contract.

    Represents the deterministic reconciliation result for one
    candidate field.

    Truth has been evaluated, but no permanent knowledge has yet
    been stored.
    """

    parent_candidate_name: str

    parent_candidate_url: str

    field_name: str

    relationship: EvidenceRelationship

    reconciliation_state: ReconciliationState

    selected_value: str | None

    distinct_values: list[str] = field(
        default_factory=list
    )

    evidence: list[
        WeightedEvidenceAssessment
    ] = field(
        default_factory=list
    )

    reconciliation_method: str = (
        "EVIDENCE_RELATIONSHIP_POLICY"
    )