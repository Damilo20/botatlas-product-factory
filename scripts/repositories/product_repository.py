from scripts.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository):

    def __init__(self):
        super().__init__("COMM_Products")

    def list_products(self):
        return self.all()

    def create_product(self, fields):
        return self.create(fields)

    def update_product(self, record_id, fields):
        return self.update(record_id, fields)

    def delete_product(self, record_id):
        return self.delete(record_id)