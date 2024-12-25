from typing import Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.postgres.models.base import Base

ModelT = TypeVar("ModelT", bound=Base)


class PostgresStorage(Generic[ModelT]):
    """Same as Repository"""

    model_cls: Type[ModelT]

    def __init__(self, db: AsyncSession) -> None:
        self._db: AsyncSession = db

