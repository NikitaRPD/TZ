from uuid import UUID

from sqlalchemy import UUID as PGUUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.postgres.models.base import Base


class BookAuthor(Base):
    __tablename__ = "book_author"

    book_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("books.id", ondelete="CASCADE"),
        primary_key=True,
    )
    author_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("authors.id", ondelete="CASCADE"),
        primary_key=True,
    )
