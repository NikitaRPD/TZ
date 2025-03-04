from uuid import UUID

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    authors: list[UUID]
    publication_year: int
    pages: int
    genre: str


class BookCreateRequest(BookBase):
    ...

class BookResponse(BookBase):
    id: UUID
