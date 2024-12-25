from asyncio import current_task
from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from src.app_config import app_config

connect_args = {
    "server_settings": {
        "jit": "off",
        "statement_timeout": "30000",
    }
}

engine: AsyncEngine = create_async_engine(
    app_config.uri,
    echo=False,
    echo_pool=False,
    connect_args=connect_args,
    poolclass=AsyncAdaptedQueuePool,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=3600,
)

async_session_factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
session: async_scoped_session[AsyncSession] = async_scoped_session(
    session_factory=async_session_factory,
    scopefunc=current_task,
)


@asynccontextmanager
async def get_db() -> AsyncIterator[AsyncSession]:
    async with session() as db:
        try:
            yield db
            await db.commit()
        except Exception as error:
            await db.rollback()
            raise error
        finally:
            await db.close()
