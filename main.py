import pytest
from PyInquirer import prompt
from pony.orm import select, db_session, delete

from models import Menu, create_database


def load_fixtures():
    with db_session:
        main = Menu(name='MagicMenu', global_=True, parent=1)

    with db_session:
        Menu(name='Create menu', global_=True, parent=main.id)
        Menu(name='Update menu', global_=True, parent=main.id)
        Menu(name='Delete menu', global_=True, parent=main.id)


@db_session
def get_root_menus():
    result = select(m for m in Menu if m.id == m.parent)
    return [m for m in result]


@db_session
def array_menu(menus):
    amount = len(menus)
    numbered_dict = zip(range(amount), menus)

    return [
        {
            'key': str(index),
            'name': menu.name,
            'value': menu
        } for index, menu in numbered_dict
    ]


def get_menu_dict(menus):
    return {
        'type': 'list',
        'message': 'Choice an option: ',
        'name': 'option',
        'default': '1',
        'choices': array_menu(menus)
    }


def ask(menu_dict):
    reply = prompt(menu_dict)['option']

    if reply.has_children():
        children = reply.children()
        md = get_menu_dict(children)
        ask(md)


if __name__ == '__main__':
    create_database('./settings')

    load_fixtures()

    root_menus = get_root_menus()
    menu_dict = get_menu_dict(root_menus)

    ask(menu_dict)

