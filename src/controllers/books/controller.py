from typing import Annotated, AsyncIterator

from fastapi import Depends

from src.controllers.base import BaseController

from src.infra.postgres.uow import PostgresUnitOfWorkDep
from src.schemas.books.read import BookResponse


class BookController(BaseController):
    async def read_books(self) -> list[BookResponse]:
        # books = await self.uow...
        ...

    async def create_book(self) -> BookResponse:
        # books = await self.uow...
        ...


async def get_controller(uow: PostgresUnitOfWorkDep) -> AsyncIterator[BookController]:
    yield BookController(uow=uow)


BookControllerDep = Annotated[BookController, Depends(get_controller)]
