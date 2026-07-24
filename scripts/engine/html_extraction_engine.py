"""
BotAtlas HTML Extraction Engine

Converts retrieved HTML evidence into an ExtractedDocument.
"""

from html.parser import HTMLParser

from scripts.models.extracted_document import (
    ExtractedDocument,
)
from scripts.models.retrieved_evidence_material import (
    RetrievedEvidenceMaterial,
)


class _HTMLTextExtractor(HTMLParser):

    def __init__(self):
        super().__init__()

        self._parts: list[str] = []
        self._ignore_depth = 0
        self.title: str | None = None
        self._inside_title = False

    def handle_starttag(self, tag, attrs):

        if tag in {"script", "style"}:
            self._ignore_depth += 1

        if tag == "title":
            self._inside_title = True

    def handle_endtag(self, tag):

        if tag in {"script", "style"} and self._ignore_depth:
            self._ignore_depth -= 1

        if tag == "title":
            self._inside_title = False

    def handle_data(self, data):

        if self._ignore_depth:
            return

        text = data.strip()

        if not text:
            return

        if self._inside_title and self.title is None:
            self.title = text

        self._parts.append(text)

    def get_text(self) -> str:
        return "\n".join(self._parts)


class HtmlExtractionEngine:
    """
    Converts retrieved evidence material into an ExtractedDocument.
    """

    def extract(
        self,
        material: RetrievedEvidenceMaterial,
    ) -> ExtractedDocument:

        parser = _HTMLTextExtractor()

        parser.feed(material.content)
        parser.close()

        return ExtractedDocument(
            source_name=material.source_name,
            source_url=material.source_url,
            source_family=material.source_family,
            parent_candidate_name=material.parent_candidate_name,
            parent_candidate_url=material.parent_candidate_url,
            search_query=material.search_query,
            title=parser.title,
            text=parser.get_text(),
            extraction_method="HTML",
        )