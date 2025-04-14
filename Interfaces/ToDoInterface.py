from abc import ABC, abstractmethod


class ToDoInterface(ABC):
    """
    Интерфейс для взаимодействия со списком задач.
    """

    @abstractmethod
    def add_task(self, text: str) -> None:
        """
        Добавить задачу.

        :param text: Текст задачи.
        """
        pass

    @abstractmethod
    def edit_task(self, uid: str, text: str) -> None:
        """
        Отредактировать задачу.

        :param uid: ID задачи.
        :param text: Новый текст задачи.
        """
        pass

    @abstractmethod
    def mark_done(self, uid: str) -> None:
        """
        Отметить задачу как выполненную.

        :param uid: ID задачи.
        """
        pass

    @abstractmethod
    def get_task(self) -> list:
        """
        Получить список всех задач.

        :return: Список задач.
        """
        pass

    @abstractmethod
    def delete_task(self, uid: str) -> None:
        """
        Удалить задачу.

        :param uid: ID задачи.
        """
        pass
