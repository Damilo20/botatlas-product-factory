from collections import defaultdict
from decimal import Decimal, InvalidOperation

from scripts.commercial.models.commercial_performance_report import (
    CommercialPerformanceReport,
)
from scripts.commercial.models.product_revenue_summary import (
    ProductRevenueSummary,
)
from scripts.commercial.models.revenue_channel_summary import (
    RevenueChannelSummary,
)
from scripts.commercial.models.revenue_event import (
    RevenueEvent,
    RevenueEventStatus,
)


class RevenueReportingEngine:
    """
    Aggregates commercial revenue events.

    Reporting consumes RevenueEvent contracts only.

    Does not verify products, resolve claims, rank evidence,
    assign trust, or alter intelligence conclusions.
    """

    @staticmethod
    def _amount(event: RevenueEvent) -> Decimal:
        if event.gross_amount is None:
            return Decimal("0")

        try:
            return Decimal(event.gross_amount)
        except (InvalidOperation, ValueError):
            return Decimal("0")

    @staticmethod
    def _events_with_status(
        events: list[RevenueEvent],
        status: RevenueEventStatus,
    ) -> list[RevenueEvent]:
        return [
            event
            for event in events
            if event.event_status is status
        ]

    def report(
        self,
        events: list[RevenueEvent],
    ) -> CommercialPerformanceReport:
        channel_events: dict[str, list[RevenueEvent]] = defaultdict(list)
        product_events: dict[
            tuple[str, str],
            list[RevenueEvent],
        ] = defaultdict(list)

        for event in events:
            channel_events[event.revenue_channel].append(event)
            product_events[
                (event.product_name, event.product_url)
            ].append(event)

        recorded = self._events_with_status(
            events,
            RevenueEventStatus.RECORDED,
        )
        pending = self._events_with_status(
            events,
            RevenueEventStatus.PENDING,
        )
        confirmed = self._events_with_status(
            events,
            RevenueEventStatus.CONFIRMED,
        )
        reversed_events = self._events_with_status(
            events,
            RevenueEventStatus.REVERSED,
        )

        return CommercialPerformanceReport(
            total_event_count=len(events),
            recorded_event_count=len(recorded),
            pending_event_count=len(pending),
            confirmed_event_count=len(confirmed),
            reversed_event_count=len(reversed_events),
            confirmed_gross_revenue=sum(
                (self._amount(event) for event in confirmed),
                Decimal("0"),
            ),
            pending_revenue=sum(
                (self._amount(event) for event in pending),
                Decimal("0"),
            ),
            reversed_revenue=sum(
                (self._amount(event) for event in reversed_events),
                Decimal("0"),
            ),
            channel_summaries=[
                self._channel_summary(channel, grouped_events)
                for channel, grouped_events in channel_events.items()
            ],
            product_summaries=[
                self._product_summary(
                    product_name,
                    product_url,
                    grouped_events,
                )
                for (
                    product_name,
                    product_url,
                ), grouped_events in product_events.items()
            ],
        )

    def _channel_summary(
        self,
        channel: str,
        events: list[RevenueEvent],
    ) -> RevenueChannelSummary:
        recorded = self._events_with_status(
            events,
            RevenueEventStatus.RECORDED,
        )
        pending = self._events_with_status(
            events,
            RevenueEventStatus.PENDING,
        )
        confirmed = self._events_with_status(
            events,
            RevenueEventStatus.CONFIRMED,
        )
        reversed_events = self._events_with_status(
            events,
            RevenueEventStatus.REVERSED,
        )

        return RevenueChannelSummary(
            revenue_channel=channel,
            event_count=len(events),
            recorded_event_count=len(recorded),
            pending_event_count=len(pending),
            confirmed_event_count=len(confirmed),
            reversed_event_count=len(reversed_events),
            confirmed_revenue=sum(
                (self._amount(event) for event in confirmed),
                Decimal("0"),
            ),
            pending_revenue=sum(
                (self._amount(event) for event in pending),
                Decimal("0"),
            ),
            reversed_revenue=sum(
                (self._amount(event) for event in reversed_events),
                Decimal("0"),
            ),
        )

    def _product_summary(
        self,
        product_name: str,
        product_url: str,
        events: list[RevenueEvent],
    ) -> ProductRevenueSummary:
        recorded = self._events_with_status(
            events,
            RevenueEventStatus.RECORDED,
        )
        pending = self._events_with_status(
            events,
            RevenueEventStatus.PENDING,
        )
        confirmed = self._events_with_status(
            events,
            RevenueEventStatus.CONFIRMED,
        )
        reversed_events = self._events_with_status(
            events,
            RevenueEventStatus.REVERSED,
        )

        return ProductRevenueSummary(
            product_name=product_name,
            product_url=product_url,
            event_count=len(events),
            recorded_event_count=len(recorded),
            pending_event_count=len(pending),
            confirmed_event_count=len(confirmed),
            reversed_event_count=len(reversed_events),
            confirmed_revenue=sum(
                (self._amount(event) for event in confirmed),
                Decimal("0"),
            ),
            pending_revenue=sum(
                (self._amount(event) for event in pending),
                Decimal("0"),
            ),
            reversed_revenue=sum(
                (self._amount(event) for event in reversed_events),
                Decimal("0"),
            ),
        )
