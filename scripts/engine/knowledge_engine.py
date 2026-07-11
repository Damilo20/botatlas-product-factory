class KnowledgeEngine:

    """
    Central source of truth for BotAtlas.
    """

    def get_product(self, robot_name):

        print("🧠 Querying Knowledge Engine...")

        return {
            "manufacturer": "Figure AI",
            "brand": "Figure",
            "category": "Humanoid Robot"
        }