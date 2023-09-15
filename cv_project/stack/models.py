from database import Base

from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class Type(Base):
    __tablename__ = 'types'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(length=30), nullable=False)

    tools = relationship('Tool', back_populates='type')


class Tool(Base):
    __tablename__ = 'tools'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(length=30), nullable=False)
    description: str = Column(Text)
    link: str = Column(String(length=255))
    cover: str = Column(String(length=150), nullable=True)
    type_id: int = Column(Integer, ForeignKey('types.id'))

    type = relationship('Type', back_populates='tools')