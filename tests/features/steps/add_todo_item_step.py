import inspect

from behave import when, then

from tests.features.base_context import TestBaseContext


class TodoItemTestDataType(TestBaseContext):
    item_id: str
    item_text: str


def context_to_args(func):
    def inner(*args, **kwargs):
        prepared_args = []
        expected_args = list(inspect.signature(func).parameters.keys())
        for arg in expected_args:
            if arg not in kwargs and hasattr(args[0], arg):
                prepared_args.append(getattr(args[0], arg))

        result = func(*prepared_args, **kwargs)
        if type(result) is dict:
            for key, value in result.items():
                setattr(args[0], key, value)
        return result

    return inner


@when('user adds new todo item with text {text}')
@context_to_args
def step_implementation(todo_list, text):
    item_id = todo_list.add(text)
    return {
        "item_id": item_id,
        "item_text": text
    }


@when('user adds {number:d} new todo items')
@context_to_args
def step_implementation(todo_list, number):
    for _ in range(0, number):
        todo_list.add(f"item {_}")


@then('todo items list should contain {number:d} items')
@context_to_args
def step_implementation(todo_list, number):
    todo_items_list = todo_list.list()
    assert len(todo_items_list) == number


@then('todo item with text {text} should be present on the list')
@context_to_args
def step_implementation(todo_list, item_id, item_text, text):
    todo_items_list = todo_list.list()
    for item in todo_items_list:
        if item_id == item['id']:
            assert item_text == text


# ---------------------------- the original way: ------------------------------------
# @when('user adds new todo item with text {text}')
# def step_implementation(context, text):
#     context.item_id = context.todo_list.add(text)
#     context.item_text = text
#
#
# @when('user adds {number:d} new todo items')
# def step_implementation(context, number):
#     for _ in range(0, number):
#         context.todo_list.add(f"item {_}")
#
#
# @then('todo items list should contain {number:d} items')
# def step_implementation(context, number):
#     todo_items_list = context.todo_list.list()
#     assert len(todo_items_list) == number
#
#
# @then('todo item with text {text} should be present on the list')
# def step_implementation(context, text):
#     todo_items_list = context.todo_list.list()
#     for item in todo_items_list:
#         if context.item_id == item['id']:
#             assert context.item_text == text
