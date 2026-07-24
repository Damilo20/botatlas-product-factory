import re

from scripts.engine.claim_extractors.base_claim_extractor import (
    BaseClaimExtractor,
)


class BatteryExtractor(BaseClaimExtractor):

    FIELD_NAME = "battery_capacity"

    PATTERN = re.compile(
        r"\b(?:battery(?:\s+capacity)?(?:\s+is)?|capacity)"
        r"\s*(\d+(?:\.\d+)?)\s*"
        r"(mah|wh|kwh)\b",
        re.IGNORECASE,
    )