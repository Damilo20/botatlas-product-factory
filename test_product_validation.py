from scripts.commercial.product_validation_engine import ProductValidationEngine
from scripts.commercial.product_acquisition_engine import ProductAcquisitionEngine

engine = ProductAcquisitionEngine()

validator = ProductValidationEngine()

product = engine.acquire_from_manual({

    "product_name": "Unitree G1",

    "manufacturer": "Unitree",

    "category": "Humanoid Robots"

})

result = validator.validate(product)

print(result)