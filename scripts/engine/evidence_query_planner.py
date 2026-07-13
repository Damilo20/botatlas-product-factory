from scripts.models.evidence_search_target import EvidenceSearchTarget
from scripts.models.evidence_source_candidate import EvidenceSourceCandidate


class EvidenceQueryPlanner:
    """
    Layer 7 evidence query planning.

    Converts untrusted EvidenceSourceCandidate records into retrieval
    search targets.

    Does not retrieve evidence, verify sources, assign trust,
    score authority, or resolve claims.
    """

    QUERY_TEMPLATES = {
        "OFFICIAL_MANUFACTURER": "{identity} official manufacturer",
        "OFFICIAL_DOCUMENTATION": "{identity} documentation specifications manual",
        "AUTHORIZED_RETAILER": "{identity} authorized retailer distributor",
        "TECHNICAL_SOURCE": "{identity} technical specifications review",
        "INDEPENDENT_REPORTING": "{identity} independent reporting news",
    }

    def plan(
        self,
        source_candidates: list[EvidenceSourceCandidate],
    ) -> list[EvidenceSearchTarget]:
        targets = []

        for candidate in source_candidates:
            identity_parts = [
                part
                for part in (
                    candidate.parent_candidate_name,
                    candidate.source_name,
                )
                if part
            ]

            identity = " ".join(dict.fromkeys(identity_parts))

            template = self.QUERY_TEMPLATES.get(
                candidate.source_family,
                "{identity}",
            )

            targets.append(
                EvidenceSearchTarget(
                    parent_candidate_name=candidate.parent_candidate_name,
                    parent_candidate_url=candidate.parent_candidate_url,
                    source_family=candidate.source_family,
                    search_query=template.format(identity=identity),
                )
            )

        return targets
