from scripts.repositories.product_repository import ProductRepository

repo = ProductRepository()

print(repo)
print(repo.table)
print(type(repo.table))

records = repo.table.all()

print(f"\nRecords: {len(records)}")

for r in records:
    print(r)