from scripts.engine.http_retrieval_adapter import (
    HttpRetrievalAdapter,
)

from scripts.models.discovered_evidence_source import (
    DiscoveredEvidenceSource,
)


def test_http_retrieval():
    source = DiscoveredEvidenceSource(
        source_name="Python",
        source_url="https://www.python.org/",
        source_family="Official",
        parent_candidate_name="Python",
        parent_candidate_url="https://www.python.org/",
        search_query="Python",
    )

    adapter = HttpRetrievalAdapter()

    content = adapter.retrieve(source)

    # Basic validation
    assert isinstance(content, str)
    assert len(content) > 100

    print()
    print("========== Retrieval Preview ==========")
    print(content[:500])
    print("=======================================")

    print()
    print("===================================")
    print(" HTTP Retrieval PASSED")
    print("===================================")


if __name__ == "__main__":
    test_http_retrieval()