from scripts.integrations.airtable_client import airtable


class BaseRepository:
    """
    Base repository for all Airtable tables.
    Provides generic CRUD operations.
    """

    def __init__(self, table_name):
        self.table = airtable.table(table_name)

    def all(self):
        return self.table.all()

    def get(self, record_id):
        return self.table.get(record_id)

    def create(self, fields):
        return self.table.create(fields)

    def update(self, record_id, fields):
        return self.table.update(record_id, fields)

    def delete(self, record_id):
        return self.table.delete(record_id)