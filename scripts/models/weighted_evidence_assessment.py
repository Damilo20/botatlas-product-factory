from dataclasses import dataclass
from enum import Enum

from scripts.models.source_authority_assessment import (
    SourceAuthorityAssessment,
)


class DirectnessSignal(str, Enum):
    DIRECT = "DIRECT"
    INDIRECT = "INDIRECT"
    UNKNOWN = "UNKNOWN"


class ProvenanceSignal(str, Enum):
    COMPLETE = "COMPLETE"
    PARTIAL = "PARTIAL"
    LIMITED = "LIMITED"
    UNKNOWN = "UNKNOWN"


class SpecificitySignal(str, Enum):
    MODEL_SPECIFIC = "MODEL_SPECIFIC"
    PRODUCT_FAMILY = "PRODUCT_FAMILY"
    GENERAL = "GENERAL"
    UNKNOWN = "UNKNOWN"


class FreshnessSignal(str, Enum):
    CURRENT = "CURRENT"
    DATED = "DATED"
    AGE_UNKNOWN = "AGE_UNKNOWN"


class CorroborationSignal(str, Enum):
    INDEPENDENT = "INDEPENDENT"
    RELATED = "RELATED"
    NONE = "NONE"
    UNKNOWN = "UNKNOWN"


class DuplicationSignal(str, Enum):
    DISTINCT = "DISTINCT"
    POSSIBLE_COPY = "POSSIBLE_COPY"
    SHARED_LINEAGE = "SHARED_LINEAGE"
    UNKNOWN = "UNKNOWN"


@dataclass
class WeightedEvidenceAssessment:
    authority_assessment: SourceAuthorityAssessment
    directness_signal: DirectnessSignal
    provenance_signal: ProvenanceSignal
    specificity_signal: SpecificitySignal
    freshness_signal: FreshnessSignal
    corroboration_signal: CorroborationSignal
    duplication_signal: DuplicationSignal
    assessment_method: str
