from dataclasses import dataclass

from scripts.commercial.models.optimization_priority import OptimizationPriority


@dataclass(frozen=True)
class BudgetRecommendation:
    revenue_channel: str

    current_budget: float

    recommended_budget: float

    budget_change: float

    priority: OptimizationPriority

    rationale: str

    expected_revenue_uplift: float = 0.0

    confidence: str = "UNKNOWN"

    active: bool = True