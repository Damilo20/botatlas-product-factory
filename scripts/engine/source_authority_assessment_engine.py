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
    Layer 10 descriptive source authority assessment.

    Maps preserved source-family provenance into authority
    characteristics.

    Does not verify claims, rank truth, or select winners.
    """

    ASSESSMENT_BY_SOURCE_FAMILY = {
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
    }

    def assess(
        self,
        claim: AttributedEvidenceClaim,
    ) -> SourceAuthorityAssessment:
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
        return [
            self.assess(claim)
            for claim in claims
        ]
