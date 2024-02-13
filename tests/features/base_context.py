from src.todo_list import ToDoList


class BaseContext:
    todo_list: ToDoList


class TestBaseContext(BaseContext):
    data: dict