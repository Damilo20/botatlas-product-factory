import re

from scripts.engine.claim_extractors.base_claim_extractor import (
    BaseClaimExtractor,
)


class DimensionsExtractor(BaseClaimExtractor):
    """
    Extract dimensions claims.
    """

    FIELD_NAME = "dimensions"

    PATTERN = re.compile(
        r"(\d+(?:\.\d+)?)\s*[x×]\s*"
        r"(\d+(?:\.\d+)?)\s*[x×]\s*"
        r"(\d+(?:\.\d+)?)\s*"
        r"(mm|cm|m|in|inch|inches|ft|feet)\b",
        re.IGNORECASE,
    )