from uuid import UUID, uuid4

from sqlalchemy import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.postgres.models.base import Base


class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str]
