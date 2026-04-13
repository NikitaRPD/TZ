from uuid import UUID
from collections.abc import Sequence
from sqlalchemy import select

from src.infra.postgres.models import Author
from src.infra.postgres.storage.base_storage import PostgresStorage


class AuthorStorage(PostgresStorage[Author]):
    async def get_by_ids(self, ids: list[UUID]) -> Sequence[Author]:
        result = await self._db.execute(
            select(Author).where(Author.id.in_(ids))
        )
        return result.scalars().all()
