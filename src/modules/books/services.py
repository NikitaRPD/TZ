from src.infra.postgres.storage.author import AuthorStorage
from src.infra.postgres.storage.book import BookStorage
from src.infra.transaction_manager import TransactionManager
from src.modules.books.schemas import BookResponse


class BookCreateInteractor:
    def __init__(
        self,
        book_storage: BookStorage,
        author_storage: AuthorStorage,
        transaction_manager: TransactionManager,
    ) -> None:
        self._book_storage = book_storage
        self._author_storage = author_storage
        self._transaction_manager = transaction_manager

    async def execute(self) -> BookResponse:
        book = await self._book_storage.create_book()
        # TODO commit and return BookResponse


class BooksListQuery:
    def __init__(self, book_storage: BookStorage) -> None:
        self._book_storage = book_storage

    async def execute(self) -> list[BookResponse]:
        books = await self._book_storage.read_books()
        # TODO return list[BookResponse]
