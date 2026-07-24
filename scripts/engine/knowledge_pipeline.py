"""
BotAtlas Knowledge Pipeline

Coordinates the complete end-to-end knowledge acquisition workflow.

Pipeline
--------
DiscoveredEvidenceSource
        ↓
EvidenceMaterialAcquisition
        ↓
RetrievedEvidenceMaterial
        ↓
HtmlExtractionEngine
        ↓
ExtractedDocument
        ↓
ClaimExtractionEngine
        ↓
ExtractedClaimCandidate
        ↓
EvidenceAttributionEngine
        ↓
AttributedEvidenceClaim
        ↓
ClaimGroupingEngine
        ↓
ClaimGroup
        ↓
TruthEngine
        ↓
ClaimReconciliation
"""

from scripts.engine.evidence_material_acquisition import (
    EvidenceMaterialAcquisition,
)
from scripts.engine.html_extraction_engine import (
    HtmlExtractionEngine,
)
from scripts.engine.claim_extraction_engine import (
    ClaimExtractionEngine,
)
from scripts.engine.evidence_attribution_engine import (
    EvidenceAttributionEngine,
)
from scripts.engine.claim_grouping_engine import (
    ClaimGroupingEngine,
)
from scripts.engine.truth_engine import (
    TruthEngine,
)

from scripts.models.discovered_evidence_source import (
    DiscoveredEvidenceSource,
)
from scripts.models.retrieved_evidence_material import (
    RetrievedEvidenceMaterial,
)
from scripts.models.extracted_document import (
    ExtractedDocument,
)
from scripts.models.extracted_claim_candidate import (
    ExtractedClaimCandidate,
)
from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)
from scripts.models.claim_group import (
    ClaimGroup,
)
from scripts.models.claim_reconciliation import (
    ClaimReconciliation,
)


class KnowledgePipeline:
    """
    Layer 8–10 orchestration pipeline.

    Responsibilities
    ----------------
    - Coordinate acquisition.
    - Coordinate extraction.
    - Coordinate attribution.
    - Coordinate grouping.
    - Coordinate reconciliation.

    Non-Responsibilities
    --------------------
    - HTTP retrieval
    - HTML parsing
    - Claim extraction
    - Evidence comparison
    - Truth reasoning
    - Knowledge persistence
    """

    def __init__(
        self,
        acquisition: EvidenceMaterialAcquisition,
        extraction: HtmlExtractionEngine,
        claim_extraction: ClaimExtractionEngine,
        attribution: EvidenceAttributionEngine,
        grouping: ClaimGroupingEngine,
        truth: TruthEngine,
    ):
        self.acquisition = acquisition
        self.extraction = extraction
        self.claim_extraction = claim_extraction
        self.attribution = attribution
        self.grouping = grouping
        self.truth = truth

    def process_source(
        self,
        source: DiscoveredEvidenceSource,
    ) -> dict[
        str,
        RetrievedEvidenceMaterial
        | ExtractedDocument
        | list[ExtractedClaimCandidate]
        | list[AttributedEvidenceClaim]
        | list[ClaimGroup]
        | list[ClaimReconciliation]
    ]:
        """
        Execute the complete knowledge pipeline for one evidence source.
        """

        # Layer 8 — Material Acquisition
        material = self.acquisition.acquire(source)

        # Layer 8 — HTML Extraction
        document = self.extraction.extract(material)

        # Layer 8 — Claim Extraction
        claims = self.claim_extraction.extract(document)

        # Layer 9 — Evidence Attribution
        attributed_claims = self.attribution.attribute(
            claims
        )

        # Layer 9 — Claim Grouping
        claim_groups = self.grouping.group(
            attributed_claims
        )

        # Layer 10 — Truth Reconciliation
        reconciliations = self.truth.reconcile(
            claim_groups
        )

        return {
            "material": material,
            "document": document,
            "claims": claims,
            "attributed_claims": attributed_claims,
            "claim_groups": claim_groups,
            "reconciliations": reconciliations,
        }

    def process_sources(
        self,
        sources: list[DiscoveredEvidenceSource],
    ) -> list[
        dict[
            str,
            RetrievedEvidenceMaterial
            | ExtractedDocument
            | list[ExtractedClaimCandidate]
            | list[AttributedEvidenceClaim]
            | list[ClaimGroup]
            | list[ClaimReconciliation]
        ]
    ]:
        """
        Execute the pipeline for multiple evidence sources.
        """

        return [
            self.process_source(source)
            for source in sources
        ]