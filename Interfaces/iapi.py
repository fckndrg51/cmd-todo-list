from abc import ABC, abstractmethod
from Interfaces.ToDoInterface import ToDoInterface


class IApi(ABC):
    """
    Интерфейс API-контроллера.
    """
    def __init__(self, todo: ToDoInterface):
        """
        Инициализация API с задачами.
        """
        self.todo = todo

    @abstractmethod
    def run(self):
        """
        Запуск API или консольного режима.
        """
        pass
