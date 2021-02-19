from app.application import Application
from app.functions import clear

import app.database.create_db as db


def main():
    """"""
    db.create_db()
    clear()

    print("Bienvenue dans le programme Pur Beurre !\n")
    print("1: Chercher un aliment")
    print("2: Retrouver mes aliments substitués")
    print("3: Réinitialiser la base de données")
    choices = ["1", "2", "3"]
    choice = input("> ")

    if choice not in choices:
        main()
    else:
        if choice != choices[2]:
            app = Application(choice)
            app.run()
        else:
            print("Confirmez-vous la réinitialisation de la base de données? (O/N)")
            confirm = input("> ")

            if confirm == "o" or confirm == "O":
                db.recreate_db()


if __name__ == "__main__":
    main()
