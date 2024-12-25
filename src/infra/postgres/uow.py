from typing import Annotated, AsyncIterator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.postgres.pg import get_db
from src.infra.postgres.storage.author import AuthorStorage
# from src.infra.postgres.storage.book import BookStorage


class PostgresUnitOfWork:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db
        self.author = AuthorStorage(self.db)
        # self.book = BookStorage(self.db)


async def get_uow() -> AsyncIterator[PostgresUnitOfWork]:
    async with get_db() as db:
        yield PostgresUnitOfWork(db)


PostgresUnitOfWorkDep = Annotated[PostgresUnitOfWork, Depends(get_uow)]
