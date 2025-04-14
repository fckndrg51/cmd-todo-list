from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from Api.schemas import TaskInput, TaskOut
from psql_todolist.psql_todo import ToDoPsql
from Exceptions.Exceptions import TaskNotFoundException, TaskAlreadyDoneException

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    return ToDoPsql()


@router.get("/", response_model=List[TaskOut])
def get_tasks(todo: ToDoPsql = Depends(get_db)):
    """
    Получить список всех задач.

    :return: Список задач в формате TaskOut.
    """
    return [
        TaskOut(uid=uid, text=text, is_done=is_done)
        for uid, text, is_done in todo.get_task()
    ]


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskInput, todo: ToDoPsql = Depends(get_db)):
    """
    Создать новую задачу.

    :param task: Входные данные задачи (текст).
    :return: Созданная задача.
    """
    todo.add_task(task.text)
    all_tasks = todo.get_task()
    return TaskOut(
        uid=all_tasks[-1][0], text=all_tasks[-1][1], is_done=all_tasks[-1][2]
    )


@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: str, task: TaskInput, todo: ToDoPsql = Depends(get_db)):
    """
    Обновить текст задачи по её ID.

    :param task_id: Идентификатор задачи.
    :param task: Новые данные задачи.
    :return: Обновлённая задача.
    """
    try:
        todo.edit_task(task_id, task.text)
        for uid, text, is_done in todo.get_task():
            if uid == task_id:
                return TaskOut(uid=uid, text=text, is_done=is_done)
    except TaskNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{task_id}/done", response_model=TaskOut)
def mark_task_done(task_id: str, todo: ToDoPsql = Depends(get_db)):
    """
    Отметить задачу выполненной.

    :param task_id: Идентификатор задачи.
    :return: Обновлённая задача со статусом выполнено.
    """
    try:
        todo.mark_done(task_id)
        for uid, text, is_done in todo.get_task():
            if uid == task_id:
                return TaskOut(uid=uid, text=text, is_done=is_done)
    except TaskAlreadyDoneException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TaskNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, todo: ToDoPsql = Depends(get_db)):
    """
    Удалить задачу по ID.

    :param task_id: Идентификатор задачи.
    """
    try:
        todo.delete_task(task_id)
    except TaskNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
