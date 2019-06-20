from pony.orm import Database, Required, Set, sql_debug, Optional, select, \
    db_session

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

    def get_menu_dict(self):
        return {
            'type': 'expand',
            'message': 'Choice an option: ',
            'name': 'option',
            'default': '1',
            'choices': self.array_menu()
        }

    def array_menu(self):
        with db_session:
            silibings = select(
                m for m in Menu if m.parent == self.parent
            )

        amount = len(silibings)
        numbered_dict = zip(range(amount), silibings)

        return [
            {
                'key': str(index),
                'name': silibing.name,
                'value': silibing
            } for index, silibing in numbered_dict
        ]





def create_database(db_name):
    sql_debug(True)
    db.bind(provider='sqlite', filename=db_name, create_db=True)
    db.generate_mapping(create_tables=True)

    return db
