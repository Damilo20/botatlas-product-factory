from scripts.models.product import Product
from scripts.models.research_result import ResearchResult
from scripts.models.evidence import Evidence

class ResearchAgent:
    """
    BotAtlas Product Identity Research Agent.

    Responsible for identifying the canonical identity
    of a robot before downstream enrichment begins.
    """

    def research_identity(self, robot_name: str) -> ResearchResult:

        print(f"🔎 Resolving product identity for {robot_name}...")

        normalized_name = robot_name.strip()

        # Temporary deterministic identity knowledge.
        # This will later be replaced by live research providers.
        known_products = {
            "figure ai figure 02": ResearchResult(
                product_name="Figure 02",
                manufacturer="Figure AI, Inc.",
                brand="Figure",
                model="02",
                category="Humanoid Robot",
                official_url="https://www.figure.ai/",
                confidence_score=95.0,
                sources=[
                    "Official Figure AI product identity"
                ],
            )
        }

        result = known_products.get(normalized_name.lower())

        if result:
            return result

        return ResearchResult(
            product_name=normalized_name,
            confidence_score=10.0,
            warnings=[
                "Canonical product identity could not be resolved."
            ],
        )

    def research(self, robot_name: str) -> Product:

        result = self.research_identity(robot_name)

        product = Product(
            product_id="TEMP-001",
            product_name=result.product_name,
            manufacturer=result.manufacturer,
            brand=result.brand,
            model=result.model,
            category=result.category,
            official_url=result.official_url,
            confidence_score=result.confidence_score,
        )

        product.sources.extend(result.sources)
        product.warnings.extend(result.warnings)

        if result.official_url:

            identity_claims = {
                "product_name": result.product_name,
                "manufacturer": result.manufacturer,
                "brand": result.brand,
                "model": result.model,
                "category": result.category,
            }

            for field_name, claimed_value in identity_claims.items():

                if claimed_value is not None:

                    product.evidence.append(
                        Evidence(
                            field_name=field_name,
                            claimed_value=str(claimed_value),
                            source_name="Official Figure AI Website",
                            source_url=result.official_url,
                            source_type="MANUFACTURER",
                            confidence_score=result.confidence_score / 100.0,
                            verified=True,
                        )
                    )

        return product