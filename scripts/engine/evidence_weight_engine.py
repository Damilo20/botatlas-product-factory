"""
BotAtlas Evidence Weight Engine

Produces descriptive evidence characteristics for attributed
evidence claims.

Responsibilities
----------------
- Assess evidence characteristics.
- Preserve descriptive weighting signals.
- Describe evidence quality.

Non-Responsibilities
--------------------
- Numerical scoring
- Truth resolution
- Claim verification
- Knowledge persistence
"""

from datetime import datetime, timezone

from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)
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
    Layer 10 Evidence Weight Engine.

    Produces descriptive evidence characteristics from attributed
    evidence and source authority assessments.

    This engine intentionally avoids assigning a final numerical
    confidence score. It only describes evidence quality.
    """

    def assess(
        self,
        authority_assessment: SourceAuthorityAssessment,
    ) -> WeightedEvidenceAssessment:
        """
        Produce a descriptive evidence assessment for one claim.
        """

        claim: AttributedEvidenceClaim = (
            authority_assessment.claim
        )

        return WeightedEvidenceAssessment(

            authority_assessment=authority_assessment,

            directness_signal=self._directness(claim),

            provenance_signal=self._provenance(claim),

            specificity_signal=self._specificity(claim),

            freshness_signal=self._freshness(claim),

            # Populated later by comparison engines.
            corroboration_signal=CorroborationSignal.NONE,

            duplication_signal=DuplicationSignal.UNKNOWN,

            assessment_method=(
                "DESCRIPTIVE_EVIDENCE_CHARACTERISTICS"
            ),
        )

    def assess_all(
        self,
        assessments: list[SourceAuthorityAssessment],
    ) -> list[WeightedEvidenceAssessment]:
        """
        Assess an entire collection of authority assessments.
        """

        return [
            self.assess(assessment)
            for assessment in assessments
        ]

    @staticmethod
    def _directness(
        claim: AttributedEvidenceClaim,
    ) -> DirectnessSignal:
        """
        Evaluate how directly the claim originates from the source.
        """

        if (
            claim.attribution_method
            == "DIRECT_MATERIAL_PROVENANCE"
        ):
            return DirectnessSignal.DIRECT

        if claim.attribution_method:
            return DirectnessSignal.INDIRECT

        return DirectnessSignal.UNKNOWN

    @staticmethod
    def _provenance(
        claim: AttributedEvidenceClaim,
    ) -> ProvenanceSignal:
        """
        Evaluate provenance completeness.
        """

        required = (

            claim.source_name,

            claim.source_url,

            claim.source_family,

            claim.parent_candidate_name,

            claim.parent_candidate_url,

            claim.search_query,

        )

        present = sum(
            bool(value)
            for value in required
        )

        if present == len(required):
            return ProvenanceSignal.COMPLETE

        if present >= 3:
            return ProvenanceSignal.PARTIAL

        if present > 0:
            return ProvenanceSignal.LIMITED

        return ProvenanceSignal.UNKNOWN

    @staticmethod
    def _specificity(
        claim: AttributedEvidenceClaim,
    ) -> SpecificitySignal:
        """
        Evaluate how specifically the evidence refers to the
        product being analyzed.
        """

        candidate = (
            claim.parent_candidate_name or ""
        ).strip().lower()

        claim_text = (
            claim.claim_text or ""
        ).strip().lower()

        query = (
            claim.search_query or ""
        ).strip().lower()

        if candidate and (
            candidate in claim_text
            or candidate in query
        ):
            return SpecificitySignal.MODEL_SPECIFIC

        if claim.parent_candidate_name:
            return SpecificitySignal.PRODUCT_FAMILY

        if claim.claim_text:
            return SpecificitySignal.GENERAL

        return SpecificitySignal.UNKNOWN

    @staticmethod
    def _freshness(
        claim: AttributedEvidenceClaim,
    ) -> FreshnessSignal:
        """
        Evaluate evidence freshness.
        """

        acquired_at = claim.material_acquired_at

        if acquired_at is None:
            return FreshnessSignal.AGE_UNKNOWN

        if acquired_at.tzinfo is None:
            acquired_at = acquired_at.replace(
                tzinfo=timezone.utc
            )

        age = (
            datetime.now(timezone.utc)
            - acquired_at
        )

        if age.days <= 365:
            return FreshnessSignal.CURRENT

        return FreshnessSignal.DATED