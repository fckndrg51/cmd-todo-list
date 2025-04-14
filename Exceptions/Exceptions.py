class TaskException(Exception):
    """
    Исключение для работы с несуществующими ID.
    """
    def __init__(self, uid: str):
        self.task_id = uid
        self.message = f"Нет таска с таким ID: {uid}"
    def __str__(self):
        return self.message

class TaskIsDone(Exception):
    """
    Исключение для работы с завершенными тасками.
    """
    def __init__(self, uid: str):
        self.task_id = uid
        self.message = f"Таск {uid} был завершен ранее"

    def __str__(self):
        return self.message

