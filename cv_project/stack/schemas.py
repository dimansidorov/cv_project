from typing import Optional
from pydantic import BaseModel


class TypeCreate(BaseModel):
    id: int
    name: str


class ToolCreate(BaseModel):
    id: int
    name: str
    description: str
    link: str
    cover: Optional[str]
    type_id: int