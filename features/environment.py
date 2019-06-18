from behave import fixture
from behave.fixture import use_fixture_by_tag, use_fixture
from pony.orm import db_session

from models import create_database, Menu


@fixture
@db_session
def add_default_menu(context):
    Menu(name='MagicMenu', global_=True)

@fixture
def setup_testing_db(context):
    return create_database(':memory:')


def setup_testing_db_and_add_default_menu(context):
    use_fixture(setup_testing_db, context)
    use_fixture(add_default_menu, context)


def before_tag(context, tag):
    if tag.startswith('fixture'):
        fixtures = {
            'fixture.setup_testing_db_and_add_default_menu': (
                setup_testing_db_and_add_default_menu
            )
        }

        return use_fixture_by_tag(tag, context, fixtures)
