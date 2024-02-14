from behave import fixture, use_fixture

# more here:
# https://www.tutorialspoint.com/behave/behave_hooks.htm
# https://behave.readthedocs.io/en/stable/fixtures.html


@fixture
def pickles_storage(context):
    print("Creating pickles storage")
    context.pickles = []
    yield
    print("Removing everything from storage")
    context.pickles = []


def before_all(context):
    pass


def before_tag(context, tag):
    # if tag == "with-pickles":
    #     use_fixture(pickles_storage, context)
    pass


def before_feature(context, scenario):
    pass


def before_scenario(context, scenario):
    use_fixture(pickles_storage, context)
    # you could also just do context.pickles = [] here to create this list before feature starts
