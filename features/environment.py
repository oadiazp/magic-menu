import pytest
from behave import fixture

from main import create_database

@fixture
def set_up_testing_db():
    pytest.set_trace()
    create_database(':memory:')
