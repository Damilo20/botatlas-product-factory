from scripts.integrations.airtable_client import airtable

products = airtable.table("COMM_Products")

records = products.all()

print("✅ Connected successfully!")
print(f"Records found: {len(records)}")