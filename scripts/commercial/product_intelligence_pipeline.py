"""
BotAtlas Product Intelligence Pipeline

Coordinates the complete product intelligence workflow.

This is the primary entry point for product processing.
"""

from scripts.commercial.product_pipeline import ProductPipeline
from scripts.repositories.product_repository import ProductRepository


class ProductIntelligencePipeline:

    def __init__(self):

        self.pipeline = ProductPipeline()

        self.repository = ProductRepository()

    def process(self, raw_product):

        product = self.pipeline.process(raw_product)

        if product is None:
            return None

        self.repository.create_product(product.to_airtable())

        return product