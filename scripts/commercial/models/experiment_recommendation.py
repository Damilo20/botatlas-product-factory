from dataclasses import dataclass

from scripts.commercial.models.optimization_priority import OptimizationPriority


@dataclass(frozen=True)
class ExperimentRecommendation:
    experiment_name: str

    category: str

    hypothesis: str

    success_metric: str

    priority: OptimizationPriority

    estimated_duration_days: int

    expected_revenue_uplift: float = 0.0

    confidence: str = "UNKNOWN"

    active: bool = True