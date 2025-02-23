from dataclasses import dataclass


@dataclass
class Task:
    """
    Представляет задачу в списке БД.
    uid (str): Уникальный идентификатор задачи.
    text (str): Описание задачи.
    is_done (bool): Статус выполнения задачи (по умолчанию False).
    """

    uid: str
    text: str
    is_done: bool = False
