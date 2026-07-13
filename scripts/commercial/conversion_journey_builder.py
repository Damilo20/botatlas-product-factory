from collections import defaultdict

from scripts.commercial.models.conversion_journey import ConversionJourney
from scripts.commercial.models.conversion_touchpoint import ConversionTouchpoint


class ConversionJourneyBuilder:
    """
    Builds commercial journeys from explicit touchpoints.

    Groups only by journey reference and preserves commercial product identity.

    Does not inspect evidence, resolve claims, assign trust, or decide truth.
    """

    def build(
        self,
        touchpoints: list[ConversionTouchpoint],
    ) -> list[ConversionJourney]:
        grouped: dict[str, list[ConversionTouchpoint]] = defaultdict(list)

        for touchpoint in touchpoints:
            if touchpoint.active:
                grouped[touchpoint.journey_reference].append(touchpoint)

        journeys: list[ConversionJourney] = []

        for journey_reference, journey_touchpoints in grouped.items():
            ordered = sorted(
                journey_touchpoints,
                key=lambda touchpoint: touchpoint.occurred_at,
            )

            product_urls = {
                touchpoint.product_url
                for touchpoint in ordered
            }

            product_names = {
                touchpoint.product_name
                for touchpoint in ordered
            }

            if len(product_urls) != 1 or len(product_names) != 1:
                raise ValueError(
                    "Conversion journey cannot collapse multiple product identities"
                )

            journeys.append(
                ConversionJourney(
                    journey_reference=journey_reference,
                    product_name=ordered[0].product_name,
                    product_url=ordered[0].product_url,
                    touchpoints=ordered,
                )
            )

        return journeys
