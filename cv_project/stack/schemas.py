from typing import Optional
from pydantic import BaseModel, Field


class TypeBase(BaseModel):
    name: str


class TypeRead(TypeBase):
    class Config:
        from_attributes= True


class TypeCreate(TypeBase):
    pass


class ToolBase(BaseModel):
    name: str
    description: str
    link: str
    cover: Optional[str]


# class ToolRead(ToolBase):
#     type: TypeRead
#     class Config:
#         from_attributes= True


# class ToolCreate(ToolBase):
#     type_id: int = Field(..., description="ID of the related Type")