from typing import Optional

from fastapi import APIRouter, Query

from app.schemas.schemas import ThingTypes


thing_router = APIRouter(
    prefix='/thing',
    tags=['All Hadddan Items']
)


@thing_router.get('/')
def get_things():
    return 'Здесь будут все предметы из таблицы thing '


@thing_router.get('/{user}')
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
