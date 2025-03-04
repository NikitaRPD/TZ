from typing import Sequence

from src.infra.postgres.models import Book
from src.infra.postgres.storage.base_storage import PostgresStorage


class BookStorage(PostgresStorage[Book]):
    async def create_book(self, book: Book) -> Book:
        # TODO
        ...

    async def read_books(self) -> Sequence[Book]:
        # TODO
        ...
