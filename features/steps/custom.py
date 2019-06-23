from behave import *
from pony.orm import db_session, count

from models import Menu

use_step_matcher("parse")


@when("I add a submenu to a menu")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    with db_session:
        menu = Menu[1]
        Menu(name='Create a menu', global_=True, parent=menu.id)
        Menu(name='Update a menu', global_=True, parent=menu.id)
        Menu(name='Delete a menu', global_=True, parent=menu.id)


@then("There is a submenu")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    with db_session:
        menu = Menu[1]
        amount = count(m for m in Menu if m.parent == menu.id)
        assert amount == 3, 'Amount: {}'.format(amount)
