from scripts.models.claim import Claim
from scripts.models.product import Product


class TruthApplicator:
    """
    Applies resolved BotAtlas claims to a Product object.

    Only selected claims are allowed to modify product fields.
    """

    def apply(
        self,
        product: Product,
        claims: list[Claim],
    ) -> Product:
        for claim in claims:
            if not claim.selected:
                continue

            if not hasattr(product, claim.field_name):
                product.warnings.append(
                    f"Unknown product field: {claim.field_name}"
                )
                continue

            value = (
                claim.normalized_value
                if claim.normalized_value is not None
                else claim.claimed_value
            )

            setattr(product, claim.field_name, value)

        return product