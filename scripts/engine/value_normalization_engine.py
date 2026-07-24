"""
BotAtlas Value Normalization Engine

Normalizes claimed values into comparable canonical forms.

Responsibilities
----------------
- Normalize formatting.
- Normalize whitespace.
- Normalize capitalization.
- Prepare values for comparison.

Non-Responsibilities
--------------------
- Truth resolution
- Unit conversion (future)
- Semantic interpretation
"""

import re


class ValueNormalizationEngine:
    """
    Layer 11 Value Normalization Engine.

    Produces canonical string representations suitable for
    evidence comparison.
    """

    def normalize(
        self,
        value: str | None,
    ) -> str:
        """
        Normalize a claimed value.
        """

        if value is None:
            return ""

        value = value.strip().lower()

        value = re.sub(
            r"\s+",
            " ",
            value,
        )

        return value

    def normalize_all(
        self,
        values: list[str],
    ) -> list[str]:
        return [
            self.normalize(value)
            for value in values
        ]