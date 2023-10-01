from typing import AsyncGenerator

from sqlalchemy import NullPool, create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

Base = declarative_base()

DB_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
# engine = create_async_engine(DB_URL, poolclass=NullPool)
engine1 = create_engine(DB_URL)
# async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
session_maker = sessionmaker(engine1, expire_on_commit=False)

