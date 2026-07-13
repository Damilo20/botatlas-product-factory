from scripts.commercial.models.conversion_attribution import (
    AttributionState,
    ConversionAttribution,
)
from scripts.commercial.models.conversion_journey import ConversionJourney
from scripts.commercial.models.revenue_event import RevenueEvent


class ConversionAttributionEngine:
    """
    Attributes revenue events to commercial journeys.

    Attribution is based on explicit commercial identity signals.

    Does not rank products, inspect evidence quality, resolve claims,
    assign trust, verify products, or decide truth.
    """

    def attribute(
        self,
        revenue_event: RevenueEvent,
        journeys: list[ConversionJourney],
    ) -> ConversionAttribution:
        product_matches = [
            journey
            for journey in journeys
            if journey.product_url == revenue_event.product_url
        ]

        if not product_matches:
            return ConversionAttribution(
                revenue_event=revenue_event,
                journey=None,
                attribution_state=AttributionState.UNATTRIBUTED,
                matched_product_url=False,
                matched_commercial_reference=False,
                attribution_method="NO_COMMERCIAL_IDENTITY_MATCH",
            )

        commercial_matches = [
            journey
            for journey in product_matches
            if self._matches_commercial_reference(
                revenue_event,
                journey,
            )
        ]

        if len(commercial_matches) == 1:
            return ConversionAttribution(
                revenue_event=revenue_event,
                journey=commercial_matches[0],
                attribution_state=AttributionState.ATTRIBUTED,
                matched_product_url=True,
                matched_commercial_reference=True,
                attribution_method="PRODUCT_URL_AND_COMMERCIAL_REFERENCE",
            )

        if len(product_matches) == 1:
            return ConversionAttribution(
                revenue_event=revenue_event,
                journey=product_matches[0],
                attribution_state=AttributionState.PARTIALLY_ATTRIBUTED,
                matched_product_url=True,
                matched_commercial_reference=False,
                attribution_method="CANONICAL_PRODUCT_URL",
            )

        return ConversionAttribution(
            revenue_event=revenue_event,
            journey=None,
            attribution_state=AttributionState.PARTIALLY_ATTRIBUTED,
            matched_product_url=True,
            matched_commercial_reference=False,
            attribution_method="AMBIGUOUS_PRODUCT_JOURNEY",
        )

    def attribute_all(
        self,
        revenue_events: list[RevenueEvent],
        journeys: list[ConversionJourney],
    ) -> list[ConversionAttribution]:
        return [
            self.attribute(revenue_event, journeys)
            for revenue_event in revenue_events
        ]

    @staticmethod
    def _matches_commercial_reference(
        revenue_event: RevenueEvent,
        journey: ConversionJourney,
    ) -> bool:
        if revenue_event.commercial_reference is None:
            return False

        return any(
            touchpoint.commercial_reference
            == revenue_event.commercial_reference
            for touchpoint in journey.touchpoints
        )
