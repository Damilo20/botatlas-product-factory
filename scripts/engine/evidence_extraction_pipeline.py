from scripts.engine.claim_attribution_engine import ClaimAttributionEngine
from scripts.engine.claim_extraction_engine import ClaimExtractionEngine
from scripts.engine.evidence_material_acquisition import (
    EvidenceMaterialAcquisition,
    MaterialRetriever,
)
from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)
from scripts.models.discovered_evidence_source import (
    DiscoveredEvidenceSource,
)


class EvidenceExtractionPipeline:
    """
    BotAtlas Layer 8 evidence extraction and attribution orchestration.

    Source discovery output -> material acquisition -> claim extraction
    -> evidence attribution.

    Does not verify, score trust, select claims, or resolve truth.
    """

    def __init__(
        self,
        retriever: MaterialRetriever,
    ):
        self.acquisition = EvidenceMaterialAcquisition(
            retriever=retriever,
        )
        self.extraction = ClaimExtractionEngine()
        self.attribution = ClaimAttributionEngine()

    def run(
        self,
        sources: list[DiscoveredEvidenceSource],
    ) -> list[AttributedEvidenceClaim]:
        attributed_claims: list[AttributedEvidenceClaim] = []

        materials = self.acquisition.acquire_all(sources)

        for material in materials:
            extracted_claims = self.extraction.extract(material)

            attributed_claims.extend(
                self.attribution.attribute_all(
                    extracted_claims
                )
            )

        return attributed_claims
