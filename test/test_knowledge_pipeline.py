import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

"""
Integration test for the BotAtlas Knowledge Pipeline.
"""

from scripts.engine.claim_extraction_engine import (
    ClaimExtractionEngine,
)
from scripts.engine.claim_grouping_engine import (
    ClaimGroupingEngine,
)
from scripts.engine.evidence_attribution_engine import (
    EvidenceAttributionEngine,
)
from scripts.engine.evidence_material_acquisition import (
    EvidenceMaterialAcquisition,
)
from scripts.engine.html_extraction_engine import (
    HtmlExtractionEngine,
)
from scripts.engine.http_retrieval_adapter import (
    HttpRetrievalAdapter,
)
from scripts.engine.knowledge_pipeline import (
    KnowledgePipeline,
)
from scripts.engine.truth_engine import (
    TruthEngine,
)
from scripts.models.discovered_evidence_source import (
    DiscoveredEvidenceSource,
)

def main():

    source = DiscoveredEvidenceSource(
        source_name="Python",
        source_url="https://www.python.org/",
        source_family="OFFICIAL",
        parent_candidate_name="Python",
        parent_candidate_url="https://www.python.org/",
        search_query="Python Official Website",
        discovery_method="MANUAL",
    )

    pipeline = KnowledgePipeline(
        acquisition=EvidenceMaterialAcquisition(
            retriever=HttpRetrievalAdapter(),
        ),
        extraction=HtmlExtractionEngine(),
        claim_extraction=ClaimExtractionEngine(),
        attribution=EvidenceAttributionEngine(),
        grouping=ClaimGroupingEngine(),
        truth=TruthEngine(),
    )

    result = pipeline.process_source(source)

    print("=" * 60)
    print("KNOWLEDGE PIPELINE PASSED")
    print("=" * 60)

    print()

    print("Source")
    print("------")
    print(result["material"].source_name)

    print()

    print("Document")
    print("--------")
    print(result["document"].title)
    print(f"Characters: {len(result['document'].text):,}")

    print()

    print("Claims")
    print("------")
    print(len(result["claims"]))

    print()

    print("Attributed Claims")
    print("-----------------")
    print(len(result["attributed_claims"]))

    print()

    print("Claim Groups")
    print("------------")
    print(len(result["claim_groups"]))

    print()

    print("Reconciliations")
    print("---------------")
    print(len(result["reconciliations"]))

    print()

    for reconciliation in result["reconciliations"]:

        print(
            f"{reconciliation.field_name:<20}"
            f"{reconciliation.status.name:<18}"
            f"{reconciliation.distinct_values}"
        )


if __name__ == "__main__":
    main()