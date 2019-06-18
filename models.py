from pony.orm import Database, Required, Set

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
