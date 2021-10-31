from typing import List

from sqlalchemy.orm import Session  # type: ignore

from models import Task


def get_task_by_id(session: Session, uuid: str) -> Task:
    return session.query(Task).filter(Task.task_uuid == uuid).first()


def get_task(session: Session, skip: int = 0, limit: int = 100) -> List[Task]:
    return session.query(Task).offset(skip).limit(limit).all()

