from src.todo_list import ToDoList


def before_scenario(context, _):
    context.todo_list = ToDoList()
