import logging

from fastapi import APIRouter, FastAPI

from src.modules.books.router import router as books_router

main_router = APIRouter(prefix="/api")
main_router.include_router(books_router)

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(main_router)
