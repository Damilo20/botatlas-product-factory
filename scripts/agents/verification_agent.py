from scripts.models.product import Product


class VerificationAgent:
    """
    BotAtlas Product Verification Agent.

    Evaluates product completeness, source coverage,
    and trust before assigning verification status.
    """

    def enrich(self, product: Product) -> Product:

        print("🔐 Verifying product intelligence...")

        product.warnings.clear()
        product.notes.clear()

        score = 0.0

        # --------------------------------
        # Identity verification
        # --------------------------------

        identity_fields = [
            product.product_name,
            product.manufacturer,
            product.brand,
            product.model,
            product.category,
        ]

        identity_score = sum(
            1 for value in identity_fields if value
        ) / len(identity_fields)

        score += identity_score * 25

        # --------------------------------
        # Technical verification
        # --------------------------------

        technical_fields = [
            product.weight,
            product.runtime,
            product.battery,
            product.connectivity,
        ]

        technical_score = sum(
            1 for value in technical_fields if value
        ) / len(technical_fields)

        score += technical_score * 25

        # --------------------------------
        # Pricing verification
        # --------------------------------

        pricing_fields = [
            product.msrp,
            product.current_price,
            product.currency,
        ]

        pricing_score = sum(
            1 for value in pricing_fields if value is not None
        ) / len(pricing_fields)

        score += pricing_score * 20

        # --------------------------------
        # Source verification
        # --------------------------------

        if product.official_url:
            score += 20

            if product.official_url not in product.sources:
                product.sources.append(product.official_url)
        else:
            product.warnings.append(
                "Official manufacturer source has not been attached."
            )

        # --------------------------------
        # Content verification
        # --------------------------------

        content_fields = [
            product.description,
            product.ai_summary,
        ]

        content_score = sum(
            1 for value in content_fields if value
        ) / len(content_fields)

        score += content_score * 10

        # --------------------------------
        # Final trust classification
        # --------------------------------

        product.confidence_score = round(score, 1)
        product.quality_score = round(score, 1)

        if score >= 90 and product.official_url:
            product.verification_status = "Verified"

        elif score >= 70:
            product.verification_status = "Partially Verified"

        elif score >= 40:
            product.verification_status = "Needs Review"

        else:
            product.verification_status = "Unverified"

        product.notes.append(
            "Product record processed by BotAtlas Verification Agent."
        )

        return product