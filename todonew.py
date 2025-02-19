import json
import os
from uuid import uuid4
from task import Task


class ToDo:
    def __init__(self):
        self.json_name = "db.json"
        self.data = self.load_json()
        self.tasks = {}


    def load_json(self) -> None:
        """
        Загружает список задач из json
        :return: Словарь с задачами
        """
        if not os.path.exists(self.json_name):
            return {}

        with open(self.json_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                return {uid: Task.from_dict(task) for uid, task in data.items()}


    def save_json(self) -> None:
        """
        Сохраняет текущие задачи в JSON
        """
        with open(self.json_name, "w", encoding="utf-8") as file:
            json.dump({uid: task.to_dict() for uid, task in self.data.items()}, file, ensure_ascii=False)


    def add_task(self, text: str) -> None:
        """
        Добавляет новую задачу
        :param text: Описание задачи
        :return: ID созданной задачи
        """

        uid = str(uuid4())
        self.data[uid] = Task(uid, text)
        self.save_json()
        return uid

    def mark_done(self, uid: str) -> None:
        """
        Отмечает задачу выполненной
        :param uid: ID задачи
        """
        if uid not in self.data:
            raise KeyError(f"Задача с ID {uid} не найдена")

        self.data[uid].mark_done(True)
        self.save_json()

    def edit_task(self, uid: str, new_text: str) -> None:
        """
        Редактирует текст задачи
        :param uid: ID задачи
        :param new_text: Новый текст задачи
        """
        if uid not in self.data:
            raise KeyError(f"Задача с ID {uid} не найдена")

        self.data[uid].edit_text(new_text)
        self.save_json()

    def get_task(self) ->None:
        """
        Возвращает список всех задач
        :return: ID, текст, статус
        """
        return [(uid, task.text, task.is_done) for uid, task in self.data.items()]

    def delete_task(self, uid: str) ->None:
        """
        Удаляет задачу по ID
        :param uid: ID задачи
        """
        if uid not in self.data:
            raise KeyError(f"Задача с ID {uid} не найдена")

        del self.data[uid]
        self.save_json()


    def delete_db(self) -> None:
        """
        Удаляет JSON-файл с задачами
        """
        if os.path.exists(self.json_name):
            os.remove(self.json_name)
            print("Файл базы данных удалён")
        else:
            print("Файл базы данных не найден")








