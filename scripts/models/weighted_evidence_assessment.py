"""
BotAtlas Weighted Evidence Assessment

Canonical descriptive evidence assessment model.

Represents evidence quality characteristics without assigning
numerical confidence or determining truth.
"""

from dataclasses import dataclass
from enum import Enum

from scripts.models.source_authority_assessment import (
    SourceAuthorityAssessment,
)


class DirectnessSignal(str, Enum):
    """Describes how directly evidence originates from the source."""

    DIRECT = "DIRECT"
    INDIRECT = "INDIRECT"
    UNKNOWN = "UNKNOWN"


class ProvenanceSignal(str, Enum):
    """Describes provenance completeness."""

    COMPLETE = "COMPLETE"
    PARTIAL = "PARTIAL"
    LIMITED = "LIMITED"
    UNKNOWN = "UNKNOWN"


class SpecificitySignal(str, Enum):
    """Describes how specifically evidence identifies the product."""

    MODEL_SPECIFIC = "MODEL_SPECIFIC"
    PRODUCT_FAMILY = "PRODUCT_FAMILY"
    GENERAL = "GENERAL"
    UNKNOWN = "UNKNOWN"


class FreshnessSignal(str, Enum):
    """Describes evidence freshness."""

    CURRENT = "CURRENT"
    DATED = "DATED"
    AGE_UNKNOWN = "AGE_UNKNOWN"


class CorroborationSignal(str, Enum):
    """
    Describes whether evidence is independently supported
    by other sources.
    """

    INDEPENDENT = "INDEPENDENT"
    RELATED = "RELATED"
    NONE = "NONE"
    UNKNOWN = "UNKNOWN"


class DuplicationSignal(str, Enum):
    """
    Describes whether evidence appears to originate from the
    same underlying source.
    """

    DISTINCT = "DISTINCT"
    POSSIBLE_COPY = "POSSIBLE_COPY"
    SHARED_LINEAGE = "SHARED_LINEAGE"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class WeightedEvidenceAssessment:
    """
    Layer 10 descriptive evidence assessment.

    Aggregates evidence quality characteristics for an attributed
    evidence claim without assigning a confidence score or
    determining truth.
    """

    authority_assessment: SourceAuthorityAssessment

    directness_signal: DirectnessSignal

    provenance_signal: ProvenanceSignal

    specificity_signal: SpecificitySignal

    freshness_signal: FreshnessSignal

    corroboration_signal: CorroborationSignal

    duplication_signal: DuplicationSignal

    assessment_method: str