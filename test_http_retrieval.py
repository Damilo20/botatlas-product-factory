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

    html = adapter.retrieve(source)

    assert "Python" in html

    print()

    print("==============================")
    print(" HTTP Retrieval PASSED")
    print("==============================")


if __name__ == "__main__":
    test_http_retrieval()