from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from .config import settings


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class Thing(Base):
    """Модель вещей игроков."""
    name = Column(String)
    type = Column(String(200))
    serial_number = Column(String, unique=True)
    part_number = Column(String)
    owner = Column(String, nullable=True)
    href = Column(String, unique=True)


class Item(Base):
    """Модель предмета"""
    part_number = Column(String, unique=True)
    name = Column(String)
    type = Column(String)
    href = Column(String, unique=True)


database_url = (f'postgresql+psycopg2://{settings.postgres_user}:'
                f'{settings.postgres_password}@'
                f'{settings.db_host}:{settings.db_port}/{settings.db_name}')

engine = create_async_engine(database_url)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
