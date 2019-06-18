from pony.orm import select

import click

from models import Menu, create_database


@click.command()
def show_menu():
    menus = select(m for m in Menu)

    return menus


if __name__ == '__main__':
    create_database('./settings')
    show_menu()

