from typing import TYPE_CHECKING
from uuid import UUID
from sqlalchemy import UUID as PGUUID, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.postgres.models.base import Base

if TYPE_CHECKING:
    from src.infra.postgres.models.author import Author


class Book(Base):
    __tablename__ = "books"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    title: Mapped[str] = mapped_column()
    genre: Mapped[str] = mapped_column()

    authors: Mapped[list["Author"]] = relationship(secondary="book_author")
