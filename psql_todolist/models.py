from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from database import Base

class Task(Base):
    """
    Модель задачи (Tasks) для хранения информации о задачах в базе данных.
    uid (str): Уникальный идентификатор задачи.
    text (str): Описание задачи.
    is_done (bool): Статус выполнения задачи (по умолчанию False).
    """
    __tablename__ = "tasks"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, comment="Уникальный ID задачи")
    text = Column(String, nullable=False, comment="Текст задачи")
    is_done = Column(Boolean, default=False, comment="Статус выполнения задачи")