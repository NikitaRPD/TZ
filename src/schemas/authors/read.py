from uuid import UUID

from src.schemas.authors.base import AuthorBase


class AuthorResponse(AuthorBase):
    id: UUID
