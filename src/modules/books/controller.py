from collections.abc import AsyncIterator
from typing import Annotated

from fastapi import Depends

from src.infra.postgres.uow import PostgresUnitOfWorkDep
from src.modules.base.controller import BaseController
from src.modules.books.errors import AuthorsNotFoundError
from src.modules.books.schemas import BookCreateRequest, BookResponse


class BookController(BaseController):
    async def read_books(self) -> list[BookResponse]:
        books = await self.uow.book.read_books()
        return [
            BookResponse(
                id=book.id,
                title=book.title,
                genre=book.genre,
                authors=[author.id for author in book.authors]
            )
            for book in books
        ]

    async def create_book(self, data: BookCreateRequest) -> BookResponse:
        authors = await self.uow.author.get_by_ids_for_update(data.authors)

        if len(authors) != len(data.authors):
            found_ids = {a.id for a in authors}
            raise AuthorsNotFoundError(
                missing_ids=[i for i in data.authors if i not in found_ids]
            )

        book = await self.uow.book.create_book(data, authors)

        return BookResponse(
            id=book.id,
            title=book.title,
            genre=book.genre,
            authors=[author.id for author in authors]
        )


async def get_controller(uow: PostgresUnitOfWorkDep) -> AsyncIterator[BookController]:
    yield BookController(uow=uow)


BookControllerDep = Annotated[BookController, Depends(get_controller)]
