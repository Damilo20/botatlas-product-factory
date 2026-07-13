from dataclasses import fields

from scripts.engine.evidence_expansion_pipeline import EvidenceExpansionPipeline
from scripts.engine.evidence_query_planner import EvidenceQueryPlanner
from scripts.engine.static_retrieval_adapter import StaticRetrievalAdapter
from scripts.models.discovered_evidence_source import DiscoveredEvidenceSource
from scripts.models.evidence_search_target import EvidenceSearchTarget
from scripts.models.evidence_source_candidate import EvidenceSourceCandidate
from scripts.models.retrieval_result import RetrievalResult


FORBIDDEN_TRUST_FIELDS = {
    "verified",
    "verification_status",
    "confidence_score",
    "quality_score",
    "authority_score",
    "reputation_score",
    "selected",
    "true",
    "truth",
}


def audit_contracts():
    print("\n=== CONTRACT AUDIT ===")

    models = [
        EvidenceSourceCandidate,
        EvidenceSearchTarget,
        RetrievalResult,
        DiscoveredEvidenceSource,
    ]

    for model in models:
        names = {field.name for field in fields(model)}
        leaked = names & FORBIDDEN_TRUST_FIELDS

        print(model.__name__, sorted(names))

        assert not leaked, (
            f"{model.__name__} leaked trust fields: {sorted(leaked)}"
        )

    print("PASS: Layer 7 contracts contain no trust fields")


def build_pipeline_evidence():
    planner = EvidenceQueryPlanner()

    bootstrap = EvidenceExpansionPipeline()

    candidates = bootstrap.expansion.expand(
        candidate_name="Figure 02",
        candidate_url="https://www.figure.ai/",
        manufacturer_hint="Figure AI",
        model_hint="02",
    )

    targets = planner.plan(source_candidates=candidates)

    results_by_query = {
        target.search_query: [
            RetrievalResult(
                title=f"{target.source_family} Figure 02 Source",
                url=(
                    "https://example.com/"
                    f"{target.source_family.lower()}/figure-02"
                ),
                snippet="Raw retrieved reference material",
                provider="STATIC_TEST",
            )
        ]
        for target in targets
    }

    pipeline = EvidenceExpansionPipeline(
        retrieval_adapter=StaticRetrievalAdapter(results_by_query),
    )

    discovered = pipeline.run(
        candidate_name="Figure 02",
        candidate_url="https://www.figure.ai/",
        manufacturer_hint="Figure AI",
        model_hint="02",
    )

    return candidates, targets, discovered


def audit_orchestration():
    print("\n=== ORCHESTRATION AUDIT ===")

    candidates, targets, discovered = build_pipeline_evidence()

    print("EXPANDED:", len(candidates))
    print("TARGETS:", len(targets))
    print("DISCOVERED:", len(discovered))

    assert len(candidates) == 5
    assert len(targets) == len(candidates)
    assert len(discovered) == len(targets)

    candidate_families = [
        candidate.source_family
        for candidate in candidates
    ]

    target_families = [
        target.source_family
        for target in targets
    ]

    discovered_families = [
        source.source_family
        for source in discovered
    ]

    assert candidate_families == target_families
    assert target_families == discovered_families

    print("PASS: expansion output drives query planning")
    print("PASS: query planning drives retrieval")
    print("PASS: retrieval drives source discovery")
    print("PASS: source-family lineage survives orchestration")


def audit_provenance():
    print("\n=== PROVENANCE AUDIT ===")

    _, _, discovered = build_pipeline_evidence()

    for source in discovered:
        assert source.parent_candidate_name == "Figure 02"
        assert source.parent_candidate_url == "https://www.figure.ai/"
        assert source.source_family
        assert source.search_query

        print(
            source.source_family,
            "| PARENT:",
            source.parent_candidate_name,
            "| QUERY:",
            source.search_query,
        )

    print("PASS: parent candidate provenance survives")
    print("PASS: source-family provenance survives")
    print("PASS: search-query provenance survives")


def audit_runtime_trust_boundary():
    print("\n=== RUNTIME TRUST INJECTION AUDIT ===")

    models = [
        EvidenceSourceCandidate,
        EvidenceSearchTarget,
        RetrievalResult,
        DiscoveredEvidenceSource,
    ]

    for model in models:
        instance_fields = {
            field.name
            for field in fields(model)
        }

        for forbidden in FORBIDDEN_TRUST_FIELDS:
            assert forbidden not in instance_fields

    print("PASS: Layer 7 runtime contracts cannot carry trust fields")


def main():
    print("\n=== BOTATLAS LAYER 7 EVIDENCE GATE ===")

    audit_contracts()
    audit_orchestration()
    audit_provenance()
    audit_runtime_trust_boundary()

    print("\n=== ARCHITECTURE RESULT ===")
    print("Layer 7 evidence expansion: PASS")
    print("Evidence lineage: PASS")
    print("Trust boundary: PASS")
    print("PASS: BOTATLAS LAYER 7 EVIDENCE GATE")


if __name__ == "__main__":
    main()
