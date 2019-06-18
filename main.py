from pony.orm import select, db_session

from models import Menu, create_database

@db_session
def show_menu():
    return [r for r in select(m for m in Menu)]


if __name__ == '__main__':
    create_database('./settings')
    show_menu()

