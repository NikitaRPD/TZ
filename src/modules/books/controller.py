from typing import Annotated, AsyncIterator

from fastapi import Depends

from src.infra.postgres.uow import PostgresUnitOfWorkDep
from src.modules.base.controller import BaseController
from src.modules.books.schemas import BookResponse


class BookController(BaseController):
    async def read_books(self) -> list[BookResponse]:
        books = await self.uow.book.read_books()
        # TODO return list[BookResponse]

    async def create_book(self) -> BookResponse:
        book = await self.uow.book.create_book()
        # TODO return BookResponse


async def get_controller(uow: PostgresUnitOfWorkDep) -> AsyncIterator[BookController]:
    yield BookController(uow=uow)


BookControllerDep = Annotated[BookController, Depends(get_controller)]
