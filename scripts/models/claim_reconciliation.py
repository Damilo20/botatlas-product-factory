from dataclasses import dataclass, field
from enum import Enum

from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)
from scripts.models.evidence_comparison import EvidenceRelationship


class ReconciliationState(Enum):
    CONSISTENT = "CONSISTENT"
    DISPUTED = "DISPUTED"
    UNDERDETERMINED = "UNDERDETERMINED"


@dataclass
class ClaimReconciliation:
    """
    Layer 9 reconciliation state.

    Represents the unresolved state of compared evidence.

    Does not select a winner, assign trust, verify a claim,
    or declare a value true.
    """

    parent_candidate_name: str
    parent_candidate_url: str
    field_name: str
    relationship: EvidenceRelationship
    reconciliation_state: ReconciliationState
    distinct_values: list[str] = field(default_factory=list)
    claims: list[AttributedEvidenceClaim] = field(
        default_factory=list
    )
