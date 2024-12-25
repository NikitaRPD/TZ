from src.infra.postgres.models import Author
from src.infra.postgres.storage.base_storage import PostgresStorage


class AuthorStorage(PostgresStorage[Author]):
    ...
