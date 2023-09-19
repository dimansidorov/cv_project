from typing import Optional
from pydantic import BaseModel, Field


class TypeBase(BaseModel):
    name: str


class TypeRead(TypeBase):
    pass


class TypeCreate(TypeBase):
    pass


class ToolBase(BaseModel):
    name: str
    description: str
    link: str
    type_id: int


class ToolRead(ToolBase):
    pass


class ToolCreate(ToolBase):
    pass