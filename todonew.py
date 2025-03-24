import json
import os
from uuid import uuid4
from task import Task
from dataclasses import asdict


class ToDo:
    """
    Класс для управления списком задач.
    Задачи хранятся в JSON-файле и могут быть добавлены, изменены, удалены (в том числе и вся БД) или помечены как выполненные.
    json_name (str): Имя JSON-файла для хранения задач.
    data (dict): Словарь с загруженными задачами.
    """

    def __init__(self):
        self.json_name = "db.json"
        self.data = self._load_json()

    def _load_json(self) -> dict:
        """
        Загружает список задач из json
        :return: Словарь с задачами
        """
        if not os.path.exists(self.json_name):
            return {}

        with open(self.json_name, "r", encoding="utf-8") as file:
            data = json.load(file)
            return {uid: Task(**task_data) for uid, task_data in data.items()}

    def _save_json(self) -> None:
        """
        Сохраняет текущие задачи в JSON
        """
        with open(self.json_name, "w", encoding="utf-8") as file:
            json.dump(
                {uid: asdict(task) for uid, task in self.data.items()},
                file,
                ensure_ascii=False,
            )

    def add_task(self, text: str) -> None:
        """
        Добавляет новую задачу
        :param text: Описание задачи
        :return: ID созданной задачи
        """
        uid = str(uuid4())
        self.data[uid] = Task(uid, text)
        self._save_json()
        return uid

    def mark_done(self, uid: str) -> None:
        """
        Отмечает задачу выполненной
        :param uid: ID задачи
        """
        if uid not in self.data:
            raise KeyError(f"Задача с ID {uid} не найдена")

        self.data[uid].is_done = True
        self._save_json()

    def edit_task(self, uid: str, text: str) -> None:
        """
        Редактирует текст задачи
        :param uid: ID задачи
        :param text: Новый текст задачи
        """
        if uid not in self.data:

            raise KeyError(f"Задача с ID {uid} не найдена")

        self.data[uid].text = text
        self._save_json()

    def get_task(self) -> None:
        """
        Возвращает список всех задач
        :return: ID, текст, статус
        """
        return [(uid, task.text, task.is_done) for uid, task in self.data.items()]

    def delete_task(self, uid: str) -> None:
        """
        Удаляет задачу по ID
        :param uid: ID задачи
        """
        if uid not in self.data:
            raise KeyError(f"Задача с ID {uid} не найдена")

        del self.data[uid]
        self._save_json()

    def delete_db(self) -> None:
        """
        Удаляет JSON-файл с задачами
        """
        if os.path.exists(self.json_name):
            os.remove(self.json_name)
            self.data.clear()
            print("Файл базы данных удалён")
        else:
            print("Файл базы данных не найден")
