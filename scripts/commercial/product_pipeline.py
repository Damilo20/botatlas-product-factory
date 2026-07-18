"""
BotAtlas Product Processing Pipeline
"""

from scripts.commercial.product_acquisition_engine import ProductAcquisitionEngine
from scripts.commercial.product_normalization_engine import ProductNormalizationEngine
from scripts.commercial.product_validation_engine import ProductValidationEngine


class ProductPipeline:

    def __init__(self):

        self.acquisition = ProductAcquisitionEngine()

        self.validation = ProductValidationEngine()

        self.normalizer = ProductNormalizationEngine()

    def process(self, raw_product):

        product = self.acquisition.acquire_from_manual(raw_product)

        product = self.normalizer.normalize(product)

        validation = self.validation.validate(product)

        if not validation.valid:

            print("Validation Failed")

            print(validation.errors)

            return None

        print("Validation Passed")

        return product