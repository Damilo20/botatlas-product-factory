from dataclasses import dataclass, field
from typing import Optional

from scripts.models.evidence import Evidence


@dataclass
class Claim:
    """
    Represents a single intelligence claim about a product.

    A Claim groups competing or supporting evidence
    around one product field and claimed value.
    """

    field_name: str
    claimed_value: str

    normalized_value: Optional[str] = None

    confidence_score: float = 0.0
    verification_status: str = "Pending"

    selected: bool = False

    evidence: list[Evidence] = field(default_factory=list)