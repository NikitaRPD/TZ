from uuid import UUID

from src.schemas.books.base import BookBase


class BookResponse(BookBase):
    id: UUID
