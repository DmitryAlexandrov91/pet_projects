from pydantic import BaseModel


class ThingDB(BaseModel):
    name: str
    type: str
    serial_number: str
    part_number: str
    owner: str
    href: str
