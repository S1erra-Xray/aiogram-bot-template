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
from sqlalchemy.orm import DeclarativeBase

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

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in self.__table__.columns}

    @classmethod
    async def get_all(cls, session: AsyncSession):
        stmt = select(cls)
        objs = (await session.scalars(stmt)).all()
        session.expunge_all()
        return objs

    @classmethod
    async def get(cls, session: AsyncSession, id: int):
        stmt = select(cls).where(cls.id == id)
        obj = await session.scalar(stmt)
        session.expunge_all()
        return obj

    @classmethod
    async def get_by(cls, session: AsyncSession, **kwargs):
        stmt = select(cls).where(and_(getattr(cls, k) == v for k, v in kwargs.items()))
        obj = await session.scalar(stmt)
        session.expunge_all()
        return obj

    @classmethod
    async def create(cls, session: AsyncSession, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        await session.flush()
        session.expunge_all()
        return obj

    @classmethod
    async def update(cls, session: AsyncSession, id: int, **kwargs):
        if obj := await cls.get(session, id):
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
