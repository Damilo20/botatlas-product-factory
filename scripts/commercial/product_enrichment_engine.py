"""
BotAtlas Product Enrichment Engine

Adds intelligence and derived metadata to a normalized product.

Responsibilities
----------------
- Record enrichment metadata
- Track AI enrichment version
- Prepare products for future AI enhancements

Future Responsibilities
-----------------------
- AI-generated summaries
- SEO metadata
- Product DNA
- Market positioning
- Competitor analysis
- Feature extraction
- Keyword generation

Non-Responsibilities
--------------------
- Evidence retrieval
- Truth resolution
- Product normalization
- Product persistence
"""

from datetime import datetime

from scripts.models.product import Product


class ProductEnrichmentEngine:
    """
    Enriches canonical products with derived intelligence.
    """

    AI_VERSION = "BotAtlas AI v1"

    def enrich(
        self,
        product: Product,
    ) -> Product:
        """
        Enrich a normalized product.

        Current MVP:
        - Record enrichment timestamp
        - Record AI version
        """

        product.last_ai_analysis = datetime.utcnow().isoformat()
        product.ai_version = self.AI_VERSION

        return product