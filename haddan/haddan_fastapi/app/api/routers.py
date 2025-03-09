from fastapi import APIRouter

from app.api.endpoints import things_router

main_router = APIRouter()


main_router.include_router(
    things_router,
    prefix='/things',
    tags=['All players things']
)
