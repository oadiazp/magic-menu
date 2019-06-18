from pony.orm import Database, Required, Set, sql_debug

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
    path = Required(str)

    actions = Set(Action)

def create_database(db_name):
    sql_debug(True)
    db.bind(provider='sqlite', filename=db_name, create_db=True)
    db.generate_mapping(create_tables=True)

    return db
