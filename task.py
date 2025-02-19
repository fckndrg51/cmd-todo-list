from dataclasses import dataclass, asdict

@dataclass
class Task:
    uid: str
    text: str
    is_done: bool = False

    def mark_done(self, is_done: bool) -> None:
        """
        Устанавливает статус выполнения
        :param is_done: True - завершена, False - нет
        """
        self.is_done = is_done

    def edit_text(self, text: str) -> None:
        """
        Редактирует текст задачи
        :param text: Новый текст
        """
        self.text = text

    def to_dict(self) -> dict:
        """
        Преобразует объект Task в словарь
        :return: словарь с полями uid, text, is_done
        """
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Task":
        """
        Создает объект Task из словаря
        :param data: словарь с полями uid, text, is_done
        :return: объект Task
        """
        return Task(**data)
