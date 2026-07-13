import re

from scripts.models.extracted_claim_candidate import (
    ExtractedClaimCandidate,
)
from scripts.models.retrieved_evidence_material import (
    RetrievedEvidenceMaterial,
)


class ClaimExtractionEngine:
    """
    Layer 8 untrusted claim extraction.

    Extracts explicit candidate claims from retrieved evidence material.

    Does not verify, score trust, select, or resolve claims.
    """

    EXTRACTION_PATTERNS = (
        (
            "runtime",
            re.compile(
                r"\b(?:operate|operates|run|runs|runtime)"
                r"(?:\s+for)?\s+(?:up\s+to\s+)?"
                r"(\d+(?:\.\d+)?)\s*(hours?|hrs?)\b",
                re.IGNORECASE,
            ),
        ),
        (
            "weight",
            re.compile(
                r"\b(?:weighs?|weight(?:\s+is)?)\s+"
                r"(\d+(?:\.\d+)?)\s*(kg|kilograms?|lbs?|pounds?)\b",
                re.IGNORECASE,
            ),
        ),
    )

    def extract(
        self,
        material: RetrievedEvidenceMaterial,
    ) -> list[ExtractedClaimCandidate]:
        candidates: list[ExtractedClaimCandidate] = []

        content = material.content or ""

        for field_name, pattern in self.EXTRACTION_PATTERNS:
            for match in pattern.finditer(content):
                claim_text = self._claim_text(
                    content=content,
                    start=match.start(),
                    end=match.end(),
                )

                claimed_value = " ".join(
                    part
                    for part in match.groups()
                    if part is not None
                ).strip()

                candidates.append(
                    ExtractedClaimCandidate(
                        field_name=field_name,
                        claimed_value=claimed_value,
                        claim_text=claim_text,
                        source_name=material.source_name,
                        source_url=material.source_url,
                        source_family=material.source_family,
                        parent_candidate_name=material.parent_candidate_name,
                        parent_candidate_url=material.parent_candidate_url,
                        search_query=material.search_query,
                        extraction_method="PATTERN",
                        material_acquired_at=str(material.acquired_at),
                    )
                )

        return candidates

    @staticmethod
    def _claim_text(
        content: str,
        start: int,
        end: int,
    ) -> str:
        sentence_start = max(
            content.rfind(".", 0, start),
            content.rfind("!", 0, start),
            content.rfind("?", 0, start),
        )

        sentence_start = (
            0
            if sentence_start == -1
            else sentence_start + 1
        )

        sentence_ends = [
            position
            for position in (
                content.find(".", end),
                content.find("!", end),
                content.find("?", end),
            )
            if position != -1
        ]

        sentence_end = (
            min(sentence_ends) + 1
            if sentence_ends
            else len(content)
        )

        return content[sentence_start:sentence_end].strip()
