from Api.IApi import IApi
from Exceptions.Exceptions import TaskException, TaskIsDone


class ConsoleControl(IApi):
    """
    Менеджер для управления приложением через консоль
    """
    def run(self):
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
                    for uid, text, is_done in self.todo.get_task():
                        print(f"ID: {uid} | {text} | {'Выполнена' if is_done else 'Не выполнена'}")
                case "2":
                    self.todo.add_task(input("Введите текст задачи: "))
                case "3":
                    try:
                        self.todo.edit_task(input("ID: "), input("Новый текст: "))
                    except TaskException as e:
                        print(e)
                case "4":
                    try:
                        self.todo.mark_done(input("ID: "))
                    except TaskIsDone as e:
                        print(e)
                    except TaskException as e:
                        print(e)
                case "5":
                    try:
                        self.todo.delete_task(input("ID: "))
                    except TaskException as e:
                        print(e)
                case "6":
                    break
                case _:
                    print("Неправильный ввод")
