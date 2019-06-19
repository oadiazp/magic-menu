from behave import *

use_step_matcher("parse")


@when("I add a submenu to a menu")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    root_menu = Menu[1]