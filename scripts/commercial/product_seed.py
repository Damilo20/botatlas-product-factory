from scripts.repositories.product_repository import ProductRepository


class ProductSeeder:

    def __init__(self):
        self.repo = ProductRepository()

    def seed(self):

        products = [

            {
                "Product ID": "BOT-HUM-000001",
                "Product Name": "Unitree G1",
                "Brand": "Unitree",
                "Model": "G1",
                "Category": "Humanoid Robots",
                "Primary Use": "Research",
                "Industry": "Education",
                "Environment": "Indoor",
                "Target User": "Research Labs",
                "Mobility": "Bipedal",
                "Autonomy Level": "Semi-Autonomous",
                "Status": "Research"
            },

            {
                "Product ID": "BOT-QDR-000001",
                "Product Name": "Unitree Go2",
                "Brand": "Unitree",
                "Model": "Go2",
                "Category": "Robot Pets",
                "Primary Use": "Security",
                "Industry": "Commercial",
                "Environment": "Indoor/Outdoor",
                "Target User": "Businesses",
                "Mobility": "Quadruped",
                "Autonomy Level": "Semi-Autonomous",
                "Status": "Research"
            }

        ]

        for product in products:
            self.repo.create_product(product)

        print(f"Inserted {len(products)} products.")