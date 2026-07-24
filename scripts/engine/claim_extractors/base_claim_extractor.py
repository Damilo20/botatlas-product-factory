"""
BotAtlas Base Claim Extractor

Provides shared extraction behavior for all structured claim extractors.
"""

from abc import ABC
from typing import Pattern

from scripts.models.extracted_claim_candidate import (
    ExtractedClaimCandidate,
)
from scripts.models.extracted_document import (
    ExtractedDocument,
)


class BaseClaimExtractor(ABC):
    """
    Base implementation for all structured claim extractors.
    """

    FIELD_NAME: str
    PATTERN: Pattern[str]

    def extract(
        self,
        document: ExtractedDocument,
    ) -> list[ExtractedClaimCandidate]:

        candidates: list[ExtractedClaimCandidate] = []

        content = document.text or ""

        for match in self.PATTERN.finditer(content):

            claim_text = self._claim_text(
                content,
                match.start(),
                match.end(),
            )

            claimed_value = " ".join(
                g
                for g in match.groups()
                if g is not None
            ).strip()

            candidates.append(
                ExtractedClaimCandidate(
                    field_name=self.FIELD_NAME,
                    claimed_value=claimed_value,
                    claim_text=claim_text,
                    source_name=document.source_name,
                    source_url=document.source_url,
                    source_family=document.source_family,
                    parent_candidate_name=document.parent_candidate_name,
                    parent_candidate_url=document.parent_candidate_url,
                    search_query=document.search_query,
                    extraction_method=document.extraction_method,
                    document_title=document.title,
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
            0 if sentence_start == -1
            else sentence_start + 1
        )

        sentence_ends = [
            p
            for p in (
                content.find(".", end),
                content.find("!", end),
                content.find("?", end),
            )
            if p != -1
        ]

        sentence_end = (
            min(sentence_ends) + 1
            if sentence_ends
            else len(content)
        )

        return content[
            sentence_start:sentence_end
        ].strip()