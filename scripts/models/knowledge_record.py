from dataclasses import dataclass, field

from scripts.models.claim_reconciliation import (
    ClaimReconciliation,
)


@dataclass
class KnowledgeRecord:
    """
    Canonical knowledge stored by BotAtlas.
    """

    parent_candidate_name: str

    parent_candidate_url: str

    field_name: str

    selected_value: str

    confidence: float

    reconciliation: ClaimReconciliation

    version: int = 1

    active: bool = True

    metadata: dict = field(default_factory=dict)