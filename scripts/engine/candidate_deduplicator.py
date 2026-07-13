from urllib.parse import urlsplit, urlunsplit

from scripts.models.discovery_candidate import DiscoveryCandidate


class CandidateDeduplicator:
    """
    BotAtlas Layer 6 candidate deduplication boundary.

    Detects duplicate discovery candidates using normalized URLs.

    Deduplication does not verify candidates, assign confidence,
    classify source authority, resolve claims, or apply truth.
    """

    def normalize_url(self, url: str) -> str:
        value = url.strip()

        if "://" not in value:
            value = f"https://{value}"

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
        if not path:
            path = ""

        return urlunsplit(
            (
                scheme,
                netloc,
                path,
                parts.query,
                "",
            )
        )

    def deduplicate(
        self,
        candidates: list[DiscoveryCandidate],
    ) -> list[DiscoveryCandidate]:
        unique_candidates = []
        seen_urls = set()

        for candidate in candidates:
            normalized_url = self.normalize_url(candidate.candidate_url)

            if normalized_url in seen_urls:
                continue

            seen_urls.add(normalized_url)
            unique_candidates.append(candidate)

        return unique_candidates
