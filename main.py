from pony.orm import select, sql_debug

import click

from models import db, Menu


def create_database(db_name):
    sql_debug(True)
    db.bind(provider='sqlite', filename=db_name, create_db=True)
    db.generate_mapping(create_tables=True)


@click.command()
def show_menu():
    menus = select(m for m in Menu)
    pass


if __name__ == '__main__':
    create_database('./settings')
    show_menu()

