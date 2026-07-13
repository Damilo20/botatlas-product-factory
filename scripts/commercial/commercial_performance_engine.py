from collections import defaultdict
from decimal import Decimal

from scripts.commercial.models.channel_performance import ChannelPerformance
from scripts.commercial.models.commercial_performance_snapshot import (
    CommercialPerformanceSnapshot,
)
from scripts.commercial.models.conversion_attribution import (
    AttributionState,
    ConversionAttribution,
)
from scripts.commercial.models.conversion_journey import ConversionJourney
from scripts.commercial.models.journey_performance import JourneyPerformance
from scripts.commercial.models.product_performance import ProductPerformance
from scripts.commercial.models.revenue_event import (
    RevenueEvent,
    RevenueEventStatus,
    RevenueEventType,
)


class CommercialPerformanceEngine:
    """
    Aggregates commercially descriptive performance metrics.

    Does not inspect evidence, resolve claims, rank products,
    assign trust, verify products, recommend products, or decide truth.
    """

    CONVERSION_EVENT_TYPES = {
        RevenueEventType.AFFILIATE_CONVERSION,
        RevenueEventType.QUALIFIED_LEAD,
        RevenueEventType.SUBSCRIPTION,
        RevenueEventType.DATA_LICENSE,
        RevenueEventType.MANUFACTURER_INTELLIGENCE,
    }

    def build_snapshot(
        self,
        revenue_events: list[RevenueEvent],
        journeys: list[ConversionJourney],
        attributions: list[ConversionAttribution],
    ) -> CommercialPerformanceSnapshot:
        active_events = [
            event
            for event in revenue_events
            if event.active
        ]

        return CommercialPerformanceSnapshot(
            total_event_count=len(active_events),
            confirmed_event_count=sum(
                event.event_status is RevenueEventStatus.CONFIRMED
                for event in active_events
            ),
            conversion_count=sum(
                self._is_conversion(event)
                for event in active_events
            ),
            confirmed_gross_revenue=self._confirmed_revenue(active_events),
            product_performance=self._product_performance(
                active_events,
                attributions,
            ),
            channel_performance=self._channel_performance(active_events),
            journey_performance=self._journey_performance(
                journeys,
                attributions,
            ),
        )

    def _product_performance(
        self,
        events: list[RevenueEvent],
        attributions: list[ConversionAttribution],
    ) -> list[ProductPerformance]:
        grouped: dict[str, list[RevenueEvent]] = defaultdict(list)

        for event in events:
            grouped[event.product_url].append(event)

        attribution_by_event = {
            attribution.revenue_event.event_reference: attribution
            for attribution in attributions
        }

        results: list[ProductPerformance] = []

        for product_url, product_events in grouped.items():
            states = [
                attribution_by_event[event.event_reference].attribution_state
                for event in product_events
                if event.event_reference in attribution_by_event
            ]

            results.append(
                ProductPerformance(
                    product_name=product_events[0].product_name,
                    product_url=product_url,
                    event_count=len(product_events),
                    confirmed_event_count=sum(
                        event.event_status is RevenueEventStatus.CONFIRMED
                        for event in product_events
                    ),
                    conversion_count=sum(
                        self._is_conversion(event)
                        for event in product_events
                    ),
                    confirmed_gross_revenue=self._confirmed_revenue(
                        product_events
                    ),
                    attributed_event_count=states.count(
                        AttributionState.ATTRIBUTED
                    ),
                    partially_attributed_event_count=states.count(
                        AttributionState.PARTIALLY_ATTRIBUTED
                    ),
                    unattributed_event_count=states.count(
                        AttributionState.UNATTRIBUTED
                    ),
                )
            )

        return results

    def _channel_performance(
        self,
        events: list[RevenueEvent],
    ) -> list[ChannelPerformance]:
        grouped = defaultdict(list)

        for event in events:
            grouped[event.revenue_channel].append(event)

        return [
            ChannelPerformance(
                revenue_channel=revenue_channel,
                event_count=len(channel_events),
                confirmed_event_count=sum(
                    event.event_status is RevenueEventStatus.CONFIRMED
                    for event in channel_events
                ),
                conversion_count=sum(
                    self._is_conversion(event)
                    for event in channel_events
                ),
                confirmed_gross_revenue=self._confirmed_revenue(
                    channel_events
                ),
            )
            for revenue_channel, channel_events in grouped.items()
        ]

    def _journey_performance(
        self,
        journeys: list[ConversionJourney],
        attributions: list[ConversionAttribution],
    ) -> JourneyPerformance:
        attributed = [
            attribution
            for attribution in attributions
            if attribution.attribution_state is AttributionState.ATTRIBUTED
        ]

        partially_attributed = [
            attribution
            for attribution in attributions
            if attribution.attribution_state
            is AttributionState.PARTIALLY_ATTRIBUTED
        ]

        unattributed = [
            attribution
            for attribution in attributions
            if attribution.attribution_state is AttributionState.UNATTRIBUTED
        ]

        converting_journey_references = {
            attribution.journey.journey_reference
            for attribution in attributed
            if attribution.journey is not None
            and self._is_conversion(attribution.revenue_event)
        }

        attribution_count = len(attributions)

        attribution_coverage = (
            Decimal(len(attributed)) / Decimal(attribution_count)
            if attribution_count
            else Decimal("0")
        )

        journey_conversion_rate = (
            Decimal(len(converting_journey_references))
            / Decimal(len(journeys))
            if journeys
            else Decimal("0")
        )

        return JourneyPerformance(
            journey_count=len(journeys),
            converting_journey_count=len(converting_journey_references),
            attributed_event_count=len(attributed),
            partially_attributed_event_count=len(partially_attributed),
            unattributed_event_count=len(unattributed),
            attribution_coverage=attribution_coverage,
            journey_conversion_rate=journey_conversion_rate,
        )

    @classmethod
    def _is_conversion(cls, event: RevenueEvent) -> bool:
        return event.event_type in cls.CONVERSION_EVENT_TYPES

    @staticmethod
    def _confirmed_revenue(
        events: list[RevenueEvent],
    ) -> Decimal:
        total = Decimal("0")

        for event in events:
            if (
                event.event_status is RevenueEventStatus.CONFIRMED
                and event.gross_amount is not None
            ):
                total += Decimal(event.gross_amount)

        return total
