from scripts.config import schema_options


class ProductNormalizationEngine:

    def normalize(self, product):

        product.category = self.normalize_category(product.category)
        product.primary_use = self.normalize_primary_use(product.primary_use)
        product.industry = self.normalize_industry(product.industry)
        product.environment = self.normalize_environment(product.environment)
        product.target_user = self.normalize_target_user(product.target_user)
        product.mobility = self.normalize_mobility(product.mobility)
        product.autonomy_level = self.normalize_autonomy(product.autonomy_level)

        return product

    def normalize_category(self, value):
        return self.closest_match(value, schema_options.CATEGORIES)

    def normalize_primary_use(self, value):
        return self.closest_match(value, schema_options.PRIMARY_USES)

    def normalize_industry(self, value):
        return self.closest_match(value, schema_options.INDUSTRIES)

    def normalize_environment(self, value):
        return self.closest_match(value, schema_options.ENVIRONMENTS)

    def normalize_target_user(self, value):
        return self.closest_match(value, schema_options.TARGET_USERS)

    def normalize_mobility(self, value):
        return self.closest_match(value, schema_options.MOBILITY)

    def normalize_autonomy(self, value):
        return self.closest_match(value, schema_options.AUTONOMY)

    def closest_match(self, value, dictionary):

        if not value:
            return ""

        value = value.strip().lower()

        for key, display in dictionary.items():

            if value == key:
                return display

            if value == display.lower():
                return display

        return value.title()