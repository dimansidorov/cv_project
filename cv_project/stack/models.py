from database import Base

from sqlalchemy import Column, String, Integer, Text, ForeignKey, Table
from sqlalchemy.orm import relationship


types = Table(
    'types',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(length=30), nullable=False, unique=True),
)

tools = Table(
    'tools',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(length=30), nullable=False),
    Column('description', Text),
    Column('link', String(length=255)),
    Column('cover', String(length=150), nullable=True),
    Column('type_id', Integer, ForeignKey('types.id')),
)
    

class Type(Base):
    __table__ = types

    tools = relationship('Tool', back_populates='type')


class Tool(Base):
    __table__ = tools

    type = relationship('Type', back_populates='tools')