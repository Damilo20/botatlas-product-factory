from urllib.parse import urlsplit, urlunsplit

from scripts.models.discovered_evidence_source import (
    DiscoveredEvidenceSource,
)
from scripts.models.evidence_search_target import EvidenceSearchTarget


class EvidenceSourceDiscovery:
    """
    Layer 7 evidence source discovery.

    Converts raw retrieval results into untrusted discovered
    evidence source records.

    Does not verify evidence, score authority, resolve claims,
    or assign product trust.
    """

    @staticmethod
    def _normalize_url(value: str) -> str:
        value = value.strip()
        parts = urlsplit(value)

        scheme = parts.scheme.lower()
        hostname = (parts.hostname or "").lower()

        if hostname.startswith("www."):
            hostname = hostname[4:]

        port = parts.port

        if port and not (
            (scheme == "https" and port == 443)
            or (scheme == "http" and port == 80)
        ):
            netloc = f"{hostname}:{port}"
        else:
            netloc = hostname

        path = parts.path.rstrip("/")

        return urlunsplit(
            (
                scheme,
                netloc,
                path,
                parts.query,
                "",
            )
        )

    def discover(
        self,
        target: EvidenceSearchTarget,
        retrieval_results: list[dict],
    ) -> list[DiscoveredEvidenceSource]:
        discovered = []
        seen_urls = set()

        for result in retrieval_results:
            source_url = str(result.get("url", "")).strip()

            if not source_url:
                continue

            normalized_url = self._normalize_url(source_url)

            if not normalized_url or normalized_url in seen_urls:
                continue

            seen_urls.add(normalized_url)

            source_name = str(
                result.get("name")
                or result.get("title")
                or normalized_url
            ).strip()

            discovered.append(
                DiscoveredEvidenceSource(
                    source_name=source_name,
                    source_url=normalized_url,
                    source_family=target.source_family,
                    parent_candidate_name=target.parent_candidate_name,
                    parent_candidate_url=target.parent_candidate_url,
                    search_query=target.search_query,
                )
            )

        return discovered
