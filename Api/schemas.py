from pydantic import BaseModel, Field
from uuid import UUID


class TaskInput(BaseModel):
    """
    Схема входных данных задачи.
    """
    text: str = Field(title="Описание задачи")


class TaskOut(BaseModel):
    """
    Схема выходных данных задачи.
    """
    uid: UUID = Field(title="ID задачи")
    text: str = Field(title="Описание задачи")
    is_done: bool = Field(False, title="Статус выполнения задачи")

