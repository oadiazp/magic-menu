import pytest
from behave import *

from main import add_a_submenu
from models import Menu

use_step_matcher("parse")


@when("I add a submenu to a menu")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.menu = add_a_submenu(Menu[1], Menu(name='Submenu', global_=False))


@then("The dict should contain a key called submenus")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pytest.set_trace()