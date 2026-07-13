from datetime import datetime, timezone

from scripts.models.evidence_source_candidate import EvidenceSourceCandidate


class EvidenceExpansionEngine:
    """
    Layer 7 evidence expansion.

    Generates untrusted evidence-source candidates.
    Does not assign authority, confidence, verification, or truth.
    """

    SOURCE_FAMILIES = (
        "OFFICIAL_MANUFACTURER",
        "OFFICIAL_DOCUMENTATION",
        "AUTHORIZED_RETAILER",
        "TECHNICAL_SOURCE",
        "INDEPENDENT_REPORTING",
    )

    def expand(
        self,
        candidate_name: str,
        candidate_url: str,
        manufacturer_hint: str | None = None,
        model_hint: str | None = None,
    ) -> list[EvidenceSourceCandidate]:
        identity_parts = [
            part
            for part in (
                manufacturer_hint,
                model_hint,
                candidate_name,
            )
            if part
        ]

        identity = " ".join(dict.fromkeys(identity_parts))

        candidates = []

        for source_family in self.SOURCE_FAMILIES:
            candidates.append(
                EvidenceSourceCandidate(
                    source_name=f"{identity} {source_family}",
                    source_url=candidate_url,
                    source_family=source_family,
                    discovery_method="EVIDENCE_EXPANSION",
                    parent_candidate_name=candidate_name,
                    parent_candidate_url=candidate_url,
                    discovered_at=datetime.now(
                        timezone.utc
                    ).isoformat(),
                )
            )

        return candidates
