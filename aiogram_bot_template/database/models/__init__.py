import asyncio

from .base import async_engine, async_session, Base
from .user import User


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(create_tables())
