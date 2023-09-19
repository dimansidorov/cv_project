from typing import List
from database import Base
from sqlalchemy import Table, Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from stack.models import Tool


projects = Table(
    'projects',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('desciprion', Text, nullable=False),
    Column('link', String, nullable=True),
    Column('type', String, nullable=False)
)

projects_tools_association = Table(
    "projects_tools_association",
    Base.metadata,
    Column("project_id", ForeignKey("projects.id"), primary_key=True),
    Column("tool_id", ForeignKey("tools.id"), primary_key=True),
)

class Project(Base):
    __table__ = projects

    stack: Mapped[List[Tool]] = relationship(
        secondary=projects_tools_association, back_populates="projects"
    )



