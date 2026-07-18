from dataclasses import dataclass, field

from scripts.commercial.models.optimization_opportunity import (
    OptimizationOpportunity,
)
from scripts.commercial.models.optimization_strategy import (
    OptimizationStrategy,
)
from scripts.commercial.models.budget_recommendation import (
    BudgetRecommendation,
)
from scripts.commercial.models.experiment_recommendation import (
    ExperimentRecommendation,
)


@dataclass(frozen=True)
class OptimizationSnapshot:
    opportunities: list[OptimizationOpportunity] = field(default_factory=list)

    strategies: list[OptimizationStrategy] = field(default_factory=list)

    budget_recommendations: list[BudgetRecommendation] = field(default_factory=list)

    experiment_recommendations: list[
        ExperimentRecommendation
    ] = field(default_factory=list)

    total_estimated_revenue_uplift: float = 0.0

    active: bool = True