import inspect
from dataclasses import fields

from scripts.commercial.models.channel_performance import ChannelPerformance
from scripts.commercial.models.commercial_performance_snapshot import CommercialPerformanceSnapshot
from scripts.commercial.models.journey_performance import JourneyPerformance
from scripts.commercial.models.product_performance import ProductPerformance
from scripts.commercial.commercial_performance_engine import CommercialPerformanceEngine


FORBIDDEN = {
    "truth",
    "truth_value",
    "verified",
    "verification_status",
    "accepted_claim",
    "rejected_claim",
    "winning_claim",
    "final_value",
}


def assert_boundary(model: type) -> None:
    names = {field.name for field in fields(model)}
    leaked = names & FORBIDDEN
    print(model.__name__, "TRUST / INTELLIGENCE LEAK:", sorted(leaked))
    assert not leaked


print("=== BOTATLAS R10 COMMERCIAL PERFORMANCE AUDIT ===")

print("\n=== CONTRACT BOUNDARY AUDIT ===")

for model in (
    ProductPerformance,
    ChannelPerformance,
    JourneyPerformance,
    CommercialPerformanceSnapshot,
):
    assert_boundary(model)

print("\n=== ENGINE SOURCE AUDIT ===")

source = inspect.getsource(CommercialPerformanceEngine)

for forbidden in FORBIDDEN:
    assert forbidden not in source

print("PASS: engine contains no truth or claim-decision vocabulary")

print("\n=== ARCHITECTURE RESULT ===")
print("Product performance boundary: PASS")
print("Channel performance boundary: PASS")
print("Journey performance boundary: PASS")
print("Commercial snapshot boundary: PASS")
print("Decision leakage: NONE")
print("PASS: BOTATLAS R10 COMMERCIAL PERFORMANCE GATE")

print("\n=== FINAL STATUS ===")
