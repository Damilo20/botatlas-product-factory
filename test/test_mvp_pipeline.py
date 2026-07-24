"""
BotAtlas MVP Integration Test

Tests the complete Product Intelligence Pipeline from raw input
to a canonical enriched product.

This is the official Sprint 1 release gate.
"""

from scripts.commercial.product_intelligence_pipeline import (
    ProductIntelligencePipeline,
)


def test_mvp_pipeline():
    pipeline = ProductIntelligencePipeline()

    raw_product = {
        "product_name": "Unitree G1",
        "manufacturer": "Unitree Robotics",
        "category": "Humanoid Robot",
        "primary_use": "Research",
        "industry": "Education",
        "environment": "Indoor",
        "target_user": "Developers",
        "mobility": "Bipedal",
        "autonomy_level": "Semi Autonomous",
    }

    product = pipeline.process(raw_product)

    assert product is not None

    assert product.product_name == "Unitree G1"
    assert product.manufacturer == "Unitree Robotics"

    assert product.category != ""
    assert product.primary_use != ""
    assert product.industry != ""
    assert product.environment != ""
    assert product.target_user != ""
    assert product.mobility != ""
    assert product.autonomy_level != ""

    assert product.ai_version == "BotAtlas AI v1"
    assert product.last_ai_analysis != ""

    print()
    print("===================================")
    print(" BotAtlas MVP Pipeline PASSED")
    print("===================================")
    print(product)


if __name__ == "__main__":
    test_mvp_pipeline()