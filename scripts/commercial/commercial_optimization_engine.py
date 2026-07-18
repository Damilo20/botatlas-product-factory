from __future__ import annotations

from scripts.commercial.models.commercial_performance_snapshot import (
    CommercialPerformanceSnapshot,
)
from scripts.commercial.models.optimization_opportunity import (
    OptimizationOpportunity,
)
from scripts.commercial.models.optimization_priority import (
    OptimizationPriority,
)
from scripts.commercial.models.optimization_snapshot import (
    OptimizationSnapshot,
)
from scripts.commercial.models.optimization_strategy import (
    OptimizationStrategy,
)


class CommercialOptimizationEngine:

    def build_snapshot(
        self,
        performance: CommercialPerformanceSnapshot,
    ) -> OptimizationSnapshot:

        opportunities = self.generate_opportunities(performance)
        strategies = self.generate_strategies(opportunities)

        total_uplift = sum(
            o.estimated_revenue_uplift
            for o in opportunities
        )

        return OptimizationSnapshot(
            opportunities=opportunities,
            strategies=strategies,
            budget_recommendations=[],
            experiment_recommendations=[],
            total_estimated_revenue_uplift=total_uplift,
            active=True,
        )

    def generate_opportunities(
        self,
        performance: CommercialPerformanceSnapshot,
    ) -> list[OptimizationOpportunity]:

        opportunities: list[OptimizationOpportunity] = []

        # --------------------------------------------------
        # Product Performance
        # --------------------------------------------------

        for product in performance.product_performance:

            if product.confirmed_gross_revenue <= 0:

                opportunities.append(
                    OptimizationOpportunity(
                        product_name=product.product_name,
                        product_url=product.product_url,
                        category="PRODUCT",
                        priority=OptimizationPriority.CRITICAL,
                        title="Generate First Revenue",
                        description="Product has no confirmed commercial revenue.",
                        estimated_revenue_uplift=5000.0,
                        confidence="HIGH",
                        active=True,
                    )
                )

            elif product.confirmed_gross_revenue < 1000:

                opportunities.append(
                    OptimizationOpportunity(
                        product_name=product.product_name,
                        product_url=product.product_url,
                        category="PRODUCT",
                        priority=OptimizationPriority.MEDIUM,
                        title="Increase Product Revenue",
                        description="Commercial revenue is below expected threshold.",
                        estimated_revenue_uplift=2000.0,
                        confidence="MEDIUM",
                        active=True,
                    )
                )

        # --------------------------------------------------
        # Channel Performance
        # --------------------------------------------------

        for channel in performance.channel_performance:

            if channel.confirmed_event_count == 0:

                opportunities.append(
                    OptimizationOpportunity(
                        product_name="Revenue Channel",
                        product_url="",
                        category=channel.revenue_channel,
                        priority=OptimizationPriority.HIGH,
                        title="Activate Revenue Channel",
                        description="Revenue channel has no confirmed commercial events.",
                        estimated_revenue_uplift=3000.0,
                        confidence="HIGH",
                        active=True,
                    )
                )

        # --------------------------------------------------
        # Journey Performance
        # --------------------------------------------------

        for journey in performance.journey_performance:

            if journey.attribution_coverage < 0.75:

                opportunities.append(
                    OptimizationOpportunity(
                        product_name="Commercial Journey",
                        product_url="",
                        category="ATTRIBUTION",
                        priority=OptimizationPriority.HIGH,
                        title="Improve Attribution Coverage",
                        description="Commercial attribution coverage is below target.",
                        estimated_revenue_uplift=1500.0,
                        confidence="MEDIUM",
                        active=True,
                    )
                )

        return opportunities

    def generate_strategies(
        self,
        opportunities: list[OptimizationOpportunity],
    ) -> list[OptimizationStrategy]:

        strategies: list[OptimizationStrategy] = []

        for opportunity in opportunities:

            strategies.append(
                OptimizationStrategy(
                    strategy_name=opportunity.title,
                    category=opportunity.category,
                    priority=opportunity.priority,
                    objective=opportunity.description,
                    estimated_effort="MEDIUM",
                    estimated_revenue_uplift=opportunity.estimated_revenue_uplift,
                    confidence=opportunity.confidence,
                    active=True,
                )
            )

        return strategies