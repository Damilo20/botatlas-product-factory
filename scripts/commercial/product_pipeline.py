"""
BotAtlas Product Processing Pipeline

Coordinates the Product Domain workflow.

Responsibilities
----------------
- Acquire products
- Validate products
- Normalize products
- Enrich products

Non-Responsibilities
--------------------
- Evidence retrieval
- Claim extraction
- Truth resolution
- Product persistence
"""

from scripts.commercial.product_acquisition_engine import ProductAcquisitionEngine
from scripts.commercial.product_validation_engine import ProductValidationEngine
from scripts.commercial.product_normalization_engine import ProductNormalizationEngine
from scripts.commercial.product_enrichment_engine import ProductEnrichmentEngine

from scripts.models.product import Product


class ProductPipeline:

    def __init__(self):

        self.acquisition = ProductAcquisitionEngine()

        self.validation = ProductValidationEngine()

        self.normalization = ProductNormalizationEngine()

        self.enrichment = ProductEnrichmentEngine()

    def process(
        self,
        raw_product,
    ) -> Product | None:

        product = self.acquisition.acquire_from_manual(raw_product)

        validation = self.validation.validate(product)

        if not validation.valid:

            print("Validation Failed")

            print(validation.errors)

            return None

        product = self.normalization.normalize(product)

        product = self.enrichment.enrich(product)

        print("Pipeline Completed")

        return product