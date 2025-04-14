
from abc import ABC, abstractmethod
from Interfaces.ToDoInterface import ToDoInterface


class IApi(ABC):
    def __init__(self, todo: ToDoInterface):
        self.todo = todo

    @abstractmethod
    def run(self):
        pass