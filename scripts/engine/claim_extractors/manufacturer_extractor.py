import re

from scripts.engine.claim_extractors.base_claim_extractor import (
    BaseClaimExtractor,
)


class ManufacturerExtractor(BaseClaimExtractor):
    """
    Extract manufacturer claims.
    """

    FIELD_NAME = "manufacturer"

    PATTERN = re.compile(
        r"(?:manufacturer|made\s+by|built\s+by)"
        r"\s*[:\-]?\s*"
        r"([A-Z][A-Za-z0-9&.,' -]+)",
        re.IGNORECASE,
    )