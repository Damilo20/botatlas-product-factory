from scripts.commercial.models.revenue_event import RevenueEvent
from scripts.commercial.models.revenue_attribution import RevenueAttribution


class RevenueAttributionEngine:
    """
    Attributes commercial revenue events to product identity.

    Attribution describes where a commercial event belongs.

    It does not rank evidence, verify products, resolve claims,
    assign trust, or decide truth.
    """

    def attribute(
        self,
        event: RevenueEvent,
    ) -> RevenueAttribution:
        attribution_key = event.product_url.rstrip("/").lower()

        if not attribution_key:
            raise ValueError(
                "Revenue event requires canonical product identity"
            )

        return RevenueAttribution(
            event=event,
            product_name=event.product_name,
            product_url=event.product_url,
            attribution_key=attribution_key,
            attribution_method="CANONICAL_PRODUCT_URL",
        )

    def attribute_all(
        self,
        events: list[RevenueEvent],
    ) -> list[RevenueAttribution]:
        return [
            self.attribute(event)
            for event in events
        ]
