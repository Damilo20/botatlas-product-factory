from dataclasses import fields

from scripts.engine.evidence_extraction_pipeline import (
    EvidenceExtractionPipeline,
)
from scripts.models.attributed_evidence_claim import (
    AttributedEvidenceClaim,
)
from scripts.models.extracted_claim_candidate import (
    ExtractedClaimCandidate,
)
from scripts.models.retrieved_evidence_material import (
    RetrievedEvidenceMaterial,
)
from scripts.models.discovered_evidence_source import (
    DiscoveredEvidenceSource,
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
}


class StaticMaterialRetriever:
    def __init__(self, content_by_url: dict[str, str]):
        self.content_by_url = content_by_url

    def retrieve(
        self,
        source: DiscoveredEvidenceSource,
    ) -> str:
        return self.content_by_url.get(source.source_url, "")


def assert_trust_boundary(model: type) -> None:
    names = {
        field.name
        for field in fields(model)
    }

    leaked = names & FORBIDDEN

    assert not leaked, (
        f"{model.__name__} leaked trust fields: "
        f"{sorted(leaked)}"
    )


print("\n=== BOTATLAS LAYER 8 EVIDENCE AUDIT ===")

print("\n=== RUNTIME TRUST CONTRACT AUDIT ===")

for model in (
    RetrievedEvidenceMaterial,
    ExtractedClaimCandidate,
    AttributedEvidenceClaim,
):
    assert_trust_boundary(model)
    print(
        "PASS:",
        model.__name__,
        "cannot carry trust fields",
    )


print("\n=== CONTRADICTION PRESERVATION AUDIT ===")

sources = [
    DiscoveredEvidenceSource(
        source_name="Figure AI Documentation",
        source_url="https://example.com/figure-docs",
        source_family="OFFICIAL_DOCUMENTATION",
        parent_candidate_name="Figure 02",
        parent_candidate_url="https://www.figure.ai/",
        search_query="Figure 02 documentation specifications manual",
    ),
    DiscoveredEvidenceSource(
        source_name="Figure 02 Technical Review",
        source_url="https://example.com/figure-review",
        source_family="TECHNICAL_SOURCE",
        parent_candidate_name="Figure 02",
        parent_candidate_url="https://www.figure.ai/",
        search_query="Figure 02 technical specifications review",
    ),
]

retriever = StaticMaterialRetriever(
    {
        "https://example.com/figure-docs": (
            "Figure 02 can operate for 5 hours. "
            "The robot weighs 70 kg."
        ),
        "https://example.com/figure-review": (
            "Figure 02 can operate for 4.5 hours. "
            "The robot weighs 70 kg."
        ),
    }
)

pipeline = EvidenceExtractionPipeline(
    retriever=retriever,
)

claims = pipeline.run(sources)

runtime_claims = [
    claim
    for claim in claims
    if claim.field_name == "runtime"
]

assert len(runtime_claims) == 2

runtime_values = {
    claim.claimed_value
    for claim in runtime_claims
}

assert runtime_values == {
    "5 hours",
    "4.5 hours",
}

runtime_families = {
    claim.source_family
    for claim in runtime_claims
}

assert runtime_families == {
    "OFFICIAL_DOCUMENTATION",
    "TECHNICAL_SOURCE",
}

for claim in runtime_claims:
    print(
        claim.field_name,
        "|",
        claim.claimed_value,
        "|",
        claim.source_family,
        "|",
        claim.source_name,
    )

print("PASS: contradictory claims remain independent")
print("PASS: contradiction provenance remains attached")


print("\n=== LINEAGE AUDIT ===")

assert all(
    claim.parent_candidate_name == "Figure 02"
    for claim in claims
)

assert all(
    claim.parent_candidate_url == "https://www.figure.ai/"
    for claim in claims
)

assert all(
    claim.source_name
    for claim in claims
)

assert all(
    claim.source_url
    for claim in claims
)

assert all(
    claim.search_query
    for claim in claims
)

print("PASS: parent candidate lineage survives")
print("PASS: source lineage survives")
print("PASS: search-query lineage survives")


print("\n=== ARCHITECTURE RESULT ===")
print("Layer 8 extraction/attribution: PASS")
print("Evidence lineage: PASS")
print("Contradiction preservation: PASS")
print("Trust boundary: PASS")
print("PASS: BOTATLAS LAYER 8 EVIDENCE GATE")
