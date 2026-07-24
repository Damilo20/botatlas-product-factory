"""
BotAtlas Truth Engine

Produces deterministic reconciliation results from evidence
comparisons.
"""

from scripts.models.claim_reconciliation import (
    ClaimReconciliation,
    ReconciliationState,
)
from scripts.models.evidence_comparison import (
    EvidenceComparison,
    EvidenceRelationship,
)


class TruthEngine:
    """
    Layer 12 Truth Engine.

    Responsibilities
    ----------------
    - Evaluate evidence comparisons.
    - Produce reconciliation states.
    - Preserve supporting evidence.

    Non-Responsibilities
    --------------------
    - AI reasoning
    - Source weighting
    - Claim extraction
    - Knowledge persistence
    """

    def reconcile(
        self,
        comparisons: list[EvidenceComparison],
    ) -> list[ClaimReconciliation]:

        reconciliations: list[
            ClaimReconciliation
        ] = []

        for comparison in comparisons:

            relationship = comparison.relationship

            if (
                relationship
                == EvidenceRelationship.AGREEMENT
            ):
                state = (
                    ReconciliationState.CONSISTENT
                )

                selected_value = (
                    comparison.distinct_values[0]
                    if comparison.distinct_values
                    else None
                )

            elif (
                relationship
                == EvidenceRelationship.PARTIAL_AGREEMENT
            ):
                state = (
                    ReconciliationState.DISPUTED
                )

                selected_value = (
                    comparison.distinct_values[0]
                    if comparison.distinct_values
                    else None
                )

            elif (
                relationship
                == EvidenceRelationship.CONFLICT
            ):
                state = (
                    ReconciliationState.DISPUTED
                )

                selected_value = None

            else:
                state = (
                    ReconciliationState.UNDERDETERMINED
                )

                selected_value = (
                    comparison.distinct_values[0]
                    if comparison.distinct_values
                    else None
                )

            reconciliations.append(
                ClaimReconciliation(
                    parent_candidate_name=(
                        comparison.parent_candidate_name
                    ),
                    parent_candidate_url=(
                        comparison.parent_candidate_url
                    ),
                    field_name=comparison.field_name,
                    relationship=relationship,
                    reconciliation_state=state,
                    selected_value=selected_value,
                    distinct_values=list(
                        comparison.distinct_values
                    ),
                    evidence=list(
                        comparison.evidence
                    ),
                    reconciliation_method=(
                        "EVIDENCE_RELATIONSHIP_POLICY"
                    ),
                )
            )

        return reconciliations