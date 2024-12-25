from src.infra.postgres.models import Book
from src.infra.postgres.storage.base_storage import PostgresStorage


class BookStorage(PostgresStorage[Book]):
    ...
