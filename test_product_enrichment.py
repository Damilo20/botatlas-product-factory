from scripts.commercial.product_acquisition_engine import ProductAcquisitionEngine
from scripts.commercial.product_enrichment_engine import ProductEnrichmentEngine

engine = ProductAcquisitionEngine()

enrichment = ProductEnrichmentEngine()

product = engine.acquire_from_manual({

    "product_name": "Unitree G1",

    "manufacturer": "Unitree",

    "category": "Humanoid Robots"

})

product = enrichment.enrich(product)

print(product)