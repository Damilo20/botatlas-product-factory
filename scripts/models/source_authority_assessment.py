from dataclasses import dataclass
from enum import Enum

from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)


class AuthoritySignal(str, Enum):
    PRIMARY = "PRIMARY"
    DOCUMENTARY = "DOCUMENTARY"
    AUTHORIZED_COMMERCIAL = "AUTHORIZED_COMMERCIAL"
    SPECIALIZED_TECHNICAL = "SPECIALIZED_TECHNICAL"
    INDEPENDENT_EDITORIAL = "INDEPENDENT_EDITORIAL"
    UNKNOWN = "UNKNOWN"


class SourceRelationship(str, Enum):
    MANUFACTURER = "MANUFACTURER"
    OFFICIAL_DOCUMENTATION = "OFFICIAL_DOCUMENTATION"
    AUTHORIZED_RETAILER = "AUTHORIZED_RETAILER"
    TECHNICAL_SPECIALIST = "TECHNICAL_SPECIALIST"
    INDEPENDENT_REPORTER = "INDEPENDENT_REPORTER"
    UNKNOWN = "UNKNOWN"


@dataclass
class SourceAuthorityAssessment:
    claim: AttributedEvidenceClaim
    authority_signal: AuthoritySignal
    source_relationship: SourceRelationship
    assessment_method: str
