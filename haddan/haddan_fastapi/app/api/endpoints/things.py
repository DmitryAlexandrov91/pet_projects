from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.schemas import ThingDB
from app.core import get_async_session
from app.crud import things_crud


things_router = APIRouter()


@things_router.get(
    '/',
    response_model=list[ThingDB],
    response_model_exclude_none=True)
async def get_all_things(
    session: AsyncSession = Depends(get_async_session)
):
    return await things_crud.get_multi(session)
