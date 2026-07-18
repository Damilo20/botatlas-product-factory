from pyairtable import Api
from scripts.config.settings import (
    AIRTABLE_API_KEY,
    AIRTABLE_BASE_ID,
)


class AirtableClient:
    def __init__(self):
        self.api = Api(AIRTABLE_API_KEY)
        self.base = self.api.base(AIRTABLE_BASE_ID)

    def table(self, table_name):
        return self.base.table(table_name)


airtable = AirtableClient()