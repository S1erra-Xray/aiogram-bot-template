import typing
from contextlib import asynccontextmanager

import orjson
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncAttrs,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped

from aiogram_bot_template.data.config import DB_URI


async_engine = create_async_engine(DB_URI, echo=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


def orjson_dumps(
    v: typing.Any,
    *,
    default: typing.Callable[[typing.Any], typing.Any] | None,
) -> str:
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, default=default).decode()


class Base(AsyncAttrs, DeclarativeBase):
    @asynccontextmanager
    async def _get_session(self) -> typing.AsyncGenerator:
        async with async_session() as session:
            async with session.begin():
                yield session


class BaseModel(Base):
    __abstract__ = True
    id: Mapped[int]

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in self.__table__.columns}

    @classmethod
    async def get_all(cls):
        stmt = select(cls)
        async with cls._get_session() as session:
            objs = (await session.scalars(stmt)).all()
            session.expunge_all()
        return objs

    @classmethod
    async def get(cls, id: int):
        stmt = select(cls).where(cls.id == id)
        async with cls._get_session() as session:
            obj = await session.scalar(stmt)
            session.expunge_all()
        return obj

    @classmethod
    async def get_by(cls, **kwargs):
        stmt = select(cls).where(and_(getattr(cls, k) == v for k, v in kwargs.items()))
        async with cls._get_session() as session:
            obj = await session.scalar(stmt)
            session.expunge_all()
        return obj

    @classmethod
    async def create(cls, **kwargs):
        obj = cls(**kwargs)
        async with cls._get_session() as session:
            await session.add(obj)
            await session.flush()
            await session.expunge_all()
        return obj

    @classmethod
    async def update(cls, id: int, **kwargs):
        if obj := await cls.get(id):
            for key, value in kwargs.items():
                setattr(obj, key, value)
            async with cls._get_session() as session:
                await session.flush()
                await session.expunge_all()
        return obj

    def __repr__(self, **kwargs):
        return f"{self.__class__.__name__}({kwargs})"
