from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import models
from database import SessionLocal, engine
from models import Task
from schemas import TaskBase, TaskSerialized

models.Base.metadata.create_all(bind=engine)
itemrouter = APIRouter()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@itemrouter.get("/tasks/", response_model=List[TaskSerialized])
def read_task(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    items = crud.get_task(session=session, skip=skip, limit=limit)
    return [i.serialize for i in items]


@itemrouter.put("/tasks/{name}", response_model=TaskBase)
def update_task(detail: TaskSerialized, session: Session = Depends(get_session)):
    item = crud.get_task_by_id(session=session, uuid=detail.task_uuid)
    item.description = detail.description
    item.params = detail.params
    session.commit()
    return {"updated_item": item.task_uuid}


@itemrouter.post("/tasks/add")
def create_task(detail: TaskBase, session: Session = Depends(get_session)):
    to_create = Task(
        description=detail.description,
        params=detail.params
    )
    session.add(to_create)
    session.commit()
    return {"created_item": to_create.task_uuid}
