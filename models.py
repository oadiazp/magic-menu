from pony.orm import Database, Required, Set, sql_debug, Optional

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

    actions = Set(Action)
    parent = Optional('Menu', reverse='parent')
    submenus = Set('Menu', reverse='submenus')

    def __str__(self):
        return self.name


def create_database(db_name):
    sql_debug(True)
    db.bind(provider='sqlite', filename=db_name, create_db=True)
    db.generate_mapping(create_tables=True)

    return db
