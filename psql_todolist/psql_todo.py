from uuid import UUID
from psql_todolist.models import Task
from database import SessionLocal
from Exceptions.Exceptions import TaskException, TaskIsDone
from Interfaces.ToDoInterface import ToDoInterface

class ToDoPsql(ToDoInterface):
    """
    Менеджер для работы с to-do листом используя postgresql
    """
    def add_task(self, text: str) -> None:
        """
        Добавляет новую задачу
        :param text: Описание задачи
        """
        with SessionLocal() as session:
            task = Task(text=text)
            session.add(task)
            session.commit()
            session.refresh(task)

    def mark_done(self, uid: str) -> None:
        """
        Отмечает задачу выполненной
        :param uid: ID задачи
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(uid))
            if not task:
                raise TaskException(uid)
            if task.is_done:
                raise TaskIsDone(uid)
            task.is_done = True
            session.commit()
            session.refresh(task)

    def edit_task(self, uid: str, text: str) -> None:
        """
        Редактирует текст задачи
        :param uid: ID задачи
        :param text: Новый текст задачи
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(uid))
            if not task:
                raise TaskException(uid)
            task.text = text
            session.commit()
            session.refresh(task)

    def get_task(self) -> None:
        """
        Возвращает список всех задач
        :return: ID, текст, статус
        """
        with SessionLocal() as session:
            tasks = session.query(Task).all()
            return [(str(task.uid), task.text, task.is_done) for task in tasks]

    def delete_task(self, uid: str) -> None:
        """
        Удаляет задачу по ID
        :param uid: ID задачи
        """
        with SessionLocal() as session:
            task = session.get(Task, UUID(uid))
            if not task:
                raise TaskException(uid)
            session.delete(task)
            session.commit()



