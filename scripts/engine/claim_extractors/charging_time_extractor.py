import re

from scripts.engine.claim_extractors.base_claim_extractor import (
    BaseClaimExtractor,
)


class ChargingTimeExtractor(BaseClaimExtractor):

    FIELD_NAME = "charging_time"

    PATTERN = re.compile(
        r"\b(?:charging\s*time|charge(?:s|d)?\s*in|full\s*charge\s*in)"
        r"\s*(?:of\s*)?"
        r"(\d+(?:\.\d+)?)\s*"
        r"(hours?|hrs?|minutes?|mins?)\b",
        re.IGNORECASE,
    )