from pony.orm import select, db_session, commit

from models import Menu, create_database

@db_session
def show_menu():
    return [str(r) for r in select(m for m in Menu)]

@db_session
def add_a_submenu(menu, submenu):
    menu.submenus.append(submenu)
    commit()

    return menu


if __name__ == '__main__':
    create_database('./settings')
    show_menu()

