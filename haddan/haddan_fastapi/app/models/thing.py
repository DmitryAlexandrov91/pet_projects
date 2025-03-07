from sqlalchemy import Column, String

from app.core.db import Base


class Thing(Base):
    """Модель вещей игроков."""
    name = Column(String)
    type = Column(String(200))
    serial_number = Column(String, unique=True)
    part_number = Column(String)
    owner = Column(String, nullable=True)
    href = Column(String, unique=True)
