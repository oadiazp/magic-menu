import pytest
from pony.orm import (
    Database,
    Required,
    Set,
    sql_debug,
    Optional,
    select,
    db_session,
    count)

db = Database()

class Argument(db.Entity):
    name = Required(str)
    required = Required(bool)

    action = Required(lambda: Action)


class Action(db.Entity):
    name = Required(str)
    command = Required(str)

    arguments = Set(Argument)
    menu = Required(lambda: Menu)


class Menu(db.Entity):
    name = Required(str)
    global_ = Required(bool)
    path = Optional(str)
    parent = Optional(int)
    command = Optional(str)

    actions = Set(Action)

    def __str__(self):
        return self.name

    def get_menu_dict(self, menus):
        return {
            'type': 'expand',
            'message': 'Choice an option: ',
            'name': 'option',
            'default': '1',
            'choices': self.array_menu(menus)
        }

    @db_session
    def has_children(self):
        parent = self.id

        return count(m for m in Menu if m.parent == parent) > 0

    def array_menu(self, menus):
        if not isinstance(menus, list):
            menus = [menus]

        amount = len(menus)
        numbered_dict = zip(range(amount), menus)

        return [
            {
                'key': str(index),
                'name': menu.name,
                'value': menu
            } for index, menu in numbered_dict
        ]


def create_database(db_name):
    sql_debug(False)
    db.bind(provider='sqlite', filename=db_name, create_db=True)
    db.generate_mapping(create_tables=True)

    return db
