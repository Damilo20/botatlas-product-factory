from scripts.engine.claim_grouping_engine import ClaimGroupingEngine
from scripts.engine.evidence_comparison_engine import (
    EvidenceComparisonEngine,
)
from scripts.engine.claim_reconciliation_engine import (
    ClaimReconciliationEngine,
)
from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)
from scripts.models.claim_reconciliation import ClaimReconciliation


class ClaimResolutionPipeline:
    """
    BotAtlas Layer 9 claim resolution orchestration.

    Groups attributed claims, classifies evidence relationships,
    and maps those relationships into unresolved reconciliation states.

    Does not verify claims, select winners, assign trust,
    score authority, or declare truth.
    """

    def __init__(self) -> None:
        self.grouping = ClaimGroupingEngine()
        self.comparison = EvidenceComparisonEngine()
        self.reconciliation = ClaimReconciliationEngine()

    def run(
        self,
        claims: list[AttributedEvidenceClaim],
    ) -> list[ClaimReconciliation]:
        groups = self.grouping.group(claims)
        comparisons = self.comparison.compare_all(groups)

        return self.reconciliation.reconcile_all(comparisons)
