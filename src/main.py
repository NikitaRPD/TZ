import logging
from contextlib import asynccontextmanager
from uuid import UUID

import uvicorn
from fastapi import FastAPI, APIRouter
from sqlalchemy import select

from src.modules.books.router import router as books_router
from src.infra.postgres.models.author import Author
from src.infra.postgres.pg import get_db

main_router = APIRouter(prefix="/api")
main_router.include_router(books_router)

logger = logging.getLogger(__name__)

STARTUP_AUTHORS = [
    (UUID("11111111-1111-1111-1111-111111111111"), "Author One"),
    (UUID("22222222-2222-2222-2222-222222222222"), "Author Two"),
]


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with get_db() as db:
        author_ids = [author_id for author_id, _ in STARTUP_AUTHORS]
        existing = await db.execute(select(Author).where(Author.id.in_(author_ids)))
        existing_authors = {author.id: author for author in existing.scalars().all()}

        new_authors = [
            Author(id=author_id, name=name)
            for author_id, name in STARTUP_AUTHORS
            if author_id not in existing_authors
        ]
        if new_authors:
            db.add_all(new_authors)
            await db.flush()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(main_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
