"""
BotAtlas Product Intelligence Report

Canonical output produced by the Product Factory.

Represents everything BotAtlas discovered, extracted,
evaluated, reconciled, and learned about one product during
a single pipeline execution.
"""

from dataclasses import dataclass, field
from datetime import datetime

from scripts.models.acquired_material import (
    RetrievedEvidenceMaterial,
)
from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)
from scripts.models.claim_reconciliation import (
    ClaimReconciliation,
)
from scripts.models.discovery_candidate import (
    DiscoveryCandidate,
)
from scripts.models.discovered_evidence_source import (
    DiscoveredEvidenceSource,
)
from scripts.models.extracted_claim_candidate import (
    ExtractedClaimCandidate,
)
from scripts.models.extracted_document import (
    ExtractedDocument,
)
from scripts.models.knowledge_record import (
    KnowledgeRecord,
)
from scripts.models.source_authority_assessment import (
    SourceAuthorityAssessment,
)
from scripts.models.weighted_evidence_assessment import (
    WeightedEvidenceAssessment,
)
from scripts.models.evidence_comparison import (
    EvidenceComparison,
)


@dataclass(frozen=True)
class ProductIntelligenceReport:
    """
    Canonical Product Intelligence Report.

    This object represents the complete output of one
    Product Factory execution.

    Every stage of the intelligence pipeline contributes to
    this report.

    Nothing inside this object should ever require
    recomputation.
    """

    #
    # Product
    #

    product: DiscoveryCandidate

    #
    # Discovery
    #

    sources: list[
        DiscoveredEvidenceSource
    ] = field(default_factory=list)

    #
    # Retrieval
    #

    retrieved_material: list[
        RetrievedEvidenceMaterial
    ] = field(default_factory=list)

    #
    # Extraction
    #

    documents: list[
        ExtractedDocument
    ] = field(default_factory=list)

    claims: list[
        ExtractedClaimCandidate
    ] = field(default_factory=list)

    attributed_claims: list[
        AttributedEvidenceClaim
    ] = field(default_factory=list)

    #
    # Intelligence
    #

    authority_assessments: list[
        SourceAuthorityAssessment
    ] = field(default_factory=list)

    weighted_evidence: list[
        WeightedEvidenceAssessment
    ] = field(default_factory=list)

    comparisons: list[
        EvidenceComparison
    ] = field(default_factory=list)

    reconciliations: list[
        ClaimReconciliation
    ] = field(default_factory=list)

    #
    # Knowledge
    #

    knowledge_records: list[KnowledgeRecord] = field(
        default_factory=list,
        init=False,
)

    #
    # Execution Metadata
    #

    pipeline_version: str = "2.0"

    started_at: datetime | None = None

    completed_at: datetime | None = None

    processing_duration_seconds: float | None = None