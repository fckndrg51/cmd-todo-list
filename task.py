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

    def to_dict(self) -> dict:
        """
        Преобразует объект Task в словарь
        :return: словарь с полями uid, text, is_done
        """
        return asdict(self)
