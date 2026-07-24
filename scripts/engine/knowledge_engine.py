from scripts.registry.knowledge_registry import (
    KnowledgeRegistry,
)


class KnowledgeEngine:
    """
    Central access point for BotAtlas knowledge.
    """

    def __init__(
        self,
        registry: KnowledgeRegistry,
    ):

        self.registry = registry

    def get_product(
        self,
        product_name: str,
        field_name: str,
    ):

        return self.registry.get(
            product_name,
            field_name,
        )

    def all_knowledge(self):

        return self.registry.all()