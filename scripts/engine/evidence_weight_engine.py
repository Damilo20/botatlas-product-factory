from datetime import datetime, timezone

from scripts.models.source_authority_assessment import (
    SourceAuthorityAssessment,
)
from scripts.models.weighted_evidence_assessment import (
    CorroborationSignal,
    DirectnessSignal,
    DuplicationSignal,
    FreshnessSignal,
    ProvenanceSignal,
    SpecificitySignal,
    WeightedEvidenceAssessment,
)


class EvidenceWeightEngine:
    """
    Layer 10 descriptive evidence characteristic assessment.

    Produces multidimensional evidence signals.

    Does not calculate a final evidence score, verify claims,
    select winners, or resolve disputes.
    """

    def assess(
        self,
        authority_assessment: SourceAuthorityAssessment,
    ) -> WeightedEvidenceAssessment:
        claim = authority_assessment.claim

        return WeightedEvidenceAssessment(
            authority_assessment=authority_assessment,
            directness_signal=self._directness(claim),
            provenance_signal=self._provenance(claim),
            specificity_signal=self._specificity(claim),
            freshness_signal=self._freshness(claim),
            corroboration_signal=CorroborationSignal.NONE,
            duplication_signal=DuplicationSignal.UNKNOWN,
            assessment_method="DESCRIPTIVE_EVIDENCE_CHARACTERISTICS",
        )

    def assess_all(
        self,
        assessments: list[SourceAuthorityAssessment],
    ) -> list[WeightedEvidenceAssessment]:
        return [
            self.assess(assessment)
            for assessment in assessments
        ]

    @staticmethod
    def _directness(claim) -> DirectnessSignal:
        if claim.attribution_method == "DIRECT_MATERIAL_PROVENANCE":
            return DirectnessSignal.DIRECT

        if claim.attribution_method:
            return DirectnessSignal.INDIRECT

        return DirectnessSignal.UNKNOWN

    @staticmethod
    def _provenance(claim) -> ProvenanceSignal:
        required = (
            claim.source_name,
            claim.source_url,
            claim.source_family,
            claim.parent_candidate_name,
            claim.parent_candidate_url,
            claim.search_query,
        )

        present = sum(bool(value) for value in required)

        if present == len(required):
            return ProvenanceSignal.COMPLETE

        if present >= 3:
            return ProvenanceSignal.PARTIAL

        if present > 0:
            return ProvenanceSignal.LIMITED

        return ProvenanceSignal.UNKNOWN

    @staticmethod
    def _specificity(claim) -> SpecificitySignal:
        candidate_name = (
            claim.parent_candidate_name or ""
        ).strip().lower()

        claim_text = (
            claim.claim_text or ""
        ).strip().lower()

        search_query = (
            claim.search_query or ""
        ).strip().lower()

        if candidate_name and (
            candidate_name in claim_text
            or candidate_name in search_query
        ):
            return SpecificitySignal.MODEL_SPECIFIC

        if claim.parent_candidate_name:
            return SpecificitySignal.PRODUCT_FAMILY

        if claim.claim_text:
            return SpecificitySignal.GENERAL

        return SpecificitySignal.UNKNOWN

    @staticmethod
    def _freshness(claim) -> FreshnessSignal:
        acquired_at = claim.material_acquired_at

        if acquired_at is None:
            return FreshnessSignal.AGE_UNKNOWN

        if acquired_at.tzinfo is None:
            acquired_at = acquired_at.replace(
                tzinfo=timezone.utc
            )

        age = datetime.now(timezone.utc) - acquired_at

        if age.days <= 365:
            return FreshnessSignal.CURRENT

        return FreshnessSignal.DATED
