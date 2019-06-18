from behave import fixture
from behave.fixture import use_fixture_by_tag

from models import create_database


@fixture
def setup_testing_db(context):
    return create_database(':memory:')


def before_tag(context, tag):
    if tag.startswith('fixture'):
        fixtures = {
            'fixture.setup.testing.db': setup_testing_db
        }

        return use_fixture_by_tag(tag, context, fixtures)
