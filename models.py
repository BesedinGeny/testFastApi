import uuid
from typing import TypedDict

from sqlalchemy import Column, Integer, String, JSON  # type: ignore

from database import Base


class TaskDict(TypedDict):
    task_uuid: str
    description: str
    params: dict


class Task(Base):
    """
    Defines the items model
    """

    __tablename__ = "task"
    task_uuid = Column(String, primary_key=True, default=str(uuid.uuid4()), nullable=True)
    description = Column(String, nullable=True)
    params = Column(JSON, nullable=True)

    def __init__(self, description: str, params: dict):
        self.description = description
        self.params = params

    def __repr__(self) -> str:
        return f"<Item {self.task_uuid}>"

    @property
    def serialize(self) -> TaskDict:
        """
        Return item in serializeable format
        """
        return {"task_uuid": self.task_uuid,
                "description": self.description,
                "params": self.params
                }
