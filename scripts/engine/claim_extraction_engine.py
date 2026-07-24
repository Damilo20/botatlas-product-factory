from scripts.engine.claim_extractors import (
    RuntimeExtractor,
    WeightExtractor,
    BatteryExtractor,
    ChargingTimeExtractor,
    DegreesOfFreedomExtractor,
    DimensionsExtractor,
    ManufacturerExtractor,
    PayloadExtractor,
    PriceExtractor,
    ReleaseDateExtractor,
    SpeedExtractor,
)

from scripts.models.extracted_claim_candidate import (
    ExtractedClaimCandidate,
)
from scripts.models.extracted_document import (
    ExtractedDocument,
)


class ClaimExtractionEngine:
    """
    Executes all registered claim extractors.
    """

    def __init__(self):

        self.extractors = [

            RuntimeExtractor(),

            WeightExtractor(),

            BatteryExtractor(),

            ChargingTimeExtractor(),

            DegreesOfFreedomExtractor(),

            DimensionsExtractor(),

            ManufacturerExtractor(),

            PayloadExtractor(),

            PriceExtractor(),

            ReleaseDateExtractor(),

            SpeedExtractor(),

        ]

    def extract(
        self,
        document: ExtractedDocument,
    ) -> list[ExtractedClaimCandidate]:

        candidates: list[ExtractedClaimCandidate] = []

        for extractor in self.extractors:

            candidates.extend(
                extractor.extract(document)
            )

        return candidates