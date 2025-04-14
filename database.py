from os import getenv
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv("ci/.env")

@dataclass
class AlchemySettings:
    """
    Конфигурация для подключения к базе данных.
    Получает значения из переменных окружения.
    """

    user: str = getenv("POSTGRES_USER")
    password: str = getenv("POSTGRES_PASSWORD")
    host: str = getenv("POSTGRES_HOST")
    port: str = getenv("POSTGRES_PORT")
    db: str = getenv("POSTGRES_DB")
    schema: str = getenv("SCHEMA")

    def url_base(self) -> str:
        """
        Формирует URL для подключения к базе данных на основе переменных окружения.
        :return: Строка подключения к БД в формате SQLAlchemy.
        """
        return f"{self.schema}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


db_config = AlchemySettings()
engine = create_engine(db_config.url_base())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
