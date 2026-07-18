from scripts.commercial.base_repository import BaseRepository


class RevenueEventEngine(BaseRepository):
    """
    Handles all COMM_RevenueEvents operations.
    """

    def __init__(self):
        super().__init__("COMM_RevenueEvents")

    def record_event(self, fields):
        """
        Create a new revenue event.
        """
        return self.create(fields)

    def list_events(self):
        """
        Return all revenue events.
        """
        return self.all()

    def get_event(self, record_id):
        """
        Return one revenue event.
        """
        return self.get(record_id)

    def update_event(self, record_id, fields):
        """
        Update a revenue event.
        """
        return self.update(record_id, fields)

    def delete_event(self, record_id):
        """
        Delete a revenue event.
        """
        return self.delete(record_id)

    def events_for_product(self, product_record_id):
        """
        Return all events belonging to one product.
        """
        formula = f"{{product}}='{product_record_id}'"
        return self.table.all(formula=formula)

    def total_gross_revenue(self):
        """
        Sum gross revenue.
        """
        total = 0

        for record in self.all():
            value = record["fields"].get("gross_revenue", 0)
            total += float(value)

        return total

    def total_confirmed_revenue(self):
        """
        Sum confirmed revenue.
        """
        total = 0

        for record in self.all():
            value = record["fields"].get("confirmed_revenue", 0)
            total += float(value)

        return total

    def total_conversions(self):
        """
        Sum conversion count.
        """
        total = 0

        for record in self.all():
            value = record["fields"].get("conversion_count", 0)
            total += int(value)

        return total