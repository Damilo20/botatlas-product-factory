import hashlib
import re


class IdentityEngine:
    """
    BotAtlas Product Identity Engine.

    Generates stable BotAtlas product identifiers.
    """

    PREFIX = "BA"

    def generate_product_id(
        self,
        product_name: str,
        manufacturer: str | None = None,
        model: str | None = None,
    ) -> str:

        manufacturer_code = self._normalize(
            manufacturer or "UNKNOWN"
        )

        model_code = self._normalize(
            model or product_name
        )

        identity_source = "|".join([
            manufacturer or "UNKNOWN",
            model or "UNKNOWN",
            product_name,
        ]).lower()

        identity_hash = hashlib.sha256(
            identity_source.encode("utf-8")
        ).hexdigest()[:8].upper()

        return (
            f"{self.PREFIX}-"
            f"{manufacturer_code[:10]}-"
            f"{model_code[:15]}-"
            f"{identity_hash}"
        )

    def _normalize(self, value: str) -> str:
        """
        Convert identity text into a safe ID segment.
        """

        value = value.upper()
        value = re.sub(r"[^A-Z0-9]+", "-", value)

        return value.strip("-")