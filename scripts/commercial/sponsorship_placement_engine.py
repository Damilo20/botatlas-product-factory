from scripts.commercial.models.sponsored_placement import SponsoredPlacement


class SponsorshipDisclosureError(ValueError):
    pass


class SponsorshipPlacementEngine:
    """
    Commercial visibility placement boundary.

    Sponsorship may create commercial visibility.

    Sponsorship does not modify evidence, authority assessment,
    evidence characteristics, claim reconciliation, or truth.
    """

    def __init__(self) -> None:
        self._placements: list[SponsoredPlacement] = []

    def register(self, placement: SponsoredPlacement) -> None:
        if not placement.disclosure_text.strip():
            raise SponsorshipDisclosureError(
                "Sponsored placement requires explicit disclosure"
            )

        self._placements.append(placement)

    def register_all(
        self,
        placements: list[SponsoredPlacement],
    ) -> None:
        for placement in placements:
            self.register(placement)

    def get_active_placements(
        self,
        placement_surface,
    ) -> list[SponsoredPlacement]:
        return [
            placement
            for placement in self._placements
            if placement.active
            and placement.placement_surface == placement_surface
        ]
