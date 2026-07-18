"""
BotAtlas Commercial Scoring Service

Centralized scoring logic used across all commercial intelligence
engines.

This service contains no Airtable or external API logic.
"""

from dataclasses import dataclass


@dataclass
class ScoreResult:
    score: float
    status: str


class ScoringService:
    """
    Shared scoring service for BotAtlas.
    """

    def normalize(self, value, minimum, maximum):
        """
        Normalize a value to the range 0–100.
        """
        if maximum == minimum:
            return 0.0

        score = ((value - minimum) / (maximum - minimum)) * 100

        return max(0.0, min(100.0, score))

    def performance_status(self, score):
        """
        Convert a numeric score into a human-readable status.
        """
        if score >= 90:
            return "Excellent"

        if score >= 75:
            return "Good"

        if score >= 60:
            return "Fair"

        if score >= 40:
            return "Needs Attention"

        return "Critical"

    def health_score(self, revenue, conversions):
        """
        Simple commercial health score.

        Version 1.0:
        Weighted equally between revenue and conversions.
        """

        revenue_score = self.normalize(revenue, 0, 10000)
        conversion_score = self.normalize(conversions, 0, 100)

        final_score = (revenue_score + conversion_score) / 2

        return ScoreResult(
            score=round(final_score, 2),
            status=self.performance_status(final_score),
        )

    def confidence_score(self, confirmed_events, total_events):
        """
        Confidence based on event confirmation ratio.
        """

        if total_events == 0:
            return ScoreResult(0.0, "No Data")

        score = (confirmed_events / total_events) * 100

        return ScoreResult(
            score=round(score, 2),
            status=self.performance_status(score),
        )