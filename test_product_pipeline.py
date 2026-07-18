from scripts.repositories.product_repository import ProductRepository

repo = ProductRepository()

products = repo.list_products()

for product in products:
    print("=" * 60)
    print(product["fields"])