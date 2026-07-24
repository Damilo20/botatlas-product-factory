from scripts.commercial.product_acquisition_engine import ProductAcquisitionEngine

engine = ProductAcquisitionEngine()

product = engine.acquire_from_manual({

    "product_name": "Unitree G1",

    "manufacturer": "Unitree",

    "brand": "Unitree",

    "model": "G1",

    "category": "Humanoid Robots",

    "primary_use": "Research",

    "industry": "Research",

    "environment": "Indoor",

    "target_user": "Research Labs",

    "mobility": "Bipedal",

    "autonomy_level": "Semi-Autonomous",

    "description": "General purpose humanoid robot.",

    "msrp": 16000,

    "current_price": 16000

})

print(product)