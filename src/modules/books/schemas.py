from uuid import UUID
from pydantic import BaseModel, field_validator


class BookBase(BaseModel):
    title: str
    authors: list[UUID]
    genre: str 

    @field_validator('authors')
    @classmethod
    def authors_validator(cls, v: list[UUID]) -> list[UUID]:
        if len(v) != len(set(v)):
            raise ValueError('The list of authors must contain unique IDs')
        return v

class BookCreateRequest(BookBase):
    ...

class BookResponse(BookBase):
    id: UUID
