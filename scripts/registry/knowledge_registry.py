from scripts.models.knowledge_record import (
    KnowledgeRecord,
)


class KnowledgeRegistry:
    """
    In-memory registry for canonical knowledge.

    This will later be backed by a database.
    """

    def __init__(self):

        self._records: dict[
            tuple[str, str],
            KnowledgeRecord,
        ] = {}

    def register(
        self,
        record: KnowledgeRecord,
    ):

        key = (
            record.parent_candidate_name,
            record.field_name,
        )

        self._records[key] = record

    def get(
        self,
        product_name: str,
        field_name: str,
    ) -> KnowledgeRecord | None:

        return self._records.get(
            (
                product_name,
                field_name,
            )
        )

    def all(self):

        return list(self._records.values())