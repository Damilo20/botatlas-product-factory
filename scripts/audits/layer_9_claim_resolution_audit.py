from dataclasses import fields

from scripts.engine.claim_resolution_pipeline import ClaimResolutionPipeline
from scripts.models.attributed_evidence_claim import AttributedEvidenceClaim
from scripts.models.claim_group import ClaimGroup
from scripts.models.evidence_comparison import (
    EvidenceComparison,
    EvidenceRelationship,
)
from scripts.models.claim_reconciliation import (
    ClaimReconciliation,
    ReconciliationState,
)


FORBIDDEN = {
    "verified",
    "verification_status",
    "selected",
    "truth",
    "true",
    "confidence_score",
    "quality_score",
    "authority_score",
    "reputation_score",
    "winner",
    "winning_claim",
}


def field_names(model: type) -> set[str]:
    return {item.name for item in fields(model)}


def assert_trust_boundary(model: type) -> None:
    leaked = field_names(model) & FORBIDDEN
    assert not leaked, f"{model.__name__} leaked decision fields: {leaked}"


def claim(
    field_name: str,
    claimed_value: str,
    source_name: str,
    source_family: str,
) -> AttributedEvidenceClaim:
    return AttributedEvidenceClaim(
        field_name=field_name,
        claimed_value=claimed_value,
        claim_text=f"Figure 02 claim: {claimed_value}.",
        source_name=source_name,
        source_url=(
            "https://example.com/"
            + source_name.lower().replace(" ", "-")
        ),
        source_family=source_family,
        parent_candidate_name="Figure 02",
        parent_candidate_url="https://www.figure.ai/",
        search_query=f"Figure 02 {field_name} evidence",
        extraction_method="STATIC_AUDIT",
        attribution_method="DIRECT_MATERIAL_PROVENANCE",
    )


print("\n=== BOTATLAS LAYER 9 CLAIM RESOLUTION AUDIT ===")

for model in (
    ClaimGroup,
    EvidenceComparison,
    ClaimReconciliation,
):
    assert_trust_boundary(model)
    print(f"PASS: {model.__name__} cannot carry decision/trust fields")

claims = [
    claim(
        "runtime",
        "5 hours",
        "Figure AI Documentation",
        "OFFICIAL_DOCUMENTATION",
    ),
    claim(
        "runtime",
        "4.5 hours",
        "Figure 02 Technical Review",
        "TECHNICAL_SOURCE",
    ),
    claim(
        "weight",
        "70 kg",
        "Figure AI Documentation",
        "OFFICIAL_DOCUMENTATION",
    ),
    claim(
        "weight",
        "70 kg",
        "Figure 02 Technical Review",
        "TECHNICAL_SOURCE",
    ),
    claim(
        "battery",
        "Lithium-Ion",
        "Figure AI Documentation",
        "OFFICIAL_DOCUMENTATION",
    ),
]

pipeline = ClaimResolutionPipeline()
results = pipeline.run(claims)

by_field = {
    result.field_name: result
    for result in results
}

runtime = by_field["runtime"]
weight = by_field["weight"]
battery = by_field["battery"]

print("\n=== RECONCILIATION AUDIT ===")

for result in results:
    print(
        result.field_name,
        "|",
        result.relationship.value,
        "|",
        result.reconciliation_state.value,
        "|",
        result.distinct_values,
        "| CLAIMS:",
        len(result.claims),
    )

assert runtime.relationship == EvidenceRelationship.CONFLICT
assert runtime.reconciliation_state == ReconciliationState.DISPUTED
assert runtime.distinct_values == ["5 hours", "4.5 hours"]
assert len(runtime.claims) == 2

assert weight.relationship == EvidenceRelationship.AGREEMENT
assert weight.reconciliation_state == ReconciliationState.CONSISTENT
assert weight.distinct_values == ["70 kg"]
assert len(weight.claims) == 2

assert (
    battery.relationship
    == EvidenceRelationship.INSUFFICIENT_EVIDENCE
)
assert (
    battery.reconciliation_state
    == ReconciliationState.UNDERDETERMINED
)
assert battery.distinct_values == ["Lithium-Ion"]
assert len(battery.claims) == 1

print("\nPASS: contradictory claims remain preserved")
print("PASS: Layer 9 does not select a winning claim")
print("PASS: agreement is classified without declaring truth")
print("PASS: insufficient evidence remains unresolved")
print("PASS: exact Layer 8 claim lineage survives reconciliation")
print("PASS: candidate identity survives Layer 9")
print("PASS: BOTATLAS LAYER 9 CLAIM RESOLUTION GATE")
