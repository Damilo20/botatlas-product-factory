import re

from scripts.engine.claim_extractors.base_claim_extractor import (
    BaseClaimExtractor,
)


class RuntimeExtractor(BaseClaimExtractor):

    FIELD_NAME = "runtime"

    PATTERN = re.compile(
        r"\b(?:operate|operates|run|runs|runtime)"
        r"(?:\s+for)?\s+(?:up\s+to\s+)?"
        r"(\d+(?:\.\d+)?)\s*"
        r"(hours?|hrs?)\b",
        re.IGNORECASE,
    )