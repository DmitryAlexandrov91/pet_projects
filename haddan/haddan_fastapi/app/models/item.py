from sqlalchemy import Column, String

from app.core.db import Base


class Item(Base):
    """Модель предмета"""
    part_number = Column(String, unique=True)
    name = Column(String)
    type = Column(String)
    href = Column(String, unique=True)
