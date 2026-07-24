from scripts.commercial.product_acquisition_engine import ProductAcquisitionEngine
from scripts.commercial.product_normalization_engine import ProductNormalizationEngine

engine = ProductAcquisitionEngine()

normalizer = ProductNormalizationEngine()

product = engine.acquire_from_manual({

    "product_name": "Unitree G1",

    "manufacturer": "Unitree",

    "category": "humanoid robots",

    "primary_use": "research",

    "industry": "research",

    "environment": "indoor",

    "target_user": "research labs",

    "mobility": "bipedal",

    "autonomy_level": "semi-autonomous"

})

product = normalizer.normalize(product)

print(product)