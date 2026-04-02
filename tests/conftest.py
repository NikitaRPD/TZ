import os

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.app_config import app_config

APP_URL = os.getenv("APP_URL", "http://localhost:8000")

AUTHOR_1 = "11111111-1111-1111-1111-111111111111"
AUTHOR_2 = "22222222-2222-2222-2222-222222222222"


@pytest_asyncio.fixture(autouse=True)
async def setup_and_cleanup():
    engine = create_async_engine(app_config.uri)
    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with session_factory() as session:
        await session.execute(
            text(
                "INSERT INTO authors (id, name) VALUES (:id1, :name1), (:id2, :name2) "
                "ON CONFLICT (id) DO NOTHING"
            ),
            {"id1": AUTHOR_1, "name1": "Author One", "id2": AUTHOR_2, "name2": "Author Two"},
        )
        await session.commit()

    yield

    async with session_factory() as session:
        await session.execute(text("TRUNCATE books CASCADE"))
        await session.commit()

    await engine.dispose()


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(base_url=APP_URL, timeout=10.0) as c:
        yield c
