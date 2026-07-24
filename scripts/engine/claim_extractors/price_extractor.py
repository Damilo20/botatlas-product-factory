import re

from scripts.engine.claim_extractors.base_claim_extractor import (
    BaseClaimExtractor,
)


class PriceExtractor(BaseClaimExtractor):
    """
    Extract price claims.
    """

    FIELD_NAME = "price"

    PATTERN = re.compile(
        r"(?:\$|usd\s*)"
        r"(\d[\d,]*(?:\.\d{2})?)",
        re.IGNORECASE,
    )