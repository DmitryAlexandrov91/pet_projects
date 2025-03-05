from typing import Optional

from fastapi import APIRouter, Query

from app.schemas.schemas import Gamer, ThingTypes


router = APIRouter()


@router.get('/item')
def get_items():
    return 'Здесь будут все предметы из таблицы item'


@router.get('/things')
def get_things():
    return 'Здесь будут все предметы из таблицы thing '


@router.get('/things/{user}')
def get_user_things(
    user: str,
    types: Optional[list[ThingTypes]] = Query(None)
) -> dict:
    if types is not None:
        return {
            f'{user.capitalize()}': types
        }
    return {
        user.capitalize(): ''
    }


@router.post('/reg')
def registration(user: Gamer) -> str:
    return f'Приветствеую {user.username} с id {user.user_id}'
