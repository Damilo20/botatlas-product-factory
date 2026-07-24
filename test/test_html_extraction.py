from scripts.engine.html_extraction_engine import (
    HtmlExtractionEngine,
)

from scripts.engine.http_retrieval_adapter import (
    HttpRetrievalAdapter,
)

from scripts.models.discovered_evidence_source import (
    DiscoveredEvidenceSource,
)


def test_html_extraction():

    source = DiscoveredEvidenceSource(
        source_name="Python",
        source_url="https://www.python.org/",
        source_family="Official",
        parent_candidate_name="Python",
        parent_candidate_url="https://www.python.org/",
        search_query="Python",
    )

    html = HttpRetrievalAdapter().retrieve(source)

    text = HtmlExtractionEngine().extract(html)

    assert len(text) > 100

    print()
    print("========== Extracted Text ==========")
    print(text[:1000])
    print("====================================")

    print()
    print("===================================")
    print(" HTML Extraction PASSED")
    print("===================================")


if __name__ == "__main__":
    test_html_extraction()