from typing import AsyncGenerator

from sqlalchemy import NullPool, create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DB_URL = 'postgresql://postgres:postgres@localhost:5432/b1_words'
# engine = create_async_engine(DB_URL, poolclass=NullPool)
engine1 = create_engine(DB_URL)
# async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
session_maker = sessionmaker(engine1, expire_on_commit=False)

