from app.crud.base import CRUDBase
from app.models import Thing


class CRUDThings(CRUDBase):
    """Класс CRUD эндпоинта things."""


things_crud = CRUDThings(Thing)
