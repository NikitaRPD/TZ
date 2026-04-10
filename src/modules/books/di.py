from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.postgres.pg import get_db
from src.infra.postgres.storage.author import AuthorStorage
from src.infra.postgres.storage.book import BookStorage
from src.infra.transaction_manager import TransactionManager
from src.modules.books.services import BookCreateInteractor, BooksListQuery


# infra
def _get_transaction_manager(db: "SessionDep") -> TransactionManager:
    return TransactionManager(db)


def _get_author_storage(db: "SessionDep") -> AuthorStorage:
    return AuthorStorage(db)


def _get_book_storage(db: "SessionDep") -> BookStorage:
    return BookStorage(db)


# services
def _get_list_books_query(book_storage: "BookStorageDep") -> BooksListQuery:
    return BooksListQuery(book_storage=book_storage)


def _get_create_book_interactor(
    book_storage: "BookStorageDep",
    author_storage: "AuthorStorageDep",
    transaction_manager: "TransactionManagerDep",
) -> BookCreateInteractor:
    return BookCreateInteractor(
        book_storage=book_storage,
        author_storage=author_storage,
        transaction_manager=transaction_manager,
    )


# infra
SessionDep = Annotated[AsyncSession, Depends(get_db)]

TransactionManagerDep = Annotated[TransactionManager, Depends(_get_transaction_manager)]
BookStorageDep = Annotated[BookStorage, Depends(_get_book_storage)]
AuthorStorageDep = Annotated[AuthorStorage, Depends(_get_author_storage)]

# services
BookCreateInteractorDep = Annotated[BookCreateInteractor, Depends(_get_create_book_interactor)]
BooksListQueryDep = Annotated[BooksListQuery, Depends(_get_list_books_query)]
