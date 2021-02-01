import os

import app.classes.models.categories as categories
import app.database.create_db as db


clear = lambda: os.system('cls')

def main():
    """"""
    print("Creating database... This might take a few minutes.")
    #db.create_db()
    print("Database is ready.")
    show_menu()

def show_menu():
    """"""
    clear()
    print("1 - Chercher un aliment")
    print("2 - Retrouver mes aliments substitués")
    choice = input("> ")

    if choice == "1":
        categories.get_categories()
    elif choice == "2":
        pass
    else:
        show_menu()


if __name__ == "__main__":
    main()
