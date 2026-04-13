from typing import TYPE_CHECKING
from typing import Protocol
from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.infra.postgres.models import Book
from src.infra.postgres.models.author import Author
from src.infra.postgres.storage.base_storage import PostgresStorage
    

class BookCreateData(Protocol):
    title: str
    genre: str


class BookStorage(PostgresStorage[Book]):
    async def create_book(
        self, data: BookCreateData, authors: Sequence[Author]
    ) -> Book:
        book = Book(
           title=data.title,
           genre=data.genre,
           authors=authors
        )
        self._db.add(book)
        await self._db.flush()
        return book

    async def read_books(self) -> Sequence[Book]:
        stmt = select(Book).options(selectinload(Book.authors))
        return (await self._db.execute(stmt)).scalars().all()
