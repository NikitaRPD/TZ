from fastapi import APIRouter

from src.controllers.books.controller import BookControllerDep
from src.schemas.books.read import BookResponse

router = APIRouter(prefix="/books")


@router.get("/")
async def get(controller: BookControllerDep) -> list[BookResponse]:
    return await controller.read_books()


@router.post("/")
async def post() -> BookResponse:
    pass