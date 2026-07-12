from datetime import datetime, timezone

from scripts.models.provenance import Provenance
from scripts.models.source import Source


class ProvenanceEngine:
    """
    Creates provenance records for intelligence observed by BotAtlas.

    Layer 5 records origin history but does not resolve claims.
    """

    def create(
        self,
        source: Source,
        discovery_method: str = "UNKNOWN",
        content_type: str = "UNKNOWN",
        content_reference: str | None = None,
    ) -> Provenance:
        source_id = source.source_id or self._fallback_source_id(source)

        return Provenance(
            source_id=source_id,
            source_url=source.source_url,
            discovery_method=discovery_method,
            observed_at=datetime.now(timezone.utc).isoformat(),
            content_type=content_type,
            content_reference=content_reference,
        )

    def _fallback_source_id(self, source: Source) -> str:
        domain = source.domain or "unknown"

        normalized = (
            domain.upper()
            .replace(".", "-")
            .replace("_", "-")
        )

        return f"SRC-{normalized}"
