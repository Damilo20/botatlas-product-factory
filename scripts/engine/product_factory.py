from scripts.agents.research_agent import ResearchAgent
from scripts.agents.technical_agent import TechnicalAgent
from scripts.agents.pricing_agent import PricingAgent
from scripts.agents.verification_agent import VerificationAgent

from scripts.engine.product_repository import ProductRepository
from scripts.engine.identity_engine import IdentityEngine
from scripts.engine.claim_engine import ClaimEngine
from scripts.engine.claim_resolver import ClaimResolver
from scripts.engine.truth_applicator import TruthApplicator

class ProductFactory:
    """
    Main BotAtlas Product Factory.

    Coordinates every AI agent responsible
    for creating a complete product profile.
    """

    def __init__(self):
        self.research = ResearchAgent()
        self.technical = TechnicalAgent()
        self.pricing = PricingAgent()
        self.verification = VerificationAgent()

        self.identity = IdentityEngine()
        self.repository = ProductRepository()

        self.claim_engine = ClaimEngine()
        self.claim_resolver = ClaimResolver()
        self.truth_applicator = TruthApplicator()

    def build_product(self, robot_name: str):

        print("=" * 50)
        print("BOTATLAS PRODUCT FACTORY")
        print("=" * 50)

        product = self.research.research(robot_name)
        product = self.technical.enrich(product)
        product = self.pricing.enrich(product)

        # Layer 4 — Intelligence Graph
        claims = self.claim_engine.build_claims(product.evidence)
        product.claims = claims

        selected_claims = self.claim_resolver.resolve(product.claims)
        product = self.truth_applicator.apply(product, selected_claims)

        product.product_id = self.identity.generate_product_id(
            product_name=product.product_name,
            manufacturer=product.manufacturer,
            model=product.model,
        )

        product = self.verification.enrich(product)

        self.repository.save(product)

        print()

        print("✓ Product Created")

        print(product)

        return product