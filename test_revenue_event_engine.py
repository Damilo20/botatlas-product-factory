from scripts.commercial.revenue_event_engine import RevenueEventEngine

engine = RevenueEventEngine()

events = engine.list_events()

print("=" * 50)
print("Revenue Event Engine Test")
print("=" * 50)

print(f"Found {len(events)} revenue events")
print(f"Gross Revenue: ${engine.total_gross_revenue():,.2f}")
print(f"Confirmed Revenue: ${engine.total_confirmed_revenue():,.2f}")
print(f"Conversions: {engine.total_conversions()}")

print("=" * 50)

for event in events:
    fields = event["fields"]

    print(
        fields.get("event_type", "Unknown"),
        fields.get("gross_revenue", 0),
        fields.get("confirmed_revenue", 0),
    )