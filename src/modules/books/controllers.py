from fastapi import APIRouter

from src.modules.books.di import BookCreateInteractorDep, BooksListQueryDep
from src.modules.books.schemas import BookCreateRequest, BookResponse

router = APIRouter(prefix="/books")


@router.get("/")
async def get(query: BooksListQueryDep) -> list[BookResponse]:
    return await query.execute()


@router.post("/")
async def post(body: BookCreateRequest, interactor: BookCreateInteractorDep) -> BookResponse:
    return await interactor.execute(body)
