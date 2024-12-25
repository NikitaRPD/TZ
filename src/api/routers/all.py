from fastapi import APIRouter

from src.api.routers.books.router import router

main_router = APIRouter(prefix="/api")
main_router.include_router(router)
