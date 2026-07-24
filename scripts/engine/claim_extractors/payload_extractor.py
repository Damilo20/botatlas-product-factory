import re

from scripts.engine.claim_extractors.base_claim_extractor import (
    BaseClaimExtractor,
)


class PayloadExtractor(BaseClaimExtractor):
    """
    Extract payload claims.
    """

    FIELD_NAME = "payload"

    PATTERN = re.compile(
        r"\b(?:payload|maximum\s+payload|max\s+payload|carry(?:ing)?\s+capacity)"
        r"\s*(?:of|is)?\s*"
        r"(\d+(?:\.\d+)?)\s*"
        r"(kg|kilograms?|lbs?|pounds?)\b",
        re.IGNORECASE,
    )