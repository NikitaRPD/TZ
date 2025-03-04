import uvicorn
from fastapi import FastAPI, APIRouter

from src.modules.books.router import router as books_router

app = FastAPI()

main_router = APIRouter(prefix="/api")
main_router.include_router(books_router)
app.include_router(main_router)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)