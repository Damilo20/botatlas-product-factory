import re

from scripts.engine.claim_extractors.base_claim_extractor import (
    BaseClaimExtractor,
)


class SpeedExtractor(BaseClaimExtractor):
    """
    Extract speed claims.
    """

    FIELD_NAME = "speed"

    PATTERN = re.compile(
        r"\b(?:speed|top\s+speed|maximum\s+speed)"
        r"\s*(?:of|is)?\s*"
        r"(\d+(?:\.\d+)?)\s*"
        r"(km/h|kph|mph|m/s)\b",
        re.IGNORECASE,
    )