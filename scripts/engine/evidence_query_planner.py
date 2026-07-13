from scripts.models.evidence_search_target import EvidenceSearchTarget


class EvidenceQueryPlanner:
    """
    Layer 7 source query planning.

    Produces distinct discovery intents for evidence source families.
    Does not retrieve evidence or assign trust.
    """

    QUERY_TEMPLATES = {
        "OFFICIAL_MANUFACTURER": '"{identity}" official manufacturer',
        "OFFICIAL_DOCUMENTATION": '"{identity}" documentation specifications manual',
        "AUTHORIZED_RETAILER": '"{identity}" authorized retailer distributor',
        "TECHNICAL_SOURCE": '"{identity}" technical specifications review',
        "INDEPENDENT_REPORTING": '"{identity}" independent reporting news',
    }

    def plan(
        self,
        candidate_name: str,
        candidate_url: str,
        manufacturer_hint: str | None = None,
        model_hint: str | None = None,
    ) -> list[EvidenceSearchTarget]:
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

        targets = []

        for source_family, template in self.QUERY_TEMPLATES.items():
            targets.append(
                EvidenceSearchTarget(
                    parent_candidate_name=candidate_name,
                    parent_candidate_url=candidate_url,
                    source_family=source_family,
                    search_query=template.format(identity=identity),
                )
            )

        return targets
