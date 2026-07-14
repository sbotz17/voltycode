from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings


def normalize_database_url(url: str) -> str:
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+asyncpg://", 1)

    if url.startswith("postgres://"):
        return url.replace("postgres://", "postgresql+asyncpg://", 1)

    return url


engine = None
AsyncSessionFactory = None

if settings.database_url:
    engine = create_async_engine(
        normalize_database_url(settings.database_url),
        pool_pre_ping=True,
        echo=settings.debug,
    )

    AsyncSessionFactory = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )


async def get_db_session() -> AsyncGenerator[AsyncSession]:
    if AsyncSessionFactory is None:
        raise RuntimeError("DATABASE_URL non configurato")

    async with AsyncSessionFactory() as session:
        yield session
