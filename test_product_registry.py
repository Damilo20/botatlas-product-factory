from scripts.commercial.revenue_event_engine import RevenueEventEngine

engine = RevenueEventEngine()

events = engine.list_events()

print(f"Found {len(events)} revenue events")

print("Gross Revenue:", engine.total_gross_revenue())
print("Confirmed Revenue:", engine.total_confirmed_revenue())
print("Conversions:", engine.total_conversions())