import os
from psql_todolist.psql_todo import ToDoPsql
from service_control.ApiControl import FastApiControl
from service_control.ConsoleControl import ConsoleControl

if __name__ == "__main__":
    mode = os.getenv("APP_MODE", "fastapi").lower()
    db = ToDoPsql()

    match mode:
        case "fastapi":
            control = FastApiControl(db)
        case "console":
            control = ConsoleControl(db)
        case _:
            raise ValueError("APP_MODE должен быть 'fastapi' или 'console'")

    control.run()
