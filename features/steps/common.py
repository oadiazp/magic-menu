import pytest
import requests
from behave import *
from jsonpath_rw import parse
from pytest import fail

from main import show_menu

use_step_matcher('parse')


@when("I ask for {method}")
def step_impl(context, method):
    """
    :type context: behave.runner.Context
    """
    methods = {
        'the list of menus': show_menu
    }

    if not hasattr(context, 'params'):
        context.response = methods[method]()
    else:
        context.response = methods[method](**context.params)


@then("I expect for a list that contains {expected_items}")
def step_impl(context, expected_items):
    """
    :type context: behave.runner.Context
    """
    expected_items_list = expected_items.split(', ')
    missing_items = []

    for expected_item in expected_items_list:
        if expected_item not in context.response:
            missing_items.append(expected_item)

    if missing_items:
        fail("Those items are missing: {}".format(missing_items))


@then("I expect for a list that don't contains {not_expected_items}")
def step_impl(context, not_expected_items):
    """
    :type context: behave.runner.Context
    """
    not_expected_items_list = not_expected_items.split(', ')
    present_items = []

    for not_expected_item in not_expected_items_list:
        if not_expected_item in context.response:
            present_items.append(not_expected_item)

    if present_items:
        fail(
            "These elements should not be in the results: {}".format(
                present_items
            )
        )


@step("the param {name} is {value}")
def step_impl(context, name, value):
    """
    :type context: behave.runner.Context
    """
    if not hasattr(context, 'params'):
        context.params = {}

    context.params[name] = value


@then("Filter the results by a JSONPath {json_path}")
def step_impl(context, json_path):
    """
    :type context: behave.runner.Context
    """
    json_path_expr = parse(json_path)
    context.response = [
        match.value for match in json_path_expr.find(context.response)
    ]


@when("I clean the params")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.params = {}


@then("{url} should be reachable")
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    """
    assert requests.get(url).status_code == 200

