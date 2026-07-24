import re

from scripts.engine.claim_extractors.base_claim_extractor import (
    BaseClaimExtractor,
)


class ReleaseDateExtractor(BaseClaimExtractor):
    """
    Extract release date claims.
    """

    FIELD_NAME = "release_date"

    PATTERN = re.compile(
        r"\b(?:released?|launch(?:ed)?|available(?:\s+from)?)"
        r"\s*(?:on)?\s*"
        r"([A-Z][a-z]+(?:\s+\d{1,2},)?\s+\d{4}|\d{4})",
        re.IGNORECASE,
    )