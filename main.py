from psql_todolist.psql_todo import ToDoPsql
from Exceptions import TaskException, TaskIsDone


class Menu:
    """
    Класс для управления консольным меню
    Позволяет пользователю управлять списком задач через командную строку.
    """
    def __init__(self, console: ToDoPsql):
        self.console = console

    def start_console(self) -> None:
        while True:
            print("\n" + "_" * 30)
            print("1. Вывести задачи")
            print("2. Добавить задачу")
            print("3. Редактировать задачу")
            print("4. Завершить задачу")
            print("5. Удалить задачу")
            print("6. Выйти")
            print("_" * 30)

            match input("Введите номер команды: "):
                case "1":
                    for uid, text, is_done in self.console.get_task():
                        print(
                            f"ID: {uid} | {text} | {'Выполнена'if is_done else 'Не выполнена'}"
                        )
                case "2":
                    self.console.add_task(input("Введите текст задачи: "))
                case "3":
                    try:
                        self.console.edit_task(input("ID: "), input("Новый текст: "))
                    except TaskException as e:
                        print (e)
                        continue
                case "4":
                    try:
                        self.console.mark_done(input("ID: "))
                    except TaskException as e:
                        print(e)
                    except TaskIsDone as e:
                        print(e)
                case "5":
                    try:
                        self.console.delete_task(input("ID: "))
                    except TaskException as e:
                        print(e)
                case "6":
                    break
                case _:
                    print("Неправильный ввод")
                    break


if __name__ == "__main__":
    todo = ToDoPsql()
    Menu(todo).start_console()
