from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    text = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)