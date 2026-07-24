import re

from scripts.engine.claim_extractors.base_claim_extractor import (
    BaseClaimExtractor,
)


class WeightExtractor(BaseClaimExtractor):

    FIELD_NAME = "weight"

    PATTERN = re.compile(
        r"\b(?:weighs?|weight(?:\s+is)?)\s+"
        r"(\d+(?:\.\d+)?)\s*"
        r"(kg|kilograms?|lbs?|pounds?)\b",
        re.IGNORECASE,
    )