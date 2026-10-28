from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from sqlalchemy.orm import DeclarativeBase
from app.config import Settings

engine=create_async_engine(
    Settings.DATABASE_URL,
    connect_args={"check_same_thread":False},
    echo=True,
)

AsyncSessionLocal=async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass

async def get_db()->AsyncGenerator[AsyncSession,None]:
    async with AsyncSessionLocal as session:
        yield session
        