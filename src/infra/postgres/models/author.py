from uuid import UUID

from sqlalchemy import UUID as PGUUID, text
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.postgres.models.base import Base


class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    name: Mapped[str]
