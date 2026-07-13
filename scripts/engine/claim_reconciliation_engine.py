from scripts.models.claim_reconciliation import (
    ClaimReconciliation,
    ReconciliationState,
)
from scripts.models.evidence_comparison import (
    EvidenceComparison,
    EvidenceRelationship,
)


class ClaimReconciliationEngine:
    """
    Layer 9 claim reconciliation.

    Maps explicit evidence relationships into unresolved
    reconciliation states.

    Does not select a winner, verify claims, assign trust,
    score evidence, or declare truth.
    """

    STATE_BY_RELATIONSHIP = {
        EvidenceRelationship.AGREEMENT:
            ReconciliationState.CONSISTENT,
        EvidenceRelationship.CONFLICT:
            ReconciliationState.DISPUTED,
        EvidenceRelationship.INSUFFICIENT_EVIDENCE:
            ReconciliationState.UNDERDETERMINED,
        EvidenceRelationship.PARTIAL_AGREEMENT:
            ReconciliationState.DISPUTED,
    }

    def reconcile(
        self,
        comparison: EvidenceComparison,
    ) -> ClaimReconciliation:
        reconciliation_state = self.STATE_BY_RELATIONSHIP[
            comparison.relationship
        ]

        return ClaimReconciliation(
            parent_candidate_name=comparison.parent_candidate_name,
            parent_candidate_url=comparison.parent_candidate_url,
            field_name=comparison.field_name,
            relationship=comparison.relationship,
            reconciliation_state=reconciliation_state,
            distinct_values=list(comparison.distinct_values),
            claims=list(comparison.claims),
        )

    def reconcile_all(
        self,
        comparisons: list[EvidenceComparison],
    ) -> list[ClaimReconciliation]:
        return [
            self.reconcile(comparison)
            for comparison in comparisons
        ]
