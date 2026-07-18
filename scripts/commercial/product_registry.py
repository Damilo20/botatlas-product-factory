from scripts.commercial.base_repository import BaseRepository


class ProductRegistry(BaseRepository):
    """
    Handles all COMM_Products operations.
    """

    def __init__(self):
        super().__init__("COMM_Products")

    def list_products(self):
        """Return all products."""
        return self.all()

    def get_product(self, record_id):
        """Return one product."""
        return self.get(record_id)

    def create_product(self, fields):
        """Create a new product."""
        return self.create(fields)

    def update_product(self, record_id, fields):
        """Update an existing product."""
        return self.update(record_id, fields)

    def delete_product(self, record_id):
        """Delete a product."""
        return self.delete(record_id)

    def find_by_name(self, product_name):
        """
        Find a product by its Product Name.
        """
        formula = f"{{Product Name}}='{product_name}'"
        return self.first(formula=formula)