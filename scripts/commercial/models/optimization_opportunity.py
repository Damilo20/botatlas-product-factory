from dataclasses import dataclass

from scripts.commercial.models.optimization_priority import OptimizationPriority


@dataclass(frozen=True)
class OptimizationOpportunity:
    product_name: str
    product_url: str

    category: str

    priority: OptimizationPriority

    title: str

    description: str

    estimated_revenue_uplift: float = 0.0

    confidence: str = "UNKNOWN"

    active: bool = True