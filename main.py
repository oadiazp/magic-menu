import pytest
from PyInquirer import prompt
from pony.orm import select, db_session

from models import Menu, create_database

@db_session
def get_menu(parent):
    result = select(m for m in Menu if m.parent == parent)
    return [r for r in result]


def load_fixtures():
    with db_session:
        main = Menu(name='MagicMenu', global_=True, parent=None)

    with db_session:
        Menu(name='Create menu', global_=True, parent=main.id)
        Menu(name='Update menu', global_=True, parent=main.id)
        Menu(name='Delete menu', global_=True, parent=main.id)


def show_menu(menu):
    selected_option = prompt(menu.get_menu_dict(menu))['option']

    if isinstance(selected_option, Menu):
        pytest.set_trace()

        if selected_option.has_children():
            show_menu(selected_option)
        else:
            print('Run command')


if __name__ == '__main__':
    create_database('./settings')

    load_fixtures()
    menu = get_menu(None)[0]

    show_menu(menu)
