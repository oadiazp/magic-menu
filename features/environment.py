from behave import fixture, use_fixture

from models import create_database


@fixture
def setup_testing_db(context):
    return create_database(':memory:')


def before_tag(context, tag):
    fixtures = {
        'fixture.setup.testing.db': setup_testing_db
    }

    return use_fixture(fixtures[tag], context)
