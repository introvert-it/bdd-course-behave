from behave import given, when, then


@given("user has {number:d} closed jar(s) of pickles")
def step_definition(context, number):
    for _ in range(number):
        context.pickles.append({"closed": True})


@given("user grabs jar number {number:d}")
def step_definition(context, number):
    context.active_jar_index = number - 1


@when("user spins the lid")
def step_definition(context):
    pass


@when("the lid loosens up")
def step_definition(context):
    pass


@then("user should be able to take the lid off")
def step_definition(context):
    context.pickles[0]["closed"] = False


@then('jar of pickles number {number:d} should be opened')
def step_definition(context, number):
    assert context.pickles[0]["closed"] == False


@then('jar of pickles number {number:d} should be closed')
def step_definition(context, number):
    assert context.pickles[1]["closed"] == True
