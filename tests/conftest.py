import os
import pytest

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.db.base import Base
from src.users.models import User

from src.core.config import settings


def get_test_db_url() -> str:
    url = settings.database_url_async
    if not url:
        raise RuntimeError("DATABASE_URL is not set for tests")
    return url


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def engine():
    engine = create_async_engine(get_test_db_url(), echo=False, future=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    await engine.dispose()


@pytest.fixture
async def db_session(engine) -> AsyncSession:
    async with engine.connect() as conn:
        trans = await conn.begin()

        Session = async_sessionmaker(
            bind=conn,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )
        session = Session()

        try:
            yield session
        finally:
            await session.close()
            await trans.rollback()
