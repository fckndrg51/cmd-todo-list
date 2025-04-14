from abc import ABC, abstractmethod


class ToDoInterface(ABC):
    @abstractmethod
    def add_task(self, text: str) -> None:
        pass

    @abstractmethod
    def edit_task(self, uid: str, text: str) -> None:
        pass

    @abstractmethod
    def mark_done(self, uid: str) -> None:
        pass

    @abstractmethod
    def get_task(self) -> list:
        pass

    @abstractmethod
    def delete_task(self, uid: str) -> None:
        pass