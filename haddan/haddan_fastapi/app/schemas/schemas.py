from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, root_validator, validator


class ThingTypes(str, Enum):
    OVERARMOR = 'overarmor'
    OVERHELMET = 'overhelmet'
    OVERGLOVES = 'overgloves'
    OVERPANTS = 'overpants'
    RING1 = 'ring1'
    RING2 = 'ring2'
    RING3 = 'ring3'


class Profession(str, Enum):
    MINER = 'Шахтёр'
    REAPER = 'Жнец'
    BLACKSMITH = 'Кузнец'
    ALCHEMIST = 'Алхимик'
    FORESTER = 'Лесничий'


class Gamer(BaseModel):
    username: str = Field(...,
                          description='Никнейм персонажа',
                          example='Пердолятор'
                          )
    user_id: int = Field(...,
                         description='id персонажа',
                         example=111111)
    clan: Optional[str] = Field(None, example='Пердящие во тьме')
    proffession: Optional[Profession] = None

    class Config:
        str_max_length = 20

    @validator('user_id')
    def user_id_validator(cls, value: int):
        if len(str(value)) > 6:
            raise ValueError('Поле user_id должно быть максимум 6ти значным!')
        return value

    @root_validator(skip_on_failure=True)
    def custom_validator(csl, values):
        """Докстринг чтобы был"""
        # Проверяем поля pydantic модели по ключам словаря values
        # Возвращаем values
