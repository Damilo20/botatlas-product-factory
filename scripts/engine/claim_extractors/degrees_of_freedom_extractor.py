import re

from scripts.engine.claim_extractors.base_claim_extractor import (
    BaseClaimExtractor,
)


class DegreesOfFreedomExtractor(BaseClaimExtractor):

    FIELD_NAME = "degrees_of_freedom"

    PATTERN = re.compile(
        r"\b(\d+)\s*"
        r"(?:degrees?\s+of\s+freedom|dof)\b",
        re.IGNORECASE,
    )