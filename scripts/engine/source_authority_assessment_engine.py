"""
BotAtlas Source Authority Assessment Engine

Maps preserved source provenance into descriptive authority
characteristics.

Responsibilities
----------------
- Assess source authority characteristics.
- Classify source relationships.
- Preserve provenance metadata.

Non-Responsibilities
--------------------
- Trust scoring
- Evidence weighting
- Truth resolution
- Claim verification
"""

from types import MappingProxyType

from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)
from scripts.models.source_authority_assessment import (
    AuthoritySignal,
    SourceAuthorityAssessment,
    SourceRelationship,
)


class SourceAuthorityAssessmentEngine:
    """
    Layer 10 Source Authority Assessment Engine.

    Produces descriptive authority assessments from preserved
    source provenance.

    This engine classifies the nature of a source without
    assigning trust scores or determining truth.
    """

    ASSESSMENT_BY_SOURCE_FAMILY = MappingProxyType({
        "OFFICIAL_MANUFACTURER": (
            AuthoritySignal.PRIMARY,
            SourceRelationship.MANUFACTURER,
        ),
        "OFFICIAL_DOCUMENTATION": (
            AuthoritySignal.DOCUMENTARY,
            SourceRelationship.OFFICIAL_DOCUMENTATION,
        ),
        "AUTHORIZED_RETAILER": (
            AuthoritySignal.AUTHORIZED_COMMERCIAL,
            SourceRelationship.AUTHORIZED_RETAILER,
        ),
        "TECHNICAL_SOURCE": (
            AuthoritySignal.SPECIALIZED_TECHNICAL,
            SourceRelationship.TECHNICAL_SPECIALIST,
        ),
        "INDEPENDENT_REPORTING": (
            AuthoritySignal.INDEPENDENT_EDITORIAL,
            SourceRelationship.INDEPENDENT_REPORTER,
        ),
        "USER_GENERATED": (
            AuthoritySignal.COMMUNITY,
            SourceRelationship.USER_COMMUNITY,
        ),
    })

    def assess(
        self,
        claim: AttributedEvidenceClaim,
    ) -> SourceAuthorityAssessment:
        """
        Produce a descriptive authority assessment for a single
        attributed evidence claim.
        """

        authority_signal, source_relationship = (
            self.ASSESSMENT_BY_SOURCE_FAMILY.get(
                claim.source_family,
                (
                    AuthoritySignal.UNKNOWN,
                    SourceRelationship.UNKNOWN,
                ),
            )
        )

        return SourceAuthorityAssessment(
            claim=claim,
            authority_signal=authority_signal,
            source_relationship=source_relationship,
            assessment_method="SOURCE_FAMILY_RELATIONSHIP",
        )

    def assess_all(
        self,
        claims: list[AttributedEvidenceClaim],
    ) -> list[SourceAuthorityAssessment]:
        """
        Assess authority for an entire collection of attributed
        evidence claims.
        """

        return [
            self.assess(claim)
            for claim in claims
        ]