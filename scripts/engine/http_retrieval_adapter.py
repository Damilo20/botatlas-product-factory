"""
BotAtlas HTTP Retrieval Adapter

Retrieves live HTML content from discovered evidence sources.

Implements the EvidenceMaterialRetriever protocol.
"""

from urllib.request import Request, urlopen

from scripts.engine.evidence_material_acquisition import (
    EvidenceMaterialRetriever,
)
from scripts.models.discovered_evidence_source import (
    DiscoveredEvidenceSource,
)


class HttpRetrievalAdapter(EvidenceMaterialRetriever):

    USER_AGENT = (
        "BotAtlas/1.0 (+https://botatlas.ai)"
    )

    def retrieve(
        self,
        source: DiscoveredEvidenceSource,
    ) -> str:

        request = Request(
            source.source_url,
            headers={
                "User-Agent": self.USER_AGENT,
            },
        )

        with urlopen(request, timeout=30) as response:

            return response.read().decode(
                "utf-8",
                errors="ignore",
            )