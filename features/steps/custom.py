import pytest
from behave import *
from pony.orm import db_session

from models import Menu

use_step_matcher("parse")


@when("I add a submenu to a menu")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    with db_session:
        menu = Menu[1]
        menu.submenus.add(Menu(name='Create a menu', global_=True))


@then("There is a submenu")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    with db_session:
        menu = Menu[1]
        assert menu.submenus.count() > 0
