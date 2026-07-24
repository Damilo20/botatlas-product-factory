from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)
from scripts.models.extracted_claim_candidate import (
    ExtractedClaimCandidate,
)


class EvidenceAttributionEngine:
    """
    Layer 9 Evidence Attribution Engine.

    Converts extracted claim candidates into attributed evidence claims
    while preserving complete source provenance.

    Responsibilities
    ----------------
    - Preserve evidence lineage.
    - Preserve extraction metadata.
    - Create attributed evidence claims.

    Non-Responsibilities
    --------------------
    - Trust scoring
    - Claim comparison
    - Truth resolution
    """

    def attribute(
        self,
        claims: list[ExtractedClaimCandidate],
    ) -> list[AttributedEvidenceClaim]:

        attributed: list[AttributedEvidenceClaim] = []

        for claim in claims:

            attributed.append(
                AttributedEvidenceClaim(
                    field_name=claim.field_name,
                    claimed_value=claim.claimed_value,
                    claim_text=claim.claim_text,
                    source_name=claim.source_name,
                    source_url=claim.source_url,
                    source_family=claim.source_family,
                    parent_candidate_name=claim.parent_candidate_name,
                    parent_candidate_url=claim.parent_candidate_url,
                    search_query=claim.search_query,
                    extraction_method=claim.extraction_method,
                    attribution_method="DIRECT",
                    material_acquired_at=claim.material_acquired_at,
                    document_title=claim.document_title,
                    document_section=claim.document_section,
                    sentence_index=claim.sentence_index,
                )
            )

        return attributed