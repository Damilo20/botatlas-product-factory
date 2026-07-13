from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)
from scripts.models.extracted_claim_candidate import (
    ExtractedClaimCandidate,
)


class ClaimAttributionEngine:
    """
    Layer 8 evidence claim attribution.

    Binds extracted claim candidates to their preserved evidence provenance.

    Does not verify, score trust, select, normalize truth,
    or resolve contradictions.
    """

    def attribute(
        self,
        claim: ExtractedClaimCandidate,
    ) -> AttributedEvidenceClaim:
        return AttributedEvidenceClaim(
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
            attribution_method="DIRECT_MATERIAL_PROVENANCE",
            material_acquired_at=claim.material_acquired_at,
            active=claim.active,
        )

    def attribute_all(
        self,
        claims: list[ExtractedClaimCandidate],
    ) -> list[AttributedEvidenceClaim]:
        return [
            self.attribute(claim)
            for claim in claims
        ]
