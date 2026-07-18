from scripts.repositories.product_repository import ProductRepository

repo = ProductRepository()

records = repo.list_products()

print(f"Records returned: {len(records)}")

for record in records:
    print("=" * 60)
    print(record)