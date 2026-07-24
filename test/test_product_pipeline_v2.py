from scripts.commercial.product_pipeline import ProductPipeline

pipeline = ProductPipeline()

product = pipeline.process({

    "product_name": "Unitree G1",

    "manufacturer": "Unitree",

    "category": "Humanoid Robots"

})

print()

print(product)