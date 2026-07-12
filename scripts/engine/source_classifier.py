from urllib.parse import urlparse

from scripts.models.source import Source


class SourceClassifier:
    """
    Classifies BotAtlas sources by source type and ownership.

    Layer 5 classification is deterministic and does not perform
    network access.
    """

    MANUFACTURER_DOMAINS = {
        "figure.ai",
    }

    MARKETPLACE_DOMAINS = {
        "amazon.com",
        "ebay.com",
        "walmart.com",
    }

    def classify(self, source: Source) -> Source:
        domain = self._normalize_domain(source.source_url)

        source.domain = domain

        if domain in self.MANUFACTURER_DOMAINS:
            source.source_type = "MANUFACTURER"
            source.ownership_type = "FIRST_PARTY"

        elif domain in self.MARKETPLACE_DOMAINS:
            source.source_type = "MARKETPLACE"
            source.ownership_type = "THIRD_PARTY"

        else:
            source.source_type = "UNKNOWN"
            source.ownership_type = "THIRD_PARTY"

        return source

    def _normalize_domain(self, url: str) -> str:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]

        return domain
