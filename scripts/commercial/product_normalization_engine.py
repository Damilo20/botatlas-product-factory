from scripts.config import schema_options
from scripts.models.product import Product


class ProductNormalizationEngine:
    """
    Normalizes product taxonomy values into BotAtlas canonical values.

    Responsibilities
    ----------------
    - Normalize category
    - Normalize primary use
    - Normalize industry
    - Normalize environment
    - Normalize target user
    - Normalize mobility
    - Normalize autonomy level

    Non-Responsibilities
    --------------------
    - Product enrichment
    - Truth resolution
    - Evidence processing
    - Product persistence
    """

    def normalize(
        self,
        product: Product,
    ) -> Product:

        product.category = self.normalize_category(product.category)
        product.primary_use = self.normalize_primary_use(product.primary_use)
        product.industry = self.normalize_industry(product.industry)
        product.environment = self.normalize_environment(product.environment)
        product.target_user = self.normalize_target_user(product.target_user)
        product.mobility = self.normalize_mobility(product.mobility)
        product.autonomy_level = self.normalize_autonomy(
            product.autonomy_level
        )

        return product

    def normalize_category(
        self,
        value: str,
    ) -> str:
        return self._canonicalize(
            value,
            schema_options.CATEGORIES,
        )

    def normalize_primary_use(
        self,
        value: str,
    ) -> str:
        return self._canonicalize(
            value,
            schema_options.PRIMARY_USES,
        )

    def normalize_industry(
        self,
        value: str,
    ) -> str:
        return self._canonicalize(
            value,
            schema_options.INDUSTRIES,
        )

    def normalize_environment(
        self,
        value: str,
    ) -> str:
        return self._canonicalize(
            value,
            schema_options.ENVIRONMENTS,
        )

    def normalize_target_user(
        self,
        value: str,
    ) -> str:
        return self._canonicalize(
            value,
            schema_options.TARGET_USERS,
        )

    def normalize_mobility(
        self,
        value: str,
    ) -> str:
        return self._canonicalize(
            value,
            schema_options.MOBILITY,
        )

    def normalize_autonomy(
        self,
        value: str,
    ) -> str:
        return self._canonicalize(
            value,
            schema_options.AUTONOMY,
        )

    def _canonicalize(
        self,
        value: str,
        options: dict[str, str],
    ) -> str:
        """
        Convert an input value into the BotAtlas canonical value.

        If no canonical match exists, return a normalized title-cased value.
        """

        if not value:
            return ""

        normalized = value.strip().lower()

        for key, display in options.items():

            if normalized == key.lower():
                return display

            if normalized == display.lower():
                return display

        return value.strip().title()