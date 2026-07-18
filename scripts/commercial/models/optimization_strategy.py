from dataclasses import dataclass

from scripts.commercial.models.optimization_priority import OptimizationPriority


@dataclass(frozen=True)
class OptimizationStrategy:
    strategy_name: str

    category: str

    priority: OptimizationPriority

    objective: str

    estimated_effort: str

    estimated_revenue_uplift: float = 0.0

    confidence: str = "UNKNOWN"

    active: bool = True