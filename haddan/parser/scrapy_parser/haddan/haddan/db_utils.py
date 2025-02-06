""""Файл управления БД haddan."""
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declared_attr, declarative_base


load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


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


if __name__ == '__main__':
    engine = create_engine(DATABASE_URL, echo=False)
    # Base.metadata.drop_all(engine)  # - не запускать иначе пездес
    Base.metadata.create_all(engine)
