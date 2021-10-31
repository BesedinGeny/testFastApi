from pydantic import BaseModel


class TaskBase(BaseModel):
    description: str
    params: dict


class TaskSerialized(TaskBase):
    task_uuid: str
