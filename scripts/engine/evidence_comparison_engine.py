"""
BotAtlas Evidence Comparison Engine

Compares weighted evidence assessments describing the same
candidate field.

Responsibilities
----------------
- Compare evidence relationships.
- Identify agreement and conflict.
- Preserve all evidence.

Non-Responsibilities
--------------------
- Truth resolution
- Claim verification
- Knowledge persistence
- Canonical value selection
"""

from scripts.models.evidence_comparison import (
    EvidenceComparison,
    EvidenceRelationship,
)
from scripts.models.weighted_evidence_assessment import (
    WeightedEvidenceAssessment,
)


class EvidenceComparisonEngine:
    """
    Layer 11 Evidence Comparison Engine.

    Compares weighted evidence describing the same product field.

    This engine classifies evidence relationships without deciding
    which value is correct.
    """

    def compare(
        self,
        assessments: list[WeightedEvidenceAssessment],
    ) -> EvidenceComparison:
        """
        Compare one collection of weighted evidence assessments.
        """

        if not assessments:
            raise ValueError(
                "EvidenceComparisonEngine requires at least one assessment."
            )

        claims = [
            assessment.authority_assessment.claim
            for assessment in assessments
        ]

        distinct_values = list(
            dict.fromkeys(
                (
                    claim.claimed_value or ""
                ).strip()
                for claim in claims
            )
        )

        relationship = self._relationship(
            claims,
            distinct_values,
        )

        first = claims[0]

        return EvidenceComparison(
            parent_candidate_name=first.parent_candidate_name,
            parent_candidate_url=first.parent_candidate_url,
            field_name=first.field_name,
            relationship=relationship,
            distinct_values=distinct_values,
            evidence=list(assessments),
        )

    def compare_all(
        self,
        grouped_assessments: list[
            list[WeightedEvidenceAssessment]
        ],
    ) -> list[EvidenceComparison]:
        """
        Compare multiple groups of evidence.
        """

        return [
            self.compare(group)
            for group in grouped_assessments
        ]

    @staticmethod
    def _relationship(
        claims: list,
        distinct_values: list[str],
    ) -> EvidenceRelationship:
        """
        Classify the descriptive relationship among evidence.

        Future versions may normalize units, aliases,
        equivalent values, and ranges before determining
        PARTIAL_AGREEMENT.
        """

        if len(claims) < 2:
            return (
                EvidenceRelationship.INSUFFICIENT_EVIDENCE
            )

        if len(distinct_values) == 1:
            return (
                EvidenceRelationship.AGREEMENT
            )

        #
        # Reserved for semantic normalization in future versions.
        #
        # Examples:
        #
        #   1.50 kg == 1.5 kilograms
        #   $3,999 == 3999 USD
        #   8 hr == 8 hours
        #
        # If equivalent values are detected, return:
        #
        #   EvidenceRelationship.PARTIAL_AGREEMENT
        #

        return (
            EvidenceRelationship.CONFLICT
        )