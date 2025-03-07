from fastapi import APIRouter


item_router = APIRouter(
    prefix='/item',
    tags=['All Hadddan Items']
)


@item_router.get('/')
def get_items():
    return 'Здесь будут все предметы из таблицы item'
