from fastapi import APIRouter, HTTPException, status
from typing import List
from Api.schemas import TaskInput, TaskOut
from psql_todolist.psql_todo import ToDoPsql
from Exceptions.Exceptions import TaskException, TaskIsDone

router = APIRouter(prefix="/tasks", tags=["Tasks"])

todo = ToDoPsql()


@router.get("/", response_model=List[TaskOut])
def get_tasks():
    return [
        TaskOut(uid=uid, text=text, is_done=is_done)
        for uid, text, is_done in todo.get_task()
    ]


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskInput):
    todo.add_task(task.text)
    all_tasks = todo.get_task()
    return TaskOut(uid=all_tasks[-1][0], text=all_tasks[-1][1], is_done=all_tasks[-1][2])


@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: str, task: TaskInput):
    try:
        todo.edit_task(task_id, task.text)
        for uid, text, is_done in todo.get_task():
            if uid == task_id:
                return TaskOut(uid=uid, text=text, is_done=is_done)
    except TaskException as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{task_id}/done", response_model=TaskOut)
def mark_task_done(task_id: str):
    try:
        todo.mark_done(task_id)
        for uid, text, is_done in todo.get_task():
            if uid == task_id:
                return TaskOut(uid=uid, text=text, is_done=is_done)
    except TaskIsDone as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TaskException as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str):
    try:
        todo.delete_task(task_id)
    except TaskException as e:
        raise HTTPException(status_code=404, detail=str(e))
