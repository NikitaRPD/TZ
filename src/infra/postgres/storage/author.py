from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select

from src.infra.postgres.models import Author
from src.infra.postgres.storage.base_storage import PostgresStorage


class AuthorStorage(PostgresStorage[Author]):
    async def get_by_ids_for_update(self, ids: list[UUID]) -> Sequence[Author]:
        stmt = (
            select(Author)
            .where(Author.id.in_(ids))
            .with_for_update()
        )
        return (await self._db.execute(stmt)).scalars().all()
