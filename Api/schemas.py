from pydantic import BaseModel, Field
from uuid import UUID

class TaskInput(BaseModel):
    text: str = Field(title="Описание задачи")


class TaskOut(BaseModel):
    uid: UUID = Field(title="ID задачи")
    text: str = Field(title="Описание задачи")
    is_done: bool = Field(False, title="Статус выполнения задачи")

    class Config:
        from_attributes = True