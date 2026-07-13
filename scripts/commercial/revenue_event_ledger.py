from scripts.commercial.models.revenue_attribution import RevenueAttribution
from scripts.commercial.models.revenue_event import RevenueEvent


class DuplicateRevenueEventError(ValueError):
    pass


class RevenueEventLedger:
    """
    Append-only commercial revenue event ledger.

    The ledger records commercial events.

    It does not mutate BotAtlas intelligence.
    """

    def __init__(self) -> None:
        self._events: list[RevenueEvent] = []
        self._event_references: set[str] = set()

    def append(
        self,
        attribution: RevenueAttribution,
    ) -> None:
        event = attribution.event

        if event.event_reference in self._event_references:
            raise DuplicateRevenueEventError(
                "Revenue event reference already recorded"
            )

        self._events.append(event)
        self._event_references.add(event.event_reference)

    def append_all(
        self,
        attributions: list[RevenueAttribution],
    ) -> None:
        for attribution in attributions:
            self.append(attribution)

    def get_events(self) -> list[RevenueEvent]:
        return list(self._events)

    def get_events_for_product(
        self,
        product_url: str,
    ) -> list[RevenueEvent]:
        canonical = product_url.rstrip("/").lower()

        return [
            event
            for event in self._events
            if event.product_url.rstrip("/").lower() == canonical
        ]

    def __len__(self) -> int:
        return len(self._events)
