"""
BotAtlas HTTP Retrieval Adapter

Live implementation of the EvidenceMaterialRetriever protocol.

Responsibilities:
- Perform HTTP/HTTPS retrieval
- Handle common HTTP content encodings
- Decode response bytes into text

Non-Responsibilities:
- HTML parsing
- Metadata extraction
- Claim extraction
- Trust scoring
- Truth resolution
"""

from gzip import decompress
from urllib.request import Request, urlopen

from scripts.engine.evidence_material_acquisition import (
    EvidenceMaterialRetriever,
)
from scripts.models.discovered_evidence_source import (
    DiscoveredEvidenceSource,
)


class HttpRetrievalAdapter(EvidenceMaterialRetriever):
    """
    Retrieves raw text from HTTP/HTTPS evidence sources.

    Returns decoded document content while preserving retrieval
    as a separate concern from parsing and analysis.
    """

    USER_AGENT = "BotAtlas/1.0 (+https://botatlas.ai)"

    def retrieve(
        self,
        source: DiscoveredEvidenceSource,
    ) -> str:

        request = Request(
            source.source_url,
            headers={
                "User-Agent": self.USER_AGENT,
                "Accept": "*/*",
                "Accept-Encoding": "gzip",
            },
        )

        with urlopen(request, timeout=30) as response:

            data = response.read()

            # Handle gzip-compressed responses
            if response.headers.get("Content-Encoding") == "gzip":
                data = decompress(data)

            # Determine the correct character encoding
            encoding = (
                response.headers.get_content_charset()
                or "utf-8"
            )

            return data.decode(
                encoding,
                errors="replace",
            )