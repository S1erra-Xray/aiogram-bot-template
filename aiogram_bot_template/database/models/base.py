import typing
from contextlib import asynccontextmanager

import orjson
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncAttrs,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped

from aiogram_bot_template.data.config import DB_URI

async_engine = create_async_engine(DB_URI)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


def orjson_dumps(
    v: typing.Any,
    *,
    default: typing.Callable[[typing.Any], typing.Any] | None,
) -> str:
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, default=default).decode()


class Base(AsyncAttrs, DeclarativeBase):
    pass


class BaseModel(Base):
    __abstract__ = True
    id: Mapped[int]

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in self.__table__.columns}

    @classmethod
    async def get_all(self, session: AsyncSession):
        stmt = select(self)
        objs = (await session.scalars(stmt)).all()
        session.expunge_all()
        return objs

    @classmethod
    async def get(self, session: AsyncSession, id: int):
        stmt = select(self).where(self.id == id)
        obj = await session.scalar(stmt)
        session.expunge_all()
        return obj

    @classmethod
    async def get_by(self, session: AsyncSession, **kwargs):
        stmt = select(self).where(
            and_(getattr(self, k) == v for k, v in kwargs.items())
        )
        obj = await session.scalar(stmt)
        session.expunge_all()
        return obj

    @classmethod
    async def create(self, session: AsyncSession, **kwargs):
        obj = self(**kwargs)
        session.add(obj)
        await session.flush()
        session.expunge_all()
        return obj

    @classmethod
    async def update(self, session: AsyncSession, id: int, **kwargs):
        if obj := await self.get(session, id):
            for key, value in kwargs.items():
                setattr(obj, key, value)
            await session.flush()
            session.expunge_all()
        return obj


@asynccontextmanager
async def get_session():
    async with async_session() as session:
        async with session.begin():
            yield session
