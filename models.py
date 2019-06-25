import os

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

    @db_session
    def children(self):
        return select(m for m in Menu if m.parent == self.id)

    @db_session
    def has_children(self):
        parent = self.id

        return count(m for m in Menu if m.parent == parent) > 0


def create_database(db_name):
    os.remove(db_name)

    sql_debug(False)
    db.bind(provider='sqlite', filename=db_name, create_db=True)
    db.generate_mapping(create_tables=True)

    return db
