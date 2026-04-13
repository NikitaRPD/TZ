import logging

from fastapi import APIRouter, FastAPI

from src.infra.http.exception_handlers import register_exception_handlers
from src.modules.books.router import router as books_router

main_router = APIRouter(prefix="/api")
main_router.include_router(books_router)

logger = logging.getLogger(__name__)

app = FastAPI()
register_exception_handlers(app)
app.include_router(main_router)
