"""
BotAtlas Product Validation Engine

Ensures products contain the minimum information required
before entering the commercial database.
"""

from dataclasses import dataclass


@dataclass
class ValidationResult:
    valid: bool
    errors: list


class ProductValidationEngine:

    REQUIRED_FIELDS = [
        "product_name",
        "manufacturer",
        "category"
    ]

    def validate(self, product):

        errors = []

        for field in self.REQUIRED_FIELDS:

            value = getattr(product, field)

            if value is None or str(value).strip() == "":
                errors.append(field)

        return ValidationResult(

            valid=len(errors) == 0,

            errors=errors

        )